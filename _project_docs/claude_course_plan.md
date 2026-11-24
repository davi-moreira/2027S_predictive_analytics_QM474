# Implementation Plan: 2026 Fall Predictive Analytics (QM47400)

## What this document is

The **notebook-content justification** for the Fall 2026 offering: why each notebook sits
where it does, what it assumes, and what it sets up. `CLAUDE.md` names this file as the
place to update whenever a notebook's content, dependencies, or position changes.

What it is **not**: it is not the calendar (that is
[`MGMT47400_FullSemester_Plan_2026Fall.md`](MGMT47400_FullSemester_Plan_2026Fall.md)), not the
build workflow (that is [`../CLAUDE.md`](../CLAUDE.md)), and not the decision record (that is
[`DECISIONS.md`](DECISIONS.md)). Where those files are authoritative, this one defers.

> **History.** Through 2026-08-14 this file was the *2026 Summer migration runbook* — a
> phase-by-phase plan for building the 4-week intensive (create nb18–nb20, configure Quarto,
> initialize git, connect the remote, configure Pages). All of that work is long finished and
> the Fall repository is live, so those phases were removed. The notebook-sequence
> justification below is the section that carried forward.

---

## The Fall 2026 offering in one page

**QM47400 — Predictive Analytics**, Purdue Daniels School of Business, **Aug 24 – Dec 11, 2026**,
in person **Monday / Wednesday / Friday**.

| | |
|---|---|
| **Arc** | **20 notebooks** — nb00–nb09 and nb11–nb20. nb10 (Midterm Casebook) stays retired — the Fall 2026 midterm is an in-class paper exam built directly from the 2026Summer case bank. |
| **Session structure** | Monday and Wednesday carry notebook content. **Every Friday is a poster and/or Course Case Competition studio** — the single exception is **Fri Aug 28**, which carries nb02. |
| **Assessment** | Attendance 1% · Participation 4% · Quizzes 15% · Midterm Exam 20% (in class, Fri Sep 25) · Course Case Competition (Kaggle) 20% · Final Project 35% · Poster-to-Product 5%. **No final exam.** |
| **Last lecture** | **Mon Oct 26** (nb17). The remaining two notebooks, nb15 and nb20, are delivered inside the Friday poster studios on **Oct 30** and **Nov 6**. |
| **Two fixed dates** | Final poster (M10) due **Sun Nov 8**; Undergraduate Research Conference presentation **Tue Nov 17**, required of every student. |
| **After the conference** | Poster-to-Product build sprint **Fri Nov 20 – Wed Dec 9**; Kaggle closes **Sun Nov 29**; course wrap **Fri Dec 11**. |

Pedagogy is unchanged from prior offerings: **Concept → Demo → PAUSE-AND-DO Practice → Solution → Repeat**,
with micro-videos (≤12 min) and Google Colab notebooks as the hands-on spine.

---

## Notebook Sequence and Content Justification

Each notebook builds exactly one conceptual layer, assumes only what prior notebooks have taught, and prepares exactly what the next notebook needs. The table below summarizes the rationale; full speaking prompts and cell-level detail are in each `video_guides/NN_video_lecture_guide.md` (Sections 1–3).

> **Spring 2027 rollout (2026-11-24).** The rows below describe the notebooks as rebuilt for Spring 2027 (instructor copy first, executed headless with seed 474). nb01–nb07 keep the 60/20/20 split; nb08's validation split only motivates cross-validation, and from nb09 on each dataset is split once 80/20 and every model is scored on the same five folds of `X_train`. Every model comparison is `compare_paired`: paired per-fold gains, an interval corrected for fold overlap, read against a margin band declared before scoring (0.005 / **0.01** / 0.02 — the base margin decides) as one of four outcomes; there is no per-model 95% interval. A search's best cell is a nominee that faces the family default, and champions are chosen by a simplest-first ladder (MedScreen `LogisticRegression(C=1)`, robust; HomeValue the default random forest, with the tuned GBM unresolved and the call margin-sensitive at δ = 0.005). nb16 and nb18 are the temporal exceptions (walk-forward origins, per-origin differences described). nb10, nb15 and nb20 are retired; their rows stay as the Fall 2026 record. The Spring calendar is in [`QM47400_FullSemester_Plan_2027Spring.md`](QM47400_FullSemester_Plan_2027Spring.md).

