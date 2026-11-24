# Course Design Decisions

This document records design decisions made during course development and the reasoning behind them. Decisions here are **load-bearing** — changing them requires deliberate review, not casual edits. New AI assistants and contributors should read this to understand WHY conventions exist before proposing changes.

---

## Decision 1: Flat Notebook Structure

**Decision:** All 21 notebooks live in `/notebooks/` (flat, not nested by week).

**Rationale:**
- Easier to link/reference (simple URLs).
- Clear sequential numbering (`nb00`–`nb20`).
- Students navigate linearly through days.
- GitHub displays flat lists better than nested directories.

*Updated 2026-08-14: the arc is now 20 notebooks — `nb00`–`nb09` and `nb11`–`nb20` — after `nb10` was moved to `_archive/2026F_retired/`; see Decision 12. The flat structure itself is unchanged.*

---

## Decision 2: 60/20/20 Split for All Examples

**Decision:** Always use 60% train, 20% validation, 20% test.

**Rationale:**
- Consistency across all 21 notebooks.
- Students learn ONE splitting pattern.
- Sufficient validation data for tuning.
- Realistic test set size for course-scale datasets.

*Updated 2026-08-14: the arc is now 18 notebooks — see Decision 12. The 60/20/20 split still applies to every one of them.*

*Updated 2026-11-24: superseded for nb09 onward by Decision 17. This decision now governs nb01–nb08 only (nb08 uses the 60/20/20 split only to motivate cross-validation and ends on the 80/20 + 5-fold pattern).*

---

## Decision 3: `RANDOM_SEED = 474` Everywhere

**Decision:** All random operations use seed 474 (the course number, QM47400).

**Rationale:**
- Complete reproducibility — students get identical outputs.
- Easier to debug — same results every time.
- Course-specific seed (not the generic `42`).
- Memorable for students.

---

## Decision 4: Google Colab + Gemini (Not Local Jupyter)

**Decision:** Primary platform is Google Colab; AI assistance is Google Gemini.

**Rationale:**
- Zero setup for students (no installation issues).
- Consistent environment (same Python/library versions across all students).
- Built-in GPU access (for the deep-learning day).
- Gemini AI assistance integrated natively.
- Accessible from any device.

**Implication for notebook design:** Code must run in a fresh Colab runtime. No hardcoded local paths. Imports must be standard scientific-Python or pip-installable on first cell.

---

## Decision 5: Exclude Admin Materials from Git

**Decision:** `_adm_stuff/` is in `.gitignore`. *(The directory was later renamed to `_adm/`, which is also gitignored; the decision stands, only the path changed.)* Instructor notebooks (`*_instructor*.ipynb`) and `video_guides/` are also gitignored.

**Rationale:**
- Student privacy (contact info, accommodations).
- Sensitive data (grades, evaluations).
- Large files (homework solutions, zip archives).
- Public repo — cannot include private materials.
- Instructor solutions must not leak to students browsing the repo.

---

## Decision 6: Micro-Videos (≤12 min each)

**Decision:** All videos capped at 12 minutes maximum.

**Rationale:**
- Attention-span research suggests 10–15 min is optimal for instructional video.
- Mobile-friendly (students can watch on phone).
- Easy to re-watch specific topics.
- Forces concise, focused content.
- ~6 videos per day = ~1 hour total video, leaving time for hands-on notebook work.

---

## Decision 7: "PAUSE-AND-DO" (Not "Exercise" or "Assignment")

**Decision:** Use "PAUSE-AND-DO" terminology for the 10-minute in-notebook practice blocks.

**Rationale:**
- Clear action signal — pause the video, do this now.
- Distinguishes from graded assignments (which are separate).
- Emphasizes active learning over passive reading.
- 10-minute scope — not homework, not a project.
- Builds an engagement habit across all 21 notebooks.

*Updated 2026-08-14: the arc is now 18 notebooks — see Decision 12. PAUSE-AND-DO still runs across all of them.*

---

## Decision 8: Instructor-First Notebook Editing Workflow

**Decision:** The instructor notebook (`nbNN_*_instructor.ipynb`) is the source of truth. The student notebook (`nbNN_*_student.ipynb`) is generated from it by copy-then-strip-`INSTRUCTOR SOLUTION`-cells.

**Rationale:**
- Single source of truth — solutions and student version cannot drift.
- Solutions live next to the prompts they answer (easier to maintain).
- Student notebook is generated, never hand-edited; this guarantees the student version is always derivable.
- Allows last-minute solution polish without re-writing the student version separately.

