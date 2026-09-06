"""First-ever backtest of Rule Q2 (long) and Rule S (short) -- the mechanical trend-geometry
entry rules that v6.6/v7.2's own text claims were "tested across five to six major version
cycles" -- against the actual July+August 2026 screener data this repo has been using all along.

This has never been run in this repo before: every prior script here tested Rule F (fade the
30-minute pump) or Rule N (new-listing radar), not Q2/S themselves. Needed to honestly compare
"what does v6.6 actually produce" against v7.2 and the chart playbook.

Path-dependent per-symbol simulation: walk each symbol's snapshots in time order, open a
position when Q2 or S's entry geometry passes (and the symbol is flat / past its 72h cooldown),
close it on whichever of SL / TP / 72h time-stop is hit first, using price *at the snapshot*
(this data has no intrabar OHLC, so exits are snapshot-resolution -- the same accepted
limitation as every other script in this repo). Breadth is approximated as the fraction of the
alt universe with chg_24h > 0 at that same timestamp -- the skill text does not pin down its
exact computation, so this is a stated, reasonable proxy, not a verified match to the live tool.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from data_loader import FULL_MAJORS_WHITELIST, _read_one, load_altcoin_universe

JUL = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/9bf11fd3-Mai_BI_20260701_20260731_Combined_FullMonth.xlsx"
AUG = "/root/.claude/uploads/93cb574e-6efb-5564-a99e-ed13d35f4337/5a900f03-Mai_BI_20260801_20260831_Combined_FullMonth_copy.xlsx"

SL_Q2, TP_Q2 = 0.10, 0.30
SL_S, TP_S = 0.10, 0.30
TIME_STOP_H = 72.0
COOLDOWN_H = 72.0
FEE_PER_LEG = 0.0015  # v6.6 STEP 4: 0.15% round-trip on notional


def prior_signed_positive(dt: np.ndarray, val: np.ndarray, hours: float, want_positive: bool) -> np.ndarray:
    """For each row i, look back to the most recent row at least `hours` earlier and return
    whether its `val` was >0 (want_positive) or <0 (not want_positive). Requires dt sorted asc."""
    out = np.zeros(len(dt), dtype=bool)
    dt_i8 = dt.astype("datetime64[ns]").astype(np.int64)
    offset = int(pd.Timedelta(hours=hours).value)
    for i in range(len(dt)):
        target = dt_i8[i] - offset
        idx = np.searchsorted(dt_i8[:i], target, side="right") - 1
        if idx >= 0 and not np.isnan(val[idx]):
            out[i] = (val[idx] > 0) if want_positive else (val[idx] < 0)
    return out


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    d = df.sort_values(["Symbol", "datetime"]).copy()

    grp = d.groupby("Symbol", sort=False)
    d["vol_median_prev3"] = grp["volume_24h"].transform(lambda s: s.shift(1).rolling(3).median())
    d["vol_ratio"] = d["volume_24h"] / d["vol_median_prev3"]

    parts_q2, parts_s = [], []
    for sym, g in d.groupby("Symbol", sort=False):
        dt = g["datetime"].values
        w = g["chg_1w"].to_numpy(dtype=float)
        parts_q2.append(pd.Series(prior_signed_positive(dt, w, 2.0, True), index=g.index))
        parts_s.append(pd.Series(prior_signed_positive(dt, w, 2.0, False), index=g.index))
    d["prior_1w_pos"] = pd.concat(parts_q2).sort_index()
    d["prior_1w_neg"] = pd.concat(parts_s).sort_index()

    ltf = d[["chg_5m", "chg_15m", "chg_30m"]]
    d["mom_long_pass"] = np.where(d["degraded_confirm"], ltf.max(axis=1) >= 0.25, d["chg_30m"] >= 0.25)
    d["mom_short_pass"] = np.where(d["degraded_confirm"], ltf.min(axis=1) <= -0.50, d["chg_30m"] <= -0.50)

    breadth = d.groupby("datetime")["chg_24h"].apply(lambda s: (s > 0).mean())
    d["breadth"] = d["datetime"].map(breadth)

    return d


def load_btc_24h(paths: list[str]) -> pd.Series:
    frames = [_read_one(p) for p in paths]
    raw = pd.concat(frames, ignore_index=True)
    btc = raw[raw["Symbol"] == "BTCUSDT.P"].dropna(subset=["datetime"])
    btc = btc.drop_duplicates(subset=["datetime"]).set_index("datetime")["chg_24h"]
    return btc.sort_index()


def q2_pass(row) -> bool:
    return (
        40 <= row["chg_1m"] <= 100
        and 0 <= row["chg_1w"] <= 60
        and row["prior_1w_pos"]
        and row["magnitude"] < 8
        and -10 <= row["chg_open_1d"] <= 4
        and row["mom_long_pass"]
        and row["volume_24h"] >= 20_000_000
        and 0.5 <= row["vol_ratio"] <= 2.0
        and row["breadth"] >= 0.35
        and row["btc24h"] >= -0.5
    )


def s_pass(row) -> bool:
    return (
        -70 <= row["chg_1m"] <= -25
        and -60 <= row["chg_1w"] <= 0
        and row["prior_1w_neg"]
        and row["magnitude"] < 8
        and -4 <= row["chg_open_1d"] <= 10
        and row["mom_short_pass"]
        and row["volume_24h"] >= 20_000_000
        and 0.5 <= row["vol_ratio"] <= 2.0
        and row["btc24h"] < -0.5
    )


def simulate_symbol(g: pd.DataFrame) -> list[dict]:
    trades = []
    in_position = False
    side = entry_time = entry_price = None
    cooldown_until = None
    rows = g.to_dict("records")

    for row in rows:
        t = row["datetime"]
        if in_position:
            if side == "long":
                ret = row["price"] / entry_price - 1.0
                hit_sl, hit_tp = ret <= -SL_Q2, ret >= TP_Q2
                exit_ret = max(ret, -SL_Q2) if hit_sl else (min(ret, TP_Q2) if hit_tp else ret)
            else:
                ret = 1.0 - row["price"] / entry_price
                hit_sl, hit_tp = ret <= -SL_S, ret >= TP_S
                exit_ret = max(ret, -SL_S) if hit_sl else (min(ret, TP_S) if hit_tp else ret)
            elapsed_h = (t - entry_time).total_seconds() / 3600.0
            hit_time = elapsed_h >= TIME_STOP_H
            if hit_sl or hit_tp or hit_time:
                reason = "SL" if hit_sl else ("TP" if hit_tp else "TIME")
                trades.append({
                    "symbol": row["Symbol"], "side": side, "entry_time": entry_time,
                    "exit_time": t, "entry_price": entry_price, "exit_price": row["price"],
                    "gross_ret": exit_ret, "exit_reason": reason,
                    "hold_hours": elapsed_h,
                })
                in_position = False
                cooldown_until = t + pd.Timedelta(hours=COOLDOWN_H)
            continue

        if cooldown_until is not None and t < cooldown_until:
            continue
        if pd.isna(row["chg_1m"]) or pd.isna(row["chg_1w"]) or pd.isna(row["btc24h"]):
            continue
        if q2_pass(row):
            in_position, side, entry_time, entry_price = True, "long", t, row["price"]
        elif s_pass(row):
            in_position, side, entry_time, entry_price = True, "short", t, row["price"]

    return trades


def main() -> None:
    full = load_altcoin_universe([JUL, AUG], majors=FULL_MAJORS_WHITELIST)
    feats = build_features(full)
    btc24 = load_btc_24h([JUL, AUG])
    feats["btc24h"] = feats["datetime"].map(btc24)
    print(f"BTC 24h coverage: {feats['btc24h'].notna().mean()*100:.1f}% of rows matched")

    all_trades = []
    for sym, g in feats.groupby("Symbol", sort=False):
        all_trades.extend(simulate_symbol(g.sort_values("datetime")))

    trades = pd.DataFrame(all_trades)
    print(f"\nTotal Q2+S trades found: {len(trades)}")
    if len(trades) == 0:
        print("No trades passed the entry geometry on this data at all -- reporting zero, not "
              "fabricating a result.")
        return

    print(trades["side"].value_counts())
    trades.to_csv("results/rule_q2s_trades.csv", index=False)

    for label, sub in [("Q2 (long)", trades[trades["side"] == "long"]),
                        ("S (short)", trades[trades["side"] == "short"]),
                        ("Combined", trades)]:
        if len(sub) == 0:
            print(f"\n{label}: 0 trades")
            continue
        net = sub["gross_ret"] - FEE_PER_LEG
        risk_pct = 0.0050
        notional_frac = risk_pct / SL_Q2
        pos_ret = net * notional_frac
        equity = (1 + pos_ret.sort_index()).cumprod()
        gains = pos_ret[pos_ret > 0].sum()
        losses = -pos_ret[pos_ret < 0].sum()
        pf = gains / losses if losses > 0 else np.inf
        print(f"\n{label}: n={len(sub)} win_rate={(net>0).mean()*100:.1f}% "
              f"avg_gross_ret={sub['gross_ret'].mean()*100:.2f}% "
              f"realistic_total_return={ (equity.iloc[-1]-1)*100:.2f}% PF={pf:.2f} "
              f"maxDD={(equity/equity.cummax()-1).min()*100:.2f}%")
        print("  exit reasons:", sub["exit_reason"].value_counts().to_dict())


if __name__ == "__main__":
    main()
