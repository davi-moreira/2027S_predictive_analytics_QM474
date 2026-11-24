#!/usr/bin/env python3
"""Score the LIVE round of the S&P 500 competition (host-run, after the close of Fri Apr 23, 2027).

Kaggle freezes a community competition's answer key at launch, so the live month cannot be
scored on Kaggle. The host scores it with this script, which uses exactly the published metric
(`sp500_scoring.score`), and posts the standings on Brightspace.

Usage (from the repo root):
    python _course_case_competition/2027S/scripts/score_live_round.py \
        --submissions <folder with NN_live_forecast.csv files> [--csv closes.csv] [--out <folder>]

The folder holds the files downloaded from the Brightspace assignment, one per team, named
`NN_live_forecast.csv` (NN = two-digit group number). Every file is validated with the same rules
as Kaggle; an invalid file is listed with the reason and ranked last. Output (gitignored by
default, `_adm/kaggle_sp500_2027S/live_results/`): standings.csv (rank, group, score, skill vs the
random walk, points) and per_row_losses.csv (each team's loss by horizon), plus a printed summary.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import sp500_scoring as sc  # noqa: E402
from build_competition_files import LIVE_ORIGIN, load_close  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
RANK_POINTS = 5.0        # live-round rank component (points out of the competition's 100)


def rank_points(ranks: pd.Series, n: int) -> pd.Series:
    """Top team RANK_POINTS, last team 0, equal steps in between; ties share the average rank."""
    if n == 1:
        return pd.Series(RANK_POINTS, index=ranks.index)
    return RANK_POINTS * (n - ranks) / (n - 1)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--submissions", required=True)
    ap.add_argument("--csv", help="CSV of daily closes (Date, Close); default: Yahoo Finance via yfinance")
    ap.add_argument("--origin", default=str(LIVE_ORIGIN.date()), help="live origin (default 2027-03-25)")
    ap.add_argument("--out", default=str(REPO / "_adm" / "kaggle_sp500_2027S" / "live_results"))
    a = ap.parse_args()

    close = load_close(a.csv)
    sol = sc.truth_rows(close, [a.origin])
    print("Live truth (percent log return from the origin close):")
    print(sol[["id", "target_date", "y", "scale"]].round(4).to_string(index=False))
    bench = sc.benchmark_rows(sol)
    bench_score = sc.score(sol, bench, "id")

    rows, per_row = [], []
    for f in sorted(Path(a.submissions).glob("*.csv")):
        m = re.match(r"^(\d{2})_live_forecast\.csv$", f.name)
        group = f"Group {m.group(1)}" if m else f"(misnamed) {f.name}"
        try:
            sub = pd.read_csv(f)
            s = sc.score(sol, sub, "id")
            rows.append({"group": group, "file": f.name, "valid": True, "score": s,
                         "skill_vs_random_walk": sc.skill_vs_benchmark(s, bench_score), "problem": ""})
            q = sub.set_index("id").loc[sol["id"], sc.QCOLS].to_numpy(float)
            u = sol["y"].to_numpy()[:, None] - q
            loss = np.maximum(sc.TAUS * u, (sc.TAUS - 1) * u).mean(axis=1) / (
                sol["scale"].to_numpy() * np.sqrt(sol["h"].to_numpy()))
            per_row += [{"group": group, "h": h, "loss": l} for h, l in zip(sol["h"], loss)]
        except Exception as e:  # invalid file: keep it in the table, ranked last
            rows.append({"group": group, "file": f.name, "valid": False, "score": np.nan,
                         "skill_vs_random_walk": np.nan, "problem": str(e)})

    st = pd.DataFrame(rows)
    valid = st[st.valid].copy()
    valid["rank"] = valid["score"].rank(method="average")
    valid["rank_points"] = rank_points(valid["rank"], len(valid))
    st = st.merge(valid[["file", "rank", "rank_points"]], on="file", how="left")
    st["rank_points"] = st["rank_points"].fillna(0.0)
    st = st.sort_values(["valid", "score"], ascending=[False, True])
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    st.to_csv(out / "standings.csv", index=False)
    pd.DataFrame(per_row).pivot(index="group", columns="h", values="loss").to_csv(out / "per_row_losses.csv")
    print(f"\nRandom-walk benchmark score: {bench_score:.4f}")
    print(st[["group", "valid", "score", "skill_vs_random_walk", "rank", "rank_points", "problem"]]
          .round(4).to_string(index=False))
    beat = int((valid["score"] < bench_score).sum())
    print(f"\n{beat} of {len(valid)} valid teams beat the random-walk benchmark this month.")
    print(f"Results written to {out}")


if __name__ == "__main__":
    main()
