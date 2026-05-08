# Contributing

Thanks for helping make AI coding projects more sustainable.

## What Belongs Here

Good contributions:

- make the skill easier to use in real repos
- improve minimal harness artifact quality
- add small, reusable templates
- improve validation
- clarify multi-session or multi-agent handoffs
- add realistic examples

Avoid:

- large governance systems
- fictional benchmarks
- generic AI hype
- templates that require users to fill a long questionnaire before doing work
- docs that duplicate the skill body

## Development Loop

1. Edit the skill, references, templates, or docs.
2. Run:

```bash
python3 scripts/validate.py
```

3. Test with a realistic project plan.
4. Keep the change small enough that a future agent can understand it quickly.

## Skill Design Rules

- `SKILL.md` should route the workflow.
- `references/` should hold deeper guidance loaded only when needed.
- `assets/templates/` should contain files intended to be copied or adapted.
- README should speak to humans.
- Every new artifact needs a reason to exist.

## Commit Style

Use short, conventional messages when possible:

- `feat: add harness audit prompt`
- `fix: tighten AGENTS template`
- `docs: improve launch copy`
- `test: validate template references`
