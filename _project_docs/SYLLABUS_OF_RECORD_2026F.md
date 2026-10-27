# Syllabus of Record — Fall 2026 (QM 47400)

**The official syllabus is `_syllabus/2026F/2026F_predictive_analytics_purdue_QM474.docx`** (updated 2026-08-17, PDF exported alongside it). `_syllabus/` is gitignored, so the file itself is local-only — this page is the tracked record of what it says.

When the docx and any other artifact disagree — `syllabus.qmd`, `schedule.qmd`, `_project_docs/`, Brightspace copy — **the docx wins** and the other artifact is the thing to fix.

---

## Facts of record

| Field | Value |
|---|---|
| Course | QM 47400 — Predictive Analytics, Fall 2026 |
| Sections | **001 and 002**, both Monday / Wednesday / Friday, **WTHR 114** |
| Term | Aug 24 – Dec 11, 2026 |
| Instructor | Professor Davi Moreira · Young Hall 1019 · dcordeir@purdue.edu |
| **Office hours** | **Mondays 2:30–3:30 p.m. EST**, Zoom `https://purdue-edu.zoom.us/j/9397534582` |
| Appointments | Outlook "Book time with me" link (Virtual — General Office Hours) |
| **Prerequisite** | **MGMT 305 Business Analytics** or a similar statistical foundations course |
| Brightspace | Official source of record for material and announcements |
| Course website | https://davi-moreira.github.io/2026F_predictive_analytics_QM474/ — explicitly **non-official**, supplementary |

### Honors contract (added to the docx 2026-08-21)

The official syllabus now carries a top-level **HONORS CONTRACT (OPTIONAL)** section, placed after the DataCamp extra-credit block and before the Netiquette guidelines. It is the source of record for the honors route and `syllabus.qmd` was synced to it the same day.

| Field | Value of record |
|---|---|
| Route | John Martinson Honors College honors contract; the honors work is an individual research angle on the group final project, not a parallel course |
| **Student intake deadline** | **Thu Sep 3, 2026, 11:59 p.m.** — Daniels request form + Qualtrics; cannot be extended |
| Coordinator decision deadline | Fri Sep 18, 2026 (4th Friday), entered in the Registration Workflow |
| Step 1 | **The student supplies the research question and Davi must approve it** (this replaced an earlier "we talk it over" framing) |
| Attachments the student uploads | **The official syllabus alone** — confirmed by Davi 2026-08-21. Because the honors section carries its own grading scheme inside the official syllabus, that one file satisfies both the standard and the modified-syllabus requirement on the contract form. `QM47400_2026F_honors_syllabus.docx` is therefore **not** the upload; it is retained only in case a future term or another college asks for a separate modified syllabus |
| Deliverables | **H1** honors question memo (rides M01) · **H2** modeling extension, CV-first, paired folds vs. the team baseline (rides M08) · **H3** one clearly labeled honors section on the team poster plus a conference walkthrough (rides M10 and the conference) |
| Deliverable due dates | **"Check the course Brightspace page"** in the syllabus. Specific dates appear only in the attachable honors syllabus, which the contract requires to carry them |
| Weights | Final Project 35% → 25%, all five components scaled; **Honors Research Extension 10%** (H1 2% · H2 5% · H3 3%). Total stays 100% |
| Entire-honors-group case | The ten-point reallocation and the separate poster section apply **only when the team is not entirely an honors group** |
| Group contracts | Allowed, **limited to the course maximum group size** |
| Scholarly Project | The contract is built to qualify (individually attributable new knowledge, public presentation at the URC, Davi as mentor). Approval stays with JMHC; student files the proposal by **Thu Oct 1, 2026** and the completion verification afterward |
| Meetings | Three one-on-ones of about fifteen minutes — late September, late October, after the conference — booked through the team's existing instructor/TA meeting procedure |
| **Poster-rubric exclusion** | The honors section on the poster is graded **exclusively** under the Honors Research Extension. It is not evaluated under the group poster rubric and cannot raise or lower the team's poster grade. (Restored to the docx 2026-08-21 after an earlier draft dropped it.) |
| **Gradebook mechanics** | **During the term the Brightspace gradebook shows only the grade earned through the regular course requirements.** After the student completes the full contract, Davi **manually adjusts the final course grade** to incorporate the Honors Research Extension. Nothing honors-related appears in the running gradebook, so the adjustment is a manual end-of-term step that must not be forgotten. |

