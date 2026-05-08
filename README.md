# Vibe Harness

**A lightweight repository harness for AI coding projects.**

[English](README.md) | [简体中文](README.zh-CN.md)

[![Validate](https://github.com/myshkin451/vibe-harness/actions/workflows/validate.yml/badge.svg)](https://github.com/myshkin451/vibe-harness/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/myshkin451/vibe-harness)](https://github.com/myshkin451/vibe-harness/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![Vibe Harness social card](assets/vibe-harness-card.svg)

Vibe Harness is a portable AI coding skill that turns a human project plan into durable repo context, progress tracking, verification loops, and handoff rules so AI coding work can continue across sessions, agents, and tools.

> Give agents a runway, not a cage.

## The Problem

AI coding is fast until the project needs memory, verification, and handoff.

| Before | After Vibe Harness |
| --- | --- |
| Every new session needs the same explanation. | `AGENTS.md` gives agents a short working map. |
| The original product intent lives in chat history. | `docs/index.md` routes durable project context. |
| Nobody knows what was verified. | `progress.md` records current state and evidence. |
| Multi-agent work causes file conflicts. | Work slices and handoff rules define safe parallelism. |
| Docs grow into a stale manual. | The harness stays lightweight and evidence-based. |

Vibe coding is one visible version of this problem. The deeper need is broader: any AI-coded project that survives past the first session needs a small project memory layer.

## Not Just Vibe Coding

Use Vibe Harness for:

- quick prototypes that need to become maintainable
- production apps built with coding agents
- team repos using async PR agents
- personal projects you will resume weeks later
- multi-agent work where context and ownership can drift

If an AI coding project will be touched again, handed off, verified, or resumed, it can use a harness.

## Works With

Vibe Harness is platform-neutral Markdown. Native skill loading varies by product, but the minimum integration is always:

```text
Read skills/vibe-harness/SKILL.md and use it to turn this project plan into the lightest useful agent-ready harness.
```

| Agent / Tool | Best Use | Invocation |
| --- | --- | --- |
| Codex | Native skill folder | `Use $vibe-harness ...` |
| Claude Code | Native skill folder | `Use the vibe-harness skill ...` |
| Cursor | Project rule or explicit prompt | `Read skills/vibe-harness/SKILL.md ...` |
| GitHub Copilot Coding Agent | Repo instructions plus explicit prompt | Reference `SKILL.md` from the task |
| Gemini CLI / other coding agents | Portable instruction package | Ask the agent to read `SKILL.md` |

Auto-invocation is platform-specific. The skill itself is just Markdown plus templates, so it remains usable anywhere an agent can read files.

See [`docs/compatibility.md`](docs/compatibility.md) for details.

## Quick Start

Clone the repo:

```bash
git clone https://github.com/myshkin451/vibe-harness.git
cd vibe-harness
```

Use directly with any file-reading coding agent:

```text
Read skills/vibe-harness/SKILL.md and use it with docs/project-plan.md to initialize the lightest useful agent-ready harness for this repo.
```

Optional native install for Codex:

```bash
mkdir -p ~/.codex/skills
cp -R skills/vibe-harness ~/.codex/skills/vibe-harness
```

Then invoke:

```text
Use $vibe-harness with docs/project-plan.md to initialize the lightest useful agent-ready harness for this repo.
```

Optional native install for Claude Code-style skill folders:

```bash
mkdir -p ~/.claude/skills
cp -R skills/vibe-harness ~/.claude/skills/vibe-harness
```

For Cursor, Copilot Coding Agent, Gemini CLI, or any other coding agent, point the agent at:

```text
skills/vibe-harness/SKILL.md
```

## Audit A Repo

Vibe Harness includes a static audit script so the project is not only a template pack:

```bash
python3 scripts/audit.py /path/to/repo
```

It checks for missing harness files, broken Markdown links, stale path references, progress-state gaps, and validation commands that are not backed by obvious repo config. It does not execute project commands by default.

Try it on the included example:

```bash
python3 scripts/audit.py examples/expected-harness
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
Read skills/vibe-harness/SKILL.md and use it with examples/project-plan.md. Create the Seed harness only: AGENTS.md, docs/index.md, and progress.md. Keep unknowns explicit.
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
Read skills/vibe-harness/SKILL.md. I have a project plan in docs/project-plan.md. Create only the minimal docs needed so future agents can continue the project safely.
```

```text
Use Vibe Harness to diagnose why agents keep losing context in this repo. Do not add heavy process; find the smallest harness fixes.
```

```text
Use Vibe Harness to refresh AGENTS.md and docs/index.md after this refactor. Ground every claim in current repo evidence.
```

## Why This Exists Now

Agentic coding is moving from single prompts to long-running work. The useful pattern is no longer "write a better mega-prompt"; it is giving agents the right repo-local context, verification paths, and handoff surfaces.

Vibe coding is the sharpest entry point because it exposes the failure quickly, but the harness is for the wider category: AI-assisted engineering, async coding agents, multi-session implementation, and multi-agent collaboration.

Vibe Harness is inspired by the current harness/context engineering direction across coding-agent tools:

- One influential Codex case study describes `AGENTS.md` as a short map, with deeper knowledge living in structured repo docs: [Harness engineering](https://openai.com/index/harness-engineering/).
- Modern coding-agent workflows increasingly emphasize configured dev environments, reliable tests, clear docs, terminal logs, and test evidence: [Introducing Codex](https://openai.com/index/introducing-codex/).
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
├── scripts/audit.py
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
AI coding moves fast. Vibe Harness keeps projects coherent.

It turns project plans into lightweight agent-ready repos for AI coding: AGENTS.md, docs/index.md, progress.md, verification loops, and multi-agent handoff rules.
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
