#!/usr/bin/env python3
"""
CV-First / Test-Set-Lock / Data-Roles Audit
===========================================

Scans notebooks/*_student.ipynb for two kinds of regression against the
CV-first rule (see CLAUDE.md -> "CRITICAL RULE - CV-First Evaluation +
Test-Set Lock" and _project_docs/CV_INFERENCE_DOCTRINE.md -> "Data roles
after nb08").

1. Test-set lock. Model-evaluation uses of X_test / y_test. The only
   authorized hits are nb14_model_selection_protocol_student.ipynb cells 30
   (classification ceremony) and 34 (regression ceremony) -- one test-set
   opening per business case, for the frozen champion only. (Until Fall 2026
   nb18's Kaggle-submission demo was also allowed; from Spring 2027 nb18 is the
   S&P 500 forecasting-competition notebook, which locks the most-recent window
   and uses walk-forward origins, so it has no X_test and no exception.)

2. Data roles (D11 + D12, adopted 2026-10-27; landed 2026-11-24). From nb09
   on every notebook splits each dataset ONCE, 80/20, and does all model
   work by 5-fold CV on X_train. In nb09-nb19 the check flags:
     * validation objects:   any [Xy]..._val name (X_val, y_val_clf, Xte_val, ...)
     * temporary splits:     any *_temp name (X_reg_temp, Xs_temp, ...)
     * a split that is not the single 80/20 split (test_size other than 0.20,
       or a split of an existing *_train / *_temp / *_dev object)
     * a fold count other than 5 (n_splits=, cv=<int>, KFold(<int>))
     * hidden carve-outs:    validation_fraction, early_stopping=True,
                             validation_split, validation_data
     * a dataset loaded and then modelled before any train_test_split
   Exempt: nb16 and nb18 -- the forecasting notebooks (temporal train/test +
   walk-forward CV; nb18 became the S&P 500 forecasting competition notebook
   in Spring 2027). nb01-nb08 teach the train/validation/test split and are
   not checked.

Exit code: 0 when the only hits are the authorized test-set openings and the
data-roles check is clean; 1 otherwise; 2 on a setup error.

Usage
-----
    python scripts/audit_cv_first.py            # both checks
    python scripts/audit_cv_first.py --lock     # test-set lock only
    python scripts/audit_cv_first.py --roles    # data roles only

Run from anywhere; paths resolve from this file. Tested draft of the
data-roles check: the Fall 2026 review plan's code/proposed_audit_data_roles.py.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------- 1. test-set lock
MODEL_EVAL_TEST_PATTERNS = [
    r"\.score\(X_test",
    r"\.predict\(X_test",
    r"\.predict_proba\(X_test",
    r"roc_auc_score\(y_test",
    r"accuracy_score\(y_test",
    r"f1_score\(y_test",
    r"precision_score\(y_test",
    r"recall_score\(y_test",
    r"classification_report\(y_test",
    r"brier_score_loss\(y_test",
    r"permutation_importance\([^,)]+,\s*X_test",
]
AUTHORIZED_CELLS = {14: {30, 34}}      # nb14: one ceremony per business case
AUTHORIZED_NOTEBOOKS: set[int] = set()  # none since Spring 2027 (nb18 is temporal, no X_test)


def nb_number(path: Path) -> int | None:
    m = re.match(r"nb(\d+)_", path.name)
    return int(m.group(1)) if m else None


def audit_notebook(path: Path) -> list[tuple[int, str]]:
    """Return a list of (cell_index, matched_pattern) hits for one notebook."""
    nb = json.loads(path.read_text())
    hits: list[tuple[int, str]] = []
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        src = "".join(cell["source"])
        for pat in MODEL_EVAL_TEST_PATTERNS:
            for m in re.finditer(pat, src):
                line_start = src.rfind("\n", 0, m.start()) + 1
                next_newline = src.find("\n", m.start())
                line = src[line_start : next_newline if next_newline != -1 else len(src)]
                if line.lstrip().startswith("#"):
                    continue
                hits.append((i, m.group(0)))
    return hits


def is_authorized(n: int | None, cell: int) -> bool:
    return n in AUTHORIZED_NOTEBOOKS or cell in AUTHORIZED_CELLS.get(n, set())


# --------------------------------------------------------------------------- 2. data roles
DATA_ROLE_PATTERNS = {
    "validation object": r"\b[Xy]\w*_val(?:_\w+)?\b",
    "temporary split": r"\b\w+_temp\b",
    "fold count != 5": r"n_splits\s*=\s*(?!5\b)\d+|\bcv\s*=\s*(?!5\b)\d+|KFold\(\s*(?!5\b)\d+",
    "hidden carve-out": r"validation_fraction|early_stopping\s*=\s*True|validation_split|validation_data",
}
LOADER = r"load_breast_cancer\(|fetch_california_housing\(|read_csv\(|load_\w+\(\s*return_X_y"
SPLIT = r"train_test_split\("
MODEL = r"cross_val_score\(|cross_validate\(|cross_val_predict\(|GridSearchCV\(|RandomizedSearchCV\(|\.fit\("
ROLES_FIRST, ROLES_LAST = 9, 19
ROLES_EXEMPT = {16, 18}


def code_lines(src: str):
    for line in src.splitlines():
        if not line.lstrip().startswith("#"):
            yield line


def audit_data_roles(path: Path) -> list[tuple[int, str, str]]:
    nb = json.loads(path.read_text())
    hits: list[tuple[int, str, str]] = []
    unsplit = False
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        src = "\n".join(code_lines("".join(cell["source"])))
        for name, pat in DATA_ROLE_PATTERNS.items():
            for m in re.finditer(pat, src):
                hits.append((i, name, m.group(0)))
        for m in re.finditer(r"train_test_split\(([^)]*)\)", src, re.S):
            args = m.group(1)
            if not re.search(r"test_size\s*=\s*0?\.20?\b", args) or re.search(
                r"_temp|_train|_dev", args.split(",")[0]
            ):
                hits.append((i, "not the single 80/20 split", re.sub(r"\s+", " ", args)[:50]))
        events = sorted(
            [(m.start(), "load") for m in re.finditer(LOADER, src)]
            + [(m.start(), "split") for m in re.finditer(SPLIT, src)]
            + [(m.start(), "model") for m in re.finditer(MODEL, src)]
        )
        for _, ev in events:
            if ev == "load":
                unsplit = True
            elif ev == "split":
                unsplit = False
            elif ev == "model" and unsplit:
                hits.append((i, "modelled before splitting", "loader then fit/CV"))
                unsplit = False
    seen, out = set(), []
    for h in hits:
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out


# --------------------------------------------------------------------------- main
def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parent.parent
    notebooks_dir = repo_root / "notebooks"
    if not notebooks_dir.is_dir():
        print(f"ERROR: {notebooks_dir} not found.", file=sys.stderr)
        return 2
    run_lock = "--roles" not in argv
    run_roles = "--lock" not in argv
    students = sorted(notebooks_dir.glob("*_student.ipynb"))
    failed = False

    if run_lock:
        print("== 1. Test-set lock (model evaluation on X_test / y_test) ==")
        any_hits = False
        for path in students:
            hits = audit_notebook(path)
            if not hits:
                continue
            any_hits = True
            n = nb_number(path)
            print(f"{path.name}: {len(hits)} hits")
            for cell, pat in hits:
                ok = is_authorized(n, cell)
                failed |= not ok
                print(f"  cell {cell}: {pat}   [{'authorized' if ok else 'NOT AUTHORIZED'}]")
        if not any_hits:
            print("Clean — no model-evaluation uses of X_test/y_test found.")
        print("Authorized: nb14 cells 30 + 34 (one ceremony per business case).")
        print()

    if run_roles:
        print("== 2. Data roles after nb08 (D11 + D12: one 80/20 split, 5 folds, no validation set) ==")
        any_hits = False
        for path in students:
            n = nb_number(path)
            if n is None or n < ROLES_FIRST or n > ROLES_LAST or n in ROLES_EXEMPT:
                continue
            hits = audit_data_roles(path)
            if not hits:
                continue
            any_hits = True
            failed = True
            print(f"{path.name}: {len(hits)} data-role hits")
            grouped: dict[tuple[int, str], list[str]] = {}
            for cell, name, txt in hits:
                grouped.setdefault((cell, name), []).append(txt)
            for (cell, name), txts in grouped.items():
                print(f"  cell {cell}: {name}: {', '.join(sorted(set(txts)))[:110]}")
        if not any_hits:
            print("Clean — one 80/20 split, 5 folds, no validation objects in nb09–nb19 (nb16, nb18 exempt).")
        else:
            print("\nD12: after nb08, split once (80/20) and work on X_train with 5 folds; "
                  "nb16 and nb18 are the temporal exceptions.")
        print()

    print("RESULT:", "FAIL — fix before commit." if failed else "PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
