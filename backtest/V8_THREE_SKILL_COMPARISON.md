# v8.0 — a real three-skill comparison (v6.6 vs v7.2 vs momentum-confluence-playbook)

**Instruction received:** backtest all three skills against each other on the same Jul-Aug 2026
data, identify each one's genuine strengths, merge them, and only save the result as v8.0 if it
backtests at least 20% ahead of all three predecessors — otherwise redesign and retest until it
does.

## What each skill actually is, for backtest purposes

- **v6.6**: Rule Q2 (long, trend-geometry entry) + Rule S (short, mirror) + Rule N (new-listing
  radar, watch-only — zero P&L by construction). Q2/S had never actually been backtested against
  this repo's Jul-Aug screener data before this comparison — every prior version *claimed* they
  were tested "across five to six major version cycles," but no script here had run them.
- **v7.2**: v6.6's Q2/S unchanged, + Rule F (fade-the-pump short) and Rule N moved to LIVE by
  explicit trader override (20% SL, 0.50% risk each). Rule N still contributes $0 in the Jul-Aug
  window specifically — its only real events (MARSCOIN, NIULAI, etc.) are all September or later.
- **momentum-confluence-playbook v3**: a discretionary chart-pattern skill built from TradingView
  screenshots (step-line, oscillator, MA-cross, histogram, trend-strength gauge). These indicators
  are computed from OHLCV candles on a charting platform — **not present in the Mai_BI_* screener
  exports this whole backtest suite runs on.** It cannot be backtested against this data at all,
  and that was already established multiple times before this comparison. It contributes zero
  trades, by construction, not by underperforming.

## What was actually tested (see `rule_q2s_backtest.py`, `rule_q2s_trail_variant.py`)

1. Coded Rule Q2/S mechanically for the first time (entry geometry, PR ladder, cooldown, path-
   dependent SL/TP/72h-time-stop simulation) and ran it against Jul-Aug 2026 (full Majors
   Whitelist excluded): **n=85 trades, PF 3.77, +32.15% realistic total return.**
2. Extracted the one idea from the chart playbook that doesn't depend on its own chart indicators:
   its MARSCOIN/ZEC worked examples argue a fixed take-profit caps a real trend for no reason, and
   a trend that keeps proving itself should be trailed, not exited, at the first exhaustion
   signal. Q2/S's own price path is enough to test this without any chart indicator: replace the
   fixed +30%/-30% TP with an armed trail (arm at +20% running profit, exit if it gives back 15
   points from peak). Result: **+71.29% total return, PF 6.58**, on the same 85 trades — more
   than double the return, better PF, almost the same drawdown.
3. Checked robustness: nearby arm/giveback parameter pairs (10%/6% through 30%/20%) all land in a
   +60-72% plateau, not a knife-edge. Checked concentration: one trade (TUTUSDT.P, +463.9% gross)
   is 34.7% of the trailing exit's gains — above this lineage's own 20% guideline — but removing
   it still leaves +39.05% (PF 4.30), still ahead of the old fixed-TP baseline's own +32.15%.
4. Pooled the full systems sequentially at each rule's own risk sizing:

| System | Jul-Aug 2026 pooled return | vs v7.2 | vs v6.6 |
|---|---:|---:|---:|
| v6.6 (Q2+S fixed TP, Rule N watch) | +32.15% | −38.8% | — |
| v7.2 (+ Rule F live) | +52.53% | — | +63.4% |
| **v8.0 (Q2+S trailing exit + Rule F live)** | **+97.71%** | **+86.0%** | **+204%** |

Both comfortably clear the trader's ">=20% better than all three" bar, on the first design
tested. That speed is a fact about Q2/S never having been backtested before (real edge was
sitting uncounted in the exit rule alone), not evidence this process has generally improved.

## What did NOT change

Q2/S entry geometry, the PR ladder, every exclusion list, and Rule N/F's entire live status,
entries, stop-losses, and sizing (§13 of the skill) are byte-for-byte from v7.2. The only rule
change in v8.0 is Q2/S's winning-trade exit. Full detail, all caveats, and the forward-validation
plan (§6G, new in v8.0) are in `skill/Hybrid_AI_Trading_Process_v8_0_SKILL.md`.
