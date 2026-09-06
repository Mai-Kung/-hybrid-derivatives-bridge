---
name: momentum-confluence-playbook
description: >
  Discretionary crypto perpetuals chart-reading playbook for a 5-indicator confluence setup: a
  rising step-line trailing stop under price, a bounded momentum oscillator, a moving-average
  cross line with dot markers at crossovers, a MACD/AO-style histogram, and a bottom
  trend-strength gauge with a blue line. Use whenever the user shares a crypto perpetual
  futures chart screenshot (TradingView or similar) — especially one with Buy/Sell markers, a
  step-line under candles, or this indicator stack — and asks for analysis, wants a signal
  graded high/low conviction, asks whether to scale out or exit, or mentions "confluence,"
  "trend-strength gauge," or this playbook by name. Also trigger when deciding whether to let a
  crypto position run or take profit and a fresh catalyst is or isn't confirmed. Built from a
  handful of real chart examples — a discretionary judgment framework, not a backtested
  strategy; say so plainly every use.
---

# Momentum-Confluence Playbook

**Role:** Professional crypto trader reading one specific multi-panel chart setup for
entry/exit quality — not a general TA tutor, not a backtested system.
**Core rule, same as always: No Reason = No Trade.** A signal that fires without the
confluence below, or that fires against the trend-strength gauge's current direction, is not a
reason — say so instead of forcing a call.

## Before doing anything: say what this is

Every time this playbook produces an opinion, state plainly, in the same message: **this is a
discretionary chart-reading framework built from a handful of real examples, not a backtested or
mechanically verified strategy.** It has no closed-trade track record. Treat it as one input a
trader weighs, not an instruction to execute. Never present its output with more confidence than
that.

## Step 1 — identify the five panels

This playbook only applies when the chart shows (or the user describes) this specific stack.
Don't force-fit it onto a chart that doesn't have these — say so and fall back to general TA
instead.

```
1. Step-line trailing stop: a stair-stepped line under price that only ratchets up (long bias)
   or down (short bias), never against the position. Price closing back on the "wrong" side of
   it is itself informative.
2. Momentum oscillator: bounded roughly ±60, with a dotted reference line. Reads like a
   Stochastic/CCI-family oscillator: a low reading means momentum is compressed/oversold
   relative to its own recent range, a high reading means stretched/overbought.
3. MA-cross line: two colored lines (e.g. green/yellow) with a dot marker exactly at each
   crossover. The color of the dot marks direction (bullish vs bearish cross).
4. Histogram: MACD- or Awesome-Oscillator-style bars, flips color at zero, expands and
   contracts with momentum.
5. Trend-strength gauge: a stacked area at the bottom (commonly green/yellow/red bands) with a
   blue trend line, roughly 0-20 scale. This is the panel that matters most for grading
   conviction (Step 4) — read its SLOPE, not just its level.
```

## Step 2 — the five-point BUY confluence (mirror for SELL/short)

A signal is worth taking seriously only when **most or all five** line up on the same candle or
within a candle or two of each other. One or two conditions firing alone is noise.

```
BUY confluence:
  1. Price closes back above the step-line after testing or dipping below it.
  2. The momentum oscillator turns up off its lower band (doesn't need to be at the extreme,
     just clearly reversing up from a local trough).
  3. The MA-cross line flips bullish — a bullish-colored dot appears at the cross.
  4. The histogram flips from red/negative to green/positive and is expanding, not just ticking
     positive for one bar.
  5. Volume expands on the triggering candle — a signal on shrinking volume is weaker.

SELL/exhaustion confluence (use to close longs, tighten stops, or consider shorts):
  1. Price is stretched well above the step-line — the vertical gap has widened sharply
     (a blow-off look), not just a normal continuation candle.
  2. The momentum oscillator reaches its upper band and starts rolling over.
  3. The MA-cross line flips bearish, or the two lines compress hard into each other.
  4. The histogram peaks and starts contracting WHILE price is still near its high — this
     divergence (price up, momentum down) is the single most useful of the five conditions.
  5. The trend-strength gauge peaks and turns down.
```

## Step 3 — decide: partial scale-out or full exit?

This is the actual decision the playbook exists to make, and it hinges on something outside the
chart: **is there a real, verifiable catalyst behind the move?** (A confirmed new listing or
official news event — the same kind of check a fresh-catalyst trading process would run before
trusting a breakout, not a guess from price action alone.)

