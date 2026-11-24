# Course Case Competition — Forecasting the S&P 500 (Spring 2027)

## About the Course Case Competition

The Course Case Competition is a **team competition**. Your group — the same Brightspace group as your Final Project team — forecasts the **S&P 500** over the coming course weeks. You submit a **range**, not a single number: five quantiles of the index's return for the next trading day and for each of the next four weeks. A **practice round runs on Kaggle** on past weeks; the **live round** is the real market from **Monday, March 29 to Friday, April 23, 2027**. Check the course syllabus for the weight of the competition in your course grade (20%).

The workflow is taught in **nb16** (walk-forward validation, the random walk, volatility) and **nb18** (quantile forecasts, the scoring rule, the backtest, the submission file). Start from nb18: your competition notebook is nb18 adapted to your own model.

> **Why a range?** The direction of the stock market over the next month is close to a coin flip — nb16 showed that no model read it better than the random walk. The **size** of the coming moves is forecastable. A range that is honest (the truth lands below your 10% quantile about 10% of the time) and tight (no wider than needed) is a real skill, and it is what the competition scores.

---

## Key Dates (Eastern Time)

| Date | What |
|---|---|
| **Wed Mar 3** | Kickoff in class (nb18). The Kaggle practice round opens. |
| **Sun Mar 7, 11:59 PM** | **Kaggle team setup due**: every member joined, team name `Group NN`. Kaggle team merges close at this time. |
| Wed Mar 10, Fri Mar 12 | Virtual work sessions (competition + final project). |
| Mar 15–20 | Spring break (no class). |
| **Thu Mar 25, 11:59 PM** | Kaggle practice round closes. |
| **Thu Mar 25, 4:00 PM** | The **live origin**: the S&P 500 close of Thursday, March 25 is the last information your forecast may use. |
| **Fri Mar 26, 11:59 PM** | **Live forecast, code and memo due on Brightspace.** (The NYSE is closed for Good Friday.) |
| Mon Mar 29 – Fri Apr 23 | The live window: 20 trading days. |
| **Sun Apr 25** | Final standings posted on Brightspace. |
| Fri Apr 30 | Final peer evaluation (Final Project + Competition). |

---

## The Challenge

**Target.** For a forecast **origin** $T$ (the close of a trading day) and a **horizon** $h$ (trading days after it), the target is the cumulative log return of the S&P 500 in percent:

$$y(T, h) = 100 \cdot \ln\!\left(\frac{P_{T+h}}{P_T}\right),$$

where $P$ is the index's daily closing level. A value of 1.5 means the index ended about 1.5% above its origin close.

**Horizons.** $h \in \{1, 5, 10, 15, 20\}$ — the next trading day and one, two, three and four weeks ahead. For the live round the origin is the close of **Thursday, March 25, 2027**, and the five horizons fall on:

| id | Horizon | Target date (close) |
|---|---|---|
| `2027-03-25_h01` | 1 trading day | Mon Mar 29, 2027 |
| `2027-03-25_h05` | 5 trading days | Fri Apr 2, 2027 |
| `2027-03-25_h10` | 10 trading days | Fri Apr 9, 2027 |
| `2027-03-25_h15` | 15 trading days | Fri Apr 16, 2027 |
| `2027-03-25_h20` | 20 trading days | Fri Apr 23, 2027 |

(If the NYSE closes unexpectedly during the window, the $h$-th trading day moves later and the standings follow it.)

**What you forecast.** For each row, five quantiles of $y$: **`q10`, `q25`, `q50`, `q75`, `q90`**. They must be numbers in percent and non-decreasing (`q10 ≤ q25 ≤ q50 ≤ q75 ≤ q90`).

**Evaluation metric: scaled pinball loss (lower is better).** For each row, the pinball loss of each quantile is

$$L_\tau(y, q_\tau) = \max\big(\tau\,(y - q_\tau),\; (\tau - 1)\,(y - q_\tau)\big),$$