Artifacts, both regenerated from source and never hand-edited:

| File | Built by | Purpose |
|---|---|---|
| `_syllabus/2026F/honors_contract/QM47400_2026F_honors_contract_section.docx` | `scripts/build_honors_section_docx.py` (slices `syllabus.qmd`) | The section alone, for pasting into the official docx or sending on its own |
| `_syllabus/2026F/honors_contract/QM47400_2026F_honors_syllabus.docx` | `scripts/build_honors_syllabus_docx.py` | The **modified honors syllabus** in the DSB template format, carrying the specific deadlines the contract requires |

### Assessment weights

Attendance 1% · Participation 4% · Quizzes 15% · Midterm Exam 20% · Course Case Competition 20% · Final Project 35% · Poster-to-Product 5%. **No final exam.** Matches `CLAUDE.md` and `DECISIONS.md` Decision 13 — unchanged by the 2026-08-17 update.

### Midterm exam

In person, on paper, during class time; covers material through `nb09`. **The docx states no date** (the schedule pins it to Fri Sep 25). 15 multiple-choice questions, five alternatives each, 45 minutes. Closed book: *no notes, no textbooks, no calculators, no phones, no laptops, no AI tools*. Make-up requests by email with documentation no later than 7 days before the exam.

### Course Case Competition (20%)

Kaggle **Case Competition: Bank Churn**, adapted from the 2024 Kaggle Playground Series (AI-generated synthetic data). Groups of **up to four**; **five submissions per day**.

- **Opens September 4, 2026** *in the docx* — **superseded on 2026-09-04:** the competition now opens **Fri Sep 18, 2026**, the first studio after nb07 lands ROC-AUC. `schedule.qmd` and the planning docs carry the new date; the docx sentence still reads "September 4, 2026" and needs Davi's edit in Word. See register item 16.
- **Final submission deadline November 29, 2026.**
- **Invitation link:** `https://www.kaggle.com/t/e32195d923ae45edbebe05fa5ce57fdd`
- Breakdown: Team Participation 20% · Leaderboard Performance 60% (rank-scaled, AUC = 0.5 earns zero) · Peer Evaluation 20%.

### Final Project (35%)

Group project culminating in a research poster. **The docx currently carries two contradictory Final Project sections** — see the discrepancy register. The later of the two, which matches the course website, is:

Milestone Deliverables 30% · Peer Evaluation 20% · Peer Review 10% · Poster Presentation at the URC 20% · Instructor/TA Evaluation 20%.

Award-winning poster examples: `https://davi-moreira.github.io/applied_projects.html`. Conference info: `https://www.purdue.edu/undergrad-research/conferences/index.php`.

### Poster-to-Product (5%)

Two-week in-class build sprint after the conference: validated model → stakeholder-ready dashboard/app + executive brief, following scope → data engineering → model validation → UX → deployment → usability testing → showcase. Assigned AI assistant per team under human-in-the-loop sign-offs. **Showcase Wednesday, December 9, 2026.** Funded by a **Mitch Daniels School of Business Experiential Learning Grant**. Breakdown: Deliverables and Showcase 80% (NACE competencies — Technology, Teamwork, Communication, Critical Thinking) · Peer Evaluation 20%.

### Extra credit (not published on the course website)

1. **Course evaluations** — screenshot of the midterm and/or final evaluation confirmation earns **+0.5%** on the final Participation grade.
2. **Issues in course materials** — **+0.25%** toward final Participation per confirmed issue, reported by email by **Fri Dec 4, 11:59 pm**; upload a PDF of the email thread with the instructor's confirmations in the last week of class.
3. **DataCamp — up to 5% of the overall course grade.** Every enrolled student gets a six-month subscription. Each fully completed course = **1%**, maximum five. Submit the Statement of Accomplishment PDFs on Brightspace by **Fri Dec 4, 2026, 11:59 pm**. Only courses completed during this term count; partial completions earn nothing; courses must be completed independently, and **no two may share a completion date or fall within two days of each other**.

### Grade challenges

Within **3 calendar days** of release; **1 calendar day** during the last week of class. Grades are never discussed in the classroom.

### AI policy

