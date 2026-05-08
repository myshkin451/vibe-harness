# Vibe Harness Repository Guide

## Start Here

- Main skill: `skills/vibe-harness/SKILL.md`
- Source-of-truth docs: `docs/index.md`
- Current state board: `progress.md`
- Detailed skill references: `skills/vibe-harness/references/`
- Copyable templates: `skills/vibe-harness/assets/templates/`
- Repo validation: `scripts/validate.py`
- Audit script: `scripts/audit.py`
- Launch guidance: `docs/launch-playbook.md`

## Project Goal

Vibe Harness turns a human project plan into a lightweight agent-ready repository harness for sustainable AI coding.

## Working Rules

- Keep the skill body concise; move deeper guidance to `skills/vibe-harness/references/`.
- Keep templates generic, small, and easy to adapt.
- Do not add heavyweight governance artifacts unless they solve a clear continuity or verification problem.
- Prefer concrete paths, commands, and evidence over broad agent philosophy.
- Do not make unverified adoption, benchmark, or compatibility claims.

## Validation

Run before finishing changes:

```bash
python3 scripts/validate.py
python3 scripts/audit.py examples/expected-harness
```

If validation cannot run, explain why and record the likely impact.

## Release Shape

The repo should stay installable as a skill package and understandable as an open-source project. README is for users; `skills/vibe-harness/SKILL.md` is for agents; `docs/launch-playbook.md` is for maintainers preparing public launch.
