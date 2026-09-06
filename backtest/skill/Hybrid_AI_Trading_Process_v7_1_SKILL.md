---
name: hybrid-ai-trading
version: 7.1
effective_date: 2026-09-06
supersedes: >
  7.0 — Q2 (long), S (short), the Participation-Ratio risk ladder, and exits are UNCHANGED and
  remain byte-for-byte, still PILOT-F. Rule F's own mechanical definition (F1-F6) is UNCHANGED;
  this version adds a deep-dive evidence pass (full Majors Whitelist re-test, a September
  out-of-sample slice, a direct LV-Guard/F4 test) but Rule F remains WATCH-ONLY / PILOT-CANDIDATE
  -- STEP 6F is not satisfied. Rule N's N1-N5 are UNCHANGED; N6 is REVISED to add an explicit
  tokenized-equity identity check, after live verification found two of twelve systematically
  logged candidates were tokenized stocks, not crypto listings. Rule N remains WATCH-ONLY/SHADOW
  -- STEP 6E is not satisfied (n=12, and fails its own >20%-concentration rule).
status: >
  Q2, S, the Participation-Ratio ladder, and exits are UNCHANGED from v7.0 and keep PILOT-F.
  Rule F is UNCHANGED in its own definition and remains WATCH-ONLY / PILOT-CANDIDATE, zero
  execution authority: this version's deep-dive confirms the edge survives the process's full
  Majors Whitelist (+249.4% vs the original +246.7%), quantifies the LV-Guard/F4 trade-off
  directly (applying it roughly halves total return, 26.0% -> 11.1%, but cuts the worst trade
  from -111.8% to -47.3%), and -- most importantly -- finds a real losing stretch in the one new
  out-of-sample window available (September 2-5: -11.5%, Sharpe -9.34, n=17 periods). None of
  this clears STEP 6F; if anything the September result raises the bar. Rule N remains
  WATCH-ONLY / SHADOW, zero execution authority: a systematic mechanical pass grew its event log
  from n=1 (MARSCOIN) to n=12, but live verification found 2 of the 12 are tokenized equities
  (SK Hynix, Yushu Technology/UNITREE), not crypto listings -- a real gap in N6, revised in this
  version. Of the real crypto-listing candidates, MARSCOIN alone still accounts for 75-80% of
  total positive result at +24h; removing it flips the average return negative and the profit
  factor below 1. STEP 6E's own concentration rule, applied honestly, says Rule N still does not
  pass, and n=12 remains well short of the >=20-30 bar regardless. Kikuji's written sign-off is
  still required before either rule graduates past Watch/Pilot-Candidate into anything that
  touches capital.
description: >
  Hybrid AI Trading Process v7.1. A deep-dive evidence pass on Rule F and Rule N, requested to
  find ways to improve profitability -- honest result: neither rule got closer to tradable, and
  one important warning sign surfaced. Rule F: confirmed the edge is not a universe artifact
  (full Majors Whitelist re-test barely moves the numbers), quantified the LV-Guard/F4 question
  directly instead of leaving it a hypothesis (a real trade-off: about half the return for less
  than half the tail risk), and found a real losing out-of-sample stretch in September that
  larger baskets, signal caps, and price floors did nothing to fix -- none of the profit-
  improvement attempts tried actually improved profit. Rule N: systematically logged 12 events
  instead of 1, live-verified two as tokenized-equity false positives (a real methodology fix,
  included here), verified one new genuine case (NIULAI), and then found that its own
  concentration test fails once applied honestly -- MARSCOIN is still ~80% of the positive
  result. Q2, S, the PR ladder, and exits are untouched. Core rule unchanged: No Reason = No
  Trade. Unknown is a valid analytical result. Fabricated certainty is not. More evidence that
  still says no is progress; it is not permission.
---

# HYBRID AI TRADING PROCESS v7.1 — Deeper Evidence, Same Verdict

