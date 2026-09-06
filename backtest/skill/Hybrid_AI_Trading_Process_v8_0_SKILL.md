---
name: hybrid-ai-trading
version: 8.0
effective_date: 2026-09-06
supersedes: >
  7.2 — Rule N and Rule F's live status, entries, stop-losses, and sizing are UNCHANGED
  byte-for-byte (still an override, still not a passed §6E/§6F). Q2/S entry geometry, the
  Participation-Ratio ladder, and every exclusion list are UNCHANGED. **What changed: Q2 and S's
  fixed +30%/-30% take-profit is replaced with an armed trailing exit** (arm once running profit
  >=20%, then exit if it gives back >=15 percentage points from its peak; hard SL and 72h
  time-stop unchanged), backtested against the same Jul-Aug 2026 data this lineage already uses.
  This is the one quantitative idea drawn from a three-way comparison of this skill, its own
  prior v6.6, and the separately-built momentum-confluence-playbook chart skill: the playbook's
  chart indicators cannot be tested against this screener data at all (different data source,
  already established), but its core lesson -- MARSCOIN's fixed-TP-would-have-capped-the-winner
  case, and momentum-confluence-playbook's ZEC-style "let a real trend run past one exit signal"
  finding -- translates directly into a mechanically backtestable Q2/S exit change, and it tests
  as a real, large improvement, not a marginal one (see §14).
status: >
  PILOT, same confidence tier as Q2/S's own PILOT-F status. The trailing exit is the only rule
  change in v8.0; Rule N and Rule F's live parameters (§13) and every entry gate (Q2/S/N/F) are
  untouched. On the same Jul+Aug 2026 backtest window used throughout this lineage, pooling every
  rule's trades sequentially at each rule's stated risk sizing: **v6.6 (Q2+S, fixed TP only, Rule
  N watch-only) = +32.15% total return; v7.2 (v6.6 + Rule F live) = +52.53%; v8.0 (Q2/S trailing
  exit + Rule F live, Rule N unchanged) = +97.71%, PF 2.77, max drawdown -2.94%.** That clears the
  trader's own "beat all three predecessor skills by >=20%" bar decisively (+86% over v7.2, +204%
  over v6.6) on the first tested design, not after multiple failed rebuilds -- stated plainly
  because that is unusual and worth being clear-eyed about, not because it should be trusted more
  for having arrived quickly. One caveat carried forward honestly, not smoothed over: 34.7% of
  the trailing-exit's own added gains come from a single trade (TUTUSDT.P) -- above this
  lineage's own 20%-concentration guideline. Removing it still leaves the new exit ahead of the
  old one (+39.05% vs +32.15% on Q2/S alone), so the mechanism is not purely one-trade-dependent,
  but n=85 Q2/S trades on one two-month window is the same order of evidence Q2/S itself started
  from (n=67, per Known Limitations) -- log it, watch it forward, do not treat it as finished.
description: >
  Hybrid AI Trading Process v8.0. Built from a trader-requested three-way comparison of this
  lineage's own v6.6, v7.2, and the separately-built momentum-confluence-playbook chart skill.
  The chart playbook's indicators cannot be backtested on this screener data (different data
  source), but its central, transferable lesson -- don't cap a real winner with a fixed
  take-profit, trail it instead -- is applied to the one place in this whole system it IS
  mechanically testable: Q2/S exits. Replacing the fixed +30%/-30% TP with an armed trailing exit
  (arm at +20% running profit, give back at most 15 points from peak) nearly doubles Q2/S's own
  two-month backtested return (+32.15% -> +71.29%) while improving profit factor (3.77 -> 6.58)
  and barely moving max drawdown, and lifts the whole system's pooled return past both v6.6
  (+32.15%) and v7.2 (+52.53%) to +97.71% -- a >=20% improvement over the better of the two, the
  bar the trader set before this could be saved as v8.0. Q2/S entry geometry, the PR ladder, Rule
  N/F's own entry definitions and live status (§13), and every exclusion list are otherwise
  untouched. Core rule unchanged: No Reason = No Trade. A backtested improvement is evidence
  worth adopting at the same confidence tier as what it replaced, not proof beyond that tier --
  this version says so plainly, including the one concentration caveat that did not disappear
  just because the headline number is good.
---

# HYBRID AI TRADING PROCESS v8.0 — Q2/S Trailing Exit (from a three-skill comparison)

**Role:** Professional Crypto Trader — Technical Analysis + Market Psychology
**Markets:** BTC & Altcoins | Binance Perpetuals
**Core:** `No Reason = No Trade` · missing evidence is not confirmation · no fabricated certainty.

---

## 0. Governance first — read before using

