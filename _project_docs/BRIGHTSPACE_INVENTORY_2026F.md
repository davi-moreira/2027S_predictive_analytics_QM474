# Brightspace Inventory of Record — Fall 2026 (QM 47400)

**Brightspace is the source of record for what students actually see.** This page is the tracked
reconciliation of the live Brightspace course against the repo. When the two disagree, decide
deliberately: either Brightspace is right and the repo artifact is fixed, or the repo is right and
Brightspace is edited. Never let them drift silently.

**Source:** the Assignments and Manage Quizzes pages exported from
`Fall 2026 QM 47400 Davi Moreira - Merge` on **2026-08-18**. The PDFs and their text extracts are
filed in `_adm/_brightspace/2026F/` (gitignored).

**Live totals: 62 items** — 43 assignments and 19 quizzes.

| Category | Count |
|---|---:|
| Participation (assignments) | 21 |
| Quizzes (16 content + 3 participation-type) | 19 |
| Final Project | 16 |
| Extra Credit | 4 |
| Course Case Competition | 1 |
| Peer Evaluation | 1 |

**Status legend:** ✅ repo artifact exists and agrees · ⚠️ exists but conflicts or needs confirmation ·
❌ nothing in the repo · ➖ no repo artifact expected

---

## 1. Participation — notebook exercises (18)

Every one of these is the "Pause and Do Exercises" submission for its notebook. All 18 notebooks
exist and are current, so the deliverable side is covered; what is **not** yet confirmed is whether
the Brightspace instructions on each page match the notebook's own submission section.

| # | Brightspace item | Due | Repo artifact | Status |
|---|---|---|---|---|
| 1 | Participation: NB00 "Pause and Do Exercises" | Aug 24 | `notebooks/nb00_launchpad_course_setup_student.ipynb` | ✅ |
| 2 | Participation: NB01 | Aug 26 | `nb01_eda_splits_student.ipynb` | ✅ |
| 3 | Participation: NB02 | Aug 28 | `nb02_preprocessing_pipelines_student.ipynb` | ✅ |
| 4 | Participation: NB03 | Aug 31 | `nb03_regression_metrics_baselines_student.ipynb` | ✅ |
| 5 | Participation: NB04 | Sep 2 | `nb04_linear_features_diagnostics_student.ipynb` | ✅ |
| 6 | Participation: NB05 | Sep 9 | `nb05_regularization_project_proposal_student.ipynb` | ✅ |
| 7 | Participation: NB06 | Sep 14 | `nb06_logistic_pipelines_student.ipynb` | ✅ |
| 8 | Participation: NB07 | Sep 16 | `nb07_classification_metrics_thresholding_student.ipynb` | ✅ |
| 9 | Participation: NB08 | Sep 21 | `nb08_cross_validation_model_comparison_student.ipynb` | ✅ |
| 10 | Participation: NB09 | Sep 23 | `nb09_tuning_feature_engineering_project_baseline_student.ipynb` | ✅ |
| 11 | Participation: NB11 | Sep 28 | `nb11_decision_trees_student.ipynb` | ✅ |
| 12 | Participation: NB12 | Sep 30 | `nb12_random_forests_importance_student.ipynb` | ✅ |
| 13 | Participation: NB13 | Oct 5 | `nb13_gradient_boosting_student.ipynb` | ✅ |
| 14 | Participation: NB14 | Oct 7 | `nb14_model_selection_protocol_student.ipynb` | ✅ |
| 15 | Participation: NB16 | Oct 14 | `nb16_time_series_forecasting_student.ipynb` | ✅ |
| 16 | Participation: NB17 | Oct 26 | `nb17_data_communication_poster_student.ipynb` | ✅ |
| 17 | Participation: NB18 | Oct 19 | `nb18_competition_workflow_student.ipynb` | ✅ |
| 18 | Participation: NB19 | Oct 21 | `nb19_deep_learning_student.ipynb` | ✅ |

**Confirms the retirement decision:** there is no participation item for NB10, NB15, or NB20.
Brightspace and the repo agree that those three notebooks are out.

