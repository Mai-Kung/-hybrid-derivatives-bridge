"""Load and clean the Binance-perp altcoin screener export (TradingView BI dumps).

Each row is one symbol's snapshot at one scan timestamp. Scans happen a few
times a day at irregular intervals (not fixed-interval OHLCV bars), so this
loader treats every unique timestamp as one cross-sectional "rebalance point".
"""
from __future__ import annotations

import pandas as pd

RAW_COLUMNS = {
    "Change from open %, 1 day": "chg_open_1d",
    "Price change %, 5 minutes": "chg_5m",
    "Price change %, 15 minutes": "chg_15m",
    "Price change %, 30 minutes": "chg_30m",
    "Price change %, 1 week": "chg_1w",
    "Price change %, 1 month": "chg_1m",
    "Price change %, 24 hours": "chg_24h",
    "Price": "price",
    "Volume in USD, 24 hours": "volume_24h",
}

MAJORS = {"BTCUSDT.P", "ETHUSDT.P"}

SIGNAL_COLS = ["chg_5m", "chg_15m", "chg_30m", "chg_open_1d", "chg_24h", "chg_1w", "chg_1m"]


def _read_one(path: str) -> pd.DataFrame:
    if path.lower().endswith(".csv"):
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)
    df = df.rename(columns=RAW_COLUMNS)
    df["Date"] = pd.to_datetime(df["Date"])
    # Time comes as "HH:MM" strings from CSV, datetime.time objects from Excel.
    time_str = df["Time"].astype(str)
    df["datetime"] = pd.to_datetime(
        df["Date"].dt.strftime("%Y-%m-%d") + " " + time_str, errors="coerce"
    )
    return df


def load_altcoin_universe(paths: list[str], min_volume_usd: float = 1_000_000) -> pd.DataFrame:
    """Combine the exports, keep alt perpetuals only, dedupe, and sort.

    Excludes BTCUSDT.P / ETHUSDT.P (majors, not "altcoins") and any symbol
    below `min_volume_usd` 24h volume (illiquid names -> unreliable fills).
    """
    frames = [_read_one(p) for p in paths]
    df = pd.concat(frames, ignore_index=True)

    df = df[df["Symbol"].str.endswith("USDT.P") & ~df["Symbol"].isin(MAJORS)].copy()
    df = df.drop_duplicates(subset=["Symbol", "datetime"])
    df = df.dropna(subset=["datetime", "price"])
    df = df[df["volume_24h"] >= min_volume_usd]

    df = df.sort_values(["Symbol", "datetime"]).reset_index(drop=True)

    # Forward return to the symbol's *next* snapshot, plus the hours until it,
    # so the engine can drop stale/too-far-apart pairs (delistings, data gaps).
    grp = df.groupby("Symbol", sort=False)
    df["next_price"] = grp["price"].shift(-1)
    df["next_dt"] = grp["datetime"].shift(-1)
    df["gap_hours"] = (df["next_dt"] - df["datetime"]).dt.total_seconds() / 3600.0
    df["fwd_ret"] = df["next_price"] / df["price"] - 1.0

    return df.reset_index(drop=True)


if __name__ == "__main__":
    import sys

    df = load_altcoin_universe(sys.argv[1:])
    print(df.shape)
    print(df["datetime"].min(), "->", df["datetime"].max())
    print(df["Symbol"].nunique(), "symbols")
    print(df[["chg_open_1d", "fwd_ret", "gap_hours"]].describe())