**Role:** Professional Crypto Trader — Technical Analysis + Market Psychology
**Markets:** BTC & Altcoins | Binance Perpetuals
**Core:** `No Reason = No Trade` · missing evidence is not confirmation · no fabricated certainty.

---

## 0. Governance first — read before using

**What changed and what didn't.** Rule Q2, Rule S, the Participation-Ratio risk ladder (§2C),
exits (SL −10% / TP +30% / 72h time-stop), and every exclusion list except N6 are copied
byte-for-byte from v7.0. Rule F's own mechanical definition (§8, F1-F6) is untouched. Rule N's
N1-N5 are untouched; **N6 is revised** (see §12) after live verification found two of twelve
systematically-logged candidates were tokenized equities, not crypto listings. Neither Rule N
nor Rule F gained execution authority — both remain exactly as gated as in v7.0, on their own
separately-defined admission tests (§6E, §6F). This version answers a direct request: "take
Rule N and Rule F results, find ways to improve them, and maximize profit." The honest answer,
worked through in §11-§12, is that the deep-dive did not find a way to increase profit, and
found one real warning sign (a September losing stretch) plus one real methodology fix (the N6
tokenized-equity gap) instead. Log first, prove it later, promote never without an admission
test — unchanged since Rule A in v4.4.

**Why a v7.1 exists at all instead of staying silent.** Because "we looked and found nothing to
improve, plus one new caution" is still information the trader needs, and burying a negative
result (the September test) would be exactly the "fabricated certainty" this process exists to
refuse. v7.0's own headline finding — the naive best-July config losing more than half its value
in August — is precisely the kind of surprise this version re-confirms the discipline against:
more testing revealed more risk, not more edge, and that gets reported the same way a good
result would.

**What this version explicitly does NOT do.** It does not promote Rule F or Rule N past
Watch/Pilot-Candidate. It does not resolve the LV-Guard/F4 question in either direction — it
quantifies the trade-off (§11.3) and leaves the decision open. It does not treat n=12 as
sufficient evidence for Rule N (§12) — the admission test's own concentration rule, applied
honestly, still fails. It does not touch Q2, S, the PR ladder, or exits in any way.

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
PR≥0.20 → 1.60% risk). Exits: SL −10%, TP +30%, 72h time-stop. All exclusion lists (majors
whitelist, DB-Red, tokenized-equity list+heuristic, delisting block, LV-Guard ≥25%, 1W>150%
no-chase). The DEGRADED-CONFIRM data gate. BTC leader gates. Seven Views at exactly 12 rows each.
Thai-language, light-theme reporting. Rule N (§3) — still Watch/Shadow-only, still gated on its
own admission test (§6E); only its N6 exclusion criterion is revised this version (see §12), N1-N5
untouched. Rule F (§8) — mechanical definition F1-F6 fully unchanged, still gated on §6F.
**Every Q2/S/PR/exits number here was tested across five to six major version cycles; none of
that evidence is touched by a deep-dive evidence pass on two non-executing watch/pilot rules.**

---

## 3. Rule N — New-Listing / Futures-Catalyst Radar (N6 REVISED in v7.1, WATCH-ONLY)

**Status: Watch/Shadow only for its first 20-30 logged events. Cannot size. Cannot execute.**

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
This is a reporting output, not a trade ticket. It tells the trader what the system saw and why
it still did not — and does not — authorize a Long.

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
Radar**, listing the top chg_30m/30m% candidates that pass F1-F5, tagged **"Fade-the-Pump
Candidate (WATCH/PILOT-CANDIDATE, no live trade authorized)"**, with no fixed row count. A symbol
can appear in View 8 and View 9 in the same session — a brand-new listing that is also spiking
hard on the 30-minute clock — report both tags plainly rather than merging them; they come from
independent evidence bases (§1 vs §7) and neither authorizes the other.

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

