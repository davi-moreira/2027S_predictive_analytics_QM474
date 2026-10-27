#!/usr/bin/env python3
"""build_2027S_calendar.py — the ONE source of the Spring 2027 calendar.

Every Spring 2027 date lives here: class sessions, notebook days, quizzes, participation, milestones,
the midterm, the Course Case Competition, the conference, Poster-to-Product, honors and extra credit.
The script writes, from this single table:

  schedule.qmd                                        the course schedule page (table + full deadline list)
  _final_project/2027S/deadlines_2027S.csv            one row per gradebook item, to enter in Brightspace
  _final_project/2027S/deadlines_2027S.md             the same, readable
  _announcements/2027S/upcoming_deadlines_and_key_dates.md   the "important dates" announcement

Change a date HERE and re-run; never hand-edit the outputs.

How the calendar was built (plan: _project_docs/QM47400_FullSemester_Plan_2027Spring.md):
  * Purdue Spring 2027 (Registrar): classes Jan 11 – May 1, MLK Day Jan 18, spring break Mar 15–20,
    finals May 3–8. Spring Undergraduate Research Conference Apr 12–16, posters Tue Apr 13;
    abstracts due in OURConnect Mon Mar 1, final abstract edits Mar 22, mentor approval Mar 24.
  * Fall 2026 is the template, week for week: Spring weeks 1–9 = Fall weeks 1–9; Spring week 10 is
    spring break; Spring weeks 11–16 = Fall weeks 10–15. Milestone deadlines keep their Fall week of
    term, so M10 (final poster) lands nine days before the conference, as in Fall.
  * Fall's due-date rules: participation (PAUSE-AND-DO) on the lecture day; a Monday notebook's quiz
    on Tuesday, a Wednesday's on Sunday, 11:59 PM ET.
Usage:  python3 scripts/build_2027S_calendar.py
"""
from __future__ import annotations
import csv
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "davi-moreira/2027S_predictive_analytics_QM474"
D = dt.date
T = "11:59 PM"

NOTEBOOKS = {  # number -> (file stem, schedule topic, quiz title)
    "nb00": ("nb00_launchpad_course_setup", "Course launch + Launchpad (setup, Colab, Gemini, AI policy, case competition preview, Poster-to-Product preview)", None),
    "nb01": ("nb01_eda_splits", "Predictive analytics fundamentals, EDA, and data splitting", "Predictive Analytics Fundamentals, EDA, and Data Splitting"),
    "nb02": ("nb02_preprocessing_pipelines", "Data setup and preprocessing pipelines", "Data Preprocessing Pipelines"),
    "nb03": ("nb03_regression_metrics_baselines", "Regression metrics and baseline modeling", "Regression Metrics and Baseline Models"),
    "nb04": ("nb04_linear_features_diagnostics", "Linear regression: features, interactions, diagnostics", "Feature Engineering and Model Diagnostics"),
    "nb05": ("nb05_regularization_project_proposal", "Regularization (Ridge & Lasso)", "Regularization (Ridge & Lasso)"),
    "nb06": ("nb06_logistic_pipelines", "Logistic regression: probabilities, boundaries, pipelines", "Logistic Regression — Probabilities, Decision Boundaries, and Pipelines"),
    "nb07": ("nb07_classification_metrics_thresholding", "Classification metrics: confusion matrix, ROC/PR, business costs", "Classification Metrics — Confusion Matrix, ROC/PR, and Business Costs"),
    "nb08": ("nb08_cross_validation_model_comparison", "Resampling and cross-validation: comparing models on the same five folds", "Resampling and Cross-Validation — How to Compare Models Without Fooling Yourself"),
    "nb09": ("nb09_tuning_feature_engineering_project_baseline", "Hyperparameter tuning + feature engineering + leakage detection", "Hyperparameter Tuning, Feature Engineering, and Leakage Detection"),
    "nb11": ("nb11_decision_trees", "Decision trees: interpretable models with sharp edges", "Decision Trees"),
    "nb12": ("nb12_random_forests_importance", "Random forests: bagging, OOB, feature importance", "Random Forests — Bagging, OOB Intuition, and Feature Importance"),
    "nb13": ("nb13_gradient_boosting", "Gradient boosting: performance with discipline", "Gradient Boosting — Performance with Discipline"),
    "nb14": ("nb14_model_selection_protocol", "Model selection: choosing a champion + test-set ceremony + monitoring", "Model Selection Protocol — Choosing a Champion, the Day the Test Set Opens, and Monitoring"),
    "nb16": ("nb16_time_series_forecasting", "Time-series forecasting: walk-forward CV, lag features", "Time-Series Forecasting — Walk-Forward CV, Lag Features, and Baselines"),
    "nb17": ("nb17_data_communication_poster", "Data communication and poster design", "Data Communication and Poster Design — Turning Your Model Into a Story"),
    "nb18": ("nb18_competition_workflow", "Competition workflow: from notebook to `submission.csv` — the full pipeline, tree ensembles, and the champion model", None),
    "nb19": ("nb19_deep_learning", "Deep learning (PyTorch + when-to-use + LLM lab)", "Deep Learning"),
}

