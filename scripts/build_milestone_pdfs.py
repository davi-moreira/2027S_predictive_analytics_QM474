#!/usr/bin/env python3
"""build_milestone_pdfs.py — the Spring 2027 Final Project instruction PDFs.

Every Markdown file in `_final_project/2027S/milestones/` becomes a PDF with the SAME STEM, beside it:
milestone_00 … milestone_13, final_project_overview, peer_review, conference_presentation,
peer_evaluation and poster_to_product. Brightspace carries a short assignment note plus the PDF
(Spring 2027 plan, §1: "Milestone instructions").

Pipeline, one command, idempotent (same sources -> same PDFs, byte for byte):

    Markdown --pandoc 3.x (-t typst, TEMPLATE below)--> Typst --quarto typst compile--> PDF

The look (Purdue gold and black, the title block, the Due / Opens / Submit / Grading box, the footer)
lives in TEMPLATE; the sources carry content only. Front matter of a source:

    kicker: "Milestone 01"              # line above the title; also in the footer
    title:  "Initial Project Proposal"
    fontsize: "10pt"                    # optional; the default body size is 10.4pt
    csv:    ["Milestone 01 —"]          # deadlines_2027S.csv item(s) this document covers (prefix)
    box:                                # the box under the title, in this order
      - {label: Due,     value: "Sunday, February 7, 2027, 11:59 PM ET"}
      - {label: Opens,   value: "Wednesday, January 27, 2027"}
      - {label: Submit,  value: "..."}
      - {label: Grading, value: "..."}

Checks. Any failure stops the run with exit code 1 and names the file and the problem.
  1. Dates. `_final_project/2027S/deadlines_2027S.csv` (written by scripts/build_2027S_calendar.py)
     is the only source of deadlines. The Due row must state, for every `csv` item, its due date
     (and "11:59 PM" when the CSV says so); the Opens row its opens date. Any markdown table row
     whose first cell names an item (M00 … M13, Peer review, Conference, Peer evaluation, P2P …)
     must show that item's CSV dates. Every other date in the text must carry the right weekday and
     be a date the calendar knows: the CSV, the calendar script's class sessions and key dates, or
     the plan's meeting windows (PLAN_DATES below).
  2. Voice. Written to you: no "student(s)" in the third person, no instructor or camera language.
  3. Escapes. No bare `$` or `~` (write `\\$` and `\\~`), as everywhere in this course.
  4. Build. pandoc and typst must succeed, and the PDF must exist and be non-empty.
Placeholders `[[PENDING <id>: …]]` (plan §4) are rendered highlighted, kept verbatim so
`pdftotext … | grep PENDING` finds them, and listed at the end of every run.

Usage:
    python3 scripts/build_milestone_pdfs.py                       # build every PDF
    python3 scripts/build_milestone_pdfs.py --only m06 overview   # a subset (m06 or a stem substring)
    python3 scripts/build_milestone_pdfs.py --check               # run the checks, render nothing
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_final_project" / "2027S" / "milestones"
DEADLINES = ROOT / "_final_project" / "2027S" / "deadlines_2027S.csv"
CALENDAR = ROOT / "scripts" / "build_2027S_calendar.py"
YEAR = 2027

QUARTO = "/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto"
if not Path(QUARTO).exists():
    QUARTO = shutil.which("quarto") or "quarto"
PANDOC = shutil.which("pandoc") or "pandoc"

D = dt.date
#: Dates that come from the Spring 2027 plan (_project_docs/QM47400_FullSemester_Plan_2027Spring.md §2),
#: not from the gradebook or the class sessions. Edit here if the plan changes.
PLAN_DATES = {
    # Meeting Round 01: TA Feb 8–21, instructor Feb 22–28.
    D(2027, 2, 8), D(2027, 2, 21), D(2027, 2, 22), D(2027, 2, 28),
    # Meeting Round 02: TA Mar 8–14 and Mar 22–28, instructor Mar 29 – Apr 3.
    D(2027, 3, 8), D(2027, 3, 14), D(2027, 3, 22), D(2027, 3, 28), D(2027, 3, 29), D(2027, 4, 3),
    # Spring break ends Sat Mar 20; OURConnect mentor approval Wed Mar 24.
    D(2027, 3, 20), D(2027, 3, 24),
}

#: First cell of a table row -> the CSV item (prefix) whose dates that row must show.
ROW_KEYS = {f"M{n:02d}": f"Milestone {n:02d} —" for n in range(14)}
ROW_KEYS.update({
    "Peer review": "Peer Review Submission",
    "Conference": "Conference Poster Presentation",
    "Peer evaluation": "Peer Evaluation Submission",
    "P2P product": "Poster-to-Product: team product",
    "P2P live link": "Poster-to-Product: individual live dashboard link",
})

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
MONTH_NUM = {m: i for i, m in enumerate(MONTHS, 1)} | {m[:3]: i for i, m in enumerate(MONTHS, 1)}
MONTH_NUM["Sept"] = 9
WEEKDAY_NUM = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
DATE_RE = re.compile(
    r"\b(?:(?P<wd>Mon|Tue|Wed|Thu|Fri|Sat|Sun)(?:day|sday|nesday|rsday|urday)?\.?,?\s+)?"
    r"(?P<mon>" + "|".join(MONTHS) + r"|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\.?\s+"
    r"(?P<day>\d{1,2})(?!\d)(?:,?\s+(?P<year>20\d\d))?")
#: "the Instructor/TA Evaluation" is a Final Project component's name, so "/" after it is allowed.
VOICE_RE = re.compile(r"\bstudents?\b(?!'s t)|\bthe instructor\b(?!/)|on camera|speaking prompt", re.I)
PENDING_RE = re.compile(r"\[\[PENDING ([^:\]]+):", re.S)


def long_date(d: dt.date) -> str:
    return f"{d:%A}, {d:%B} {d.day}, {d.year}"


def short_date(d: dt.date) -> str:
    return f"{d:%a} {d:%b} {d.day}"


# ---------------------------------------------------------------------------
# sources of dates

def load_deadlines() -> list[dict]:
    with DEADLINES.open(newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["opens"] = dt.date.fromisoformat(r["opens"])
        r["due"] = dt.date.fromisoformat(r["due"])
    return rows


def calendar_dates() -> set[dt.date]:
    """Class sessions and key dates from build_2027S_calendar.py (imported, never run as main)."""
    spec = importlib.util.spec_from_file_location("build_2027S_calendar", CALENDAR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {s[0] for s in mod.SESSIONS} | {k[0] for k in mod.KEY}


def csv_item(rows: list[dict], prefix: str) -> dict:
    hits = [r for r in rows if r["item"].startswith(prefix)]
    if len(hits) != 1:
        raise ValueError(f"CSV prefix {prefix!r} matches {len(hits)} rows (need exactly 1)")
    return hits[0]


# ---------------------------------------------------------------------------
# reading a source

def front_matter(src: Path) -> dict:
    """Front matter as plain-text JSON, via pandoc (no PyYAML needed)."""
    with tempfile.TemporaryDirectory() as td:
        tpl = Path(td) / "meta.tpl"
        tpl.write_text("$meta-json$")
        r = subprocess.run([PANDOC, str(src), "-t", "plain", "--template", str(tpl)],
                           capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"pandoc could not read the front matter:\n{r.stderr}")
    return json.loads(r.stdout or "{}")


def check(src: Path, meta: dict, rows: list[dict], known: set[dt.date]) -> list[str]:
    """Every problem found in one source, as readable lines (empty = clean)."""
    text = src.read_text()
    errs: list[str] = []
    for key in ("kicker", "title", "box"):
        if not meta.get(key):
            errs.append(f"front matter has no `{key}`")
    box = {b.get("label", ""): b.get("value", "") for b in meta.get("box", [])}

    # 1a. the box against the CSV
    for prefix in meta.get("csv", []):
        try:
            item = csv_item(rows, prefix)
        except ValueError as e:
            errs.append(str(e))
            continue
        due, opens = item["due"], item["opens"]
        if long_date(due) not in box.get("Due", ""):
            errs.append(f"Due row must say {long_date(due)!r} for CSV item {item['item']!r}")
        if item["due_time_ET"] == "11:59 PM" and "11:59 PM" not in box.get("Due", ""):
            errs.append(f"Due row must say 11:59 PM for CSV item {item['item']!r}")
        if "Opens" in box:
            if long_date(opens) not in box["Opens"]:
                errs.append(f"Opens row must say {long_date(opens)!r} for CSV item {item['item']!r}")
        elif opens != due:
            errs.append(f"no Opens row, but CSV item {item['item']!r} opens {long_date(opens)}")

    # 1b. table rows that name a gradebook item
    for n, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|"):
            continue
        first = line.strip("|").split("|")[0].replace("*", "").strip()
        if first not in ROW_KEYS:
            continue
        item = csv_item(rows, ROW_KEYS[first])
        for d in {item["due"], item["opens"]}:
            if short_date(d) not in line and long_date(d) not in line:
                errs.append(f"line {n}: table row {first} must show {short_date(d)} "
                            f"(CSV {item['item']!r})")

    # 1c. every date: right weekday, and a date the calendar knows
    for n, line in enumerate(text.splitlines(), 1):
        for m in DATE_RE.finditer(line):
            year = int(m["year"]) if m["year"] else YEAR
            try:
                d = dt.date(year, MONTH_NUM[m["mon"]], int(m["day"]))
            except ValueError:
                errs.append(f"line {n}: {m[0]!r} is not a real date")
                continue
            if m["wd"] and WEEKDAY_NUM[m["wd"]] != d.weekday():
                errs.append(f"line {n}: {m[0]!r} — {d:%B} {d.day}, {year} is a {d:%A}")
            if year == YEAR and d not in known:
                errs.append(f"line {n}: {m[0]!r} is not in the CSV, the calendar script or PLAN_DATES")

    # 2. voice, 3. escapes
    for n, line in enumerate(text.splitlines(), 1):
        if m := VOICE_RE.search(line):
            errs.append(f"line {n}: voice — {m[0]!r} (write to the reader, in the second person)")
        if re.search(r"(?<!\\)\$", line):
            errs.append(f"line {n}: bare $ (write \\$)")
        if re.search(r"(?<!\\)~", line):
            errs.append(f"line {n}: bare ~ (write \\~)")
    return errs


# ---------------------------------------------------------------------------
# rendering

#: pandoc template (pandoc variables are $…$; this file has no Typst math, so no literal $).
TEMPLATE = r"""// Generated by scripts/build_milestone_pdfs.py from the Markdown source of the same name. Do not edit.
#let gold = rgb("#CFB991")   // Purdue Boilermaker Gold
#let aged = rgb("#8E6F3E")   // Purdue Aged: the dark gold used for text on white
#let tint = rgb("#F7F1E1")   // light gold wash
#let ink = rgb("#000000")
#let sans = ("Avenir Next", "Helvetica Neue", "Helvetica", "Arial")
#let serif = ("Charter", "Georgia", "Libertinus Serif")
#let mono = ("Menlo", "DejaVu Sans Mono")