### Sequencing Map

| NB | Title | Key Libraries/Tools | Depends On | Prepares For | Why This Position |
|----|-------|---------------------|------------|--------------|-------------------|
| 00 | Launchpad: Course Setup | Google Colab, Google Gemini | — (first) | 01 (platform ready), all subsequent | Pre-course: Colab navigation, Gemini Ask→Verify→Document, course structure, environment verification. The course map states that every case ends with one champion and a written reason, chosen by criteria stated before scoring; previews the **group S&P 500 forecasting competition on Kaggle**, played by the final-project team; and draws the arc in Spring teaching order nb16 → nb18 → nb19 → nb17 |
| 01 | EDA & Splits | pandas, numpy, matplotlib, seaborn, train_test_split | 00 (platform ready) | 02 (pipeline), all subsequent | Foundation: statistical learning framework, EDA workflow, 60/20/20 split (the split nb01–nb07 use; nb08 moves the course to one 80/20 split), leakage vocabulary. The workflow preview names the incumbent, a criteria block, fold scores with mean and spread, and a simplest-first ladder that ends in one champion with a stated reason; the leakage demo compares train-only vs train+validation scaler statistics and never scores `y_test` |
| 02 | Preprocessing Pipelines | Pipeline, ColumnTransformer, SimpleImputer, OneHotEncoder, StandardScaler | 01 (split, leakage) | 03 (metrics assume pipeline solved) | Operationalizes leakage prevention with the tool that makes safe preprocessing automatic; Exercise 2 is a single-split, provisional comparison read against a gap declared in advance |
| 03 | Regression Metrics & Baselines | mean_absolute_error, mean_squared_error, r2_score, DummyRegressor | 02 (pipeline) | 04 (needs metrics to measure feature engineering impact) | Teaches how to measure model quality before attempting to improve it; the Evaluation Documentation Template records the **Incumbent Model**, the **Decision Margins** (0.005 / 0.01 / 0.02 R², taught fully in nb08) and **Status: provisional** — the linear model is the incumbent, not yet a champion |
| 04 | Linear Features & Diagnostics | LinearRegression, PolynomialFeatures, make_pipeline | 03 (evaluation framework) | 05 (creates overfitting problem Ridge/Lasso solves) | Feature engineering + residual analysis; exposes polynomial overfitting; the best single-split model is a "validation leader" — one split cannot crown a winner |
| 05 | Regularization (Ridge/Lasso) | Ridge, Lasso, RidgeCV, LassoCV, ElasticNet | 04 (overfitting problem) | 06 (complete regression toolkit before classification pivot) | Direct solution to nb04's overfitting — a tuning maximum is a nominee, not a champion; closes Week 1 regression arc + project proposal; its Course Case Competition section introduces the group S&P 500 competition that kicks off with nb18 |
| 06 | Logistic Regression & Pipelines | LogisticRegression, accuracy_score, log_loss | 05 (regularization via alpha → C) | 07 (needs probability foundations) | Regression → classification pivot; reuses Pipeline pattern in new context; MedScreen's chief medical officer is the named stakeholder; the threshold sweep counts missed malignant cases against unnecessary reviews; the wrap-up names `LogisticRegression(C=1)` the screening incumbent |
| 07 | Classification Metrics | confusion_matrix, precision/recall/f1, roc_curve, precision_recall_curve, brier_score_loss, calibration_curve | 06 (probabilities, confusion matrix) | 08 (needs metric vocabulary for CV scoring) | Complete classification evaluation toolkit; cost-based threshold selection; **Section 6 — probability quality: Brier score + reliability curve** (a good ROC-AUC does not mean good probabilities). The wrap-up declares MedScreen's decision rules before nb08: ROC-AUC primary, margins 0.005 / 0.01 / 0.02, a malignant-recall safety guardrail and a Brier probability-quality guardrail — guardrails can block a promotion, never create one |
| 08 | Cross-Validation | cross_val_score, KFold, StratifiedKFold, cross_validate, `compare_paired` | 07 (metrics for scoring param) | 09 (CV embedded inside grid search; the 80/20 + five-fold pattern every later notebook uses) | Reliable model comparison replacing the fragile single split — the 60/20/20 validation split here only motivates CV; fold scores, mean and SD describe each model. Adds §4 *Comparing two models — paired gains and the four outcomes* (`compare_paired`, the margin band, the champion statement) and §5 *one 80/20 split and five folds*; no per-model interval |
| 09 | Tuning + Feature Eng. + Leakage Detection | GridSearchCV, RandomizedSearchCV, ColumnTransformer, FunctionTransformer, OneHotEncoder, SelectKBest, `compare_paired` | 08 (standalone CV, `compare_paired`) | 11 (full toolkit before the tree-based arc), 13 (leakage callout bridges here) | Three-section single file with opening toolkit-closer banner (cell 1, before LO): (A) grid search as nb08 × a grid — a search's best cell is a nominee that faces the default with `compare_paired`; one 80/20 split (both nominees are practically equivalent, so OLS and `C = 1` stay) + `C`-parameter primer; (B) TechCorp synthetic business case with real categoricals + target-encoding leak (the leak would read as a worthwhile gain — the teaching point) + SelectKBest leak detection; (C) Toolkit Recap — one-page reference consolidating concepts, workflow, sklearn primitives, decision rules across nb01–nb09 |
| 11 | Decision Trees (paired clf + reg) | DecisionTreeClassifier on breast cancer + DecisionTreeRegressor on California Housing, plot_tree, paired depth sweep with the plot_train_cv_curve helper, predicted-vs-actual scatter | 09 (evaluation skills consolidated) | 12 (high-variance problem motivates forests; dual-spine pattern continues) | First non-linear model on both cases; paired depth sweep with `plot_train_cv_curve`; readability caps (depth ≤ 3 / ≤ 5) declared up front; one-SE heuristic (SD/√5) nominates, `compare_paired` decides. **§7:** tree vs LogReg unresolved, tree vs OLS unresolved → both nb09 references stay. |
| 12 | Random Forests + Importance (paired clf + reg) | RandomForestClassifier on breast cancer + RandomForestRegressor on California Housing; **joint 3D `(n_estimators × max_features × max_depth)` 27-cell tuning grid** with fold scores kept per cell — the largest-mean cell is a nominee, labelled optimistic, that faces the default forest with `compare_paired`; OOB scoring on both; permutation_importance and drop-column inside the 5-fold loop on held-out rows; four-method importance table; fold-SD error bars; champion ladder with the nb09 references as incumbents | 11 (tree instability on both cases) | 13 (bagging baseline for boosting contrast), 14 (the default forest carried to the roster) | Bagging on both cases; same-depth forest wins every MedScreen fold yet unresolved (fold wins describe); 27-cell grid nominee vs default forest → default forest carried on both cases; OOB; four-method importance with permutation/drop-column on held-out folds; §9 ladder: forest promoted over OLS (+0.199 [+0.180, +0.218]); LogReg stays (forest unresolved). |
| 13 | Gradient Boosting (paired clf + reg) | GradientBoostingClassifier on breast cancer + GradientBoostingRegressor on California Housing, **joint 4D tuning grid** `n_estimators × learning_rate × max_features × max_depth` (54 classification cells; 27 depth-3 regression cells) whose largest-mean cell is a nominee facing the default GBM with `compare_paired`; learning-rate sweep; champion ladder | 12 (bagging baseline on both cases) | 14 (carried roster: default GBM for MedScreen, tuned `n_estimators=200, learning_rate=0.2` GBM for HomeValue) | Boosting on both cases; default GBM unresolved vs both champions; learning-rate × n_estimators coupling; grid nominee vs default GBM → default (clf), tuned n=200/lr=0.2 (reg); §7 four-step ladder: LogReg (robust), forest stays over tuned GBM (+0.018 [+0.009, +0.027] unresolved; margin-sensitive, cutoff 0.0091); leakage callout. |
| 14 | Model Selection Protocol + Two Ceremonies + Post-Deployment Monitoring (paired clf + reg) | `compare_paired`, `champion_ladder`, per-fold multi-metric evaluation using nb03/nb06/nb07 metric functions (no `neg_*` scoring strings), fold-strip and ladder plots, `describe_test` (deployment bar + INSIDE/ABOVE/BELOW description), money plot, `scipy.stats.ks_2samp` for the §7.4 drift-detection demo | 13 (full candidate pool on both cases), 08 (`compare_paired`, margin band) | 16 (ceremony pattern for the locked year), 17 (champion statement and paired-gain chart on the poster), 19 (the champions the MLP challenges) | Formal, fair, reproducible comparison on **both** cases: criteria block → fold scores → `champion_ladder` → frozen champion → one ceremony per case refit on `X_train`; champions `LogisticRegression(C=1)` (robust) and the default random forest (margin-sensitive vs the tuned GBM). The roster is declared before scoring, each candidate in the configuration its source notebook carried forward — **6 classification candidates** (Dummy, LogReg(C=1.0), LogReg L1(C=0.1), Tree(d=3), default forest, default GBM) and **7 regression candidates** (Dummy, OLS, Ridge, Lasso, Tree(d=5), default forest, GBM(lr=0.2, n=200)). MedScreen: every challenger unresolved. HomeValue: the forest is promoted over OLS (+0.1992 [+0.1800, +0.2183]); the tuned GBM's +0.0181 [+0.0091, +0.0271] over the forest is unresolved, so the forest stays (the GBM would win at δ = 0.005). In each ceremony the **deployment bar decides** (MedScreen ROC-AUC ≥ 0.95, HomeValue R² ≥ 0.75; a miss means "no model approved under this protocol", never a runner-up fallback) and **INSIDE/ABOVE/BELOW** (test score vs CV mean ± δ) only describes: test ROC-AUC 0.9993 and test R² 0.8005 (RMSE ≈ \$51,800), both cleared, both INSIDE; §6.3 playbook per description; **§7 post-deployment monitoring** — Re-evaluate → Re-train → Rebuild ladder, case-specific monitoring checklists, coded KS drift demo, one-page Monitoring Card; `audit_cv_first.py` authorizes only the two ceremony cells (30 + 34) |
| 15 | Final Project Milestone 03 Walkthrough — Complex Model + Hyperparameter Tuning + Draft Abstract | **Markdown-only walkthrough** (no code, no PAUSE-AND-DO) — companion read for the `milestone_03_complex_model_and_abstract.md` rubric | 14 (champion committed), 09 (hyperparameter tuning), 08 (CI-overlap rule) | 16 (time-series CV splitter pivot) | Same shape as nb05 §6/§7. Sections map directly to the M3 rubric: §0 Prediction Goals, §1a Baseline Replication (M2) with 95% CI, §1b Complex Model + Tuning + CI-overlap rule + final-training step on the full training fold (with random_state locked so M4 reproduces the same fitted Pipeline), §1c Required Visualizations, §2 Draft Abstract (~250 words), Course Case Competition (Kaggle Bank Churn) alignment, and Tips and Common Pitfalls. **No Interpretation, Calibration, or Decision-Quality content.** |
| 16 | Time-Series Forecasting: Walk-Forward Validation, Baselines, and the Random Walk | statsmodels (`ExponentialSmoothing`, `ARIMA`, `plot_acf`), scikit-learn `Ridge` on lag features, scipy, yfinance — all preinstalled in Colab (sktime retired) | 08 (paired comparison), 14 (ceremony) | 18 (Part B is the preparation for the Course Case Competition) | The course's exception to the random 80/20 split (D12), which nb18 inherits: a temporal train/test split (last 12 months locked) plus walk-forward validation (five origins one year apart = five folds, D11). Part A (workforce planner, US retail employment): Seasonal-Naive incumbent vs Naive, Drift, ETS, SARIMA and a lag-feature Ridge; paired per-origin differences described (D6, Diebold–Mariano Q&A); bands judged calibration first; the locked year opened once for the declared incumbent. Part B (state pension fund treasury officer, S&P 500): log returns, ACF of returns vs absolute returns, a 104-origin weekly walk-forward race against the random walk, and the random-walk volatility band — the preparation for the Course Case Competition. **Spring 2027:** Mon Mar 1. |
| 17 | Data Communication & Poster Design (formerly nb19) | — (markdown/narrative, no new libraries) | 14 (champion statement, paired gains, locked-test verdict), 16 (forecast comparison) | M10 final poster and the conference presentation | Six principles applied to the eleven-section URC poster architecture; chart audit + outline + 120–150-word abstract drafted in studio; §14 adds the paired-gain chart and the champion statement for the poster (fold scores, mean and SD per model; the only interval is the one around the gain). **Spring 2027:** the last lecture, Mon Mar 22, after nb16 → nb18 → nb19 — every headline number the poster reports already exists by then, and the poster (M10, Sun Apr 4) and the conference (Tue Apr 13) follow. (Fall 2026: week 10, Mon Oct 26.) |
| 18 | Course Case Competition Workflow: Forecasting the S&P 500 | yfinance, pandas, numpy, scipy (Student's t quantiles), the competition's scaled pinball loss | 16 (Part B) | the Course Case Competition (Kaggle practice round; live forecast), 19 (Exercise 1 rates the competition against the deep-learning rubric) | Replaces the bank-churn workflow. Information cutoff (`DATA_END`), quantile forecasts at 1/5/10/15/20 trading days, the competition's scaled pinball loss and random-walk benchmark, a 104-Thursday walk-forward backtest with described paired gains, calibration of 50%/80% bands, and a validated, reproducible submission file. No quiz. Temporal (information cutoff + walk-forward origins): no random split and no `X_test`. **Spring 2027:** Wed Mar 3, the competition kickoff. |
| 19 | Deep Learning | PyTorch (`torch`/`torchvision`) for the §4 FashionMNIST lab; `sklearn.neural_network.MLPClassifier`/`MLPRegressor` with `compare_paired` for the §5 contest against nb14's champions; **Hugging Face `transformers`** for the §6 LLM lab (sentiment + zero-shot pipelines); `requests` for the optional Purdue GenAI Studio API call; figures from `notebooks/figures/` | 14 (the champions and their 80/20 split), 08 (`compare_paired`), 18 (the competition Exercise 1 rates) | — (closes the modeling arc; nb17 follows in teaching order) | Awareness + hands-on module: historical arc, frameworks, MLP / CNN / RNN / Transformer structural inventions, **end-to-end PyTorch training on FashionMNIST**, four-question rubric for "is DL right for this problem?" (Exercise 1 applies it to the group S&P 500 competition and the nb16 employment forecast), an honest contest on nb14's 80/20 split and five folds in which an MLP is one more challenger against the nb14 champions (`LogisticRegression(C=1)`, the default random forest), read with `compare_paired` at the declared margins — unresolved on both cases, so both champions keep their jobs (Exercise 2: a deeper network earns no worthwhile gain either); softmax output is not calibrated confidence; and a **special topic + hands-on lab on Large Language Models (LLMs)** — run a sentiment classifier and a zero-shot ticket router with no API key, then optionally call a hosted model via Purdue GenAI Studio. Designed for business-undergrad audience. **Spring 2027:** Mon Mar 8. |
| 20 | Course End and Reflection | — (audit + review + survey link) | 19 (awareness arc closed) | — (last) | Self-audit, M4 poster + Kaggle submission + intra-group peer evaluation, postmortem, **course-end Reflection Survey** (10–15 min on Brightspace, required for completion). |

> **NB10 retired (Fall 2026).** The Midterm Casebook + Cheat Sheet stays out of the arc: the Fall midterm (in class, Fri Sep 25) is administered directly from the 2026Summer case bank, so no casebook notebook stages it. The Fall course covers **twenty** notebooks — nb00–nb09 and nb11–nb20.

> **NB15 and NB20 retired (Spring 2027).** The Spring arc is **eighteen** notebooks — nb00–nb09, nb11–nb14 and nb16–nb19 (`CLAUDE.md`). The nb15 and nb20 rows above are kept as the Fall 2026 record.

### Conceptual order vs. Fall delivery order

The dependency chain below is the *conceptual* order — it is what each notebook assumes and
prepares, and it does not change between offerings. The Fall **delivery** order deviates from it
in three deliberate places, because three notebooks are themselves poster or competition content
and therefore belong on Fridays.

**Conceptual modules (dependency chain):**

- **Module 1 — Foundations & Regression (nb01–nb05):** EDA/Splits → Pipelines → Metrics → Features → Regularization
- **Module 2 — Classification & Cross-Validation (nb06–nb09):** Logistic regression → Classification metrics → Cross-validation → Tuning + leakage detection
- **Module 3 — Trees, Ensembles & Selection (nb11–nb15):** Trees → Forests + importance → Boosting → Selection + test-set ceremonies → Milestone walkthrough *(Spring 2027: nb11–nb14; the walkthrough is retired)*
- **Module 4 — Delivery & Competition (nb16–nb20):** Time series → Poster design → Competition workflow → Deep learning → Closeout *(Spring 2027: Time series → S&P 500 competition workflow, which builds on nb16 Part B → Deep learning → Poster design; the closeout notebook is retired)*

**Fall delivery order (session by session):**

| Notebook | Session | Note |
|---|---|---|
| nb00 | Mon Aug 24 | Launchpad; case competition previewed (it opens Fri Sep 18, after nb07) |
| nb01 | Wed Aug 26 | |
| nb02 | **Fri Aug 28** | The one content Friday in the semester |
| nb03 | Mon Aug 31 | |
| nb04 | Wed Sep 2 | |
| nb05 | Wed Sep 9 | Live lecture (Ridge/Lasso benefits from real-time explanation) |
| nb06 | Mon Sep 14 | |
| nb07 | Wed Sep 16 | Classification arc closes here; ROC-AUC lands, so the **case competition opens** in the Fri Sep 18 studio |
| nb08 | Mon Sep 21 | |
| nb09 | Wed Sep 23 | Single session — the Fri Sep 25 midterm covers the toolkit it closes |
| **Midterm Exam** | **Fri Sep 25** | In class, on paper — 14 MC questions per case form on nb00–nb09, built from the 2026Summer case bank |
| nb11 | Mon Sep 28 | |
| nb12 | Wed Sep 30 | |
| nb13 | Mon Oct 5 | |
| nb14 | Wed Oct 7 | Test-set ceremonies — taught in person, deliberately |
| nb16 | Wed Oct 14 | First session after fall break (Oct 12–13) |
| **nb18** | **Mon Oct 19** | *Out of conceptual order.* Full coverage — random forests, boosting, and nb14's champion protocol in the submission pipeline |
| nb19 | Wed Oct 21 | |
| **nb17** | **Mon Oct 26** | *Out of conceptual order.* Last lecture — every headline number the poster reports already exists |

**Why the three deviations are safe.** nb17 has no upstream dependency at all (it forward-references
nb18 only), so it can sit anywhere; placing it last puts poster design immediately before the poster
block. nb18 depends on the classification arc for its logistic baseline and on nb11–nb14 for its ensemble
section (LASSO / random forest / gradient boosting) and champion protocol, which is why Mon Oct 19 —
after nb14 and nb16 — is its slot: the full roster runs in a single session. nb15 depends on nb14,
which is satisfied by a three-week margin.

**Spring 2027 delivery (2026-11-24).** The last notebook block runs **nb16 Mon Mar 1 → nb18 Wed Mar 3 (competition kickoff) → nb19 Mon Mar 8 → nb17 Mon Mar 22** (the last lecture, after spring break). The Spring nb18 is the S&P 500 competition workflow and depends only on nb16 Part B, so it follows nb16 directly; nb19's contest needs nb14's champions (Wed Feb 24); nb17 stays last for the same reason as in Fall. Full calendar: [`QM47400_FullSemester_Plan_2027Spring.md`](QM47400_FullSemester_Plan_2027Spring.md).

**Known drift, flagged not fixed.** nb15's row above references the Summer milestone file
`milestone_03_complex_model_and_abstract.md`. In the Fall M00–M12 track its content maps by topic to
**M08** (complex models, `NN_complex_models.pdf`) and **M03** (draft abstract). The notebooks retain
the Summer's internal "M1–M4" shorthand; that mapping is documented in
[`MGMT47400_FullSemester_Plan_2026Fall.md`](MGMT47400_FullSemester_Plan_2026Fall.md) and notebook
content is unchanged this term.

> **Cross-reference:** For full speaking prompts, cell references, and timestamps, see `video_guides/NN_video_lecture_guide.md` Sections 1–3 (Why exists, Why after N-1, Why before N+1).

---

## Maintenance

This course is built; what remains is upkeep. The authoritative procedures live in
[`../CLAUDE.md`](../CLAUDE.md) — do not duplicate them here. The short version:

| Trigger | Action |
|---|---|
| Any notebook edited | Edit the `*_instructor.ipynb` **first**, regenerate the student copy, update `video_guides/NN_video_lecture_guide.md`, and update the sequencing map above if dependencies or position changed |
| Any nb09–nb20 evaluation code touched | `python scripts/audit_cv_first.py` — only nb14 cells 30 + 34 (one ceremony per spine) are acceptable, and the data-roles check must be clean (nb16, nb18 temporal and exempt) — `RESULT: PASS` |
| Any student notebook edited | Voice grep for third-person "students" / instructor-voice language |
| Any quiz or exam CSV touched | `python scripts/audit_answer_length.py --file <csv>` must PASS before Brightspace import |
| Any content change at all | `quarto render`, commit `docs/`, push — the site is stale otherwise |
| Instructor notebook, video guide, quiz bank, or `instructor.qmd` changed | `bash _adm/_instructor_page/scripts/sync_instructor_repo.sh` |

## Open items

- **nb15 sequencing.** nb15 is delivered Fri Oct 30, after M03 (Sun Oct 4) and M08 (Sun Oct 25) are
  already submitted. It functions as a retrospective walkthrough plus the peer-review studio feeding
  M09 (Sun Nov 1) rather than as a pre-deadline guide. Re-anchoring it earlier, or re-describing the
  session, is a pedagogical decision that has not been made.
- **Milestone shorthand.** nb15, nb17, and nb20 speak the Summer "M1–M4" track internally while the
  official deliverables are M00–M12. The topic mapping is documented; a full re-key has not been done.

---

**Last updated:** 2026-08-14 — rewritten from the 2026 Summer migration runbook into the Fall 2026
notebook-content justification.
