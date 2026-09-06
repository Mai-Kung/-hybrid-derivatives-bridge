"""Deep-dive Rule F analysis for v7.1: full Majors Whitelist, Sept extension, LV-Guard A/B,
and profit-improvement variants. Research only -- does not change Rule F's WATCH-ONLY status.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from data_loader import FULL_MAJORS_WHITELIST, MAJORS, load_altcoin_universe
from engine import StrategyConfig, estimate_periods_per_year, get_trades, run_backtest

JUL = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/fdf652a4-Mai_BI_20260701_20260731_Combined_FullMonth.xlsx"
AUG = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/0446091f-Mai_BI_20260801_20260831_Combined_FullMonth_copy.xlsx"
SEP2 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/afc33c65-Mai_BI_20260902_Combined.csv"
SEP3 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/3cf37395-Mai_BI_20260903_Combined.csv"
SEP5 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/d5308254-Mai_BI_20260905_Combined.csv"

CFG = StrategyConfig(signal="chg_30m", n=10, direction="reversion", side="short_only")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def report_backtest(df: pd.DataFrame, label: str, cfg: StrategyConfig = CFG) -> dict:
    if df["datetime"].nunique() < 2:
        print(f"{label}: too few timestamps, skipped")
        return {}
    ppy = estimate_periods_per_year(df)
    _, m = run_backtest(df, cfg, ppy)
    print(f"{label}: n_periods={m.get('n_periods')} total_return={m.get('total_return_pct', float('nan')):.1f}% "
          f"sharpe={m.get('sharpe', float('nan')):.2f} maxdd={m.get('max_drawdown_pct', float('nan')):.1f}% "
          f"winrate={m.get('win_rate_pct', float('nan')):.1f}%")
    return m


def main() -> None:
    section("STEP A -- reload with FULL Majors Whitelist (was BTC/ETH-only)")
    full_btceth = load_altcoin_universe([JUL, AUG], majors=MAJORS)
    full_whitelist = load_altcoin_universe([JUL, AUG], majors=FULL_MAJORS_WHITELIST)
    print(f"BTC/ETH-only excl: {full_btceth['Symbol'].nunique()} symbols")
    print(f"Full whitelist excl: {full_whitelist['Symbol'].nunique()} symbols "
          f"({full_btceth['Symbol'].nunique() - full_whitelist['Symbol'].nunique()} removed)")

    jul_fw = full_whitelist[full_whitelist["datetime"] < "2026-08-01"]
    aug_fw = full_whitelist[full_whitelist["datetime"] >= "2026-08-01"]

    print("\nReproduction check (BTC/ETH-only excl, should match prior report):")
    report_backtest(full_btceth, "  Full Jul+Aug, BTC/ETH-only")

    print("\nCorrected universe (full Majors Whitelist excluded):")
    report_backtest(jul_fw, "  July (in-sample)")
    report_backtest(aug_fw, "  August (out-of-sample)")
    report_backtest(full_whitelist, "  Full Jul+Aug")

    section("STEP B -- add September (2,3,5) as a third, mini out-of-sample slice")
    all_full = load_altcoin_universe([JUL, AUG, SEP2, SEP3, SEP5], majors=FULL_MAJORS_WHITELIST)
    sep_fw = all_full[all_full["datetime"] >= "2026-09-01"]
    print(f"September slice: {sep_fw['datetime'].nunique()} timestamps, "
          f"{sep_fw['datetime'].min()} -> {sep_fw['datetime'].max()} "
          "(note: 2026-09-04 is missing -- a 1-day gap between the 09-03 and 09-05 files)")
    report_backtest(sep_fw, "  September (tiny OOS slice)")
    report_backtest(all_full, "  Full Jul+Aug+Sep, full whitelist")

    section("STEP C -- LV-Guard (F4) A/B test, single-trade discretionary mode")
    trades_all = get_trades(all_full, CFG)
    trades_all["rank"] = trades_all.groupby("entry_time")["signal_value"].rank(
        ascending=False, method="first"
    )
    # Re-derive magnitude per trade from the source frame (entry_time+symbol -> magnitude)
    mag_lookup = all_full.set_index(["Symbol", "datetime"])["magnitude"]
    trades_all["magnitude"] = trades_all.set_index(["symbol", "entry_time"]).index.map(mag_lookup)

    def rank1_from(pool: pd.DataFrame) -> pd.DataFrame:
        p = pool.copy()
        p["rank"] = p.groupby("entry_time")["signal_value"].rank(ascending=False, method="first")
        return p[p["rank"] == 1].sort_values("entry_time").reset_index(drop=True)

    variant_a = rank1_from(trades_all)  # current v7.0 design: no magnitude filter
    variant_b = rank1_from(trades_all[trades_all["magnitude"] < 25])  # LV-Guard applied

    def single_trade_stats(df: pd.DataFrame, stop: float = 0.15, risk_pct: float = 0.50) -> dict:
        notional_frac = (risk_pct / 100.0) / stop
        gross = df["gross_ret"].clip(lower=-stop)
        net = (gross - 0.0005) * notional_frac
        equity = (1 + net).cumprod()
        gains = net[net > 0].sum()
        losses = -net[net < 0].sum()
        return {
            "n_trades": len(df),
            "total_return_pct": (equity.iloc[-1] - 1) * 100,
            "max_drawdown_pct": (equity / equity.cummax() - 1).min() * 100,
            "win_rate_pct": (net > 0).mean() * 100,
            "profit_factor": gains / losses if losses > 0 else np.inf,
            "worst_trade_pct": df["gross_ret"].min() * 100,
        }

    print(f"Variant A (no LV-Guard, current F4 design): n={len(variant_a)}")
    print(" ", single_trade_stats(variant_a))
    print(f"Variant B (LV-Guard Auto-Skip applied, magnitude<25 only): n={len(variant_b)}")
    print(" ", single_trade_stats(variant_b))

    section("STEP D -- what was the worst trade, exactly?")
    worst = trades_all.sort_values("gross_ret").head(5)
    print(worst[["entry_time", "symbol", "signal_value", "magnitude", "entry_price", "exit_price",
                 "gross_ret"]].to_string(index=False))

    section("STEP E -- profit-improvement variants (full whitelist, Jul+Aug+Sep)")
    variants = {
        "baseline (N=10)": all_full,
    }
    for n in [15, 20]:
        cfg = StrategyConfig(signal="chg_30m", n=n, direction="reversion", side="short_only")
        report_backtest(all_full, f"  N={n}", cfg)

    print("\nExclude extreme signal outliers (chg_30m > 50% treated as data/flash-crash artifact):")
    capped = all_full[all_full["chg_30m"] <= 50].copy()
    # Recompute fwd_ret validity isn't affected (we only filter the ranking pool via signal itself,
    # but engine ranks on the full frame passed in -- so filtering rows here removes them from
    # BOTH the ranking pool and as potential winners/losers, which is what we want to test).
    report_backtest(capped, "  chg_30m capped at 50%")

    print("\nExclude sub-cent, most-illiquid-feeling prices (price < $0.001):")
    price_filtered = all_full[all_full["price"] >= 0.001].copy()
    report_backtest(price_filtered, "  price >= $0.001")


if __name__ == "__main__":
    main()
