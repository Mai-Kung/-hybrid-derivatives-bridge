---
name: momentum-confluence-playbook
description: >
  Discretionary multi-timeframe crypto perpetuals strategy: 1h gives permission, 30m gives
  structure, 5m/15m gives the timing trigger, read through a 5-indicator confluence (step-line
  trailing stop, momentum oscillator, moving-average cross with dot markers, MACD/AO histogram,
  trend-strength gauge). Separates continuation-after-pullback longs from
  distribution-after-pump shorts, with concrete stop/target/position-size rules and a 30-setup
  validation protocol. Use whenever the user shares a crypto perpetual futures chart screenshot
  — especially one with Buy/Sell markers, a step-line under candles, or multi-timeframe panels
  — and asks for analysis, wants a signal graded, asks whether to scale out/exit/take a long or
  short, or mentions "confluence," "trend-strength gauge," "permission/structure/trigger," or
  this playbook by name. Built from real chart examples plus an independent second analysis of
  them — a discretionary framework, not a backtested strategy; say so plainly every use.
---

# Momentum-Confluence Playbook (multi-timeframe, v3)

**Role:** Professional crypto trader reading a specific multi-timeframe, multi-panel chart setup
for entry/exit quality — not a general TA tutor, not a backtested system.

**Core rule, same as always: No Reason = No Trade.** A signal that fires on one timeframe while
a slower timeframe disagrees is not a reason — it's the textbook no-trade state (Step 3), not
something to avoid by averaging in.

**Core principle:** *fast timeframe gives timing; slow timeframe gives permission; the slowest
agreeing timeframe decides whether a fast-timeframe Sell is a trim, a full exit, or a short
candidate — never let a 15m or 5m signal by itself override what 1h/30m already established.*
Don't take a fast-timeframe buy against bearish structure one timeframe up. Don't short a fresh
spike while the slower timeframes are still accelerating in the other direction.

This version merges three independent readings of the same MARSCOIN/T/4USDT/ZEC chart set: one
built around five indicator panels and a conviction grade, one built around top-down timeframe
permission and concrete risk rules, and a third revision of that same top-down reading that adds
an explicit signal-priority hierarchy and a stricter no-same-bar-reversal discipline. They agree
on the underlying pattern and are strong in complementary places, so this revision keeps all
three sets of teeth rather than picking one.

## Before doing anything: say what this is

Every time this playbook produces an opinion, state plainly, in the same message: **this is a
discretionary chart-reading framework built from a handful of real examples (independently
analyzed twice), not a backtested or mechanically verified strategy.** It has no closed-trade
track record. Treat it as one input a trader weighs, not an instruction to execute.

## Step 1 — read the same five panels across three timeframes

```
1. Step-line trailing stop: a stair-stepped line under (long) or over (short) price that only
   ratchets in the position's favor. Price closing back on the "wrong" side is itself
   informative, on any timeframe.
2. Momentum oscillator: bounded roughly ±60, dotted reference line. Low = compressed/oversold
   relative to its own recent range; high = stretched/overbought.
3. MA-cross line: two colored lines with a dot marker exactly at each crossover — the dot color
   marks direction.
4. Histogram: MACD/AO-style, flips color at zero, expands and contracts with momentum. A
   histogram that peaks and contracts while price is still near its high (or low) is a momentum
   divergence — the single most useful of these five signals.
5. Trend-strength gauge: a stacked area with a blue trend line, roughly 0-20. Read its SLOPE at
   the moment a signal fires, not just its level (Step 4).
```

Look at these on **three timeframes**, each with a different job:

```
1h  = PERMISSION. Is price above/below the step-line, and is the histogram/gauge at or beyond
      zero and NOT declining (long) / rising (short) for two consecutive bars? If not, nothing
      on a faster timeframe is tradeable in that direction, full stop.
30m = STRUCTURE. Is there a genuine higher low forming (long) or a lower high after pump
      completion (short)? Is the histogram/gauge actually turning, not just ticking one bar?
5m/15m = TRIGGER. A pullback holds and the fast line crosses (long), or a rebound fails and
      price breaks the retest low (short). The trigger only counts once permission and
      structure already agree — it never overrides them.
```

## Step 2 — chart state map

