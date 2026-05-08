# Product Launch Guide

Use this guide when the user wants the skill to be shared, published, or positioned as an open-source project.

## Positioning

Primary line:

> Sustainable AI coding starts with a harness.

One-sentence pitch:

> Vibe Harness turns a project plan into the minimal repo context, state board, verification loops, and collaboration rules that let AI coding agents work across sessions.

Short tagline:

> Give agents a runway, not a cage.

## Audience

Serve people who:

- use Codex, Claude Code, Cursor, Copilot, Gemini, or similar coding agents
- start AI coding projects quickly but lose continuity later
- want agent collaboration without heavyweight process
- need `AGENTS.md` and docs that stay useful
- care about tests, evidence, and handoffs but dislike bureaucracy

## Differentiation

Emphasize:

- plan-to-harness workflow, not generic governance
- minimal artifact packs
- progressive disclosure
- honest verification paths
- multi-session and multi-agent continuity
- model freedom inside clear boundaries
- portable Markdown usage instead of platform lock-in

Avoid overclaiming:

- no fake benchmark numbers
- no claims of fully autonomous engineering
- no promise that every agent will auto-trigger the skill
- no Codex-only framing
- no "replace engineers" framing

## README Shape

Lead with:

1. problem: AI coding starts fast but context decays
2. solution: convert project plans into lightweight harnesses
3. quick start prompt
4. what it creates
5. before/after example
6. installation
7. contribution invitation

## Launch Channels

Good first channels:

- GitHub README and topics: `ai-agents`, `codex`, `claude-code`, `cursor`, `github-copilot`, `gemini-cli`, `vibe-coding`, `agents-md`, `context-engineering`, `harness-engineering`, `agent-ready`
- X/LinkedIn post with the tagline and a concrete before/after
- Hacker News "Show HN" once the example and validation are solid
- Reddit communities focused on AI coding and agent workflows
- skill marketplaces after the first release tag
- short demo video showing a project plan becoming `AGENTS.md`, `docs/index.md`, and `progress.md`

## Launch Copy

Short post:

```text
AI coding is great at moving fast. It is bad at remembering why the project exists three sessions later if the context only lives in chat history.

I built Vibe Harness: a skill that turns a project plan into a lightweight repo harness for AI coding: AGENTS.md, docs/index.md, progress.md, validation loops, and multi-agent handoff rules.

Give agents a runway, not a cage.
```

For bilingual launch copy, demo prompts, community posts, and Show HN text, see the repository-level `docs/promotion-kit.md` if it exists.

## Release Checklist

- README explains the pain in the first screen
- README has language links if the project is intended for bilingual adoption
- README has a compatibility section if the project should spread beyond one agent tool
- installation works for at least Codex and Claude Code style skill folders
- `scripts/validate.py` passes
- example project plan exists
- example output exists
- demo script exists
- share copy exists
- license is present
- contribution rules explain what "lightweight" means
- first GitHub release has a changelog and a demo prompt

## Roadmap Ideas

Useful future additions:

- scored harness audit mode
- docs drift checker
- example packs for frontend app, backend API, personal site, data project, and browser extension
- marketplace packaging
- small eval set that compares repeated agent sessions with and without the harness
