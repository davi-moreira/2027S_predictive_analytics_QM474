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

### Sequencing Map

| NB | Title | Key Libraries/Tools | Depends On | Prepares For | Why This Position |
|----|-------|---------------------|------------|--------------|-------------------|
| 00 | Launchpad: Course Setup | Google Colab, Google Gemini | — (first) | 01 (platform ready), all subsequent | Pre-course: Colab navigation, Gemini Ask→Verify→Document, course structure, environment verification |
| 01 | EDA & Splits | pandas, numpy, matplotlib, seaborn, train_test_split | 00 (platform ready) | 02 (pipeline), all subsequent | Foundation: statistical learning framework, EDA workflow, 60/20/20 split, leakage vocabulary |
| 02 | Preprocessing Pipelines | Pipeline, ColumnTransformer, SimpleImputer, OneHotEncoder, StandardScaler | 01 (split, leakage) | 03 (metrics assume pipeline solved) | Operationalizes leakage prevention with the tool that makes safe preprocessing automatic |
| 03 | Regression Metrics & Baselines | mean_absolute_error, mean_squared_error, r2_score, DummyRegressor | 02 (pipeline) | 04 (needs metrics to measure feature engineering impact) | Teaches how to measure model quality before attempting to improve it |
| 04 | Linear Features & Diagnostics | LinearRegression, PolynomialFeatures, make_pipeline | 03 (evaluation framework) | 05 (creates overfitting problem Ridge/Lasso solves) | Feature engineering + residual analysis; exposes polynomial overfitting |
| 05 | Regularization (Ridge/Lasso) | Ridge, Lasso, RidgeCV, LassoCV, ElasticNet | 04 (overfitting problem) | 06 (complete regression toolkit before classification pivot) | Direct solution to nb04's overfitting; closes Week 1 regression arc + project proposal |
| 06 | Logistic Regression & Pipelines | LogisticRegression, accuracy_score, log_loss | 05 (regularization via alpha → C) | 07 (needs probability foundations) | Regression → classification pivot; reuses Pipeline pattern in new context |
| 07 | Classification Metrics | confusion_matrix, precision/recall/f1, roc_curve, precision_recall_curve | 06 (probabilities, confusion matrix) | 08 (needs metric vocabulary for CV scoring) | Complete classification evaluation toolkit; cost-based threshold selection |
| 08 | Cross-Validation | cross_val_score, StratifiedKFold, cross_validate | 07 (metrics for scoring param) | 09 (CV embedded inside grid search) | Reliable model comparison replacing fragile single split |
| 09 | Tuning + Feature Eng. + Leakage Detection | GridSearchCV, RandomizedSearchCV, ColumnTransformer, FunctionTransformer, OneHotEncoder, SelectKBest | 08 (standalone CV) | 18 (competition workflow needs the full pipeline template), 11 (full toolkit before the tree-based arc), 13 (leakage callout bridges here) | Three-section single file with opening toolkit-closer banner (cell 1, before LO): (A) grid search as nb08 × a grid with CI-overlap ranking + `C`-parameter primer; (B) TechCorp synthetic business case with real categoricals + target-encoding leak + SelectKBest leak detection; (C) Toolkit Recap — one-page reference consolidating concepts, workflow, sklearn primitives, decision rules across nb01–nb09 |
| 11 | Decision Trees (paired clf + reg) | DecisionTreeClassifier on breast cancer + DecisionTreeRegressor on California Housing, plot_tree, paired depth sweep with the plot_train_val_curve helper, predicted-vs-actual scatter | 09 (evaluation skills consolidated) | 12 (high-variance problem motivates forests; dual-spine pattern continues) | First non-linear model on both spines; concrete bias-variance demonstration via paired depth sweep; one-SE-rule depth selection on each spine; `_clf` / `_reg` namespace convention introduced here and used through nb15. **§7 verdicts:** classification keeps `LogReg(C=1.0)` (CI-clear win); regression switches to `DecisionTreeRegressor(max_depth=5)` under the **dominance tiebreaker** — tree CV mean 0.613 AND lower-CI 0.604 both above OLS's 0.586 and 0.554 → modest winner. OLS becomes the close-second runner-up; the tree is the new regression floor for nb12 |
| 12 | Random Forests + Importance (paired clf + reg) | RandomForestClassifier on breast cancer + RandomForestRegressor on California Housing; **joint 3D `(n_estimators × max_features × max_depth)` tuning grid** that **includes nb11's per-case `max_depth` picks (3 clf / 5 reg) as candidates alongside `None`**; CV mean + 95% CI half-width annotated per cell (red rectangle marks the largest-mean-smallest-CI cell per case); permutation_importance, OOB scoring on both, drop-column refit; four-method importance heatmap; CV-CI dot plot with nb09 references as the floor | 11 (tree instability on both cases) | 13 (bagging baseline for boosting contrast), 15 (feature-importance plot required by the M03 walkthrough) | Parallel ensemble solving single-tree variance on both cases; **four-method feature-importance reconciliation heatmap** (linear coef / MDI / permutation / drop-column); §5 joint 3D grid lands on `(n_estimators=50, max_features='sqrt', max_depth=3)` for clf (**nb11's depth survives** — all 27 cells tie under CI-overlap, parsimony picks the simplest) and `(n_estimators=50, max_features=0.5, max_depth=None)` for reg (**nb11's depth does NOT survive** — depth-3 and depth-5 cells are CI-clear below depth-None on California Housing); comprehensive comparison plot benchmarks single tree, forest, and nb09 reference |
| 13 | Gradient Boosting (paired clf + reg) | GradientBoostingClassifier on breast cancer + GradientBoostingRegressor on California Housing, **joint 4D tuning grid** `n_estimators × learning_rate × max_features × max_depth` (54 cells per case across 12 panels, CV mean + 95% CI half-width annotated per cell, red rectangle marks the largest-mean-smallest-CI cell per case) that includes nb12's per-case RF shipped `(max_features, max_depth)` pairs as candidates | 12 (bagging baseline on both cases) | 14 (needs full candidate roster: Reference, Tree, RF, default GBM, tuned GBM per case) | Sequential ensemble on both cases; bias reduction vs variance reduction contrast; the 4D grid lands on **the same config for both cases** — `(learning_rate=0.2, n_estimators=200, max_features=0.5, max_depth=3)`; nb12's clf RF pick `(mf='sqrt', md=3)` transfers cleanly; nb12's reg RF pick `(mf=0.5, md=None)` does NOT transfer (unlimited depth overfits in boosting); tuned GBM ships regression as a **modest winner**: higher mean R² (0.8117 vs 0.8038), lower mean RMSE, ≈-tied MAE, AND higher CV CI lower bound (0.7983 vs 0.7937) than nb12's RF — the dominance tiebreaker breaks the upper-end CI overlap in the GBM's favor (the RF stays as the close-second runner-up); **leaky-features-dominate-boosting callout** referencing nb09 |
| 14 | Model Selection Protocol + Two Ceremonies + Post-Deployment Monitoring (paired clf + reg) | comparison harness (`compare_models_comprehensive`, post-hoc multi-metric CV using nb03/nb06/nb07 metric functions — no `neg_*` scoring strings), Student's *t* 95% CI helper, verdict helper, money plot for INSIDE/ABOVE/BELOW, `scipy.stats.ks_2samp` for the §7.4 drift-detection demo | 13 (full candidate pool on both cases), 08 (CI vocabulary) | 15 (champion committed for downstream tuning + deployment walkthrough) | Formal, fair, reproducible comparison on **both** cases; **7 classification candidates** (Dummy, LogReg(C=1.0), LogReg L1, Tree(d=3), RF(n=50, sqrt, d=3) — nb12 ship, GBM default, GBM tuned (lr=0.2, n=200, mf=0.5, d=3) — nb13 ship) and **8 regression candidates** (Dummy, OLS, Ridge, Lasso, Tree(d=5), RF(n=50, mf=0.5) — nb12 ship, GBM default, GBM tuned (lr=0.2, n=200, mf=0.5, d=3) — nb13 ship); **two parallel test-set ceremonies** with explicit singleness-rule callout (one ceremony per project, two in this notebook are pedagogical demos); **§6.3 verdict playbook** (INSIDE → ship + record CI / test point / retrain triggers; small-drift ABOVE → ship with documented gap from Step 1's train+val refit; large-drift ABOVE → investigate before deploying; BELOW → STOP, diagnose pipeline, test-set-is-spent rule requires a NEW test set before re-opening); champions: LogReg(C=1.0) clf (CI-overlap with tree ensembles → parsimony picks the linear baseline), **tuned GBM (lr=0.2, n=200, mf=0.5, d=3) reg** (modest winner over the RF on mean R², RMSE, MAE, AND CV CI lower bound — same pick as nb13 §7); **§7 post-deployment monitoring** — Silent decay (data drift / concept drift / population shift) vs Front-door arrivals; Three R's escalation ladder (Re-evaluate → Re-train → Rebuild); case-specific monitoring checklists (MedScreen: reliability + Brier, recall, KS drift on top-3 features, population composition; HomeValue: MAE/RMSE, errors by price tier, errors by location grid, KS drift on top features, major outside events); coded KS demo with alert on KS statistic (not p-value); one-page Monitoring Card; `audit_cv_first.py` exception list updated for both ceremony cells |
| 15 | Final Project Milestone 03 Walkthrough — Complex Model + Hyperparameter Tuning + Draft Abstract | **Markdown-only walkthrough** (no code, no PAUSE-AND-DO) — companion read for the `milestone_03_complex_model_and_abstract.md` rubric | 14 (champion committed), 09 (hyperparameter tuning), 08 (CI-overlap rule) | 16 (time-series CV splitter pivot) | Same shape as nb05 §6/§7. Sections map directly to the M3 rubric: §0 Prediction Goals, §1a Baseline Replication (M2) with 95% CI, §1b Complex Model + Tuning + CI-overlap rule + final-training step on the full training fold (with random_state locked so M4 reproduces the same fitted Pipeline), §1c Required Visualizations, §2 Draft Abstract (~250 words), Course Case Competition (Kaggle Bank Churn) alignment, and Tips and Common Pitfalls. **No Interpretation, Calibration, or Decision-Quality content.** |
| 16 | Time-Series Forecasting | TimeSeriesSplit, lag features (`pd.shift`), LinearRegression | 15 (closes static-classification arc), 08 (CV CIs), 14 (locked-test ceremony pattern) | 17 (forecast as a candidate poster figure) | Forecasting ≠ generic supervised: never shuffle, walk-forward CV, lag features, three-baseline comparison (naive / seasonal-naive / linear-with-lags) on identical CV folds, one-shot opening of the locked test window. |
| 17 | Data Communication & Poster Design (formerly nb19) | — (markdown/narrative, no new libraries) | 15+16 (headline numbers, CV-CI, locked-test verdict, forecast comparison) | 20 (poster + abstract feed M4) | Six principles applied to the eleven-section URC poster architecture; chart audit + outline + 120–150-word abstract drafted in studio. **Fall 2026:** taught in week 10, Mon Oct 26, as the last content session — every headline number the poster reports already exists by then, and the deadline (M10, Sun Nov 8) and the URC presentation (Tue Nov 17) follow immediately. |
| 18 | Competition Workflow & Kaggle Submission | ColumnTransformer, Pipeline, GradientBoostingClassifier, joblib, pandas.to_csv | 09 (full pipeline + tuning template) | 19 (gradient-boosted tabular champion as the comparison anchor for DL) | End-to-end production pipeline for the Bank Churn case competition: `train_pipeline` / `predict_pipeline` refactor → `joblib` save/load → `submission.csv` with exact Kaggle column names. The Kaggle test set is unlabeled — `predict_proba(X_test)` is production prediction, not model evaluation (audit_cv_first.py exception). **Fall 2026:** taught Mon Oct 19, once random forests, gradient boosting, and nb14's selection protocol give each team a champion worth packaging; the Fri Sep 25 slot right after nb09 hosts the in-class midterm exam. |
| 19 | Deep Learning | PyTorch (`torch`/`torchvision`) for the §4 FashionMNIST lab; `sklearn.neural_network.MLPClassifier`/`MLPRegressor` for the §5 comparison against nb14's champions; **Hugging Face `transformers`** for the §6 LLM lab (sentiment + zero-shot pipelines); `requests` for the optional Purdue GenAI Studio API call; figures from `notebooks/figures/` | 18 (gradient-boosted tabular champion) | 20 (course-end horizon module) | Awareness + hands-on module: historical arc, frameworks, MLP / CNN / RNN / Transformer structural inventions, **end-to-end PyTorch training on FashionMNIST**, four-question rubric for "is DL right for this problem?", an honest deep-learning-vs-nb14-champion comparison on both business cases (Breast Cancer classification and California Housing regression) with cross-validation confidence-interval plots and per-case verdicts, and a **special topic + hands-on lab on Large Language Models (LLMs)** — run a sentiment classifier and a zero-shot ticket router with no API key, then optionally call a hosted model via Purdue GenAI Studio. Designed for business-undergrad audience. |
| 20 | Course End and Reflection | — (audit + review + survey link) | 19 (awareness arc closed) | — (last) | Self-audit, M4 poster + Kaggle submission + intra-group peer evaluation, postmortem, **course-end Reflection Survey** (10–15 min on Brightspace, required for completion). |

