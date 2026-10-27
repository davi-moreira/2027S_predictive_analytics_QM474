# Milestone 08 — More Complex Models & Performance Evaluation

## About the Final Project

The Final Project is a **group capstone** (groups of four, randomly assigned) culminating in a **research poster** and a post-conference **Poster-to-Product** build sprint. Across the term your group completes milestones **M00 through M13** (no gaps in the numbering); each member also submits a confidential intra-group peer evaluation at the end. The project is worth **35%** of the course grade — Milestone Deliverables 30%, Peer Evaluation 20%, Peer Review 10%, Poster Presentation at the conference 20%, Instructor/TA Evaluation 20%. The post-conference **Poster-to-Product** sprint is graded separately as its own **5%** of the course grade. **Presentation at the Purdue Undergraduate Research Conference is required for all students**; the final poster is due one week before the conference.

---

## What to Submit on Brightspace

| # | File | Description |
|---|------|-------------|
| 1 | **`NN_complex_models.pdf`** | Structured report (sections 0, 1a, 1b) with embedded visualizations and key code snippets. |
| 2 | **Code file** | Python script or Jupyter Notebook, runnable on the provided dataset. |

---

## Instructions

### 0. Prediction Goal(s)
State your prediction goal(s); explain why they matter; confirm whether it is **regression** (continuous) or **classification** (categorical).

### 1a. Baseline Model *(you may replicate M06)*
1. **Model Choice** — simplest reasonable model (linear/logistic) with brief justification as a baseline.
2. **Implementation & Feature Selection** — feature-selection procedure + **k-fold CV (k=5 or 10)**; compare predictor subsets via the chosen metric (CV error, RMSE, MAE, accuracy, F1).
3. **Interpretation & Next Steps** — summarize baseline performance; reflect on improvements.

### 1b. More Complex Model Implementation & Tuning
1. **Model Choice** — a more complex model (e.g., Random Forest, SVM, Gradient Boosting); justify how it may capture patterns the baseline cannot (non-linearity, interactions).
2. **Hyperparameter Tuning with CV** — define a grid of hyperparameter values; use **k-fold CV** to evaluate combinations; report the metric(s) used.
3. **Model Selection & Final Comparison** — identify the best hyperparameters by CV; compare the tuned model against the baseline; discuss improvements and interpret in practical terms.

## Submission Format

- **Structured Report (PDF):** labeled sections (0, 1a, 1b); paragraph explanations; embedded visualizations; key code snippets.
- **Code Files:** Python script or Jupyter Notebook, submitted separately.

## Rubric (Total: 100 points)

| Criterion | Pts | Exemplary | Competent | Needs Improvement |
|-----------|----:|-----------|-----------|-------------------|
| **0. Prediction Goal(s)** | 5 | Clear goal(s) tied to context; specifies regression vs. classification with justification. | Stated but lacks clarity; some ambiguity on problem type. | No clear goal or problem type; no rationale. |
| **1a. Baseline Model** | 25 | Appropriate, well-justified baseline; systematic feature selection + k-fold CV with relevant metric; clear interpretation and next steps. | Baseline chosen with weak rationale; some feature selection; CV present but under-explained; basic interpretation. | Inappropriate/absent baseline; no feature selection/CV; metrics missing; no interpretation. |
| **1b. Complex Model + Tuning** | 50 | Appropriate complex model with clear rationale; well-documented hyperparameter grid + k-fold CV with results (tables/plots); identifies best config; compares to baseline with practical interpretation. | Complex model with unclear rationale; some tuning but grid/params under-documented; CV incomplete; minimal comparison. | Complex model misaligned/absent; tuning missing or superficial; CV wrong/absent; no comparison. |
| **2. Report Quality & Clarity** | 20 | Well-structured PDF matching steps; labeled, integrated visuals; succinct code; runs error-free. | Generally understandable; minor organization issues; some unlabeled figures; minor code setup needed. | Disorganized; missing labels/code; code fails; numerous errors. |

## Additional Reminders

- Always justify modeling decisions (baseline and complex) and state performance metrics clearly, tied to the goal.
- Document how you performed k-fold CV (k=5 or 10); present results (tables, boxplots, fold summaries).
- Summarize which hyperparameters you tested and how you chose the best combination (best mean CV score, balancing performance and complexity).
- Emphasize the practical significance of any gains; if minimal, propose reasons and next steps.

---

**Course alignment (CV-first).** Tuning and comparison run on **cross-validation over the training data only** — the test set stays locked (course rule, nb08/nb14). Use **nb09** (GridSearchCV/RandomizedSearchCV) and **nb11–nb14** (trees, forests, boosting, and model selection on paired per-fold differences against a predeclared margin). The tuned champion you select here feeds the poster (M09/M10) and the Poster-to-Product build.

---

Please feel free to let me know if you have any questions.

All the best,

Prof. Moreira
