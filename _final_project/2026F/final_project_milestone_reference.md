# Final Project — Milestone Reference (Fall 2026, QM47400)

**Single source of truth for the Fall 2026 Final Project milestone numbering, due dates, and grading.** Every other document (`syllabus.qmd`, `schedule.qmd`, the planning docs, the individual milestone instruction files in this folder, and the project-related notebooks) must be kept consistent with this file. Update it first whenever the project structure changes.

> **Precedence.** This file is reconciled against the **live Brightspace course**, which is what students actually see and submit against. Where this file and Brightspace disagree, Brightspace wins and this file is corrected. Last reconciled **2026-08-20** against the Brightspace export of 2026-08-18 (see [`../../_project_docs/BRIGHTSPACE_INVENTORY_2026F.md`](../../_project_docs/BRIGHTSPACE_INVENTORY_2026F.md)).

> **⚠ Pending Brightspace change (2026-08-22).** The **M10 final poster deadline moved from Tue Nov 10 to Sun Nov 8, 11:59 PM** — instructor decision, to protect the print window and to share a single print run with HONR 46400, whose poster locks the same night. This file, the milestone files, the README, the plan docs, and the docx generators are updated. **Brightspace is NOT yet updated**: the M10 due date and its availability window (now Nov 2 – Nov 8) must be changed by hand, and the M11/M12 windows re-open Nov 8. Until that is done, Brightspace and this file disagree and the precedence rule above does *not* apply — this change is the instructor's, not Brightspace's.

### Templates and rubrics (this folder)

| File | Used by |
|---|---|
| [`template/qm474_poster_template.pptx`](template/qm474_poster_template.pptx) | M09 poster first draft, M10 final poster |
| [`rubric/Predictive_Analytics_Poster_Rubric.pdf`](rubric/Predictive_Analytics_Poster_Rubric.pdf) (also `.docx`, `.xlsx`) | M09, M10, and the Instructor/TA evaluation |
| [`template/QM474_group_contract.docx`](template/QM474_group_contract.docx) | M00 group contract; rebuilt by `scripts/build_group_contract_docx.py` |

The poster template and rubric came from the 2026Summer offering (template renamed from `mgmt474_poster_template.pptx` to `qm474_poster_template.pptx` for the current course code) and were revised on 2026-10-26. **Template:** six typos fixed and an **AI USE DISCLOSURE** section added under Acknowledgements. **Rubric:** Data Preparation 20 → 18, Baseline 20 → 17, criterion 6 rewritten to the paired per-fold comparison against a predeclared margin (`_project_docs/CV_INFERENCE_DOCTRINE.md`; feedback only at M09, scored from M10), a new criterion 8 *Sources, Acknowledgments, AI Use & Data Privacy* (5 pts; no AI disclosure caps it at 2, personally identifiable data scores 0), and a note that an honors section is not scored under this rubric (Decision 15). Total stays 100. The `.docx`/`.xlsx` were rebuilt in place and the `.pdf` exported from the `.docx`. **Second revision, same day (Amendment 1 + champion selection):** criterion 6 is now *Model Comparison and Champion Selection* — margin δ with its business meaning and a simplest-first candidate order stated before comparing, the fold-corrected paired interval read as one of four outcomes, and one champion with a rationale in the stakeholder's terms (the baseline can win; an honest "unresolved" can earn full credit). Criterion 5 asks for fold scores with their mean and SD instead of a per-model confidence interval; criteria 1 and 7 name the stakeholder's decision and make the champion easy to find. The M09 note keeps criterion 6 feedback-only on the first draft, and the Fall 2026 note protects work done as nb08/nb14 teach and accepts disclosed after-the-fact margins. M09/M10 instructions updated to match; points unchanged; the PDF stays at two pages. **Third revision, 2026-10-27 (grading consistency):** the Fall 2026 note now *controls* criterion 6 — the corrected interval is recommended, not required; the Exemplary level accepts notebook 08's rule applied correctly; the Competent deductions apply only to the rule the team used (a margin set after the results costs points only when undisclosed). M09/M10 say the same and ask for a short champion statement covering four points instead of exactly four sentences. Points unchanged; two pages. **Fourth revision, 2026-10-27 (follow the published notebooks until Nov 8):** Davi decided the rubric and template must reflect the course content as published, and that both move to the new notebook versions after Nov 8. Criterion 6 now scores notebook 08's three-outcome rule (real difference / no winner / practically equivalent, simpler model wins) against a practical margin, and the champion as notebook 14 teaches; the corrected interval, the four outcomes and δ are gone from the rubric. Criterion 5 again asks for the CV mean with its SD and approximate 95% interval, labeled descriptive. The Fall 2026 note is replaced by "Criterion 6 follows the notebooks" (late margins disclosed are not penalized; a baseline champion or an honest no-winner verdict can earn full credit). Template: Methodology, Models Performance and Business Implications prompts now follow nb02/nb08/nb14/nb17, and the Acknowledgements box became *Acknowledgements & References* with a references placeholder (nb17 section 11). Points unchanged; two pages. The M09/M10 instruction text was brought into line the same day: §1c–§1e and the course-alignment paragraph of M09, and the Model comparison and Champion paragraphs of M10, now describe the same nb08/nb14 rule as the rubric, and both Fall 2026 transition notes are gone (their disclosure and full-credit protections moved into the course-alignment and Champion paragraphs).