**Due-date cross-check:** every participation due date matches the session that teaches the notebook
in `schedule.qmd`. NB18 (Oct 19) precedes NB17 (Oct 26), which is the intended out-of-arc order.

## 2. Participation — surveys and feedback (3)

| # | Brightspace item | Due | Repo artifact | Status |
|---|---|---|---|---|
| 19 | Participation: Students Profile Survey | Aug 30 | none | ❌ |
| 20 | Participation: Midterm Feedback | Sep 30 | none | ❌ |
| 21 | Participation: Reflection Survey | Dec 11 | only in retired `nb20` | ❌ |

None of the three has published content in the repo. The Reflection Survey is referenced only inside
`nb20_final_submission_peer_review_student.ipynb`, which was retired from delivery, so that reference
is not reachable by students.

---

## 3. Quizzes — content banks (16)

| # | Brightspace quiz | Due | Repo bank | Status |
|---|---|---|---|---|
| 22 | Quiz NB01: Predictive Analytics Fundamentals, EDA, and Data Splitting | Aug 27 | `_quizzes/2026Summer/quiz_blueprint_nb01.md` + CSVs | ⚠️ |
| 23 | Quiz NB02: Data Preprocessing Pipelines | Aug 30 | `quiz_blueprint_nb02.md` + CSVs | ⚠️ |
| 24 | Quiz NB03: Regression Metrics and Baseline Models | Sep 1 | `quiz_blueprint_nb03.md` + CSVs | ⚠️ |
| 25 | Quiz NB04: Feature Engineering and Model Diagnostics | Sep 8 | `quiz_blueprint_nb04.md` + CSVs | ⚠️ |
| 26 | Quiz NB05: Regularization (Ridge & Lasso) | Sep 13 | `quiz_blueprint_nb05.md` + CSVs | ⚠️ |
| 27 | Quiz NB06: Logistic Regression | Sep 15 | `quiz_blueprint_nb06.md` + CSVs | ⚠️ |
| 28 | Quiz NB07: Classification Metrics | Sep 20 | `quiz_blueprint_nb07.md` + CSVs | ⚠️ |
| 29 | Quiz NB08: Resampling and Cross-Validation | Sep 22 | `quiz_blueprint_nb08.md` + CSVs | ⚠️ |
| 30 | Quiz NB09: Hyperparameter Tuning, Feature Engineering, and Leakage Detection | Sep 27 | `quiz_blueprint_nb09.md` + CSVs | ⚠️ |
| 31 | Quiz NB11: Decision Trees | Sep 29 | `quiz_blueprint_nb11.md` + CSVs | ⚠️ |
| 32 | Quiz NB12: Random Forests | Oct 4 | `quiz_blueprint_nb12.md` + CSVs | ⚠️ |
| 33 | Quiz NB13: Gradient Boosting | Oct 6 | `quiz_blueprint_nb13.md` + CSVs | ⚠️ |
| 34 | Quiz NB14: Model Selection Protocol | Oct 13 | `quiz_blueprint_nb14.md` + CSVs | ⚠️ |
| 35 | Quiz NB16: Time-Series Forecasting | Oct 18 | `quiz_blueprint_nb16.md` + CSVs | ⚠️ |
| 36 | Quiz NB17: Data Communication and Poster Design | Nov 1 | `quiz_blueprint_nb17.md` + CSVs | ⚠️ |
| 37 | Quiz NB19: Deep Learning | Oct 25 | `quiz_blueprint_nb19.md` + CSVs | ⚠️ |

**The set matches exactly.** Sixteen quizzes in Brightspace, sixteen blueprints in the repo, same
notebooks, and no quiz for NB00 or NB18 on either side (which `instructor.qmd` already documents).

