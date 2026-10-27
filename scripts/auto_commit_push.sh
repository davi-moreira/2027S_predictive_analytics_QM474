#!/usr/bin/env bash
# auto_commit_push.sh — invoked by the Stop hook to always commit and push.
# Stages every tracked/untracked change (honoring .gitignore), commits with a
# timestamped message, and pushes the current branch to origin.
#
# Notes:
#  - Exits 0 with no commit when the working tree is clean (nothing to do).
#  - All output goes to stderr so it surfaces in the hook log without being
#    interpreted as structured hook JSON.
#  - Push failures (offline, auth, non-fast-forward) are reported but never
#    block the session.

set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

# Only act inside a git repo.
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

# Nothing changed? Done.
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

branch="$(git branch --show-current)"

git add -A

git commit -m "chore: Auto-commit $(date '+%Y-%m-%d %H:%M:%S')

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>" >&2 \
  || { echo "auto_commit_push: nothing committed" >&2; exit 0; }

if ! git push origin "$branch" >&2 2>&1; then
  echo "auto_commit_push: push failed (commit is saved locally on '$branch')" >&2
fi

exit 0