## 8. Rule F — Fade-the-Pump Basket/Discretionary Short (NEW, WATCH-ONLY / PILOT-CANDIDATE)

**Status: Watch-only / pilot-candidate. Cannot size. Cannot execute, in basket or single-trade
form, until §6F passes.**

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
per-trade stop-loss. This is the mode with the two-month walk-forward evidence in §7. It is not
built into this process's per-trade execution model and is not proposed for that here — it would
need its own systematic sub-book, sized and risk-capped separately from every discretionary
Q2/S/N/F trade below, and that sub-book is itself unbuilt and untested.

Discretionary-Single-Trade mode (the only mode this process could actually execute today): take
the single highest-ranked F1-F5 candidate as one Rule F short. Size: UNDEFINED — do not borrow
Rule S's 0.50%/-10%/+10%/72h template without re-testing it against Rule F's own return
distribution first; Rule F's holding period (~3h backtested) and entry logic (fade a spike, not
confirm a trend) are not the same trade as Rule S. This mode has ZERO direct backtest evidence of
its own — §7 never simulated single-name selection, one order's slippage, or any stop-loss — it
inherits the basket study only as motivating evidence, not as its own track record.
```

**Reporting only, until §6F passes:**
```
F1-F6 all pass          -> "Fade-the-Pump Candidate" in View 9 (§4)
magnitude crossing 25%  -> stated, not auto-skipped (see F4) -- report the crossing plainly as
                            context, since it is part of the F4 thesis, not a block
```

**Explicitly out of scope for v7.0:** any long-side use of this signal (fading a crash upward,
i.e. buying the biggest 30-minute losers) — the backtest tested long-only and long-short variants
of every signal and none outperformed short-only fading; see §7's grid-search note. A crash-fade
long is not proposed here and would need its own separate study.

---

## 9. Known limitations of Rule F

- **Backtest evidence is basket-average, not single-trade.** The −111.8% worst-single-leg loss
  was absorbed inside a 10-name average that period; a discretionary single-name version has no
  such cushion. This is the single biggest reason Rule F cannot size a position yet.
- **No stop-loss, take-profit, or position size has been tested at all.** §8's Discretionary mode
  is presently undefined by design — inventing a number without testing it would be exactly the
  kind of fabricated certainty this process exists to refuse.
- **Universe mismatch.** §7's backtest excluded only BTC/ETH; this process's own Majors Whitelist
  is broader. Until re-tested against the correct universe, treat §7's exact percentages as
  directionally suggestive, not load-bearing.
- **One two-month regime.** Alt-heavy, volatile window (see §7). Untested in a calm or
  trending-down market.
- **Funding rate unmodeled.** Plausibly a tailwind (shorts often collect funding during a pump);
  unquantified, so not to be assumed in either direction when sizing.
- **LV-Guard's role is an open question, not a resolved one.** F4 proposes ignoring it for entry
  (the opposite of Q2/N's use), reasoning that a short's setup and a long's danger sign are not
  the same signal — but this is a hypothesis, not yet a tested result.
- **One large week (2026-08-16, +70.1%) is a meaningful share of the two-month total return** —
  §6F requires re-checking profitability with that week excluded before the headline Sharpe can
  be treated as representative.

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
that explains precisely why n=12 still isn't evidence of an edge (12.3). None of this clears
§6E.

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

## 2F. Rule N — New-Listing / Futures-Catalyst Radar (N6 REVISED in v7.1, WATCH-ONLY)

See §3 above for the full N1-N6 definition. Reproduced here for the screening checklist:
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
Passing N1-N6 produces a Listing Radar Alert or Confirmed Watch tag in View 8. **It produces
nothing else.** No entry, no size, no SL/TP. Rule N candidates are logged to the shadow journal
exactly like Rule A candidates, under their own tag.

## 2G. Rule F — Fade-the-Pump (NEW, WATCH-ONLY / PILOT-CANDIDATE)

See §8 above for the full F1-F6 definition and the two execution modes. Reproduced here for the
screening checklist:
```
F1  Full Majors Whitelist (§2A) + DB-Red + tokenized-equity + delisting exclusions applied
F2  24h volume >= $1,000,000
F3  Ranked by 30m%/chg_30m, descending
F4  No magnitude ceiling; LV-Guard Auto-Skip does NOT apply (state any >=25% crossing as context)
F5  Identity/exclusion checks clear (redundant with F1, kept explicit)
F6  Session LTF triple-dup rate stated alongside the candidate
```
Passing F1-F6 produces a "Fade-the-Pump Candidate" tag in View 9. **It produces nothing else.**
No entry, no size, no SL/TP — Discretionary-Single-Trade mode (§8) remains undefined until §6F.
Rule F candidates are logged to the shadow journal exactly like Rule A/N candidates, under their
own tag.

# STEP 3 — CONFLUENCE

Informational ranking only: Technical/Momentum/RS 30 · Liquidity 15 · Catalyst 15 ·
Macro/Regime 15 · Social 10 · Funding 8 bonus if real · OI 7 bonus if real.
No proxy values. Missing data stays zero. Confluence cannot override Q2 or S.

Rule N alerts get a confluence score for reporting/ranking purposes only within View 8 — it never
authorizes execution and is not comparable to a Q2/S confluence score. Rule F candidates get a
confluence score for View 9 ranking only, on the same non-authorizing basis — never comparable to
a Q2/S/N confluence score either.

# STEP 4 — EXITS & RISK

```
LONG Q2 : SL -10%   TP +30%   time-stop 72 real hours
          risk 0.50% if PR < 0.20 ; 1.60% if PR >= 0.20
