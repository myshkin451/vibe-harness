# Documentation Index

This directory keeps durable project context for Vibe Harness itself.

## Start Here

- `../README.md`: user-facing project overview
- `../README.zh-CN.md`: Chinese project overview
- `../AGENTS.md`: agent entry map for this repository
- `../progress.md`: current state board
- `compatibility.md`: platform-neutral usage notes
- `demo-script.md`: short demo flow

## Skill Package

- `../skills/vibe-harness/SKILL.md`: core agent workflow
- `../skills/vibe-harness/references/artifact-guide.md`: artifact selection and content rules
- `../skills/vibe-harness/references/product-launch.md`: launch positioning guidance
- `../skills/vibe-harness/scripts/audit.py`: static harness audit
- `../skills/vibe-harness/assets/templates/`: copyable harness templates

## Examples

- `../examples/project-plan.md`: small input plan
- `../examples/expected-harness/`: expected Seed harness output
- `../examples/project-types/`: scenario-specific project plans

## Verification

- Package validation: `python3 scripts/validate.py`
- Example audit: `python3 scripts/audit.py examples/expected-harness`
- Optional skill validation: run the skill-creator quick validation script if it is available in the local Codex environment.

## Publishing Context

- `launch-playbook.md`: launch checklist and positioning
- `promotion-kit.md`: copy for external posts

## Maintenance Rules

- Keep this index as a router, not a manual.
- Move detailed usage guidance to README or skill references.
- Update `../progress.md` after changes that affect positioning, validation, or next work.
