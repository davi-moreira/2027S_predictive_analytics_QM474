# 2026 Fall Predictive Analytics — AI Assistant Guide

This file documents the rules and workflows that change Claude's behavior in this repository. Reference material lives in linked files — read those when relevant, not by default.

## Project Mission

**QM47400 — Predictive Analytics**, a full-semester course for Purdue's Daniels School of Business, **Spring 2027** (Jan 11 – Apr 30, 2027). In-person **Monday / Wednesday / Friday** class meetings, with the course's micro-videos (≤12 min) and Google Colab notebooks as the hands-on spine. Pedagogy: Concept → Demo → PAUSE-AND-DO Practice → Solution → Repeat.

**This edition is where the Fall 2026 course-material review is applied.** The repo was seeded from `../2026F_predictive_analytics_QM474` on 2026-10-27; the Fall review plan of record is `../2026F_predictive_analytics_QM474/_adm/doctrine_drafts/2026-10-26_amendment1_course_review/AMENDMENT1_COURSE_REVIEW_PLAN.md`, and its open decisions are task #56 in the Fall private tracker. Until a notebook is converted, the notebooks and the rule sections below still describe the Fall 2026 material. Spots that wait on an open decision carry `[[PENDING <id>: …]]` (find them with `grep -rn "\[\[PENDING" .`).

The same **18-notebook arc (nb00–nb09, nb11–nb14, nb16–nb19; nb10, nb15 and nb20 retired)** is paced across 16 weeks. **Mondays and Wednesdays carry the notebook content; Fridays are Group Work sessions for the final project and the Course Case Competition** — the only Friday with a notebook is Fri Jan 15 (nb02), and **Fri Feb 12 hosts the in-class paper Midterm Exam**. Anchors: **MLK Day Mon Jan 18** and **spring break Mar 15–20** (no class); the last **lecture** is **nb17 on Mon Mar 22**; the **Spring Undergraduate Research Conference poster presentation is Tue Apr 13** (all students present; poster due Sun Apr 4; OURConnect abstracts due Mon Mar 1); the post-poster **Poster-to-Product** sprint runs **Fri Apr 16 – Wed Apr 28** (funding to be confirmed); the course wraps Fri Apr 30.

**Every Spring 2027 date lives in `scripts/build_2027S_calendar.py`**, which writes `schedule.qmd`, the Brightspace deadline sheet `_final_project/2027S/deadlines_2027S.csv` and the deadlines announcement. Change dates there and re-run; never hand-edit those outputs. **Milestone instructions are PDFs** (simple narrative) in `_final_project/2027S/milestones/`, built by `scripts/build_milestone_pdfs.py`.

**Assessment weights (unchanged from Fall, Decision 13):** Attendance 1% · Participation 4% · Quizzes 15% · **Midterm Exam 20%** · Course Case Competition 20% (peer evaluation is 20% of that) · Final Project 35% (peer evaluation 20% of that) · Poster-to-Product 5% (peer evaluation 20% of that). No final exam.

- **Instructor:** Professor Davi Moreira — office hours on Brightspace
- **Meetings:** Sections **001 and 002**, Monday / Wednesday / Friday, **WTHR 114** (confirm on Brightspace)
- **Prerequisite:** MGMT 305 Business Analytics or similar
- **Repository (planned, not yet created):** https://github.com/davi-moreira/2027S_predictive_analytics_QM474
- **Website (planned):** https://davi-moreira.github.io/2027S_predictive_analytics_QM474/
- **Deployment:** Quarto → `docs/` → GitHub Pages
- **Edition plan:** `_project_docs/QM47400_FullSemester_Plan_2027Spring.md`
- **Official syllabus:** `_syllabus/2027S/` (gitignored Word file, edited by Davi) is the **source of record for course policy** — when it disagrees with `syllabus.qmd`, the website is what gets fixed.

## See Also (Reference Files)