**Implication:** Every cell that should be excluded from the student version MUST contain the literal string `INSTRUCTOR SOLUTION`. The strip script keys on this marker. Unmarked solution cells leak into the student notebook.

---

## Decision 9: CV-First Evaluation, Test-Set Locked Until nb14

**Decision:** From `nb09` onward, all model-performance claims come from cross-validation. The test set (`X_test`, `y_test`) is locked — no model evaluation touches it until `nb14`'s "Opening the Locked Test Set" ceremony.

**Rationale:**
- The test-set-lock ceremony in nb14 is pedagogically central. If the test set is touched 30 times beforehand, the ceremony loses meaning.
- Cross-validation is the professionally honest evaluation method; the course teaches it as the spine.
- Students learn that "I peeked at the test set 30 times before reporting accuracy" is the most common subtle leak in industry.

**Exceptions:**
- `nb14` cells 30 and 34 only — the authorized test-set openings, **one per spine**: cell 30 is the classification business case, cell 34 the regression business case. Each test set still opens exactly ONCE; the singleness rule is preserved per case, not diluted across spines.
- `nb18` Kaggle-submission demo — uses `X_test` to simulate predicting on a held-out CSV (production-pipeline pattern, not model evaluation). *(Fall 2026 only: dropped on 2026-11-24 when nb18 became the temporal S&P 500 competition notebook, which has no `X_test` — Decision 18.)*

**Implication:** Before every commit in `nb09`–`nb20`, run `scripts/audit_cv_first.py`. The only acceptable hits are the nb14 exceptions (from Spring 2027; Fall 2026 also allowed nb18).

---

## Decision 10: Narrative Polish Pattern (nb08 Style)

**Decision:** Every student-notebook markdown cell follows the nb08 narrative style — named business stakeholder in "Why This Matters", flowing prose over bullet lists, inline `"A question that often comes up here"` Q&A blocks, explicit section bridges, warm wrap-ups bridging to the next notebook.

**Rationale:**
- Students read notebooks alone, often late at night. The voice must be encouraging and complete, not skeletal.
- Named stakeholders (HomeValue CFO, MedScreen chief medical officer) make business framing concrete instead of abstract.
- Inline Q&A pre-empts the most common confusions, reducing "I'm stuck and don't know what to ask" moments.
- The `"A question that often comes up here"` phrase is grep-findable for tooling and audits.

**Implication:** New markdown cells longer than ~150 words should be checked against the polish pattern before commit. See `claude.md` for the polish helper script and the audit checklist.

---

## Decision 11: MC Option-Length Parity in All Assessments

**Decision:** In every multiple-choice question (quizzes, midterm, any future exam), all options must sit in the same length-and-elaboration band: every option ≥ 60% of the question's longest option, and per bank the correct option is strictly longest in ≤ 40% of questions (target ~25%, chance). Distractors carry their own flawed-but-specific rationale at the correct option's elaboration and connector-word density.

**Rationale:**
- In 2026Summer, correct options were authored as full decisions-with-rationale while distractors stayed terse. Two students independently reported (extra-credit program, 2026-06-12) that "always pick the longest option" scored ~100%. Hypothesis tests confirmed it: correct-is-longest in 96% of quiz questions (250 analyzed) and 99.5% of midterm questions (210 analyzed) vs. 25% chance, p < 10⁻¹²³; the midterm's connector-word density showed the same cue.
- Length-balanced, equally-elaborated distractors restore the assessments' validity: the only way to eliminate an option is to recognize the misconception it encodes.

**Exceptions:** none. Numeric/label options satisfy the band by formatting all options in the same shape (e.g., `k = 2` / `k = 100`).

**Implication:** Before importing any quiz/exam CSV to Brightspace, run `python scripts/audit_answer_length.py --file <csv>` — PASS is mandatory. Authoring spec: `scripts/_distractor_rewrite_instructions.md`; per-bank rules embedded in `_quizzes/2026Summer/quiz_generation_plan.md` §4.5 and `_midterm_exam/2026Summer/midterm_generation_plan.md` §5.6. All 48 quiz CSVs and 14 midterm case CSVs were rewritten to this standard on 2026-06-12.

---

## Decision 12: Fall 2026 — Midterm Dropped, Weights Reallocated, nb10 Retired (2026-08-14)

> **Superseded in part by Decision 13 (2026-08-15):** items 1, 2, 4, and 5 below no longer hold — the midterm is reinstated in class on paper, the weights are restructured, and nb18 runs once. Item 3 (nb10/nb15/nb20 retired) and the archival mechanics stand.