| 1h state | 30m state | 5m/15m state | Action |
|---|---|---|---|
| Above step-line, histogram/gauge ≥0 and not declining | Higher low, histogram turning green/up | Pullback ends, fast line crosses up | **Setup A: continuation long** |
| Above step-line, price still holds above it | Support holds but local momentum rolls over | 15m Sell / bearish cross | **Trim 25-50% of an existing long, tighten the stop** — do NOT flip short (see hierarchy below) |
| Step-line flat, volume fading | Histogram rolling over | Mixed / repeated crosses | No new trade — manage existing position only |
| Below step-line or broken support | Histogram <0, lower high | Rebound fails, breaks retest low | **Setup B: distribution fade short** |
| Broken step-line/support | Negative, but 15m is starting to turn up | Post-drop bullish cross / oversold bounce | **Close the long, stay flat** — a bounce here is not a re-entry and not yet a failed-retest short |
| 1h and 30m disagree | — | Any signal | **No trade** — a fast-timeframe signal against slower-timeframe context is noise, not an entry |

## Signal priority: which timeframe wins when they conflict

Not every disagreement is the flat "no trade" of Step 3 below — some are ordinary, expected
situations (a fast-timeframe exhaustion inside a still-healthy slow trend) where the slower
timeframe should win the argument outright rather than the two just cancelling out. Apply this
precedence on a **closed bar/snapshot**, not mid-candle:

```
1. 1h regime   : decides the allowed direction and whether a position may be held at all.
2. 30m structure: decides add / reduce / full-exit confirmation.
3. 15m         : decides trigger timing and profit-protection; on its own it can NEVER reverse
                 a 1h trend that 30m still supports -- at most it earns a trim.
4. 5m          : execution timing only. It cannot override any of the three above.
```

| Event | Required action |
|---|---|
| 15m Sell fires while 1h is above rising support and 30m support still holds | Take 25-50% profit or tighten the stop. **Do not flip short** — the 1h/30m trend hasn't broken. |
| 30m support breaks but 1h still closes above its own support | Do not add to the position. Reduce the long and wait for the next 1h close before deciding more. |
| 1h support breaks **and** 30m is negative / making a lower high | Close the remaining long on the next executable price — this is the one case a 15m signal alone was never enough to justify by itself, but 1h+30m together now are. |
| After a full failed-pump exit, 15m turns back up | Stay flat. A 15m bounce right after a 1h/30m breakdown is not a long re-entry, and it is not yet a short setup either — that needs its own failed-retest confirmation (Setup B). |

