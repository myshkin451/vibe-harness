#!/usr/bin/env python3
"""Validate the Vibe Harness skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "vibe-harness"

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/launch-playbook.md",
    "skills/vibe-harness/SKILL.md",
    "skills/vibe-harness/agents/openai.yaml",
    "skills/vibe-harness/references/artifact-guide.md",
    "skills/vibe-harness/references/product-launch.md",
    "skills/vibe-harness/assets/templates/agents.md",
    "skills/vibe-harness/assets/templates/docs-index.md",
    "skills/vibe-harness/assets/templates/progress.md",
    "skills/vibe-harness/assets/templates/exec-plan.md",
    "skills/vibe-harness/assets/templates/decision.md",
    "examples/project-plan.md",
    "examples/expected-harness/AGENTS.md",
    "examples/expected-harness/docs/index.md",
    "examples/expected-harness/progress.md",
]

ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
LOCAL_LINK_RE = re.compile(r"\]\(([^)]+)\)")
BAD_MARKERS = ("TO" + "DO", "[TO" + "DO")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value
    return data


def validate_skill_frontmatter() -> None:
    skill_md = SKILL / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    data = parse_frontmatter(text)

    unexpected = set(data) - ALLOWED_FRONTMATTER
    if unexpected:
        fail(f"Unexpected SKILL.md frontmatter keys: {sorted(unexpected)}")

    name = data.get("name", "")
    if name != "vibe-harness":
        fail("SKILL.md name must be vibe-harness")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        fail("Skill name must be lowercase hyphen-case")

    description = data.get("description", "")
    if not description:
        fail("SKILL.md description is required")
    if len(description) > 1024:
        fail("SKILL.md description must be <= 1024 chars")
    if any(marker in description for marker in BAD_MARKERS):
        fail("SKILL.md description still contains placeholder text")


def validate_required_files() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            fail(f"Missing required file: {rel}")
        if path.is_file() and path.stat().st_size == 0:
            fail(f"Required file is empty: {rel}")


def validate_no_placeholders() -> None:
    allowed = {
        "skills/vibe-harness/assets/templates/agents.md",
        "skills/vibe-harness/assets/templates/docs-index.md",
        "skills/vibe-harness/assets/templates/progress.md",
        "skills/vibe-harness/assets/templates/exec-plan.md",
        "skills/vibe-harness/assets/templates/decision.md",
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in allowed:
            continue
        if path.suffix not in {".md", ".yaml", ".yml", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in BAD_MARKERS):
            fail(f"Unexpected placeholder marker in {rel}")


def validate_local_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in LOCAL_LINK_RE.finditer(text):
            target = match.group(1)
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"Local link escapes repo in {path.relative_to(ROOT)}: {target}")
            if not resolved.exists():
                fail(f"Broken local link in {path.relative_to(ROOT)}: {target}")


def validate_openai_yaml() -> None:
    text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$vibe-harness" not in text:
        fail("agents/openai.yaml default_prompt must mention $vibe-harness")


def main() -> None:
    validate_required_files()
    validate_skill_frontmatter()
    validate_openai_yaml()
    validate_no_placeholders()
    validate_local_links()
    print("OK: Vibe Harness package is valid")


if __name__ == "__main__":
    main()
