# Chart-pattern playbook: MARSCOIN (sustained) vs T (faded) — discretionary confluence overlay

**Status: proposal, not backtested, not part of any live rule. n=2 chart examples — treat this
exactly as cautiously as this whole document treats a 1-2 case backtest anywhere else.**

Source: two TradingView chart sets the trader shared (MARSCOIN/USDT.P and T/USDT.P, multiple
timeframes each), each showing a Buy→ride→Sell cycle picked out by an on-chart signal tool, with
five sub-panel indicators visible: a rising step-line trailing stop under price, a bounded
momentum oscillator (~0-60 scale, dotted reference line), a paired moving-average cross line
(colored dot at each cross), a histogram (MACD/AO-style), and a bottom "trend-strength" stacked
area with a blue trend line. Exact indicator names weren't given — everything below describes
*observed behavior*, not a specific script.

## What both cases have in common (the entry/exit mechanics that worked in both)

```
BUY confluence (both charts show this at their Buy points):
  1. Price closes back above the rising step-line (was below/testing it, now reclaims it)
  2. The momentum oscillator turns up off its lower band
  3. The MA-cross line flips bullish (green dot marks the cross)
  4. The histogram flips from red to green and starts expanding
  5. Volume expands on the triggering candle, not just price

SELL/exhaustion confluence (both charts show this before price gives back gains):
  1. Price becomes stretched well above the step-line (the gap widens sharply -- a blow-off look)
  2. The momentum oscillator reaches its upper band and starts rolling over
  3. The MA-cross line flips bearish, or the two lines compress hard into each other
  4. The histogram peaks and starts contracting WHILE price is still near its high
     (a momentum divergence -- price higher, momentum lower)
  5. The bottom trend-strength gauge peaks and turns down
```

Both trades were built on the same five-point entry and five-point exit logic. That part isn't
the interesting difference.

## What's different: the move MARSCOIN was riding vs the move T was riding

**MARSCOIN**: the step-line rose in one continuous staircase across the whole visible window —
each pullback found support at a *higher* step, never broke it, and the rally kept making new
highs across multiple sessions before the current pullback. This is a catalyst-driven move (the
same MARSCOIN this document already knows from §1/§12 — a genuine new-listing event with real,
verifiable news behind it). The Sell signals along the way (image 3) look more like scale-out
points inside a continuing trend than a final exit — the trader who kept re-buying dips and
holding through them is exactly why letting MARSCOIN run with no fixed take-profit (§13.2)
captured the +288% a 72h hold saw, instead of the +25-30% a tight TP would have banked.

**T**: one rally, one step up in the trailing stop, then the exhaustion signals (widened gap,
oscillator rollover, histogram divergence) all line up together and the Sell fires — and price
does not make a new step after that; it round-trips back down toward the entry zone. There's no
visible second leg, no news catalyst implied, nothing to re-buy. This is what an *ordinary*
momentum swing without a fresh catalyst looks like: the same five-point entry works, but the
exit needs to be respected the first time the exhaustion confluence appears, because there's no
underlying reason to expect a second wave.

## The strategy this implies

**The entry and exit confluence checklists above are the same regardless of context.** What
changes is how you act on the exit signal:

```
IF a genuine, verifiable catalyst exists (Rule N territory: N1 confirmed, fresh listing/notice)
  -> treat the first exhaustion confluence as a PARTIAL scale-out signal, not a full exit.
     Trail the stop up to the new step-line level instead of closing everything. This is the
     MARSCOIN pattern, and it's already why §13.2 uses no fixed TP for Rule N.

IF no verifiable catalyst exists (an ordinary momentum swing -- most Rule F candidates, and any
  Rule N alert that never got its N1 confirmed)
  -> treat the first full exhaustion confluence (3+ of the 5 exit conditions firing together)
     as a FULL exit signal. This is the T pattern: one leg, no reason to expect a second one,
     exit when the technical picture says the move is done rather than waiting for a fixed
     SL/TP to be hit.
```

## Proposed use: an early-exit overlay, not a new entry gate

This does **not** replace the hard stop-losses already defined for Rule N (§13.2, -20%) or Rule
F (§13.1, -20%) — those stay as the hard floor no matter what the chart pattern says. What this
adds is a **profit-protection trigger that can fire before the hard stop or time-stop**: if 3 or
more of the 5 exhaustion-confluence conditions align on an open Rule N/F position, and there is
no verified catalyst extending the thesis, close the position at market rather than waiting for
the 24h/72h time-stop to do it. This would have improved exactly the failure mode already found
in this document: Rule F's September loss (§11.2) and the 11-of-12 losing Rule N events (§12.3,
§13.2) are both "the position round-tripped before the time-stop caught it" stories — an
exhaustion-based early exit is aimed directly at that gap.

## What this is NOT, stated as plainly as everything else in this document

- **n = 2.** One sustained (MARSCOIN) and one single-leg (T) example is not a sample size,
  it's an illustration. Every number in the "what's different" section above is a description
  of two charts, not a statistic.
- **Not backtested against the screener data this process otherwise uses.** The indicators
  shown (step-line, oscillator, MA-cross, histogram, trend-strength gauge) aren't in the
  `Mai_BI_*` CSV/XLSX exports at all — they're TradingView chart indicators computed from OHLCV
  candles, a different data source entirely. Testing this for real requires either pulling
  actual OHLCV history for past Rule N/F trades and replaying the same indicators, or forward-
  paper-trading it from here.
- **Discretionary, not mechanical.** "3 of 5 conditions align" requires a human (or a much more
  specific technical spec) to judge in real time; it is not a CSV-computable gate the way
  N1-N6/F1-F6 are.
- Exactly per this document's own standard: this is a hypothesis worth logging and
  forward-testing, not a rule that has earned execution authority. It should sit alongside Rule
  N/F's live entries as an optional discretionary overlay the trader applies by eye, not as a new
  mechanical gate, until it has its own track record.
