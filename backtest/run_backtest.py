"""Grid-search the altcoin long/short screener strategy and validate walk-forward.

Usage:
    python run_backtest.py <july_file> <august_file> [--min-volume 1000000]

Splits data into July (in-sample, used to pick the strategy) and August
(out-of-sample, used to check it isn't overfit), then reports both plus the
full two-month combined result for the picked config.
"""
from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from data_loader import SIGNAL_COLS, load_altcoin_universe
from engine import StrategyConfig, estimate_periods_per_year, run_backtest

RESULTS_DIR = Path(__file__).parent / "results"

N_GRID = [5, 10, 15, 20, 30]
DIRECTIONS = ["momentum", "reversion"]
SIDES = ["long_short", "long_only", "short_only"]
MIN_PERIODS_FOR_RANKING = 20  # ignore configs with too few valid periods to be meaningful
MIN_N_FOR_ROBUST_PICK = 10  # N=5 baskets are noisy / easy to curve-fit on one month


def grid_search(df: pd.DataFrame, periods_per_year: float) -> pd.DataFrame:
    rows = []
    for signal, n, direction, side in itertools.product(SIGNAL_COLS, N_GRID, DIRECTIONS, SIDES):
        cfg = StrategyConfig(signal=signal, n=n, direction=direction, side=side)
        _, m = run_backtest(df, cfg, periods_per_year)
        rows.append(m)
    return pd.DataFrame(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("july_file")
    ap.add_argument("august_file")
    ap.add_argument("--min-volume", type=float, default=1_000_000)
    args = ap.parse_args()

    RESULTS_DIR.mkdir(exist_ok=True)

    full = load_altcoin_universe([args.july_file, args.august_file], min_volume_usd=args.min_volume)
    july = full[full["datetime"] < "2026-08-01"].reset_index(drop=True)
    august = full[full["datetime"] >= "2026-08-01"].reset_index(drop=True)

    ppy_full = estimate_periods_per_year(full)
    ppy_july = estimate_periods_per_year(july)
    ppy_aug = estimate_periods_per_year(august)

    print(f"Full universe: {full['Symbol'].nunique()} alt perpetuals, "
          f"{full['datetime'].nunique()} scan timestamps, "
          f"{full['datetime'].min()} -> {full['datetime'].max()}")

    print("\nRunning grid search on JULY (in-sample)...")
    gs_july = grid_search(july, ppy_july)
    gs_july = gs_july[gs_july["n_periods"] >= MIN_PERIODS_FOR_RANKING]
    gs_july = gs_july.sort_values("sharpe", ascending=False)
    gs_july.to_csv(RESULTS_DIR / "grid_search_july.csv", index=False)

    print("Running grid search on AUGUST (for reference / comparison)...")
    gs_aug = grid_search(august, ppy_aug)
    gs_aug = gs_aug[gs_aug["n_periods"] >= MIN_PERIODS_FOR_RANKING]
    gs_aug = gs_aug.sort_values("sharpe", ascending=False)
    gs_aug.to_csv(RESULTS_DIR / "grid_search_august.csv", index=False)

    print("\nTop 10 configs by July in-sample Sharpe (naive pick -- watch for overfitting):")
    print(gs_july.head(10).to_string(index=False))

    # --- Naive pick: best July Sharpe, no robustness check. Kept to demonstrate
    # how badly a single-month optimum can overfit before we do it properly.
    naive_best = gs_july.iloc[0]
    naive_cfg = StrategyConfig(signal=naive_best["signal"], n=int(naive_best["n"]),
                                direction=naive_best["direction"], side=naive_best["side"])
    _, m_naive_july = run_backtest(july, naive_cfg, ppy_july)
    ret_naive_aug, m_naive_aug = run_backtest(august, naive_cfg, ppy_aug)
    naive_summary = pd.DataFrame([
        {"period": "July (in-sample)", **m_naive_july},
        {"period": "August (out-of-sample)", **m_naive_aug},
    ])
    print(f"\nNaive July-optimal config: signal={naive_cfg.signal} n={naive_cfg.n} "
          f"direction={naive_cfg.direction} side={naive_cfg.side}")
    print(naive_summary.to_string(index=False))
    naive_summary.to_csv(RESULTS_DIR / "naive_overfit_example.csv", index=False)

    # --- Robust pick: merge July & August grid searches, require the config to
    # hold up in BOTH months (score = min of the two Sharpes), and require
    # N >= MIN_N_FOR_ROBUST_PICK so the basket isn't a handful of noisy names.
    merged = gs_july.merge(gs_aug, on=["signal", "n", "direction", "side"], suffixes=("_jul", "_aug"))
    merged = merged[merged["n"] >= MIN_N_FOR_ROBUST_PICK]
    merged["combo_sharpe"] = merged[["sharpe_jul", "sharpe_aug"]].min(axis=1)
    merged = merged.sort_values("combo_sharpe", ascending=False)
    merged.to_csv(RESULTS_DIR / "robust_candidates.csv", index=False)

    print(f"\nTop 10 robust candidates (min of July & August Sharpe, N>={MIN_N_FOR_ROBUST_PICK}):")
    show_cols = ["signal", "n", "direction", "side", "sharpe_jul", "sharpe_aug", "combo_sharpe",
                 "total_return_pct_jul", "total_return_pct_aug"]
    print(merged[show_cols].head(10).to_string(index=False))

    robust_best = merged.iloc[0]
    picked_cfg = StrategyConfig(signal=robust_best["signal"], n=int(robust_best["n"]),
                                 direction=robust_best["direction"], side=robust_best["side"])

    ret_july, m_july = run_backtest(july, picked_cfg, ppy_july)
    ret_aug, m_aug = run_backtest(august, picked_cfg, ppy_aug)
    ret_full, m_full = run_backtest(full, picked_cfg, ppy_full)

    summary = pd.DataFrame([
        {"period": "July (in-sample)", **m_july},
        {"period": "August (out-of-sample)", **m_aug},
        {"period": "Full (Jul+Aug)", **m_full},
    ])
    summary.to_csv(RESULTS_DIR / "picked_strategy_summary.csv", index=False)
    print(f"\nRobust picked strategy: signal={picked_cfg.signal} n={picked_cfg.n} "
          f"direction={picked_cfg.direction} side={picked_cfg.side}")
    print(summary.to_string(index=False))

    # Cost sensitivity: how much does the edge survive under harsher slippage assumptions?
    cost_rows = []
    for cost_bps in [5, 10, 20, 30, 50]:
        c = StrategyConfig(signal=picked_cfg.signal, n=picked_cfg.n, direction=picked_cfg.direction,
                            side=picked_cfg.side, cost_bps_per_leg=cost_bps)
        _, m = run_backtest(full, c, ppy_full)
        cost_rows.append({"cost_bps_per_leg": cost_bps, **m})
    cost_df = pd.DataFrame(cost_rows)
    cost_df.to_csv(RESULTS_DIR / "cost_sensitivity.csv", index=False)
    print("\nCost sensitivity (full period, robust config):")
    print(cost_df[["cost_bps_per_leg", "total_return_pct", "sharpe", "max_drawdown_pct"]].to_string(index=False))

    # Equity curve chart: robust pick vs the naive overfit example, full period.
    equity_full = (1.0 + ret_full).cumprod()
    equity_naive_aug = (1.0 + ret_naive_aug).cumprod()
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=False)

    ax = axes[0]
    ax.plot(equity_full.index, equity_full.values, color="#2563eb", linewidth=1.5)
    split_ts = pd.Timestamp("2026-08-01")
    if split_ts >= equity_full.index.min() and split_ts <= equity_full.index.max():
        ax.axvline(split_ts, color="#94a3b8", linestyle="--", linewidth=1)
        ax.text(split_ts, ax.get_ylim()[1], " Aug (OOS) starts", va="top", fontsize=8, color="#64748b")
    ax.set_title(f"Robust pick: {picked_cfg.signal} / N={picked_cfg.n} / "
                 f"{picked_cfg.direction} / {picked_cfg.side} (Jul+Aug)")
    ax.set_ylabel("Equity (start = 1.0)")
    ax.grid(alpha=0.3)

    ax2 = axes[1]
    ax2.plot(equity_naive_aug.index, equity_naive_aug.values, color="#dc2626", linewidth=1.5)
    ax2.set_title(f"Naive July-optimal pick on August (OOS): {naive_cfg.signal} / N={naive_cfg.n} / "
                  f"{naive_cfg.direction} / {naive_cfg.side} -- overfitting blows up")
    ax2.set_ylabel("Equity (start = 1.0)")
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(RESULTS_DIR / "equity_curve.png", dpi=150)
    print(f"\nSaved: {RESULTS_DIR / 'equity_curve.png'}")

    ret_full.rename("period_return").to_csv(RESULTS_DIR / "picked_strategy_returns.csv")

    # Weekly stability check: is the edge broad-based or one lucky week carrying it?
    weekly = ret_full.groupby(pd.Grouper(freq="W")).apply(lambda r: (1 + r).prod() - 1)
    weekly.rename("weekly_return").to_csv(RESULTS_DIR / "weekly_returns.csv")
    print(f"\nWeekly returns ({(weekly > 0).sum()}/{len(weekly)} weeks positive):")
    print(weekly.to_string())

    # Liquidity-threshold sensitivity: does the edge survive on a more liquid subset?
    liq_rows = []
    for min_vol in [1_000_000, 5_000_000, 20_000_000, 50_000_000]:
        df_liq = load_altcoin_universe([args.july_file, args.august_file], min_volume_usd=min_vol)
        ppy_liq = estimate_periods_per_year(df_liq)
        _, m = run_backtest(df_liq, picked_cfg, ppy_liq)
        liq_rows.append({"min_volume_usd": min_vol, "n_symbols": df_liq["Symbol"].nunique(), **m})
    liq_df = pd.DataFrame(liq_rows)
    liq_df.to_csv(RESULTS_DIR / "liquidity_sensitivity.csv", index=False)
    print("\nLiquidity-threshold sensitivity (robust config):")
    print(liq_df[["min_volume_usd", "n_symbols", "total_return_pct", "sharpe", "max_drawdown_pct"]]
          .to_string(index=False))


if __name__ == "__main__":
    main()