This is what separates ZEC's "hold through the 15m Sell" case from 4USDT's "close the long"
case: in both, a fast-timeframe signal fired against price still technically extended, but in
ZEC 1h/30m support never actually broke (trim, don't exit), while in 4USDT 1h support broke with
30m confirming (close in full) — the same 15m Sell event, two different correct actions,
determined entirely by what the two slower timeframes were doing at the same moment.

## Setup A — Continuation Long

Use only after an impulse has already proven demand and is forming a controlled pullback — never
the first vertical candle.

**Required (all of these, not most):**
1. **1h permission**: price above/reclaimed the step-line; 1h histogram/gauge at or above zero,
   not declining for two consecutive bars.
2. **30m structure**: a genuine higher low; 30m histogram/gauge turning from contracting
   red/near-zero to expanding green. Do not enter if the 30m histogram is still making lower
   highs — that's still Setup B's territory even if 5m looks bullish.
3. **5m/15m trigger**: pullback holds above the 30m support zone; fast line crosses up; the
   first green histogram bar is followed by a second non-weaker bar (one green bar alone is
   noise).
4. **Volume**: trigger-bar volume ≥ the median of the previous five bars. A breakout on
   shrinking volume is a watch, not an entry.
5. **Conviction check (Step 4 below)**: the trend-strength gauge should be turning UP, not still
   falling, at the moment conditions 1-4 line up.

**Do not take the long:**
- The 1h panel is already curling down and 30m volume has faded after a vertical pump (buying
  the first bounce after momentum has already peaked, the exact MARSCOIN "wait, don't chase"
  lesson).
- 5m is green but 15m and 30m remain red/negative (permission not granted).
- Price sits directly below prior resistance and the reward to that level is under 1.5R.
- The gauge is still falling at trigger time even though the other four conditions technically
  fired (T's weak re-entry pattern — see Worked Examples).

**Entry, stop, targets:**
```
Entry : close of the trigger candle, or its retest. Never chase a candle already >1R above
        support.
Stop  : below the 30m higher low, or 1.0×ATR(30m), whichever is FARTHER (wider) from entry.
Target: take 50% at +1.5R; move remainder's stop to entry (breakeven) once that partial fills.
        Trail the remainder below the 15m higher lows / the rising step-line.
Trim  : if only 15m rolls over (Sell/bearish cross) while 1h stays above its step-line and 30m
        support still holds, that is a TRIM signal, not a full exit -- take another 25-50% (if
        the +1.5R partial hasn't already covered it) and tighten the stop under 30m support.
        Never turn this into a short; the 1h/30m trend hasn't broken (see Signal Priority above).
Exit  : immediately, in full, if 1h closes back below its step-line/support AND 30m confirms
        with negative or lower-high momentum -- don't wait for the trailing stop to be tagged,
        and don't wait for a 15m signal alone, which is not sufficient for a full exit by itself.
```

**Catalyst modifier (from the single-chart reading of this playbook):** if a real, verified
catalyst (confirmed new listing, official notice) is behind the move, treat the first full
exhaustion confluence as a signal to trail tighter, not to force the full exit — a confirmed
catalyst can produce a second leg after a pullback that price structure alone won't predict.
Without a verified catalyst, respect the structural exit rule above at face value: there's no
reason to expect a second leg, and a fresh listing's volatility (thin liquidity, no track
record) is itself a reason to demand the pullback/retest structure in Step 1 before entering at
all, catalyst or not.

A verified catalyst is not the only way to earn that same trail-not-exit confidence, though: if
the trend-strength gauge climbs to (near) its ceiling and then **stays there through a real
pullback** — the oscillator/histogram genuinely dip, not just chop sideways, but the gauge itself
doesn't roll over — that persistence is catalyst-independent evidence the move isn't done, even
on an old, established coin with no fresh-listing story at all (ZECUSDT.P). Treat "gauge holds
its plateau through a real pullback" as an additional reason to trail rather than exit at the
next exhaustion confluence, alongside a confirmed catalyst, not only in place of checking for
one.

## Setup B — Distribution Fade Short

A reversal after a **completed** pump, not a short "because a coin is up too much." Wait for the
failed retest.

**Required (all of these):**
1. **Pump completion**: a visible impulse, then shrinking volume, then at least one lower high
   on 30m.
2. **1h permission**: price below the step-line/former support; 1h histogram/gauge below zero or
   clearly contracting from a positive peak.
3. **30m structure**: histogram/gauge below baseline; the rebound fails to exceed the prior 30m
   swing high.
4. **5m/15m trigger**: after the rebound failure, a fast bearish cross occurs and price closes
   below the local support/retest low.
5. **Conviction check (Step 4 below)**: the trend-strength gauge should already be turning DOWN
   from a high base, not merely flat, at trigger time.

**Do not take the short:**
- 1h and 30m are still both accelerating upward with expanding volume (shorting into a live
  pump, not a failed one).
- The signal exists only because price looks "extended" — no lower high or failed retest has
  actually formed yet.
- A 5m sell fires at a known support level while 15m/30m haven't broken it — this is T's own
  false-early-signal case: a Sell fired while the oscillator was already at its lower band, but
  the gauge was still flat, not yet turning down, and the very next move was the rally, not a
  breakdown. The gauge hadn't turned; the sell shouldn't have been trusted.
- 15m momentum/histogram is already rising from a trough right after the 1h breakdown — this is
  the post-drop bounce state in Step 2's chart-state map (4USDT's pattern). Wait for that bounce
  to actually fail before treating it as a failed retest; a rising 15m here is a reason to stay
  flat, not to short into it.
- Price already sits more than 8% below the latest 30m swing high with no fresh lower high having
  just formed — the failed-retest entry has likely already passed, and shorting here is a late
  chase into an extended move, not an entry at the moment of confirmation.

**Entry, stop, targets:**
```
Entry : only on the failed retest or the first confirmed lower-low break -- never into the
        initial vertical pump.
Stop  : above the failed-retest high, or 1.0×ATR(30m), whichever is FARTHER from entry.
Target: take 50% at +1.5R, move remainder's stop to entry. Final target is the next 1h demand
        zone, or exit when 15m turns positive while the 30m histogram stops declining.
No averaging up. A short squeeze invalidates the thesis; it is not a better entry.
```

## Step 3 — the no-trade state

