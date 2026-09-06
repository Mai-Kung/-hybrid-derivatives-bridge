# Chart-pattern playbook: MARSCOIN (sustained), T (slow fade), 4USDT.P (fast crash), ZECUSDT.P (multi-leg continuation)

**Status: proposal, not backtested, not part of any live rule. n=4 symbols (MARSCOIN, T,
4USDT.P, ZECUSDT.P), several individual signal instances examined in detail across them — still
an illustration, not a statistic. Treat this exactly as cautiously as this whole document treats
a 1-2 case backtest anywhere else.**

Source: TradingView chart sets the trader shared (MARSCOIN/USDT.P and T/USDT.P, multiple
timeframes each, including one closer 15m look at T's full cycle), each showing a Buy→ride→Sell
cycle picked out by an on-chart signal tool, with
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
the interesting difference — see the closer look at T below for the part that is: the same
five points can fire on both a real signal and a false one, and the trend-strength gauge's
*slope* is what tells them apart.

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

## A closer look at T (15m, full cycle): a false signal and a risky re-entry

A more detailed T/USDT.P chart (15m, showing the whole cycle from before the rally to the
current dip) adds two more cases beyond the clean win/fade comparison above — both are about
**telling a good signal from a weak one using the same five indicators, not adding new ones.**

**Case 3 — the premature Sell that the rally overran.** Before the real rally, a "Sell" fires
while the oscillator is already down near its lower band (roughly -53) and the bottom
trend-strength gauge is still flat near zero. Price does not fall — it reverses almost
immediately into the big rally. **This is what a false signal looks like on this exact setup:
a Sell (or Buy) that fires while the trend-strength gauge has not yet turned is low-conviction,
even if the oscillator/MA-cross conditions technically align.** The winning Buy that follows
shortly after fires as the trend-strength gauge is visibly *lifting off zero* — that's the
tell that distinguishes it from the false Sell just before it.

**Case 4 — the late re-Buy while the trend gauge is still falling.** After the peak, price gives
back the whole rally and chops sideways, and a new "Buy" appears on the right edge as the
oscillator dips oversold again (~-40 to -53) — but the trend-strength gauge is still on its way
down (from a prior peak near 19 to about 11.7 at the Buy), not yet turned up. This is
structurally a **different, weaker kind of Buy** than the one that caught the original rally
(which fired as the gauge was rising from near zero): it's a bounce attempt inside a still-
weakening trend, not a fresh trend igniting. Both may satisfy the same 5-point BUY confluence
checklist — the oscillator and MA-cross can technically flip on a dead-cat bounce too — which is
exactly why the checklist alone is not sufficient without also reading the gauge's *slope*.

**The refinement this adds to the checklist:** grade every Buy/Sell signal by whether the
bottom trend-strength gauge is rising or falling at the moment the signal fires, not only by
whether price crossed it:

```
HIGH-CONVICTION signal: the trend-strength gauge is turning UP from a low base (or turning DOWN
  from a high base, for a Sell/short) at the same time the 5-point confluence fires. This is
  what preceded T's real rally and MARSCOIN's whole move.
LOW-CONVICTION signal: the trend-strength gauge is still moving in the OPPOSITE direction from
  the signal (falling on a Buy, rising on a Sell) when the confluence fires. This is what
  preceded T's premature early Sell and its risky late re-Buy. Treat these as smaller size, a
  tighter invalidation, or skip -- not equal-weight with a high-conviction signal.
```

## A third symbol: "4USDT.P" — the same Setup-B exit, but a fast liquidation-style crash

A third chart set (4/USDT.P, 1h/30m/15m) shows a different *speed* of the same distribution
pattern: price had been in a rising staircase (green step-line), then a Sell fires and price
craters **-27.7% in a very short window** — visually a single sharp leg, not T's slower
multi-candle fade. This looks like a leveraged liquidation cascade rather than an ordinary
momentum swing, and it's a cleaner, more dramatic version of the same exhaustion confluence:

- The trend-strength gauge was sitting at a **plateau near its top** (around 20) exactly at the
  Sell trigger, and rolled over sharply right after — the gauge peaking *at* the signal, rather
  than having visibly turned down beforehand, is still a valid high-conviction read: a flat top
  about to break is the leading edge of "turning down," not a reason to wait for confirmation
  that arrives after the move.
- The oscillator went from near its upper band (~60) to deeply negative (readings around
  -20 to -47 across the three timeframes) within the same short window — a much sharper
  rollover than T's, matching how much faster the price move was.
- The MA-cross line flipped bearish essentially at the Sell, then diverged hard and fast — no
  slow compression first, unlike a normal topping process.
- **No dip-buy signal has fired on the way down** (as of the last visible candle on any
  timeframe). This is worth noting on its own: the same signal system that produced T's
  premature early Sell and weak late re-Buy did *not* manufacture a buy signal here just because
  price fell a lot — it stayed quiet while the trend-strength gauge was still clearly declining,
  which is the correct "no trade" state, not a flaw.
- The 15m chart also shows an early Sell right before the original rally's Buy trigger — the
  same "false signal right before the real one" shape already seen on T, now observed on a
  **second, independent symbol**. That doesn't make it a proven pattern, but it's one more data
  point in the same direction rather than a one-off coincidence on T alone.

**What this adds to Setup B (distribution fade short):** the checklist works whether the
distribution plays out over many candles (T) or nearly all at once (4USDT.P) — the same five
conditions and the same gauge-plateau/rollover read applied to both. It also reinforces the
"don't manufacture a buy on every oversold reading during a still-declining gauge" caution: this
system correctly produced *no* signal on the way down here, where T's version did eventually
throw a low-conviction one. Whether that's because not enough time had passed or because the
downtrend was simply too strong to satisfy the BUY confluence yet isn't something one chart can
answer — logged as an open question, not a conclusion.

## A fourth symbol: ZECUSDT.P — sustained continuation on an established coin, no listing catalyst

A fourth chart set (ZEC/USDT.P, +14.4% on the day, 1h/30m/15m) is the cleanest single-symbol
illustration of the *whole* lifecycle in one place: a Buy trigger, three distinct legs up while
holding through two real pullbacks, and finally a Sell trigger exactly as the trend-strength
gauge breaks a long plateau — all on Zcash, an old, established coin with no fresh-listing
catalyst behind the move at all.

- After the Buy, price made three separate step-ups (visible as three plateaus in the rising
  step-line), each preceded by a genuine pullback where the oscillator and histogram both
  dipped hard — not just chopped sideways — before the next leg started.
- Through all three legs, the trend-strength gauge climbed fast to near its ceiling (~19.6-20)
  and **stayed there** across both pullbacks — it did not roll over during either interim dip,
  which is exactly why neither pullback should have been read as a full exit signal even though
  the oscillator/histogram briefly went negative each time.
- Only on the most recent candle, after the third leg, does the gauge finally start rolling over
  from that long plateau (30m: ~19.6 down to ~14.96; 15m: ~20 down to ~7.65) at the same moment a
  Sell fires — the textbook Setup B exhaustion trigger, arriving only after the plateau breaks,
  not during any of the earlier dips.

**What this adds:** MARSCOIN's "let it run" case had a verified news catalyst; this one doesn't,
and it still produced a genuine multi-leg continuation. **The gauge's persistence at or near its
ceiling through repeated pullbacks is itself evidence worth trusting, independent of whether a
formal catalyst exists** — catalyst verification (Rule N's N1) is one way to gain confidence a
pullback isn't the top in advance, but watching the gauge fail to roll over through two or more
genuine dips is a technical way to earn that same confidence in real time, on any symbol. This
refines Setup A's catalyst modifier: treat "gauge holds its plateau through a real pullback" as
an additional, catalyst-independent reason to trail rather than exit, not only a confirmed news
event.

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

- **n = 4 symbols.** One sustained move (MARSCOIN), one slow single-leg fade with a false early
  signal and a weak late re-entry (T), one fast liquidation-style crash with the same exhaustion
  shape and a matching false early signal (4USDT.P), one sustained multi-leg continuation on an
  established coin with no listing catalyst at all (ZECUSDT.P) is not a sample size, it's a
  slightly broader illustration. Every observation above, including the gauge-slope grading and
  the gauge-plateau-persistence read, is a description of a handful of charts, not a statistic.
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
