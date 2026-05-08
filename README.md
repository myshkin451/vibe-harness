# Vibe Harness

Sustainable vibe coding starts with a harness.

Vibe Harness is an AI coding skill that turns a human project plan into the minimal repo context, state board, verification loops, and collaboration rules that let agents keep working across sessions.

> Give agents a runway, not a cage.

## Why

Vibe coding is great at starting projects. It gets weaker when:

- the agent forgets why decisions were made
- `AGENTS.md` grows into a stale wall of text
- every new session needs the same explanation
- tests and manual validation are unclear
- multiple agents edit overlapping files
- docs drift away from the code

Vibe Harness solves the continuity problem without turning your repo into a governance museum.

## Why This Exists Now

Agentic coding is moving from single prompts to long-running work. The useful pattern is no longer "write a better mega-prompt"; it is giving agents the right repo-local context, verification paths, and handoff surfaces.

Vibe Harness is inspired by the current harness/context engineering direction:

- OpenAI's Codex team describes `AGENTS.md` as a short map, with deeper knowledge living in structured repo docs: [Harness engineering](https://openai.com/index/harness-engineering/).
- OpenAI's Codex launch notes emphasize configured dev environments, reliable tests, clear docs, terminal logs, and test evidence: [Introducing Codex](https://openai.com/index/introducing-codex/).
- Context engineering frames reliability as giving the model the right information and tools at the right step: [Context Engineering for Agents](https://www.langchain.com/blog/context-engineering-for-agents).

This project is not affiliated with Harness.io. It uses "harness" in the agent-engineering sense: the scaffolding that lets agents do reliable work.

## What It Creates

The skill helps an agent create or refresh the lightest useful harness:

- `AGENTS.md`: a short entry map for coding agents
- `docs/index.md`: a source-of-truth router
- `progress.md`: a high-signal state board for multi-session work
- optional `docs/architecture.md`: only when boundaries matter
- optional `docs/exec-plans/`: for long-running or multi-agent work
- optional `docs/decisions/`: for durable tradeoffs
- honest verification paths: commands, browser/API/log evidence, CI, or explicit gaps

## Quick Start

Clone the repo and copy the skill into your Codex skills folder:

```bash
git clone https://github.com/myshkin451/vibe-harness.git
cd vibe-harness
mkdir -p ~/.codex/skills
cp -R skills/vibe-harness ~/.codex/skills/vibe-harness
```

Then invoke it explicitly in a project:

```text
Use $vibe-harness with docs/project-plan.md to initialize the lightest useful agent-ready harness for this repo.
```

For Claude Code-style skill folders:

```bash
mkdir -p ~/.claude/skills
cp -R skills/vibe-harness ~/.claude/skills/vibe-harness
```

For any other AI coding assistant, point it at:

```text
skills/vibe-harness/SKILL.md
```

## Example Prompts

```text
Use $vibe-harness. I have a project plan in docs/project-plan.md. Create only the minimal docs needed so future agents can continue the project safely.
```

```text
Use $vibe-harness to diagnose why agents keep losing context in this repo. Do not add heavy process; find the smallest harness fixes.
```

```text
Use $vibe-harness to refresh AGENTS.md and docs/index.md after this refactor. Ground every claim in current repo evidence.
```

## Harness Packs

- **Seed**: `AGENTS.md`, `docs/index.md`, `progress.md`
- **Working**: Seed plus architecture, exec-plan, and decision templates
- **Mature**: Working plus drift checks, CI links, runbooks, and cleanup loops

Default to Seed. Grow only when the project earns it.

## Repository Layout

```text
skills/vibe-harness/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── artifact-guide.md
│   └── product-launch.md
└── assets/templates/
    ├── agents.md
    ├── docs-index.md
    ├── progress.md
    ├── exec-plan.md
    └── decision.md
```

## Design Principles

- Map, not manual.
- Evidence, not ceremony.
- Progressive disclosure, not context flooding.
- Mechanical checks beat repeated reminders.
- Multi-agent coordination only when work is actually separable.
- Human judgment stays visible for taste, priority, secrets, destructive actions, and product direction.

## Validate

```bash
python3 scripts/validate.py
```

The validator checks skill frontmatter, required files, broken local references, and leftover placeholder markers.

## Launch Positioning

Primary line:

```text
Sustainable vibe coding starts with a harness.
```

Short pitch:

```text
Vibe Harness turns project plans into lightweight agent-ready repos: AGENTS.md, docs/index.md, progress.md, verification loops, and multi-agent handoff rules.
```

See `docs/launch-playbook.md` for launch copy, channels, and release checklist.

## Contributing

Contributions are welcome if they make agent work more durable without adding unnecessary process. Start with `CONTRIBUTING.md`.

Good first contributions:

- try the skill on a real project plan and share the before/after harness
- add a focused example for one project type
- improve template wording without making it longer
- add a small drift check that catches broken paths or stale commands

## License

MIT