Encouraged for learning; **not allowed during exams**. Refine prompts, ask for explanations rather than solutions, verify output (errors are the student's responsibility), and **always cite AI use** in a short note at the end of any document.

---

## Discrepancy register — open items for Davi

These are contradictions *inside* the official docx or between it and other artifacts. None are fixed automatically; each needs Davi's decision.

| # | Issue | Where | Impact |
|---|---|---|---|
| 1 | ✅ **RESOLVED 2026-08-20** (verified: no "May 18", "June 12", "Day 0", or Summer-repo links remain in the docx). ~~The embedded "TENTATIVE COURSE SCHEDULE" was the Summer 2026 4-week intensive table~~ — "May 18 – June 12, 2026", Day 0–20, Colab links pointing at the `2026Summer_predictive_analytics_purdue_MGMT474` repo. Entirely the wrong offering. | syllabus docx, final section | **High.** Students would read a May–June calendar with dead notebook links. Replace with the Fall table now in `2026F_predictive_analytics_QM474_schedule.docx`. |
| 2 | ✅ **RESOLVED 2026-08-20** by Brightspace: the live *Peer Review Submission* proves the 30/20/10/20/20 version is operative. ~~Two contradictory "Final Project" sections.~~ The first says conference presentation is **required**, poster due Tue Nov 10, breakdown 40/20/40. The second says presenting is **"not required"** but encouraged, and uses the 30/20/10/20/20 breakdown. | syllabus docx | **High.** The two disagree on both the requirement and the grade split. The website publishes the 30/20/10/20/20 version and treats presentation as required. |
| 3 | ✅ **CLOSED — superseded by item 16.** ~~Kaggle opens "August 28, 2026" in the docx;~~ the docx was later changed to **September 4, 2026**, and on 2026-09-04 the open date moved again to **Fri Sep 18** (after nb07). | docx vs. site/plan | Superseded; the live conflict is tracked in item 16. |
| 4 | ✅ **RESOLVED 2026-08-20.** ~~Typo: "after August 248, 2026"~~ in the DataCamp extra-credit rule. | docx, extra credit §3 | Low — but it is the eligibility start date, so it should read Aug 24 or Aug 28 to match #3. |
| 5 | Typo: "within **1 calendar days**". | docx, grade challenges | Low. |
| 6 | Office hours are **Mon 2:30–3:30 EST** in the docx; the website now says only "details on the course Brightspace" (changed 2026-08-17 at Davi's request). | docx vs. site | None — intentional. The docx and Brightspace carry the time; the site defers to them. |
| 7 | The docx keeps the **Poster-to-Product 80/20 breakdown** and the **competition 20/60/20 breakdown**; the website dropped both in the 2026-08-17 trim. | docx vs. site | None — intentional. The docx is the fuller document. |
| 8 | Prerequisite (**MGMT 305**), section numbers, room (**WTHR 114**), the **Kaggle invitation link**, the **poster examples link**, and the whole **extra-credit section** appear only in the docx. | docx | Low. The site links to Brightspace for these; noted here so they are not lost. |

| 9 | **The docx still says the midterm covers "cross-validation with 95% confidence intervals".** That is retired claim W1 in `CV_INFERENCE_DOCTRINE.md`; the fold interval is descriptive, not a confidence interval for true performance. `schedule.qmd`, `syllabus.qmd`, the midterm README, and the published site were corrected on 2026-08-20, so the docx is now the **only** artifact still carrying it. | docx, Midterm Exam section | Medium. Suggested replacement: "cross-validation and paired model comparison". Not edited automatically because the file was open in Word. |

| 10 | ✅ **RESOLVED 2026-08-21** — Davi pasted the section into the docx and edited it there; `syllabus.qmd` was synced to the docx the same day (step 1 now requires his approval of the research question, deliverable dates defer to Brightspace, H3 is an "honors section" on the poster, group contracts are capped at the course max group size, and the ten-point reallocation applies only when the team is not entirely an honors group). ~~The Honors Contract section exists only on the website.~~ | site vs. docx | None. |

| 11 | ✅ **RESOLVED 2026-08-21** — Davi corrected it in the docx and regenerated the PDF; H3 now reads "carrying your extension **if** it is not an honors group". ~~Typo "it it" in the H3 row.~~ | docx | None. |

| 12 | **The "How to start" list renders as 3. / 4. / 5. instead of 1. / 2. / 3.** in the syllabus PDF — a Word list-numbering continuation from the preceding list. Cosmetic, but it is the first thing an honors student reads, and this PDF is what Brightspace serves under Content > Syllabus PDF. Fix: right-click the first item, "Restart at 1", and re-export. | docx and PDF, Honors Contract section | Low. |
| 13 | **The exam resource policy changed and the docx has not caught up.** On 2026-08-29 Davi specified that the printed midterm allows **any type of calculator** and **one sheet of notes, in any format**. The docx still reads *"Closed book: no notes, no textbooks, no calculators, no phones, no laptops, no AI tools"*, and `syllabus.qmd` (two places) plus the midterm README repeat it. The printed booklets state the new policy on their signed instruction page, and **`syllabus.qmd` and the README were brought into line on 2026-08-29** (rendered and pushed). **Only the docx is still out of date.** | docx, Midterm Exam section | **High — docx only.** The website and the paper now agree; the docx does not. Paste the replacement text below into the docx in Word. |
| 14 | **The midterm is now 10 questions, not 15.** Changed 2026-08-29. The docx, `syllabus.qmd` (line ~95) and the schedule handout all still say *"15 multiple-choice questions with five alternatives each"*. The printed booklets and their instruction page now say 10, at the same 45 minutes (about 4.5 min per question). The five held-back items stay in each bank as replacements. | docx, Midterm Exam section | **High — docx only.** `syllabus.qmd` and the README now say 10 (updated 2026-08-29); the docx still says 15. The question count is what a student plans their time around. |
| 15 | **The notesheet wording is now fixed text.** The instruction page prints exactly *"One sheet of paper, 8.5” x 11”, front and back, is allowed as a notesheet."* Any syllabus language about notes must match this exactly, including the size, or a student can argue the two documents permit different things. | docx | Medium — docx only. `syllabus.qmd` now carries the exact sentence. Listed separately because the wording, not just the permission, is load-bearing: the paper and the syllabus must describe the same notesheet. |
| 16 | **The docx says the competition opens "September 4, 2026".** Changed 2026-09-04: the Course Case Competition now opens **Fri Sep 18, 2026** — the first Friday studio after nb07 (Wed Sep 16) teaches ROC-AUC, the metric the leaderboard scores. `schedule.qmd`, `MGMT47400_FullSemester_Plan_2026Fall.md`, `claude_course_plan.md`, and `notebook_sequence_justification.md` were updated the same day; the docx paragraph beginning *"Course Case Competition: we will have a course-long predictive analytics competition"* still needs Davi's edit in Word — replace *"The competition will open on September 4, 2026"* with *"The competition will open on September 18, 2026"*. The Brightspace **Competition Team Setup (due Sun Sep 20)** already assumes the later start. | docx vs. site/plan | **Medium.** The docx is the source of record and is student-facing; it currently promises an open date two weeks earlier than the schedule. |


### Paste-ready replacement for the docx Midterm Exam section (items 13-15)

Replace the sentence beginning "You have 15 multiple-choice questions" and the closed-book sentence
after it with:

> You have **10 multiple-choice questions with five alternatives each**, and **45 minutes** of class
> time to complete them (about 4.5 minutes per question).
>
> **Answers are marked on a scantron form, and only the scantron is scored** — nothing written in the
> exam booklet is graded. Bring a **number 2 pencil**. Print your name, your instructor, and your
> section on the scantron. Several business cases are in use, so **your exam version number will be
> announced at the start of the exam**; code it on your scantron, because a scantron without the
> correct version cannot be graded.
>
> **You may use any type of calculator**, and **one sheet of paper, 8.5" x 11", front and back, is
> allowed as a notesheet**. The notesheet can be prepared in any way and is not collected. Otherwise
> the exam is **closed book**: no textbooks, no other notes, **no AI tools**, and no phones, laptops,
> tablets, smart watches, earbuds, or any other device that can communicate or reach the internet.

And in the AI-policy list, replace the midterm bullet with:

> You are **not allowed to use AI tools while taking quizzes or the midterm exam**. The midterm is an
> in-person paper exam: no AI tools and no electronic devices. A calculator and one 8.5" x 11"
> notesheet, front and back, are the only permitted aids.

This is the text now published on the website, so pasting it makes the two agree exactly.

---

**Last updated:** 2026-08-29 (items 13-15: `syllabus.qmd` and the README updated and published; the docx remains outstanding, paste-ready text above. Originally opened: the midterm now allows a calculator and a fixed-wording notesheet, and is 10 questions rather than 15 — all three contradict the docx). Previously 2026-08-21 (honors contract complete in the docx and PDF; items 10-11 resolved, item 12 opened); facts of record last read 2026-08-17 from `2026F_predictive_analytics_purdue_QM474.docx` (modified 2026-08-17 16:54).
