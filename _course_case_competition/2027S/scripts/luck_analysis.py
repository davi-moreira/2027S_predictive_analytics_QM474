#!/usr/bin/env python3
"""How much of a one-month ranking is luck? Evidence for the competition's grade weights.

Real S&P 500 data (Yahoo Finance via yfinance, or --csv), every Thursday origin from 2019 on with a
full 20-day future, the competition's exact metric (sp500_scoring.score). For pairs of forecasters,
prints how often the one that is better ON AVERAGE also wins (a) a single origin — the live round —
and (b) a block of 26 consecutive weekly origins — the practice round.

Usage (repo root): python _course_case_competition/2027S/scripts/luck_analysis.py [--csv closes.csv] [--end 2026-10-30]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import sp500_scoring as sc  # noqa: E402
from build_competition_files import load_close  # noqa: E402


def ewma(x, lam=0.94, window=252):
    x = x[-window:]
    w = lam ** np.arange(len(x))[::-1]
    return np.sqrt(np.sum(w * x ** 2) / w.sum())


FORECASTERS = {
    "Benchmark": lambda r, h: sc.Z * r[-252:].std(ddof=1) * np.sqrt(h),
    "EWMA": lambda r, h: sc.Z * ewma(r) * np.sqrt(h),
    "Drift+EWMA": lambda r, h: r[-1260:].mean() * h + sc.Z * ewma(r) * np.sqrt(h),
    "Overconfident (half width)": lambda r, h: 0.5 * sc.Z * r[-252:].std(ddof=1) * np.sqrt(h),
    "Point only (all quantiles 0)": lambda r, h: np.zeros(5),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--start", default="2019-01-01")
    ap.add_argument("--end", default="2026-10-30")
    a = ap.parse_args()
    close = load_close(a.csv, start="2013-01-01").loc[:a.end]
    ret = sc.log_returns_pct(close)
    dates = close.index
    origins = [d for d in dates[:-20] if d.weekday() == 3 and d >= pd.Timestamp(a.start)]
    sol = sc.truth_rows(close, origins)
    per = {}
    for name, f in FORECASTERS.items():
        s = []
        for o in origins:
            r = ret.loc[:o].to_numpy()
            sub = pd.DataFrame([[sc.make_id(o, h), *np.sort(f(r, h))] for h in sc.HORIZONS], columns=["id"] + sc.QCOLS)
            s.append(sc.score(sol[sol.origin == f"{o:%Y-%m-%d}"], sub, "id"))
        per[name] = s
    per = pd.DataFrame(per, index=origins)
    print(f"{len(origins)} Thursday origins, {origins[0]:%Y-%m-%d} -> {origins[-1]:%Y-%m-%d}")
    print("Mean score (lower is better):")
    print(per.mean().round(4).to_string())
    pairs = [("EWMA", "Benchmark"), ("Benchmark", "Overconfident (half width)"),
             ("EWMA", "Overconfident (half width)"), ("Benchmark", "Drift+EWMA"),
             ("Benchmark", "Point only (all quantiles 0)")]
    print("\nP(first beats second) — single origin | 26-origin block (non-overlapping blocks):")
    for x, y in pairs:
        single = (per[x] < per[y]).mean()
        blocks = [per[x].iloc[i:i + 26].mean() < per[y].iloc[i:i + 26].mean()
                  for i in range(0, len(per) - 25, 26)]
        print(f"  {x:>28} vs {y:<28} {single:.3f} | {np.mean(blocks):.3f} (n={len(blocks)})")


if __name__ == "__main__":
    main()
