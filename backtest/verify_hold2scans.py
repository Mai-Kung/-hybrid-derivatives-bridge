"""Independently verify the external "v7.1" document's claim that holding the Rule F basket
for 2 scans (non-overlapping) produces +2,659% (July) / +810% (August) basket research returns,
vs +615%/+272% for the 1-scan version. Those numbers look like a compounding artifact (the same
trap flagged in rule_f_risk_design.py's "STEP 1 -- NOT a real sizing plan" section): compounding
a K-scan forward return at every single scan (i.e. overlapping baskets) roughly squares the
apparent edge instead of just capturing it once per real holding period.

This script builds the K-scan variant correctly (non-overlapping: rebalance only every Kth
global scan) and reports what the basket-level return actually is under both interpretations.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from data_loader import FULL_MAJORS_WHITELIST, load_altcoin_universe

JUL = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/fdf652a4-Mai_BI_20260701_20260731_Combined_FullMonth.xlsx"
AUG = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/0446091f-Mai_BI_20260801_20260831_Combined_FullMonth_copy.xlsx"
SEP2 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/afc33c65-Mai_BI_20260902_Combined.csv"
SEP3 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/3cf37395-Mai_BI_20260903_Combined.csv"
SEP5 = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/d5308254-Mai_BI_20260905_Combined.csv"

N = 10
COST_PER_LEG = 0.0010  # the external doc's own stated 0.10% round-trip assumption
MAX_GAP_PER_SCAN_H = 8.0


def build_k_scan_frame(df: pd.DataFrame, k: int) -> pd.DataFrame:
    """Forward return over k subsequent snapshots per symbol (not just the next one)."""
    d = df.sort_values(["Symbol", "datetime"]).copy()
    grp = d.groupby("Symbol", sort=False)
    d[f"price_fwd{k}"] = grp["price"].shift(-k)
    d[f"dt_fwd{k}"] = grp["datetime"].shift(-k)
    d[f"gap{k}_hours"] = (d[f"dt_fwd{k}"] - d["datetime"]).dt.total_seconds() / 3600.0
    d[f"fwd_ret{k}"] = d[f"price_fwd{k}"] / d["price"] - 1.0
    return d


def basket_return_per_period(d: pd.DataFrame, k: int, cost_per_leg: float) -> pd.Series:
    valid = d[(d[f"gap{k}_hours"] <= MAX_GAP_PER_SCAN_H * k) & d[f"fwd_ret{k}"].notna()
              & d["chg_30m"].notna()]

    def per_period(g: pd.DataFrame):
        if len(g) < N:
            return None
        top = g.sort_values("chg_30m").iloc[-N:]
        short_ret = -top[f"fwd_ret{k}"].mean() - cost_per_leg
        return short_ret

    return valid.groupby("datetime", sort=True).apply(per_period, include_groups=False).dropna()


def compound_overlapping(returns_by_time: pd.Series) -> float:
    """WRONG method: compound the K-scan return at every single scan (overlapping baskets,
    as if you had K independent copies of capital running staggered -- the likely bug)."""
    return (1 + returns_by_time).prod() - 1


def compound_nonoverlapping(returns_by_time: pd.Series, k: int) -> float:
    """CORRECT method for 'one basket at a time, do not stack': only take every Kth
    rebalance point (chronologically), so positions never overlap."""
    times = returns_by_time.index
    picked = times[::k]
    return (1 + returns_by_time.loc[picked]).prod() - 1, len(picked)


def main() -> None:
    full = load_altcoin_universe([JUL, AUG], majors=FULL_MAJORS_WHITELIST)
    jul = full[full["datetime"] < "2026-08-01"]
    aug = full[full["datetime"] >= "2026-08-01"]

    for label, seg in [("July", jul), ("August", aug)]:
        print(f"\n=== {label} ===")
        for k in [1, 2]:
            d = build_k_scan_frame(seg, k)
            rets = basket_return_per_period(d, k, COST_PER_LEG)
            overlapping_total = compound_overlapping(rets)
            nonoverlap_total, n_used = compound_nonoverlapping(rets, k)
            gains = rets[rets > 0].sum()
            losses = -rets[rets < 0].sum()
            pf = gains / losses if losses > 0 else np.inf
            print(f"  k={k} scan hold: {len(rets)} raw rebalance points, PF(all pts)={pf:.2f}")
            print(f"    if compounded at EVERY scan (overlapping, likely the doc's method): "
                  f"{overlapping_total*100:,.1f}%")
            print(f"    if compounded only every {k} scans (non-overlapping, matches the doc's "
                  f"own 'one basket at a time' rule): {nonoverlap_total*100:,.1f}% "
                  f"over {n_used} actual baskets")


if __name__ == "__main__":
    main()
