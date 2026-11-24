## Notebook Sequence and Content Justification

### Design Philosophy

The 20 notebooks (NB00–NB09 and NB11–NB20) follow a **single-layer-at-a-time** principle: each notebook introduces exactly one new concept, assumes only what prior notebooks taught, and prepares exactly what the next one needs. No notebook can be skipped without breaking its successor's assumptions.

The course is organized into a **pre-course orientation** and **four weekly arcs**, each ending with a project milestone that forces students to integrate that week's skills.

> **Fall 2026 note.** NB10 (the Midterm Casebook) stays retired from the arc — the Fall 2026 midterm is an in-class paper exam (Fri Sep 25) built directly from the 2026Summer case bank, so no casebook notebook stages it — leaving **20** notebooks. The four arcs below describe the conceptual sequence, not calendar weeks: Fall 2026 re-paces the same arc across \~15 weeks, with Monday and Wednesday carrying content and every Friday reserved as a poster and/or competition studio — the exceptions are Fri Aug 28, which carries NB02, and Fri Sep 25, which hosts the in-class midterm exam.

> **Spring 2027 note (2026-11-24).** Spring 2027 runs **18** notebooks — NB00–NB09, NB11–NB14 and NB16–NB19; NB10, NB15 and NB20 are retired (their rows below are marked). The rollout of 2026-11-24 rebuilt every remaining notebook, and the tables below describe them as they now stand. NB01–NB07 keep the 60/20/20 split; NB08's validation split only motivates cross-validation, and from NB09 on each dataset is split once 80/20 with five folds on `X_train`. Every model comparison is `compare_paired` — paired per-fold gains, an interval corrected for fold overlap, read against a margin band declared before scoring (0.005 / 0.01 / 0.02; the base margin decides) as one of four outcomes — and there is no per-model 95% interval. A search's best cell is a nominee that faces the family default, and champions come from a simplest-first ladder. NB16 and NB18 are temporal (walk-forward origins, per-origin differences described). Spring teaching order for the last block: NB16 Mon Mar 1 → NB18 Wed Mar 3 → NB19 Mon Mar 8 → NB17 Mon Mar 22; full calendar in `_project_docs/QM47400_FullSemester_Plan_2027Spring.md`.

---

### Pre-Course — Orientation (NB 00)

**Goal:** Eliminate all setup friction so Day 1 can focus entirely on analytics content.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **00** Launchpad: Course Setup | Colab navigation, Gemini Ask→Verify→Document, course structure, environment verification; the course map (every case ends with one champion and a written reason, chosen by criteria stated before scoring) and a preview of the group S&P 500 forecasting competition on Kaggle | Day 0 pre-course activity. Students can't engage with any technical content until they understand the platform and AI assistant policy. Separating logistics from analytics prevents NB01 from being overloaded. |

**Arc logic:** Platform fluency → ready for content.

---

### Week 1 — The Regression Arc (NB 01–05)

**Goal:** Build the complete supervised learning workflow from scratch, using regression as the vehicle.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **01** EDA & Splits | Statistical learning framework (Y = f(X) + ε), EDA checklist, 60/20/20 splits (the split NB01–NB07 use), leakage vocabulary, bias-variance trade-off; a workflow preview that names the incumbent and ends in one champion with a stated reason | The conceptual foundation. Students can't preprocess, model, or evaluate until they understand predictive analytics concepts, data exploration, and why splitting matters. NB00 handled platform setup; NB01 handles content. |
| **02** Preprocessing Pipelines | Pipeline + ColumnTransformer (impute, encode, scale) | NB01 taught *why* you must fit only on training data; NB02 teaches the *tool* that enforces it. Separating these avoids cognitive overload. |
| **03** Regression Metrics & Baselines | MAE, RMSE, R², DummyRegressor baseline; an evaluation template that records the incumbent model, the decision margins (0.005 / 0.01 / 0.02 R²) and a provisional status | You must know how to *measure* quality before trying to *improve* it. NB04's feature engineering would be blind without metrics. |
| **04** Linear Features & Diagnostics | PolynomialFeatures, interactions, residual analysis; the best single-split model is only a "validation leader" | Now that students can measure improvement, they learn to engineer features — and discover the overfitting problem when 8 features explode to 44. |
| **05** Regularization (Ridge/Lasso) | RidgeCV, LassoCV, coefficient shrinkage/sparsity; a tuning maximum is a nominee, not a champion | The direct solution to NB04's overfitting. These two notebooks form a deliberate **problem → solution pair**. Also hosts the project proposal milestone, closing the regression arc, and introduces the group S&P 500 competition that kicks off with NB18. |

**Arc logic:** Concepts & data workflow → Safe preprocessing → Measurement → Improvement → Control. Each step is prerequisite to the next.

---

### Week 2 — The Classification Arc (NB 06–09)