averaged over the five quantiles and divided by $s_T\sqrt{h}$, where $s_T$ is the standard deviation of the 252 daily log returns (in percent) that end at the origin close — known before you forecast. The score averages the five horizons, and (in the practice round) then averages the origins. The exact code is in nb18 and in the published scorer `_course_case_competition/2027S/scripts/sp500_scoring.py`; it is the same function on Kaggle and in the live round.

**The benchmark** is the random walk with one-year volatility: median zero and quantiles $z_\tau \, s_T \sqrt{h}$ (normal quantiles). It appears on the Kaggle leaderboard as *Random walk benchmark*. Your **skill** is $1 - \text{your score} / \text{benchmark score}$: positive means you beat the random walk.

---

## Data — Pull It Yourself, Never Upload It

There is **no dataset on Kaggle**. Each group downloads daily S&P 500 closes itself, in Colab, with the loader in nb18 (Yahoo Finance through `yfinance`, preinstalled in Colab). If Yahoo is unavailable, download the daily history yourself as a CSV with columns `Date` and `Close` and load it with `load_sp500(csv_path=...)`.

- The S&P 500 index values are the property of **S&P Dow Jones Indices**. Use them for your own coursework only. **Do not upload index data** to Kaggle, Brightspace, GitHub or anywhere else, and do not share data files between groups. Your submission files contain only your forecasts.
- Do **not** use FRED for this competition: FRED's terms prohibit using its content in the development or training of machine-learning systems, for every kind of use, including educational.
- You may use other free data (for example interest rates or a volatility index) if your group pulls it the same way, applies the same information cutoff, documents the source and its terms in the notebook, and never uploads it. The backtest must show it helps.

---

## What to Submit

### On Kaggle (practice round, ungraded leaderboard)

At least **one valid submission** to the practice round under your team name `Group NN`, by **Thu Mar 25, 11:59 PM**. The practice origins are past Thursdays, listed in `practice_origins.csv` on the competition's Data tab. You know these outcomes already — that is fine. The practice round exists to rehearse your pipeline, your file format and your team setup before the live forecast, which nobody can look up. Use it honestly: forecast each practice origin from the data up to that origin's close only, exactly as your backtest does.

### On Brightspace (one upload per team, by Fri Mar 26, 11:59 PM)

| # | File | Description |
|---|---|---|
| 1 | **`NN_live_forecast.csv`** *(e.g., group 03: `03_live_forecast.csv`)* | The live forecast: exactly six columns `id,q10,q25,q50,q75,q90` and the five rows `2027-03-25_h01` … `2027-03-25_h20`, numbers in percent. |
| 2 | **`NN_competition_code.ipynb`** | The notebook that produced the file: `DATA_END = "2027-03-25"`, the weekly walk-forward backtest, the paired comparison with the benchmark, the calibration check, and the cell that writes the live file. A fresh **Runtime → Run all** in Colab must regenerate the same file. |
| 3 | **`NN_forecast_memo.pdf`** | One to two pages for the treasury officer (see the rubric): your champion statement against the random walk, your calibration evidence, and the range of scores your backtest leads you to expect for the live month. |

A live forecast submitted after the deadline is not ranked (the market will have moved). The notebook and memo then follow the course's late-work policy.

### Penalties

| Issue | Deduction |
|---|---|
| A filename does not follow the `NN_…` convention (e.g., group 03: `03_live_forecast.csv`, `03_competition_code.ipynb`, `03_forecast_memo.pdf`) | **−10 points** |
| Your team's name on the Kaggle leaderboard is not `Group NN` (with the leading zero, e.g. `Group 03`) at the practice-round deadline | **−10 points** |
| The submitted notebook, re-run with `DATA_END = "2027-03-25"`, does not reproduce the submitted live forecast (beyond rounding) | **The live-forecast points (15) are forfeited** |

---

## How to Participate — Step by Step

### Step 1 — Join the practice round on Kaggle