SHORT S : SL +10%   TP -30%   time-stop 72 real hours   risk 0.50%
RULE N  : no position, therefore no SL/TP/risk. Watch/log only.
RULE F  : Systematic-Basket mode has no per-trade SL/TP (basket-average backtest only, not a
          live-tradable ticket as specified). Discretionary-Single-Trade mode: SL/TP/size
          UNDEFINED — may not open a position of any kind until §6F defines and validates one.

Fees in audit = 0.15% round-trip on notional (Q2/S only — Rule N and Rule F generate no fees,
no fills).
Gap-through stop = first observed price through the stop, never forced to nominal -10%.
Shadow variants logged in parallel: TP25-fallback, TP32-shadow, S-060-shadow.
```
Do not use Kelly until >=20 **new live** closed trades exist. Rule N is never part of a Kelly
calculation — it has no closed trades, by construction, until it is promoted (§6E). Rule F is
never part of a Kelly calculation either, for the same reason, until it is promoted (§6F).

# STEP 5 — EXECUTION CHECKLIST

```
□ Q2 LONG or S SHORT identified; side/session gates do not conflict.
□ Every entry gate explicitly PASS — no "close enough".
□ 1M, 1W, prior-1W (with the gap in hours), Open, magnitude, LTF momentum all stated.
□ Volume and the 3-observation volume ratio stated.
□ Breadth and BTC 24h stated.
□ Cooldown and open-position status stated.
□ Exclusions / delisting / identity checks clear; BMNR and TAC flags respected.
□ If Q2: PR computed and stated, AFTER the gates pass; risk tier assigned from it.
□ If S: risk fixed at 0.50%.
□ SL / TP / time-stop calculated from the actual entry price.
□ Funding / OI / Whale reported only if grounded; never fabricated.
□ Catalyst class and reflexivity label shown.
□ Rule N alerts (if any) reported in View 8 — explicitly labelled NOT A TRADE.
□ Rule F candidates (if any) reported in View 9 — explicitly labelled NOT A TRADE
  (SL/TP/size undefined, §8).
