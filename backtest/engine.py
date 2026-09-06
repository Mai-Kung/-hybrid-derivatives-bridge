"""Cross-sectional long/short backtest engine for the altcoin screener snapshots.

At every scan timestamp we rank the liquid altcoin universe by one signal
column, go long the top N / short the bottom N (or vice versa for a
mean-reversion variant), hold to the *next* scan of each name, and rebalance
fully every period. Returns are dollar-neutral (equal capital long and
short) unless side is restricted to "long" or "short" only.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

MAX_GAP_HOURS = 8.0  # drop symbol-periods whose "next snapshot" is a data gap


@dataclass
class StrategyConfig:
    signal: str
    n: int
    direction: str  # "momentum" (long winners/short losers) or "reversion"
    side: str  # "long_short", "long_only", "short_only"
    cost_bps_per_leg: float = 5.0  # round-trip taker+slippage assumption per leg, in bps


def _period_returns(df: pd.DataFrame, cfg: StrategyConfig) -> pd.Series:
    valid = df[(df["gap_hours"] <= MAX_GAP_HOURS) & df[cfg.signal].notna() & df["fwd_ret"].notna()]
    cost = cfg.cost_bps_per_leg / 10_000.0

    def per_period(g: pd.DataFrame) -> float | None:
        if len(g) < 2 * cfg.n:
            return None
        ranked = g.sort_values(cfg.signal)
        losers, winners = ranked.iloc[: cfg.n], ranked.iloc[-cfg.n :]
        long_leg, short_leg = (winners, losers) if cfg.direction == "momentum" else (losers, winners)

        long_ret = long_leg["fwd_ret"].mean() - cost
        short_ret = -short_leg["fwd_ret"].mean() - cost

        if cfg.side == "long_only":
            return long_ret
        if cfg.side == "short_only":
            return short_ret
        return 0.5 * long_ret + 0.5 * short_ret

    out = valid.groupby("datetime", sort=True).apply(per_period, include_groups=False)
    return out.dropna()


def metrics_from_returns(returns: pd.Series, periods_per_year: float) -> dict:
    if len(returns) == 0:
        return {"n_periods": 0}
    equity = (1.0 + returns).cumprod()
    total_return = equity.iloc[-1] - 1.0
    years = len(returns) / periods_per_year
    cagr = (equity.iloc[-1]) ** (1.0 / years) - 1.0 if years > 0 else np.nan
    vol = returns.std(ddof=1)
    sharpe = (returns.mean() / vol) * np.sqrt(periods_per_year) if vol > 0 else np.nan
    running_max = equity.cummax()
    drawdown = equity / running_max - 1.0
    max_dd = drawdown.min()
    win_rate = (returns > 0).mean()
    return {
        "n_periods": len(returns),
        "total_return_pct": total_return * 100,
        "cagr_pct": cagr * 100,
        "sharpe": sharpe,
        "max_drawdown_pct": max_dd * 100,
        "win_rate_pct": win_rate * 100,
        "avg_period_ret_bps": returns.mean() * 10_000,
    }


def run_backtest(df: pd.DataFrame, cfg: StrategyConfig, periods_per_year: float) -> tuple[pd.Series, dict]:
    returns = _period_returns(df, cfg)
    m = metrics_from_returns(returns, periods_per_year)
    m.update({"signal": cfg.signal, "n": cfg.n, "direction": cfg.direction, "side": cfg.side})
    return returns, m


def estimate_periods_per_year(df: pd.DataFrame) -> float:
    span_days = (df["datetime"].max() - df["datetime"].min()).total_seconds() / 86400.0
    n_periods = df["datetime"].nunique()
    return n_periods / span_days * 365.25
