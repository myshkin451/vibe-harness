# Artifact Guide

Use this guide when deciding which harness artifacts to create or refresh.

## Principle

Each artifact needs a job. If an artifact does not route context, preserve state, guide verification, record a durable decision, or coordinate work, skip it.

## Core Artifacts

### AGENTS.md

Purpose: the repo entry map for coding agents.

Good content:

- where to start
- package/module map
- exact validation commands
- important docs that outrank the map
- project-specific constraints
- handoff and safety rules

Keep it around 80-120 lines. Link out instead of copying deep explanations.

Avoid:

- long essays
- generic coding advice
- historical detail
- duplicate style guides
- aspirations not backed by code, docs, or tests

### docs/index.md

Purpose: the source-of-truth router.

Good content:

- active docs and what each one is for
- which docs are canonical
- which docs are archived or generated
- where future agents should write plans, decisions, and runbooks

### progress.md

Purpose: cross-session state board.

Good content:

- current status
- completed work slices
- active risks
- next actions
- validation evidence
- open questions

Keep it high signal. Do not turn it into a chat log.

### docs/architecture.md

Create only when the repo has meaningful boundaries.

Good content:

- domain/module boundaries
- data flow
- integration points
- constraints that affect implementation
- where mechanical enforcement lives

If architecture is still unknown, write a short "current shape" section and an "unknowns" section.

### docs/exec-plans/

Use for long-running work, multi-agent slices, risky migrations, or anything likely to span sessions.

An exec plan should include:

- goal
- scope
- ownership
- phases
- validation
- progress log
- decisions
- rollback or stop conditions

### docs/decisions/

Use when a decision will shape future implementation.

Record:

- context
- decision
- alternatives considered
- consequences
- revisit trigger

### docs/harness.md

Create only when the harness itself needs explanation.

Good content:

- artifact map
- verification map
- agent collaboration conventions
- drift management
- how to change the harness

## Harness Depth

### Seed

Use for new projects and early prototypes.

Create:

- `AGENTS.md`
- `docs/index.md`
- `progress.md`

### Working

Use when implementation is underway or multiple sessions will touch the repo.

Create Seed plus:

- `docs/architecture.md`
- `docs/exec-plans/_template.md`
- `docs/decisions/_template.md`

### Mature

Use when the repo has real users, CI, deployment, or multiple agents.

Create Working plus selected:

- `docs/harness.md`
- drift checks
- operator runbooks
- CI/documentation link checks
- periodic cleanup plan

## Verification Rules

Prefer exact commands and evidence:

- `npm test`
- `pnpm lint`
- `pytest`
- `make check`
- browser walkthrough
- API call with request and response
- log/trace query
- CI workflow name

If no check exists, say so and propose the smallest first check.

## Multi-Agent Rules

Only add coordination where the work needs it.

Useful coordination content:

- disjoint file ownership
- active plan location
- current branch/worktree assumptions
- how to preserve or close local servers
- when to ask the user
- what each agent must report before stopping

Avoid:

- permanent role hierarchies before there is enough work
- broad "architect/reviewer/builder" theater
- making every small edit require a plan
