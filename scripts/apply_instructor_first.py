#!/usr/bin/env python3
"""Apply prose edits to a notebook pair, instructor copy first.

The project rule is that the instructor artifact is the source of truth and the
student copy is derived from it. This applier enforces that mechanically: an
edit is written to `*_instructor.ipynb` first, and only if it landed there is
the same edit written to `*_student.ipynb`. An edit whose text cannot be found
in the instructor copy is REJECTED, not silently applied to the student file.

Edits come from a workflow journal whose result rows look like
    {"notebook": "<student filename>", "edits": [{cell_index, old_text, new_text, ...}]}
`cell_index` is only a hint — the instructor and student copies do not share
indices, so the text is located by search and must be unique.

Usage: python scripts/apply_instructor_first.py <journal.jsonl> [--dry-run]
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NB = REPO / 'notebooks'


def load(p):
    return json.loads(p.read_text())


def save(p, nb):
    p.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n')


def find_cells(nb, needle):
    """Indices of cells containing needle."""
    return [i for i, c in enumerate(nb['cells']) if needle in ''.join(c['source'])]


def apply_one(nb, needle, replacement):
    hits = find_cells(nb, needle)
    if len(hits) != 1:
        return None, f'{"no match" if not hits else f"{len(hits)} matches"}'
    i = hits[0]
    src = ''.join(nb['cells'][i]['source'])
    nb['cells'][i]['source'] = src.replace(needle, replacement).splitlines(keepends=True)
    return i, None


def main():
    journal = Path(sys.argv[1])
    dry = '--dry-run' in sys.argv
    results = []
    for line in journal.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line).get('result')
        if isinstance(r, dict) and 'edits' in r and r.get('notebook'):
            results.append(r)

    applied = rejected = 0
    for r in results:
        stu_p = NB / r['notebook']
        ins_p = NB / r['notebook'].replace('_student.ipynb', '_instructor.ipynb')
        if not stu_p.exists() or not ins_p.exists():
            print(f'!! missing pair for {r["notebook"]}'); continue
        ins, stu = load(ins_p), load(stu_p)
        ok = 0
        for e in r['edits']:
            old, new = e['old_text'], e['new_text']
            if old == new:
                continue
            # INSTRUCTOR FIRST — a miss here rejects the edit outright
            i_idx, err = apply_one(ins, old, new)
            if err:
                print(f'  REJECT {r["notebook"]} cell~{e.get("cell_index")} [{e.get("claim","?")}]'
                      f' — instructor copy: {err}')
                rejected += 1
                continue
            # scope 'instructor-only' marks solution cells that exist only in the
            # instructor file (INSTRUCTOR SOLUTION blocks); a student-copy miss is
            # expected there, not a warning.
            if e.get('scope') == 'instructor-only':
                ok += 1
                applied += 1
                continue
            s_idx, serr = apply_one(stu, old, new)
            if serr:
                print(f'  WARN   {r["notebook"]} cell~{e.get("cell_index")} — applied to instructor'
                      f' (cell {i_idx}) but student copy: {serr}')
            ok += 1
            applied += 1
        if ok and not dry:
            save(ins_p, ins)
            save(stu_p, stu)
        print(f'{r["notebook"][:46]:48s} {ok}/{len(r["edits"])} applied')

    print(f'\n{applied} applied, {rejected} rejected across {len(results)} notebooks'
          + (' (DRY RUN — nothing written)' if dry else ''))
    return 1 if rejected else 0


if __name__ == '__main__':
    sys.exit(main())