### Individual milestone files (this folder)

[`milestone_00_meetings_schedule_and_group_contract.md`](milestone_00_meetings_schedule_and_group_contract.md) · [`milestone_01_initial_proposal.md`](milestone_01_initial_proposal.md) · [`milestone_02_expanded_outline.md`](milestone_02_expanded_outline.md) · [`milestone_03_draft_abstract.md`](milestone_03_draft_abstract.md) · [`milestone_04_meetings_round01_confirmation.md`](milestone_04_meetings_round01_confirmation.md) · [`milestone_05_conference_application.md`](milestone_05_conference_application.md) · [`milestone_06_simple_model.md`](milestone_06_simple_model.md) · [`milestone_07_meetings_round02_schedule.md`](milestone_07_meetings_round02_schedule.md) · [`milestone_08_complex_models.md`](milestone_08_complex_models.md) · [`milestone_09_poster_first_draft.md`](milestone_09_poster_first_draft.md) · [`milestone_10_final_poster.md`](milestone_10_final_poster.md) · [`milestone_11_presentation_planning.md`](milestone_11_presentation_planning.md) · [`milestone_12_post_invitation.md`](milestone_12_post_invitation.md) · [`milestone_13_meetings_round02_confirmation.md`](milestone_13_meetings_round02_confirmation.md) · [`final_project_peer_review_submission.md`](final_project_peer_review_submission.md) · [`final_project_conference_presentation.md`](final_project_conference_presentation.md) · [`peer_evaluation_instrument.md`](peer_evaluation_instrument.md)

> **Milestone numbering.** The track runs **M00 through M13 with no gaps**. Every number is used. (An earlier version of this file stated that M04, M07, and M13 were unused this term; that was wrong. All three are live in Brightspace and carry the instructor/TA meeting schedule-and-confirm cycle.)

> **Notebook vs. milestone numbering.** The course notebooks refer to a simplified "M1–M4" project track (e.g., nb05 proposal, nb09 baseline). Those are *skill* checkpoints inside the notebooks; the **official deliverables and deadlines are the M00–M13 milestones in this document**. Where a notebook says "M3," map it to the official milestone by topic (complex model → **M08**; draft abstract → **M03**).

---

## The Final Project at a glance

In the same group, students complete a practical predictive analytics project culminating in a final research poster. **Presentation of the poster at the Fall 2026 Purdue Undergraduate Research Conference on Tuesday, November 17, 2026, is required for all students**, and the final poster is due nine days before the conference, on **Sunday, November 8, 2026**. Professor Moreira serves as faculty mentor throughout the process.