**Decision:** Effective with the Fall 2026 offering of QM47400:

1. **The midterm exam is dropped.** There is no midterm in Fall 2026.
2. **Its 20% is reallocated** — +10 points to the Course Case Competition (20% → 30%) and +10 points to the Final Project (35% → 45%). Participation (5%) and Quizzes (20%) are unchanged, so the weights are Participation 5% / Quizzes 20% / Course Case Competition (Kaggle) 30% / Final Project 45%.
3. **nb10 (the Midterm Casebook + Cheat Sheet) retires from the notebook arc.** As of 2026-08-14 **nb15 and nb20 retire as well**, leaving **eighteen** notebooks — nb00–nb09, nb11–nb14 and nb16–nb19.
4. **Monday and Wednesday carry content; every Friday is a Group Work session for the final project and the Course Case Competition.** Two Fridays are exceptions: Fri Aug 28 carries nb02 and Fri Sep 25 carries nb18's first pass.
5. **The last lecture session is Mon Oct 26** (nb17, Data Communication & Poster Design). **nb18 is taught twice** — Fri Sep 25 with linear models only, and Mon Oct 19 in full once the ensembles and nb14's protocol are in hand — and **nb19 moves to Wed Oct 21**, so all eighteen notebooks are covered by Mon Oct 26, leaving the calendar clear for the final poster.

**Rationale:**
- The full-semester format already assesses the same strategic reasoning the midterm tested — continuously, through the Kaggle competition and the twelve project milestones — so a one-shot in-person exam duplicated evidence the course was collecting anyway.
- Reallocating the 20% to the two authentic deliverables makes the grade track what the semester is actually built around: a deployed, reproducible predictive model and a poster defended in public.
- The Friday studio rhythm needs protected, recurring time. A midterm consumed a content session plus the review and consolidation sessions around it; dropping it is what makes the every-Friday studio pattern fit inside the Purdue calendar (Labor Day Sep 7, Fall break Oct 12–13, Thanksgiving break Nov 25–28).
- nb10 existed only to stage the midterm. Without the exam it has no successor to prepare, and its consolidation role is absorbed by nb09's Toolkit Recap and by the Friday studios.
- Finishing the lecture content on Mon Oct 26 gives every team two clear weeks to build the poster before it is due Tue Nov 10, ahead of the Fall Undergraduate Research Conference presentation on Tue Nov 17 and the Poster-to-Product sprint that follows.

**Exceptions:** none. The nb10 notebook files were moved out of `notebooks/` into `_archive/2026F_retired/` for archival reference — the student copy `git mv`'d and still tracked there, the instructor copy moved alongside it and gitignored by that folder's own `.gitignore` — and are not taught, scheduled, or assessed in Fall 2026.

**Implication:** Decision 11 (MC option-length parity) remains fully in force — it now governs the quizzes and any future exam rather than a midterm. Grade weights are published in `syllabus.qmd`; the session-by-session sequence is in `schedule.qmd` and `_project_docs/MGMT47400_FullSemester_Plan_2026Fall.md`. Milestone due dates are unchanged by this decision (M00 Sep 6 through M11/M12 Nov 15).

---

## Decision 13: Fall 2026 — Midterm Reinstated In Class (Paper), Weights Restructured, nb18 Single Session (2026-08-15)

**Decision:** Effective 2026-08-15, superseding Decision 12 items 1, 2, 4, and 5 (item 3 — nb10/nb15/nb20 retired — and the archival mechanics stand):

1. **The midterm exam is reinstated** as an **in-person, on-paper exam during class time on Fri Sep 25**, covering nb00–nb09. It is built **directly from the 2026Summer 14-case bank** (`_midterm_exam/2026F/`): per case form, **15 MC questions** (all fifteen Summer questions carried forward — kept, repaired, or replaced where they tested post-nb09 content or rested on a false premise), **five alternatives each** (a fifth length-parity distractor authored per question), 3 min/question = the full 45-minute window. nb10 (the Midterm Casebook) **stays retired**: the exam is administered from the case bank without a staging notebook.
2. **Weights:** Attendance 1% / Participation 4% / Quizzes 15% / **Midterm Exam 20%** / Course Case Competition 20% (20/60/20 internal split as in Summer; the peer-evaluation slice is 4 course points) / Final Project 35% (40/20/40 as in Summer; peer evaluation 7 course points) / **Poster-to-Product 5%** (80/20; peer evaluation 1 course point). Poster-to-Product becomes its own top-level grade line.
3. **nb18 is taught once, Mon Oct 19** — the full four-model pipeline in one session. The Round 01/Round 02 split (2026-08-14) is reverted in the notebook, the schedule, nb00/nb16/nb19 bridges, and the Brightspace pages (single `18_competition_workflow.md`).
4. **Fridays:** every Friday remains a Group Work session, with two exceptions — Fri Aug 28 (nb02) and **Fri Sep 25 (midterm exam)**.

