# Altcoin perpetual long/short backtest

Backtests a cross-sectional long/short strategy on Binance USDT-margined
altcoin perpetuals, using periodic market-screener snapshots (TradingView BI
export: `Mai_BI_*_Combined_FullMonth.{csv,xlsx}`) rather than continuous
OHLCV bars. Each snapshot lists ~700 alt perpetuals with their price and
momentum stats (5m/15m/30m/24h/1w/1m % change, intraday change from open,
24h volume) a few times a day.

## How the backtest works

- **Universe**: every `*USDT.P` perpetual except `BTCUSDT.P` / `ETHUSDT.P`
  (majors, not "alts"), filtered to 24h volume >= $1M to avoid illiquid names.
- **Rebalance point**: every unique scan timestamp. At each one, rank the
  universe by one momentum signal, go long the top N and short the bottom N
  (or the reverse, for a mean-reversion variant), hold until each symbol's
  next snapshot (capped at an 8h gap to skip data holes / delistings), then
  fully rotate.
- **Costs**: 5 bps per leg per rebalance (taker + slippage assumption),
  applied to both the long and short leg every period.
- **Signals tested**: `chg_5m, chg_15m, chg_30m, chg_open_1d, chg_24h,
  chg_1w, chg_1m`, each as momentum-continuation or mean-reversion, at
  N in {5,10,15,20,30}, and as long+short / long-only / short-only.
- **Validation**: grid search is fit on July (in-sample); the best-Sharpe
  config is then re-run untouched on August (out-of-sample) to check it
  isn't overfit, plus on the full two-month window.

## Run it

```
pip install pandas numpy matplotlib openpyxl
python run_backtest.py <july_file.xlsx> <august_file.csv> [--min-volume 1000000]
```

Outputs land in `results/`:
- `grid_search_july.csv`, `grid_search_august.csv` — full sweep, sorted by Sharpe.
- `picked_strategy_summary.csv` — the July-picked config's July / August / combined metrics.
- `picked_strategy_returns.csv` — per-period returns for the picked config.
- `equity_curve.png` — equity curve over the full period.

Raw data files are not committed (see `.gitignore`); point the script at
your own exports.
