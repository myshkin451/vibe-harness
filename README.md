# Vibe Harness

**Vibe coding starts projects. Vibe Harness keeps them alive.**

[English](README.md) | [简体中文](README.zh-CN.md)

[![Validate](https://github.com/myshkin451/vibe-harness/actions/workflows/validate.yml/badge.svg)](https://github.com/myshkin451/vibe-harness/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/myshkin451/vibe-harness)](https://github.com/myshkin451/vibe-harness/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![Vibe Harness social card](assets/vibe-harness-card.svg)

Vibe Harness is an AI coding skill that turns a human project plan into the minimal repo context, state board, verification loops, and collaboration rules that let agents keep working across sessions.

> Give agents a runway, not a cage.

## The Pain

Vibe coding is fast until the project has memory.

| Before | After Vibe Harness |
| --- | --- |
| Every new session needs the same explanation. | `AGENTS.md` gives agents a short working map. |
| The original product intent lives in chat history. | `docs/index.md` routes durable project context. |
| Nobody knows what was verified. | `progress.md` records current state and evidence. |
| Multi-agent work causes file conflicts. | Work slices and handoff rules define safe parallelism. |
| Docs grow into a stale manual. | The harness stays lightweight and evidence-based. |

## Quick Start

Install the skill:

```bash
git clone https://github.com/myshkin451/vibe-harness.git
cd vibe-harness
mkdir -p ~/.codex/skills
cp -R skills/vibe-harness ~/.codex/skills/vibe-harness
```

Use it in any project:

```text
Use $vibe-harness with docs/project-plan.md to initialize the lightest useful agent-ready harness for this repo.
```

For Claude Code-style skill folders:

```bash
mkdir -p ~/.claude/skills
cp -R skills/vibe-harness ~/.claude/skills/vibe-harness
```

For other coding agents, point them at:

```text
skills/vibe-harness/SKILL.md
```

## What It Creates

Vibe Harness helps an agent create or refresh only the artifacts the project has earned:

- `AGENTS.md`: short entry map for coding agents
- `docs/index.md`: source-of-truth router
- `progress.md`: high-signal state board for multi-session work
- optional `docs/architecture.md`: only when boundaries matter
- optional `docs/exec-plans/`: for long-running or multi-agent work
- optional `docs/decisions/`: for durable tradeoffs
- honest verification paths: commands, browser/API/log evidence, CI, or explicit gaps

## See It Work

Start with the tiny demo:

- input plan: [`examples/project-plan.md`](examples/project-plan.md)
- expected harness: [`examples/expected-harness/`](examples/expected-harness/)
- demo script: [`docs/demo-script.md`](docs/demo-script.md)

Try the example prompt:

```text
Use $vibe-harness with examples/project-plan.md. Create the Seed harness only: AGENTS.md, docs/index.md, and progress.md. Keep unknowns explicit.
```

## Example Project Types

More realistic starting points live in [`examples/project-types/`](examples/project-types/):

- [`personal-site.md`](examples/project-types/personal-site.md)
- [`saas-tool.md`](examples/project-types/saas-tool.md)
- [`backend-api.md`](examples/project-types/backend-api.md)
- [`browser-extension.md`](examples/project-types/browser-extension.md)

## Harness Packs

| Pack | Use When | Creates |
| --- | --- | --- |
| Seed | New idea, prototype, first repo setup | `AGENTS.md`, `docs/index.md`, `progress.md` |
| Working | Implementation spans sessions or agents | Seed plus architecture, exec-plan, decision templates |
| Mature | Real users, CI, deployment, or recurring drift | Working plus drift checks, runbooks, cleanup loops |

Default to Seed. Grow only when the project earns it.

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

## Why This Exists Now

Agentic coding is moving from single prompts to long-running work. The useful pattern is no longer "write a better mega-prompt"; it is giving agents the right repo-local context, verification paths, and handoff surfaces.

Vibe Harness is inspired by the current harness/context engineering direction:

- OpenAI's Codex team describes `AGENTS.md` as a short map, with deeper knowledge living in structured repo docs: [Harness engineering](https://openai.com/index/harness-engineering/).
- OpenAI's Codex launch notes emphasize configured dev environments, reliable tests, clear docs, terminal logs, and test evidence: [Introducing Codex](https://openai.com/index/introducing-codex/).
- Context engineering frames reliability as giving the model the right information and tools at the right step: [Context Engineering for Agents](https://www.langchain.com/blog/context-engineering-for-agents).

This project is not affiliated with Harness.io. It uses "harness" in the agent-engineering sense: the scaffolding that lets agents do reliable work.

## Design Principles

- Map, not manual.
- Evidence, not ceremony.
- Progressive disclosure, not context flooding.
- Mechanical checks beat repeated reminders.
- Multi-agent coordination only when work is actually separable.
- Human judgment stays visible for taste, priority, secrets, destructive actions, and product direction.

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

## Validate

```bash
python3 scripts/validate.py
```

The validator checks skill frontmatter, required files, broken local references, and leftover placeholder markers.

## Share

Want to help it spread? Use the copy in [`docs/promotion-kit.md`](docs/promotion-kit.md).

Short version:

```text
Vibe coding starts projects. Vibe Harness keeps them alive.

It turns project plans into lightweight agent-ready repos: AGENTS.md, docs/index.md, progress.md, verification loops, and multi-agent handoff rules.
```

## Contributing

Contributions are welcome if they make agent work more durable without adding unnecessary process. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

Good first contributions:

- try the skill on a real project plan and share the before/after harness
- add a focused example for one project type
- improve template wording without making it longer
- add a small drift check that catches broken paths or stale commands

## License

MIT
