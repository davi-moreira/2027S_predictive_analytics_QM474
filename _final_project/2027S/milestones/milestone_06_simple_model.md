---
kicker: "Milestone 06"
title: "Simple Model and Performance Evaluation"
csv: ["Milestone 06 —"]
box:
  - label: Due
    value: "**Sunday, March 7, 2027, 11:59 PM ET**"
  - label: Opens
    value: "Thursday, February 18, 2027"
  - label: Submit
    value: "Two files per group, uploaded by one member: the report `NN_simple_model.pdf` and your code (a `.py` script or a `.ipynb` notebook that runs on your dataset)"
  - label: Grading
    value: "100 points"
---

## What this milestone is for

This is your first real model. You explore the data, prepare it, and fit the simplest reasonable model, evaluated honestly with cross-validation. That model is your **baseline**: the reference every more complex model must beat in Milestone 08, and, if nothing beats it by enough to matter, your champion.

## What to do

Write a report with these labeled sections.

0. **Prediction goal(s).** State them clearly and say why they matter; say whether this is regression (a continuous response) or classification (a categorical one).
1. **Dataset exploration.** (a) An overview: the number of observations and features, a short description of each feature (type, range), and the response. (b) Summary statistics for the response, at least one useful chart, and what stands out (skew, outliers). (c) The type of each predictor and the relationship you expect with the response, from domain knowledge or a first look at correlations.
2. **Feature engineering.** Create at least one new feature that could improve performance or interpretability (a combination of features, a time-based feature, an interaction) and explain why.
3. **Missing values.** Which features have missing values and how many, and your strategy (dropping or imputing), with the reason. For full marks, compare it with at least one alternative.
4. **Baseline model.** (a) The model: linear regression for a continuous response, logistic regression for a categorical one, and why. (b) The implementation: a feature-selection procedure run inside five-fold cross-validation, with the cross-validation score used to choose. (c) Interpretation and next steps: what the results say, and whether more feature work, selection or tuning is needed.

**How to evaluate: the course's rules from notebook 08 on.**

- **Split once, at the start**: 80% training set, 20% test set, with `train_test_split(X, y, test_size=0.20, random_state=474)` (add `stratify=y` for classification). Then put the test set away. You open it once, at the very end, for your chosen model only.
- **Everything else runs on the training set, with five-fold cross-validation**: `KFold(n_splits=5, shuffle=True, random_state=474)` for regression, `StratifiedKFold` with the same settings for classification. Keep the splitter in a variable: Milestone 08 reuses exactly the same folds.
- **Keep preprocessing and feature selection inside a pipeline**, so each fold refits them on its own training rows. Anything fitted on all the rows first leaks information.
- **Report your baseline's five fold scores, their mean and their standard deviation.** [[PENDING D4: whether to report a per-model 95% interval — currently: report fold scores, mean and SD]]

## What to submit

One member uploads two files for the whole group. The **report**, `NN_simple_model.pdf`, has the labeled sections 0 to 4, explanations in paragraphs, charts embedded, and key code snippets in the sections or an appendix. The **code** is your Python script or Jupyter notebook, which must run on your dataset.

## How it is graded

One hundred points, by criterion:

| Criterion | Points |
|------------------------------------------------------------|-----:|
| 0\. Prediction goal(s): clear, specific, with the problem type | 5 |
| 1\. Dataset exploration: overview, statistics, charts, insight | 20 |
| 2\. Feature engineering: a new feature with a convincing reason | 15 |
| 3\. Missing values: identified, a justified strategy, an alternative compared | 10 |
| 4a. Model choice: the simplest reasonable model, justified | 5 |
| 4b. Implementation: feature selection inside five-fold CV, CV used to choose | 15 |
| 4c. Interpretation and next steps | 10 |
| 5\. Report quality: clear structure, labeled charts and code, code runs without errors | 20 |

## Tips

- Lean on notebooks 02 (pipelines), 03 and 07 (metrics), and 08 and 09 (cross-validation, and feature selection inside the pipeline).
- Never use the test set to choose features or models. If you catch yourself scoring on it, stop.
- If your data are ordered in time, split by time and validate walk-forward instead (notebook 16), so the model never trains on the future.
- Run your notebook from top to bottom on a fresh runtime before you submit.

*The Final Project Overview PDF has every date, the meeting rounds, and how the project is graded.*
