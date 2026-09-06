# v7.1 deep-dive — Rule N and Rule F

**Data added this round**: `Mai_BI_20260902_Combined.csv`, `Mai_BI_20260903_Combined.csv`,
`Mai_BI_20260905_Combined.csv` (2026-09-04 is missing — a 1-day gap between the 09-03 and 09-05
files). July/August files re-confirmed identical to the original backtest (same row counts,
same date range).

Reproduce: `python rule_f_v71_analysis.py` and `python rule_n_systematic.py` from `backtest/`.

## Rule F — what changed, and one real warning sign

### 1. Full Majors Whitelist re-test: the edge is not a universe artifact

The original backtest only excluded `BTCUSDT.P`/`ETHUSDT.P`; this process's own Majors Whitelist
(§2A) excludes 22 names. Re-running with the correct exclusion:

| | BTC/ETH-only (original) | Full Majors Whitelist (corrected) |
|---|---|---|
| July | +72.8%, Sharpe 5.07 | +72.4%, Sharpe 5.05 |
| August | +100.7%, Sharpe 7.67 | +102.7%, Sharpe 7.75 |
| Combined | +246.7%, Sharpe 6.15 | +249.4%, Sharpe 6.18 |

Essentially unchanged. The edge does not depend on trading majors — one §6F prerequisite is now
satisfied.

### 2. September mini-slice: the edge did NOT hold up (important caution)

Adding the three September snapshots as a third, independent (if tiny and discontinuous) slice:

| Period | Periods | Total return | Sharpe | Win rate |
|---|---|---|---|---|
| September (Sep 2, 3, 5 only) | 17 | **−11.5%** | **−9.34** | 35.3% |
| Full Jul+Aug+Sep | 418 | +209.3% | 5.33 | 56.5% |

**This is a real negative result, not noise to explain away.** n=17 periods over 4 discontinuous
days is far too small to draw a firm conclusion, and this exact window overlaps the MARSCOIN
squeeze (§1) — a period where several of Rule F's short candidates were themselves in the middle
of parabolic upside moves that kept squeezing higher, exactly the tail-risk mechanism the
strategy is vulnerable to. But the honest reading is: the one clean out-of-sample extension
tested since the original backtest was closed with a loss. This raises, rather than lowers, the
bar for §6F's "≥3 additional independent months" requirement — it should not be treated as a
formality.

### 3. LV-Guard (F4) — tested directly, and it's a real trade-off, not a clear win

§6F asked whether entering a short exactly as magnitude crosses 25% (LV-Guard territory)
increases or decreases realized edge and tail risk. Tested directly, single-trade discretionary
mode, stop=15%/risk=0.50%, full Jul+Aug+Sep:

| Variant | Total return | Profit factor | Worst trade |
|---|---|---|---|
| A — no LV-Guard (current F4 design) | +26.0% | 1.61 | **−111.8%** |
| B — LV-Guard applied (magnitude≥25% excluded) | +11.1% | 1.35 (fails the §6F bar) | −47.3% |

Applying LV-Guard roughly **halves** total return and drops profit factor below the 1.50
admission bar, but it also cuts the worst-case loss by more than half. This is a genuine
risk/return trade-off the trader has to decide on, not something the data resolves cleanly —
recorded here as tested evidence rather than left as an open assumption.

### 4. The worst trade, identified

`EVAAUSDT.P`, entered 2026-07-12 08:34, magnitude **80.2%** at entry (already deep into a
blow-off before Rule F even shorted it), price then roughly doubled again (0.5025 → 1.0642,
−111.8%). This is precisely the LV-Guard scenario in #3 — a magnitude filter would have skipped
this exact trade. The #2 worst trade was `TACUSDT.P` (−57.3%) — the same symbol this process's
own governance notes (§2A) already flag as "proposed for permanent DB-Red addition; currently
auto-blocked by LV-Guard only." This is independent, additional evidence supporting that
existing (still-pending-approval) flag.

### 5. Profit-improvement attempts that did NOT help