#let horizontalrule = block(above: 0.9em, below: 0.9em, line(length: 100%, stroke: 0.6pt + gold))
#let pending(body) = highlight(fill: rgb("#FFE58F"), extent: 1.2pt)[#text(font: sans, size: 0.86em, weight: "medium", fill: rgb("#5C3A00"))[#body]]

#set document(title: [QM47400 · Spring 2027 · $kicker$ — $title$], author: "Davi Moreira")
#set page(
  paper: "us-letter",
  margin: (left: 2.1cm, right: 2.1cm, top: 1.8cm, bottom: 2.0cm),
  footer: context [
    #set text(font: sans, size: 7.4pt, fill: luma(105))
    #line(length: 100%, stroke: 0.4pt + gold)
    #v(-3pt)
    #grid(columns: (1fr, auto), align: (left, right),
      [QM47400 Predictive Analytics · Spring 2027 · $kicker$ — $title$],
      [Page #counter(page).display() of #counter(page).final().first()])
  ],
)
#set text(font: serif, size: $if(fontsize)$$fontsize$$else$10.4pt$endif$, lang: "en", hyphenate: false)
#set par(leading: 0.58em, spacing: 0.8em)
#set list(indent: 0.3em, body-indent: 0.5em, spacing: 0.48em, marker: text(fill: aged)[•])
#set enum(indent: 0.3em, body-indent: 0.5em, spacing: 0.48em)
#show heading: set text(font: sans, fill: ink)
#show heading.where(level: 2): it => block(above: 1.1em, below: 0.55em, sticky: true)[
  #box(width: 3.2pt, height: 0.8em, fill: gold) #h(3pt) #text(size: 11.6pt, weight: "bold")[#it.body]
]
#show heading.where(level: 3): it => block(above: 0.85em, below: 0.45em, sticky: true)[
  #text(size: 10.2pt, weight: "bold", fill: aged)[#it.body]
]
#show link: it => underline(stroke: 0.5pt + gold, offset: 1.6pt)[#text(fill: aged)[#it]]
#show raw: set text(font: mono, size: 0.86em)
#show raw.where(block: false): set text(fill: rgb("#4A3A12"))
#show quote.where(block: true): it => block(width: 100%, fill: tint, inset: (x: 9pt, y: 7pt), radius: 2pt,
  stroke: (left: 2.4pt + gold), above: 0.75em, below: 0.75em)[
  #set text(size: 9.6pt)
  #it.body
]
#set table(
  stroke: (x, y) => if y == 0 { (bottom: 0.8pt + aged) } else { (bottom: 0.4pt + luma(212)) },
  inset: (x: 5pt, y: 3.4pt),
  fill: (x, y) => if y == 0 { tint },
)
#show table: set text(size: 9pt)
#show table: set par(leading: 0.48em)
#show table.cell.where(y: 0): set text(font: sans, weight: "bold", size: 8.5pt)
#show figure: set block(breakable: true)
#show figure.where(kind: table): set block(above: 0.75em, below: 0.85em)

