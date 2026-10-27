#!/usr/bin/env bash
# Build the course data archive: _data/data.zip
#
# Deliberately edition-agnostic — it carries only the datasets the notebook arc
# uses, so the same archive can be posted in any offering of the course. The
# per-edition case-competition files live with their edition under
# _course_case_competition/<term>/ and are NOT included here.
#
# Extracting data.zip creates exactly one folder: data/
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/_data/data.zip"

FILES=(
  "$ROOT/notebooks/california_housing.csv"
  "$ROOT/notebooks/us_employment.csv"
)
for f in "${FILES[@]}"; do
  [ -f "$f" ] || { echo "missing dataset: $f" >&2; exit 1; }
done

STAGE="$(mktemp -d)/data"
mkdir -p "$STAGE"
cp "${FILES[@]}" "$STAGE/"

rm -f "$OUT"
( cd "$(dirname "$STAGE")" && zip -q -r "$OUT" data -x '*.DS_Store' )
echo "built $OUT"
unzip -l "$OUT"
