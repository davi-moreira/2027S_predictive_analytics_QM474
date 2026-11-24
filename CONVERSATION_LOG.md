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

## 2026-10-28 — Fall 2026 student-reported errata carried over

The Fall repo corrected student-reported errors in nb02, nb06 and nb07 and in the NB06/NB07 quiz banks
(NB06 Q23, Q24, Q27–Q30; NB07 Q19 now follow the benign-positive convention). The Spring copies were
byte-identical to Fall's originals, so the corrected files were copied over: three student notebooks
(`5a3db67`), plus the gitignored instructor notebooks, nb06/nb07 video guides and quiz banks (audit PASS),
synced to the private instructor mirror.

## 2026-11-24 — Spring 2027 setup in one push: rollout, competition, grading, P2P, videos, Brightspace (Claude Code, main + seven parallel sessions)

Davi asked for the course to be set up end to end, with sub-sessions, working non-stop. Contract for the parallel
sessions (decisions, file ownership, rules): `_adm/2027S_setup_2026-11-24/COORDINATION.md`; each session's report is in
`_adm/2027S_setup_2026-11-24/reports/`. Record of decisions: `_project_docs/QM47400_FullSemester_Plan_2027Spring.md` §7;
`DECISIONS.md` 17–19.

- **Davi's answers (same day):** Attendance 1% → **5%**, taken from **Quizzes 15% → 11%**; the Course Case Competition
  becomes a **group S&P 500 forecasting competition** replacing Bank Churn, with a **new nb18**; **nb16 Mon Mar 1, nb18
  Wed Mar 3, nb19 Mon Mar 8, Wed Mar 10 and Fri Mar 12 virtual**; the **midpoint peer evaluation is formative**
  (Sun Mar 7) and the final one graded (Fri Apr 30); **pilot two avatar videos first** (nb00, nb08); adapt P2P from
  the Fall 2026 version as run. Also: a **presentation at every TA/instructor meeting**; **no M09 poster draft = no
  conference**. Later in a side session: **Brightspace instructions only as an attached PDF**; peer evaluations on Qualtrics.
- **Model-comparison rollout (sessions rollout-core, rollout-trees, rollout-early, sp500-competition):** all 18
  notebooks converted to Amendment 1/2 + D11/D12, instructor first, executed headless, gates clean
  (`audit_cv_first.py` RESULT: PASS with the new data-roles check; nb18 is no longer an authorized test-set use).
  Open review decisions defaulted to the plan's recommendations (D2, D3, D4, D6, D7, R1, R7, R12) — tracker #18 to
  confirm. Champions as executed: MedScreen `LogisticRegression(C=1)` (robust); HomeValue the default random forest
  (tuned GBM unresolved, margin-sensitive at δ = 0.005). nb07 gains Brier + reliability (Section 6); nb19 compares an
  MLP with the nb14 champions via `compare_paired`. Guides, Brightspace pages, rule files (CLAUDE.md, doctrine,
  DECISIONS 14 addendum, 17, 18, 19, template, troubleshooting, workflow.qmd) updated. Quiz banks of record now
  `_quizzes/2027S/` (16 masters, 460 questions, all 62 files PASS). Midterm banks: rollout-core pass (see its report §6).
- **Competition (sp500-competition):** `_course_case_competition/2027S/` — quantile forecasts of cumulative log returns
  at 1/5/10/15/20 trading days, scaled pinball loss vs random walk; Kaggle cannot rescore after launch, so Kaggle hosts an
  ungraded practice round and the live round (Mar 29 – Apr 23) is host-scored; FRED not used (its terms bar ML use).
  Grade 15 live forecast · 45 method notebook · 20 memo · 20 peer. Instructions PDF built. Codex partner run stopped
  on credits (salvaged, verified).
- **Poster-to-Product (p2p-spring):** Purdue gives students Google Antigravity, Microsoft 365 Copilot Chat and GenAI
  Studio at no cost; Spring P2P builds on those, no paid seats by default. Launch Sprint Wed Apr 14 – Fri Apr 30, Round
  03 Sprint Reviews with a team presentation, Demo Days Apr 28 and Apr 30; 12 P2P gradebook items in the calendar.
  Plan `_adm/_qm474_poster_product/2027S/P2P_PLAN_2027S.md`.
- **Main session:** calendar (`build_2027S_calendar.py`: 77 items, 18 key dates), syllabus (weights, iClicker policy,
  competition, peer evaluations, presentations, gate, P2P, midterm format 15 × 4), 20 milestone PDFs + new
  `peer_evaluation_midpoint`, announcements, README, Instructor page (competition + quiz sections), Word-syllabus change
  list `_syllabus/2027S/SYLLABUS_DOCX_CHANGES_2026-11-24.md`, iClicker guide `_adm/_brightspace/2027S/ICLICKER_ATTENDANCE_SETUP.md`
  (Purdue's 2026–27 student license unconfirmed — tracker #16), planning docs (subagent). Site rendered and pushed (`f12f27a`).
- **Brightspace (brightspace-build):** plan + generated specs only (Davi: "plan only for now");
  `_adm/_brightspace/2027S/BRIGHTSPACE_BUILD_PLAN_2027S.md`.
- **Videos (video-pilot):** voice-only drafts for nb00 and nb08 (overviews + Colab walkthroughs), ≈ \$2.81 of voice
  credits; HeyGen waits on Davi's review — tracker #17 (HeyGen renews and the ElevenLabs key expires ~Dec 14).
- **Git:** the project's auto-commit Stop hook fired on every session stop and pushed intermediate states ("chore:
  Auto-commit", d31d45d …); no solution leaked (checked). A 4th pre-commit check now refuses any staged
  `*_student.ipynb` containing `INSTRUCTOR SOLUTION` (`.git/hooks/pre-commit` + copy of record). Whether to pause the
  hook during parallel work is Davi's call.
- **Tracker:** comments on #1–#5, #8–#11, #13; #10 re-titled and re-dated (2027-03-02); new #16 (iClicker license),
  #17 (videos before Dec 14), #18 (confirm the defaults), #19 (Colab Run all).
- **Midterm banks (rollout-core subagent, late 2026-11-24):** all 14 forms of `_midterm_exam/2026F/` brought to
  Amendment 1/2 for the Fri Feb 12, 2027 sitting. Slot 13 now gives the five per-fold gains, the `compare_paired`
  interval and the declared margin, and is keyed by the four outcomes. Slot 12 is keyed to fold mean ± SD, with no
  per-model interval. Slot 14 (7 forms re-keyed): the grid winner is a nominee that faces the default. Main recomputed
  all 14 slot-13 intervals independently (all match) and re-ran the gates: item_lint 0 FAIL, validate_banks 0
  failures, check_exam_structure and check_pdfs PASS, answer length PASS on 14 + 3 practice CSVs, option cues PASS.
  Open for Davi: slot 4 on NeuroLogic, NovaCure and TelcoBoost still keys "compare on the validation set"; a blind
  solve of slots 12–15 before printing (Codex was unavailable). Full list:
  `_midterm_exam/2026F/_rewrite/2027S_REVISION_2026-11-24.md`.
- **Instructor repo synced** (`c971511` in the private companion): 20 notebooks, 23 Brightspace pages, 21 guides,
  142 quiz CSVs, 14 midterm cases.