GW = "Group Work: Final Project"
GWC = "Group Work: Final Project/Competition"
# (date, topic, notebook or None, kind)   kind: lecture | group | none | exam | conf | p2p | wrap
SESSIONS = [
    (D(2027, 1, 11), None, "nb00", "lecture"), (D(2027, 1, 13), None, "nb01", "lecture"), (D(2027, 1, 15), None, "nb02", "lecture"),
    (D(2027, 1, 18), "*No class — Martin Luther King Jr. Day*", None, "none"), (D(2027, 1, 20), None, "nb03", "lecture"), (D(2027, 1, 22), GW, None, "group"),
    (D(2027, 1, 25), None, "nb04", "lecture"), (D(2027, 1, 27), None, "nb05", "lecture"), (D(2027, 1, 29), GW, None, "group"),
    (D(2027, 2, 1), None, "nb06", "lecture"), (D(2027, 2, 3), None, "nb07", "lecture"),
    (D(2027, 2, 5), "Group Work: Final Project + **Course Case Competition kickoff** (join on Kaggle, form your `Group NN` team, download the data, first submission)", None, "group"),
    (D(2027, 2, 8), None, "nb08", "lecture"), (D(2027, 2, 10), None, "nb09", "lecture"), (D(2027, 2, 12), "**MIDTERM EXAM — in class, on paper.**", None, "exam"),
    (D(2027, 2, 15), None, "nb11", "lecture"), (D(2027, 2, 17), None, "nb12", "lecture"), (D(2027, 2, 19), GWC, None, "group"),
    (D(2027, 2, 22), None, "nb13", "lecture"), (D(2027, 2, 24), None, "nb14", "lecture"), (D(2027, 2, 26), GWC, None, "group"),
    (D(2027, 3, 1), GWC, None, "group"), (D(2027, 3, 3), None, "nb16", "lecture"), (D(2027, 3, 5), GWC, None, "group"),
    (D(2027, 3, 8), None, "nb18", "lecture"), (D(2027, 3, 10), None, "nb19", "lecture"), (D(2027, 3, 12), GWC, None, "group"),
    (D(2027, 3, 15), "*No class — Spring Break (Mar 15–20)*", None, "none"), (D(2027, 3, 17), "*No class — Spring Break (Mar 15–20)*", None, "none"),
    (D(2027, 3, 19), "*No class — Spring Break (Mar 15–20)*", None, "none"),
    (D(2027, 3, 22), None, "nb17", "lecture"), (D(2027, 3, 24), GW, None, "group"), (D(2027, 3, 26), GW, None, "group"),
    (D(2027, 3, 29), GW, None, "group"), (D(2027, 3, 31), GW, None, "group"), (D(2027, 4, 2), GW, None, "group"),
    (D(2027, 4, 5), GW, None, "group"), (D(2027, 4, 7), GW, None, "group"), (D(2027, 4, 9), GW, None, "group"),
    (D(2027, 4, 12), GW, None, "group"),
    (D(2027, 4, 13), "**Spring Undergraduate Research Conference — Poster Presentation (all students present)**", None, "conf"),
    (D(2027, 4, 14), "*No class — time to rest and catch up on other coursework*", None, "none"),
    (D(2027, 4, 16), "Poster-to-Product kickoff — scoping, partner framing, AI-assistant assignment", None, "p2p"),
    (D(2027, 4, 19), "Poster-to-Product — data engineering + model validation", None, "p2p"),
    (D(2027, 4, 21), "Poster-to-Product — deployment + partner checkpoint", None, "p2p"),
    (D(2027, 4, 23), "Poster-to-Product — usability testing + iteration", None, "p2p"),
    (D(2027, 4, 26), "Poster-to-Product — executive brief drafting + showcase preparation", None, "p2p"),
    (D(2027, 4, 28), "**Poster-to-Product SHOWCASE** (partners + feedback)", None, "p2p"),
    (D(2027, 4, 30), "Course wrap — peer evaluation, reflection survey, competition results", None, "wrap"),
]
TERM_START = D(2027, 1, 11)