| File | When to read |
|---|---|
| `_project_docs/COURSE_MATERIAL_WORKFLOW.md` | Producing a notebook's full material set end-to-end — notebook → videos → Brightspace page → NotebookLM splits → quizzes (the per-notebook production pipeline + dependency order) |
| `_project_docs/NOTEBOOK_TEMPLATE.md` | Creating or restructuring a notebook — full 8-section templates |
| `_project_docs/SYLLABUS_OF_RECORD_2026F.md` | Any question about official course policy, dates, weights, office hours, extra credit — and the open discrepancy register |
| `_project_docs/DECISIONS.md` Decision 15 | Anything touching the **honors contract** — deliverables, weights, deadlines, the two generated .docx artifacts |
| `_project_docs/DECISIONS.md` | Before proposing changes to conventions (seeds, splits, format) |
| `_project_docs/TROUBLESHOOTING.md` | Render fails, GitHub Pages stale, Colab errors, leaked solutions |
| `CONVERSATION_LOG.md` | Project history and prior decisions |
| `_project_docs/QM47400_FullSemester_Plan_2027Spring.md` | The Spring 2027 edition plan (calendar, decisions, work list); the Fall plan `MGMT47400_FullSemester_Plan_2026Fall.md` stays for the sequencing rationale |
| `_project_docs/claude_course_plan.md` | Implementation plan with notebook-content justification |
| `scripts/audit_cv_first.py` | Run before every commit in nb09–nb19 |
| `scripts/voice_check_guides.py` | Run before every video-guide edit |
| `scripts/audit_answer_length.py` | Run before importing ANY quiz/exam CSV to Brightspace (MC answer-length cue gate) |
| `_midterm_exam/2026F/README.md` | Working on the paper midterm — 15 x 4 banks (authoring spec `STYLE_GUIDE_15x4.md`), CSVs, LaTeX sources, build script, PDFs, release gates; the Sep 25 sitting is archived in `archive/administered_2026-09-25/` |
| `scripts/_distractor_rewrite_instructions.md` | Authoring/rewriting MC distractors — the full length-parity spec |

**Canonical notebook reference:** `notebooks/nb01_eda_splits_student.ipynb`. Match its formatting exactly.

---

## 🚨 CRITICAL RULE — Voice and Audience in Student-Facing Content

**The student notebook is read BY students, not BY instructors who then teach it.** Every sentence in a student notebook — including Gemini prompts and "After running, verify" checklists — must be written **TO the student**, never ABOUT the student and never TO the instructor.

**Hard rules:**

1. **Never write "students" as a third-party noun inside a student-facing cell.** If the text says "so students see X", "help students understand Y", "when students run this", or "as students work through", it is wrong. Rewrite in second person (`you`), neutral imperative (`print X to see Y`), or first person (`I want to see X`).
2. **Gemini prompts are scripts the student copies into Gemini.** They must sound like something a student would actually type. *Wrong:* `"... print classification_report so students see the per-class breakdown."` *Right:* `"... print classification_report to show the per-class breakdown."`
3. **No instructor-voice, video-guide, or camera language in student cells.** Forbidden phrases in student notebooks: `"on camera"`, `"the instructor should"`, `"speaking prompt"`, `"you (the instructor)"`. Those belong only in `video_guides/NN_video_lecture_guide.md` (gitignored, instructor-facing).
4. **The video guide can reference students in the third person** — wrapper prose is read silently by the instructor, so "Students often ask…" is fine there. But **inside blockquote read-aloud scripts** (`> *"..."*`), the listener IS a student, so the student-notebook rule applies.

**Before shipping any edit to a student notebook**, grep for failure modes:

```bash
# Should return zero hits in any notebooks/*_student.ipynb (Student's t is the only OK match)
grep -iE '\bstudents?\b|\bthe instructor\b|on camera|speaking prompt' notebooks/nbNN_*_student.ipynb
```

**Before shipping any video-guide edit**, run the blockquote-only voice check:

```bash
python scripts/voice_check_guides.py video_guides/NN_video_lecture_guide.md
```

Hits in wrapper prose (lines not starting with `>`) are fine — only blockquote violations are flagged.

**The most common regression:** trailing `"so students see"` / `"so students understand"` in Gemini prompts. If you feel the urge to explain *why* Gemini should print something, say `"... to show the per-class breakdown"` — the justification is part of the prompt, not a side-note about the audience.

---

## 🚨 CRITICAL RULE — Narrative Polish Pattern (nb08 Style)

Every student-notebook markdown cell follows the nb08 narrative style. This is the course's voice. **Coverage is partial:** the pattern is applied from **nb08 onward** (nb08, nb09, nb11-nb14, nb16-nb19 each carry 7-17 Q&A blocks). **nb00-nb07 carry none yet** and are the outstanding backlog — check with `grep -c 'A question that often comes up' notebooks/nbNN_*_student.ipynb` before assuming a notebook is polished.

**Five structural elements every student notebook has:**

