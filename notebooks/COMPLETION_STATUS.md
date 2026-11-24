# Notebook Creation Status

**Spring 2027 edition — status as of the 2026-11-24 rollout.** Session reports: `_adm/2027S_setup_2026-11-24/reports/` (rollout-early, rollout-core, rollout-trees, sp500-competition).

## Rebuilt / updated 2026-11-24 (18/18 Spring notebooks)
✅ Instructor copy edited first, student copy derived; executed headless (seed 474, scikit-learn 1.6.1), 0 errors; gates clean

| NB | 2026-11-24 change | Headless run | Gates | Colab "Run all" |
|---|---|---|---|---|
| nb00 Launchpad | Updated — course map (one champion per case, criteria stated before scoring), group S&P 500 competition, arc in teaching order nb16 → nb18 → nb19 → nb17 | ✅ | ✅ | ⏳ not done |
| nb01 EDA & Splits | Updated — workflow preview (incumbent, criteria block, ladder); leakage demo no longer scores `y_test` | ✅ | ✅ | ⏳ not done |
| nb02 Preprocessing Pipelines | Updated — Exercise 2 is a provisional single-split comparison against a declared gap | ✅ | ✅ | ⏳ not done |
| nb03 Regression Metrics & Baselines | Updated — template records incumbent, decision margins, provisional status | ✅ | ✅ | ⏳ not done |
| nb04 Linear Features & Diagnostics | Updated — "validation leader", not winner | ✅ | ✅ | ⏳ not done |
| nb05 Regularization | Updated — a tuning maximum is a nominee; competition section → S&P 500 | ✅ | ✅ | ⏳ not done |
| nb06 Logistic Regression & Pipelines | Updated — `LogisticRegression(C=1)` named incumbent; FP/FN labels and numbers re-derived | ✅ | ✅ | ⏳ not done |
| nb07 Classification Metrics | Updated — new Section 6 (Brier score + reliability curve); MedScreen decision rules | ✅ | ✅ | ⏳ not done |
| nb08 Cross-Validation | Rebuilt — `compare_paired` and the four outcomes; ends on one 80/20 split + five folds | ✅ | ✅ | ⏳ not done |
| nb09 Tuning + FE + Leakage | Rebuilt — a search's best cell is a nominee that faces the default; one 80/20 split | ✅ | ✅ | ⏳ not done |
| nb11 Decision Trees | Rebuilt — readability caps, one-SE nominee, `compare_paired` | ✅ | ✅ | ⏳ not done |
| nb12 Random Forests | Rebuilt — nominee vs default forest; importance inside the 5-fold loop; champion ladder | ✅ | ✅ | ⏳ not done |
| nb13 Gradient Boosting | Rebuilt — instructor order repaired; nominee vs default GBM; four-step ladder | ✅ | ✅ | ⏳ not done |
| nb14 Model Selection Protocol | Rebuilt — criteria block → `champion_ladder` → frozen champion → one ceremony per case | ✅ | ✅ | ⏳ not done |
| nb16 Time-Series Forecasting | Rebuilt — walk-forward origins, Seasonal-Naive incumbent, S&P 500 Part B | ✅ | ✅ | ⏳ not done |
| nb17 Data Communication & Poster | Updated — §14 paired-gain chart + champion statement | ✅ | ✅ | ⏳ not done |
| nb18 Competition Workflow | Replaced — S&P 500 group forecasting competition workflow | ✅ | ✅ | ⏳ not done |
| nb19 Deep Learning | Updated — MLP vs the nb14 champions with `compare_paired`; Exercise 1 → S&P 500 competition | ⚠️ partial (see below) | ✅ | ⏳ not done |

**Gates run:** voice grep on every student copy (only sanctioned matches remain: "Student's t" in nb08, nb09 and nb18, and the CCO URL path `…/Students/…` in nb17); no `INSTRUCTOR SOLUTION` in any student copy; JSON valid, student = instructor minus solution cells; `scripts/audit_cv_first.py` prints `RESULT: PASS` (test-set lock: only nb14 cells 30 + 34; data roles clean, nb16 and nb18 exempt); `scripts/voice_check_guides.py` clean on the changed guides; `scripts/audit_answer_length.py` PASS on every changed quiz bank.

## Still to do
⏳ **Colab "Runtime → Run all"** on all 18 student notebooks — not done for any of them. nb12 and nb13 are the slow ones (≈6.6 and ≈4.8 minutes of compute with 2 workers locally; free Colab is likely slower).
⏳ **nb19:** the FashionMNIST cells (c16–c47, PyTorch/torchvision) and the LLM cells (c71–c81, transformers) were **not executed locally** (code unchanged); run nb19 end to end in Colab.

## Retired (not in the Spring 2027 arc)
nb10 (midterm casebook), nb15 (M03 walkthrough), nb20 (course wrap). The nb15 and nb20 files remain in `notebooks/` as Fall 2026 versions; they were not rebuilt.

## Target
🎯 18/18 Spring 2027 notebooks Colab-verified before release