1. **Create a Kaggle account** if you don't already have one. Use a name and email the instructor will recognize (your Purdue identity is preferred).
2. Open the **invitation link** posted on Brightspace and click **"Join"**; read and **accept the competition rules**.
3. The competition then appears in "My Competitions". Its **Data** tab holds `sample_submission.csv` (the random-walk benchmark in the submission format), `practice_origins.csv` and a README — no index data.

### Step 2 — Form your team on Kaggle (by Sun Mar 7)

Form your team **before any teammate submits** — it is much simpler that way. **Your team name on Kaggle must be `Group NN`** (e.g., `Group 03`) so the instructor and TA can map the leaderboard to Brightspace.

#### Option A — Designate one teammate to create the team (recommended)

1. Each teammate joins the competition individually (Step 1).
2. **One designated member** (the "team captain") opens the competition's **"Team"** tab.
3. In **"Team Name"**, enter **`Group NN`** with the leading zero. Click **Save**.
4. In **"Invite teammate"**, enter each teammate's **Kaggle username** and click **Invite**.
5. Each teammate accepts the invitation from the same **"Team"** tab.

#### Option B — Merge existing teams (only if some teammates already submitted)

1. One captain clicks **"Request Merge"** on the **"Team"** tab and enters the other team's name; the other captain accepts.
2. Set the merged team's name to **`Group NN`**.
3. **Merges share submissions:** the merged team's daily count is the sum of what both teams already used that day.

#### Rules and limits

- A team shares **5 practice submissions per day**, not 5 each.
- Kaggle **closes team merges on Sun Mar 7 at 11:59 PM** — after that, nobody can join or merge.
- The team name must read **`Group NN`** at the practice-round deadline.

### Step 3 — Build and backtest your forecast (nb18)

- Start from nb18. Keep the information cutoff as one variable, `DATA_END`, and keep every forecaster a function of **the returns up to the origin close only**.
- **Backtest weekly on at least 52 Thursday origins** (one year; nb18 uses 104), with the five competition horizons, the competition's `score` function, and **identical origins for every model**.
- Compare **the benchmark and at least two challengers** — at least one that changes the **width** (for example an EWMA or GARCH-style volatility) and at least one that changes the **center or shape** (drift, an AR model, a lag-feature ML model, empirical or fat-tailed quantiles).
- **Describe the paired per-origin gains** over the benchmark: mean, SD, origins won, best and worst week, and a running-total plot. With overlapping weekly windows the course describes these differences rather than certifying them; the Diebold–Mariano test is an optional "going further".
- **Check calibration**: the share of backtest outcomes inside your q25–q75 band (target 0.50) and your q10–q90 band (target 0.80), at every horizon.
- **Choose your champion by the rule you wrote down before running the backtest**, and keep the simpler model when the evidence does not make the case.

### Step 4 — Practice on Kaggle

