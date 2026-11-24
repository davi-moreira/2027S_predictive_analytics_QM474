# Course Case Competition — Reference (Spring 2027, S&P 500 Forecast)

**Course:** QM47400 — Predictive Analytics · **Term:** Spring 2027 (sections 001 and 002, one shared competition)
**Instructor:** Professor Davi Moreira
**Competition title:** Spring 2027 QM47400 Case Competition — S&P 500 Forecast
**Weight:** 20% of the course grade; peer evaluation is 20% of the competition.

> **This file is the canonical reference for the Spring 2027 competition.** The syllabus, the schedule
> (`scripts/build_2027S_calendar.py`), the Brightspace assignment text, nb16, nb18 and the student
> instructions (`course_case_competition_instructions.md`) must agree with it. Change this file first.
> Built 2026-11-24 by the `sp500-competition` session (Claude, with a partial Codex partner run).

---

## 1. Decision record

- **2026-11-24 (Davi):** the competition switches from bank churn (Kaggle classification) to a **group
  forecasting competition on the S&P 500 with current data**, run with/after the time-series topic, with
  a new nb18. Teams = final-project groups, Kaggle team name `Group NN`. Calendar: nb16 Mon Mar 1,
  nb18 Wed Mar 3 (kickoff), nb19 Mon Mar 8, Wed Mar 10 and Fri Mar 12 virtual work sessions.
- **This design (2026-11-24, for Davi to confirm):** quantile forecasts of the cumulative log return at
  five horizons; scaled pinball loss; random-walk benchmark; an **ungraded Kaggle practice round** on
  past Thursdays; a **host-scored live round** (Kaggle cannot rescore a community competition after
  the solution is known — §5); grade weights that put 5 of 100 points on rank (§7).

## 2. Calendar (all times Eastern)

| Date | Event | Notes |
|---|---|---|
| Wed Mar 3 | Kickoff (nb18); Kaggle practice round opens | Davi launches the practice competition before class |
| Sun Mar 7, 11:59 PM | Kaggle team setup due; Kaggle **team-merger deadline** | Same day: midpoint peer evaluation (formative) |
| Wed Mar 10, Fri Mar 12 | Virtual work sessions | Competition + final project |
| Mar 15–20 | Spring break | |
| Thu Mar 25, 11:59 PM | Practice round closes | See §6 on Kaggle deadline times |
| Thu Mar 25, close | **Live origin** $T$ | Last information a forecast may use |
| Fri Mar 26, 11:59 PM | **Live forecast + code + memo due (Brightspace)** | NYSE closed (Good Friday) — verified, §4 |
| Mon Mar 29 – Fri Apr 23 | Live window, 20 trading days | No NYSE holiday inside (verified) |
| Sat Apr 24 – Sun Apr 25 | Host scores the live round (§8) | Yahoo has Friday's close the same evening |
| **Sun Apr 25** | Standings posted on Brightspace | If the data source lags, post Mon Apr 26 |
| Fri Apr 30 | Final peer evaluation | Carries the 20% peer share |

## 3. The task — exact definitions

- **Target:** $y(T,h) = 100\ln(P_{T+h}/P_T)$, $P$ = S&P 500 daily close, $T+h$ = the $h$-th trading day after $T$.
- **Horizons:** $h \in \{1,5,10,15,20\}$. Live: $T$ = Thu 2027-03-25; targets Mon Mar 29, Fri Apr 2, Fri Apr 9,
  Fri Apr 16, Fri Apr 23 (computed by `scripts/build_competition_files.py` from the NYSE 2027 calendar).
- **Forecast:** quantiles q10, q25, q50, q75, q90 per row (non-decreasing, percent).
- **Row id:** `YYYY-MM-DD_hNN` (origin date, horizon), e.g. `2027-03-25_h05`.
- **Score (lower is better):** row loss = mean over the five quantiles of $\max(\tau u, (\tau-1)u)$, $u = y - q_\tau$,
  divided by $s_T\sqrt{h}$; $s_T$ = SD (ddof 1) of the 252 daily log returns in percent ending at the origin close.
  Average rows within an origin, then origins. Code: `scripts/sp500_scoring.py::score` (Kaggle signature,
  `ParticipantVisibleError` messages, self-test: `python scripts/sp500_scoring.py`).