1. **Business-case "Why This Matters" cell** with a named stakeholder (HomeValue CFO, MedScreen chief medical officer, TechCorp People Analytics lead). The stakeholder's concern is phrased as a direct quote. This cell opens the analytical work and motivates every section below.
2. **Narrative prose over bullet lists** — "Reading the output" cells are paragraphs, not terse enumerations. A bullet list is a fallback when the structure is genuinely list-like (a rubric, a checklist); flowing prose is the default.
3. **Inline Q&A blocks** with the exact phrase **"A question that often comes up here"** (or "A question that often comes up at this point"). Placement: after each dense explanation, anticipate one specific student confusion and answer it in one paragraph. The phrase is grep-findable for tooling. **Format (nb09 convention — load-bearing, do not deviate):**

   ```markdown
   > **A question that often comes up here:** *"<student question in double quotes>"* <single paragraph of flowing prose — concrete examples, decision rules, named stakeholders where relevant; no bullets, no nested lists, no headers>.
   ```

   Four required elements: (1) `>` blockquote prefix; (2) `**A question that often comes up here:**` (or `at this point:`) as a bolded opener ending in a colon; (3) italicized question in double quotes: `*"..."*`; (4) answer body as one flowing paragraph in the same blockquote. If the answer needs to enumerate options, fold them inline as `(1) ..., (2) ..., or (3) ...` rather than breaking out a numbered list — the single-paragraph shape is part of the convention. To retrofit older inline-paragraph Q&As to this format, run `python scripts/qa_format_to_nb09.py <notebook>` — it is idempotent.
4. **Section bridges** that explicitly name the transition: *"Section 2 landed the regression estimate with a tight CI. Now apply the identical four steps to the classification problem."* Never jump between sections without a one-sentence bridge.
5. **Warm wrap-ups with next-notebook bridges** — the "Wrap-Up" cell ends with a paragraph naming the next notebook and what it builds on today's work. Often carries one closing Q&A.

**When polishing is warranted:**
- Any new markdown cell longer than ~150 words in a student notebook.
- Any "Reading the output" cell currently a bullet list.
- Any abrupt section transition.
- Any "Why This Matters" cell lacking a named stakeholder.

**Idempotent polish helper** (the pattern used across every NB polish batch):

```python
def append_qa_if_missing(nb, signature_prefix, qa_block):
    for c in nb['cells']:
        if c['cell_type'] != 'markdown':
            continue
        src = ''.join(c['source'])
        if not src.lstrip().startswith(signature_prefix):
            continue
        if 'A question that often comes up' in src:
            return False  # already has Q&A — idempotent
        stripped = src.rstrip()
        if stripped.endswith('---'):
            stripped = stripped[:-3].rstrip()
        c['source'] = [stripped + '\n\n' + qa_block + '\n\n---\n']
        return True
    return False
```

The idempotent check (`if 'A question that often comes up' in src`) is critical — it prevents duplicating Q&As on re-runs.

**Batching rule:** polish in groups of 2–3 notebooks per commit. Polish + voice-check + render + commit per batch. Keeps commit messages meaningful and docs rendering in sync.

---

## 🚨 CRITICAL RULE — CV-First Evaluation + Test-Set Lock

**From nb09 onward, all model-performance claims come from cross-validation.** Before nb14, the test set (`X_test`, `y_test`) is *locked* — no model evaluation touches it. nb14's "Opening the Locked Test Set" ceremony is the only authorized test-set opening in the course. It runs **once per spine** — one ceremony for the classification business case, one for the regression business case — and each test set opens exactly once. The singleness rule holds per case; it is not diluted across spines.

| Where | What to use |
|---|---|
| nb01–nb07 | Single train/val/test split is introduced; `X_val` for mid-course evaluation |
| nb08 | k-fold CV + Student's *t* **descriptive** \~95% interval becomes the course's evaluation spine (see the CV-inference doctrine below) |
| nb09–nb13, nb16, nb17 | `cross_val_score`, `cross_val_predict`, `GridSearchCV`, `RandomizedSearchCV` on `X_train`; held-out evaluation uses `X_val`, never `X_test` |
| **nb14 cells 30 + 34 ONLY** | `X_test` / `y_test` opened for the one-shot ceremony (INSIDE/ABOVE/BELOW verdict) — cell 30 is the **classification** spine, cell 34 the **regression** spine; one opening per business case |
| nb18 | `X_test` may appear in the Kaggle-submission demo (production-pipeline pattern, not model evaluation) |

