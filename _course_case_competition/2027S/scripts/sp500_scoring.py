"""Scoring rule of the Spring 2027 QM47400 Course Case Competition (S&P 500 forecast).

This file is the single published definition of the competition metric. The same function is
(1) pasted into the Kaggle custom-metric notebook of the practice round, (2) used by the host to
score the live round, and (3) reproduced in nb18 so teams score their own walk-forward backtests.

Target. For a forecast origin T (the close of a trading day) and a horizon h (trading days),
    y(T, h) = 100 * ln( P[T+h] / P[T] )          -- the cumulative log return in percent,
where P is the S&P 500 closing level and T+h is the h-th trading day after T.

Forecast. For every (origin, horizon) row a team submits five quantiles of y:
    q10, q25, q50, q75, q90   (non-decreasing).

Score (lower is better). For each row,
    row loss = mean over the five quantiles of pinball_tau(y - q_tau)  /  (s_T * sqrt(h)),
where pinball_tau(u) = max(tau * u, (tau - 1) * u) and s_T is the standard deviation (ddof = 1) of
the 252 daily log returns in percent that end at the origin close (known before the forecast is
made). Dividing by s_T * sqrt(h) puts every horizon and every origin on the scale of a typical
move. The score averages the row losses within each origin, then averages the origins.

Benchmark. The random walk with one-year volatility: q_tau = z_tau * s_T * sqrt(h), where z_tau is
the standard-normal quantile (median zero).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

TAUS = np.array([0.10, 0.25, 0.50, 0.75, 0.90])
QCOLS = ["q10", "q25", "q50", "q75", "q90"]
HORIZONS = [1, 5, 10, 15, 20]
VOL_WINDOW = 252
Z = np.array([-1.2815515655446004, -0.6744897501960817, 0.0, 0.6744897501960817, 1.2815515655446004])


class ParticipantVisibleError(Exception):
    """Errors whose message a participant may see (Kaggle convention)."""


def make_id(origin, h):
    return f"{pd.Timestamp(origin):%Y-%m-%d}_h{int(h):02d}"


def score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float:
    """Scaled pinball loss. `solution` columns: id, y, h, scale, origin (+ Usage on Kaggle).
    `submission` columns: id, q10, q25, q50, q75, q90."""
    rid = row_id_column_name
    missing_cols = [c for c in [rid] + QCOLS if c not in submission.columns]
    if missing_cols:
        raise ParticipantVisibleError(f"Submission is missing columns: {missing_cols}")
    extra = [c for c in submission.columns if c not in [rid] + QCOLS]
    if extra:
        raise ParticipantVisibleError(f"Submission has unexpected columns: {extra}")
    if submission[rid].duplicated().any():
        raise ParticipantVisibleError("Submission has duplicate ids")
    sol_ids, sub_ids = set(solution[rid].astype(str)), set(submission[rid].astype(str))
    if sol_ids != sub_ids:
        n_miss, n_extra = len(sol_ids - sub_ids), len(sub_ids - sol_ids)
        raise ParticipantVisibleError(f"Ids do not match the expected rows ({n_miss} missing, {n_extra} unexpected)")
    sub = submission.copy()
    sub[rid] = sub[rid].astype(str)
    sub = sub.set_index(rid)
    sol = solution.copy()
    sol[rid] = sol[rid].astype(str)
    try:
        q = sub.loc[sol[rid], QCOLS].to_numpy(dtype=float)
    except (TypeError, ValueError):
        raise ParticipantVisibleError("Quantile columns must be numeric")
    if not np.isfinite(q).all():
        raise ParticipantVisibleError("Quantiles must be finite numbers (no blanks, NaN or inf)")
    if (np.diff(q, axis=1) < 0).any():
        raise ParticipantVisibleError("Quantiles must be non-decreasing: q10 <= q25 <= q50 <= q75 <= q90")
    y = sol["y"].to_numpy(dtype=float)
    h = sol["h"].to_numpy(dtype=float)
    scale = sol["scale"].to_numpy(dtype=float)
    u = y[:, None] - q
    pinball = np.maximum(TAUS * u, (TAUS - 1.0) * u)
    row_loss = pinball.mean(axis=1) / (scale * np.sqrt(h))
    per_origin = pd.Series(row_loss).groupby(sol["origin"].astype(str).to_numpy()).mean()
    return float(per_origin.mean())


def log_returns_pct(close: pd.Series) -> pd.Series:
    """Daily log returns in percent from a Series of closing levels indexed by date."""
    return 100.0 * np.log(close).diff().dropna()


def origin_scale(close: pd.Series, origin) -> float:
    """s_T: SD of the last 252 daily log returns (percent) ending at the origin close."""
    r = log_returns_pct(close.loc[:pd.Timestamp(origin)])
    if len(r) < VOL_WINDOW:
        raise ValueError(f"Need {VOL_WINDOW} returns before {origin}; have {len(r)}")
    return float(r.iloc[-VOL_WINDOW:].std(ddof=1))


def truth_rows(close: pd.Series, origins, horizons=HORIZONS) -> pd.DataFrame:
    """Solution rows (id, y, h, scale, origin, target_date) for the origins whose futures are known."""
    close = close.dropna().sort_index()
    dates = close.index
    rows = []
    for o in origins:
        o = pd.Timestamp(o)
        if o not in dates:
            raise ValueError(f"Origin {o:%Y-%m-%d} is not a trading day in the data")
        i = dates.get_loc(o)
        s = origin_scale(close, o)
        for h in horizons:
            if i + h >= len(dates):
                raise ValueError(f"Horizon {h} after {o:%Y-%m-%d} is not in the data yet")
            rows.append({"id": make_id(o, h), "y": 100.0 * np.log(close.iloc[i + h] / close.iloc[i]),
                         "h": h, "scale": s, "origin": f"{o:%Y-%m-%d}",
                         "target_date": f"{dates[i + h]:%Y-%m-%d}"})
    return pd.DataFrame(rows)


def benchmark_rows(ids_h_scale: pd.DataFrame) -> pd.DataFrame:
    """Random-walk benchmark quantiles for rows with columns id, h, scale."""
    out = pd.DataFrame({"id": ids_h_scale["id"].to_numpy()})
    sd = ids_h_scale["scale"].to_numpy(dtype=float) * np.sqrt(ids_h_scale["h"].to_numpy(dtype=float))
    for c, z in zip(QCOLS, Z):
        out[c] = z * sd
    return out


def skill_vs_benchmark(team_score: float, benchmark_score: float) -> float:
    """1 - team/benchmark: positive = better than the random walk, 0 = equal, negative = worse."""
    return 1.0 - team_score / benchmark_score


def _self_test():
    # hand-computed example: one origin, two rows
    sol = pd.DataFrame({"id": ["a", "b"], "y": [2.0, 0.0], "h": [1, 4], "scale": [1.0, 1.0], "origin": ["o", "o"]})
    sub = pd.DataFrame({"id": ["a", "b"], "q10": [-3.0, 0.0], "q25": [-1.0, 0.0], "q50": [0.0, 0.0],
                        "q75": [1.0, 0.0], "q90": [3.0, 0.0]})
    # row a: u = [5, 3, 2, 1, -1] -> pinball = [.5, .75, 1.0, .75, .1] -> mean .62 ; row b: 0
    assert np.isclose(score(sol, sub, "id"), (0.62 + 0.0) / 2), score(sol, sub, "id")
    assert np.isclose(score(sol, sub.iloc[::-1].reset_index(drop=True), "id"), 0.31)
    perfect = sub.copy()
    perfect[QCOLS] = np.repeat(sol["y"].to_numpy()[:, None], 5, axis=1)
    assert score(sol, perfect, "id") == 0.0
    for bad_kind in ["crossing", "nan", "missing", "duplicate", "extra"]:
        bad = sub.copy()
        if bad_kind == "crossing":
            bad.loc[0, "q10"] = 9.0
        elif bad_kind == "nan":
            bad.loc[0, "q90"] = np.nan
        elif bad_kind == "missing":
            bad = bad.iloc[:1]
        elif bad_kind == "duplicate":
            bad.loc[1, "id"] = "a"
        elif bad_kind == "extra":
            bad["note"] = "x"
        try:
            score(sol, bad, "id")
        except ParticipantVisibleError:
            pass
        else:
            raise AssertionError(bad_kind)
    print("sp500_scoring self-test: all checks passed")


if __name__ == "__main__":
    _self_test()