- **Benchmark:** random walk, $q_\tau = z_\tau s_T\sqrt{h}$. **Skill** = 1 − team score / benchmark score.

## 4. Why this design — evidence (A1: every number below was computed)

**One live month is mostly luck.** `scripts/luck_analysis.py` (Yahoo data, 392 Thursday origins
2019-01-03 → 2026-10-01, the competition's exact metric; run 2026-11-24):

| Forecaster | Mean score |
|---|---|
| Random-walk benchmark | 0.2730 |
| EWMA volatility (λ = 0.94) | 0.2634 |
| Drift + EWMA | 0.2603 |
| Overconfident (benchmark at half width) | 0.2869 |
| Point only (all quantiles 0) | 0.3766 |

| Pair (first is better on average unless noted) | P(first wins) — one origin | — 26-origin block (n = 15) |
|---|---|---|
| EWMA vs benchmark | 0.638 | 0.733 |
| Benchmark vs overconfident | **0.492** | 0.667 |
| EWMA vs overconfident | 0.615 | 1.000 |
| Benchmark vs Drift + EWMA (drift better here) | 0.344 | 0.267 |
| Benchmark vs point only | 0.878 | 1.000 |

Reading: a **range** is essential (a point-only forecast loses 88% of single months), but between two
reasonable ranges a single month is close to a coin toss — the benchmark beats a band half as wide in
**49%** of single weeks although it is better on average. A 26-week block (the practice round's size)
separates them much better. nb18's first worked example shows the same thing on one origin
(2026-10-01: overconfident 0.1547 beats the benchmark 0.1724).

**Independent check (Codex, synthetic GARCH(1,1) with Student's t(5) innovations, 60,000 simulated
months; code in `_adm/codex_collab/2026-11-24_sp500-competition-design/run_log.txt`, re-run and
reproduced by Claude 2026-11-24):** with one month, the better of two close methods wins 53–54% of the
time under the interval score; MAE and RMSE **cannot distinguish** a volatility-aware forecast from a naive
one at all (exact ties); a severely overconfident range still wins 35% of months; pooling 12 independent
months raises the volatility-aware method's win rate against overconfidence to 98%. The 20 daily
cumulative returns of one month are so correlated that they are worth about **1.45** independent
observations — so the competition scores 5 horizons, not 20. A score expressed as a ratio to the random
walk on one month ranges from 0.54 to 1.98 (1st–99th percentile) for two near-identical methods — so the
ranking uses the scaled loss, and skill is only reported.

**Consequences:** quantiles + pinball loss (not a point metric); five horizons; scale by $s_T\sqrt h$; an
ungraded multi-origin practice round to teach the method; rank carries 5 of 100 points.

## 5. Kaggle platform facts (verified 2026-11-24)

| Fact | Source |
|---|---|
| A solution file has a `Usage` column with values Public, Private or Ignored | [Kaggle — Competitions Setup](https://www.kaggle.com/docs/competitions-setup), "Prepare the Dataset" |
| Custom Python metrics are available to community hosts (Host › Evaluation Metric): function of `solution`, `submission`, `row_id_column_name`, all arguments and the return type-annotated, `ParticipantVisibleError` for messages, 30-minute runtime limit, no internet | same page, "Set Up Scoring" / "Creating a New Metric" |
| **"You can upload a new solution file, but you must contact Kaggle Support to trigger a full rescore of an active competition"**; Kaggle "does not provide hands-on support for Community Competitions" | same page, FAQs |
| Via the CLI, re-uploading a solution "only works pre-launch; after launch the solution file is frozen"; rerun scoring "requires Kaggle admin access for now" | [Kaggle CLI — competition_creation.md](https://github.com/Kaggle/kaggle-cli/blob/main/docs/competition_creation.md) |
| A host can designate a submission as a "Benchmark"; set "Score Decimals to Display" | Competitions Setup, "Test Your Competition" / "Finalize & Launch" |
| Visibility: private competitions, invitation URL, optional restricted email list (notebooks disabled by default there) | Competitions Setup, "Visibility & Access" |

**Design consequence:** a live round whose answer key exists only after Apr 23 cannot be scored
self-service on Kaggle. **Kaggle hosts the practice round** (answer key known at launch); **the live round
is scored by the host** with `scripts/score_live_round.py` — the same `score` function — and the
standings are posted on Brightspace. Optional upside: Davi may ask in the Competition Hosting forum or
Kaggle Support whether they would rescore a live competition after a solution upload; the course does not
depend on it.

## 6. Data source and licensing (verified 2026-11-24)

| Source | What its terms say (short quotes) | Course use |
|---|---|---|
| **FRED `SP500`** ([series](https://fred.stlouisfed.org/series/SP500), [legal](https://fred.stlouisfed.org/legal/)) | Series notice: S&P Dow Jones Indices copyright; "Reproduction of S&P 500 in any form is prohibited except with the prior written permission"; tagged "Copyrighted: Pre-Approval Required" (non-commercial educational or personal use only). Legal page, prohibitions that apply to **"all use … including non-commercial, educational, and personal use"**: using FRED content "in connection with the development or training of any software program or system or machine learning". 10 years of daily history only. | **Not used** for modelling (nb16/nb18 do not touch FRED). |
| **Yahoo Finance via `yfinance`** ([terms](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html)) | Content may not be reproduced or distributed; automated collection is restricted without permission; Yahoo displays content it does not own. `yfinance` is an unofficial library, preinstalled in Colab. | **Default student pull** (each student downloads for their own coursework; nothing redistributed). Residual terms risk — see the decision below. |
| **Stooq** | Downloads sit behind a JavaScript bot check (tested 2026-11-24) | Not usable from Colab. |
| **S&P Dow Jones Indices** (owner) | Its terms page returned 404/403 to automated reading — **UNVERIFIED**. FRED lists `index_services@spdji.com` for permission requests. | Permission route. |

**What the course publishes:** forecasts, code and scores only. The builder writes the practice answer key
(derived log returns, hidden from participants) to the gitignored `_adm/kaggle_sp500_2027S/`; it is
uploaded **only** to the private Kaggle competition as the hidden solution.

`[[PENDING sp500-data-license: Davi decides (a) accept the residual risk — students pull Yahoo data for
their own coursework; the hidden Kaggle answer key holds derived returns only; or (b) email
index_services@spdji.com for written classroom permission (draft in kaggle_host_setup_guide.md §0); or (c) ask
Purdue Libraries' business librarian for a licensed daily S&P 500 source usable in class. Until decided,
the materials follow (a).]]`

## 7. Grading (of 100 competition points)

| Component | Points | Of course | Depends on the market? |
|---|---:|---:|---|
| Live forecast — valid, on time, reproduced by the notebook | 10 | 2.0% | No |
| Live forecast — rank | 5 | 1.0% | Yes |
| Walk-forward method notebook | 45 | 9.0% | No |
| Forecast memo | 20 | 4.0% | No |
| Peer evaluation (final, Apr 30) | 20 | 4.0% | No |

- **Rank points** = 5 × (N − rank) / (N − 1), ties share the average rank; invalid or late files are not ranked
  (0 rank points, and the 10 validity points are lost). Max luck spread: 1 point of the course grade.
  Codex's partial run argued for an even smaller rank share (rank effect capped at 0.4 course points); this
  design keeps 1.0 so the live month still matters. `[[PENDING sp500-rank-weight: Davi may lower the rank
  share to 2 points and move 3 to the method notebook.]]`
- **Rubrics:** the student instructions hold the full method (45) and memo (20) rubrics. Grading anchors:
  *Reproducible* — the host or TA re-runs the notebook with `DATA_END = "2027-03-25"` and compares the
  regenerated file with the submitted one (tolerance 0.001 per quantile; Yahoo history can shift by
  rounding). *Honest comparison* — full marks require the paired description and a champion rule stated
  before the backtest; a memo claiming an edge the backtest does not show loses the champion-statement
  points even if the live rank is good. *Expectation* — the memo's predicted score range is graded for being
  stated and derived from the backtest, not for being right.
- **Penalties (−10 each):** `NN_` filename convention; Kaggle team name not `Group NN` at the practice
  deadline. Non-reproducing notebook: the 15 live-forecast points are forfeited.
- **Peer evaluation:** midpoint (Sun Mar 7) formative, completion credit, flags trigger a team check-in; final
  (Fri Apr 30) carries the 20 points, collected with the Final Project peer evaluation.

## 8. Host procedures

**Before Mar 3 (practice round):** run the builder on or after **Mon Mar 1, 2027** and follow
`kaggle_host_setup_guide.md`:

```bash
python _course_case_competition/2027S/scripts/build_competition_files.py
```

Defaults: 26 Thursday origins ending at the latest Thursday whose 20-day outcome is known; the earliest 13
public, the latest 13 private; output in `_adm/kaggle_sp500_2027S/` (gitignored). Test run 2026-11-24:
origins 2026-04-30 → 2026-10-22, 130 rows, benchmark 0.2288 (public 0.2463, private 0.2112).

**Live round (Sat Apr 24 or Sun Apr 25):** download the Brightspace submissions into one folder, then

```bash
python _course_case_competition/2027S/scripts/score_live_round.py --submissions <folder>
```

It prints the truth for the five horizons, validates every file with the Kaggle rules, scores the valid
ones, ranks them, computes rank points and each team's skill against the random walk, and writes
`standings.csv` and `per_row_losses.csv` to `_adm/kaggle_sp500_2027S/live_results/`. Dry run 2026-11-24 on
a past origin with five fake files: ranking, tie handling, a misnamed file and a crossing-quantile file
(rejected with its reason) all behaved as intended. Post the standings (group, score, skill, rank) on
Brightspace; do not post index values.

**Integrity check (before grading the notebooks):** re-run each `NN_competition_code.ipynb` with
`DATA_END = "2027-03-25"`; confirm the last close used is 2027-03-25 and the regenerated file matches.

## 9. Risk register

| Risk | Mitigation |
|---|---|
| Yahoo/yfinance blocked or rate-limited in Colab | `load_sp500(csv_path=...)` with a self-downloaded CSV; groups keep their own CSV from an earlier successful pull (never shared). |
| Kaggle cannot score the live round | Designed out: host-scored live round (§5). |
| Kaggle deadline granularity (UTC) | Set the practice deadline to 2027-03-26 03:59 UTC (= Thu Mar 25, 11:59 PM EDT) if the form accepts a time; otherwise 23:59 UTC Mar 25 (7:59 PM EDT) and say so on Brightspace. `[[PENDING kaggle-deadline-time: confirm in the Kaggle host form]]` |
| Unscheduled NYSE closure in the window | Horizons follow trading days; standings move later by the same number of days. |
| Extreme market move | Scaling by $s_T\sqrt h$ is fixed before the window; a crash inflates every team's loss, which leaves ranks meaningful; the grade depends on rank for only 5 points. |
| Ties | Average rank. |
| Late live forecast | Not ranked (information advantage); notebook and memo follow the late policy. |
| Data revisions between Mar 26 and Apr 25 | The host scores with the data as downloaded on scoring day; reproduction tolerance 0.001. |
| Group data sharing or uploading index data | Instructions forbid it; graded as an integrity issue. |

## 10. Files in this folder

| File | Purpose |
|---|---|
| `course_case_competition_instructions.md` | Student-facing rules, dates, rubric (Brightspace text) |
| `course_case_competition_reference.md` | This file |
| `kaggle_host_setup_guide.md` | Step-by-step Kaggle setup for Davi |
| `scripts/sp500_scoring.py` | The metric (Kaggle custom-metric code), benchmark, helpers, self-test |
| `scripts/build_competition_files.py` | Practice answer key, sample submission, origins list, live template/calendar |
| `scripts/score_live_round.py` | Host scoring of the live round |
| `scripts/luck_analysis.py` | The §4 evidence |
| Teaching notebooks | `notebooks/nb16_time_series_forecasting_*.ipynb`, `notebooks/nb18_competition_workflow_*.ipynb` |

## 11. Change log

| Date | Change | Authored by |
|---|---|---|
| 2026-11-24 | Initial Spring 2027 S&P 500 design: quantile/pinball target and metric, practice round on Kaggle, host-scored live round, 10/5/45/20/20 grade, scripts, verified Kaggle/NYSE/licensing facts. Codex partner run (gpt-6.1-sol, max, read-only) stopped early on credits; its independent design (Kaggle practice + Brightspace-frozen live forecast + published scorer; q10–q90 wide format; small rank weight) and its GARCH simulation were verified and merged. | Davi Moreira (with Claude assistance) |