**The CV-first principle is not a style preference; it is the course's pedagogical spine.** nb14's ceremony loses its meaning if the test set has been touched 30 times before students get there.

**Before shipping any evaluation code in nb09–nb19**, run the audit:

```bash
python scripts/audit_cv_first.py
```

The only acceptable output is hits in `nb14` cells 30 + 34 (one per spine) plus `nb18`'s Kaggle-submission demo. Anything else is a regression and must be fixed before commit.

**Common CV-first patterns to reach for:**

- Classifier comparison: `cross_val_score(model, X_train, y_train, cv=StratifiedKFold(5, ...), scoring='roc_auc')`, then report `mean ± (t_crit * sd / sqrt(k))` as an **approximate 95% interval** — descriptive, since the folds share training rows. **Model-vs-model verdicts come from paired per-fold differences on identical folds, read from the fold-corrected interval `mean(d) ± t·sd(d)·√(1/k + 1/(k−1))` against a predeclared margin — never from whether two marginal intervals overlap, from fold signs alone, or from either model's own interval lower bound** — the full rule, its four outcomes (Amendment 1, 2026-10-26), and its authoring rules are binding in `_project_docs/CV_INFERENCE_DOCTRINE.md`.
- `classification_report` on held-out predictions: `y_pred = cross_val_predict(model, X_train, y_train, cv=cv_strat)` — every prediction comes from a fold that never saw it during fitting.
- Permutation importance that would otherwise touch `X_test`: split `X_train` further (e.g., 75/25 inside the cell), fit on the 75% slice, measure permutation importance on the 25% slice. Test set stays locked.
- Calibration that needs a held-out sample: use `CalibratedClassifierCV(base, cv=5)` fit on `X_train` (internal CV handles the calibrator fit), evaluate Brier on `X_val`.

---

## 🚨 CRITICAL RULE — MC Option-Length Parity (Quizzes and Exams)

**The correct answer must not be identifiable by its length or elaboration.** This actually happened in the 2026Summer offering: correct options were authored as full decisions-with-rationale while distractors stayed terse one-liners. Students discovered that "always pick the longest option" scored \~100% (correct-is-longest in 96% of quiz questions and 99.5% of midterm questions vs. 25% chance — hypothesis-tested at p < 10⁻¹²³; see `_project_docs/DECISIONS.md` Decision 11). All inherited banks were rewritten on 2026-06-12; this rule keeps it fixed.

**Hard rules for every multiple-choice question (quizzes and any future exam):**

1. **Every option ≥ 60% of the length of that question's longest option.** (Quizzes and the paper midterm both use **four options** — the midterm since its 2026-10-07 rewrite to 15 x 4, Decision 16; the Sep 25, 2026 sitting used five and is archived — so chance is 25% and the per-bank correct-is-longest budget is measured against that.) Distractors carry their own flawed-but-specific rationale at the same elaboration and connector-word density as the correct option — wrongness comes from a real misconception, never from brevity, vagueness, or "always/never" tells.
2. **Per bank, the correct option is strictly longest in ≤ 40% of questions** (target \~25%, chance). Vary the correct option's length rank — it must land at longest, middle, and shortest across the bank, and the longest option's position must vary.
3. **Full authoring spec:** `scripts/_distractor_rewrite_instructions.md` (also embedded in the quiz and midterm generation plans, §4.5 and §5.6).

**Before importing ANY quiz or exam CSV to Brightspace**, run the gate — PASS is mandatory:

```bash
python scripts/audit_answer_length.py --file <path-to-csv>   # per-bank gate (PASS/FAIL)
python scripts/audit_answer_length.py                        # corpus-wide statistics
```

---

## 🚨 CRITICAL WORKFLOW — Instructor-First Editing (ALL material)

**The instructor artifact is always edited FIRST; the student-facing artifact is derived from it afterwards.** This is not a notebooks-only rule — it governs every paired surface in the course:

| Edit this first | Then update this from it |
|---|---|
| `notebooks/nbNN_*_instructor.ipynb` | `notebooks/nbNN_*_student.ipynb` |
| `video_guides/NN_video_lecture_guide.md` | the notebook prose it narrates |
| `instructor.qmd` (the gated **Instructor** tab) | the public pages that link into it |
| `_quizzes/`, `_midterm_exam/` banks + keys | the Brightspace import / printed student copy |
| `brightspace/NN_*.md` instructor-facing plan | the published module page |