**Rationale:** instructor decision to restore a summative in-person checkpoint on the mid-course toolkit while keeping the applied-work spine. The paper format avoids the online-integrity constraints Decision 11 documented, and five alternatives per question lower the guessing floor from 25% to 20%.

**Implication:** Decision 11 (MC option-length parity) applies to the 2026F midterm banks — every option ≥ 60% of the question's longest and correct-strictly-longest ≤ 40% per bank (chance is now 1/5). Grade weights are published in `syllabus.qmd`; the exam material lives in gitignored `_midterm_exam/2026F/` and syncs to the private instructor repo.

---

## Decision 14: Corrected CV-Inference Doctrine (2026-08-15)

**Decision:** The course's model-comparison rule changes. Three claims previously taught from `nb08` outward are retired as false: (1) that Student's *t* compensates for dependent folds — it only corrects for estimating the SD from few samples, and because folds share training rows the naive `s/sqrt(k)` interval is *optimistic*; (2) that overlapping marginal 95% CIs show two models are statistically indistinguishable — marginal-interval overlap is not a test of the paired difference; (3) that a test score landing INSIDE the CV interval confirms generalisation — a fold-mean interval is not a prediction interval for a different statistic on a different sample.

**What replaces them** (full spec, references, and authoring rules: `_project_docs/CV_INFERENCE_DOCTRINE.md` — binding):

1. The `mean ± t·s/√k` arithmetic stays, relabelled a **descriptive / approximate 95% interval**, with the dependence caveat stated once per notebook.
2. Model comparison = **paired per-fold differences on identical folds** (same splitter object, same seed) judged against a **predeclared practical-equivalence margin**, with three distinct outcomes: same sign + clears margin → real difference; signs flip → the comparison does not support a winner; same sign under the margin → practically equivalent, the simpler model wins (the parsimony tiebreak survives on honest grounds).
3. The nb14 ceremony's INSIDE/ABOVE/BELOW vocabulary survives as *description only*; deployment is judged against the predeclared business tolerance, never against the CV interval.

**Trigger:** An independent Codex `ultra` review of the Fall 2026 midterm traced invalid exam items to the teaching material itself (Bengio & Grandvalet 2004; Nadeau & Bengio 2003; Schenker & Gentleman 2001).

**Scope:** the 2026F midterm banks (rebuilt to the doctrine), 10 notebooks (nb02, nb06, nb08, nb09, nb11–nb14, nb16, nb18 — instructor copy first, per the instructor-first rule), 17 quiz banks with keyed options asserting the overlap rule, the video guides, and the Brightspace pages. Decision 9 (test-set lock) is unaffected and stands.

**Implication:** any new material that states a CV comparison rule must follow the doctrine file; its "Authoring rules" section (A1–A6: never assert an uncomputed number; keep the three outcomes distinct; declare the margin before results, once; prose and code move together; sweep whole notebooks, not mapped cells; instructor copy first) is part of the decision.

**Addendum — Amendment 1 (2026-10-26).** Point 2's verdict rule is replaced. A literature check on the CV-interval lower-bound tiebreaker (Claude and a Codex partner run, sources and numbers re-verified) found that the August rule's "same sign on every fold" is weak evidence at k = 5 (1 in 16 by chance with independent folds, about 1 in 6.5 with correlated folds) and that "same sign but under the margin" was being read as practical equivalence, which is absence of evidence (Lakens 2017). The verdict now comes from the **Nadeau–Bengio corrected paired interval**, `mean(d) ± t·sd(d)·√(1/k + 1/(k−1))`, read against ±margin, with **four outcomes**: worthwhile gain (`L > δ`), worthwhile loss (`U < −δ`), practically equivalent (interval inside ±δ), unresolved (anything else). The parsimony rule survives as a **stated business policy**: the complex model is adopted only on a worthwhile gain, and only the equivalent outcome may be called "practically equivalent". A2 now reads "keep the four outcomes distinct". Applied 2026-10-26 to the doctrine, this file, `CLAUDE.md`, and poster rubric criterion 6 (with a Fall 2026 transition clause that accepts the August verdict for full credit); the notebook, quiz, midterm, guide, and Brightspace rollout is pending — the doctrine's Amendment 1 section tracks it.

