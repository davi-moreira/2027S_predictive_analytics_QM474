# Milestone 06 — Simple Model & Performance Evaluation

## About the Final Project

The Final Project is a **group capstone** (groups of four, randomly assigned) culminating in a **research poster** and a post-conference **Poster-to-Product** build sprint. Across the term your group completes milestones **M00 through M13** (no gaps in the numbering); each member also submits a confidential intra-group peer evaluation at the end. The project is worth **35%** of the course grade — Milestone Deliverables 30%, Peer Evaluation 20%, Peer Review 10%, Poster Presentation at the conference 20%, Instructor/TA Evaluation 20%. The post-conference **Poster-to-Product** sprint is graded separately as its own **5%** of the course grade. **Presentation at the Purdue Undergraduate Research Conference is required for all students**; the final poster is due one week before the conference.

---

## What to Submit on Brightspace

| # | File | Description |
|---|------|-------------|
| 1 | **`NN_simple_model.pdf`** | Structured report with clearly labeled sections (0–5 below), embedded visualizations, and key code snippets. |
| 2 | **Code file** | Your Python script or Jupyter Notebook, runnable on the provided dataset. |

---

## Instructions

### 0. Prediction Goal(s)
Clearly state your prediction goal(s).

### 1. Dataset Exploration
1. **Dataset Overview** — dataset size (observations, features); brief description of each feature (type, range); identify the response variable (continuous or categorical).
2. **Descriptive Statistics & Visualizations** — summary statistics for the response; ≥1 relevant visualization (histogram, bar plot, etc.); discuss notable findings (skewness, outliers).
3. **Predictor & Response Variables** — classify each predictor's type; discuss expected relationships to the response (domain knowledge, preliminary correlation).

### 2. Feature Engineering
1. **Create ≥1 new feature** with potential to improve performance or interpretability (combine features, temporal features, interaction terms).
2. **Justification** — clear rationale tied to domain knowledge or data-driven insights.

### 3. Handling Missing Values
Identify which features have missing values and the extent; present and justify a clear strategy (dropping vs. imputing).

### 4. Baseline Model Implementation
1. **Model Choice** — the simplest reasonable model: linear regression (continuous response) or logistic regression (categorical response).
2. **Implementation** — combine a **feature-selection procedure** with **k-fold (k=5 or 10) cross-validation**; use the CV error to select the best model.
3. **Interpretation & Next Steps** — summarize performance; reflect on whether further engineering, feature selection, or tuning is needed.

## Submission Format

- **Structured Report (PDF):** labeled sections; explanations/findings/rationale in paragraph form; visualizations embedded; key code snippets in the appendix or relevant sections.
- **Code Files:** Python script or Jupyter Notebook, submitted separately.

## Rubric (Total: 100 points)

| Criterion | Pts | Exemplary | Competent | Needs Improvement |
|-----------|----:|-----------|-----------|-------------------|
| **0. Prediction Goal(s)** | 5 | Clear, specific goal(s); explains why they matter; understands regression vs. classification. | Stated but lacking clarity/detail; limited context. | Not stated or indistinguishable from general exploration; no rationale. |
| **1. Dataset Exploration** | 20 | Comprehensive overview (size, feature types, response) + meaningful stats and appropriate visualizations with insightful discussion. | Basic overview; response identified; some stats + ≥1 visualization; discussion lacks detail. | Little/no mention of size or features; response unclear; stats/visuals missing or irrelevant. |
| **2. Feature Engineering** | 15 | ≥1 new feature with convincing justification and clear expected impact; well-explained method. | New feature created but rationale minimal; impact mentioned but not explored. | No new (or trivial) feature; no explanation; superficial or missing. |
| **3. Handling Missing Values** | 10 | Thorough identification; clear, well-justified strategy; compares ≥1 alternative. | Some identification; method applied with basic rationale; little comparison. | Fails to identify/address; inappropriate or unjustified method. |
| **4a. Model Choice** | 5 | Clearly identifies the simplest reasonable model, well justified for the response type. | Generally appropriate but weak justification. | Inappropriate or not stated. |
| **4b. Implementation (feature selection + k-fold CV)** | 15 | Systematic feature selection inside k-fold CV; correct CV to compare/select; tracks CV metrics carefully. | Some feature selection; CV used but rationale incomplete. | No feature selection/CV evidence; CV incorrect or unexplained. |
| **4c. Interpretation & Next Steps** | 10 | Summarizes results; insightful reflection; realistic next steps. | Basic results; minimal interpretation; vague next steps. | No interpretation; no next steps. |
| **5. Report Quality & Clarity** | 20 | Well-structured PDF matching sections; labeled visuals/code; logical flow; code runs error-free. | Generally understandable; minor organization/labeling issues; code needs minor fixes. | Disorganized; missing labels/code; numerous errors; code fails to run. |

---

**Course alignment (CV-first).** All performance claims must come from **k-fold cross-validation** on the training data — do **not** touch a held-out test set for model selection (course rule, nb08). Lean on **nb02** (pipelines), **nb03/nb07** (metrics), **nb08–nb09** (CV + feature selection inside the pipeline) so feature selection happens *inside* each CV fold (no leakage).

---

Please feel free to let me know if you have any questions.

All the best,

Prof. Moreira