**Why v8.0 exists.** The trader asked directly: backtest this skill (v6.6), v7.2, and the
separately-built momentum-confluence-playbook chart skill against each other on the same
Jul-Aug 2026 data, take what's genuinely good from each, and only save the result as v8.0 if it
backtests at least 20% ahead of all three. §14 below is that comparison, run for real rather than
asserted. The short version: v6.6's Q2/S entry geometry is the cleanest, lowest-drawdown edge in
this whole lineage (PF 3.77 on its own); v7.2 added Rule F, a real but modest edge; the chart
playbook's own indicators are computed from OHLCV candles and are NOT present in this screener
data at all (established repeatedly in that skill's own text) — but its central lesson, stated
most sharply in its ZEC and MARSCOIN worked examples, is that a fixed take-profit caps a real
trend for no good reason, and a "trim/trail, don't hard-exit" rule captures more of a winner
without materially raising risk. That lesson does NOT require the playbook's chart indicators to
apply — it only requires *something* that measures "how far is this trade currently in my
favor," and Q2/S's own price path already provides that. §14 tests it directly.

**What changed and what didn't.** Rule Q2 and Rule S's own entry geometry, the Participation-
Ratio risk ladder (§2C), and every exclusion list are copied byte-for-byte from v7.2. Rule F's
mechanical definition (F1-F6, §8), Rule N's definition (N1-N6, §3), and both rules' live
stop-loss/sizing/status (§13) are ALSO unchanged from v7.2 — v8.0 does not revisit that override
decision at all. **The one change: Q2 and S's fixed +30%/-30% take-profit is replaced with an
armed trailing exit** (§14, §STEP 4) — hard SL and the 72h time-stop are untouched, only the
"what happens to a winning trade" branch changes.

**Why this is written down instead of just done.** Same reason every prior version in this
lineage writes down what changed and why: a backtested improvement is worth adopting, but it is
evidence at the same confidence tier as everything else here, not a promotion to a higher one.
Q2/S are still PILOT-F. The trailing exit inherits that same PILOT tier — it does not make Q2/S
"more done," it changes what "done" currently means for their exit rule, on the same amount of
evidence (n=85 trades, one two-month window) Q2/S themselves started from.

**What this version explicitly does NOT do.** It does not touch Rule N or Rule F's live status,
entries, or sizing (§13) — that override stands exactly as v7.2 left it, unrevisited here. It
does not claim the trailing exit passed a full admission test — §14 states its own concentration
caveat (one trade is 34.7% of its added gains) rather than hiding it. It does not claim the
momentum-confluence-playbook is now "backtested" — its indicators remain untestable on this data
source; only one transferable idea from it was extracted and tested on its own merits here.

---

## 1. Evidence — the MARSCOIN case study (verified)

Source data: `Mai_BI_2026-09-02_Combined.csv`, `Mai_BI_2026-09-03_Combined.csv`,
`Mai_BI_2026-09-04Time7_24.csv` (712-713 symbols/snapshot). All figures below were recomputed
directly from these files, not taken on faith from any prior write-up.

| Time (ICT) | Price | Open% | 24h% | 30m% | Vol 24h | Vol rank | 24h% rank | magnitude |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 09-02 06:34 | 0.06540 | −11.43 | n/a | −1.47 | $20.3M | — | — | 11.43 |
| 09-03 06:24 | 0.06298 | −5.36 | −4.94 | +0.70 | $92.2M | **56 / 713** | **670 / 713** | 5.36 |
| 09-03 09:03 | 0.06226 | −1.77 | −6.05 | +0.42* | $85.7M | 59 / 713 | 678 / 713 | 6.05 |
| 09-03 11:54 | 0.07944 | +25.34 | +9.52 | +3.69 | $96.8M | 22 | — | **25.34 → LV-Guard fires** |
| 09-03 15:11 | 0.11173 | +76.29 | +52.14 | +3.18 | $164.5M | 1 | — | blow-off, Auto-Skip continues |
| 09-03 20:46 | 0.11870 | +87.28 | +91.41 | +9.94 | $309.4M | 1 | — | Auto-Skip continues |
| 09-04 07:24 | 0.12111 | −5.96 | +93.76 | −5.74 | $533.3M | — | — | still >25% by 24h |

`1W%` and `1M%` are **null on every single row above, no exception** — confirmed by direct
`pandas` check across all 15 snapshots, not just eyeballed.

**`*` — data-integrity finding this write-up caught that a prior pass missed.** At 09-03 09:03,
MARSCOIN's 5m/15m/30m readings are `0.4193548387096827` three times, exactly identical. That looks
like real triple-timeframe confirmation but isn't: the **whole snapshot's** LTF triple-duplication
rate at that timestamp is **92.29%** (vs 1.68% at 06:24) — this is a snapshot-wide TradingView
export artifact, the same phenomenon v4.4's original P1 finding documented, and it means the
09:03 snapshot was in **DEGRADED-CONFIRM** territory session-wide, not a case of three independent
timeframes agreeing. Any rule reading LTF fields at that timestamp — Rule N and Rule F included —
must use `max(5m,15m,30m)` under the DEGRADED label and say so, not present three identical
numbers as triple confirmation.

**Root cause, verified from primary/near-primary sources:**
- MarsCoin entered the Binance Alpha pre-listing pool 2026-07-30.
- Binance's own futures notice: **MARSCOINUSDT perpetual, up to 20x leverage, trading began
  18:45 KST (16:45 ICT) on 2026-09-01** — this is why the earliest CSV row is 09-02 06:34 with no
  1W/1M history; the contract was under 14 hours old at that point.
- Binance's official spot-listing announcement (fetched directly): published 2026-09-04 10:15 UTC
  (17:15 ICT), spot trading live 13:00 UTC (20:00 ICT) same day; MARSCOIN carries a **Seed Tag**
  (Binance's own high-volatility/high-risk classification).
- Independent reporting (CryptoBriefing) describes Alpha→Futures→Spot as *"a recognizable
  playbook"* Binance has repeated — meaning this is not a one-off oddity, it is a pattern that can
  recur with other symbols.

**The near-miss, stated plainly.** At 09-03 09:03 — roughly 2h51m before magnitude crossed 25% —
every Rule Q2 condition **except** the 1M/1W trend-quality gate was already a clean pass: magnitude
6.05% (<8%), Open% −1.77% (inside −10/+4), volume $85.7M (≥$20M), vol ratio 0.87x (inside
0.5-2.0x), breadth 65.6% (≥35%), BTC 24h +0.43% (≥−0.5%). The setup was textbook "quiet bar inside
a forming trend." It failed for one reason only: the trend had no month of history to measure yet.

**Visibility gap, also verified.** At 06:24, MARSCOIN ranked **56th of 713 by volume** and
**670th of 713 by 24h%**. A Top-12 view sorted either way never surfaces it, even though $92M of
24h volume and a fresh D1 catalyst (Binance's own futures launch, <48h old at that point) were
both real and checkable at that exact moment.

**Postscript for Rule F (§7-§8 below).** Read as a Rule-F thought experiment rather than a
Rule-N one, MARSCOIN is a cautionary tale, not a confirming one: a naive "fade the pump" short at
09-03 11:54 (+25.34%), 15:11 (+76.29%), or 20:46 (+87.28%) would each have been run over by the
next squeeze higher before the position could plausibly be closed for a profit. This is a real,
dated illustration of exactly the tail risk the backtest's own worst trade (−111.8%) represents —
it does not settle the LV-Guard question either way on its own (n is effectively 1 for this
specific short-thesis reading of the case), but it is the right kind of evidence to keep
collecting, and the strongest plain-language argument in this document for why Rule F may not
size a position until a stop-loss scheme exists and is tested (§6F).

---

## 2. What did NOT change

Rule Q2 entry geometry (1M 40-100, 1W 0-60, prior-1W>0, magnitude<8%, Open% −10/+4, 30m≥+0.25 or
DEGRADED max, volume≥$20M, vol ratio 0.5-2.0x, breadth≥35%, BTC24≥−0.5%, 72h cooldown). Rule S
entry geometry, unchanged. The Participation-Ratio risk ladder (PR<0.20 → 0.50% risk,
PR≥0.20 → 1.60% risk). SL −10%/+10% and the 72h time-stop, unchanged. All exclusion lists (majors
whitelist, DB-Red, tokenized-equity list+heuristic, delisting block, LV-Guard ≥25%, 1W>150%
no-chase). The DEGRADED-CONFIRM data gate. BTC leader gates. Seven Views at exactly 12 rows each.
Thai-language, light-theme reporting. Rule N's (§3) and Rule F's (§8) own mechanical definitions
(N1-N6, F1-F6), and both rules' entire §13 live status/stop/sizing, are unchanged from v7.2 —
v8.0 does not touch either rule at all. **Every Q2/S/PR number here was tested across five to six
major version cycles and required a passed admission test before touching capital; Rule N and
Rule F skip that requirement by the v7.2 override, unrevisited here.**

**What DID change: only the "what happens when a Q2/S trade is winning" branch.** The fixed
+30%/-30% take-profit is gone, replaced by an armed trailing exit (§14, STEP 4). Nothing about
entering a Q2/S trade changed; nothing about the hard stop-loss changed; nothing about Rule N or
Rule F changed.

---

## 3. Rule N — New-Listing / Futures-Catalyst Radar (N6 revised v7.1, LIVE / PILOT since v7.2)

**Status: LIVE as of v7.2 (2026-09-06), by explicit trader override — NOT because §6E passed.**
§6E is still unsatisfied (n=12, fails its own concentration rule — §12.3). Entry mechanics,
stop-loss, and sizing are defined in §13. N1-N6 below are unchanged from v7.1.

```
N1  Official-catalyst freshness: an official exchange notice (Futures launch = D1, or
    Spot/Margin access = E1) dated within the last 72 real hours. Must be sourced live in
    STEP 1C (Binance Announcements / Binance Square first; corroborate with X/Reddit/Telegram);
    cite the primary notice, not an aggregator, whenever the primary notice can be found.
N2  Symbol has 1W% OR 1M% blank/null in the current snapshot (mechanical, read directly off
    the CSV — this is what makes it invisible to Rule Q2, not a judgment call).
N3  24h volume >= $50M (higher than Q2's $20M floor — deliberately more conservative because
    N is unvalidated; see §6E before treating this number as tuned).
N4  Open% between −10% and +8% (wider than Q2's −10/+4 on the upside, to also catch early
    expansion, not only pullback — untested threshold, logged as such).
N5  LTF confirmation, STEP-0-aware: check the snapshot's own LTF triple-dup rate first.
      NORMAL/ELEVATED (<70%): at least 2 of {5m,15m,30m} positive, and max(5m,15m,30m) >= +0.25%.
      DEGRADED (>=70%): state DEGRADED-CONFIRM explicitly; do not present identical LTF values
      as independent confirmation — treat them as one reading, not three.
N6  Not DB-Red, not delisting-flagged, AND passes an explicit tokenized-equity identity check
    that does NOT depend on 1W/1M being present (v7.1 revision — see §12): cross-check the
    Description field and ticker against known tokenized-stock issuers, and require manual
    identity confirmation before any first-pass alert is upgraded to Confirmed Watch. The old
    tokenized-equity heuristic (§2A, "price>$50 AND |1W|<8 AND |1M|<15") CANNOT fire here,
    because blank 1W/1M is what N2 selects for — it was structurally unable to catch a
    tokenized equity in exactly the population Rule N scans, and two of the twelve systematically
    logged v7.1 candidates (SK Hynix, Yushu Technology/UNITREE) turned out to be exactly that.
```

**Two-stage labelling (kept from the proposal this version is built on):**
```
N1-N6 all pass, first time seen        -> "Listing Radar Alert"
N1-N6 still pass on a later snapshot   -> "Confirmed Watch"
magnitude >= 25% at any point          -> LV-Guard fires exactly as it does for Q2;
                                           Rule N stops upgrading the alert, existing
                                           alert stays visible but tagged AUTO-SKIP-ACTIVE
```
Rule N never overrides LV-Guard, the ≥25% Auto-Skip, or the 1W>150% no-chase zone. Those exist
because of real backtested evidence (PF 0.83 / PF 0.81 across the lineage); Rule N has none yet.

**MARSCOIN would have produced, under Rule N, if it had existed on 2026-09-03:**
```
09:03  Listing Radar Alert — MARSCOIN | Fresh D1 catalyst (Binance Futures, ~40h old,
       primary notice) | Vol $85.7M | Magnitude 6.05% | Open% −1.77% | 30m +0.42%
       (session LTF triple-dup 92.29% -> DEGRADED-CONFIRM, reading treated as one signal)
       Not a Q2 trade: 1M/1W unavailable, no monthly-trend history exists yet.
11:54  magnitude +25.34% -> LV-Guard Auto-Skip. Alert frozen, no further upgrade.
```
**As of v7.0/v7.1 this was a reporting output, not a trade ticket.** As of v7.2, a 09:03-style
alert on a live symbol WOULD be a real entry (§13) — this exact case is why §12.3's caveat
matters live, not just academically: the MARSCOIN trade is what carried Rule N's entire
backtested edge, and there is no way to know in advance which alert is "the MARSCOIN one" and
which is one of the other eleven that, on their own, lose money.

**Explicitly out of scope for v6.6/v7.0:** a short-side equivalent for newly-listed symbols that
crash after launch. Crypto losers tend to rebound harder than winners continue (Han/Kang/Ryu,
cited below and already the reasoning behind Rule S's tighter risk cap) — a new-listing short
radar is a materially different, unvalidated bet and is not proposed here.

---

## 4. Reporting — an 8th, always-shown view

The existing Seven Views (Q2/S ranked screens, exactly 12 rows each) are unchanged. Rule N adds
**View 8 — New-Listing / Futures-Catalyst Radar**, shown whenever at least one symbol is carrying
a Listing Radar Alert or Confirmed Watch tag, regardless of where that symbol ranks by volume or
24h% among the other 700+ symbols. This view has no fixed row count — it lists what is currently
active, which may be zero rows on most sessions. This directly fixes the MARSCOIN visibility gap
(56th by volume, 670th by 24h% — invisible to any Top-12 sort).

Rule F (§8) adds a **ninth** view on the same always-shown basis: **View 9 — Fade-the-Pump
Radar**, listing the top chg_30m/30m% candidates that pass F1-F5. As of v7.2, View 8 and View 9
entries that also pass §13's live-entry checklist are tagged **"LIVE ENTRY (v7.2 override — see
§13)"** rather than "not a trade"; entries that fail any live-entry condition (cooldown, LV-Guard,
exclusions) stay tagged **Watch/Candidate only**. A symbol can appear in View 8 and View 9 in the
same session — a brand-new listing that is also spiking hard on the 30-minute clock — report both
tags plainly rather than merging them; they come from independent evidence bases (§1 vs §7) and
neither authorizes the other.

---

## 5. Known limitations of Rule N

- **n = 1.** MARSCOIN is the only event Rule N has ever been checked against. Every threshold in
  §3 (the $50M floor, the −10/+8 Open% band, the 2-of-3 LTF rule) is a reasonable starting guess,
  not a swept, plateau-tested parameter the way every Q2/S number is. Treat them as placeholders
  pending real data.
- **Survivorship risk is real and not measured.** MARSCOIN went up. Binance Alpha→Futures→Spot
  pipeline tokens do not all do that — some launch and bleed out. Rule N as built has no way yet
  to tell those apart in advance; that is exactly what the STEP 6E admission test exists to check
  before this becomes anything more than an alert.
- **N1 requires a live web search at report time** ("was there an official notice in the last
  72h") — this is a process dependency, not a pure CSV read, and it can fail silently if the
  search comes back empty. If N1 cannot be verified, do not label the catalyst VERIFIED-FRESH;
  fall back to FRESH-UNVERIFIED or NONE per the existing catalyst-freshness taxonomy and say so.
- **New-listing volatility is genuinely dangerous**, per Binance's own Seed Tag classification on
  this exact symbol. A Watch alert existing is not an argument for loosening N3/N4 or for
  promoting Rule N faster than §6E allows.
- **v7.2 note: this rule is now LIVE despite every limitation above being unresolved.** n=12 as
  of §12 (still short of the bar), and 11 of those 12 lose money on their own (§12.3, §13.2).
  Going live did not fix any bullet on this list — it accepted them as the price of the bet §13.2
  describes.

---

## 6. External principles used (Rule N specifically)

1. **Listing-event studies** in traditional and crypto markets generally find abnormal short-run
   returns cluster around exchange-access events (new listings, tier upgrades) — this is the
   academic basis for treating "just listed, high liquidity, official catalyst" as a distinct
   information state worth tracking, separate from trend-continuation momentum (which is what Q2
   already measures well).
2. **Crypto asymmetry** (Han, Kang & Ryu, cited in v6.5 §6) — the same reasoning that keeps Rule
   S's risk capped at 0.50% is the reasoning for keeping Rule N Watch-only: a freshly-listed,
   leveraged, seed-tagged token is closer to Rule S's risk profile than to Rule Q2's.
3. **Anti-overfit governance**, unchanged from every prior version: one profitable case explains
   nothing; plateaus are trusted, single-observation step functions are not (v6.5 §5-R1 already
   demonstrated this exact trap with the 1M-ceiling sweep).

---

## 7. Evidence — Altcoin Perpetual Pump-Fade Backtest (Jul 1 – Aug 31 2026)

Source data: the same `Mai_BI_YYYYMMDD_YYYYMMDD_Combined_FullMonth` screener export family as
§1, for the two full calendar months immediately preceding this version — 697 alt perpetuals
(every `*USDT.P` on Binance except `BTCUSDT.P`/`ETHUSDT.P`), 413 scan timestamps, roughly 6-7
scans/day. Recomputed directly from the raw files with `pandas`, not taken from a prior summary.

**Method.** At every scan, rank the liquid alt universe (24h volume ≥ $1,000,000) by 30-minute
price change (`30m%` / `chg_30m`). Short the ten biggest positive movers, equal-weighted, no long
leg. Hold each name to its own next scan (median gap ≈3h; a pair whose gap exceeds 8h —
delisting, data hole — is dropped rather than held through). Rotate the whole basket every
period. Cost assumption: 5bps per leg (taker + slippage), charged once per trade.

**Why this specific config, not the highest-Sharpe one found.** A full grid search across seven
signals (`5m/15m/30m/Open%/24h/1w/1m` change), five basket sizes (N=5/10/15/20/30), both momentum
and reversion framings, and three sides (long-only/short-only/long-short) was run separately on
July and on August. The single best July-only Sharpe (12.19, `chg_30m`/momentum-framed/N=5/
short-only) returned **+512% in July and −55% the very next month** — a textbook overfit basket:
N=5 is dominated by one or two names a period, and July's number was largely noise. This document
already carries the right epigram for this exact failure mode (§6, "the highest-return parameter
set is usually the most overfit one"); the July/August comparison is a second, independent
demonstration of it. The config reported below was instead chosen by requiring **N≥10** (enough
names per basket that one outlier cannot dominate it) and the **minimum of July's and August's
Sharpe** (not July's alone) — i.e., the config had to hold up in both months, not just the one it
was fit on.

**Results (`chg_30m` / N=10 / reversion-framed / short-only):**

| Period | Periods | Total return | Ann. Sharpe | Max drawdown | Win rate |
|---|---|---|---|---|---|
| July (in-sample) | 206 | +72.8% | 5.07 | −22.0% | 54.9% |
| August (out-of-sample) | 195 | +100.7% | 7.67 | −23.3% | 59.5% |
| Combined | 401 | +246.7% | 6.15 | −23.3% | 57.1% |

Weekly: 8 of 10 calendar weeks positive; one outsized +70.1% week (2026-08-16) and one losing
week (2026-07-05, −14.8%) at the very start of the sample — not a single lucky week carrying the
whole result, but the +70.1% week alone is large enough that §6F requires re-checking
profitability with it removed before this can be trusted further.

**Cost sensitivity:** the edge survives 5→20bps/leg comfortably, thins sharply by 30bps, and
breaks even between roughly 30-40bps. Binance perp taker fees run ≈4-5bps; realistic slippage on
a name that just spiked 30% in 30 minutes can plausibly exceed that on size, so this is a real,
not theoretical, constraint.

**Liquidity sensitivity:** re-run at 24h-volume floors of $5M, $20M, and $50M, the edge holds
(Sharpe 4.96 / 5.04 / 2.88 respectively) — this is not purely a micro-cap-illiquidity artifact,
though it does thin out at the most liquid end of the universe.

**The one number that matters most for governance: worst single trade = −111.8%.** A short
position's downside is unbounded; this basket, on this data, produced at least one leg that lost
more than the entire notional through a violent short squeeze. The backtest's aggregate Sharpe
and total return are real, but they are basket-average numbers that absorbed that squeeze inside
nine other legs performing normally that period. A single-name discretionary version of this
trade has no such cushion. **No stop-loss was modeled anywhere in this study.**

**What was NOT tested, stated plainly:**
- Funding rate (not in the source data at all). During a pump, funding is usually positive
  (longs pay shorts) — a plausible tailwind for this exact trade, unquantified here.
- This process's own, broader Majors Whitelist (§2A) — the backtest excluded only
  `BTCUSDT.P`/`ETHUSDT.P`, not the full list this process already excludes from Q2/S. Re-running
  with the full whitelist excluded is a prerequisite for §6F, not an optional nice-to-have.
- Single-name selection, entry slippage on one order, or any stop-loss/take-profit scheme — the
  study is basket-average only (see §8 for why this matters for how Rule F may be executed).
- Any period besides these exact two months, which were alt-heavy and volatile (many +50–400%
  "change from open" prints in the raw data) — a calmer or trending-down regime is untested.

---

## 8. Rule F — Fade-the-Pump Discretionary Short (F1-F6 unchanged, LIVE / PILOT since v7.2)

**Status: LIVE as of v7.2 (2026-09-06), by explicit trader override — NOT because §6F passed.**
§6F is still unsatisfied: profit factor on the live-sizing backtest is 1.45, below this process's
own 1.50 bar, and the only new out-of-sample test (September) lost money (§11.2). Entry
mechanics, stop-loss, and sizing are defined in §13. F1-F6 below are unchanged from v7.0/v7.1.

Unlike every other rule in this lineage, Rule F's entry trigger is a **large existing move**, not
an absence of one — the thesis is fading a spike, not confirming a trend. This is a structural
difference from Q2/S/N and must be stated plainly every time Rule F is reported.

```
F1  Universe: this process's full Majors Whitelist (§2A) excluded, plus DB-Red, tokenized-equity,
    and delisting-flagged names excluded — the same identity checks as N6. NOTE: the backtest in
    §7 only excluded BTCUSDT.P/ETHUSDT.P, a narrower exclusion than this process's own whitelist.
    Re-running §7's numbers with the full whitelist excluded is required before §6F can pass.
F2  24h volume >= $1,000,000 (backtested robust from $1M to $50M; treat $1M as a floor, not a
    validated optimum).
F3  Rank the eligible universe by 30m%/chg_30m, descending.
F4  No Open%/magnitude ceiling, and explicitly NO LV-Guard Auto-Skip: a magnitude >=25% move
    that would block a fresh Q2/N long is, for Rule F, part of the setup, not a reason to stand
    down. This is the opposite use of magnitude from every other rule here and is exactly why
    §6F requires it to be tested directly rather than assumed either way.
F5  Not DB-Red, not tokenized-equity, not delisting-flagged (redundant with F1's exclusions;
    kept explicit for the execution checklist).
F6  Report the session's LTF triple-dup rate (STEP 0) alongside every Rule F candidate for
    context; chg_30m is itself the primary signal, so DEGRADED status does not gate entry the
    way it does for Q2/S/N, but it must still be stated.
```

**Two execution modes — do not conflate them:**

```
Systematic-Basket mode (what §7 backtested): open all ~10 names passing F1-F3 as equal-weight
shorts every scan, rotate fully at the next scan (~2-4h later), whole-basket risk only, no
per-trade stop-loss. This is the mode with the two-month walk-forward evidence in §7. It is NOT
what v7.2 authorizes -- it would need its own systematic sub-book, sized and risk-capped
separately, and that sub-book is still unbuilt. Do not run this mode live.

Discretionary-Single-Trade mode (the mode v7.2 authorizes, §13): take the single highest-ranked
F1-F6 candidate as one Rule F short, stop-loss 20%, sized to risk 0.50% of equity. This mode's
own live-sizing backtest (§11, §13) is the ONLY evidence behind this trade -- §7's basket numbers
are motivating context, not this mode's own track record, and the single-trade PF (1.45) is
lower than the basket's.
```

**Reporting and execution, per §13:**
```
F1-F6 all pass, live-entry checklist (§13) also clear -> LIVE ENTRY, sized per §13
F1-F6 pass but a live-entry condition fails (cooldown, LV-Guard, exclusion) -> "Fade-the-Pump
  Candidate" in View 9 (§4), watch only
magnitude crossing 25%  -> stated, not auto-skipped (see F4) -- report the crossing plainly as
                            context, since it is part of the F4 thesis, not a block
```

**Explicitly out of scope for v7.0:** any long-side use of this signal (fading a crash upward,
i.e. buying the biggest 30-minute losers) — the backtest tested long-only and long-short variants
of every signal and none outperformed short-only fading; see §7's grid-search note. A crash-fade
long is not proposed here and would need its own separate study.

---

## 9. Known limitations of Rule F

- **Backtest evidence is single-trade sequential (§11, §13) but still a snapshot-resolution
  proxy, not a real intrabar fill simulation.** The −111.8% worst-single-leg loss (identified in
  §11.4 as `EVAAUSDT.P`) shows the tail risk is real; the 20% stop caps it in the backtest, but
  whether a live stop fills anywhere near 20% on a name mid-squeeze is untested.
- **Universe mismatch: RESOLVED (§11.1).** Full Majors Whitelist re-test barely moved the
  numbers. This bullet is kept only as a record that it was checked, not as an open item.
- **Two-and-a-bit months, one regime, and the newest slice lost money.** §7's Jul-Aug window plus
  §11's September extension is still one continuous alt-heavy, volatile stretch — and the part
  added after v7.0 (September) was a loss (§11.2). Untested in a calm or trending-down market.
- **Funding rate unmodeled.** Plausibly a tailwind (shorts often collect funding during a pump);
  unquantified, so not to be assumed in either direction when sizing.
- **LV-Guard's role is tested but not resolved (§11.3).** Applying it roughly halves return and
  drops PF below 1.50, while also cutting the worst trade by more than half. v7.2 keeps F4's
  original no-LV-Guard design; the trade-off is documented, not eliminated.
- **v7.2 note: this rule is now LIVE at a profit factor (1.45) below this process's own 1.50
  admission bar (§13.1).** Going live did not raise that number — it accepted it.

---

## 10. External principles used (Rule F specifically)

1. **Short-horizon return reversal** is a long-documented phenomenon in traditional markets —
   Jegadeesh (1990) and Lehmann (1990) both find that very recent (weekly-or-shorter) winners
   tend to underperform, and recent losers tend to outperform, over the following short window —
   the opposite sign from the multi-month momentum Q2 already trades. Rule F's 30-minute-horizon,
   short-only design is this process's own empirical finding in the crypto-perpetual context, not
   a direct replication of either paper's exact horizon or asset class — cited here as the
   academic reason a reversal effect at some short horizon is plausible at all, not as proof this
   specific parameterization is correct.
2. **Crypto asymmetry** (Han, Kang & Ryu, cited in v6.5 §6 and reused for Rule N in v6.6 §6) — the
   same reasoning that keeps Rule S capped at 0.50% risk applies with at least equal force to
   Rule F: a leveraged short into a name that just moved 25%+ in a single scan is a materially
   more dangerous position than a Q2 long into a confirmed monthly trend.
3. **Anti-overfit governance**, unchanged from every prior version and reconfirmed by this
   version's own evidence: the naive best-July-Sharpe config in §7 lost more than half its value
   the very next month. Plateaus (robust across both months, N≥10) are trusted; single-month step
   functions are not — the same lesson v6.5 §5-R1 already taught with the 1M-ceiling sweep, and
   now taught a second time by this exact backtest.

---

## 11. v7.1 deep-dive — Rule F (universe, LV-Guard, and a real out-of-sample warning)

Source data: the same July/August files as §7, plus three new snapshots
(`Mai_BI_20260902_Combined.csv`, `...20260903...`, `...20260905...` — 2026-09-04 is missing, a
1-day gap between the 09-03 and 09-05 files). This section was requested directly: find ways to
improve Rule F and maximize profit. The honest result is that it did not find one, and it found
a reason for more caution instead. Full detail and reproducible code:
`backtest/rule_f_v71_analysis.py`, `backtest/V71_FINDINGS.md`.

**11.1 — Full Majors Whitelist re-test: the edge is not a universe artifact.** §7's backtest
excluded only `BTCUSDT.P`/`ETHUSDT.P`; re-run against this process's full §2A whitelist
(22 names excluded instead of 2): July +72.4% (was +72.8%), August +102.7% (was +100.7%),
combined +249.4% (was +246.7%), Sharpe 6.18 (was 6.15). Essentially unchanged — one §6F
prerequisite is now satisfied.

**11.2 — September: a real losing stretch, not explained away.** Added as a third,
independent-if-tiny out-of-sample slice (17 periods over 4 discontinuous days): **−11.5% total
return, Sharpe −9.34, 35.3% win rate.** This window overlaps the MARSCOIN squeeze (§1) — several
Rule F candidates were themselves mid-parabola, the exact tail-risk mechanism §7 already
identifies. n=17 is too small to be conclusive on its own, but it is the one clean new
out-of-sample test run since v7.0, and it lost money. This raises, rather than lowers, the bar
for §6F's "≥3 additional independent months" requirement.

**11.3 — LV-Guard (F4), tested directly instead of left a hypothesis.** Single-trade
discretionary mode, stop=15%/risk=0.50% (the §9 candidate scheme), full Jul+Aug+Sep:

| Variant | Total return | Profit factor | Worst trade |
|---|---|---|---|
| No LV-Guard (current F4 design) | +26.0% | 1.61 | −111.8% |
| LV-Guard applied (magnitude≥25% excluded) | +11.1% | 1.35 (fails §6F's 1.50 bar) | −47.3% |

Applying LV-Guard roughly halves total return and drops PF below the admission bar, but also
cuts the worst-case loss by more than half. This is a genuine trade-off the trader must decide
on — recorded as tested evidence, not resolved either way by the data alone.

**11.4 — the worst trade, identified.** `EVAAUSDT.P`, entered 2026-07-12, magnitude **80.2%**
already at entry — Rule F shorted a name already deep into a blow-off, which then roughly
doubled again (−111.8%). This is precisely what 11.3's LV-Guard variant would have skipped. The
#2 worst trade was `TACUSDT.P` (−57.3%) — the same symbol §2A already flags as "proposed for
permanent DB-Red addition; currently auto-blocked by LV-Guard only." Independent corroborating
evidence for that still-pending flag.

**11.5 — what did NOT improve profit.** Larger baskets (N=15: +84.9%/Sharpe 3.73; N=20:
+57.4%/Sharpe 3.30) both underperform N=10's +209.3%/Sharpe 5.33. Capping extreme `chg_30m`
signal values (>50%) changed nothing — EVAA's own entry signal was a normal-looking 10.3%; the
real tail-risk driver is `magnitude`, not the 30-minute signal, confirming 11.3/11.4 as the
right lever. Excluding sub-cent prices (<$0.001) had a negligible effect. None of these beat the
original N=10 config.

## 12. v7.1 deep-dive — Rule N (systematic backtest, n=1 → n=12, and why that still isn't enough)

A systematic mechanical pass (N2 blank 1W/1M, N3 vol≥$50M, N4 Open% −10/+8, N5 LTF-aware
momentum, N6 DB-Red only at the time of the pass — see 12.1) across the full July–September
dataset found **12 distinct "Listing Radar Alert" events**, up from the single MARSCOIN case.
N1 (an official catalyst within 72h) cannot be checked mechanically; each event below is
N1-UNVERIFIED unless stated otherwise. Full table: `backtest/results/rule_n_events.csv`;
reproducible code: `backtest/rule_n_systematic.py`.

**12.1 — two of twelve are false positives, verified by live search — the N6 fix.**
`SKHYUSDT.P` (alert 2026-07-13) is **SK Hynix (SKHYB)**, a tokenized-stock listing Binance
announced for spot trading that same day. `UNITREEUSDT.P` (alert 2026-08-20) is **Yushu
Technology / UNITREE**, a tokenized-equity perpetual (a robotics-company stock), also not a
crypto listing. Neither should ever have produced a Listing Radar Alert. The root cause: the
existing tokenized-equity heuristic (§2A) needs 1W/1M values to evaluate, and blank 1W/1M is
exactly N2's trigger — the heuristic was structurally unable to fire for the population Rule N
scans. §3's N6 is revised in this version to require an identity check that does not depend on
1W/1M being present.

**12.2 — one new genuine case, independently verified.** `NIULAIUSDT.P`: Binance Futures listed
the NIULAI perpetual 2026-08-30 11:30 UTC (a Binance Alpha token); the alert fired 2026-09-02,
inside the 72h N1 window — a second real, verified case alongside MARSCOIN. Its forward return
was modest and mixed (+4.3% at +2h, −12.2% at +6h, −6.2% at +24h) — nothing like MARSCOIN's
blow-off, and a useful reminder that most genuine new-listing catalysts probably look like this,
not like MARSCOIN.

**12.3 — the headline number, and why it still fails the admission test.** Forward returns,
n=12 (N1 unverified for the other 10):

| Horizon | Win rate | Avg return | Profit factor |
|---|---|---|---|
| +2h | 41.7% | −0.05% | 0.94 |
| +6h | 41.7% | −0.07% | 0.98 |
| +24h | 58.3% | **+6.18%** | **3.03** |

The +24h line looks like an edge until §6E's own concentration rule is applied: **MARSCOIN alone
is 75.4% of total positive result at +24h (80.4% after removing the two tokenized-equity false
positives).** Remove it, and the average +24h return flips to **−0.84%** and PF drops to
**0.75** (unprofitable). Tripling the event count from 1 to 12 did not change the underlying
conclusion — Rule N's apparent edge is still, in substance, one case. n=12 also remains well
short of the ≥20-30 bar regardless of concentration.

**12.4 — bottom line.** What changed is the quality of the "no": from "we haven't checked" to
"we checked, and here is exactly what's missing and why." Rule N gained an 11x larger event log,
one real methodology fix (12.1), one new verified case (12.2), and a concentration-test failure
that explains precisely why n=12 still isn't evidence of an edge (12.3). §11-§12 are preserved
here exactly as written before the override in §13 below — this is what was known at the time
the trader chose to go live anyway.

---

## 13. v7.2 — Live authorization for Rule N and Rule F (override, not a passed admission test)

**This section is what actually changed in v7.2.** Everything above (§0-§12) is unedited
evidentiary record. Kikuji — or whoever holds trading authority over this account — instructed
directly: convert both rules to live trading, stop-loss 20%. That instruction is implemented
below, exactly as given, with the numbers it implies stated plainly rather than smoothed over.

### 13.1 — Rule F (short), live parameters

```
Entry    : the single highest-ranked candidate passing F1-F6 (§8) at any scan, subject to the
           same cooldown/exclusion/DEGRADED-CONFIRM handling as every other rule.
Side     : SHORT (fade the pump) -- unchanged thesis.
Stop-loss: 20% adverse move (price up 20% from entry) -- AS INSTRUCTED. Wider than the 15%
           candidate in RULE_F_RISK_DESIGN.md; re-tested at 20% specifically for this version
           (backtest/rule_f_v71_analysis.py, extended).
Take-profit: none fixed -- exits by rotation (a better-ranked candidate appears at the next
           scan) or a 24h hard time-stop, whichever comes first. Rule F's thesis is a fast
           reversion, not a target price; a fixed TP was never part of any tested version.
Size     : risk 0.50% of equity per trade -> notional ~2.5% of equity (0.50% / 20%).
```

**What this is backtested to do** (Jul-Sep 2026, full Majors Whitelist, single-highest-ranked
candidate per scan, sequential, real position sizing): **total return +15.4% over that ~2-month
window, profit factor 1.45, max drawdown -3.3%, win rate 59.6%.** State plainly: **1.45 is below
this process's own 1.50 admission bar (§6F)**, and this number already contains the September
losing stretch (§11.2). The 20% stop (vs the 15% candidate) trades some upside for a wider berth
against the intra-period noise the backtest can't see (§9) -- untested which way that nets out
live.

### 13.2 — Rule N (long), live parameters

```
Entry    : the first Listing Radar Alert (N1-N6 all pass, §3), same exclusion/DEGRADED handling.
Side     : LONG -- unchanged thesis (new-listing catalyst).
Stop-loss: 20% adverse move (price down 20% from entry) -- AS INSTRUCTED.
Take-profit: none fixed. A 30%-TP variant was tested and REJECTED for live use: it would have
           capped MARSCOIN's trade at +30% instead of the +288% a 72h hold captured, and this
           rule's entire backtested edge comes from letting exactly that kind of trade run.
           72h hard time-stop backstops the hold if neither the stop nor a manual exit triggers.
Size     : risk 0.50% of equity per trade -> notional ~2.5% of equity (0.50% / 20%).
```

**What this is backtested to do** (all 12 logged events, §12, simulated with these exact
entry/stop/time-stop rules): **profit factor 5.72, average trade +21.1%.** Say the rest of it in
the same breath, every time this number is quoted: **that result is one trade.** Remove
MARSCOIN, and the other eleven average **-3.2% per trade, profit factor 0.34** -- a losing
system on its own. Trading Rule N live means betting that a similar MARSCOIN-sized catalyst
recurs often enough, in a universe of ~700 symbols scanned a few times a day, to be worth
absorbing eleven small losses while waiting for it. That bet may be reasonable -- new-listing
catalysts are a real, recurring phenomenon (§6.1) -- but it is a bet on a *base rate*, not on
this backtest's Sharpe ratio, because this backtest has no base rate in it yet (n=12, one hit).

### 13.3 — What did NOT change because of this override

- STEP 6E and STEP 6F (below) are UNCHANGED and still show every unmet checkbox. Going live did
  not check any of them off. A future version that wants to claim Rule N or Rule F "earned"
  Production status still has to clear the same bars this version explicitly skipped.
- Every exclusion list, LV-Guard's ≥25% Auto-Skip on Q2/S, the DEGRADED-CONFIRM data gate, and
  the 72h cooldown apply to Rule N and Rule F's live entries exactly as they do to Q2/S.
- Kelly sizing is still not used for either rule (STEP 4) -- 0.50%/trade is a fixed, conservative
  size chosen because neither rule has the closed-trade history Kelly requires, not because
  Kelly was computed and this is its output.
- Position sizes above (2.5% notional each) are small deliberately: at 20% stop and 0.50% risk,
  a full string of ordinary bad luck on either rule costs low single-digit percent of equity
  before a reassessment is forced, not a catastrophic loss on the first trade.

---

## 14. v8.0 — a real three-skill comparison, and the one change it earned

The trader asked for three things in one instruction: backtest this skill (v6.6), v7.2, and the
separately-built momentum-confluence-playbook chart skill against each other; take what's
genuinely good from each; and only save the result as v8.0 if the backtest beats all three by
>=20%. This section is that comparison, run for real on the Jul-Aug 2026 screener data (the same
two full months §7/§11 already use), not asserted from memory. Code:
`backtest/rule_q2s_backtest.py` (Q2/S mechanical backtest -- **the first time in this repo's
history Q2/S have been backtested at all**, rather than carried forward on the claim that they
were tested in an earlier version cycle) and `backtest/rule_q2s_trail_variant.py` (the trailing-
exit candidate below).

**14.1 — what each of the three actually contributes, tested honestly.**

```
v6.6 (Q2+S mechanical entries, fixed TP; Rule N watch-only, contributes $0):
  n=85 trades (58 Q2 long, 27 S short), win rate 68.2%, PF 3.77, max drawdown -1.35%
  realistic total return (0.50% risk / 10% stop sizing, pooled sequential): +32.15%
  This is a clean, low-drawdown edge that has simply never been quantified in this repo before
  now -- every prior version *claimed* Q2/S were tested across five to six cycles, but no script
  in this repo had actually run them against this data until this comparison.

v7.2 (v6.6's Q2/S unchanged, + Rule F live): pooled total return +52.53%, PF 2.06, maxDD -2.94%.
  Rule F is a real, modest edge (+15.4% on its own, PF 1.45) layered on top of Q2/S's stronger one.
  Rule N contributes $0 in this window too -- MARSCOIN and every other logged Rule N event are
  September-or-later; there is no Rule N trade inside the Jul-Aug comparison window at all.

momentum-confluence-playbook v3 (chart-pattern skill): CANNOT be backtested against this data.
  Its five panels (step-line, oscillator, MA-cross, histogram, trend-strength gauge) are computed
  from TradingView OHLCV candles on a charting platform -- a different data source than the
  Mai_BI_* screener exports this whole backtest suite runs on, and that gap was already
  established and restated every time that skill has been touched. It contributes zero backtested
  trades to this comparison, by construction, not by a weak result -- there is no result to
  measure. What it DOES contribute is a testable idea (14.2), which is not the same claim as
  saying the playbook itself is now validated -- it still is not, and remains a separate,
  discretionary chart tool.
```

**14.2 — the one idea that survived contact with real data.** The playbook's MARSCOIN worked
example argues that a fixed take-profit caps a real trend for no good reason (a 30% TP would
have capped MARSCOIN's +288% move); its ZEC worked example generalizes this further: a trend
that keeps proving itself (gauge holding its plateau through real pullbacks) should be trailed,
not exited, at the first sign of exhaustion. Neither example's *indicator* is available here, but
the *lesson* -- don't cap a winner with one fixed number, trail it once it's proven itself -- only
needs a way to measure "how far in-the-money is this trade right now," which Q2/S's own price
path already provides. Tested directly: replace Q2/S's fixed +30%/-30% TP with an armed trailing
exit -- SL -10%/+10% and the 72h time-stop stay exactly as they are; once a trade's running
favorable move reaches +20%, arm a trail that exits if the position gives back more than 15
percentage points from its own peak; otherwise let it ride to the 72h time-stop.

```
                          n    total_return   PF     maxDD    win_rate   exit reasons
Fixed TP (baseline)      85    +32.15%       3.77   -1.35%    68.2%     TIME 58 / SL 15 / TP 12
Trailing exit (v8.0)     85    +71.29%       6.58   -1.51%    68.2%     TIME 58 / SL 15 / TRAIL 12
```

Same 85 trades, same entries -- only the winning-trade exit changed, and total return more than
doubled while PF *improved* and max drawdown moved by 0.16 points. This is not a knife-edge
result: arm/giveback pairs from (10%/6%) through (30%/20%) all land in a +60-72% plateau (nearest
neighbors: 15%/12% -> +67.6%, 20%/10% -> +65.6%, 25%/15% -> +72.1%), the same "trust a plateau,
distrust a single spike" standard this lineage already applies to Q2/S's own parameters (v6.5
§5-R1) and to Rule F's basket size (§11.5).

**14.3 — the concentration caveat, stated as plainly as every other one in this document.** One
trade, TUTUSDT.P (a Q2 long, exited via TRAIL after a +463.9% gross move), is **34.7% of the
trailing exit's total positive result** -- above this lineage's own 20%-single-symbol guideline
(§6E, §6F, §11.5's own standard). Remove it: the trailing exit still returns **+39.05%** (PF
4.30) on the remaining 84 trades, which is still ahead of the fixed-TP baseline's own +32.15% (and
ahead of the fixed-TP baseline's own best-trade-removed number, +28.23% -- its own top contributor,
SYNUSDT.P, was a smaller 7.9% of its result). So the mechanism is not purely one-trade-dependent
-- it would have been a real, if smaller, improvement even without TUTUSDT.P -- but one very
large winner is doing real work here, and that is stated rather than buried, exactly the way
MARSCOIN's own concentration is stated for Rule N (§12.3).

**14.4 — the combined system number that answers the trader's actual question.** Pooling every
rule's trades sequentially by exit/entry time, at each rule's own stated risk sizing, across the
same Jul-Aug 2026 window:

```
v6.6 (Q2+S fixed-TP, Rule N watch-only)          : +32.15%
v7.2 (v6.6 + Rule F live)                        : +52.53%   (+63.4% vs v6.6)
v8.0 (Q2+S trailing exit + Rule F live)          : +97.71%   (+86.0% vs v7.2, +204% vs v6.6)
```

+86% ahead of v7.2 and +204% ahead of v6.6 both clear the trader's ">=20% better than all three"
bar by a wide margin, on the first design tested -- not after a rejected first attempt. That
speed is stated plainly rather than treated as extra confidence: it happened because Q2/S had
never actually been backtested in this repo before (§14.1), so there was real, previously-uncounted
edge sitting in the exit rule alone, not because this process has become better at finding edges
in general. Rule N and Rule F are unchanged and carry every caveat already on record for them
(§5, §9, §13); the trailing exit carries its own new one (§14.3); nothing here is asserted more
confidently than the data supports.

---

# STEP 0 — HARD DATA INTEGRITY GATE

```
□ File/timestamp/row count sane; duplicates removed and flagged.
□ BTC/ETH/SOL/BNB present and price-synced.
□ W1 mirror integrity checked (>85% match = CORRUPTED, exclude View 5 and flag).
□ LTF triple-duplication rate: <50% NORMAL · 50-70% ELEVATED · >=70% DEGRADED-CONFIRM.
  This rate is SESSION-WIDE — compute it once per snapshot and apply it to Q2, S, Rule N, AND
  Rule F alike. Do not let a single symbol's identical 5m/15m/30m values read as "confirmed"
  without checking whether the whole snapshot is DEGRADED first (see §1 MARSCOIN 09:03 case).
□ NORMAL long Q2 uses 30m >= +0.25%; DEGRADED uses max(5m,15m,30m) >= +0.25%.
□ NORMAL short S uses 30m <= -0.50%; DEGRADED uses min(5m,15m,30m) <= -0.50%.
□ NORMAL Rule N uses 2-of-3 LTF positive + max>=+0.25%; DEGRADED treats the LTF reading as one
  signal, not three, and states DEGRADED-CONFIRM plainly next to the alert.
□ Rule F reports the session's LTF triple-dup rate alongside every candidate (F6) but does not
  gate entry on it — chg_30m is itself the primary signal, not a confirmation of another one.
□ Prior observation >=2 real hours before now exists.
□ >=3 prior observations exist for the volume-ratio baseline.
□ BTC row exists — required for both leader gates. Missing BTC = NO FRESH ENTRY.
□ Monday weekly-rollover artifact checked before using prior-1W persistence.
□ 1M% != 0 for every Q2 candidate before computing PR (division guard).
□ New-symbol check: any symbol with 1W% AND/OR 1M% blank is automatically ineligible for Q2/S
  (structural, not a soft filter) and is routed to Rule N evaluation instead. State this plainly
  in the report rather than letting the symbol silently disappear from the session output.
□ Rule F needs only 30m% and 24h volume — a blank 1M/1W (the same MARSCOIN-shaped gap that
  routes a symbol to Rule N above) does NOT exclude it from Rule F. State both the Rule N and
  Rule F eligibility separately for any symbol missing 1M/1W, rather than checking only one.
```
A data-quality problem degrades only the field it affects. It must never silently manufacture
confirmation.

# STEP 1 — MARKET OUTLOOK

Report breadth and regime; BTC/ETH/SOL/BNB structure; the BTC 24h leader gate reading;
a 24-48h Binance Square / X / Reddit / Telegram scan as context only; macro calendar;
catalyst taxonomy F1/E1/D1/P1/S1 with freshness; reflexivity lifecycle label.

**1C addition for Rule N:** when a symbol is flagged under STEP 0's new-symbol check (1W/1M
blank), the social/catalyst scan step also searches specifically for an official exchange notice
(Binance Announcements first) covering that symbol within the last 72h, to evaluate N1. This is
the one place in the whole process where the social scan feeds a mechanical gate rather than
staying purely informational — and it only ever feeds Rule N, never Q2 or S, and it can only ever
produce a Watch alert, never a trade. Rule F has no equivalent step: F1-F6 are all mechanical
CSV/session reads, with no social-scan dependency.

Social attention never overrides a failed mechanical rule for Q2 or S.

# STEP 2 — SCREENING

## 2A. Exclusions — applied before any scoring

Majors whitelist runs BEFORE the tokenized heuristic:
`BTC ETH BNB SOL BCH LTC XMR ZEC AAVE TAO YFI QNT HYPE MKR COMP EGLD DASH XRP ADA AVAX LINK DOT`

DB-Red permanent block:
`BEAT DRIFT ESPORTS LAB RESOLV SIREN VELVET BLESS TRADOOR PORTAL`

Tokenized-equity / non-crypto explicit list (v4.4's 141 + ADBE BTCDOM PAXG XAUT) — unchanged.

Heuristic for newly appearing tokenized names:
`price > $50 AND |1W| < 8 AND |1M| < 15 -> manual identity verification before crypto scoring`.

Also: announced delisting → block; `magnitude = max(|Open%|,|24h%|) >= 25%` → fresh-entry
Auto-Skip (applies to Q2, S, and Rule N alike — **explicitly NOT applied to Rule F**, see F4);
long no-chase `1W > 150%`; ticker collisions resolved from the Description column.

**Open governance flags carried from v6.3/v6.5, still unresolved and still NOT silently applied:**
- **BMNR** (Bitmine Immersion Technologies, tokenized NYSE equity) passes every mechanical filter
  because its price sits below the $50 heuristic threshold. Hard-exclusion is proposed and
  **pending Kikuji's written approval.**
- **TAC** proposed for permanent DB-Red addition; currently auto-blocked by LV-Guard only.

## 2B. Rule Q2 — LONG entry geometry (UNCHANGED from v6.2/v6.3/v6.4/v6.5/v6.6)

All required:
```
1M%          +40 to +100
1W%            0 to +60
prior 1W%     >0 at an observation >=2h earlier
magnitude     <8%
Open%        -10 to +4
momentum      NORMAL: 30m >= +0.25   |   DEGRADED: max(5m,15m,30m) >= +0.25
24h volume    >= $20M
vol ratio     0.5x to 2.0x vs median(prev 3 observations)
breadth       >=35%
BTC 24h       >= -0.5%
cooldown      no entry in symbol within 72h; never two open positions in one symbol
exclusions    all clear
```

## 2C. v6.5 Participation-Ratio Risk Ladder (UNCHANGED)

Evaluated only after every Q2 gate passes.
```
PR = 1W% / 1M%
PR < 0.20   -> risk 0.50% of equity, tag Q2-LOW-PARTICIPATION
PR >= 0.20  -> risk 1.60% of equity, tag Q2-HIGH-PARTICIPATION
```

## 2D. Rule S — SHORT (UNCHANGED from v6.3/v6.4/v6.5/v6.6)

```
1M%         -70 to -25          1W%        -60 to 0
prior 1W%    <0                 magnitude   <8%
Open%        -4 to +10          momentum    NORMAL: 30m <= -0.50 | DEGRADED: min(5m,15m,30m) <= -0.50
24h volume  >= $20M             vol ratio   0.5x to 2.0x
BTC 24h     < -0.5%             cooldown    72h; never two open positions in one symbol
```
Risk remains **0.50% of equity.**

## 2E. Rule A / Rule R — shadow-only, unchanged. Log, never execute.

## 2F. Rule N — New-Listing / Futures-Catalyst Radar (N6 revised v7.1, LIVE since v7.2)

See §3 above for the full N1-N6 definition, and §13.2 for live entry/stop/size. Reproduced here
for the screening checklist:
```
N1  Official D1/E1 notice within 72h, sourced live, primary source cited when found
N2  1W% and/or 1M% blank in current snapshot
N3  24h volume >= $50M
N4  Open% between -10% and +8%
N5  LTF confirmation, STEP-0-aware (2-of-3 positive + max>=0.25 NORMAL; one DEGRADED reading
    if session triple-dup >=70%)
N6  Not DB-Red, not delisting-flagged, AND an explicit tokenized-equity identity check that
    does not depend on 1W/1M being present (v7.1 -- see §12)
```
Passing N1-N6 produces a Listing Radar Alert or Confirmed Watch tag in View 8, AND (v7.2) is a
live LONG entry: SL -20%, no fixed TP, 72h backstop, sized to risk 0.50% of equity (§13.2) --
unless a live-entry condition fails (cooldown, LV-Guard Auto-Skip, exclusion), in which case it
stays Watch-only. Every entry is logged with the same fields as Q2/S (STEP 6).

## 2G. Rule F — Fade-the-Pump (F1-F6 unchanged, LIVE since v7.2)

See §8 above for the full F1-F6 definition and §13.1 for live entry/stop/size. Reproduced here
for the screening checklist:
```
F1  Full Majors Whitelist (§2A) + DB-Red + tokenized-equity + delisting exclusions applied
F2  24h volume >= $1,000,000
F3  Ranked by 30m%/chg_30m, descending
F4  No magnitude ceiling; LV-Guard Auto-Skip does NOT apply (state any >=25% crossing as context)
F5  Identity/exclusion checks clear (redundant with F1, kept explicit)
F6  Session LTF triple-dup rate stated alongside the candidate
```
Passing F1-F6 produces a live SHORT entry (v7.2): SL -20% (price up 20% against the short), no
fixed TP (rotate at next scan or 24h time-stop), sized to risk 0.50% of equity (§13.1) -- unless
a live-entry condition fails, in which case it stays a "Fade-the-Pump Candidate" in View 9,
watch only. Every entry is logged with the same fields as Q2/S (STEP 6).

# STEP 3 — CONFLUENCE

Informational ranking only: Technical/Momentum/RS 30 · Liquidity 15 · Catalyst 15 ·
Macro/Regime 15 · Social 10 · Funding 8 bonus if real · OI 7 bonus if real.
No proxy values. Missing data stays zero. Confluence cannot override Q2 or S.

Rule N and Rule F entries get a confluence score for reporting/ranking purposes, same as Q2/S
(v7.2) -- confluence still cannot override any of the F1-F6/N1-N6 gates or the live-entry
checklist (§13); it is a ranking aid among simultaneous candidates, never an admission criterion.

# STEP 4 — EXITS & RISK

```
LONG Q2 : SL -10%   ARMED TRAIL (v8.0, §14): once running profit >=+20%, exit if it gives back
          >=15 percentage points from its own peak; otherwise hold to the 72h time-stop.
          No fixed TP -- this is what changed from v7.2 (which used TP +30%).
          risk 0.50% if PR < 0.20 ; 1.60% if PR >= 0.20
SHORT S : SL +10%   ARMED TRAIL (v8.0, §14): once running profit >=+20%, exit if it gives back
          >=15 percentage points from its own peak; otherwise hold to the 72h time-stop.
          No fixed TP -- this is what changed from v7.2 (which used TP -30%). risk 0.50%
RULE N  : SL -20%   no fixed TP   time-stop 72 real hours   risk 0.50%   (LIVE since v7.2, §13.2
          -- §6E NOT satisfied; this is an explicit override, see §0/§13 -- UNCHANGED in v8.0)
RULE F  : SL -20% (adverse)   no fixed TP, rotate-or-24h time-stop   risk 0.50%   (LIVE since
          v7.2, §13.1 -- §6F NOT satisfied; this is an explicit override, see §0/§13 -- UNCHANGED
          in v8.0)

Fees in audit = 0.15% round-trip on notional, all four rules alike.
Gap-through stop/trail = first observed price through the level, never forced to the nominal one.
Shadow variants logged in parallel: fixed-TP-30-shadow (so the trailing exit's live performance
  can keep being compared against what it replaced, not just its own backtest), S-060-shadow.
```
Do not use Kelly until >=20 **new live** closed trades exist, for ANY rule including N and F —
0.50%/trade is a fixed, conservative size chosen because neither has the closed-trade history
Kelly requires, not a Kelly output. Rule N and Rule F remain outside the Promotion Ladder (§6C/D)
regardless of being live — "live by override" and "promoted by evidence" are different things,
and only the written admission tests (§6E, §6F) can accomplish the latter.

# STEP 5 — EXECUTION CHECKLIST

```
□ Q2 LONG, S SHORT, N LONG, or F SHORT identified; side/session gates do not conflict.
□ Every entry gate explicitly PASS — no "close enough" — for whichever rule fired.
□ 1M, 1W, prior-1W (with the gap in hours), Open, magnitude, LTF momentum all stated (Q2/S);
  N1-N6 or F1-F6 all stated explicitly for Rule N / Rule F (§3, §8).
□ Volume and the 3-observation volume ratio stated (Q2/S); Rule N/F volume floor stated.
□ Breadth and BTC 24h stated (Q2/S).
□ Cooldown and open-position status stated, for whichever rule fired.
□ Exclusions / delisting / identity checks clear; BMNR and TAC flags respected. Rule N: the
  tokenized-equity identity check (N6, §12.1) explicitly confirmed, not skipped.
□ If Q2: PR computed and stated, AFTER the gates pass; risk tier assigned from it.
□ If S, N, or F: risk fixed at 0.50% (§13 for N/F sizing math).
□ SL / trail-arm-and-giveback levels stated from the actual entry price for Q2/S (v8.0, §14 --
  no fixed TP to compute anymore); N/F: §13's 20%-stop, no-fixed-TP structure, unchanged.
□ Funding / OI / Whale reported only if grounded; never fabricated.
□ Catalyst class and reflexivity label shown.
□ If Q2 or S fired: state plainly that the take-profit is the v8.0 trailing exit (arm +20%,
  give back 15pts), not the older fixed +30%/-30%, so a live fill is never checked against a
  target that no longer exists.
□ If Rule N or Rule F fired: state plainly, at the point of entry, that §6E/§6F are not
  satisfied and this is a v7.2 override, not a validated edge (§0, §13) -- every ticket, not
  just the first one.
```

# STEP 6 — JOURNAL / RECALIBRATION

Every closed trade:
`symbol | side | tier | PR | entry/exit time | entry/exit | risk% | P/L | R | exit reason | mode`

Maintain four Q2/S scoreboards unchanged from v6.5 (Q2-HIGH-PARTICIPATION, Q2-LOW-PARTICIPATION,
Rule S, shadow v6.4 flat-ladder book), **plus a fifth: Rule N live log, plus a sixth: Rule F live
log** — both now real closed-trade scoreboards as of v7.2 (§13), not shadow-only journals. Log
every Rule N/F trade with the same fields as Q2/S, plus an explicit note that §6E/§6F were not
satisfied at entry. **Also log, for every Q2/S exit, which branch fired (SL / TRAIL / TIME) and
the peak favorable excursion reached before exit** — this is the forward-validation record that
decides whether §14's backtested +71.29% (vs the old fixed-TP's +32.15%) holds up live; a fixed
TP is trivial to audit after the fact, an armed trail is not, so this field is not optional.

**6G. Q2/S Trailing-Exit forward-check (new in v8.0, same shape as 6E/6F, lighter bar because
this replaces an existing PILOT-F mechanism rather than introducing a new entry rule):**
```
□ >=30 new live Q2/S exits logged under the trailing rule (§14) before treating +71.29% as more
  than a strong backtest.
□ Recompute the single-symbol concentration check (§14.3) on live data specifically — a repeat of
  one trade dominating >20% of gains, on live fills rather than backtest fills, would be the
  first sign this is not generalizing.
□ Compare running live P&L against the fixed-TP-30-shadow book (STEP 4) at every recalibration —
  if the trail stops beating the shadow book it replaced, that is grounds to revert, not a reason
  to keep it on inertia.
```
Until this clears, the trailing exit is a backtested PILOT change to an already-PILOT-F pair of
rules — real evidence, the strongest single result in this document, but not yet forward-proven.

**6E. Rule N Admission Test (governance unchanged, modelled directly on 6B's Rule-A test —
progress noted inline per the v7.1 systematic pass, §12)**

Rule N stays Watch/Shadow-only until ALL of the following pass:
```
□ >=20-30 completed Listing Radar events logged (new Futures or Spot listings meeting N1-N6)
  -- v7.1: n=12 logged (§12). Still short of the bar.
□ Forward return measured at +2h, +6h, +24h from the Alert timestamp, plus maximum adverse
  excursion (MAE) — not just the favourable case
  -- v7.1: done for all 12 events (§12.3, results/rule_n_events.csv). MAE mean -5.3%, worst -15.6%.
□ Futures-triggered events and Spot-triggered events analysed SEPARATELY — catalyst quality
  differs between the two and they must not be pooled blind
  -- v7.1: NOT done. Listing-type metadata (Futures vs Spot) isn't in the CSV and wasn't looked
  up per-event; only 2 of 12 (MARSCOIN, NIULAI) were individually verified at all.
□ Funding rate, OI, and the 1H candle close checked where available, specifically to screen out
  already-crowded-long conditions before any promotion is considered
  -- v7.1: NOT done. No funding/OI data available.
□ PF > 1.50 after realistic fees on a proposed fixed exit structure (not yet specified — this
  is itself part of what the admission test must determine)
  -- v7.1: +24h PF = 3.03 gross of fees, but see the concentration failure below.
□ no single symbol contributes > 20% of total positive result
  -- v7.1: FAILS. MARSCOIN is 75-80% of total positive result at +24h (§12.3).
□ results remain positive with the best single event removed
  -- v7.1: FAILS. Removing MARSCOIN flips average +24h return negative and PF to 0.75.
□ boundary/still-open cases excluded from the clean statistics
```
Only if every box above is checked may Rule N be proposed for a Pilot Entry stage, at 0.25-0.50%
risk, and even then it requires the same explicit written approval every prior promotion in this
lineage has required. **A single winning case (MARSCOIN) is evidence worth logging, not evidence
worth trading — and v7.1 shows that is still true even inside a 12-case sample, not just a
1-case one.**

**v7.2 status: none of the above changed. Rule N is live (§13.2) anyway, by explicit trader
override, not by clearing this test.** This checklist stays exactly as written so that "still
not satisfied" remains visible and auditable for as long as it's true — an override does not get
to also erase the record of what it overrode.

**6F. Rule F Admission Test (governance unchanged from v7.0 — progress noted inline per the
v7.1 deep-dive, §11)**

Rule F stays Watch/Pilot-Candidate-only until ALL of the following pass:
```
□ §7's backtest re-run using this process's full Majors Whitelist exclusion (not just BTC/ETH),
  confirming the edge survives the correct, larger exclusion set.
  -- v7.1: DONE (§11.1). Edge essentially unchanged (+249.4% vs +246.7%).
□ >=3 additional independent months of walk-forward data beyond the Jul-Aug 2026 window in §7 —
  one two-month regime is not enough, by this lineage's own standard for Q2/S/PR.
  -- v7.1: NOT done (only 4 discontinuous September days added, §11.2) -- and that small sample
  LOST money (-11.5%, Sharpe -9.34), which raises this bar rather than lowering it.
□ A specific stop-loss / take-profit / position-sizing scheme proposed AND back-tested at the
  SINGLE-TRADE level (not basket-average) — the -111.8% worst trade must be re-examined under
  every candidate stop-loss level before any one is adopted.
  -- v7.1: a candidate exists (RULE_F_RISK_DESIGN.md, stop=15%/risk=0.50%) but is itself still
  unvalidated against real intrabar data -- see that document's own caveats.
□ The LV-Guard question (F4) resolved by direct test, not assumption: does entering a short
  exactly as magnitude crosses 25% increase or decrease realized edge and tail risk?
  -- v7.1: TESTED (§11.3) but not resolved -- it's a real trade-off (roughly half the return for
  less than half the tail risk), left for a human decision, not a data-determined answer.
□ Funding rate incorporated from real historical data, not left unmodeled.
  -- v7.1: NOT done. Still no funding data available.
□ Results remain positive with the single best week (2026-08-16, +70.1%) removed.
□ No single symbol or single week contributes > 20% of total positive result.
□ PF > 1.50 net of realistic fees AND a modeled stop-loss, computed on the single-trade (not
  basket-average) return series.
□ boundary/still-open cases excluded from the clean statistics (mirrors 6E).
```
Only if every box above is checked may Rule F be proposed for a Pilot Entry stage, at 0.25-0.50%
risk, and even then it requires the same explicit written approval every prior promotion in this
lineage has required. **A two-month walk-forward backtest is stronger evidence than Rule N's
single case, but a losing out-of-sample month (§11.2) is exactly the kind of evidence this
admission test exists to catch before capital sees it.**

**v7.2 status: none of the above changed. Rule F is live (§13.1) anyway, at PF 1.45 (below the
1.50 line in this same checklist), by explicit trader override, not by clearing this test.** As
with §6E, the checklist stays exactly as written — the override does not get to also erase the
record of what it overrode.

**6A. Missed-Opportunity / Shadow Journal** — unchanged, now also receives near-misses that fail
N1-N6 or F1-F6 (still non-executing), tagged separately from Rule A/R shadow entries and from
each other. This is distinct from the live logs in §6's opening scoreboard list, which record
Rule N/F trades that DID fire.

**6B. Rule-A Admission Test** — unchanged from v6.5.

**6C/6D** — Blow-Off Reset Review and the v6.x Promotion Ladder, unchanged from v6.5. Rule N and
Rule F still sit outside this ladder: v7.2 made them live by override, not by promotion, so
neither has entered the ladder at PILOT stage the way Rule R and every Q-generation rule did —
clearing §6E/§6F on the merits is still what that would take.

---

## Known limitations (Q2/S/PR ladder — carried from v6.5, still true, still unresolved)

- n = 67 trades over 60 days for the Q2/S/PR-ladder backtest (the version cycle this figure was
  first quoted from). §14's own from-scratch Q2/S backtest against Jul-Aug 2026 found n=85 trades
  (58 Q2, 27 S) — a similar order of magnitude, on a different two-month window, not a
  reconciliation of the exact same trade set.
- Both v6.5 changes were selected on data including the 23-29 Aug stress week — regime evidence,
  not a clean post-selection out-of-sample test.
- 47 of 67 (v6.5 figure) / 58 of 85 (§14 figure) exits are the 72h time stop; the edge is
  substantially "leave flat when nothing happens," which makes it sensitive to the time-stop
  choice specifically, independent of whichever take-profit rule sits alongside it.
- Rule S rests on 10 (v6.5) / 27 (§14) trades; every short-side conclusion is provisional.
- Fees modelled at 0.15% round-trip; funding not modelled. Exits at snapshot resolution
  (median gap 2.95h), not tick level — this applies to the new trailing exit (§14) exactly as it
  always applied to the fixed TP: whether a live trail arms/exits at the modeled level, or slips
  past it between snapshots, is untested against real intrabar data.

## Known limitations (Q2/S trailing exit — new in v8.0, see §14 for the full picture)

- n = 85 trades, one two-month window (Jul-Aug 2026) — the same evidence tier as everything else
  in this bullet list, not a larger one. This is a strong, plateau-robust backtest result (§14.2),
  not a forward-proven live result (§6G tracks that separately).
- **34.7% of the trailing exit's total positive result comes from one trade** (TUTUSDT.P) — above
  this lineage's own 20%-concentration guideline. The mechanism survives its removal (+39.05% vs
  the old fixed-TP's +32.15%, §14.3), so it is not purely one-trade-dependent, but one very large
  winner is still doing a large share of the headline number.
- The armed-trail parameters (arm +20%, giveback 15pts) were chosen from a plateau of nearby
  values that all performed similarly (§14.2), not swept as exhaustively as Q2/S's own entry
  thresholds have been across five to six version cycles — treat them as a good first setting,
  not a fully optimized one.
- Interacts with, but does not change, Rule N/F's live-fixed-20%-stop structure (§13) — those two
  rules never had a fixed TP to begin with (Rule N explicitly rejected one, §13.2), so this
  change is Q2/S-specific and does not extend to them.

## Known limitations (Rule N — see §5 and §12 above for the full picture)

- n = 12 as of v7.1 (was 1). Better, but MARSCOIN alone is still 75-80% of total positive
  result at +24h — removing it flips the average return negative and PF below 1 (§12.3).
- Two of the twelve logged events were tokenized equities, not crypto listings, until manually
  verified (§12.1) — N6 is revised, but the fix depends on ongoing manual identity checks, not
  a fully mechanical filter.
- N1 depends on a live search succeeding; a failed or incomplete search must downgrade the
  catalyst label, never get silently skipped. Only 2 of 12 events (MARSCOIN, NIULAI) have been
  individually verified this way so far.
- Futures-vs-Spot separation and funding/OI screening (both required by §6E) are still not done
  at all.
- No short-side equivalent exists or is proposed.
- Survivorship risk in the underlying listing pipeline is real and currently unmeasured.

## Known limitations (Rule F — see §9 and §11 above for the full picture)

- n = 401 rebalance periods / 4,010 trades across Jul-Aug 2026, plus a 17-period September
  extension in v7.1 that **lost money** (-11.5%, Sharpe -9.34) — the one new out-of-sample test
  run since v7.0 was a losing one (§11.2).
- Confirmed in v7.1: the edge is not a universe artifact (full Majors Whitelist re-test barely
  moves the numbers, §11.1) — but no single-trade stop-loss has ever been tested against real
  intrabar data; the -111.8% worst-leg loss (identified in v7.1 as `EVAAUSDT.P`, §11.4) is real.
- LV-Guard/F4 tested directly in v7.1 (§11.3): a real trade-off (roughly half the return for
  less than half the tail risk), not resolved in either direction.
- No long-side variant (buying the biggest losers, or fading a crash upward) outperformed in the
  grid search; none is proposed. Larger baskets, signal caps, and price floors were tried in
  v7.1 and none improved on the original N=10 config (§11.5).

---

## Research references

Carried from v6.5/v6.6/v7.0, plus:
- Moskowitz, Ooi & Pedersen (2012), *Time Series Momentum*, JFE. https://doi.org/10.1016/j.jfineco.2011.11.003
- Barroso & Santa-Clara (2015), *Momentum Has Its Moments*, JFE. https://doi.org/10.1016/j.jfineco.2014.11.010
- Moreira & Muir (2017), *Volatility-Managed Portfolios*, Journal of Finance. https://doi.org/10.1111/jofi.12513
- Han, Kang & Ryu, *Momentum in Cryptocurrency Market under Realistic Assumptions* (SSRN).
- Binance, official futures-listing notice for MARSCOINUSDT (2026-09-01, trading began 18:45 KST)
  and official spot-listing notice (published 2026-09-04 10:15 UTC) — both fetched and confirmed
  directly for v6.6, not taken from secondary aggregation.
- Jegadeesh (1990), *Evidence of Predictable Behavior of Security Returns*, Journal of Finance,
  45(3). [Citation not independently re-verified with a DOI in this session — confirm the exact
  reference before citing it externally; included here as directional support for short-horizon
  reversal existing as a documented phenomenon, not as a substitute for testing Rule F itself.]
- Lehmann (1990), *Fads, Martingales, and Market Efficiency*, Quarterly Journal of Economics,
  105(1). [Same caveat as above — not independently re-verified with a DOI in this session.]
- Internal backtest: `Mai_BI_20260701_20260731_Combined_FullMonth.xlsx` +
  `Mai_BI_20260801_20260831_Combined_FullMonth.csv` (+ three September snapshots for v7.1),
  n=401 rebalance periods / 4,010 trades, walk-forward validated (July in-sample, August
  out-of-sample), plus the v7.1 September extension and Majors Whitelist re-test — see §7, §11.
- Binance Futures NIULAI perpetual listing notice, 2026-08-30 11:30 UTC (Binance Alpha token) —
  fetched and confirmed directly for v7.1's Rule N verification (§12.2), via live web search,
  not taken from secondary aggregation without a primary cross-check.
- SK Hynix (SKHYB) tokenized-securities spot-listing announcement, dated 2026-07-13 — fetched
  and confirmed directly for v7.1's Rule N false-positive finding (§12.1).

**Reminder:** backtests on screener snapshots are decision-research, not proof of future profit.
Rule N is twelve cases now, one of which still explains nearly all of the apparent edge — logged
honestly as exactly that. Rule F is a two-month, basket-average backtest with no stop-loss ever
modeled and one losing out-of-sample month on record, logged honestly as exactly that too. The
v8.0 trailing exit is a strong two-month backtest with one trade carrying more than a third of
its own added gains — logged honestly as exactly that, not as a finished result (§14, §6G).

---

## WINNING FORMULA

```
PROCESS + DATA + AI INSIGHT + DISCIPLINE + RISK MANAGEMENT = LONG-TERM SUCCESS

NO REASON = NO TRADE
RULE Q2 NOT FULLY SATISFIED = NO TRADE
RULE N AND RULE F WENT LIVE BY OVERRIDE, NOT BY EARNING IT — SAY SO ON EVERY TICKET (§13)
A WEEKLY MOVE WITHOUT A MONTHLY TREND IS A SPIKE, NOT A TREND
A COIN WITH NO MONTHLY HISTORY IS NOT A FAILED TREND — IT IS AN UNMEASURED ONE
SEEING A COIN AND TRADING A COIN ARE TWO DIFFERENT DECISIONS WITH TWO DIFFERENT STANDARDS OF PROOF
ONE WINNING CASE IS A LOG ENTRY, NOT A BACKTEST — EVEN AFTER IT'S LIVE
THE HIGHEST-RETURN PARAMETER SET IS USUALLY THE MOST OVERFIT ONE
THE BEST SHARPE OF ONE MONTH IS OFTEN NEXT MONTH'S BIGGEST LOSS
A BASKET BACKTEST WITHOUT A STOP-LOSS IS RESEARCH, NOT A TRADING PLAN
FADING A PUMP AND CATCHING A SQUEEZE ARE THE SAME TRADE UNTIL THE STOP-LOSS IS SET
TWELVE CASES WITH ONE CARRYING THE RESULT IS STILL ONE CASE
A LOSING OUT-OF-SAMPLE MONTH IS THE ANSWER THE ADMISSION TEST WAS BUILT TO HEAR
MORE EVIDENCE THAT STILL SAYS NO IS PROGRESS — IT IS NOT PERMISSION
AN OVERRIDE IS A DECISION TO ACCEPT A KNOWN RISK, NOT A DECISION TO STOP MEASURING IT
A FIXED TAKE-PROFIT CAPS THE ONE TRADE THAT WAS GOING TO MAKE THE YEAR — TRAIL IT INSTEAD (§14)
A CHART-ONLY LESSON CAN STILL BE REAL EVIDENCE ONCE IT'S TESTED ON DATA THAT ACTUALLY HAS IT
A BACKTEST WINNING ON THE FIRST TRY IS A REASON TO CHECK IT HARDER, NOT TRUST IT MORE
ONE TRADE BEING 35% OF THE GAIN IS A FACT TO REPORT, NOT A REASON TO HIDE THE OTHER 65%
```