After any of these, run `bash _adm/_instructor_page/scripts/sync_instructor_repo.sh` so the private companion repo matches. A student-facing file that changed without its instructor source changing first is a bug, not a shortcut.

**ALWAYS edit `notebooks/nbNN_*_instructor.ipynb` FIRST, then generate the student file.**

- The **instructor notebook** is the source of truth (gitignored, local only).
- The **student notebook** (`nbNN_*_student.ipynb`) is generated from the instructor notebook by deleting solution cells. Only the student file is committed.

**Generating the student notebook:**

1. Copy the instructor file: `cp notebooks/nbNN_*_instructor.ipynb notebooks/nbNN_*_student.ipynb`.
2. Delete all cells containing `INSTRUCTOR SOLUTION` in the student copy (markdown or code).
3. Update the Colab badge URL to match the student filename.
4. Update the video guide (`video_guides/NN_video_lecture_guide.md`).
5. Commit only the student notebook (instructor notebooks are gitignored).

**Marker conventions in the instructor notebook:**

- Markdown solution headings: `### INSTRUCTOR SOLUTION — Exercise N`.
- Code solution cells: `# INSTRUCTOR SOLUTION` as the first comment line.
- Hidden markdown solutions: `<!-- INSTRUCTOR SOLUTION -->` as the first line.
- Student placeholder cells (e.g., `### YOUR FINDINGS HERE:`) MUST NOT contain `INSTRUCTOR SOLUTION`.

**Code-exercise block structure** (in the instructor notebook — the student copy strips cells 4–6):

1. `## 📝 PAUSE-AND-DO Exercise X` (exercise prompt markdown)
2. `> 💡 Gemini Prompt:` (Gemini suggestion with "After running, verify:" checklist)
3. Student code cell: `# YOUR SOLUTION CODE HERE` (must NOT contain `INSTRUCTOR SOLUTION`)
4. `### INSTRUCTOR SOLUTION — Exercise X` (heading; removed from student)
5. `# INSTRUCTOR SOLUTION` code cell (solution; removed from student)
6. `<!-- INSTRUCTOR SOLUTION -->` "Reading the output" markdown (removed from student)

See `_project_docs/NOTEBOOK_TEMPLATE.md` for the full notebook structure and `_project_docs/TROUBLESHOOTING.md` if a solution leaks into the student version.

**NotebookLM markdown sync (auto):** A `PostToolUse` hook in `.claude/settings.json` runs `scripts/sync_instructor_md.sh` after any `Edit`/`Write`/`NotebookEdit` whose path ends in `_instructor.ipynb`, regenerating `_notebook_lm/<basename>.md` for NotebookLM podcast ingestion. The directory is gitignored. For direct Jupyter edits (outside Claude), run `bash scripts/sync_instructor_md.sh` manually, or watch with `fswatch -o notebooks/*_instructor.ipynb | xargs -n1 -I{} bash scripts/sync_instructor_md.sh`.

---

## 🚨 CRITICAL WORKFLOW — The Honors Contract (added 2026-08-21)

The course carries a standing **HONORS CONTRACT (OPTIONAL)** offer for John Martinson Honors College students. Full rationale in `_project_docs/DECISIONS.md` Decision 15; the values of record are in `_project_docs/SYLLABUS_OF_RECORD_2026F.md` under "Honors contract".

**The shape, in one line:** the honors work is an *individual research angle on the group final project*, never a parallel course — H1 question memo rides M01, H2 modeling extension (CV-first, paired folds vs. the team baseline) rides M08, H3 a labeled honors section on the team poster rides M10 and the conference. Final Project 35% → 25%, all five components scaled; **Honors Research Extension 10%** (H1 2% · H2 5% · H3 3%). The student's total never grows. Where an entire team holds contracts, neither the reallocation nor the separate poster section applies.

**Grading mechanics — the step with no automatic trigger.** The honors poster section is graded *exclusively* under the Honors Research Extension, never under the group poster rubric, so non-honors teammates cannot lose points for it. And the running Brightspace gradebook shows **only** the regular course requirements: the Honors Research Extension is folded in by a **manual adjustment to the final course grade** after the contract is complete. Nothing prompts that adjustment — put it on the end-of-term checklist for every term a contract is live.

**Direction of sync — this is the part that gets it wrong.** The honors section lives in the **official syllabus docx** (`_syllabus/2026F/2026F_predictive_analytics_purdue_QM474.docx`, gitignored). `syllabus.qmd` is synced **from** the docx, never the reverse. Davi edits the docx in Word; read it back with `python-docx` and bring the website into line, then log any typo left in the docx in the discrepancy register rather than editing an open Word file.