The Final Project is worth **35% of the course grade**, assessed as follows.

| # | Component | Share of project | Share of course | What it covers |
|---|---|---:|---:|---|
| 1 | **Milestone Deliverables** | 30% | 10.5% | Incremental project components submitted on specific due dates. These allow for early feedback and ensure steady progress throughout the semester. Grades reflect each milestone's clarity, completeness, and timely submission. |
| 2 | **Peer Evaluation** | 20% | 7.0% | Students evaluate their peers' contributions, encouraging accountability and productive teamwork. These assessments help ensure balanced participation and measure collaborative effectiveness. |
| 3 | **Peer Review** | 10% | 3.5% | Each group reviews and provides constructive feedback on other teams' posters. This encourages engagement, enhances critical analysis skills, and promotes a culture of constructive critique. |
| 4 | **Poster Presentation at the Conference** | 20% | 7.0% | A poster template and assessment rubric are shared. Final posters are submitted by the syllabus due date, after which they are printed and distributed during a dedicated Poster Presentation Preparation class. |
| 5 | **Instructor / TA Evaluation** | 20% | 7.0% | After the Undergraduate Research Conference, the instructor and the TA evaluate the final submission against a rubric that is shared in advance. |
| | **Total** | **100%** | **35.0%** | |

Students are encouraged to review previous award-winning student posters for inspiration: <https://davi-moreira.github.io/applied_projects.html>. Additional details on the conference: <https://www.purdue.edu/undergrad-research/conferences/index.php>.

As the conference may not coincide with the regular class time, students should communicate with their other instructors in advance regarding potential scheduling conflicts. **The usual class immediately following the Poster Presentation is not held**, allowing time to rest and catch up on other coursework.

**Poster-to-Product** is a separate **5%** of the course grade: the post-conference, two-week in-class build sprint that converts the validated model into a stakeholder-ready dashboard or app plus an executive brief, with the showcase on Wed Dec 9. Graded 80% on deliverables and showcase (NACE competencies: Technology, Teamwork, Communication, Critical Thinking) and 20% on intra-group peer evaluation.

---

## Milestone schedule

Dates and availability windows are taken from Brightspace. Deliverables are due at **11:59 PM**.

| # | Milestone | Due | Brightspace window | Grading |
|---|---|---|---|---|
| **M00** | Instructor and TA Meetings (Round 01 Schedule) + Group Contract | **Sun Sep 20** | Sep 14 – Sep 20 | completion |
| **M01** | Initial Project Proposal | **Sun Sep 20** | Sep 9 – Sep 20 | 50 |
| **M02** | Expanded Project Outline | **Sun Sep 27** | Sep 21 – Sep 27 | 50 |
| **M03** | Project Draft Abstract | **Sun Oct 4** | Sep 28 – Oct 4 | 30 |
| **M04** | Instructor and TAs Meetings (Round 01 Confirmation) | **Sun Oct 11** | Oct 1 – Oct 11 | completion |
| **M05** | Applying to the Conference | **Sun Oct 11** | Oct 1 – Oct 11 | completion |
| **M06** | Simple Model and Performance Evaluation | **Sun Oct 18** | Oct 1 – Oct 18 | 100 |
| **M07** | Instructor and TAs Meetings (Round 02 Schedule) | **Sun Oct 18** | Oct 1 – Oct 18 | completion |
| **M08** | More Complex Models and Performance Evaluation | **Sun Oct 25** | Oct 1 – Oct 25 | 100 |
| **M09** | Poster First Draft | **Sun Nov 1** | Oct 26 – Nov 1 | rubric |
| **M10** | Final Poster Submission (`NN.pdf`) | **Sun Nov 8** | Nov 2 – Nov 8 | poster rubric |
| **M11** | Poster Presentation Planning | **Sun Nov 15** | Nov 8 – Nov 15 | rubric |
| **M12** | Post Invitation for Poster Presentation | **Sun Nov 15** | Nov 8 – Nov 15 | completion |
| **M13** | Instructor and TAs Meetings (Round 02 Confirmation) | **Sun Nov 15** | Nov 8 – Nov 15 | completion |
| — | **Peer Review Submission** | **Sun Nov 15** | Nov 8 – Nov 15 | 10% of project |
| — | **Conference Poster Presentation** (required) | **Tue Nov 17** | Nov 17 | 20% of project |
| — | **Peer Evaluation Submission** | **Fri Dec 11** | Dec 7 – Dec 11 | 20% of project |

