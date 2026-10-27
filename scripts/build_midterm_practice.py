# -*- coding: utf-8 -*-
"""Build a single Brightspace-importable practice-quiz CSV for the midterm.

The practice quiz is a participation assignment, so it needs ONE importable file
rather than the 14 per-case forms the printed exam uses. This assembles that file
from a selection manifest, so the source of the questions is a decision recorded
in data rather than baked into the script.

A manifest is JSON:

    {
      "title": "Midterm Practice Quiz",
      "source": "summer" | "fall",
      "select": [
        {"case": "medscreen", "indices": [1, 3, 4, 7]},
        {"case": "homevalue", "indices": [2, 5]}
      ]
    }

`indices` are 1-based and follow the order questions appear in the source:
  - source "summer": `_midterm_exam/2026Summer/midterm_<case>_*.csv` (4 options each)
  - source "fall":   `_midterm_exam/2026F/banks/<case>.json`          (4 options each since 2026-10-07)

Usage:
    python3 scripts/build_midterm_practice.py --manifest <path> [--out <path>]
    python3 scripts/build_midterm_practice.py --manifest <path> --check

Output is D2L multiple-choice import format, byte-compatible with the quiz banks
under _quizzes/: five-field rows, no separator rows between question blocks.

Every question is validated before the file is written: exactly one keyed option
at 100.00, at least two options, a non-empty stem, and no duplicate stems in the
pooled set. The option-length gate is NOT run here; run it afterwards, since it
is the separate pre-import gate mandated by CLAUDE.md:

    /usr/local/bin/python3 scripts/audit_answer_length.py --file <out>
"""
import argparse
import csv
import glob
import io
import json
import os
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMER = os.path.join(REPO, "_midterm_exam", "2026Summer")
FALL = os.path.join(REPO, "_midterm_exam", "2026F")


def load_summer(case):
    """Return [(stem, [(is_correct, text), ...]), ...] from a Summer case CSV."""
    hits = sorted(glob.glob(os.path.join(SUMMER, f"midterm_{case}_*.csv")))
    if not hits:
        raise SystemExit(f"no Summer CSV found for case {case!r}")
    if len(hits) > 1:
        raise SystemExit(f"ambiguous Summer CSV for {case!r}: {[os.path.basename(h) for h in hits]}")
    out, cur = [], None
    for row in csv.reader(io.open(hits[0], encoding="utf-8")):
        if not row or not row[0]:
            continue
        if row[0] == "NewQuestion":
            if cur:
                out.append(cur)
            cur = {"stem": "", "opts": []}
        elif row[0] == "QuestionText" and cur is not None:
            cur["stem"] = row[1]
        elif row[0] == "Option" and cur is not None:
            cur["opts"].append((row[1].strip() == "100.00", row[2]))
    if cur:
        out.append(cur)
    return [(q["stem"], q["opts"]) for q in out]


def load_fall(case):
    """Return [(stem, [(is_correct, text), ...]), ...] from a Fall bank JSON."""
    path = os.path.join(FALL, "banks", f"{case}.json")
    if not os.path.exists(path):
        raise SystemExit(f"no Fall bank for case {case!r}")
    d = json.load(io.open(path, encoding="utf-8"))
    out = []
    for q in d["questions"]:
        ci = q["correct_index"]
        out.append((q["stem"], [(i == ci, t) for i, t in enumerate(q["options"])]))
    return out


LOADERS = {"summer": load_summer, "fall": load_fall}


def validate(pool):
    problems = []
    stems = []
    for n, (stem, opts) in enumerate(pool, 1):
        keyed = sum(1 for is_c, _ in opts if is_c)
        if keyed != 1:
            problems.append(f"Q{n}: {keyed} keyed options (expected 1)")
        if len(opts) < 2:
            problems.append(f"Q{n}: {len(opts)} options (expected >= 2)")
        if not stem.strip():
            problems.append(f"Q{n}: empty stem")
        stems.append(stem.strip())
    for s, c in Counter(stems).items():
        if c > 1:
            problems.append(f"stem repeated {c}x -> {s[:70]!r}")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--check", action="store_true", help="validate only, write nothing")
    args = ap.parse_args()

    man = json.load(io.open(args.manifest, encoding="utf-8"))
    source = man.get("source")
    if source not in LOADERS:
        sys.exit(f"manifest 'source' must be one of {sorted(LOADERS)}, got {source!r}")

    pool, provenance = [], []
    for sel in man["select"]:
        case = sel["case"]
        questions = LOADERS[source](case)
        for idx in sel["indices"]:
            if not (1 <= idx <= len(questions)):
                sys.exit(f"{case}: index {idx} out of range (1..{len(questions)})")
            pool.append(questions[idx - 1])
            provenance.append((case, idx))

    problems = validate(pool)
    counts = Counter(c for c, _ in provenance)
    print(f"source: {source}   cases: {len(counts)}   questions pooled: {len(pool)}")
    for case in sorted(counts):
        print(f"    {case:<14} {counts[case]:>3}")
    opt_counts = Counter(len(o) for _, o in pool)
    print(f"options per question: {dict(opt_counts)}  "
          f"(chance = {', '.join(f'{100/k:.0f}%' for k in sorted(opt_counts))})")

    if problems:
        print("\nVALIDATION PROBLEMS:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("validation: OK")

    if args.check:
        print("--check: nothing written")
        return

    out = args.out or os.path.join(FALL, "practice", "midterm_practice.csv")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        w = csv.writer(f)
        for stem, opts in pool:
            w.writerow(["NewQuestion", "MC", "", "", ""])
            w.writerow(["Title", "", "", "", ""])
            w.writerow(["QuestionText", stem, "", "", ""])
            w.writerow(["Points", "1", "", "", ""])
            w.writerow(["Difficulty", "1", "", "", ""])
            for is_c, text in opts:
                w.writerow(["Option", "100.00" if is_c else "0.00", text, "", ""])
    print(f"\nwrote {out}")

    prov = os.path.splitext(out)[0] + "_provenance.json"
    json.dump({"source": source, "title": man.get("title", "Midterm Practice Quiz"),
               "questions": [{"n": i + 1, "case": c, "source_index": ix}
                             for i, (c, ix) in enumerate(provenance)]},
              io.open(prov, "w", encoding="utf-8"), indent=1)
    print(f"wrote {prov}")
    print("\nNEXT (mandatory before import):")
    print(f"  /usr/local/bin/python3 scripts/audit_answer_length.py --file {out}")


if __name__ == "__main__":
    main()
