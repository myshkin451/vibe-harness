# AGENTS.md

## Start Here

- Project goal: build a small personal publishing site for essays, project notes, and public experiments.
- Current stage: prototype.
- Source-of-truth docs: `docs/index.md`
- Current state board: `progress.md`

## Repository Map

- `src/`: application code, routes, and UI once scaffolded
- `content/`: essays and project notes once added
- `docs/`: project context that should survive across agent sessions

## Validation

- Primary check: not configured yet
- First validation target: add the local dev command and one render/build check after the stack is scaffolded
- Manual evidence: browser screenshot or local page walkthrough for the first publishing loop

## Working Rules

- Get the first publishing loop working before adding deeper architecture docs.
- Keep project context in repo files, not only chat history.
- Update `progress.md` when work changes the current state or spans sessions.
- Do not invent deployment secrets, visual identity decisions, or content strategy.

## Handoff

Before stopping after substantial work, report files changed, validation evidence, remaining gaps, and the next smallest useful action.