def week(d):
    return (d - TERM_START).days // 7 + 1


def quiz_due(d, nb):
    """Fall 2026 rule: Monday notebook -> Tuesday; Wednesday or Friday notebook -> Sunday; nb01 -> next day."""
    if nb == "nb01":
        return d + dt.timedelta(days=1)
    if nb == "nb17":                       # last notebook: the Sunday of its week, with M09
        return d + dt.timedelta(days=6 - d.weekday())
    if d.weekday() == 0:
        return d + dt.timedelta(days=1)
    return d + dt.timedelta(days=6 - d.weekday())


# (category, title, opens, due, time, grading, notes)
ITEMS = []


def add(cat, title, opens, due, time=T, grading="", notes=""):
    ITEMS.append((cat, title, opens, due, time, grading, notes))


for d, topic, nb, kind in SESSIONS:
    if kind == "lecture":
        add("Participation", f'{nb.upper()} "Pause and Do Exercises"', d, d, T, "completion")
        q = NOTEBOOKS[nb][2]
        if q:
            add("Quiz", f"Quiz {nb.upper()}: {q}", d, quiz_due(d, nb), T, "quiz")

add("Participation", "Final Project and Course Competition [Group Check-in]", D(2027, 1, 13), D(2027, 1, 15), T, "completion")
add("Participation", "Syllabus Quiz", D(2027, 1, 11), D(2027, 1, 17), T, "completion")
add("Participation", "Students Profile Survey", D(2027, 1, 11), D(2027, 1, 17), T, "completion")
add("Participation", "Course Competition Team Setup", D(2027, 2, 5), D(2027, 2, 7), T, "completion")
add("Participation", "Midterm Feedback", D(2027, 2, 15), D(2027, 2, 17), T, "completion")
add("Participation", "Reflection Survey", D(2027, 4, 26), D(2027, 4, 30), T, "completion")

MS = [  # (code, title, opens, due, grading)
    ("M00", "Instructor and TA Meetings — Round 01 Schedule + Group Contract", D(2027, 2, 1), D(2027, 2, 7), "completion"),
    ("M01", "Initial Project Proposal", D(2027, 1, 27), D(2027, 2, 7), "50 pts"),
    ("M02", "Expanded Project Outline", D(2027, 2, 8), D(2027, 2, 14), "50 pts"),
    ("M03", "Project Draft Abstract", D(2027, 2, 15), D(2027, 2, 21), "30 pts"),
    ("M04", "Instructor and TAs Meetings — Round 01 Confirmation", D(2027, 2, 18), D(2027, 2, 28), "completion"),
    ("M05", "Applying to the Conference (OURConnect abstract deadline Mon Mar 1)", D(2027, 2, 18), D(2027, 2, 28), "completion"),
    ("M06", "Simple Model and Performance Evaluation", D(2027, 2, 18), D(2027, 3, 7), "100 pts"),
    ("M07", "Instructor and TAs Meetings — Round 02 Schedule", D(2027, 2, 18), D(2027, 3, 7), "completion"),
    ("M08", "More Complex Models and Performance Evaluation", D(2027, 2, 18), D(2027, 3, 14), "100 pts"),
    ("M09", "Poster First Draft", D(2027, 3, 22), D(2027, 3, 28), "poster rubric (feedback)"),
    ("M10", "Final Poster Submission (`NN.pdf`)", D(2027, 3, 29), D(2027, 4, 4), "poster rubric"),
    ("M11", "Poster Presentation Planning", D(2027, 4, 4), D(2027, 4, 11), "rubric"),
    ("M12", "Post Invitation for Poster Presentation", D(2027, 4, 4), D(2027, 4, 11), "completion"),
    ("M13", "Instructor and TAs Meetings — Round 02 Confirmation", D(2027, 4, 4), D(2027, 4, 11), "completion"),
]
for code, title, o, due, g in MS:
    add("Final Project", f"Milestone {code[1:]} — {title}", o, due, T, g)