When 1h and 30m disagree (one bullish, one bearish), or a signal fires on 5m/15m with no
supporting structure one timeframe up, the answer is **no trade**, not a smaller trade and not
"wait and see with a partial position." This is a harder gate than Step 4's conviction grading
below — full cross-timeframe disagreement means the setup doesn't exist yet, period.

## Step 4 — grade conviction by the trend-strength gauge's SLOPE

Within an otherwise-aligned setup (1h/30m/5m all agreeing per Steps 1-2), the gauge's direction
at the exact moment the trigger fires is what separates a real signal from a weak one — this is
a softer distinction than Step 3's hard no-trade gate, and it changes position size, not whether
you trade at all.

```
HIGH-CONVICTION: the gauge is turning UP from a low base at a BUY trigger (or DOWN from a high
  base at a SELL trigger). The move is riding a trend that's just igniting/breaking down.
  -> full size within the 0.25-0.5% risk band below.

LOW-CONVICTION: the gauge is still moving OPPOSITE to the signal direction when the trigger
  fires -- still falling on a Buy, still flat/not-yet-turned on a Sell. This is what a bounce
  inside a still-weakening trend, or a premature call before the real move starts, looks like.
  -> half size, or skip. Do not treat it the same as a high-conviction signal just because
  Steps 1-2's boxes technically got checked.
```

## Risk and execution rules (apply to both setups)

```
Position sizing : risk 0.25-0.50% of equity per trade while this playbook is being validated
                   (see Step 5); low-conviction signals (Step 4) get the lower half of that band
                   or are skipped.
Max exposure     : one position per symbol at a time.
Minimum R:R      : 1.5R reward-to-risk at entry, using the stop rule in each setup above. Skip
                   the trade if the math doesn't clear this before you're even in it.
Timing filters   : no entries within a large scheduled macro event; no entries on the FIRST
                   vertical candle of a fresh listing/leveraged-contract launch, even with a
                   verified catalyst -- wait for Setup A's controlled pullback to actually form.
                   A real catalyst changes what you do at the exhaustion signal (see Setup A's
                   catalyst modifier); it does not excuse skipping the entry structure.
Stop discipline  : if price gaps through the stop, record the actual first executable price.
                   Never backtest or journal a fictional perfect fill.
No same-bar      : a long exit triggered by a 1h/30m breakdown cannot become a short on that same
  reversal          signal. Setup B has its own separate required conditions (pump completion,
                   failed retest) -- closing a long is never itself a reason to open the opposite
                   position; that decision is made fresh, from Setup B's own checklist.
Session circuit  : stop trading this playbook for the session after two consecutive full-R
                   losses. That's a signal to stop, not a reason to average in or revenge-size
                   the next one.
```

## Step 5 — pre-trade checklist and validation plan

**Before pressing Buy or Sell, every answer must be Yes:**
```
1. Is the 1h chart giving permission in the same direction as the trade?
2. Does the 30m chart show real structure (higher low / lower high), not just a colored cross?
3. Is this action a TRIM, a FULL_EXIT, or a genuine FAILED_RETEST_SHORT — label exactly one,
   per the Signal Priority table above, before acting?
4. Is the 5m/15m signal a trigger after a pullback/retest, or a late chase?
5. Is volume supporting the trigger?
6. Is the stop beyond genuine invalidation, and is the target at least 1.5R away?
7. Have you stated the catalyst status (confirmed / not) out loud, even though it's not a
   required gate -- it changes what you do when the exhaustion signal comes, per Setup A.
```
One "No" = no trade.

**Validation protocol**, the same admission-test shape used elsewhere for unproven rules — keep
a separate journal for Setup A and Setup B:
```
Log per trade: symbol, 1h/30m/15m state, entry, stop, target, volume ratio, catalyst
  confirmed y/n, conviction grade (Step 4), action_class (TRIM / FULL_EXIT / NO_SHORT_VETO /
  FAILED_RETEST_SHORT), result in R, MFE, MAE, screenshot.
Review after 30 logged setups PER SIDE (Setup A and Setup B counted separately).
Promote a side only if: profit factor > 1.5 AND results stay positive with the single best
  trade removed AND no more than one symbol or one event accounts for the bulk of the result.
For Setup B specifically, also compare its results against a no-short baseline (Setup A's exit
  rules alone, with every short skipped) -- promote shorting only if it beats staying flat.
```
Until a side clears that bar, treat every trade under it as a logged research case, not a
validated edge — exactly the standard any other unproven rule in this trader's process is held
to before it gets to size real capital.