> **NB10 retired (Fall 2026).** The Midterm Casebook + Cheat Sheet stays out of the arc: the Fall midterm (in class, Fri Sep 25) is administered directly from the 2026Summer case bank, so no casebook notebook stages it. The Fall course covers **twenty** notebooks — nb00–nb09 and nb11–nb20.

### Conceptual order vs. Fall delivery order

The dependency chain below is the *conceptual* order — it is what each notebook assumes and
prepares, and it does not change between offerings. The Fall **delivery** order deviates from it
in three deliberate places, because three notebooks are themselves poster or competition content
and therefore belong on Fridays.

**Conceptual modules (dependency chain):**

- **Module 1 — Foundations & Regression (nb01–nb05):** EDA/Splits → Pipelines → Metrics → Features → Regularization
- **Module 2 — Classification & Cross-Validation (nb06–nb09):** Logistic regression → Classification metrics → Cross-validation → Tuning + leakage detection
- **Module 3 — Trees, Ensembles & Selection (nb11–nb15):** Trees → Forests + importance → Boosting → Selection + test-set ceremonies → Milestone walkthrough
- **Module 4 — Delivery & Competition (nb16–nb20):** Time series → Poster design → Competition workflow → Deep learning → Closeout

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
| Any nb09–nb20 evaluation code touched | `python scripts/audit_cv_first.py` — only nb14 cells 30 + 34 (one ceremony per spine) and nb18's Kaggle demo are acceptable |
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