**Addendum — Amendment 2 and the Spring 2027 rollout (2026-11-24).** Davi asked (2026-11-24) for every notebook and Brightspace page of the Spring 2027 edition to be corrected to the review plan of record (`../2026F_predictive_analytics_QM474/_adm/doctrine_drafts/2026-10-26_amendment1_course_review/AMENDMENT1_COURSE_REVIEW_PLAN.md`), with its open decisions defaulted to the plan's own recommendations. Point 1 of this decision is therefore replaced: **no per-model 95% interval** — a single model is reported by its fold scores, mean and SD, and the only interval in model evaluation is the corrected interval of a paired gain (doctrine Amendment 2, the plan's D4). Every comparison uses the course's one function, `compare_paired` (challenger = A, current champion = B; only "A is better by a worthwhile amount" promotes). Each business case declares a **margin band** before scoring (small / base / large; base decides; report robust or margin-sensitive), climbs a **simplest-first ladder** from the incumbent the stakeholder runs today (D2), treats a grid's best cell as a **nominee** that faces the default (D3), and ends with a **four-point champion statement**. Point 3 is amended: the nb14 ceremony opens the test set once per case for the frozen champion, refit on `X_train`, and the ship decision is the deployment bar declared in advance; INSIDE/ABOVE/BELOW only describes the test score against the champion's CV mean ± δ. Predictive uncertainty is a declared guardrail or primary metric, never a tiebreaker (D8); prediction intervals use CV+ (R7). The defaults Davi has not yet confirmed (D2, D3, D4, D6, D7, R1, R7) are listed in the rollout sessions' reports under `_adm/2027S_setup_2026-11-24/reports/` so he can overturn any of them. Two nb14 guardrail details remain open and are kept out of the student text (doctrine, "Open items in nb14"): the MedScreen recall and Brier tolerances (*medscreen-guardrail-margins*) and whether HomeValue gets a CV+ price-range guardrail at all (*homevalue-range-guardrail*).

---

## Decision 15: Honors Contract Anchored in the Final Project (2026-08-21)

**Context.** A John Martinson Honors College student asked to contract QM 47400 on 2026-08-20. Daniels processes contract paperwork for every DSB-taught course, so the course needed standing honors language rather than a one-off arrangement — and Davi, as DSB Honors Director, wanted something reusable across courses and terms.

