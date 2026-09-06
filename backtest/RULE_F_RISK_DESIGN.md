# Rule F — candidate stop-loss / position-sizing scheme

**Status: research only. This does NOT clear §6F. Rule F remains WATCH-ONLY / PILOT-CANDIDATE.**
Nothing here authorizes a live trade. This is one input toward the "specific stop-loss /
take-profit / position-sizing scheme, back-tested at the single-trade level" that §6F requires
— it proposes numbers for review, on the same two-month sample already flagged as one regime,
using the narrower BTC/ETH-only exclusion instead of the process's full Majors Whitelist.

Reproduce with `python rule_f_risk_design.py` from `backtest/`, using `results/trade_log.csv`.

## The headline finding: without a stop, the account gets wiped out

The basket backtest's aggregate Sharpe (6.15) comes from averaging 10 names every period. But
Rule F's only currently-executable form is **Discretionary-Single-Trade mode**: one position at
a time, the single most-extreme 30-minute mover each scan (401 sequential trades, July 1 –
August 31 2026).

Simulated with full notional exposure and no risk-management stop (only the natural floor of
losing 100% of the capital allocated to that trade — what an exchange's own liquidation would do
even with no stop order placed):

| | No stop, full notional |
|---|---|
| Win rate | 59.9% |
| Average trade | +95.6 bps |
| **Total return over 2 months** | **−100.4%** (wiped out) |
| Max drawdown | −100.4% |

**A 60% win rate and a positive average trade still produces total ruin**, because the return
distribution has a fat left tail: one trade in this sample lost more than the entire position
(−111.8%, a short squeeze). This is the concrete, numeric answer to "why can't Rule F size a
position without a stop" — it is not a hypothetical caution, it is what happens when you replay
the actual single-trade sequence.

## Stop-loss grid (instrument-level, for shape only — not a sizing plan)

Capping the loss at a fixed level and re-running the same 401-trade sequence at full notional
(again: not real sizing, just to see how the distribution changes shape):

| Stop-loss | Profit factor | Sharpe | Max drawdown |
|---|---|---|---|
| none (−100% floor only) | 1.27 | 3.77 | −100.4% |
| 5% | 3.06 | 17.47 | −23.5% |
| 8% | 2.27 | 13.64 | −43.9% |
| 10% | 2.01 | 11.83 | −55.0% |
| 15% | 1.66 | 8.70 | −72.2% |
| 20% | 1.51 | 7.03 | −79.2% |
| 25% | 1.43 | 6.08 | −82.2% |
| 30% | 1.39 | 5.48 | −84.5% |

§6F's bar is PF > 1.50 — that alone rules out anything looser than ~20%. But the tightest stops
(5–8%) that look best here are the ones I trust **least**: this data is scan-snapshot resolution
(median gap ~3h), not a continuous price path, so a stop simulated this way can only trigger if
the *realized* return at the next scan breached it — it cannot see a price spike far past the
stop intra-period that reverted before the next snapshot. A tight stop on a coin that just moved
30%+ in 30 minutes is exactly the kind of level continuous, noisy price action would clip
constantly in ways this backtest cannot show. **Treat 5–10% as almost certainly overfit to this
specific historical path, not as a real edge.**

## Recommended candidate: 15–20% stop, 0.50% risk per trade

Converting to account-level returns under real position sizing (`position size = risk% ÷
stop%`, matching the Q2/S convention of a fixed % of equity risked per trade):

| Stop | Risk/trade | Position size | Total return (2mo) | Sharpe | Max DD | PF |
|---|---|---|---|---|---|---|
| 10% | 0.50% | 5.0% of equity | +55.8% | 11.83 | −3.4% | 2.01 |
| **15%** | **0.50%** | **3.3% of equity** | **+26.4%** | **8.70** | **−3.7%** | **1.66** |
| 20% | 0.50% | 2.5% of equity | +16.1% | 7.03 | −3.3% | 1.51 |
| 25% | 0.50% | 2.0% of equity | +11.3% | 6.08 | −2.9% | 1.43 (fails §6F) |

**Candidate: stop-loss 15%, take-profit not fixed (thesis exits on reversion, next-scan
rotation), risk 0.50% of equity per trade (3.3% notional position size).** 15% clears PF>1.50
with room to spare, keeps Sharpe high without leaning on the least-trustworthy tight-stop end of
the grid, and caps max drawdown near −3.7% of equity at this sizing — small enough that being
wrong about the true stop-out rate (which this proxy likely understates) doesn't threaten the
account. 20% is the more conservative fallback if 15% proves too tight once tested against real
intrabar data.

**Robustness check — single best week removed** (2026-08-16, the same outsized week flagged in
the original backtest), at risk=0.50%:

| Stop | Total incl. best week | Total excl. best week |
|---|---|---|
| 15% | +26.4% | +20.6% (78% of total remains) |
| 20% | +16.1% | +12.2% (76% of total remains) |

Neither collapses to unprofitable without its best week — a meaningfully better sign than the
naive overfit config from the original grid search, but still only one regime's worth of weeks.

## What this analysis does NOT establish

- **No real fill simulation.** Every number above assumes the stop fills exactly at the stop
  price with the same 5bps cost as a normal exit. Real slippage on a stop-out, on a name that
  just spiked hard, could be materially worse.
- **No intrabar data.** Repeated for emphasis: this is the single biggest gap. A proper single-
  trade backtest needs the actual price path during each ~3h hold, not just its endpoints.
- **Wrong universe.** Still BTC/ETH-only excluded, not this process's full Majors Whitelist.
- **One two-month regime**, same as the base backtest.
- **No take-profit tested.** The thesis exits via reversion/rotation, not a fixed TP; whether an
  explicit TP improves or hurts risk-adjusted return is untested here.
- **LV-Guard question untouched.** F4's "no Auto-Skip on entry" design choice is unaffected by
  this exercise.

None of the above changes because a stop-loss number now exists — §6F's other seven checkboxes
(independent months of data, LV-Guard resolution, real funding data, full-whitelist re-run,
Kikuji's sign-off) are all still open. This is one candidate answer to one of eight requirements.