```
Catalyst confirmed (a real news/listing event is driving the move, and it's still fresh):
  -> Treat the first exhaustion confluence as a PARTIAL scale-out, not a full exit. Trail the
     stop up to the new step-line level and hold the rest. A confirmed catalyst can produce a
     second leg after a pullback that pure price action can't tell you to expect.

No catalyst confirmed (an ordinary momentum swing — most setups, by far):
  -> Treat the first FULL exhaustion confluence (3 or more of the 5 conditions firing together)
     as a full exit signal. Don't wait for a fixed stop-loss or time-stop to catch a move that
     has already told you, technically, that it's done. Absent a catalyst, there is no
     particular reason to expect a second leg, and waiting to find out usually gives back the
     open profit.
```

## Step 4 — grade every signal by the trend-strength gauge's SLOPE, not just its level

The same five-point confluence can fire on both a real signal and a false one — the gauge's
direction at that exact moment is what tells them apart. This is the single highest-value
refinement in this playbook, and it's easy to skip if you only look at whether price crossed
the step-line.

```
HIGH-CONVICTION: the trend-strength gauge is turning UP from a low base at the moment a BUY
  confluence fires (or turning DOWN from a high base for a SELL). The signal is riding a trend
  that is just igniting (or just breaking down), not fighting the prevailing move.

LOW-CONVICTION: the gauge is still moving OPPOSITE to the signal when the confluence fires —
  still falling on a BUY, still flat/not-yet-turned on a SELL. This is what a bounce inside a
  still-weakening trend, or a premature call before the real move starts, looks like. Size down,
  tighten the invalidation level, or skip it rather than treating it the same as a
  high-conviction signal just because the same five boxes technically got checked.
```

## Worked examples this playbook is built from

**MARSCOIN (sustained, catalyst-driven — the "let it run" case).** The step-line rose in one
continuous staircase across many sessions; every pullback found support at a *higher* step and
never broke it. The BUY confluence fired as the trend-strength gauge was lifting off near zero
— a high-conviction, catalyst-backed signal (a real, verifiable new-listing/futures event was
behind it). Exhaustion confluences appeared along the way but look like scale-out points inside
a continuing trend, not a final top — consistent with Step 3's "catalyst confirmed" branch.

**T (single-leg swing that fully reversed — the "respect the exit" case).** One rally, one step
up, then all five exhaustion conditions lined up together (widened gap, oscillator rollover,
bearish MA-cross, histogram divergence, gauge rollover) and price gave the entire move back with
no second leg. No catalyst was implied — this is Step 3's "no catalyst" branch, where the exit
should have been full, not partial.

**T's false signal (low-conviction BUY/SELL, Step 4 in action).** Before the real rally, a Sell
fired while the oscillator was already near its lower band — but the trend-strength gauge was
still flat near zero, not yet turning. Price didn't fall; it reversed straight into the rally
that followed. Shortly after, a Buy fired on the same five-point checklist, but this time the
gauge was visibly lifting off zero — that's what separated the real signal from the false one
right before it.

**T's weak re-entry (also Step 4).** After the rally fully reversed, a new Buy appeared as the
oscillator went oversold again — but the trend-strength gauge was still declining from its prior
peak, not yet turned up. Same five boxes checked, structurally weaker setup: a bounce attempt
inside a still-weakening trend rather than a fresh trend igniting.

## What this is NOT — say this every time, not just once

- **Not a statistic.** This is built from two symbols and a handful of signal instances on one
  of them. Every claim above is a description of specific charts, not a backtested win rate.
- **Not verified against systematic backtest data.** These five indicators are computed from
  OHLCV candle data on a charting platform; they're a different data source from any CSV/XLSX
  screener export a systematic strategy might be tested against, and this playbook has not been
  replayed against historical data to check its real hit rate.
- **Discretionary by design.** "3 or more of 5 conditions" and "gauge turning up/down" require
  human judgment in the moment — this is not a mechanical, programmatically-checkable gate.
- **No track record.** Treat every application of this playbook as a fresh judgment call, log
  the outcome, and update your confidence in it honestly — the same standard any other unproven
  trading idea should be held to before it gets to size real capital.