The Peer Evaluation Submission is filed under its own Brightspace category (it also covers the Course Case Competition), which is why it sits outside the Final Project block above.

### The meeting cycle

Four of the sixteen items are the instructor/TA meeting cycle, which runs in two rounds. Each round is **scheduled** in one milestone and **confirmed** in a later one:

| Round | Schedule the meetings | Meeting windows | Confirm they happened |
|---|---|---|---|
| **Round 01** | **M00** (due Sep 20) | TA: Sep 21 – Oct 4 · Instructor: Oct 5 – Oct 11 | **M04** (due Oct 11) |
| **Round 02** | **M07** (due Oct 18) | TA: Oct 19 – Nov 1 · Instructor: Nov 2 – Nov 7 | **M13** (due Nov 15) |

At least one member of the group must attend each meeting; it need not be the same member every time. Round 01 focuses on the prediction problem, the data, and the proposed modeling strategy. Round 02 focuses on the predictive models, the modeling strategy, and poster development.

> **Round 01 windows are inferred**, derived from the M00 submission deadline and the M04 confirmation deadline to mirror the structure Round 02 states explicitly. Confirm or correct them before publishing M00 and M04 to students.

---

## Per-milestone summary

Full instructions and rubrics: the individual `milestone_NN_*.md` files in this folder (source: `reference/Final Project Milestones .docx`).

### M00 — Instructor and TA Meetings (Round 01 Schedule) + Group Contract · due Sun Sep 20 · completion
Two jobs. **(1)** The group completes and signs the **Group Contract** (template: [`template/QM474_group_contract.docx`](template/QM474_group_contract.docx), rebuilt by `scripts/build_group_contract_docx.py`), covering members and contact information, communication norms, meeting cadence, roles, decision-making, work distribution, accountability, and signatures. **(2)** The group emails the TA and Professor Moreira proposing dates and times for the Round 01 meetings. Three PDFs submitted: contract, TA request, instructor request.

### M01 — Initial Project Proposal · due Sun Sep 20 · 50 pts
Define a **prediction goal** (not a research question): prediction goal, motivation and significance, eligible real-data overview with source link and provenance, preliminary methods, and expected contributions. Synthetic, simulated, artificially generated, and AI-generated datasets are not eligible. 1–2 pages. *(Course support: nb01–nb05.)*

### M02 — Expanded Project Outline · due Sun Sep 27 · 50 pts
Refine the goal and detail the plan: revised goal and objectives, data preparation (cleaning and feature engineering), methodology and evaluation metrics, initial EDA findings, anticipated challenges. 2–3 pages with visualizations. *(Course support: nb02, nb06–nb09.)*

### M03 — Project Draft Abstract · due Sun Oct 4 · 30 pts
A \~250-word draft abstract for the conference: informative title, prediction problem framed as a question (with a "?"), goal and motivation, identification of the eligible real dataset and its original provider, methodology and tools, key findings and expected contributions, and broader implications. Synthetic, simulated, artificially generated, and AI-generated datasets are not eligible for the Final Project.

### M04 — Instructor and TAs Meetings (Round 01 Confirmation) · due Sun Oct 11 · completion
Upload a PDF detailing the dates and times of the group's Round 01 meetings with the instructor and the TAs.

