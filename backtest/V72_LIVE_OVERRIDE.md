# v7.2 — Rule N and Rule F go live (trader override, not a passed admission test)

**Instruction received:** "ปรับทั้ง 2 กฏให้เป็นเทรดจริงตั้ง stop loss 20%" — convert both Rule N and
Rule F to live trading, stop-loss 20%.

**Given before implementing:** Rule F's only new out-of-sample test (September) lost money
(-11.5%, Sharpe -9.34). Rule N's entire backtested edge is one trade (MARSCOIN) — the other 11
of 12 logged events lose money on their own. The trader chose to proceed anyway, explicitly
accepting these risks. This document records exactly what was implemented and exactly what it is
backtested to do, so nothing here is asserted more confidently than the data supports.

## Rule F (short) — live parameters

```
Entry   : highest-ranked F1-F6 candidate each scan
Side    : SHORT
Stop    : 20% adverse
TP      : none fixed -- rotate at next scan or 24h time-stop
Size    : risk 0.50% of equity -> ~2.5% notional
```

Backtested (Jul-Sep 2026, full Majors Whitelist, single-highest-ranked candidate per scan,
sequential, realistic sizing): **+15.4% total return, profit factor 1.45, max drawdown -3.3%,
win rate 59.6%.** PF 1.45 is below this process's own 1.50 admission bar (§6F in the skill).
Reproduce: `backtest/rule_f_v71_analysis.py` (sim function inline, stop=0.20, risk=0.50).

## Rule N (long) — live parameters

```
Entry   : first Listing Radar Alert (N1-N6 pass)
Side    : LONG
Stop    : 20% adverse
TP      : none fixed (a 30% TP was tested and rejected -- it would have capped MARSCOIN's
          real move at +30% instead of the +288% a 72h hold captured)
Time-stop: 72h backstop
Size    : risk 0.50% of equity -> ~2.5% notional
```

Backtested on the 12 events in `results/rule_n_events.csv`, simulated with exactly these
entry/stop/time-stop rules (`results/rule_n_live_sim.csv`):

| | All 12 events | Excluding MARSCOIN (11 events) |
|---|---|---|
| Win rate | 33.3% | 27.3% |
| Average return per trade | +21.1% | **-3.2%** |
| Profit factor | 5.72 | **0.34** |

**The entire positive result is one trade.** Trading Rule N live is, in substance, a bet that a
MARSCOIN-sized catalyst recurs often enough to be worth the eleven smaller losses along the way
— a bet on a base rate this backtest has no real evidence for (n=12, one hit), not a bet the
Sharpe/PF numbers above actually support on their own.

## What did not change

STEP 6E and STEP 6F in the skill still list every unmet admission-test checkbox, unedited. Going
live did not check any of them off — it accepted the gaps as a deliberate, informed risk
decision. Q2, S, the Participation-Ratio ladder, and exits are untouched. Position sizes (2.5%
notional each, 0.50% risk) are kept small specifically because neither rule has cleared its own
bar yet.
