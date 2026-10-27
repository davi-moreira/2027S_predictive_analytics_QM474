# -*- coding: utf-8 -*-
"""Build one master quiz CSV per notebook from that notebook's versioned banks.

Each `_quizzes/<edition>/quiz_nbNN_v*.csv` holds 10 questions in Brightspace D2L
multiple-choice import format. Brightspace wants a single file per notebook to
load into the quiz library, so this concatenates every version of a notebook into
`_quizzes/<edition>/masters/quiz_nbNN_master.csv`.

Concatenation is done on raw lines rather than by round-tripping through the csv
module, so the output is byte-faithful to the sources: same quoting, same field
count, same lack of separator rows between question blocks.

Usage:
    python3 scripts/build_quiz_masters.py                 # default edition 2026F
    python3 scripts/build_quiz_masters.py --edition 2026Summer
    python3 scripts/build_quiz_masters.py --check         # validate only, write nothing

Every master is validated before it is written: 5 fields per row, one block per
question, exactly one keyed option (100.00) per question, at least two options,
and no duplicate stems within the notebook.
"""
import argparse
import csv
import io
import os
import re
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS = ["01", "02", "03", "04", "05", "06", "07", "08", "09",
             "11", "12", "13", "14", "16", "17", "19"]


def version_files(qdir, nb):
    """All version banks for one notebook, ordered numerically (v2 before v10)."""
    pat = re.compile(rf"^quiz_nb{nb}_v(\d+)\.csv$")
    found = []
    for name in os.listdir(qdir):
        m = pat.match(name)
        if m:
            found.append((int(m.group(1)), os.path.join(qdir, name)))
    return [p for _, p in sorted(found)]


def read_blocks(path):
    """Split one bank into question blocks, preserving raw lines."""
    lines = io.open(path, encoding="utf-8").read().splitlines()
    blocks, cur = [], None
    for ln in lines:
        if not ln.strip() or ln.strip(",") == "":
            continue                      # drop blank / all-comma separator rows
        if ln.startswith("NewQuestion,"):
            if cur:
                blocks.append(cur)
            cur = [ln]
        elif cur is not None:
            cur.append(ln)
        else:
            raise ValueError(f"{path}: content before the first NewQuestion row")
    if cur:
        blocks.append(cur)
    return blocks


def validate(blocks, label):
    """Return a list of problem strings; empty means clean."""
    problems, stems = [], []
    for i, blk in enumerate(blocks, 1):
        rows = list(csv.reader(blk))
        n_opt = sum(1 for r in rows if r and r[0] == "Option")
        n_key = sum(1 for r in rows if r and r[0] == "Option"
                    and len(r) > 1 and r[1].strip() == "100.00")
        stem = next((r[1] for r in rows if r and r[0] == "QuestionText" and len(r) > 1), "")
        for r in rows:
            if len(r) != 5:
                problems.append(f"{label} Q{i}: row has {len(r)} fields, expected 5 -> {r[:2]}")
        if n_key != 1:
            problems.append(f"{label} Q{i}: {n_key} keyed options (expected 1)")
        if n_opt < 2:
            problems.append(f"{label} Q{i}: {n_opt} options (expected >= 2)")
        if not stem.strip():
            problems.append(f"{label} Q{i}: empty QuestionText")
        stems.append(stem.strip())
    for s, c in Counter(stems).items():
        if c > 1:
            problems.append(f"{label}: stem repeated {c}x -> {s[:60]!r}")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edition", default="2026F")
    ap.add_argument("--check", action="store_true", help="validate only, write nothing")
    args = ap.parse_args()

    qdir = os.path.join(REPO, "_quizzes", args.edition)
    if not os.path.isdir(qdir):
        sys.exit(f"no such edition directory: {qdir}")
    outdir = os.path.join(qdir, "masters")

    all_problems, rows_out = [], []
    total_q = 0
    for nb in NOTEBOOKS:
        vfiles = version_files(qdir, nb)
        if not vfiles:
            all_problems.append(f"nb{nb}: no version banks found")
            continue
        blocks = []
        for vf in vfiles:
            blocks.extend(read_blocks(vf))
        problems = validate(blocks, f"nb{nb}")
        all_problems.extend(problems)
        total_q += len(blocks)
        rows_out.append((nb, len(vfiles), len(blocks), blocks))

    if all_problems:
        print("VALIDATION PROBLEMS:")
        for p in all_problems:
            print("  " + p)
        sys.exit(1)

    print(f"{'bank':>6}  {'versions':>8}  {'questions':>9}")
    for nb, nv, nq, _ in rows_out:
        print(f"  nb{nb}  {nv:>8}  {nq:>9}")
    print(f"{'TOTAL':>6}  {sum(r[1] for r in rows_out):>8}  {total_q:>9}")

    if args.check:
        print("\n--check: validated only, nothing written")
        return

    os.makedirs(outdir, exist_ok=True)
    for nb, _, nq, blocks in rows_out:
        out = os.path.join(outdir, f"quiz_nb{nb}_master.csv")
        with io.open(out, "w", encoding="utf-8", newline="\n") as f:
            for blk in blocks:
                f.write("\n".join(blk) + "\n")
    print(f"\nwrote {len(rows_out)} master banks to {outdir}")


if __name__ == "__main__":
    main()