**Two generated artifacts, both regenerated and never hand-edited:**

```bash
python3 scripts/build_honors_section_docx.py    # slices the section out of syllabus.qmd
python3 scripts/build_honors_syllabus_docx.py   # the modified honors syllabus, DSB template
```

Both write into the gitignored `_syllabus/2026F/honors_contract/`. The **section** docx is for pasting into the official syllabus or sending on its own. The **honors syllabus** docx is *not* what students upload — Davi confirmed 2026-08-21 that the official syllabus alone satisfies the form, since the honors section carries its own grading scheme; it is retained only in case a future term or another college asks for a separate modified syllabus, and it is the one artifact stating specific deliverable dates (student-facing text says "Check the course Brightspace page").

**Deadlines shift every term — never reuse these.** Pull the student intake date from the live [Daniels Honors Contract page](https://business.purdue.edu/undergraduate/honors-program/academics/contract.php) (it tracks the Registrar's H grade-mode deadline, *not* the "2nd Friday" rule of thumb in the faculty docx), the coordinator decision date from the 4th Friday of the term, and the scholarly-project proposal deadline from JMHC (Oct 1 fall / Feb 1 spring). Fall 2026, verified: intake **Thu Sep 3**, decisions **Fri Sep 18**, proposals **Thu Oct 1**. Spring 2027: intake `[[PENDING honors-intake]]` (not yet published; Spring 2026 was Mon Jan 26), decisions **Fri Feb 5**, proposals **Mon Feb 1** — which falls before H1 (due with M01, Sun Feb 7), so H1 is drafted first (`[[PENDING honors-jmhc]]`).

**Reference material** lives outside this repo, in Davi's honors-director repo `~/Dropbox/profissional/purdue/activity_report_services/honors_program_dsb_start_20260501/` — `about_purdue_honors/04_honors_contracts.md`, `about_purdue_honors/03_scholarly_project.md`, `honors_contracting/Honors Contracting at Daniels.docx`, and prior-term sample contracts under `honors_contracting/<term>/`.


---

## 🚨 CRITICAL WORKFLOW — Sync Video Guides and Planning Docs

> Producing a **new** notebook's full material set (notebook → videos → Brightspace page → NotebookLM splits → quizzes)? Follow the end-to-end pipeline and dependency order in `_project_docs/COURSE_MATERIAL_WORKFLOW.md`. The rules below are the per-update sync gate within it.

**Every time a notebook (`notebooks/nbNN_*_student.ipynb`) is updated, you MUST:**

1. **Update its video guide** (`video_guides/NN_video_lecture_guide.md`).
   Guides are gitignored — no commit needed, but cell references, speaking prompts, and timestamps go stale fast. Guide structure: At a Glance, Purpose, 9 sections (Why exists, Why after N-1, Why before N+1, Libraries/Tools, Key Concepts, Student Takeaways, Common Questions, Course Arc, Suggested Video Structure with Options A & B). Template: `video_guides/02_video_lecture_guide.md`.
2. **Update planning docs** if the change is significant (added/removed sections, new tools/libraries, reordered content, or shifted dependencies):
   - `_project_docs/MGMT47400_FullSemester_Plan_2026Fall.md` — section "Notebook Sequence Rationale" and dependency diagram.
   - `_project_docs/claude_course_plan.md` — section "Notebook Sequence and Content Justification".

   Minor fixes (typos, wording) do not require planning-doc updates.

---

## 🚨 CRITICAL WORKFLOW — Commit AND Render Webpage

**Every content change MUST be followed by render + commit + push.** GitHub Pages serves `docs/`; without rendering, the website is stale even after `git push`.

```bash
# 1. Commit content changes
git add notebooks/nbNN_topic_student.ipynb  # or schedule.qmd, syllabus.qmd, etc.
git commit -m "feat: Update notebook NN

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# 2. Render Quarto site
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto render

# 3. Commit rendered docs/
git add docs/
git commit -m "build: Render Quarto site

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# 4. Push everything
git push origin main
```

**The most common project-wide mistake** is forgetting step 2/3 — content change is pushed but `docs/` isn't rendered, so the website doesn't update. Always render and commit `docs/` after ANY content change to `.qmd` files, notebooks, images, syllabus, or schedule.

---

## 🚨 CRITICAL WORKFLOW — Password-Gated Instructor Tab (added 2026-08-14)

The sidebar's **Instructor** tab (it replaced the old "For Instructors" tab; the AI co-design essay `workflow.qmd` stays published at its URL, unlisted, linked from the gated page) is the instructor's index to the instructor notebooks (full solutions), video guides, quiz banks, and midterm cases. Ported from the qm670 Business Analytics implementation.

- **`instructor.qmd` is gitignored** (plaintext source of the gated page; backup lives at `site/instructor.qmd` in the private repo). **`docs/instructor.html` is NOT ignored** — the encrypted page is what we publish. Do not "fix" either fact.
- **The page ships ENCRYPTED.** `_adm/_instructor_page/scripts/encrypt_instructor_page.py` (stdlib-only AES-256-GCM + PBKDF2-SHA256, 250k iterations; `--self-test` runs 22 checks) rewrites `docs/instructor.html` into a self-contained browser-decrypted gate. It runs automatically as a Quarto **post-render** hook (`postrender.sh`, wired in `_quarto.yml`), fail-closed: no password → render aborts, the page never publishes in the clear. Idempotent on the marker `<!-- qm474-encrypted-page v1 -->`. The same step prunes `docs/search.json`.
- **Password:** gitignored `_adm/_instructor_page/page_password.txt` (or `$QM474_PAGE_PASSWORD`). NEVER hardcode it, NEVER commit it, never put it in a commit message or announcement.
- **The actual files live in the private companion repo** `davi-moreira/2026F_predictive_analytics_QM474_instructor`: instructor notebooks → `notebooks/`, `video_guides/` → `video_guides/`, `_quizzes/` → `quizzes/`, `_midterm_exam/` → `midterm_exam/`, `instructor.qmd` → `site/instructor.qmd`. Mirror it with `_adm/_instructor_page/scripts/sync_instructor_repo.sh` (`--dry-run` supported; hard-stops unless `gh` reports the target repo PRIVATE and `_instructor_repo` is gitignored). The mirror is synced, never edited directly. **Run the sync after changing any instructor notebook, video guide, quiz bank, midterm file, or `instructor.qmd`.**
- **Guard:** `.git/hooks/pre-commit` refuses to commit `docs/instructor.html` without the marker, `instructor.qmd`, the password file, or any staged file containing the password. `.git/hooks/` is never cloned — the copy of record + install steps live in `_adm/_instructor_page/` (`pre-commit`, `INSTALL_HOOK.md`).

---

## Style Guidelines (Load-Bearing Values)

These values are referenced by tooling and student expectations — do not change casually. See `_project_docs/DECISIONS.md` for rationale.

| Setting | Value |
|---|---|
| Random seed | `RANDOM_SEED = 474` (course number) |
| Train/Val/Test split | 60 / 20 / 20 |
| Figure size | `plt.rcParams['figure.figsize'] = (10, 6)` |
| Display precision | `pd.set_option('display.precision', 3)` |
| Money in markdown cells | Always escape: `\$50,000` (unescaped `$` triggers LaTeX in Colab) |
| Tildes in markdown cells | Always escape: `\~341 patients`, `(\~0.52)` (unescaped `~` is interpreted as strikethrough or as a non-breaking space by Pandoc/Quarto and rots the rendered output) |
| Emoji vocabulary | `✓` success, `⚠️` warning, `📝` exercise, `💡` insight |

## Naming and Commit Conventions

- **Student notebooks (committed):** `nbNN_topic_student.ipynb`
- **Instructor notebooks (gitignored):** `nbNN_topic_instructor.ipynb`
- **Variables:** `lowercase_with_underscores`. **Constants:** `UPPERCASE`.
- **Commit messages:** `<type>: <subject>` where type is `feat`, `fix`, `docs`, `chore`, `build`, `refactor`. Always include `Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>`.
- **Stage specific files** (`git add notebooks/nb09_*.ipynb`) — avoid `git add .` to prevent committing temp files, large CSVs, or secrets.

---

## Anti-Patterns (Do Not Do)

These are the failures that have actually happened in this project. The positive form of most other rules is stated above; what follows is what gets caught in review.

- **Don't commit large files.** No `.zip`, `.mp4`, `.mp3`, `.mov`. No datasets >10 MB — link to external storage.
- **Don't use `git add .`** indiscriminately. Stage by name. Review `git status` first.
- **Don't change the random seed.** Always `RANDOM_SEED = 474`. Different seeds → students get different output → questions on the forum.
- **Don't skip Colab testing.** Click "Open in Colab" → "Runtime → Run all" before committing a notebook.
- **Don't push content without `quarto render` + commit `docs/`.** Website goes stale.
- **Don't leave instructor-solution cells unmarked.** Every excluded cell needs `INSTRUCTOR SOLUTION` somewhere in its source. Unmarked cells leak to students.
- **Don't mix student placeholder and instructor solution in one cell.** Student cell = `# YOUR SOLUTION CODE HERE` only. Solution = SEPARATE cell with `# INSTRUCTOR SOLUTION`.
- **Don't use unescaped `$` for money in markdown cells.** Use `\$50,000`. Colab's MathJax breaks the cell otherwise.
- **Don't use unescaped `~` for "approximately" in markdown cells.** Always escape: `\~341 patients`, `(\~0.52)`. Pandoc/Quarto interpret `~` as a strikethrough delimiter or non-breaking space depending on context, which silently mangles the rendered output. Same rule applies to all markdown content the course renders — student notebooks (markdown cells in `.ipynb`), instructor notebooks, video guides (`video_guides/*.md`), and `.qmd` pages.
- **Don't write fully-justified correct options against terse distractors.** Elaboration leaks correctness: students scored \~100% by always picking the longest option (caught by student reports, 2026Summer). Every option in a question must sit in the same length band, and `scripts/audit_answer_length.py --file <csv>` must PASS before Brightspace import.
- **Don't add complexity that wasn't requested.** No extra features, refactoring, or "improvements" unless asked. Over-engineering confuses students and adds maintenance burden.
- **Don't append to `CONVERSATION_LOG.md` by overwriting** — always append, never replace. Lose history once and you lose it forever.

---

## Quarto Quick Commands

```bash
# Render entire site
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto render

# Preview locally
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto preview

# Render one file
/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto render index.qmd
```

---

## ✅ Session End Checklist

Before ending any session that touched course content:

- [ ] All changes committed with clear `<type>: <subject>` messages and `Co-Authored-By:` line.
- [ ] **Voice-check grep run** on any modified student notebook (`grep -iE '\bstudents?\b|\bthe instructor\b|on camera|speaking prompt' notebooks/nbNN_*_student.ipynb` returns zero non-`Student's t` hits). If video guides changed: `python scripts/voice_check_guides.py` is clean.
- [ ] **CV-first audit run** if any nb09–nb19 evaluation code changed: `python scripts/audit_cv_first.py` returns only the nb14 cells 30 + 34 (one per spine) + nb18 Kaggle-submission exceptions.
- [ ] **Answer-length audit run** if any quiz/exam CSV was created or edited: `python scripts/audit_answer_length.py --file <csv>` returns PASS for every touched bank.
- [ ] **Narrative polish applied** if any new or rewritten student markdown cells landed: named stakeholder in Why-This-Matters, narrative prose over bullet lists in Reading-the-output, at least one `"A question that often comes up here"` Q&A, warm wrap-up with bridge to the next notebook.
- [ ] **`quarto render` run** if ANY content changed (`.qmd`, notebooks, images), AND `docs/` committed.
- [ ] **Instructor-repo sync run** (`bash _adm/_instructor_page/scripts/sync_instructor_repo.sh`) if any instructor notebook, video guide, quiz bank, midterm file, or `instructor.qmd` changed.
- [ ] `CONVERSATION_LOG.md` updated with session summary (appended, not overwritten).
- [ ] If notebooks changed: tested in Colab.
- [ ] `git push origin main` (includes BOTH content AND `docs/`).
- [ ] Clear summary delivered to the user; remaining work listed for next session.

**The two most common end-of-session misses:** forgetting to render Quarto and commit `docs/` (website goes stale), and committing a student-notebook polish without running the voice-check grep (hits get caught in review — cheaper to catch pre-commit).

---

**Last Updated:** 2026-10-12
**Version:** 2.3 — the paper midterm is now 15 questions x four options in plain language (Decision 16); MC parity line updated. Previously 2.2 — added the Honors Contract workflow (Decision 15). Previously 2.1 — slimmed from 977 lines by extracting reference material into `NOTEBOOK_TEMPLATE.md`, `DECISIONS.md`, `TROUBLESHOOTING.md`, and `scripts/`. Behavior-changing rules and workflows preserved verbatim.
**Maintained by:** Professor Davi Moreira + AI Assistants
