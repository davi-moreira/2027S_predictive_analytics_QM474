---
kicker: "Milestone 08"
title: "More Complex Models and Performance Evaluation"
csv: ["Milestone 08 —"]
box:
  - label: Due
    value: "**Sunday, March 14, 2027, 11:59 PM ET**"
  - label: Opens
    value: "Thursday, February 18, 2027"
  - label: Submit
    value: "Two files per group, uploaded by one member: the report `NN_complex_models.pdf` and your code (a `.py` script or a `.ipynb` notebook that runs on your dataset)"
  - label: Grading
    value: "100 points"
---

## What this milestone is for

You try a more complex model, tune it, and then decide, on the evidence, whether it is worth more to your stakeholder than your baseline. The model you choose here, your **champion**, is the one on your poster and in Poster-to-Product. The baseline can be the champion: a more complex model has to earn its place.

## What to do

Write a report with these labeled sections. Everything runs on the **training set** of your Milestone 06 split, with the **same five folds** (the same splitter object and seed).

**0. Prediction goal(s).** State them, say why they matter, and confirm whether this is regression or classification.

**1a. Baseline model** (you may reuse Milestone 06). The simplest reasonable model (linear or logistic), with feature selection inside five-fold cross-validation and the metric you use to compare predictor sets, its five fold scores, mean and standard deviation, and a short interpretation.

**1b. A more complex model, tuned, and your champion.**

1. *The model.* Choose a more complex model (for example a random forest, an SVM or gradient boosting) and say what it could capture that the baseline cannot, such as non-linear effects or interactions.
2. *Tuning.* Define a grid of hyperparameter values, evaluate them with five-fold cross-validation on the training set, and report the metric and the results in a table or a plot. [[PENDING D3/R1: how tuned models are evaluated]]
3. *The comparison* (notebooks 08 and 14). **Before you compare**, write down your primary metric and your **margin δ**: the smallest gain that would change your stakeholder's decision, with what it means in their terms (dollars, missed cases, customers). [[PENDING R12: required vs optional parts of the comparison]] Start with the baseline as the champion. Then, for each challenger, take the five per-fold differences (challenger minus champion, on the same folds), their mean, and the interval around that mean corrected for the overlap between folds, with `compare_paired` from notebook 08. Read the result as one of **four outcomes**:
   - *worthwhile gain*: the whole interval is above +δ, so the challenger becomes the champion;
   - *worthwhile loss*: the whole interval is below −δ, so the champion stays;
   - *practically equivalent*: the whole interval lies between −δ and +δ, so you keep the simpler model;
   - *unresolved*: anything else, so the current champion stays.

   How many folds each model wins, and whether two models' separate results overlap, do not decide anything.
4. *Your champion.* Name one champion in a short statement, in your stakeholder's terms, that covers four points: what you recommend and for which decision; the evidence (the outcome, the mean gain, its interval and δ); the checks you made (secondary metrics, fit time, interpretability) and the runner-up; and what would change your mind.
5. *The test set, once.* Only now, open the test set for your champion alone, and report its test score next to its cross-validation results. The test score describes the champion; it never re-picks it.

## What to submit

One member uploads two files for the whole group. The **report**, `NN_complex_models.pdf`, has sections 0, 1a and 1b, explanations in paragraphs, charts embedded, and key code snippets. The **code** is your Python script or Jupyter notebook, which must run on your dataset.

## How it is graded

| Criterion | Points |
|------------------------------------------------------------|-----:|
| 0\. Prediction goal(s), with the problem type justified | 5 |
| 1a. Baseline: a justified model, feature selection in five-fold CV, a relevant metric, interpretation | 25 |
| 1b. Complex model, tuning and champion: a justified model; a documented grid with its five-fold CV results; the paired comparison against δ, read as one of the four outcomes; a champion explained in practical terms | 50 |
| 2\. Report quality: clear structure, labeled charts, concise code that runs without errors | 20 |

## Tips

- Justify every modeling choice, and tie each metric to your prediction goal.
- Show how you ran cross-validation: tables, box plots or fold summaries.
- List the hyperparameters you tried and how you chose among them.
- A small or unresolved gain is an honest result. Say what it means, keep the simpler model, and propose next steps.
- Notebook 09 covers grid search; notebooks 11 to 14 cover trees, forests, boosting and choosing a champion.

*The Final Project Overview PDF has every date, the meeting rounds, and how the project is graded.*