add("Final Project", "Peer Review Submission", D(2027, 4, 4), D(2027, 4, 11), T, "10% of the project")
add("Final Project", "Conference Poster Presentation — Spring Undergraduate Research Conference (required)", D(2027, 4, 13), D(2027, 4, 13), "in person", "20% of the project")
add("Peer Evaluation", "Peer Evaluation Submission: Final Project and/or Course Case Competition", D(2027, 4, 26), D(2027, 4, 30), T, "20% of each")
add("Midterm", "Midterm Exam — in class, on paper, closed book, no AI tools; covers NB00–NB09", D(2027, 2, 12), D(2027, 2, 12), "in class", "20%")
add("Course Case Competition", "Course Case Competition: Rank Code Submission (Kaggle final)", D(2027, 2, 5), D(2027, 4, 25), T, "20% (incl. peer evaluation)")
add("Poster-to-Product", "Poster-to-Product: team product submission (one per team)", D(2027, 4, 16), D(2027, 4, 26), T, "5% (funding to be confirmed)")
add("Poster-to-Product", "Poster-to-Product: individual live dashboard link", D(2027, 4, 16), D(2027, 4, 28), T, "part of the 5%")
add("Extra Credit", "Extra Credit: Mid-term Course Evaluation — Individual Credit", D(2027, 2, 15), D(2027, 2, 19), T, "extra credit")
add("Extra Credit", "Extra Credit: Issues in Course Materials", D(2027, 1, 11), D(2027, 4, 23), T, "extra credit")
add("Extra Credit", "Extra Credit: DataCamp", D(2027, 1, 11), D(2027, 4, 23), T, "extra credit")
add("Extra Credit", "Extra Credit: Final Course Evaluation — Individual Credit", D(2027, 4, 19), D(2027, 4, 30), T, "extra credit")

KEY = [  # dated facts that are not gradebook items: (date, text)
    (D(2027, 1, 18), "No class — Martin Luther King Jr. Day."),
    (D(2027, 2, 1), "Honors: John Martinson Honors College scholarly-project proposals due (spring deadline)."),
    (D(2027, 2, 5), "Midterm accommodations: book your Purdue Testing Services seat by today (7 days ahead)."),
    (D(2027, 2, 5), "Course Case Competition opens in class (Kaggle)."),
    (D(2027, 3, 1), "Conference: abstract submission deadline in OURConnect (11:59 PM)."),
    (D(2027, 3, 15), "No class — Spring Break (Mar 15–20)."),
    (D(2027, 3, 22), "Conference: final abstract edits close in OURConnect."),
    (D(2027, 4, 14), "No class — time to rest and catch up on other coursework."),
    (D(2027, 4, 28), "Poster-to-Product showcase (in class)."),
]

FMT = lambda d: d.strftime("%a %b ") + str(d.day)
SHORT = lambda d: d.strftime("%b ") + str(d.day)


def colab(stem):
    return (f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
            f"(https://colab.research.google.com/github/{REPO}/blob/main/notebooks/{stem}_student.ipynb){{target=\"_blank\"}}")


def due_between(a, b):
    """Gradebook items due on day a up to (not including) day b, plus key dates in that span."""
    out = []
    for cat, title, o, due, time, g, n in ITEMS:
        if a <= due < b and cat != "Participation" and time not in ("in class", "in person"):
            out.append(f"{title} — due {FMT(due)}")
    return out


def schedule_rows():
    rows = []
    sess = SESSIONS + [(D(2027, 5, 1), None, None, "end")]
    for i, (d, topic, nb, kind) in enumerate(SESSIONS):
        nxt = sess[i + 1][0]
        if nb:
            stem, t, _ = NOTEBOOKS[nb]
            topic_txt = t
            nb_txt = f"**{nb}**<br>{colab(stem)}"
        else:
            topic_txt, nb_txt = topic, "—"
        notes = []
        if kind == "exam":
            notes.append("**MIDTERM EXAM (20%)**")
        if kind == "conf":
            notes.append("**POSTER PRESENTATION**")
        if d == D(2027, 2, 5):
            notes.append("**COURSE CASE COMPETITION OPENS**")
        notes += due_between(d, nxt)
        date_txt = f"**{FMT(d)}**" if kind == "conf" else FMT(d)
        rows.append(f"| {week(d)} | {date_txt} | {topic_txt} | {nb_txt} | {'<br>'.join(notes)} |")
    return rows