#block(width: 100%, below: 0.9em)[
  #text(font: sans, size: 9.4pt, weight: "bold", fill: aged, tracking: 0.04em)[QM47400 · Spring 2027 · $kicker$]
  #v(-0.3em)
  #text(font: sans, size: 18.5pt, weight: "bold", fill: ink)[$title$]
  #v(-0.5em)
  #line(length: 100%, stroke: 2pt + gold)
]
$if(box)$
#block(width: 100%, fill: tint, inset: (x: 11pt, y: 9pt), radius: 3pt, stroke: (left: 3.5pt + aged), below: 1.05em)[
  #set text(size: 9.8pt)
  #set par(leading: 0.5em)
  #grid(columns: (4.4em, 1fr), column-gutter: 10pt, row-gutter: 7pt,
$for(box)$
    text(font: sans, weight: "bold", size: 8.3pt, fill: aged, tracking: 0.04em)[#upper[$box.label$]], [$box.value$],
$endfor$
  )
]
$endif$
$body$
"""


def to_typst(src: Path, tpl: Path) -> str:
    r = subprocess.run([PANDOC, str(src), "-s", "-t", "typst", "--wrap=none", "--template", str(tpl)],
                       capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"pandoc failed:\n{r.stderr}")
    typ = r.stdout
    # [[PENDING …]] -> highlighted, text kept verbatim
    typ = re.sub(r"\\\[\\\[PENDING(.+?)\\\]\\\]", r"#pending[\\[\\[PENDING\1\\]\\]]", typ, flags=re.S)
    # tables flush left rather than centred
    typ = typ.replace("align(center)[#table(", "align(left)[#table(")
    return typ


def render(src: Path, tpl: Path, out_pdf: Path) -> None:
    typ = to_typst(src, tpl)
    env = dict(os.environ, SOURCE_DATE_EPOCH=str(int(src.stat().st_mtime)))   # reproducible PDFs
    with tempfile.TemporaryDirectory() as td:
        t = Path(td) / f"{src.stem}.typ"
        t.write_text(typ)
        pdf = Path(td) / f"{src.stem}.pdf"
        r = subprocess.run([QUARTO, "typst", "compile", str(t), str(pdf)],
                           capture_output=True, text=True, env=env)
        if r.returncode or not pdf.exists() or pdf.stat().st_size == 0:
            raise RuntimeError(f"typst failed (exit {r.returncode}, {QUARTO} typst compile):\n"
                               f"{r.stdout[-3000:]}{r.stderr[-3000:]}")
        if "warning" in r.stderr.lower():
            sys.stderr.write(f"  ⚠ typst warnings for {src.name}:\n{r.stderr}\n")
        shutil.copyfile(pdf, out_pdf)


def pages(pdf: Path) -> str:
    if not shutil.which("pdfinfo"):
        return "?"
    r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
    m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
    return m.group(1) if m else "?"


# ---------------------------------------------------------------------------

def wanted(stem: str, only: list[str] | None) -> bool:
    if not only:
        return True
    for t in only:
        if re.fullmatch(r"m\d\d", t) and stem.startswith(f"milestone_{t[1:]}"):
            return True
        if t in stem:
            return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--only", nargs="*", help="m00 … m13, or any substring of a file stem")
    ap.add_argument("--check", action="store_true", help="run the checks only; render nothing")
    args = ap.parse_args()

    for tool in (PANDOC, QUARTO):
        if not (Path(tool).exists() or shutil.which(tool)):
            raise SystemExit(f"✗ {tool} not found")
    rows = load_deadlines()
    known = {r["opens"] for r in rows} | {r["due"] for r in rows} | calendar_dates() | PLAN_DATES

    sources = [p for p in sorted(SRC.glob("*.md")) if wanted(p.stem, args.only)]
    if not sources:
        raise SystemExit(f"✗ no Markdown sources matched in {SRC.relative_to(ROOT)}")

    failures: dict[str, list[str]] = {}
    pending: list[tuple[str, str]] = []
    built: list[tuple[str, str]] = []
    with tempfile.TemporaryDirectory() as td:
        tpl = Path(td) / "template.typ"
        tpl.write_text(TEMPLATE)
        for src in sources:
            try:
                meta = front_matter(src)
                errs = check(src, meta, rows, known)
            except Exception as e:                      # noqa: BLE001 — report, never half-build
                errs = [str(e)]
            pending += [(src.stem, m.group(1).strip()) for m in PENDING_RE.finditer(src.read_text())]
            if errs:
                failures[src.name] = errs
                continue
            if args.check:
                continue
            out = src.with_suffix(".pdf")
            try:
                render(src, tpl, out)
            except Exception as e:                      # noqa: BLE001
                failures[src.name] = [str(e)]
                continue
            built.append((out.name, pages(out)))
            print(f"  ✓ {out.relative_to(ROOT)}  ({built[-1][1]} page(s))")

    if pending:
        print(f"\n{len(pending)} [[PENDING …]] placeholder(s) (plan §4):")
        for stem, pid in pending:
            print(f"  {pid:<14} {stem}")
    if failures:
        print(f"\n✗ {len(failures)} document(s) failed; their PDFs were NOT (re)written:", file=sys.stderr)
        for name, errs in failures.items():
            print(f"  {name}", file=sys.stderr)
            for e in errs:
                print(f"    - {e}", file=sys.stderr)
        sys.exit(1)
    if args.check:
        print(f"\n✓ {len(sources)} source(s) checked clean: dates match the CSV and calendar, voice and escapes OK")
    else:
        print(f"\n✓ {len(built)} PDF(s) written beside their sources in {SRC.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
