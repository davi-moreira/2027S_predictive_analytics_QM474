# QM47400 Predictive Analytics — Spring 2027 Edition Plan

**Status:** started 2026-10-27 (Claude Code, with Davi). This edition is where every update from the Fall 2026
course-material review is applied. Nothing here changes the Fall 2026 course, which keeps running from its
own repo until Dec 11, 2026.

**Folders on this computer**
- This repo: `/Users/dcordeir/Dropbox/academic/cursos/cursos-davi/predictive_analytics/2027S_predictive_analytics_QM474`
- Seeded from: `../2026F_predictive_analytics_QM474` (Fall 2026), 2026-10-27, with `rsync`. Left out: git history,
  rendered `docs/`, videos, slides, NotebookLM files, datasets, the private instructor mirror, `_archive/`, the
  administered Sep 25 midterm sitting, Fall's `_adm/` (except `_adm/_instructor_page/`, which the site's
  post-render step needs) and Fall's announcements (kept as reference in `_announcements/2026F_reference/`).
- Planned GitHub repo (not created yet; needs Davi's go-ahead, because it is public):
  `davi-moreira/2027S_predictive_analytics_QM474`, Pages from `main` / `docs`.
- Review plan of record (in the Fall repo, gitignored):
  `../2026F_predictive_analytics_QM474/_adm/doctrine_drafts/2026-10-26_amendment1_course_review/AMENDMENT1_COURSE_REVIEW_PLAN.md`;
  open decisions tracked in the Fall private tracker, task #56.

---

## 1. Decisions taken for this edition (Davi, 2026-10-27)

| Topic | Decision |
|---|---|
| Meetings | Same as Fall: **Monday / Wednesday / Friday**, sections 001 + 002, WTHR 114 (correct room/time on Brightspace if they change). Mondays and Wednesdays carry the notebooks; Fridays are group-work days. |
| Conference | **Required:** every student presents at the **Spring Undergraduate Research Conference poster session, Tue Apr 13, 2027**. |
| Poster-to-Product | **Kept** at 5%, in the last three weeks; **funding to be confirmed** (the Daniels Experiential Learning Grant that funded Fall ends Dec 31, 2026). |
| Open review decisions (task #56) | **Left as visible placeholders** until Davi decides. Every affected spot carries `[[PENDING <id>: …]]` (greppable). |
| Already adopted, applied here | D1 (δ band), D5 (MedScreen AUC primary), D8 (role of uncertainty), **D11 (five folds everywhere)**, **D12 (after nb08, one 80/20 split, all work on `X_train`)**, Amendment 1 (`compare_paired`, four outcomes). |
| Milestone instructions | **PDFs** (as in HONR 464), one per milestone, in simple narrative and plain wording — not long Brightspace pages. Brightspace carries a short assignment note plus the PDF. |

Weights stay as in Fall (Decision 13): Attendance 1% · Participation 4% · Quizzes 15% · Midterm 20% · Course Case
Competition 20% (peer evaluation 20% of it) · Final Project 35% (peer evaluation 20% of it) · Poster-to-Product 5%.

## 2. Calendar (Purdue Registrar, verified 2026-10-27)

- Classes **Mon Jan 11 – Sat May 1, 2027**; **MLK Day Mon Jan 18** (no class); **spring break Mon Mar 15 – Sat Mar 20**;
  final exams May 3–8 (no final exam in this course).
- Spring Undergraduate Research Conference **Apr 12–16, 2027**; **posters Tue Apr 13**. OURConnect: abstracts due
  **Mon Mar 1, 11:59 PM**; final abstract edits close **Mon Mar 22**; **mentor approval (Davi) by Wed Mar 24**.
- Honors: JMHC scholarly-project proposals due **Feb 1** (spring rule); Daniels coordinator decisions on the 4th
  Friday, **Fri Feb 5**; the student H-grade-mode / Daniels form deadline for Spring 2027 is **not published yet**
  (Spring 2026 was Mon Jan 26) — `[[PENDING honors-intake: check the Daniels Honors Contract page in early January]]`.
- PTS (accommodated midterm): students book 7 days ahead (**by Fri Feb 5**); instructor materials by noon
  **Thu Feb 11**; see `~/.claude/reference/purdue_testing_services_fall2026.md` (re-check the spring rules).

**How the term was laid out.** Fall 2026 is the template, week for week. Spring weeks 1–9 equal Fall weeks 1–9;
Spring week 10 is spring break; Spring weeks 11–16 equal Fall weeks 10–15. Every milestone keeps its Fall week of
term, so the final poster (M10) is due **Sun Apr 4**, nine days before the conference, exactly as in Fall
(Nov 8 → Nov 17). The extra Monday (Mar 1, Fall's fall-break Monday) becomes a group-work day.

**Single source of dates:** `scripts/build_2027S_calendar.py`. It writes `schedule.qmd`,
`_final_project/2027S/deadlines_2027S.csv` / `.md` (for Brightspace entry) and
`_announcements/2027S/upcoming_deadlines_and_key_dates.md`. Change a date there and re-run; never hand-edit those
outputs. Fall's due-date rules are kept: PAUSE-AND-DO participation on the lecture day; a Monday notebook's quiz on
Tuesday, a Wednesday's on Sunday; everything at 11:59 PM Eastern.

| Week | Mon | Wed | Fri |
|---|---|---|---|
| 1 (Jan 11) | nb00 | nb01 | nb02 |
| 2 (Jan 18) | *MLK Day* | nb03 | group work |
| 3 (Jan 25) | nb04 | nb05 | group work |
| 4 (Feb 1) | nb06 | nb07 | group work + **case competition kickoff** |
| 5 (Feb 8) | nb08 | nb09 | **MIDTERM** (Feb 12) |
| 6 (Feb 15) | nb11 | nb12 | group work |
| 7 (Feb 22) | nb13 | nb14 | group work |
| 8 (Mar 1) | group work | nb16 | group work |
| 9 (Mar 8) | nb18 | nb19 | group work |
| 10 (Mar 15) | *spring break* | *spring break* | *spring break* |
| 11 (Mar 22) | nb17 | group work | group work |
| 12–13 (Mar 29 – Apr 9) | group work | group work | group work |
| 14 (Apr 12) | group work · **Tue Apr 13 conference** | *no class (rest)* | P2P kickoff |
| 15 (Apr 19) | P2P | P2P | P2P |
| 16 (Apr 26) | P2P | **P2P showcase** | course wrap |

**Milestones** (Sunday, 11:59 PM): M00 + M01 Feb 7 · M02 Feb 14 · M03 Feb 21 · M04 + M05 Feb 28 (before the
Mar 1 abstract deadline) · M06 + M07 Mar 7 · M08 Mar 14 · M09 Mar 28 · M10 Apr 4 · M11 + M12 + M13 + peer
review Apr 11 · conference Tue Apr 13 · peer evaluation Fri Apr 30. Case competition: opens Fri Feb 5, team setup
Sun Feb 7, Kaggle final Sun Apr 25. Poster-to-Product: team product Mon Apr 26, showcase Wed Apr 28, individual
dashboard link Wed Apr 28. Meeting rounds: Round 01 — TA Feb 8–21, instructor Feb 22–28; Round 02 — TA Mar 8–14
and Mar 22–28, instructor Mar 29 – Apr 3.

## 3. What changes from Fall, and where

| Surface | Spring 2027 |
|---|---|
| Site (`_quarto.yml`, `index.qmd`, `syllabus.qmd`, `schedule.qmd`, `README.md`) | Re-dated for Spring; schedule generated; GitHub/Colab links point to the 2027S repo. |
| Official syllabus (Word) | `_syllabus/2027S/` — **Davi edits the official docx**; the website follows it (syllabus of record rule). A Spring copy of the Fall docx is the starting point; the list of changes is §5. |
| Milestones | `_final_project/2027S/milestones/` — one Markdown source + one PDF per milestone, simple narrative, built by `scripts/build_milestone_pdfs.py`. |
| Deadlines | `_final_project/2027S/deadlines_2027S.csv` — every gradebook item with opens/due, ready to enter in Brightspace. |
| Announcements | `_announcements/2027S/` — Spring versions of every reusable Fall announcement (Fall-only events dropped and listed in its README). |
| Notebooks | Rollout of the review (task #56) happens **here**, instructor copy first, batch by batch (review plan §11). Not started. |
| Rules (`CLAUDE.md`, doctrine, audit script) | The D11/D12 rule texts (review plan §16.7) go in with the first converted notebook. |
| Instructor tab | `instructor.qmd` (gitignored) and a new private companion repo `…2027S…_instructor` — to create with the GitHub repo. |
| Course tasks | A private `2027S_predictive_analytics_QM474-tasks` companion for the course-tasks skill — to create with the GitHub repo. |

## 4. Placeholders for open decisions

Format: `[[PENDING <id>: short description]]`, so `grep -rn "\[\[PENDING" .` lists every open spot.
IDs follow task #56: D2, D3/R1, D4, D6-nb16, D7, R2, R7, R10, R12, HV-guardrail, MS-guardrail, rule-texts,
colab-grids, midterm-slot14, k5or10, plus edition facts (honors-intake, p2p-funding, ta-team, room-time,
competition-data).

## 5. Work list

| # | Task | Status |
|---|---|---|
| 1 | Seed the repo; keep the instructor-page scripts; Fall announcements as reference | done 2026-10-27 |
| 2 | Calendar source + generated schedule, deadlines sheet, deadlines announcement | done 2026-10-27 |
| 3 | Site: `_quarto.yml`, `index.qmd`, `syllabus.qmd`, `README.md`, `CLAUDE.md` mission, `.Rproj`, schedule handout builder | done 2026-10-27 |
| 4 | Announcements for Spring (`_announcements/2027S/`, README with send dates) | done 2026-10-27 — 9 converted, 5 templated, 5 dropped |
| 5 | Milestone PDFs (simple narrative) + `scripts/build_milestone_pdfs.py` | done 2026-10-27 — 19 PDFs, 1–2 pages each, dates checked against the CSV |
| 6 | Render the site locally; `git init`; first commit | done 2026-10-27 (local only, no remote) |
| 7 | Create the public GitHub repo + Pages, the private instructor and tasks companions | **waiting for Davi's go-ahead** |
| 8 | Official syllabus docx for Spring | Davi (Word) |
| 9 | Notebook rollout (review plan batches), quizzes, midterm banks, guides, Brightspace pages | after the decisions in task #56 |
| 10 | **Spring poster rubric** (`_final_project/2027S/rubric/`): the only rubric is Fall's, which still carries the per-model 95% interval and "k = 5/10" (criterion 5), notebook 08's three-outcome rule and the Fall transition note (criterion 6), "M09 due Nov 1", and "no test-set opening required" — all contradict the Spring PDFs | **next** |
| 11 | Where groups open their test set: the M08 PDF makes it the last step of M08, after the champion is named; M10 is the alternative | Davi to confirm |

## 6. Questions for Davi raised while building (2026-10-27)

From the announcement conversion (`_announcements/2027S/README.md` has the full table and suggested send dates):
1. **Signature.** The drafts end "All the best, Davi" (as the Fall deadlines announcement does); some posted Fall messages were signed "Prof. Moreira". Which one?
2. **M05 grading.** The deadline sheet says *completion* (as Fall's milestone reference did), but Fall actually graded M05 with a rubric and a 20% revision window. Keep the rubric + revision for Spring?
3. **Round 02 instructor meetings.** The plan says Mar 29 – Apr 3 (Fall reference: Nov 2–7); a posted Fall announcement said "through Nov 13", whose Spring equivalent is Fri Apr 9. Which end date?
4. **Online sessions.** Fall ran some sessions online. Do Fri Mar 12 (before spring break) and Fri Apr 16 (P2P kickoff) meet online?
5. **P2P study reflections.** Fall's pre-conference and kickoff reflections were items of the P2P research study; they are not in the Spring sheet. Does the study run again?
6. **Honors order.** The JMHC spring proposal deadline (Mon Feb 1) comes before H1 (Sun Feb 7); the syllabus now asks for an H1 draft first (`[[PENDING honors-jmhc]]`).
