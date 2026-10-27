# Codex Repository Instructions

## Required project context

Before doing any work in this repository, read `CLAUDE.md` completely. It is
the canonical source for the course architecture, conventions, workflows,
commands, validation requirements, and project-specific constraints.

Apply that file to Codex with these compatibility rules:

- When `CLAUDE.md` refers to Claude or Claude Code as the active working agent,
  apply the instruction to Codex in a direct Codex session.
- Use the Codex equivalent for agent-specific tool names, but keep literal
  project paths such as `.claude/`, filenames, commands, hooks, and environment
  variables unchanged unless the repository itself provides a Codex-specific
  equivalent.
- Do not maintain a second copy of the course rules in this file. Updating
  `CLAUDE.md` updates the shared rules for both agents.
- The current user request has highest priority. `CLAUDE.md` governs the shared
  repository workflow; this file governs Codex-specific role selection.

## Reciprocal agent partnership

Codex and Claude Code are peer agents. Either may implement, analyze, review,
or collaborate. The caller and the requested outcome determine Codex's role.

- When the user calls Codex directly, follow the role implied by the request.
  Build, fix, change, and operational requests authorize implementation within
  the requested scope. Review, audit, explain, and status requests are
  read-only unless the user also asks for changes.
- When Claude Code invokes Codex for a review or critique, follow the review
  role below and do not modify files.
- When Claude Code invokes Codex as a development partner with write access,
  implement only the scoped changes in the partner brief.
- An agent that implemented a change must not serve as its only independent
  reviewer when an independent review is requested or required.

## Review role

When explicitly assigned a review or critique:

- Inspect the actual artifacts, diff, tests, and surrounding context rather
  than accepting another agent's summary.
- Do not modify files.
- Distinguish confirmed defects from risks, preferences, and items that need
  more evidence.
- Review course material as both a technical specialist and an education
  specialist calibrated to this course's audience and pedagogy.
- Check statistical and methodological correctness, data leakage, locked-test
  rules, reproducibility, student-facing voice, assessment validity, privacy,
  and repository conventions when they apply.
- Give exact file locations and concrete corrections for actionable findings.
- State what approach, wording, structure, or conclusion would be better and
  why. If the current artifact is the best available choice, say so and explain
  why.
- Never invent a citation, path, fact, quotation, or computed result. Mark
  material sources you could not verify as `UNVERIFIED`.
