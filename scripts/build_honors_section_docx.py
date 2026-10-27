# -*- coding: utf-8 -*-
"""Extract the "Honors Contract (Optional)" section from syllabus.qmd and render
it, alone, to a Word document.

Output: _syllabus/2026F/honors_contract/QM47400_2026F_honors_contract_section.docx

syllabus.qmd stays the single source of truth: this script never restates the
policy, it only slices and converts. Re-run after any edit to the section:

    python3 scripts/build_honors_section_docx.py

Use it to paste the section into the official syllabus .docx, or to send the
honors language to a student or to the Honors College on its own.
"""
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "syllabus.qmd")
OUT = os.path.join(REPO, "_syllabus/2026F/honors_contract/QM47400_2026F_honors_contract_section.docx")
HEADING = "## Honors Contract (Optional)"

PANDOC_CANDIDATES = [
    "/Applications/RStudio.app/Contents/Resources/app/quarto/bin/tools/aarch64/pandoc",
    "/Applications/RStudio.app/Contents/Resources/app/quarto/bin/tools/x86_64/pandoc",
    "/usr/local/bin/pandoc",
    "pandoc",
]

TITLE = "QM 47400 — Predictive Analytics · Fall 2026"
SUBTITLE = ("Excerpt from the course syllabus. Source of truth: "
            "https://davi-moreira.github.io/2026F_predictive_analytics_QM474/syllabus.html")


def find_pandoc():
    for p in PANDOC_CANDIDATES:
        if p == "pandoc" or os.path.exists(p):
            return p
    sys.exit("pandoc not found")


def extract(text):
    start = text.find(HEADING)
    if start < 0:
        sys.exit(f"{HEADING!r} not found in syllabus.qmd")
    # next level-2 heading after the section start
    m = re.search(r"^## ", text[start + len(HEADING):], flags=re.M)
    end = start + len(HEADING) + m.start() if m else len(text)
    return text[start:end].rstrip() + "\n"


def to_plain_markdown(md):
    """Strip Quarto-only syntax that Word has no use for."""
    md = md.replace('{target="_blank"}', "")
    md = md.replace("\\#", "#")          # escaped header in the deliverables table
    md = re.sub(r"[ \t]+$", "", md, flags=re.M)
    return md


def build():
    section = to_plain_markdown(extract(open(SRC, encoding="utf-8").read()))
    # promote to a standalone document: the section heading becomes the title
    section = section.replace(HEADING, "# Honors Contract (Optional)", 1)
    section = re.sub(r"^### ", "## ", section, flags=re.M)
    doc = f"**{TITLE}**\n\n*{SUBTITLE}*\n\n{section}"

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    proc = subprocess.run(
        [find_pandoc(), "--from", "markdown+pipe_tables", "--to", "docx",
         "--standalone", "--output", OUT],
        input=doc, text=True, capture_output=True,
    )
    if proc.returncode != 0:
        sys.exit(proc.stderr)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
