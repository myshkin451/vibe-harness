# Compatibility

Vibe Harness is intentionally platform-neutral.

It is packaged as a skill because skill folders are a convenient way to ship reusable instructions, templates, and references. But the core workflow is portable Markdown:

```text
skills/vibe-harness/SKILL.md
```

If an agent can read repository files, it can use Vibe Harness.

## Integration Levels

| Level | What It Means | Works With |
| --- | --- | --- |
| Native skill | The tool discovers or loads `SKILL.md` as a reusable skill | Codex, Claude Code-style systems |
| Project rule | The tool is told to read the skill as part of project instructions | Cursor, Copilot, many IDE agents |
| Explicit prompt | The user asks the agent to read `SKILL.md` for this task | Any file-reading coding agent |
| Manual copy | The user pastes the skill instructions into a chat | Any LLM, least ergonomic |

## Codex

Install:

```bash
mkdir -p ~/.codex/skills
cp -R skills/vibe-harness ~/.codex/skills/vibe-harness
```

Invoke:

```text
Use $vibe-harness with docs/project-plan.md to initialize the lightest useful agent-ready harness for this repo.
```

## Claude Code

Install:

```bash
mkdir -p ~/.claude/skills
cp -R skills/vibe-harness ~/.claude/skills/vibe-harness
```

Invoke:

```text
Use the vibe-harness skill with docs/project-plan.md to initialize the lightest useful agent-ready harness.
```

## Cursor

Use it as a project rule or explicit instruction.

Example prompt:

```text
Read skills/vibe-harness/SKILL.md, then use it with docs/project-plan.md. Create only the Seed harness unless the repo already needs more.
```

If the repo uses Cursor rules, add a short rule pointing to `skills/vibe-harness/SKILL.md` instead of copying the whole skill into the rule.

## GitHub Copilot Coding Agent

Use it through repository instructions or the task prompt.

Example task:

```text
Before editing, read skills/vibe-harness/SKILL.md. Use it to create the lightest useful harness for the project plan in docs/project-plan.md.
```

For best results, keep `AGENTS.md` in the target repo short and point it at the skill or generated harness docs.

## Gemini CLI And Other Agents

Use explicit file reading:

```text
Read skills/vibe-harness/SKILL.md and follow its workflow for this project plan: docs/project-plan.md.
```

## Notes On Automatic Invocation

Automatic skill invocation is not portable.

- Some tools can auto-detect skills from a folder.
- Some tools need explicit invocation.
- Some tools only support repo rules or pasted context.

Vibe Harness does not depend on automatic invocation. The portable contract is:

```text
Read SKILL.md, inspect the repo, create the lightest useful harness, keep unknowns explicit.
```

## What To Avoid

- Do not copy the entire skill into every `AGENTS.md`.
- Do not assume `$vibe-harness` syntax works outside tools that support it.
- Do not promise auto-trigger behavior across platforms.
- Do not turn compatibility notes into a long setup manual.
