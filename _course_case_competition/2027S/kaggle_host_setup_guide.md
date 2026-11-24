# Kaggle Host Setup Guide — Spring 2027 S&P 500 Competition (practice round)

For Davi. Nothing in this guide has been done on Kaggle; every step is yours, signed in to your own Kaggle
account. Kaggle facts below are from [Kaggle's Competitions Setup page](https://www.kaggle.com/docs/competitions-setup)
(read 2026-11-24); button labels may differ slightly in the live interface. Why only the **practice** round is on
Kaggle: Kaggle freezes a community competition's answer key at launch and rescoring needs Kaggle Support
(reference §5), so the live round is scored with `scripts/score_live_round.py`.

**Timeline:** build the files on or after **Mon Mar 1, 2027** (step 1); have the competition launched before
class on **Wed Mar 3** (steps 2–8).

---

## 0. Before you start — one decision

The hidden answer key holds derived S&P 500 returns (never index levels). Decide the data-licensing question
in reference §6 (`[[PENDING sp500-data-license]]`). If you choose to ask S&P Dow Jones Indices for permission,
a draft (edit freely; send from your Purdue account):

> Subject: Permission request — classroom use of S&P 500 daily closes (Purdue QM 47400)
>
> Dear S&P DJI Index Services team,
> I teach Predictive Analytics (QM 47400) at Purdue University's Daniels School of Business. In Spring 2027 my
> students will forecast the S&P 500 in a non-commercial, ungraded-practice plus graded-live class competition.
> Each student downloads daily closing levels for personal coursework; the course does not redistribute
> index values. The only stored derivative is a hidden answer key of cumulative log returns for about 26 past
> weeks, held privately on Kaggle to score practice forecasts. May we use the index in this way, and is there
> an attribution you would like us to display?
> Thank you, Davi Moreira

## 1. Build the files (Mon Mar 1 or later)

From the repo root (needs `yfinance`; on this Mac use `~/.venvs/sp500comp/bin/python`, with
`export SSL_CERT_FILE=$(~/.venvs/sp500comp/bin/python -m certifi)` if Python reports a certificate error):

```bash
python _course_case_competition/2027S/scripts/sp500_scoring.py
python _course_case_competition/2027S/scripts/build_competition_files.py
```

The first command must print `self-test: all checks passed`. The second writes to `_adm/kaggle_sp500_2027S/`
(gitignored) and prints `build_report.txt`: the 26 practice origins (Thursdays), the public/private split, and
the **random-walk benchmark score** — write that number down for step 7. Files:

| File | Goes to |
|---|---|
| `practice/solution.csv` | Kaggle **Host › Evaluation / Solution** (hidden answer key) |
| `practice/sample_submission.csv` | Kaggle **sample submission** (it is the random-walk benchmark) and the Data tab |
| `practice/practice_origins.csv` | Kaggle **Data** tab (origins, horizons, target dates — no index values) |
| `live/live_template.csv`, `live/live_calendar.csv` | Brightspace (the live file teams must fill) |

## 2. Create the custom metric notebook

1. On Kaggle, open the metric template, **[metric_template](https://www.kaggle.com/code/metric/metric-template)**, and make your own copy (**Copy & Edit**), or create a new notebook of the *metric* type if Kaggle offers it from **Host › Evaluation Metric**.
2. Replace the code with the full contents of `_course_case_competition/2027S/scripts/sp500_scoring.py`. Kaggle requires a function that takes `solution`, `submission` and `row_id_column_name`, with every argument and the return type annotated — `score(solution: pd.DataFrame, submission: pd.DataFrame, row_id_column_name: str) -> float` already is; error messages use `ParticipantVisibleError` so teams see what is wrong with their file.
3. Title: `QM474 S&P 500 scaled pinball loss`. **Save Version** and wait until Kaggle marks it valid. (Limits: Python only, no internet, 30 minutes per scoring.)

## 3. Create the competition

1. Kaggle → **Competitions** → **Host a competition** (Kaggle Community) → **Create new competition** → **Machine Learning Competition**.
2. **Title:** `Spring 2027 QM47400 Case Competition — S&P 500 Forecast (Practice Round)`
   **Subtitle:** `Forecast the range of the S&P 500 at 1 day to 4 weeks — practice on past weeks`
   **URL:** `spring-2027-qm-47400-sp500-practice`
3. **Visibility:** *Private*. **Who can join:** *Only people with a link* (or *Restricted email list* with `purdue.edu`; Kaggle disables notebooks by default in that mode, which is fine — teams work in Colab).
4. Prizes: none.

## 4. Scoring and data

1. **Host › Evaluation Metric:** choose your custom metric from step 2.
2. Upload **`solution.csv`** (columns `id, y, h, scale, origin, target_date, Usage`; `Usage` = Public for the earliest 13 origins, Private for the latest 13) and **`sample_submission.csv`** (`id, q10, q25, q50, q75, q90`). The id column is first in both.
3. **Data tab:** upload `sample_submission.csv` and `practice_origins.csv`, plus a `README.md` with this text:

   > There is no S&P 500 data in this competition. Download daily closes yourself in Colab with nb18's
   > `load_sp500()` (Yahoo Finance via yfinance) and never upload index data anywhere. For every row of
   > `practice_origins.csv`, forecast five quantiles (q10, q25, q50, q75, q90) of
   > y = 100·ln(close on target_date / close on origin) using only data up to the origin close.
   > `sample_submission.csv` is the random-walk benchmark in the exact submission format.

4. **License for the data files:** the files contain no third-party data; choose the most restrictive option offered or "Other (specified in description)" with "Course use only".

## 5. Settings

| Setting | Value |
|---|---|
| Start | Wed Mar 3, 2027 (or launch immediately once tested) |
| **Team merger deadline** | **Sun Mar 7, 2027, 11:59 PM EST = 2027-03-08 04:59 UTC** |
| Entry deadline | same as the team merger deadline |
| **Final submission deadline** | **Thu Mar 25, 2027, 11:59 PM EDT = 2027-03-26 03:59 UTC** (daylight time starts Mar 14). If the form only allows 23:59 UTC, use 2027-03-25 23:59 UTC (7:59 PM EDT) and state that time on Brightspace. |
| Max team size | 4 |
| Max daily submissions | 5 per team |
| Final submissions to select | 2 (Kaggle default) |
| Score decimals to display | 4 |
| Rules acceptance required | Yes |

## 6. Text for the competition pages (paste)

**Overview — Description**

> Forecast the range of the S&P 500. For each past Thursday close in `practice_origins.csv`, submit five quantiles
> (q10, q25, q50, q75, q90) of the index's cumulative log return in percent, y = 100·ln(P[T+h]/P[T]), at
> h = 1, 5, 10, 15 and 20 trading days. This is the **ungraded practice round** of the QM47400 Course Case
> Competition: it rehearses your walk-forward pipeline and the file format. The graded live forecast (origin: close of
> Thu Mar 25, 2027) is submitted on Brightspace. Teams are your final-project groups, named `Group NN`.

**Overview — Evaluation**

> Submissions are scored with the scaled pinball loss (lower is better): for each row, the pinball loss
> max(τ(y − q), (τ − 1)(y − q)) is averaged over τ = 0.10, 0.25, 0.50, 0.75, 0.90 and divided by s·√h, where s is
> the standard deviation of the 252 daily log returns (percent) ending at the origin close. Rows are averaged
> within each origin, then origins are averaged. The public leaderboard uses the earliest 13 origins; the private
> leaderboard, revealed at the close, the latest 13. Submission file: `id,q10,q25,q50,q75,q90`, one row per id,
> quantiles non-decreasing. The *Random walk benchmark* (median 0, normal quantiles with one-year volatility) is
> shown on the leaderboard.

**Rules (key points; add to Kaggle's standard rules)**

> Only enrolled QM47400 Spring 2027 students may participate, in their assigned group, team name `Group NN`.
> Do not upload or share S&P 500 data. Each forecast must use only information available at its origin close —
> the practice round is ungraded and exists to rehearse that discipline. 5 submissions per team per day. Team
> merges close Sun Mar 7, 11:59 PM ET.

## 7. Test before launching

1. **Sandbox submit** `sample_submission.csv`: the score must equal the benchmark number in `build_report.txt` (to 4 decimals). Then designate that submission as the **Benchmark**, named *Random walk benchmark*.
2. **Perfect submission** — must score 0:

   ```bash
   cd _adm/kaggle_sp500_2027S/practice && python -c "import pandas as pd; s=pd.read_csv('solution.csv'); p=s[['id']].copy(); [p.__setitem__(c, s['y']) for c in ['q10','q25','q50','q75','q90']]; p.to_csv('perfect_submission.csv', index=False)"
   ```

3. **A broken file** (swap q10 and q90 in one row of the sample): Kaggle must reject it with the message *Quantiles must be non-decreasing*.
4. Launch checklist all green → **Launch** (or schedule for Wed Mar 3, 8:00 AM ET).

## 8. Invite and announce

Copy the invitation URL from the launch checklist into the Brightspace competition module, with
`course_case_competition_instructions.md` and `live/live_template.csv`. Remind teams to set `Group NN` before
anyone submits.

## 9. After the practice round closes (Thu Mar 25)

- Download the private leaderboard and check that every team reads `Group NN` (penalty otherwise) and has at
  least one valid submission (method-rubric criterion, 4 points).
- On **Sat Apr 24 or Sun Apr 25**, score the live round from the Brightspace downloads:

  ```bash
  python _course_case_competition/2027S/scripts/score_live_round.py --submissions <folder with NN_live_forecast.csv files>
  ```

  and post `standings.csv` (group, score, skill vs the random walk, rank) on Brightspace by **Sun Apr 25**.