**Goal:** Pivot to classification, build a richer evaluation toolkit, and learn systematic model comparison.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **06** Logistic Regression & Pipelines | Predicted probabilities, threshold sensitivity, regularization via C; `LogisticRegression(C=1)` named MedScreen's screening incumbent | The regression-to-classification pivot. Reuses the same Pipeline pattern from Week 1, making the transition seamless. Students need probability foundations before NB07's metrics. |
| **07** Classification Metrics & Thresholding | Precision, recall, F1, ROC/PR curves, cost-based threshold selection; **Section 6: probability quality — Brier score + reliability curve** | NB06 introduces probabilities informally; NB07 formalizes them into a complete metrics framework, and shows that a good ROC-AUC does not mean good probabilities. Its wrap-up declares MedScreen's decision rules (ROC-AUC primary, margins 0.005 / 0.01 / 0.02, a malignant-recall safety guardrail and a Brier probability-quality guardrail) before NB08 compares models. NB08 needs this vocabulary to choose a `scoring` parameter for CV. |
| **08** Cross-Validation & Model Comparison | StratifiedKFold, cross_val_score, cross_validate; `compare_paired` and the four outcomes; the margin band; one 80/20 split and five folds | Replaces the fragile single train/val split (which here only motivates CV): fold scores, mean and SD describe a model, with no per-model interval, and `compare_paired` — per-fold gains on identical folds, an interval corrected for fold overlap, read against a margin declared before scoring — decides between two models. It ends on the one 80/20 split and five folds every later notebook uses. Students must understand standalone CV before NB09 embeds it inside grid search. |
| **09** Tuning & Feature Engineering | GridSearchCV, RandomizedSearchCV — a search's best cell is a nominee that faces the default with `compare_paired`; target-encoding leak; project baseline scaffold | Integration notebook — brings together pipelines, metrics, CV, and tuning into a single workflow on one 80/20 split. Provides the baseline report template the project baseline depends on, and closes the arc. Project baseline due. |

> **NB10 retired.** The Midterm Casebook used to close this arc with a strategic-reasoning assessment — "Given this business problem, what's the target? metric? split? leakage risk?" For Fall 2026 that assessment is the in-class paper midterm (Fri Sep 25), administered directly from the 2026Summer case bank, so the casebook stays retired. NB09's Toolkit Recap carries the consolidation, and the exam carries the applied strategy assessment.

**Arc logic:** New task type → New metrics → Reliable comparison → Integration.

---

### Week 3 — The Ensembles Arc (NB 11–15)

**Goal:** Introduce non-linear models, ensembles, formal model selection, and interpretation.

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **11** Decision Trees | CART, paired depth sweep (training vs cross-validated scores), overfitting demo, tree visualization; readability caps (depth ≤ 3 / ≤ 5) declared up front; the one-SE heuristic nominates, `compare_paired` decides | The first non-linear model, opening on the evaluation skills NB09 consolidated. Students see the bias-variance tradeoff concretely: training scores climb toward perfect while cross-validated scores stall, and both trees come out unresolved against the NB09 references, which stay. This instability motivates NB12. |
| **12** Random Forests | Bagging, random feature subsets, OOB; a 27-cell grid whose nominee faces the default forest; permutation and drop-column importance computed on held-out folds | Solves the single tree's variance problem by averaging many decorrelated trees. The "parallel ensemble" concept only lands after students experience NB11's instability firsthand. The default forest is carried on both cases; on HomeValue it is promoted over OLS (+0.199 [+0.180, +0.218]), while MedScreen's logistic regression stays (forest unresolved). |
| **13** Gradient Boosting | Sequential error correction, learning rate × n_estimators coupling, constrained tuning; a grid nominee that faces the default GBM | Completes the ensemble trilogy. The contrast — bagging reduces variance (NB12) vs. boosting reduces bias (NB13) — is the deepest conceptual point in the course. Its four-step ladder shows that the highest mean is not automatically the champion: the tuned GBM's gain over the forest (+0.018 [+0.009, +0.027]) is unresolved, so the forest stays — a margin-sensitive call (cutoff 0.0091). |
| **14** Model Selection Protocol | Criteria block declared before scoring, fold scores on identical folds, `champion_ladder`, frozen champion, one test-set ceremony per case (champion refit on `X_train`), post-deployment monitoring | Now that the full candidate roster exists (logistic, tree, RF, GBM), a formal protocol replaces the informal "pick the highest number" approach. Premature without all candidates. Champions: `LogisticRegression(C=1)` (robust) and the default random forest (margin-sensitive vs the tuned GBM). In each ceremony the deployment bar decides; INSIDE / ABOVE / BELOW only describes. |
| **15** *(retired in Spring 2027)* Interpretation & Error Analysis | Permutation importance, PDP/ICE, segment-level error analysis | Answers "what is the champion learning and where does it fail?" Interpretation only makes sense after committing to one model (NB14). Project improved model due. |

