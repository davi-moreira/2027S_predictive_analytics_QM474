#!/usr/bin/env python3
"""Apply exact-replacement edits to flat text files from a workflow journal.

Results look like {file, edits:[{old_text,new_text}]}. Each old_text must occur
EXACTLY ONCE in the current file, or the edit is rejected. Exits non-zero if
anything was rejected.

Usage: python scripts/apply_text_edits.py <journal.jsonl> [--dry-run]
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def main():
    journal = Path(sys.argv[1])
    dry = '--dry-run' in sys.argv
    results = []
    for line in journal.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line).get('result')
        if isinstance(r, dict) and 'edits' in r and r.get('file'):
            results.append(r)

    applied = rejected = 0
    for r in results:
        path = REPO / r['file']
        if not path.exists():
            print(f'!! missing {r["file"]}'); continue
        s = path.read_text()
        ok = 0
        for e in r['edits']:
            old, new = e['old_text'], e['new_text']
            n = s.count(old)
            if n != 1:
                print(f'  REJECT {r["file"]}: old_text occurs {n}x (need exactly 1): '
                      f'{old[:80]!r}')
                rejected += 1
                continue
            s = s.replace(old, new)
            ok += 1; applied += 1
        if ok and not dry:
            path.write_text(s)
        print(f'{r["file"]:58s} {ok}/{len(r["edits"])} applied')

    print(f'\n{applied} applied, {rejected} rejected across {len(results)} files'
          + (' (DRY RUN)' if dry else ''))
    sys.exit(1 if rejected else 0)


if __name__ == '__main__':
    main()
