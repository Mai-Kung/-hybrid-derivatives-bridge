"""Export the fill-by-fill trade log for the picked strategy (chg_30m / N=10 /
reversion / short_only) to CSV, for building the Excel trade log workbook.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from data_loader import load_altcoin_universe
from engine import StrategyConfig, get_trades

RESULTS_DIR = Path(__file__).parent / "results"

PICKED_CFG = StrategyConfig(signal="chg_30m", n=10, direction="reversion", side="short_only")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("july_file")
    ap.add_argument("august_file")
    ap.add_argument("--min-volume", type=float, default=1_000_000)
    args = ap.parse_args()

    df = load_altcoin_universe([args.july_file, args.august_file], min_volume_usd=args.min_volume)
    trades = get_trades(df, PICKED_CFG)
    trades.to_csv(RESULTS_DIR / "trade_log.csv", index=False)
    print(f"{len(trades)} trades across {trades['entry_time'].nunique()} periods")
    print(trades.head(15).to_string(index=False))


if __name__ == "__main__":
    main()