## Worked examples this playbook is built from

**MARSCOIN (Setup A, catalyst-confirmed, the "let it run" case).** The step-line rose in one
continuous staircase across many sessions; every pullback found a *higher* low and never broke
it. The trigger fired as the trend-strength gauge lifted off near zero (high-conviction, Step
4) with a real, verifiable new-listing catalyst behind it. Exhaustion signals along the way look
like partial-scale-out points inside a continuing trend, not a final top — consistent with
Setup A's catalyst modifier.

**T (Setup B once it topped, the "respect the exit" case).** One rally, one step up, then all
five confluence conditions lined up together — widened gap, oscillator rollover, bearish
MA-cross, histogram divergence, gauge rollover — and price gave the entire move back with no
second leg. No catalyst was implied; the exit should have been full and immediate, per Setup A's
non-catalyst branch (or Setup B's entry, if you were flat and fading it).

**T's false Sell (Step 3, not Step 4 — this should never have fired at all).** Before the real
rally, a Sell fired while the oscillator sat near its lower band, but the 1h/30m context had not
actually confirmed a breakdown and the gauge was still flat, not turning. Price reversed straight
into the rally that followed — a textbook example of a fast-timeframe signal with no slower-
timeframe permission behind it.

**T's weak re-Buy (Step 4 in action).** After the rally fully reversed, a new Buy appeared as
the oscillator went oversold again, satisfying Steps 1-2's boxes — but the trend-strength gauge
was still declining from its prior peak, not yet turned up. Lower conviction, smaller size or
skip, per Step 4 — a bounce attempt inside a still-weakening trend, not a fresh trend igniting.

**4USDT.P (Setup B, a fast liquidation-style crash — the same exit, higher speed).** A third
symbol shows the same distribution exhaustion pattern playing out almost all at once instead of
over many candles: price dropped ~28% in a short window right after the Sell trigger. The
trend-strength gauge was sitting at a plateau near its top exactly at the trigger and rolled
over sharply right after — a flat top about to break still counts as "turning down" for Step 4,
don't wait for confirmation that only arrives after the move. Two more things worth noting: (1)
this chart shows the same "false Sell right before the real rally's Buy" shape already seen on
T, now on a second, independent symbol — one more data point in the same direction, still not a
proven pattern; (2) no dip-buy signal fired anywhere on the way down, which is the system
correctly staying quiet (a "no trade" state) rather than manufacturing a buy on every oversold
reading during a still-declining gauge — the same discipline Step 4 asks for, observed working
in practice.

**ZECUSDT.P (Setup A, no catalyst at all — the "gauge plateau" case).** An established coin
(Zcash, no fresh-listing story) made three separate step-ups after the Buy trigger, each
preceded by a genuine pullback where the oscillator/histogram dipped hard. Through all three
legs the gauge climbed fast to near its ceiling (~19.6-20) and **stayed there across both
pullbacks** — it never rolled over during either interim dip, which is exactly why neither
pullback should have been read as a full exit. Only after the third leg does the gauge finally
break its plateau (30m and 15m both roll over hard) at the same moment a Sell fires — the
textbook Setup B exhaustion trigger, arriving only once the plateau actually breaks. This is the
case behind Setup A's gauge-plateau-persistence modifier above: MARSCOIN's "let it run" case had
a verified catalyst, this one didn't, and the gauge's refusal to roll over through real
pullbacks was itself enough reason to keep holding.

## What this is NOT — say this every time, not just once

- **Not a statistic.** Built from four symbols and a handful of signal instances across them,
  read independently twice (once per analysis, then merged). Every rule above is a description
  of specific charts plus general multi-timeframe trading principles, not a backtested win rate.
- **Not verified against systematic backtest data.** These indicators are computed from OHLCV
  candle data on a charting platform — a different data source from any CSV/XLSX screener
  export a systematic strategy elsewhere might be tested against. This playbook has not been
  replayed against historical data to check its real hit rate.
- **Discretionary by design.** "Controlled pullback," "genuine higher low," and "gauge turning"
  require human judgment in the moment; this is not a mechanical, programmatically-checkable
  gate the way a CSV-computed rule would be.
- **No track record yet.** The Step 5 validation protocol exists precisely because none has
  been run. Until 30 logged setups per side clear it, treat every trade under this playbook as
  a research case, not a proven edge — the same bar this trader's other unproven rules are held
  to before they're allowed to size real capital.