**Arc logic:** Non-linear model → Parallel ensemble → Sequential ensemble → Fair selection → Explain the winner. In Spring 2027 the arc ends at Fair selection (NB15 retired): a simplest-first ladder and one ceremony per case.

---

### Week 4 — The Production Arc (NB 16–20)

**Goal:** Bridge from "model works in a notebook" to "model deployed responsibly and communicated clearly."

| NB | What It Teaches | Why Here |
|----|----------------|----------|
| **16** Time-Series Forecasting | Temporal train/test split (last 12 months locked) + walk-forward validation (five origins one year apart = five folds); Seasonal-Naive incumbent vs Naive, Drift, ETS, SARIMA and a lag-feature Ridge; paired per-origin differences described; forecast bands judged calibration first; an S&P 500 walk-forward race against the random walk | The course's exception to the random 80/20 split, which NB18 inherits. It reuses NB08's paired comparison (described per origin, with a Diebold–Mariano Q&A, rather than given a four-outcome verdict) and NB14's ceremony (the locked year opened once for the declared incumbent). Part B — log returns, the ACF of returns vs absolute returns, a 104-origin weekly race against the random walk, the random-walk volatility band — is the preparation for the Course Case Competition. statsmodels + scikit-learn + yfinance, all preinstalled in Colab. |
| **17** Data Communication & Poster Design | Six design principles, chart audit, eleven-section URC poster architecture, 120–150-word abstract; the paired-gain chart and the champion statement (§14) | The last content session — **Mon Mar 22** in Spring 2027 (Mon Oct 26 in Fall 2026). Every headline number the poster reports — fold scores with mean and SD, the champion's paired gain with its interval corrected for fold overlap, the locked-test verdict, the forecast comparison — already exists by this point, so the notebook is purely about turning results into a story a conference visitor can read in ninety seconds. Placing it last puts poster design immediately ahead of the poster deadline (M10, Sun Apr 4) and the Spring Undergraduate Research Conference (Tue Apr 13). |
| **18** Course Case Competition Workflow: Forecasting the S&P 500 | Information cutoff (`DATA_END`), quantile forecasts at 1/5/10/15/20 trading days, the competition's scaled pinball loss and random-walk benchmark, a 104-Thursday walk-forward backtest with described paired gains, calibration of 50%/80% bands, a validated, reproducible submission file | Replaces the bank-churn workflow. It builds directly on NB16 Part B and is taught right after it (**Wed Mar 3** in Spring 2027) as the kickoff of the group S&P 500 forecasting competition: a Kaggle practice round, then a live forecast scored on the real market. Temporal like NB16, so there is no random split and no `X_test`. No quiz. |
| **19** Deep Learning | Historical arc, frameworks, MLP / CNN / RNN / Transformer inventions, PyTorch training on FashionMNIST, the four-question rubric for "is DL right for this problem?", an MLP vs the NB14 champions with `compare_paired`, an LLM lab | Taught after the competition launch (**Mon Mar 8** in Spring 2027). The MLP is one more challenger on each case's ladder, scored on NB14's 80/20 split and five folds against `LogisticRegression(C=1)` and the default random forest — unresolved on both cases, so both champions keep their jobs, and a deeper network earns no worthwhile gain either. Exercise 1 applies the rubric to the S&P 500 competition and the NB16 employment forecast; softmax output is not calibrated confidence. |
| **20** *(retired in Spring 2027)* Final Submission & Peer Review | Self-audit checklist, artifact manifest, peer review rubric, postmortem | The capstone: audit your own work, submit the complete package, evaluate a peer's project, and reflect. Closes the course arc from NB00's first Colab session and NB01's first data split to a fully reviewed deliverable. |

**Arc logic:** Forecasting on time-ordered data → Competition workflow → Deep learning tested against the champions → Poster design. Spring 2027 teaches them in that order — NB16 Mon Mar 1 → NB18 Wed Mar 3 → NB19 Mon Mar 8 → NB17 Mon Mar 22, the last lecture; NB20 is retired. (Fall 2026, with the bank-churn NB18, ran NB16 Wed Oct 14 → NB18 Mon Oct 19 → NB19 Wed Oct 21 → NB17 Mon Oct 26.)

---

### Cross-Cutting Design Choices

- **Every week ends with a project milestone** (Proposal → Baseline → Improved Model → Final), ensuring students apply each arc's skills to their own data immediately.
- **The dependency arrows within each week are strict** — each notebook assumes the previous one is mastered. Between weeks, the dependency is softer (consolidation happens at milestone boundaries).
- **Tools are introduced once and reused** — Pipeline appears in NB02 and is used in every subsequent modeling notebook. CV appears in NB08 and is embedded inside grid search in NB09+. This "teach once, reuse always" pattern reduces cognitive load.
- **The course alternates between building and evaluating** — NB02 builds pipelines, NB03 evaluates them. NB04 builds features, NB05 controls them. NB11–NB13 build the challengers, NB14 selects the champion. This rhythm teaches students that construction without evaluation is reckless.
