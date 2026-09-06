"""Systematic backtest of Rule N (New-Listing / Futures-Catalyst Radar) across all available
snapshots, moving evidence from n=1 (MARSCOIN only) toward the STEP 6E admission-test bar.

N1 (an official exchange notice within 72h) cannot be checked mechanically from the CSV alone --
it needs a live search per candidate. This script flags every event as N1-UNVERIFIED by default;
a short list of the largest/most interesting candidates should be checked manually (as MARSCOIN
was) before treating any of them as VERIFIED-FRESH. Results here are N2-N6 only, mechanically.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from data_loader import DB_RED, load_altcoin_universe

JUL = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/fdf652a4-Mai_BI_20260701_20260731_Combined_FullMonth.xlsx"
AUG = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/0446091f-Mai_BI_20260801_20260831_Combined_FullMonth_copy.xlsx"
SEP2 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/afc33c65-Mai_BI_20260902_Combined.csv"
SEP3 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/3cf37395-Mai_BI_20260903_Combined.csv"
SEP5 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/d5308254-Mai_BI_20260905_Combined.csv"

N3_MIN_VOLUME = 50_000_000
N4_OPEN_LOW, N4_OPEN_HIGH = -10.0, 8.0


def passes_n2_n6(df: pd.DataFrame) -> pd.Series:
    n2 = df["chg_1w"].isna() | df["chg_1m"].isna()
    n3 = df["volume_24h"] >= N3_MIN_VOLUME
    n4 = df["chg_open_1d"].between(N4_OPEN_LOW, N4_OPEN_HIGH)

    ltf_max = df[["chg_5m", "chg_15m", "chg_30m"]].max(axis=1)
    ltf_pos_count = (df[["chg_5m", "chg_15m", "chg_30m"]] > 0).sum(axis=1)
    n5_normal = (ltf_pos_count >= 2) & (ltf_max >= 0.25)
    n5_degraded = ltf_max >= 0.25
    n5 = np.where(df["degraded_confirm"], n5_degraded, n5_normal)

    n6 = ~df["Symbol"].isin(DB_RED)

    return n2 & n3 & n4 & n5 & n6


def forward_snapshot(symbol_series: pd.DataFrame, alert_time: pd.Timestamp, hours: float):
    target = alert_time + pd.Timedelta(hours=hours)
    after = symbol_series[symbol_series["datetime"] >= alert_time]
    candidates = after[after["datetime"] <= target + pd.Timedelta(hours=hours / 2 + 1)]
    if candidates.empty:
        return None
    idx = (candidates["datetime"] - target).abs().idxmin()
    return candidates.loc[idx]


def main() -> None:
    df = load_altcoin_universe([JUL, AUG, SEP2, SEP3, SEP5], min_volume_usd=1_000_000)
    print(f"Universe: {df['Symbol'].nunique()} symbols, {df['datetime'].nunique()} timestamps, "
          f"{df['datetime'].min()} -> {df['datetime'].max()}")

    passing = df[passes_n2_n6(df)].copy()
    print(f"\nRows passing N2-N6 mechanically (any snapshot): {len(passing)}")

    # One "Listing Radar Alert" per symbol = its first passing timestamp.
    first_pass = passing.sort_values("datetime").drop_duplicates(subset=["Symbol"], keep="first")
    print(f"Distinct symbols with a first-pass alert: {len(first_pass)}")
    print(f"(STEP 6E requires >=20-30 logged events before Rule N can leave Watch/Shadow)")

    price_by_symbol = {sym: g[["datetime", "price"]].reset_index(drop=True)
                        for sym, g in df.groupby("Symbol")}

    rows = []
    for _, alert in first_pass.iterrows():
        sym = alert["Symbol"]
        series = price_by_symbol[sym]
        entry_price = alert["price"]
        entry_time = alert["datetime"]
        rec = {
            "symbol": sym, "alert_time": entry_time, "entry_price": entry_price,
            "volume_24h": alert["volume_24h"], "chg_open_1d": alert["chg_open_1d"],
            "chg_30m": alert["chg_30m"], "degraded_confirm": alert["degraded_confirm"],
        }
        window = series[(series["datetime"] > entry_time) &
                         (series["datetime"] <= entry_time + pd.Timedelta(hours=26))]
        if len(window) > 0:
            rec["mae_pct"] = (window["price"].min() / entry_price - 1) * 100
            rec["mfe_pct"] = (window["price"].max() / entry_price - 1) * 100
        for h in [2, 6, 24]:
            snap = forward_snapshot(series, entry_time, h)
            rec[f"ret_{h}h_pct"] = ((snap["price"] / entry_price - 1) * 100) if snap is not None else np.nan
        rows.append(rec)

    events = pd.DataFrame(rows).sort_values("alert_time").reset_index(drop=True)
    events.to_csv("results/rule_n_events.csv", index=False)

    print("\nAll logged Listing Radar events (N1 NOT verified -- mechanical N2-N6 only):")
    print(events[["symbol", "alert_time", "volume_24h", "chg_open_1d", "ret_2h_pct",
                   "ret_6h_pct", "ret_24h_pct", "mae_pct"]].to_string(index=False))

    for h in [2, 6, 24]:
        col = f"ret_{h}h_pct"
        valid = events[col].dropna()
        if len(valid) == 0:
            continue
        win_rate = (valid > 0).mean() * 100
        avg = valid.mean()
        gains = valid[valid > 0].sum()
        losses = -valid[valid < 0].sum()
        pf = gains / losses if losses > 0 else np.inf
        print(f"\n+{h}h: n={len(valid)} win_rate={win_rate:.1f}% avg_ret={avg:.2f}% "
              f"PF={pf:.2f}")

    print(f"\nMAE (worst drawdown 0-26h post-alert): mean={events['mae_pct'].mean():.2f}%, "
          f"worst={events['mae_pct'].min():.2f}%")
    print(f"MFE (best run-up 0-26h post-alert): mean={events['mfe_pct'].mean():.2f}%, "
          f"best={events['mfe_pct'].max():.2f}%")

    print(f"\nEvidence status vs STEP 6E bar: {len(events)} events logged "
          f"({'MEETS' if len(events) >= 20 else 'DOES NOT YET MEET'} the >=20-30 threshold). "
          "N1 (official catalyst) unverified for all but any manually cross-checked below.")


if __name__ == "__main__":
    main()
