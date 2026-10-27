#!/usr/bin/env bash
# Convert instructor notebooks to Markdown for NotebookLM ingestion.
#
# Usage:
#   scripts/sync_instructor_md.sh                       # convert all instructor notebooks
#   scripts/sync_instructor_md.sh notebooks/nb09_*.ipynb # convert one (or several)
#
# Output: _notebook_lm/<basename>.md  (+ <basename>_files/ for embedded images)
#
# Wired to fire automatically from a Claude Code PostToolUse hook
# (.claude/settings.json) and can also be invoked manually or by fswatch.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

OUT_DIR="$REPO_ROOT/_notebook_lm"

mkdir -p "$OUT_DIR"

# Locate a working nbconvert. The repo .venv is preferred when present, but it is
# not required: any interpreter on the box that has nbconvert will do. Hardcoding
# the .venv path meant this script silently no-opped on a machine without one,
# and because it is wired to a PostToolUse hook the skip message was invisible.
NBCONVERT=""
for cand in "$REPO_ROOT/.venv/bin/jupyter-nbconvert" "$(command -v jupyter-nbconvert 2>/dev/null || true)"; do
  if [[ -n "$cand" && -x "$cand" ]]; then NBCONVERT="$cand"; break; fi
done
if [[ -z $NBCONVERT ]]; then
  for py in "$REPO_ROOT/.venv/bin/python3" /usr/local/bin/python3 /opt/homebrew/bin/python3 python3; do
    if command -v "$py" >/dev/null 2>&1 && "$py" -c 'import nbconvert' 2>/dev/null; then
      NBCONVERT="$py -m nbconvert"; break
    fi
  done
fi

if [[ -z $NBCONVERT ]]; then
  echo "sync_instructor_md: FAILED - no interpreter with nbconvert found." >&2
  echo "  _notebook_lm/ is now STALE. Fix with one of:" >&2
  echo "    /usr/local/bin/python3 -m pip install nbconvert" >&2
  echo "    python3 -m venv .venv && .venv/bin/pip install nbconvert" >&2
  exit 0   # exit 0 so a PostToolUse hook never blocks an edit
fi

if [[ $# -gt 0 ]]; then
  TARGETS=("$@")
else
  shopt -s nullglob
  TARGETS=(notebooks/*_instructor.ipynb)
fi

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  echo "sync_instructor_md: no instructor notebooks found"
  exit 0
fi

converted=0
for nb in "${TARGETS[@]}"; do
  # Only act on instructor notebooks; silently skip anything else (lets the
  # hook pass through arbitrary edited paths without erroring).
  case "$(basename "$nb")" in
    *_instructor.ipynb) ;;
    *) continue ;;
  esac
  if [[ ! -f "$nb" ]]; then
    continue
  fi
  echo "→ $nb"
  $NBCONVERT --to markdown --output-dir "$OUT_DIR" "$nb" >/dev/null
  converted=$((converted + 1))
done

echo "sync_instructor_md: converted $converted notebook(s) → $OUT_DIR"