**Why all sixteen are ⚠️ rather than ✅:** the banks live in **`_quizzes/2026Summer/`**. There is no
`_quizzes/2026F/` directory. So the repo cannot currently answer "which version of which bank is the
one loaded into the Fall course". Every bank was rewritten in August 2026 for the CV doctrine, and
the CSVs are versioned (`quiz_nb01_v1.csv` … `v4.csv`), which makes the ambiguity consequential: a
Fall course serving a pre-doctrine version would be teaching a retired rule.

**Open question for Davi:** were the Fall quizzes imported from the Summer banks, and if so, which
version file? Answering it determines whether we create `_quizzes/2026F/` as a copy of record or
simply document that Fall reuses Summer.

## 4. Quizzes — participation-type (3)

Built as Brightspace quizzes but graded as participation.

| # | Brightspace quiz | Due | Repo artifact | Status |
|---|---|---|---|---|
| 38 | Participation: Syllabus Quiz | Aug 30 | none | ❌ |
| 39 | Participation: Final Project and Course Competition [Group Check-in] | Aug 28 | none | ❌ |
| 40 | Participation: Course Competition Team Setup | Sep 20 | none | ❌ |

The Syllabus Quiz is the one nb00 used to point at; that pointer was removed on 2026-08-18 at
Davi's request. Item 39 is the deadline the "find your group in Brightspace" announcement supports.

---

## 5. Final Project (16)

| # | Brightspace item | Due | Repo artifact | Status |
|---|---|---|---|---|
| 41 | M00 - Instructor and TA Meetings - Round 01 Schedule | Sep 20 | `milestone_00_group_contact_confirmation.md` | ⚠️ **conflict** |
| 42 | M01 - Initial Project Proposal | Sep 20 | `milestone_01_initial_proposal.md` | ✅ |
| 43 | M02 - Expanded Project Outline | Sep 27 | `milestone_02_expanded_outline.md` | ✅ |
| 44 | M03 - Project Draft Abstract | Oct 4 | `milestone_03_draft_abstract.md` | ✅ |
| 45 | M04 - Instructor and TAs Meetings - Round 01 Confirmation | Oct 11 | none | ❌ **conflict** |
| 46 | M05 - Applying to the Conference | Oct 11 | `milestone_05_conference_application.md` | ✅ |
| 47 | M06 - Simple Model and Performance Evaluation | Oct 18 | `milestone_06_simple_model.md` | ✅ |
| 48 | M07 - Instructor and TAs Meetings - Round 02 Schedule | Oct 18 | none | ❌ **conflict** |
| 49 | M08 - More Complex Models and Performance Evaluation | Oct 25 | `milestone_08_complex_models.md` | ✅ |
| 50 | M09 - Poster First Draft | Nov 1 | `milestone_09_poster_first_draft.md` | ✅ |
| 51 | M10 - Final Poster Submission | Nov 10 | `milestone_10_final_poster.md` | ✅ |
| 52 | M11 - Poster Presentation Planning | Nov 15 | `milestone_11_presentation_planning.md` | ✅ |
| 53 | M12 - Post Invitation for Poster Presentation | Nov 15 | `milestone_12_linkedin_invitation.md` | ⚠️ title wording |
| 54 | M13 - Instructor and TAs Meetings - Round 02 Confirmation | Nov 15 | none | ❌ **conflict** |
| 55 | Final Project: Peer Review Submission | Nov 15 | none | ❌ |
| 56 | Final Project: Conference Poster Presentation | Nov 17 | reference doc only, no instruction file | ⚠️ |

### The four conflicts, stated plainly

**C1 — M00 is a different deliverable in each place.** The repo defines M00 as *Group Contact
Confirmation*, due **Sun Sep 6**. Brightspace defines M00 as *Instructor and TA Meetings - Round 01
Schedule*, due **Sep 20**. Different task, different date, two weeks apart. One of them is wrong, and
students will follow Brightspace.

**C2 — M04, M07, and M13 exist and are graded.** `final_project_milestone_reference.md` carries an
explicit instruction that these three are *"not used this term"* and *"Do not renumber"*. Brightspace
has all three built, dated, and pointed at 26 groups. They are the instructor/TA meeting
schedule-and-confirm cycle. The reference doc is the stale artifact here, and it is the file that
tells every other document what to believe.