**Decision.** The honors contract is **an individual research angle on the group final project**, never a parallel course. Three deliverables ride along existing milestones — H1 question memo with M01, H2 modeling extension (CV-first, paired per-fold comparison against the team's baseline) with M08, H3 a labeled honors section on the team poster with M10 and the conference. Ten points move from the Final Project (35% → 25%, all five components scaled proportionally) to a 10% Honors Research Extension, so the student's total never grows. Where an entire team holds contracts, neither the reallocation nor the separate poster section applies.

**Why not a bolt-on project.** The DSB faculty-facing guidance is explicit that contracting "doesn't have to add to your workload," and the sample contracts that work reuse an assignment the instructor already runs. Anchoring in the final project keeps the marginal cost near zero for both sides and keeps the honors student inside their team rather than beside it.

**Why it doubles as the Scholarly Project.** JMHC requires new knowledge, presented publicly, with a confirmed faculty mentor — and the review note Davi writes most often is that the individual contribution must be unmistakable. H1 names the student's question, H2 produces their result, H3 puts their name on a labeled poster section, the URC is the public venue, and Davi already mentors the final project. Approval remains JMHC's; the student files the proposal by the fall deadline (Oct 1) and the completion verification afterward.

**Source of record.** The section lives in `_syllabus/2026F/2026F_predictive_analytics_purdue_QM474.docx`; `syllabus.qmd` is synced *from* it, never the reverse. Deliverable dates in student-facing text say "Check the course Brightspace page"; the attachable honors syllabus carries the specific dates, because the contract requires "specific assignments, deadlines, and grade scheme."

**Grading mechanics (added to the docx 2026-08-21).** The honors section on the poster is graded exclusively under the Honors Research Extension — it is not evaluated under the group poster rubric and cannot raise or lower the team's poster grade, which protects non-honors teammates from absorbing a hit on the shared 100-point rubric. Separately, **the running Brightspace gradebook shows only the regular course requirements**; the Honors Research Extension is folded in by a **manual adjustment to the final course grade** once the contract is complete. That manual step is the operational risk in this design — it has no automatic trigger, so it belongs on the end-of-term checklist for every term a contract is live.

**Artifacts.** `scripts/build_honors_section_docx.py` (slices the section out of `syllabus.qmd`) and `scripts/build_honors_syllabus_docx.py` (renders the modified honors syllabus in the DSB template). Both write into the gitignored `_syllabus/2026F/honors_contract/`. Regenerate; never hand-edit the output.

**Key dates (Fall 2026, verified).** Student intake closes **Thu Sep 3, 11:59 p.m.** (Daniels form + Qualtrics, not extendable) · coordinator decisions due **Fri Sep 18** · JMHC scholarly-project proposal due **Thu Oct 1**. These shift each term — pull from the Registrar Add/Modify calendar and the live Daniels Honors Contract page rather than reusing them.

---

## Decision 16: Midterm Banks Rewritten to 15 Items x Four Options, in Plain Language (2026-10-07)

**Decision.** Effective 2026-10-07, every midterm form in `_midterm_exam/2026F/` prints **15
multiple-choice questions with four alternatives each (A–D)** in 45 minutes, one item per slot of a
common fifteen-slot blueprint, in this order:
- framing;
- two EDA items;
- split;
- pipeline;
- baseline;
- metric;
- two leakage items;
- threshold or regularization;
- a form-specific modeling item;
- two cross-validation items;
- tuning;
- an in-scope synthesis item.

Every stem, option, answer-key rationale and case briefing was rewritten in smooth, simple, fully
spelled-out language for undergraduate business students, to the spec in
`_midterm_exam/2026F/STYLE_GUIDE_15x4.md`.

This supersedes the "five alternatives each" clause of Decision 13, item 1, and the ten-item selection
of 2026-08-29. The Fri Sep 25, 2026 sitting (10 items, five options) is frozen in
`_midterm_exam/2026F/archive/administered_2026-09-25/` for grading, appeals and the version-effect
analysis.

**Rationale.** From the midterm feedback survey (85 finished responses, Sep 28 – Oct 2, 2026;
`_adm/_grade/2026F/midterm_exam/feedback_survey/REPORT.md`):
- 55% agreed the questions were clearly worded;
- 55% agreed they could tell the five options apart;
- 55% preferred more, shorter, lower-weight items;
- students reported spending more time reading than answering.

**Why fifteen items and four options.**
- **Fifteen items** lower the stakes per item: each is one fifteenth of the exam instead of one
  tenth.
- **Four plausible options** cut reading time and are not worse psychometrically than five (Rodriguez,
  2005). On Sep 25, 13 of 40 AstraOrbit and 9 of 40 SiliconPeak distractors drew no one.
- **Reading load:** about 2,200–2,400 words per form (briefing plus items), against about 3,000 for
  10 items on Sep 25.
- **Guessing floor:** it rises from 20% to 25%, which is accepted.

**How it was built and checked.**
1. A per-form rewrite. A blind solver who never saw the key, a content and doctrine reviewer, and a
   plain-language and cue reviewer checked each form, with fix rounds after.
2. A slot-wise cue fix across forms.
3. A taught-content audit of slots 2, 6, 7, 10, 12, 13 and 14 against the notebooks. It found that
   the spec's tuning rule was not taught in nb09, so the spec was corrected.
4. An independent Codex review (`gpt-6-astra`, ultra). It found ten major item defects, a new
   option-convergence cue (47.9%) and several gate false passes. Its verified findings were applied.
5. A spread pass after the convergence repair overcorrected into an "avoid the extremes" cue (40.7%).

A fresh blind solve and adjudication followed every round. In the final round the blind solver agreed
with the key on all 210 items.

**Implication.**
- **Decision 11 applies with chance at 1/4:**
  - every option is at least 60% of the length of the item's longest option;
  - the correct option is strictly the longest in 2–4 of 15 items per bank;
  - the correct option's length rank varies.
- **The release gates pass:**
  - `validate_banks.py` (built on `item_lint.py`);
  - `check_exam_structure.py`, which now checks answer labels, the answer grid, verdict placement,
    the dealt option order and signed numbers;
  - `check_pdfs.py`;
  - `scripts/audit_answer_length.py`, which now requires exactly one key per question;
  - `scripts/audit_option_cues.py --style`, which now also tests option convergence, "avoid the
    extremes" rules and every rank of the style model, and fails closed.
- **A known residual:** independent learned probes still place the key at their top pick about
  9–11 points above chance.
- **What the gates do not establish:** a common blueprint gives the forms the same organization, but
  not equal difficulty, reliability or interchangeable scores (Standards 5.12). Timing still needs a
  pilot (Standards 4.14).

The syllabus of record (docx) and `syllabus.qmd` describe the Fall 2026 sitting as administered, and
this decision does not change them. A future offering's syllabus must state "15 multiple-choice
questions with four alternatives each".

**Open for the instructor.**
- Codex's proposed rewording of the CV doctrine's C2/C3: a descriptive decision rule, not a test.
- The notebook defects in `_midterm_exam/2026F/NOTEBOOK_ISSUES_2026-10-07.md`.
- Whether NovaCure was released as practice in August.
- A common mixed-family design (classification and regression on every form) for future sittings.

---

## Decision 17: Five Folds Everywhere; Train/Test Only After nb08 (2026-10-27; applied 2026-11-24)

**Decision (Davi, 2026-10-27 — D11 and D12 in the Fall review plan, applied to the Spring 2027 edition on 2026-11-24):**

1. **D11 — five folds everywhere.** Every cross-validation in the course uses five folds: outer, inner and
   grid search. Classification: `StratifiedKFold(n_splits=5, shuffle=True, random_state=474)`; regression:
   `KFold(n_splits=5, shuffle=True, random_state=474)`; nested CV is 5 outer × 5 inner. No 3-fold or 10-fold
   splitter anywhere. If a 5-fold grid is too slow in Colab, shrink the search (e.g. `RandomizedSearchCV`
   with a fixed `n_iter`), never the folds.
2. **D12 — after nb08, train/test only.** From nb09 on each notebook splits each dataset once:
   `train_test_split(X, y, test_size=0.20, random_state=474)`, stratified for classification → `X_train` /
   `X_test`. No `X_val`, no `*_temp`, no 60/20/20, no carve-out inside a cell. All model work runs on
   `X_train` with D11's splitters; `X_test` stays locked except nb14 cells 30/34 (nb18's Fall 2026 Kaggle-demo
   allowance was dropped on 2026-11-24, when nb18 became the temporal S&P 500 competition notebook; Decision 18).
   nb01–nb07 keep the train/validation/test split (where it is taught; Decision 2); nb08 uses it only to
   motivate CV and ends on the 80/20 + 5-fold pattern; **nb16 is the temporal exception** (temporal
   train/test + walk-forward CV), and from Spring 2027 so is the S&P 500 competition notebook nb18.

