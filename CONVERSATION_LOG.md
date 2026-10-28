# Conversation Log — QM47400 Predictive Analytics, Spring 2027

Append-only. The Fall 2026 history lives in `../2026F_predictive_analytics_QM474/CONVERSATION_LOG.md`.

## 2026-10-27 — Edition started (Claude Code session from the Fall repo)

- **Davi's decisions for this edition:**
  - Same Mon/Wed/Fri pattern as Fall.
  - The Spring Undergraduate Research Conference is required (posters Tue Apr 13, 2027).
  - Poster-to-Product is kept, with funding to be confirmed.
  - Open review decisions stay as `[[PENDING …]]` placeholders.
  - Milestone instructions become PDFs in plain narrative.
  - All updates from the Fall course-material review are applied here.
- **Seeded** from the 2026F repo with `rsync`. Left out: history, renders, media, the private mirror, the archive, the administered midterm, and Fall's admin and announcements. Kept: `_adm/_instructor_page/`; Fall announcements as `_announcements/2026F_reference/`.
- **Calendar:** Purdue Spring 2027 is Jan 11 – May 1 (MLK Day Jan 18; spring break Mar 15–20). Verified on the Registrar page; the conference dates and the OURConnect Mar 1 abstract deadline come from the URC pages.
  - Fall is laid onto Spring week for week, with spring break inserted at week 10.
  - The final poster is due Sun Apr 4.
  - `scripts/build_2027S_calendar.py` is the single source of dates. It writes `schedule.qmd`, `_final_project/2027S/deadlines_2027S.csv`/`.md` (65 gradebook items) and the deadlines announcement.
- **Site:** re-dated `_quarto.yml`, `index.qmd`, `syllabus.qmd` (honors dates as placeholders; JMHC Feb 1 comes before H1), `README.md`, the `CLAUDE.md` mission, and the schedule-handout builder. Rendered locally; the Instructor page is sealed.
- **Announcements:** `_announcements/2027S/` holds 9 converted, 5 templated and 1 generated file; 5 Fall-only messages were dropped. The README there gives suggested send dates.
- **Milestone PDFs:** `_final_project/2027S/milestones/` has 19 PDFs (M00–M13, overview, peer review, conference, peer evaluation, Poster-to-Product). They are built by `scripts/build_milestone_pdfs.py` (pandoc → Typst), which checks dates against the CSV.
- **Open:**
  - Create the public GitHub repo + Pages and the private instructor/tasks companions; this needs Davi's go-ahead.
  - The Spring poster rubric.
  - Davi edits the official syllabus docx (`_syllabus/2027S/`).
  - The six questions in plan §6.
  - The notebook rollout after task #56's decisions.

## 2026-10-28 — GitHub repos, Pages and private companions (Claude Code, Davi's go-ahead)

- **Public repo:** `davi-moreira/2027S_predictive_analytics_QM474`, pushed. Pages serves `main` / `docs` at https://davi-moreira.github.io/2027S_predictive_analytics_QM474/ (HTTPS enforced). The Instructor page is served encrypted.
- **Pre-publish check:**
  - No commit contains the instructor password, the plaintext instructor page or `_adm/`.
  - No tracked text file contains a Fall 2026 roster name.
  - Student-data paths (grade exports, leaderboards) and the case-competition solution notebooks are gitignored and are not in the history.
- **Private instructor mirror:** `davi-moreira/2027S_predictive_analytics_QM474_instructor`, synced with 20 instructor notebooks, 21 guides, 96 quiz CSVs, 14 midterm cases, the Brightspace pages and the case-competition solution notebooks. The last of these are new: the sync now copies `_course_case_competition/**/*_instructor*.ipynb` to `case_competition/`. The sync script, the pre-commit hook (re-installed) and the Instructor tab now point at the 2027S repos.
- **Private tracker:** `davi-moreira/2027S_predictive_analytics_QM474-tasks` (label `course-task`), seeded with 15 setup tasks, #1–#15:
  - setup questions #1, rubric #2, review rollout #3, syllabus #4, Instructor tab #5;
  - room and times #6, TA team #7, Brightspace #8, announcements #9, competition #10;
  - midterm logistics #11, honors dates #12, P2P funding #13, OURConnect approvals #14, lecture briefings #15.

  Fall tracker #56 links to #2 and #3.
- **Links updated** to the 2027S repos in `CLAUDE.md`, `_project_docs/NOTEBOOK_TEMPLATE.md`, `TROUBLESHOOTING.md` and `COURSE_MATERIAL_WORKFLOW.md`.
- **Still open:**
  - The notebooks' Colab badges still point at the 2026F repo (rollout, #3).
  - The Instructor tab's content is still Fall's (#5).