- **Larger baskets (N=15, N=20)**: return and Sharpe both *fall* (N=15: +84.9%/3.73; N=20:
  +57.4%/3.30, vs N=10's +209.3%/5.33). N=10 remains the best-tested size, not an
  arbitrary choice.
- **Capping extreme `chg_30m` signal values (>50%)**: no effect at all — the worst trades' entry
  signal was a normal-looking chg_30m (EVAA's was only 10.3%); the real tail-risk driver is
  `magnitude` (Open%/24h%), not the 30-minute signal itself. Confirms #3/#4 is the right lever,
  not a signal-value cap.
- **Excluding sub-cent prices (<$0.001)**: negligible effect (+211.1% vs +209.3%).

**Honest conclusion: this deep-dive did not find a way to increase Rule F's profit beyond the
original N=10 config.** It found that the universe choice doesn't matter (good), that LV-Guard is
a real and quantified trade-off (useful), that one specific symbol should probably be
DB-Red-listed (actionable), and that the strategy had a real losing stretch in the only new
out-of-sample window available (a caution, not an improvement).

## Rule N — evidence grows from n=1 to n=12, but fails its own concentration test

A systematic mechanical pass (N2 blank 1W/1M, N3 vol≥$50M, N4 Open% −10/+8, N5 LTF-aware
momentum, N6 DB-Red exclusion only — **N1 catalyst-freshness cannot be checked mechanically**)
across the full July–September dataset found **12 distinct "Listing Radar Alert" events**,
up from the single MARSCOIN case in v6.6/v7.0. Full table in
`backtest/results/rule_n_events.csv`.

**Two of the twelve are false positives, verified by live search — not new coins at all:**
- `SKHYUSDT.P` (alert 2026-07-13) = **SK Hynix (SKHYB)**, a tokenized-stock listing Binance
  announced for spot trading the same day — a tokenized equity, not a cryptocurrency.
- `UNITREEUSDT.P` (alert 2026-08-20) = **Yushu Technology / UNITREE**, a tokenized-equity
  perpetual (robotics company stock), not a crypto listing either.

This is a real gap in N6: the current mechanical exclusion only checks DB-Red, not tokenized
equities, because Rule N's own tokenized-equity heuristic (§2A) needs 1W/1M values to evaluate —
and blank 1W/1M is precisely N2's trigger condition, so the heuristic can never fire for exactly
the population Rule N is scanning. **Recommendation: N6 needs its own tokenized-equity check
that doesn't depend on 1W/1M being present** (e.g., cross-referencing the Description field
against known tokenized-equity issuers, or requiring manual identity confirmation before any
alert involving an unfamiliar ticker is upgraded to Confirmed Watch).

**One of the twelve is confirmed genuine and independently verified:** `NIULAIUSDT.P` — Binance
Futures listed the NIULAI perpetual 2026-08-30 11:30 UTC (a Binance Alpha token), and the alert
fired 2026-09-02, comfortably inside the 72h N1 freshness window. This is a second real,
verified case alongside MARSCOIN — but its forward return was modest and mixed (+4.3% at +2h,
then −12.2% at +6h, −6.2% at +24h), nothing like MARSCOIN's blow-off.

**Forward-return summary (n=12, N1 unverified for the remaining 10):**

| Horizon | Win rate | Avg return | Profit factor |
|---|---|---|---|
| +2h | 41.7% | −0.05% | 0.94 |
| +6h | 41.7% | −0.07% | 0.98 |
| +24h | 58.3% | +6.18% | 3.03 |

The +24h number looks good until the concentration check §6E itself requires:

**MARSCOIN alone is 75.4% of total positive result at +24h (80.4% after removing the two
tokenized-equity false positives).** Remove it, and the average +24h return flips to **−0.84%**
and the profit factor drops to **0.75** (unprofitable). This is the single most important
finding of this deep-dive: tripling the event count from 1 to 12 did not change the underlying
conclusion — Rule N's apparent edge is still, in substance, one case. The admission test's own
"no single symbol > 20% of total positive result" rule, applied honestly, says Rule N does not
pass yet, and n=12 is still well short of the 20-30 event bar regardless.

## Bottom line for v7.1

Neither rule is ready to size real capital. What changed is the quality of the "no" — from "we
haven't checked" to "we checked, and here's exactly what's missing and why." Concretely:
Rule F gained a verified universe, a quantified LV-Guard trade-off, one governance action item
(TAC), and one real out-of-sample warning; Rule N gained an 11x larger event log, one
methodology fix needed (tokenized-equity false positives), one new verified case (NIULAI), and
a concentration-test failure that explains *why* n=12 still isn't enough. All of this is
research toward §6E/§6F, not a pass of either.
