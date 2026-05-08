# AGENTS.md

## Start Here

- Project goal: [one sentence]
- Current stage: [idea/prototype/first usable loop/production/maintenance]
- Source-of-truth docs: [docs/index.md]
- Current state board: [progress.md]

## Repository Map

- `[path]`: [purpose]
- `[path]`: [purpose]
- `[path]`: [purpose]

## Validation

- Primary check: `[command or manual evidence path]`
- Secondary check: `[optional]`
- If validation cannot run, explain why and record the gap in `progress.md`.

## Working Rules

- Prefer current repo evidence over stale docs.
- Keep changes scoped to the user's request and the active plan.
- Update `progress.md` when work spans sessions or changes project state.
- Add deeper docs only when they route context, preserve decisions, or support verification.
- Do not invent tests, owners, deployment facts, or product decisions.

## Multi-Agent Coordination

- Shared state: `progress.md`
- Long-running plans: `docs/exec-plans/`
- Use parallel agents only for separable work with disjoint write areas.
- Ask the user before destructive actions, secrets, production deployment, broad rewrites, or product-direction changes.

## Handoff

Before stopping after substantial work, report:

- files changed
- validation run and result
- remaining gaps
- next suggested action
