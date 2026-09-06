"""Design a single-trade stop-loss / position-sizing scheme for Rule F (Fade-the-Pump).

This is research toward the Hybrid AI Trading Process v7.0 STEP 6F admission test, which
requires "a specific stop-loss / take-profit / position-sizing scheme proposed AND back-tested
at the SINGLE-TRADE level (not basket-average)". It does NOT clear that gate on its own -- see
the caveats printed at the end. Rule F remains WATCH-ONLY / PILOT-CANDIDATE regardless of this
script's output; it proposes numbers for review, it does not authorize a trade.

Key limitation, stated up front: the source data is scan-snapshot resolution (median gap ~3h),
not a continuous price path. A stop-loss level is simulated by capping each trade's realized
loss at the stop -- this is a PROXY, not a true intra-period fill simulation. It likely
UNDERSTATES how often a stop would trigger (a trade could spike far past the stop intra-period
and revert to a smaller loss by the next scan, which this data cannot see), so the protection
estimated here is optimistic, not conservative.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

COST = 0.0005  # 5bps, matches the original backtest assumption


def load_trades(path: str) -> pd.DataFrame:
    t = pd.read_csv(path, parse_dates=["entry_time", "exit_time"])
    t["rank"] = t.groupby("entry_time")["signal_value"].rank(ascending=False, method="first")
    return t


def clamp_stop(gross_ret: pd.Series, stop_loss: float | None) -> pd.Series:
    """Cap the loss at `stop_loss`. `None` still floors at -100% (total loss of the margin
    allocated to that trade -- what a real exchange's liquidation engine would do even with
    no explicit stop order), so "no stop" here means "no risk-management stop", not "no
    real-world floor at all" -- a -111.8% price move cannot literally cost more than the
    capital put up.
    """
    floor = -1.0 if stop_loss is None else -stop_loss
    return gross_ret.clip(lower=floor)


def clamp_tp(gross_ret: pd.Series, take_profit: float | None) -> pd.Series:
    if take_profit is None:
        return gross_ret
    return gross_ret.clip(upper=take_profit)


def sequential_metrics(gross_ret: pd.Series, entry_times: pd.Series, notional_frac: float = 1.0) -> dict:
    """notional_frac: fraction of equity actually risked at the instrument's raw return.

    1.0 = naive "all account compounds at the instrument's own %" (unrealistic -- explodes).
    risk_pct/stop_pct = the realistic account-level return per trade under position sizing
    that risks a fixed % of equity per trade, sized by distance to the stop.
    """
    net_ret = (gross_ret - COST) * notional_frac
    equity = (1.0 + net_ret).cumprod()
    total_return = equity.iloc[-1] - 1.0
    span_days = (entry_times.max() - entry_times.min()).total_seconds() / 86400.0
    ppy = len(net_ret) / span_days * 365.25 if span_days > 0 else np.nan
    vol = net_ret.std(ddof=1)
    sharpe = (net_ret.mean() / vol) * np.sqrt(ppy) if vol > 0 else np.nan
    dd = (equity / equity.cummax() - 1.0).min()
    win_rate = (net_ret > 0).mean()
    gains = net_ret[net_ret > 0].sum()
    losses = -net_ret[net_ret < 0].sum()
    pf = gains / losses if losses > 0 else np.inf
    return {
        "n_trades": len(net_ret),
        "total_return_pct": total_return * 100,
        "sharpe": sharpe,
        "max_drawdown_pct": dd * 100,
        "win_rate_pct": win_rate * 100,
        "profit_factor": pf,
        "worst_trade_pct": net_ret.min() * 100,
        "avg_trade_bps": net_ret.mean() * 10_000,
    }


def best_week_sensitivity(net_ret: pd.Series, entry_times: pd.Series) -> dict:
    df = pd.DataFrame({"net_ret": net_ret.values, "entry_time": entry_times.values})
    weekly = df.groupby(pd.Grouper(key="entry_time", freq="W"))["net_ret"].apply(
        lambda r: (1 + r).prod() - 1
    )
    best_week_ret = weekly.max()
    total_with = (1 + df["net_ret"]).prod() - 1
    best_week_start = weekly.idxmax()
    mask_best_week = (df["entry_time"] >= best_week_start - pd.Timedelta(days=7)) & (
        df["entry_time"] < best_week_start
    )
    total_without = (1 + df.loc[~mask_best_week, "net_ret"]).prod() - 1
    return {"best_week_pct": best_week_ret * 100, "total_with_pct": total_with * 100,
            "total_without_best_week_pct": total_without * 100}


def main() -> None:
    trades = load_trades("results/trade_log.csv")
    rank1 = trades[trades["rank"] == 1].sort_values("entry_time").reset_index(drop=True)
    print(f"Rank-1 (single-trade discretionary proxy) sample: {len(rank1)} sequential trades, "
          f"{rank1['entry_time'].min()} -> {rank1['entry_time'].max()}\n")

    print("Full top-10 basket sample (for tail-risk context only, not a sequential equity curve):")
    full_desc = trades["gross_ret"].describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99])
    print(full_desc.to_string())
    print(f"Worst single trade (any rank): {trades['gross_ret'].min()*100:.1f}%")
    print(f"Worst single trade (rank-1 only): {rank1['gross_ret'].min()*100:.1f}%\n")

    # Step 1: instrument-level (100% notional, no sizing) -- shows why a stop is non-negotiable,
    # NOT a usable account plan. Without a stop, tail risk is unbounded (the -111.8% trade).
    stop_grid = [None, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]
    rows = []
    for stop in stop_grid:
        clamped = clamp_stop(rank1["gross_ret"], stop)
        m = sequential_metrics(clamped, rank1["entry_time"], notional_frac=1.0)
        m["stop_loss_pct"] = "none" if stop is None else stop * 100
        rows.append(m)
    grid_df = pd.DataFrame(rows)[["stop_loss_pct", "n_trades", "total_return_pct", "sharpe",
                                   "max_drawdown_pct", "win_rate_pct", "profit_factor",
                                   "worst_trade_pct", "avg_trade_bps"]]
    print("STEP 1 -- instrument-level (100% notional every trade -- NOT a real sizing plan,\n"
          "shown only to compare the shape of PF/Sharpe/tail across stop levels):")
    print(grid_df.to_string(index=False))
    grid_df.to_csv("results/rule_f_stop_loss_grid.csv", index=False)

    passing = grid_df[grid_df["profit_factor"] > 1.50]
    print(f"\nConfigs clearing PF > 1.50 (the §6F bar): {len(passing)} of {len(grid_df)}")
    print(passing[["stop_loss_pct", "profit_factor", "sharpe"]].to_string(index=False))

    # Step 2: realistic ACCOUNT-level returns under actual position sizing -- risk_pct of
    # equity per trade, position sized by distance to the stop (notional_frac = risk/stop).
    # This is the number that matters for "what would this be worth in real money".
    print("\n" + "=" * 78)
    print("STEP 2 -- ACCOUNT-level results under real position sizing (risk% / stop% sizing)")
    print("=" * 78)
    account_rows = []
    for stop_pct in [10, 15, 20, 25, 30]:
        stop = stop_pct / 100.0
        clamped = clamp_stop(rank1["gross_ret"], stop)
        for risk_pct in [0.25, 0.50, 1.00]:
            notional_frac = (risk_pct / 100.0) / stop
            m = sequential_metrics(clamped, rank1["entry_time"], notional_frac=notional_frac)
            m.update({"stop_loss_pct": stop_pct, "risk_pct_per_trade": risk_pct,
                      "notional_pct_of_equity": notional_frac * 100})
            account_rows.append(m)
    account_df = pd.DataFrame(account_rows)[
        ["stop_loss_pct", "risk_pct_per_trade", "notional_pct_of_equity", "total_return_pct",
         "sharpe", "max_drawdown_pct", "profit_factor", "worst_trade_pct"]
    ]
    print(account_df.to_string(index=False))
    account_df.to_csv("results/rule_f_account_level_sizing.csv", index=False)

    print("\nBest-week sensitivity (risk=0.50% of equity per trade, account-level):")
    for stop_pct in [15, 20, 25]:
        stop = stop_pct / 100.0
        notional_frac = 0.005 / stop
        clamped = clamp_stop(rank1["gross_ret"], stop)
        net = (clamped - COST) * notional_frac
        bw = best_week_sensitivity(net, rank1["entry_time"])
        print(f"  stop={stop_pct}%: best week {bw['best_week_pct']:.2f}%, "
              f"total WITH it {bw['total_with_pct']:.2f}%, "
              f"total WITHOUT it {bw['total_without_best_week_pct']:.2f}%")


if __name__ == "__main__":
    main()