**Rationale:**
- Once CV is taught, the validation set's only job — an untouched sample for choosing — is done better by
  5-fold CV on more rows; a third partition after nb08 contradicted the CV-first rule (Decision 9).
- One fold count makes every `compare_paired` interval, its correction term √(1/k + 1/(k−1)), its *t*
  quantile and every grid comparable across notebooks.
- The locked test rows do not move: the first `train_test_split` call is unchanged, so `X_test` is the
  identical set of rows and the new `X_train` is the old training rows plus the old validation rows
  (verified in the review plan §16.1 and printed by nb08 §5).

**Replacements for the validation set:** held-out predictions, classification reports and threshold choice
→ `cross_val_predict` on `X_train`; probability quality → cross-validated Brier; calibration →
`CalibratedClassifierCV(cv=5)` evaluated by CV; permutation importance → inside the 5-fold loop on each
fold's held-out rows, averaged; prediction intervals → **CV+** (Barber, Candès, Ramdas & Tibshirani, 2021),
the plan's R7 recommendation, adopted by default on 2026-11-24.

**Enforcement:** `scripts/audit_cv_first.py`, check 2 ("data roles"), on the nb09–nb19 student copies
(nb16 and nb18 exempt). Supersedes Decision 2's sentence that 60/20/20 "still applies to every one" of the
notebooks. **Open edges** (review plan §16.9): milestones M06/M08 and the poster rubric still allow
"k = 5 or 10" (main session owns those files); nb16's walk-forward origins are not "five folds" in the k-fold
sense.

---

## Decision 18: Course Case Competition Becomes a Group S&P 500 Forecasting Competition (2026-11-24)

**Decision (Davi, 2026-11-24, Spring 2027 edition):** the Course Case Competition is no longer a churning
bank-customer classification case. It is a **group S&P 500 forecasting competition**. Design of record:
`_course_case_competition/2027S/course_case_competition_reference.md` (student instructions:
`course_case_competition_instructions.pdf` in the same folder).

