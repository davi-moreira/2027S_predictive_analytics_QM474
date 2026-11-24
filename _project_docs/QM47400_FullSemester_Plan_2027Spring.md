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
- GitHub (created 2026-10-28): public `davi-moreira/2027S_predictive_analytics_QM474`, Pages from `main` / `docs`
  at https://davi-moreira.github.io/2027S_predictive_analytics_QM474/; private companions
  `davi-moreira/2027S_predictive_analytics_QM474_instructor` (instructor mirror) and
  `davi-moreira/2027S_predictive_analytics_QM474-tasks` (course-tasks tracker).
- Review plan of record (in the Fall repo, gitignored):
  `../2026F_predictive_analytics_QM474/_adm/doctrine_drafts/2026-10-26_amendment1_course_review/AMENDMENT1_COURSE_REVIEW_PLAN.md`;
  open decisions tracked in the Fall private tracker, task #56.

---

## 1. Decisions taken for this edition (Davi, 2026-10-27)

| Topic | Decision |
|---|---|
| Meetings | Same as Fall: **Monday / Wednesday / Friday**, sections 001 + 002, WTHR 114 (correct room/time on Brightspace if they change). Mondays and Wednesdays carry the notebooks; Fridays are group-work days. |
| Conference | **Required:** every student presents at the **Spring Undergraduate Research Conference poster session, Tue Apr 13, 2027**. |
| Poster-to-Product | **Kept** at 5%, **Wed Apr 14 – Fri Apr 30** (two weeks, seven sessions), on Purdue's no-cost AI tools (Google Antigravity + Microsoft 365 Copilot Chat); no paid seats by default (2026-11-24). Plan of record: `_adm/_qm474_poster_product/2027S/P2P_PLAN_2027S.md`. |
| Open review decisions (task #56) | **Left as visible placeholders** until Davi decides. Every affected spot carries `[[PENDING <id>: …]]` (greppable). |
| Already adopted, applied here | D1 (δ band), D5 (MedScreen AUC primary), D8 (role of uncertainty), **D11 (five folds everywhere)**, **D12 (after nb08, one 80/20 split, all work on `X_train`)**, Amendment 1 (`compare_paired`, four outcomes). |
| Milestone instructions | **PDFs** (as in HONR 464), one per milestone, in simple narrative and plain wording — not long Brightspace pages. Brightspace carries the PDF as an attachment and **nothing in the assignment body** (Davi, 2026-11-24); external forms are link attachments. |

Weights (changed 2026-11-24, §7): **Attendance 5%** · Participation 4% · **Quizzes 11%** · Midterm 20% · Course Case
Competition 20% (peer evaluation 20% of it) · Final Project 35% (peer evaluation 20% of it) · Poster-to-Product 5%.
(Fall, Decision 13: Attendance 1%, Quizzes 15%.)

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
| 4 (Feb 1) | nb06 | nb07 | group work |
| 5 (Feb 8) | nb08 | nb09 | **MIDTERM** (Feb 12) |
| 6 (Feb 15) | nb11 | nb12 | group work |
| 7 (Feb 22) | nb13 | nb14 | group work |
| 8 (Mar 1) | nb16 | **nb18 (new: S&P 500 competition workflow) + competition kickoff** | group work |
| 9 (Mar 8) | nb19 | *virtual work session* | *virtual work session* |
| 10 (Mar 15) | *spring break* | *spring break* | *spring break* |
| 11 (Mar 22) | nb17 | group work | group work |
| 12–13 (Mar 29 – Apr 9) | group work | group work | group work |
| 14 (Apr 12) | group work · **Tue Apr 13 conference** | *no class (rest)* · P2P opens (Stage 0, on your own) | P2P kickoff |
| 15 (Apr 19) | P2P | P2P | P2P |
| 16 (Apr 26) | P2P Launch Day | **Demo Day I** | **Demo Day II** + course wrap |

**Milestones** (Sunday, 11:59 PM): M00 + M01 Feb 7 · M02 Feb 14 · M03 Feb 21 · M04 + M05 Feb 28 (before the
Mar 1 abstract deadline) · M06 + M07 Mar 7 · M08 Mar 14 · M09 Mar 28 · M10 Apr 4 · M11 + M12 + M13 + peer
review Apr 11 · conference Tue Apr 13 · peer evaluation Fri Apr 30. Case competition (changed 2026-11-24, §7): S&P 500
forecasting, opens Wed Mar 3, team setup Sun Mar 7, final forecast + code Fri Mar 26, live scoring Mar 29 – Apr 23,
standings Sun Apr 25. Peer evaluations: midpoint (formative) Sun Mar 7, final Fri Apr 30. Poster-to-Product: Launch Package Mon Apr 26, Demo Days Wed Apr 28 and Fri Apr 30, individual
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
| Notebooks | Rollout of the review **done 2026-11-24** (§7): instructor copy first, every notebook executed headless and gated by three parallel sessions; Colab "Run all" still to do (`notebooks/COMPLETION_STATUS.md`). |
| Rules (`CLAUDE.md`, doctrine, audit script) | The D11/D12 rule texts (review plan §16.7) go in with the first converted notebook. |
| Instructor tab | `instructor.qmd` (gitignored) links to the private mirror `2027S_predictive_analytics_QM474_instructor`, which now also carries the case-competition solution notebooks (`case_competition/`). Its content is still Fall's (tracker #5). |
| Course tasks | Private `2027S_predictive_analytics_QM474-tasks` (label `course-task`), seeded 2026-10-28 with tasks #1–#15. |

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
| 7 | Create the public GitHub repo + Pages, the private instructor and tasks companions | done 2026-10-28 — student-data paths and the competition solution notebooks gitignored before the first push; instructor mirror synced; tracker seeded |
| 8 | Official syllabus docx for Spring | Davi (Word) — tracker #4 |
| 9 | Notebook rollout (review plan batches), quizzes, midterm banks, guides, Brightspace pages | **done 2026-11-24** with the review plan's defaults for the open decisions (§7); quiz banks of record `_quizzes/2027S/`; Colab "Run all" and Davi's confirmation of the defaults remain — tracker #3 |
| 10 | **Spring poster rubric** (`_final_project/2027S/rubric/`): the only rubric is Fall's, which still carries the per-model 95% interval and "k = 5/10" (criterion 5), notebook 08's three-outcome rule and the Fall transition note (criterion 6), "M09 due Nov 1", and "no test-set opening required" — all contradict the Spring PDFs | **next** — tracker #2 |
| 11 | Where groups open their test set: the M08 PDF makes it the last step of M08, after the champion is named; M10 is the alternative | Davi to confirm — tracker #1 |

The tracker (`davi-moreira/2027S_predictive_analytics_QM474-tasks`) also holds the term-launch tasks that have no row
here: room and times #6, TA team #7, Brightspace #8, announcements #9, competition #10, midterm logistics #11,
honors dates #12, P2P funding #13, OURConnect approvals #14 and lecture briefings #15.

## 6. Questions for Davi raised while building (2026-10-27)

Tracked as tracker #1, with two more: the test-set step (work-list item 11) and the P2P professional review panel
(`[[PENDING p2p-review]]`).

From the announcement conversion (`_announcements/2027S/README.md` has the full table and suggested send dates):
1. **Signature.** The drafts end "All the best, Davi" (as the Fall deadlines announcement does); some posted Fall messages were signed "Prof. Moreira". Which one?
2. **M05 grading.** The deadline sheet says *completion* (as Fall's milestone reference did), but Fall actually graded M05 with a rubric and a 20% revision window. Keep the rubric + revision for Spring?
3. **Round 02 instructor meetings.** The plan says Mar 29 – Apr 3 (Fall reference: Nov 2–7); a posted Fall announcement said "through Nov 13", whose Spring equivalent is Fri Apr 9. Which end date?
4. **Online sessions.** Fall ran some sessions online. Do Fri Mar 12 (before spring break) and Fri Apr 16 (P2P kickoff) meet online?
5. **P2P study reflections.** Fall's pre-conference and kickoff reflections were items of the P2P research study; they are not in the Spring sheet. Does the study run again?
6. **Honors order.** The JMHC spring proposal deadline (Mon Feb 1) comes before H1 (Sun Feb 7); the syllabus now asks for an H1 draft first (`[[PENDING honors-jmhc]]`).

## 7. Decisions of 2026-11-24 (Davi) and the setup they started

Davi asked for the course to be set up end to end and answered four questions the same day. The work was split
across parallel Claude Code sessions sharing this folder; the contract (decisions, file ownership, rules,
reports) is `_adm/2027S_setup_2026-11-24/COORDINATION.md`, and each session's report lands in
`_adm/2027S_setup_2026-11-24/reports/`.

| # | Decision | Where it lives |
|---|---|---|
| 1 | **Correct every notebook and Brightspace page** to the Amendment 1 doctrine and the review plan of record; open review decisions default to the plan's own recommendations (D2 ladder, D3 nominee, D4/Amendment 2 no per-model interval, D6 nb16 descriptive, D7 fixes, R1 nominee labelled optimistic, R7 CV+ where in core, R12 one margin required and the band optional) | sessions `rollout-core` (nb08, nb09, nb14, nb17, rule texts, midterm banks), `rollout-trees` (nb11–nb13), `rollout-early` (nb00–nb07, nb19), `sp500-competition` (nb16) |
| 2 | **Attendance 5%**, location-verified iClicker; **Quizzes 15% → 11%** | `syllabus.qmd`, `README.md`, honors table; instructor guide `_adm/_brightspace/2027S/ICLICKER_ATTENDANCE_SETUP.md` (confirm Purdue's 2026–27 iClicker license first) |
| 3 | **Course Case Competition → group S&P 500 forecasting competition on Kaggle** (replaces Bank Churn; same 20%, same teams), with a **new nb18** and an nb16 that covers usable forecasting models | session `sp500-competition`; calendar items and syllabus text here |
| 4 | **Weeks 8–9:** nb16 Mon Mar 1, nb18 Wed Mar 3, nb19 Mon Mar 8; **Wed Mar 10 and Fri Mar 12 virtual** | `scripts/build_2027S_calendar.py` (kind `virtual`) |
| 5 | **Two peer evaluations:** midpoint, formative (completion; flags trigger a team check-in), Sun Mar 7; final, graded, Fri Apr 30 | calendar; `peer_evaluation_midpoint.md` (new PDF), `peer_evaluation.md` |
| 6 | **No poster first draft (M09), no conference** | syllabus, M09, conference and overview PDFs, announcements |
| 7 | **A presentation at every meeting** (about five slides, five minutes; uploaded before the meeting; every member presents in each round; no presentation = the meeting does not count) | M00, M04, M07, M13 PDFs (M04 opens Feb 8, M13 Mar 8), overview, syllabus |
| 8 | **Poster-to-Product kept, adapted from the Fall 2026 Launch Journey**, without assuming Claude seats (Purdue-provided AI options) | session `p2p-spring` |
| 9 | **AI-avatar videos: pilot nb00 and nb08 first** (ElevenLabs + HeyGen, the Fall pipeline), then decide | session `video-pilot` |
| 10 | Help set up Brightspace | session `brightspace-build` (plan + specs; live changes only with Davi's OK, hidden items only) |

Also fixed while there: the syllabus's midterm format (now 15 questions × four alternatives, about 3 minutes each,
Decision 16); M06/M08/M09 placeholders D4, D3/R1, R12, R7 resolved with the defaults above.

**Changes Davi still makes in the official Word syllabus** (the source of record): see
`_syllabus/2027S/SYLLABUS_DOCX_CHANGES_2026-11-24.md`.

