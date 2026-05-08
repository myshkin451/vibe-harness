# Three-Minute Demo Script

Use this script for a short screen recording, launch post, or README demo.

## Goal

Show that Vibe Harness turns a plain project plan into an agent-ready repo without creating a heavy process.

## Setup

Use the example plan:

```text
examples/project-plan.md
```

Open an empty or throwaway repo with Vibe Harness installed.

## Script

### 0:00 - Show The Problem

Say:

> AI coding is great at moving fast, but three sessions later the agent often no longer knows what matters, what was verified, or where to continue.

Show a plain project plan. Point out that it has product intent, risks, and human-only decisions, but no durable agent workflow.

### 0:30 - Invoke Vibe Harness

Prompt:

```text
Use $vibe-harness with examples/project-plan.md. Create the Seed harness only: AGENTS.md, docs/index.md, and progress.md. Keep unknowns explicit.
```

Say:

> The skill does not try to build the product. It turns intent into the smallest useful working environment for future agents.

### 1:15 - Show The Output

Open:

- `AGENTS.md`
- `docs/index.md`
- `progress.md`

Call out:

- `AGENTS.md` is a map, not a manual
- `docs/index.md` says where durable context lives
- `progress.md` carries state across sessions
- unknown validation is explicit instead of faked

Run:

```bash
python3 scripts/audit.py .
```

Point out that the audit checks the harness itself without pretending to run the product's tests.

### 2:15 - Explain Why It Matters

Say:

> This is not governance theater. It is context continuity. Future agents can now inspect the repo, know the current stage, see validation gaps, and continue without asking the same startup questions again.

### 2:45 - Close

Say:

> Give agents a runway, not a cage. AI coding moves fast; Vibe Harness keeps projects coherent.

Show the install command and GitHub URL.

## Recording Tips

- Keep the demo under three minutes.
- Do not show a giant framework or dashboard.
- Show files being created and read.
- Emphasize that the harness starts small.
- Use the same phrase consistently: "map, state, verification, handoff."