def label(cat, title):
    if cat == "Participation":
        return f"Participation: {title}"
    if cat == "Final Project":
        return f"Final Project {title}" if title.startswith("Milestone") else f"Final Project: {title}"
    return title


def dated_list():
    ev = [(due, f"{label(cat, title)} — Due." if cat not in ("Midterm",) and time not in ("in person",) else f"{label(cat, title)}.")
          for cat, title, o, due, time, g, n in ITEMS]
    ev += [(d, t) for d, t in KEY]
    ev.sort(key=lambda x: (x[0], 0 if "No class" in x[1] else 1))
    return ev


def write_schedule():
    head = (ROOT / "scripts" / "_schedule_2027S_head.qmd").read_text()
    lines = [head.rstrip("\n"), "", "# Course Schedule", "", "::: overflow-table",
             "| Wk | Date | Topic | Notebook | Assessment / Notes |", "|----|------|-------|----------|--------------------|"]
    lines += schedule_rows()
    lines += [":::", "", "::: below-table", "", "## All deadlines", "",
              "Everything is due at **11:59 PM Eastern** on Brightspace unless it says *in class*. "
              "Each notebook's PAUSE-AND-DO exercises (participation) are due on its lecture day.", ""]
    lines += [f"- **{SHORT(d)}**: {t}" for d, t in dated_list() if '"Pause and Do' not in t]
    lines += ["", (ROOT / "scripts" / "_schedule_2027S_refs.qmd").read_text().rstrip("\n"), "", ":::", ""]
    (ROOT / "schedule.qmd").write_text("\n".join(lines))


def write_deadlines():
    out = ROOT / "_final_project" / "2027S"; out.mkdir(parents=True, exist_ok=True)
    rows = sorted(ITEMS, key=lambda r: (r[3], r[0], r[1]))
    with open(out / "deadlines_2027S.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["category", "item", "opens", "due", "due_time_ET", "grading", "notes"])
        for cat, title, o, due, time, g, n in rows:
            w.writerow([cat, title.replace("`", ""), o.isoformat(), due.isoformat(), time, g, n])
    md = ["# Spring 2027 deadlines — enter these in Brightspace", "",
          "Generated by `scripts/build_2027S_calendar.py`; do not hand-edit. All times Eastern.", "",
          "| Due | Opens | Category | Item | Time | Grading |", "|---|---|---|---|---|---|"]
    md += [f"| {FMT(due)} | {FMT(o)} | {cat} | {title} | {time} | {g} |" for cat, title, o, due, time, g, n in rows]
    (out / "deadlines_2027S.md").write_text("\n".join(md) + "\n")


def write_announcement():
    out = ROOT / "_announcements" / "2027S"; out.mkdir(parents=True, exist_ok=True)
    body = ["**Subject:** Important Dates and Topics in the Upcoming Days", "", "---", "",
            "# Important Dates and Topics in the Upcoming Days", "", "Hello everyone,", "",
            "Here are the important dates for the semester. Everything is due at 11:59 p.m. unless it says in class.", ""]
    for d, t in dated_list():
        body.append(f"- {SHORT(d)}: {t.replace('`', '')}")
    body += ["", "Please monitor the course Brightspace page carefully and use the course checklist to stay current "
             "with all required activities.", "", "Please let me know if you have any questions.", "", "All the best,", "Davi", ""]
    (out / "upcoming_deadlines_and_key_dates.md").write_text("\n".join(body))


if __name__ == "__main__":
    assert all(d.weekday() in (0, 1, 2, 4) for d, *_ in SESSIONS), "a session is not on Mon/Tue(conf)/Wed/Fri"
    assert all(TERM_START <= d <= D(2027, 5, 1) for d, *_ in SESSIONS)
    for cat, title, o, due, *_ in ITEMS:
        assert o <= due, title
        assert not (D(2027, 3, 15) <= due <= D(2027, 3, 21)), f"{title} is due during spring break"
    write_schedule(); write_deadlines(); write_announcement()
    print(f"{len(SESSIONS)} sessions, {len(ITEMS)} gradebook items, {len(KEY)} key dates written.")
