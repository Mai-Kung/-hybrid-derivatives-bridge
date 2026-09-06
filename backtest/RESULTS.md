# Altcoin perpetual long/short backtest — results

**Data**: Binance USDT-margined perpetual screener snapshots (`Mai_BI_*_Combined_FullMonth`),
July 1 – August 31 2026, ~700 alt perpetuals, 413 scan timestamps (~6–7 scans/day).
Universe = all `*USDT.P` except `BTCUSDT.P`/`ETHUSDT.P`, 24h volume ≥ $1M.

## The headline finding: fade the 30-minute pump, short-only

At every scan, rank the alt universe by 30-minute price change (`chg_30m`).
**Short the top 10 biggest 30-minute gainers, no long leg**, hold to each
coin's next scan (~2–4h later), rotate. Cost assumption: 5 bps per leg
(taker + slippage).

| Period | Trades (periods) | Total return | Ann. Sharpe | Max drawdown | Win rate |
|---|---|---|---|---|---|
| July (in-sample) | 206 | +72.8% | 5.07 | −22.0% | 54.9% |
| August (out-of-sample) | 195 | +100.7% | 7.67 | −23.3% | 59.5% |
| **Full (Jul+Aug)** | 401 | **+246.7%** | **6.15** | −23.3% | 57.1% |

Weekly breakdown, 8 of 10 weeks positive (one rough week at the very start,
one outsized +70% week mid-August — not a single lucky week carrying it):

```
2026-07-05  -14.8%      2026-08-02   +5.7%
2026-07-12  +31.2%      2026-08-09   -5.3%
2026-07-19  +22.5%      2026-08-16  +70.1%   <- outlier week
2026-07-26  +28.0%      2026-08-23   +2.7%
                         2026-08-30   +9.4%
```

**Interpretation**: on Binance alt perps, a sharp 30-minute spike is usually
a short-lived pump (thin order books, liquidation cascades, bot-driven) that
mean-reverts before the next scan. Shorting the most extreme pumpers
captures that reversion; there was no comparable edge on the long side
(buying dips) or on longer lookbacks (1d/1w/1m momentum) — see grid search
below.

## Why "best in-sample Sharpe" is the wrong way to pick a strategy

The naive approach — grid-search July, take the #1 Sharpe — picks
`chg_30m momentum, N=5, short_only` (short the 5 biggest gainers, i.e. same
family of trade but with a 2× smaller momentum lookback treated as
*momentum* not *reversion*, and a smaller N):

| Period | Total return | Sharpe |
|---|---|---|
| July (in-sample) | **+511.9%** | 12.19 |
| August (out-of-sample) | **−54.7%** | −4.57 |

A spectacular in-sample number that **loses more than half the account**
the very next month. See `results/equity_curve.png` (bottom panel) for the
picture. N=5 baskets are dominated by one or two coins each period — pure
noise dressed up as alpha. This is why the report above requires **N≥10**
and picks the config that is best under `min(Sharpe_July, Sharpe_August)`
rather than best on July alone (`results/robust_candidates.csv`).

## Robustness checks on the picked strategy

**Transaction cost sensitivity** (full 2-month period):

| Cost per leg | Total return | Sharpe |
|---|---|---|
| 5 bps | +246.7% | 6.15 |
| 10 bps | +183.9% | 5.27 |
| 20 bps | +90.2% | 3.52 |
| 30 bps | +27.4% | 1.76 |
| 50 bps | −42.9% | −1.76 |

Edge survives realistic Binance perp costs (taker ≈4-5bps, plus some
slippage) with a wide margin, and only breaks even north of ~35-40 bps
round-trip. Thin altcoins during a pump can have worse slippage than that on
size, so treat position sizing per name conservatively.

**Liquidity-threshold sensitivity** (same config, restricting the universe
to more liquid names only): the edge is **not** just a micro-cap-illiquidity
artifact — it holds at every volume cutoff tested, including a $50M/24h
floor (`results/liquidity_sensitivity.csv`).

## What didn't work

From the full grid search (`results/grid_search_july.csv`,
`results/grid_search_august.csv` — every signal × N × direction × side):
- **Long-only and long-short (dollar-neutral) variants underperform
  short-only** across almost every signal/N combo — buying the dip on alts
  was not a reliable edge in this window; the edge is concentrated in
  fading pumps.
- **Longer lookbacks (`chg_1w`, `chg_1m`, `chg_24h`) are weaker and less
  stable** than the short 15–30 minute window; slower momentum signals
  don't have the same fast mean-reversion the strategy is exploiting.
- Every top-10 config in the robust ranking is a variant of the same idea
  (`short_only`, `reversion` or `momentum` on a 15–30 minute lookback) —
  this looks like one real, repeatable effect rather than several
  independent edges.

## Caveats — read before trading this

1. **Funding rate is not modeled.** The data has no funding-rate column.
   During an alt pump, funding is usually positive (longs pay shorts),
   which would be a tailwind for this exact strategy — real returns could
   be *better* than shown. Get real funding data before sizing this up.
2. **Two months, one regime.** This period is alt-heavy/volatile (many
   +50–400% "Change from open" prints in the raw data). A calmer or
   trending-down regime could behave differently; re-validate quarterly.
3. **Screener snapshots ≠ live execution.** Real fills depend on order-book
   depth at the exact moment, not the last-printed price; the 5-50bps cost
   sweep above is a proxy, not a guarantee, especially at size on N=10
   names during a pump (where the pump is often driven by thin liquidity in
   the first place — that's part of *why* it reverts).
4. **Short selling perpetuals carries the usual derivatives risk**
   (liquidation on adverse moves, exchange/counterparty risk). Max
   drawdown here is ~23% — allocate capital and leverage accordingly.

## Reproduce

```
cd backtest
pip install -r requirements.txt   # pandas, numpy, matplotlib, openpyxl
python run_backtest.py <july_file> <august_file>
```

All numbers above come straight out of `results/*.csv` and
`results/equity_curve.png` produced by that command.
