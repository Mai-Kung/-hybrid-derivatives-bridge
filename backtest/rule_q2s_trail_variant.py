"""Test whether replacing Q2/S's fixed +30% TP with a trend-strength-gauge-inspired
trail-instead-of-exit rule (borrowed from the momentum-confluence-playbook's Setup A/B
"trim, don't cap the winner" lesson -- itself drawn from the MARSCOIN case where a fixed 30% TP
would have capped a +288% move) improves on the plain fixed-TP baseline already measured in
rule_q2s_backtest.py (+32.15% combined, PF 3.77).

The playbook's own indicators (step-line, trend-strength gauge) are chart-only and not present
in this screener data -- already established and not revisited here. What IS transferable and
mechanically computable from this data is the *behavior* the playbook is built on: once a trade
is working, don't take it off at one fixed level -- arm a trail once it's clearly in profit, and
only give back a bounded slice of the peak before exiting, so a MARSCOIN-sized move isn't capped
the way a flat +30% TP caps it. This script tests that concretely, with real numbers, rather than
asserting it works.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from data_loader import FULL_MAJORS_WHITELIST, load_altcoin_universe
from rule_q2s_backtest import (FEE_PER_LEG, SL_Q2, SL_S, TIME_STOP_H, build_features,
                                load_btc_24h, q2_pass, s_pass)

JUL = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/9bf11fd3-Mai_BI_20260701_20260731_Combined_FullMonth.xlsx"
AUG = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/5a900f03-Mai_BI_20260801_20260831_Combined_FullMonth_copy.xlsx"
COOLDOWN_H = 72.0


def simulate_symbol_trail(g: pd.DataFrame, arm: float, giveback: float) -> list[dict]:
    trades = []
    in_position = False
    side = entry_time = entry_price = None
    peak_ret = 0.0
    cooldown_until = None
    rows = g.to_dict("records")

    for row in rows:
        t = row["datetime"]
        if in_position:
            if side == "long":
                ret = row["price"] / entry_price - 1.0
            else:
                ret = 1.0 - row["price"] / entry_price
            peak_ret = max(peak_ret, ret)
            hit_sl = ret <= -(SL_Q2 if side == "long" else SL_S)
            armed = peak_ret >= arm
            hit_trail = armed and (peak_ret - ret) >= giveback
            elapsed_h = (t - entry_time).total_seconds() / 3600.0
            hit_time = elapsed_h >= TIME_STOP_H
            if hit_sl or hit_trail or hit_time:
                exit_ret = max(ret, -(SL_Q2 if side == "long" else SL_S)) if hit_sl else ret
                reason = "SL" if hit_sl else ("TRAIL" if hit_trail else "TIME")
                trades.append({"symbol": row["Symbol"], "side": side, "entry_time": entry_time,
                                "exit_time": t, "gross_ret": exit_ret, "exit_reason": reason,
                                "peak_ret": peak_ret, "hold_hours": elapsed_h})
                in_position = False
                cooldown_until = t + pd.Timedelta(hours=COOLDOWN_H)
            continue

        if cooldown_until is not None and t < cooldown_until:
            continue
        if pd.isna(row["chg_1m"]) or pd.isna(row["chg_1w"]) or pd.isna(row["btc24h"]):
            continue
        if q2_pass(row):
            in_position, side, entry_time, entry_price, peak_ret = True, "long", t, row["price"], 0.0
        elif s_pass(row):
            in_position, side, entry_time, entry_price, peak_ret = True, "short", t, row["price"], 0.0

    return trades


def run_variant(feats: pd.DataFrame, arm: float, giveback: float) -> tuple[pd.DataFrame, dict]:
    all_trades = []
    for sym, g in feats.groupby("Symbol", sort=False):
        all_trades.extend(simulate_symbol_trail(g.sort_values("datetime"), arm, giveback))
    trades = pd.DataFrame(all_trades)
    if len(trades) == 0:
        return trades, {"n": 0}
    net = (trades["gross_ret"] - FEE_PER_LEG) * (0.0050 / SL_Q2)
    net.index = trades["exit_time"]
    equity = (1 + net.sort_index()).cumprod()
    gains = net[net > 0].sum(); losses = -net[net < 0].sum()
    return trades, {
        "n": len(trades), "total_return_pct": (equity.iloc[-1] - 1) * 100,
        "PF": gains / losses if losses > 0 else np.inf,
        "maxDD_pct": (equity / equity.cummax() - 1).min() * 100,
        "win_rate_pct": (net > 0).mean() * 100,
    }


def main() -> None:
    full = load_altcoin_universe([JUL, AUG], majors=FULL_MAJORS_WHITELIST)
    feats = build_features(full)
    btc24 = load_btc_24h([JUL, AUG])
    feats["btc24h"] = feats["datetime"].map(btc24)

    print("Baseline (fixed +30% TP, from rule_q2s_backtest.py): total_return=32.15% PF=3.77 "
          "maxDD=-1.35% n=85\n")

    for arm, giveback in [(0.15, 0.08), (0.15, 0.12), (0.20, 0.10), (0.10, 0.06), (0.20, 0.15)]:
        trades, m = run_variant(feats, arm, giveback)
        print(f"arm={arm:.2f} giveback={giveback:.2f}: {m}")
        if len(trades):
            print("  exit reasons:", trades["exit_reason"].value_counts().to_dict())


if __name__ == "__main__":
    main()