- **The task.** Each team forecasts the **cumulative log return** of the S&P 500 at **1, 5, 10, 15 and 20
  trading days** ahead, as **quantile forecasts** (q10, q25, q50, q75, q90).
- **The score.** **Scaled pinball loss** against a **random-walk benchmark**; skill = 1 − team loss ÷
  benchmark loss, so a positive skill beats the benchmark.
- **Two rounds.** An **ungraded practice round hosted on Kaggle**, then a **live round scored by the host**
  (`scripts/score_live_round.py`): the live forecast origin is Thu Mar 25, 2027; forecast, code and memo are
  due Fri Mar 26, 11:59 PM (NYSE closed for Good Friday); the live window runs Mon Mar 29 – Fri Apr 23; host
  scoring Apr 24–25; final peer evaluation Fri Apr 30.
- **Grading (of 100).** Live forecast 15 (valid, on time and reproduced 10; rank 5 —
  `[[PENDING sp500-rank-weight]]`) · walk-forward **method notebook 45** · **memo 20** · **final peer
  evaluation 20**. The competition's share of the course grade is unchanged (Decision 13; Decision 19 for the
  Spring 2027 weights).
- **Notebooks.** The old nb18 (competition workflow on the bank-churn case) is **replaced** by the S&P 500
  competition notebook (kickoff Wed Mar 3, 2027); **nb16** (time series) is **extended** to carry the
  forecasting methods the competition needs.
- **Data roles.** nb18 is a second **temporal exception** to Decision 17: it locks the most-recent window
  (an information cutoff) and scores walk-forward origins, with no random split. It has no `X_test`, so the
  Fall 2026 allowance for "nb18's Kaggle-submission demo" was removed from `scripts/audit_cv_first.py`; the
  only authorized test-set openings are nb14 cells 30 + 34.

**Rationale (reference §4, computed 2026-11-24 by `scripts/luck_analysis.py`):** a forecast range is
essential — a point-only forecast loses to the random-walk benchmark in 88% of single months — but between
two reasonable ranges one live month is close to a coin toss (the benchmark beats a band half as wide in 49%
of single weeks although it is better on average). So the live forecast carries only 15 of the 100 points
and the grade rests mainly on the walk-forward method notebook (45) and the memo (20).

**Open:** the rank weight inside the live-forecast 15 points (`[[PENDING sp500-rank-weight]]`).

---

## Decision 19: Spring 2027 Grading and Process Changes (2026-11-24)

**Decision (Davi, 2026-11-24, Spring 2027 edition).** Sources of record: `syllabus.qmd` and §7 of
`_project_docs/QM47400_FullSemester_Plan_2027Spring.md`; dates live in `scripts/build_2027S_calendar.py`.

1. **Weights.** **Attendance 1% → 5%**, taken by **location-verified iClicker**; **Quizzes 15% → 11%**.
   Every other weight in Decision 13 is unchanged (Participation 4%, Midterm Exam 20%, Course Case
   Competition 20%, Final Project 35%, Poster-to-Product 5%; peer evaluation 20% of each group component).
2. **Two peer evaluations.** A **midpoint, formative** evaluation (Sun Mar 7, 2027) whose flags trigger a
   check-in with the team, and a **final, graded** evaluation (Fri Apr 30, 2027) that carries the 20% peer
   shares.
3. **A presentation at every TA/instructor meeting** (M00, M04, M07, M13): about five slides in five
   minutes, uploaded before the meeting, every member presenting each round. **No presentation means the
   meeting does not count.**
4. **No M09 draft, no conference.** A team that does not submit the M09 poster draft (Sun Mar 28, 2027) does
   not present at the Spring Undergraduate Research Conference (Tue Apr 13, 2027).
5. **Brightspace instructions only as an attached PDF.** Every assignment's instructions are the attached
   PDF (milestones built by `scripts/build_milestone_pdfs.py`); the Brightspace instructions field carries at
   most a short note.

**Where each change lands** (plan §7, rows 2 and 5–7): weights → `syllabus.qmd`, `README.md`, the honors
table, and the iClicker setup guide `_adm/_brightspace/2027S/ICLICKER_ATTENDANCE_SETUP.md` (confirm Purdue's
2026–27 iClicker license first); peer evaluations → the calendar, `peer_evaluation_midpoint.md` (new PDF) and
`peer_evaluation.md`; M09 rule → syllabus, M09, conference and overview PDFs, announcements; meeting
presentations → the M00, M04, M07 and M13 PDFs (M04 opens Feb 8, M13 Mar 8), the overview and the syllabus.
No separate rationale was recorded with these decisions.