```

# STEP 6 — JOURNAL / RECALIBRATION

Every closed trade:
`symbol | side | tier | PR | entry/exit time | entry/exit | risk% | P/L | R | exit reason | mode`

Maintain four Q2/S scoreboards unchanged from v6.5 (Q2-HIGH-PARTICIPATION, Q2-LOW-PARTICIPATION,
Rule S, shadow v6.4 flat-ladder book), **plus a fifth: Rule N Listing Radar log, plus a sixth:
Rule F Fade-the-Pump log.**

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

**6A. Missed-Opportunity / Shadow Journal** — unchanged, now also receives Rule N candidates that
failed N1-N6 and Rule F candidates that failed F1-F6 (near-misses), tagged separately from Rule
A/R shadow entries and from each other.

**6B. Rule-A Admission Test** — unchanged from v6.5.

**6C/6D** — Blow-Off Reset Review and the v6.x Promotion Ladder, unchanged from v6.5; Rule N sits
outside this ladder entirely until 6E is satisfied, and Rule F sits outside it entirely until 6F
is satisfied, at which point either would enter the ladder at PILOT stage exactly as Rule R and
every Q-generation rule did before it.

---

## Known limitations (Q2/S/PR ladder — carried from v6.5, still true, still unresolved)

- n = 67 trades over 60 days for the Q2/S/PR-ladder backtest. Bootstrap gives P(profit > 0) =
  100%, but P(v6.5 > v6.4) is only 70.4% — the point estimate clears the target, the sampling
  distribution does not clear it comfortably.
- Both v6.5 changes were selected on data including the 23-29 Aug stress week — regime evidence,
  not a clean post-selection out-of-sample test.
- 47 of 67 exits are the 72h time stop; the edge is substantially "leave flat when nothing
  happens," which makes it sensitive to the time-stop choice.
- Rule S rests on 10 trades; every short-side conclusion is provisional.
- Fees modelled at 0.15% round-trip; funding not modelled. Exits at snapshot resolution
  (median gap 2.95h), not tick level.

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
modeled and one losing out-of-sample month on record, logged honestly as exactly that too.

---

## WINNING FORMULA

```
PROCESS + DATA + AI INSIGHT + DISCIPLINE + RISK MANAGEMENT = LONG-TERM SUCCESS

NO REASON = NO TRADE
RULE Q2 NOT FULLY SATISFIED = NO TRADE
RULE N IS A RADAR, NOT A SIGNAL — IT HAS NEVER TRADED AND CANNOT UNTIL IT EARNS IT
RULE F IS A BACKTEST, NOT A TICKET — IT HAS NO STOP-LOSS AND CANNOT TRADE UNTIL IT EARNS ONE
A WEEKLY MOVE WITHOUT A MONTHLY TREND IS A SPIKE, NOT A TREND
A COIN WITH NO MONTHLY HISTORY IS NOT A FAILED TREND — IT IS AN UNMEASURED ONE
SEEING A COIN AND TRADING A COIN ARE TWO DIFFERENT DECISIONS WITH TWO DIFFERENT STANDARDS OF PROOF
ONE WINNING CASE IS A LOG ENTRY, NOT A BACKTEST
THE HIGHEST-RETURN PARAMETER SET IS USUALLY THE MOST OVERFIT ONE
THE BEST SHARPE OF ONE MONTH IS OFTEN NEXT MONTH'S BIGGEST LOSS
A BASKET BACKTEST WITHOUT A STOP-LOSS IS RESEARCH, NOT A TRADING PLAN
FADING A PUMP AND CATCHING A SQUEEZE ARE THE SAME TRADE UNTIL THE STOP-LOSS IS SET
TWELVE CASES WITH ONE CARRYING THE RESULT IS STILL ONE CASE
A LOSING OUT-OF-SAMPLE MONTH IS THE ANSWER THE ADMISSION TEST WAS BUILT TO HEAR
MORE EVIDENCE THAT STILL SAYS NO IS PROGRESS — IT IS NOT PERMISSION
```
