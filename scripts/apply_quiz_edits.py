#!/usr/bin/env python3
"""Apply doctrine edits to quiz-bank CSVs by exact text replacement.

Reads a workflow journal whose results carry {bank, edits:[{q, field,
option_index?, old_text, new_text}]} and rewrites the named CSVs in
_quizzes/2026Summer/. An edit whose old_text does not exactly match the current
stem/option text is REJECTED, never fuzzily applied. Weights (the key) are
never moved. Exits non-zero if anything was rejected.

Usage: python scripts/apply_quiz_edits.py <journal.jsonl> [--dry-run]
"""
import csv
import io
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QDIR = REPO / '_quizzes/2026Summer'


def load_rows(path):
    with open(path, newline='', encoding='utf-8-sig') as fh:
        return [row for row in csv.reader(fh)]


def save_rows(path, rows):
    buf = io.StringIO()
    w = csv.writer(buf, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for row in rows:
        w.writerow(row)
    path.write_text(buf.getvalue(), encoding='utf-8')


def index_questions(rows):
    """Map 1-based question ordinal -> {'stem': row_idx, 'options': [row_idx,...]}."""
    out, cur = [], None
    for i, row in enumerate(rows):
        tag = row[0].strip() if row else ''
        if tag == 'NewQuestion':
            cur = {'stem': None, 'options': []}
            out.append(cur)
        elif tag == 'QuestionText' and cur is not None:
            cur['stem'] = i
        elif tag == 'Option' and cur is not None:
            cur['options'].append(i)
    return {n + 1: q for n, q in enumerate(out)}


def main():
    journal = Path(sys.argv[1])
    dry = '--dry-run' in sys.argv
    results = []
    for line in journal.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line).get('result')
        if isinstance(r, dict) and 'edits' in r and r.get('bank'):
            results.append(r)

    applied = rejected = 0
    for r in results:
        path = QDIR / r['bank']
        if not path.exists():
            print(f'!! missing bank {r["bank"]}'); continue
        rows = load_rows(path)
        qidx = index_questions(rows)
        ok = 0
        for e in r['edits']:
            q = qidx.get(e['q'])
            if q is None:
                print(f'  REJECT {r["bank"]} q{e["q"]}: no such question'); rejected += 1; continue
            if e['field'] == 'stem':
                ri, col = q['stem'], 1
            else:
                oi = e.get('option_index')
                if oi is None or oi >= len(q['options']):
                    print(f'  REJECT {r["bank"]} q{e["q"]}: bad option_index {oi}'); rejected += 1; continue
                ri, col = q['options'][oi], 2
            if rows[ri][col] != e['old_text']:
                print(f'  REJECT {r["bank"]} q{e["q"]} {e["field"]}'
                      f'{e.get("option_index", "")}: old_text does not match current')
                rejected += 1; continue
            rows[ri][col] = e['new_text']
            ok += 1; applied += 1
        if ok and not dry:
            save_rows(path, rows)
        print(f'{r["bank"]:24s} {ok}/{len(r["edits"])} applied')

    print(f'\n{applied} applied, {rejected} rejected across {len(results)} banks'
          + (' (DRY RUN)' if dry else ''))
    sys.exit(1 if rejected else 0)


if __name__ == '__main__':
    main()