### M05 — Applying to the Conference · due Sun Oct 11 · completion
All groups apply to present a poster: title, abstract (no author names in the box), five keywords, all members as authors, in-person format, category **Business Case Study**, judging unit **Daniels School of Business**, mentor **Davi Cordeiro Moreira (dcordeir@purdue.edu)**. Upload a PDF proof of application. Apply: <https://www.purdue.edu/undergrad-research/conferences/fall/index.php>

### M06 — Simple Model and Performance Evaluation · due Sun Oct 18 · 100 pts
Structured report plus code: prediction goal(s); dataset exploration (overview, descriptive statistics and visualizations, predictor and response types); feature engineering (at least one new feature plus justification); missing-value strategy; **baseline model** (linear or logistic) with **feature selection inside k-fold CV (k=5 or 10)**; interpretation and next steps. *(CV-first; course support: nb03, nb06–nb09.)*

### M07 — Instructor and TAs Meetings (Round 02 Schedule) · due Sun Oct 18 · completion
Schedule two Round 02 meetings: one with the TA between **Oct 19 and Nov 1**, one with Professor Moreira between **Nov 2 and Nov 7**. Upload two PDFs of the scheduling emails; each must include proposed dates and times, specify the course section, and copy all group members.

### M08 — More Complex Models and Performance Evaluation · due Sun Oct 25 · 100 pts
Structured report plus code: prediction goal(s); baseline model (may replicate M06); a **more complex model** (e.g., Random Forest, SVM, Gradient Boosting) with **hyperparameter tuning via k-fold CV**; model selection and final comparison against the baseline with practical interpretation. *(Course support: nb11–nb14.)*

### M09 — Poster First Draft · due Sun Nov 1 · rubric
First full poster draft using the template, rubric, and the Data Communication lecture (nb17): title and authors, abstract and introduction, methods and data, results and analysis (baseline vs. advanced metrics), conclusions and future directions; logical flow, clean visual design, citations, **Acknowledgments** (Daniels School, Prof. Moreira, TAs), an **AI Use Disclosure** (syllabus AI Policy), data-privacy compliance. Single PDF named `NN.pdf`.

### M10 — Final Poster Submission · due Sun Nov 8 · poster rubric
Final poster incorporating first-draft feedback. One PDF named `NN.pdf` (e.g., `03.pdf`, `17.pdf`), no section number. Submitted **9 days before the conference**; the instructor prints it for free.

### M11 — Poster Presentation Planning · due Sun Nov 15 · rubric
A written plan (PDF): one-paragraph audience analysis; three elevator pitches (**30-second ≤75 words, 90-second ≤200 words, 2-minute ≤300 words**); poster-integration outline (where figures are referenced); and a question-and-discussion strategy (at least 3 audience-directed questions).

### M12 — Post Invitation for Poster Presentation · due Sun Nov 15 · completion
At least one member publishes a professional post inviting their network to the presentation: poster title, team members, date and time, location (exactly as in the official program). Upload a screenshot. Optionally tag the instructor: <https://www.linkedin.com/in/davimoreira/>.

### M13 — Instructor and TAs Meetings (Round 02 Confirmation) · due Sun Nov 15 · completion
Upload a PDF detailing the dates and times of the group's Round 02 meetings with the instructor and the TAs.

### Peer Review Submission · due Sun Nov 15 · 10% of the project
Each group reviews five assigned posters, completes one structured survey per poster, and uploads a single PDF of the submission screenshots. Full instructions and the review assignment matrix: [`final_project_peer_review_submission.md`](final_project_peer_review_submission.md).

### Conference Poster Presentation · Tue Nov 17 · 20% of the project
Required for all students. Upload a photo of yourself in front of your poster as proof of presentation.

### Peer Evaluation Submission · due Fri Dec 11 · 20% of the project
Confidential intra-group ratings, assessed **per member**. Instrument and logistics: [`peer_evaluation_instrument.md`](peer_evaluation_instrument.md).

---

**Maintained by:** Professor Davi Moreira + AI assistants · **Aligned to:** Fall 2026 full-semester format · **Last reconciled against Brightspace:** 2026-08-20.