Forecast every practice origin with the same function you backtested, write one row per `id` in `practice_origins.csv`, validate the file (nb18's `validate_submission`), and upload it on Kaggle (**Submit Predictions**). Add a short description (model + settings). The practice leaderboard shows your scaled pinball loss on the public origins; the private origins are revealed when the round closes.

### Step 5 — The live forecast (Thu Mar 25 – Fri Mar 26)

1. After the market closes on **Thursday, March 25**, set `DATA_END = "2027-03-25"` and run your notebook from a fresh runtime (**Runtime → Run all**).
2. Check that the last close in your data is **Thursday, March 25, 2027**.
3. Write `NN_live_forecast.csv`, validate it, and confirm that a second run produces the same file.
4. Write the memo. Upload the three files to Brightspace by **Friday, March 26, 11:59 PM ET**.

---

## Grading — How Your Competition Grade Is Computed

One live month is mostly luck: on real S&P 500 data, a calibrated forecast beat a forecast with half the width in only about half of single weeks, even though it is clearly better over many weeks. So the grade rewards what you control — a reproducible walk-forward method and an honest comparison with the random walk — far more than your rank.

> **Competition grade = Live forecast (15) + Walk-forward method notebook (45) + Forecast memo (20) + Peer evaluation (20) − penalties**

### Live forecast — 15 points

- **10 points** for a live forecast that is **valid, on time, and reproduced** by your submitted notebook.
- **5 points** for your rank in the live round: the top team earns 5, the last earns 0, in equal steps (`5 × (N − rank) / (N − 1)` with `N` ranked teams; tied scores share the average rank). An invalid or late file is not ranked.

The live standings also report each team's skill against the random-walk benchmark.

### Walk-forward method notebook — 45 points

| Criterion | Points | What earns full marks |
|---|---:|---|
| **Reproducible notebook** | 8 | A fresh **Run all** in Colab, with `DATA_END = "2027-03-25"`, pulls the data and regenerates the submitted live file exactly. |
| **Information discipline** | 6 | One cutoff variable; every forecaster receives only returns up to its origin close; an assertion checks that no data after the cutoff are loaded. |
| **Walk-forward backtest** | 9 | At least 52 weekly Thursday origins, the five horizons, the competition's `score`, identical origins for every model. |
| **Benchmark and challengers, compared honestly** | 8 | The benchmark plus at least two challengers (one width, one center or shape); paired per-origin gains described (mean, SD, origins won, extremes, running total); champion chosen by a rule written before the backtest. |
| **Calibration check** | 6 | Coverage of the 50% and 80% bands at every horizon, read against the targets. |
| **Kaggle practice submission** | 4 | At least one valid practice submission under `Group NN` by Thu Mar 25. |
| **Code quality and AI note** | 4 | Readable, commented code; a short AI-use acknowledgment at the end (tool + how it was used). |

### Forecast memo — 20 points (one to two pages, for the treasury officer)

| Criterion | Points | What earns full marks |
|---|---:|---|
| **Champion statement** | 6 | The model you submit, compared with the random walk on the same origins, in the course's four-part form (champion, evidence, checks, what would change your mind) — honest wording, no claimed edge your backtest does not show. |
| **Expectation for the live month, written in advance** | 5 | From your backtest: the range of per-origin scores you expect (e.g., the middle 80% of your weekly scores) and how often you expect to beat the benchmark in a single month. |
| **Calibration evidence** | 4 | Your coverage table summarized in plain language. |
| **Risks** | 3 | What could make the month unusual (a volatility shock, a scheduled event) and how your range treats it. |
| **Clarity** | 2 | A treasury officer with no data-science training can act on it. |

### Peer evaluation — 20 points

Each member confidentially evaluates their teammates' contributions in the **final peer evaluation (Fri Apr 30)**, which covers the Final Project and the Competition; this is the one individual part of the grade. A **midpoint peer evaluation (Sun Mar 7)** is formative — completion credit, and any concern it raises leads to a team check-in. Full details are in each assignment's instructions on Brightspace.

### The bottom line

Everything except 5 points is decided by your method, your memo and your teamwork — before the market moves at all. A clean, reproducible backtest, an honest comparison with the random walk and a calibrated range are what earn the grade; the market's month decides at most 5 points of 100.

---

## Tips and Common Pitfalls

- **Name the team first.** Set `Group NN` before anyone submits on Kaggle.
- **Never peek.** The most common bug in forecasting is look-ahead: a rolling statistic computed on the whole series, or a feature that includes the origin's future. Pass forecasters only `returns[:origin]`.
- **Scale matters more than the center.** Most of the score is about the width of your range. Get the volatility right before you try to predict direction.
- **Don't trust one lucky week.** nb18 shows an overconfident forecast winning a calm month. Judge models on the whole backtest.
- **Validate before you upload.** Six columns, five rows (live) or one row per practice `id`, numbers only, quantiles in order. Kaggle rejects invalid files; the live scorer ranks them last.
- **Keep an experiment log.** Model, settings, backtest score, coverage, practice score.
- **Cite any AI tool you used** in the notebook (course AI policy).

---

*Good luck — may your ranges be honest and tight.*

— *Prof. Moreira*

**End of Course Case Competition instructions.**
