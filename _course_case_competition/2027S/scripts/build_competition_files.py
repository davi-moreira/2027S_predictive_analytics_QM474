#!/usr/bin/env python3
"""Build the Kaggle practice-round files and the live-round template for the S&P 500 competition.

Nothing here is uploaded anywhere: the files land in a GITIGNORED folder (default
`_adm/kaggle_sp500_2027S/` at the repo root) and Davi uploads them to Kaggle by hand, following
`kaggle_host_setup_guide.md`. The S&P 500 values themselves are never written to a tracked path:
index data belong to S&P Dow Jones Indices, so the course does not republish them.

Usage (from the repo root):
    python _course_case_competition/2027S/scripts/build_competition_files.py            # Yahoo via yfinance
    python _course_case_competition/2027S/scripts/build_competition_files.py --csv my_closes.csv
    python ... --n-practice 26 --last-practice-origin 2027-01-28

Outputs (in --out):
    practice/solution.csv           hidden answer key for Kaggle (id, y, h, scale, origin, target_date, Usage)
    practice/sample_submission.csv  the random-walk benchmark in the submission format (valid file)
    practice/practice_origins.csv   the origins and horizons, with target dates (no index values)
    live/live_template.csv          the five live rows teams must fill (ids only)
    live/live_calendar.csv          live horizons and their target dates (2027 NYSE calendar)
    build_report.txt                what was built, benchmark score, self-checks
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import sp500_scoring as sc  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
LIVE_ORIGIN = pd.Timestamp("2027-03-25")          # Thu; Fri Mar 26, 2027 is Good Friday (NYSE closed)
# NYSE holidays Jan-May 2027, from https://www.nyse.com/trade/hours-calendars (checked 2026-11-24)
NYSE_HOLIDAYS_2027 = pd.to_datetime(["2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31"])


def load_close(csv_path: str | None, start: str = "2015-01-01") -> pd.Series:
    if csv_path:
        raw = pd.read_csv(csv_path)
        date_col = [c for c in raw.columns if c.lower() in ("date", "observation_date")][0]
        val_col = [c for c in raw.columns if c.lower() in ("close", "sp500", "adj close")][0]
        s = pd.Series(pd.to_numeric(raw[val_col], errors="coerce").to_numpy(),
                      index=pd.to_datetime(raw[date_col]))
    else:
        import yfinance as yf
        s = yf.download("^GSPC", start=start, auto_adjust=False, progress=False)["Close"].squeeze()
        s.index = pd.to_datetime(s.index)
        if s.index.tz is not None:
            s.index = s.index.tz_localize(None)
    return s.dropna().astype(float).sort_index()


def weekly_origins(close: pd.Series, n: int, last: str | None) -> list[pd.Timestamp]:
    """Thursdays that are trading days and whose 20-day future is in the data."""
    dates = close.index
    usable = dates[: len(dates) - max(sc.HORIZONS)]
    thursdays = [d for d in usable if d.weekday() == 3]
    if last:
        thursdays = [d for d in thursdays if d <= pd.Timestamp(last)]
    if len(thursdays) < n:
        raise SystemExit(f"Only {len(thursdays)} usable Thursdays; asked for {n}")
    return thursdays[-n:]


def live_calendar() -> pd.DataFrame:
    days = pd.bdate_range("2027-03-26", "2027-05-07")
    days = [d for d in days if d not in set(NYSE_HOLIDAYS_2027)]
    return pd.DataFrame({"id": [sc.make_id(LIVE_ORIGIN, h) for h in sc.HORIZONS],
                         "h": sc.HORIZONS,
                         "target_date": [f"{days[h - 1]:%Y-%m-%d}" for h in sc.HORIZONS]})


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", help="CSV of daily closes (Date, Close); default: Yahoo Finance via yfinance")
    ap.add_argument("--n-practice", type=int, default=26, help="number of weekly practice origins")
    ap.add_argument("--last-practice-origin", default=None, help="YYYY-MM-DD; default: latest usable Thursday")
    ap.add_argument("--public-share", type=float, default=0.5,
                    help="share of the EARLIEST practice origins on the public leaderboard")
    ap.add_argument("--out", default=str(REPO / "_adm" / "kaggle_sp500_2027S"))
    a = ap.parse_args()

    out = Path(a.out)
    (out / "practice").mkdir(parents=True, exist_ok=True)
    (out / "live").mkdir(parents=True, exist_ok=True)
    close = load_close(a.csv)
    origins = weekly_origins(close, a.n_practice, a.last_practice_origin)

    sol = sc.truth_rows(close, origins)
    n_public = int(round(a.public_share * len(origins)))
    public = {f"{o:%Y-%m-%d}" for o in origins[:n_public]}
    sol["Usage"] = np.where(sol["origin"].isin(public), "Public", "Private")
    sol[["id", "y", "h", "scale", "origin", "target_date", "Usage"]].round(6).to_csv(
        out / "practice" / "solution.csv", index=False)

    bench = sc.benchmark_rows(sol).round(6)
    bench.to_csv(out / "practice" / "sample_submission.csv", index=False)
    sol[["id", "origin", "h", "target_date"]].to_csv(out / "practice" / "practice_origins.csv", index=False)

    cal = live_calendar()
    cal.to_csv(out / "live" / "live_calendar.csv", index=False)
    pd.DataFrame({"id": cal["id"], **{c: np.nan for c in sc.QCOLS}}).to_csv(
        out / "live" / "live_template.csv", index=False)

    # self-checks
    bench_score = sc.score(sol, bench, "id")
    perfect = bench.copy()
    perfect[sc.QCOLS] = np.repeat(sol["y"].to_numpy()[:, None], 5, axis=1)
    assert sc.score(sol, perfect, "id") == 0.0
    pub_rows, priv_rows = sol[sol.Usage == "Public"], sol[sol.Usage == "Private"]
    lines = [
        f"data: {close.index[0]:%Y-%m-%d} -> {close.index[-1]:%Y-%m-%d} ({len(close)} closes), source: "
        f"{'CSV ' + a.csv if a.csv else 'Yahoo Finance (yfinance ^GSPC)'}",
        f"practice origins: {len(origins)} Thursdays, {origins[0]:%Y-%m-%d} -> {origins[-1]:%Y-%m-%d}; "
        f"public = first {n_public}, private = last {len(origins) - n_public}",
        f"solution rows: {len(sol)} (public {len(pub_rows)}, private {len(priv_rows)})",
        f"random-walk benchmark score, all rows: {bench_score:.4f}; public: "
        f"{sc.score(pub_rows, bench[bench.id.isin(pub_rows.id)], 'id'):.4f}; private: "
        f"{sc.score(priv_rows, bench[bench.id.isin(priv_rows.id)], 'id'):.4f}",
        "perfect submission scores 0.0: OK",
        "live calendar (origin = close of Thu 2027-03-25):",
        cal.to_string(index=False),
    ]
    (out / "build_report.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"\nfiles written to {out}")


if __name__ == "__main__":
    main()