**C3 — A Peer Review Submission exists that the reference doc's grade breakdown cannot account for.**
`final_project_milestone_reference.md` splits the project grade **40 / 20 / 40** (Milestone
Deliverables / Peer Evaluation / Instructor-TA). That split has no line for peer review. The syllabus
of record and the published website use **30 / 20 / 10 / 20 / 20** (Milestones / Peer Evaluation /
**Peer Review** / URC Presentation / Instructor-TA). Brightspace having a live *Peer Review
Submission* assignment is independent evidence that the 30/20/10/20/20 version is the operative one,
which makes the reference doc's breakdown wrong. This is the same contradiction logged as
discrepancy #2 in `SYLLABUS_OF_RECORD_2026F.md`; Brightspace now breaks the tie.

**C4 — M12's title.** Repo says *LinkedIn Post Invitation*; Brightspace says *Post Invitation for
Poster Presentation*. Almost certainly the same deliverable, but the repo filename encodes a channel
that the Brightspace title does not. Worth confirming before the milestone content is published.

---

## 6. Course Case Competition (1)

| # | Brightspace item | Due | Repo artifact | Status |
|---|---|---|---|---|
| 57 | Course Case Competition: Rank Code Submission | Nov 29 | `_course_case_competition/2026F/course_case_competition_instructions.md` | ⚠️ |

Instructions and reference material exist and the Fall data is staged. Not yet confirmed: whether
the instructions describe *this* Brightspace submission (rank + code) as the deliverable, or only the
Kaggle leaderboard submission. The Nov 29 date matches the syllabus of record.

## 7. Peer Evaluation (1)

| # | Brightspace item | Due | Repo artifact | Status |
|---|---|---|---|---|
| 58 | Peer Evaluation Submission: Final Project and/or Course Case Competition | Dec 11 | described in `syllabus.qmd` and milestone docs, no instrument | ❌ |

Peer evaluation is 20% of the Final Project, 20% of the Competition, and 20% of Poster-to-Product.
A single Brightspace assignment covers the first two. No rating instrument or rubric exists in the
repo, and none covers Poster-to-Product.

## 8. Extra Credit (4)

| # | Brightspace item | Due | Repo artifact | Status |
|---|---|---|---|---|
| 59 | Extra Credit: Mid-term Course Evaluation - Individual Credit | Oct 2 | `SYLLABUS_OF_RECORD_2026F.md` description only | ❌ |
| 60 | Extra Credit: DataCamp | Dec 4 | `SYLLABUS_OF_RECORD_2026F.md` description only | ❌ |
| 61 | Extra Credit: Issues in Course Materials | Dec 4 | `SYLLABUS_OF_RECORD_2026F.md` description only | ❌ |
| 62 | Extra Credit: Final Course Evaluation - Individual Credit | Dec 11 | `SYLLABUS_OF_RECORD_2026F.md` description only | ❌ |

All four are real, dated, and worth real points (DataCamp alone is up to **5% of the overall course
grade**), and none is mentioned anywhere students can see: not in `syllabus.qmd`, not in any
notebook, not on the website. The syllabus of record notes the extra-credit section exists "only in
the docx".

---

## Not in Brightspace, by design

- **Midterm Exam (Fri Sep 25, 20%)** — administered on paper in class, so it has no Brightspace
  assignment or quiz. `_midterm_exam/2026F/` holds the banks, LaTeX, and PDFs. A CSV per case exists
  for a makeup or practice import if one is ever needed.
- **Poster-to-Product (5%)** — the sprint runs Nov 20 through Dec 9 with a showcase, and carries no
  Brightspace item in this export. Its 20% peer-evaluation component has no visible instrument.
  Worth confirming this is intentional rather than not-yet-built.
- **Attendance (1%)** — no assignment; presumably tracked outside these two tools.

---

**Last updated:** 2026-08-18 from the Brightspace export of the same date.
**Maintained by:** Professor Davi Moreira + AI Assistants
