# Launch Playbook

This file turns the project into something people can understand, try, and share.

## Category

Vibe Harness is a lightweight repository harness for AI coding projects. It sits between a project plan and an implementation repo.

It is not:

- an agent framework
- a multi-agent roleplay system
- a giant governance template
- a replacement for product judgment
- a Codex-only package

## Core Message

Primary line:

> Sustainable AI coding starts with a harness.

Tagline:

> Give agents a runway, not a cage.

One-sentence pitch:

> Vibe Harness turns project plans into lightweight agent-ready repos for AI coding: AGENTS.md, docs/index.md, progress.md, verification loops, and multi-agent handoff rules.

Compatibility line:

> Works with Codex, Claude Code, Cursor, Copilot, Gemini, and any coding agent that can read Markdown instructions.

## Why It Can Spread

The pain is common:

- people start projects quickly with AI coding agents
- the third or fourth session loses the original intent
- docs either do not exist or become bloated
- multi-agent work creates file conflicts
- validation is unclear
- users do not want enterprise process for a side project
- "vibe coding" is a memorable entry point, but the continuity problem applies to any AI-assisted project that spans sessions, agents, or tools

The project wins if the first use feels like relief: "I can finally start future projects without re-explaining the same operating model."

## Demo Story

Show a small project plan becoming:

- a short `AGENTS.md`
- a `docs/index.md`
- a `progress.md`
- one honest validation path
- one explicit human judgment point

Keep the demo under five minutes.

Use `docs/demo-script.md` for the three-minute version.

## Suggested GitHub Topics

- `ai-agents`
- `codex`
- `claude-code`
- `cursor`
- `github-copilot`
- `gemini-cli`
- `vibe-coding`
- `agents-md`
- `context-engineering`
- `harness-engineering`
- `agent-ready`
- `skills`

## First Launch Post

```text
AI coding is great at moving fast. It is bad at remembering why the project exists three sessions later if the context only lives in chat history.

I built Vibe Harness: a skill that turns a project plan into a lightweight repo harness for AI coding: AGENTS.md, docs/index.md, progress.md, validation loops, and multi-agent handoff rules.

Give agents a runway, not a cage.
```

More launch copy lives in `docs/promotion-kit.md`.

## Launch Checklist

- README explains the pain in the first screen
- README has English and Chinese entry points
- README explains platform-neutral usage
- compatibility docs exist
- install instructions work locally
- `python3 scripts/validate.py` passes
- example project plan exists
- example output exists
- demo script exists
- promotion kit exists
- first release tag exists
- GitHub topics are set
- a short demo prompt is pinned in the README or release notes

## Early Roadmap

1. Add before/after examples for frontend app, backend API, personal site, and data project.
2. Add an audit mode that scores an existing repo's harness readiness.
3. Add a docs drift checker that verifies linked paths and commands.
4. Publish to skill marketplaces once the first users report successful usage.
5. Build a small eval set comparing repeated agent sessions with and without Vibe Harness.
