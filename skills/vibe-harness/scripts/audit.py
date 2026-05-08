#!/usr/bin/env python3
"""Audit a repository for lightweight AI-coding harness readiness."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".turbo",
    "coverage",
    "__pycache__",
}

LOCAL_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
COMMAND_LABEL_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?"
    r"(?:primary check|local command|validation command|test command|build command|lint command|"
    r"package validation|skill validation|example audit|harness audit)"
    r"\s*:\s*(.+?)\s*$"
)

GAP_MARKERS = (
    "not configured",
    "not yet verified",
    "not available",
    "no reliable check",
    "no local validation",
    "unknown",
    "tbd",
    "none yet",
)

PATH_SUFFIXES = (
    ".md",
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".txt",
    ".sh",
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str
    suggestion: str = ""


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def rel(repo: Path, path: Path) -> str:
    try:
        return path.relative_to(repo).as_posix()
    except ValueError:
        return path.as_posix()


def iter_markdown(repo: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def iter_harness_markdown(repo: Path) -> list[Path]:
    candidates = [
        repo / "AGENTS.md",
        repo / "progress.md",
        repo / "docs" / "index.md",
        repo / "docs" / "architecture.md",
        repo / "docs" / "harness.md",
        repo / "docs" / "runbook.md",
    ]
    for folder in (repo / "docs" / "exec-plans", repo / "docs" / "decisions"):
        if folder.exists():
            candidates.extend(folder.rglob("*.md"))
    return sorted(path for path in candidates if path.exists())


def add_finding(
    findings: list[Finding],
    severity: str,
    code: str,
    path: str,
    message: str,
    suggestion: str = "",
) -> None:
    findings.append(Finding(severity, code, path, message, suggestion))


def has_heading(text: str, heading: str) -> bool:
    return re.search(rf"(?im)^#+\s+{re.escape(heading)}\s*$", text) is not None


def check_core_files(repo: Path, findings: list[Finding]) -> None:
    core = {
        "AGENTS.md": "Agent entry map",
        "docs/index.md": "Documentation router",
        "progress.md": "Current state board",
    }
    for file_name, label in core.items():
        path = repo / file_name
        if path.exists():
            add_finding(findings, "pass", "core.present", file_name, f"{label} exists.")
        else:
            add_finding(
                findings,
                "fail",
                "core.missing",
                file_name,
                f"{label} is missing.",
                f"Create `{file_name}` or run Vibe Harness Seed setup.",
            )


def check_agents(repo: Path, findings: list[Finding]) -> None:
    path = repo / "AGENTS.md"
    if not path.exists():
        return

    text = read_text(path)
    line_count = len(text.splitlines())
    word_count = len(re.findall(r"\S+", text))

    if line_count > 180 or word_count > 1800:
        add_finding(
            findings,
            "warn",
            "agents.too_long",
            "AGENTS.md",
            f"AGENTS.md is {line_count} lines / {word_count} words.",
            "Keep AGENTS.md as a short map; move detailed context into docs.",
        )
    else:
        add_finding(findings, "pass", "agents.short_map", "AGENTS.md", "AGENTS.md is short enough to act as an entry map.")

    lowered = text.lower()
    if "docs/index.md" not in lowered:
        add_finding(
            findings,
            "warn",
            "agents.no_docs_index",
            "AGENTS.md",
            "AGENTS.md does not point agents to docs/index.md.",
            "Add a source-of-truth docs pointer.",
        )
    if "progress.md" not in lowered:
        add_finding(
            findings,
            "warn",
            "agents.no_progress",
            "AGENTS.md",
            "AGENTS.md does not point agents to progress.md.",
            "Add a current-state pointer.",
        )
    if "validation" not in lowered and "verification" not in lowered:
        add_finding(
            findings,
            "warn",
            "agents.no_validation",
            "AGENTS.md",
            "AGENTS.md does not name a validation or verification path.",
            "Add the most honest available check, even if it is currently missing.",
        )


def check_docs_index(repo: Path, findings: list[Finding]) -> None:
    path = repo / "docs" / "index.md"
    if not path.exists():
        return

    text = read_text(path)
    if has_heading(text, "Start Here") or "start here" in text.lower():
        add_finding(findings, "pass", "docs.start_here", "docs/index.md", "docs/index.md has a start-here section.")
    else:
        add_finding(
            findings,
            "warn",
            "docs.no_start_here",
            "docs/index.md",
            "docs/index.md does not have a clear start-here section.",
            "Add the 2-5 files an agent should read first.",
        )

    if "verification" in text.lower() or "validation" in text.lower():
        add_finding(findings, "pass", "docs.verification", "docs/index.md", "docs/index.md mentions verification.")
    else:
        add_finding(
            findings,
            "warn",
            "docs.no_verification",
            "docs/index.md",
            "docs/index.md does not route verification context.",
            "Add a short validation/verification section.",
        )


def check_progress(repo: Path, findings: list[Finding]) -> None:
    path = repo / "progress.md"
    if not path.exists():
        return

    text = read_text(path)
    lowered = text.lower()
    required = {
        "current status": "Current Status",
        "next actions": "Next Actions",
    }
    for needle, label in required.items():
        if needle in lowered:
            add_finding(findings, "pass", "progress.section", "progress.md", f"progress.md includes {label}.")
        else:
            add_finding(
                findings,
                "warn",
                "progress.missing_section",
                "progress.md",
                f"progress.md is missing {label}.",
                f"Add a `{label}` section so future agents can resume quickly.",
            )

    if "last verified" in lowered or "verification" in lowered or "not yet verified" in lowered:
        add_finding(findings, "pass", "progress.verification", "progress.md", "progress.md records verification state.")
    else:
        add_finding(
            findings,
            "warn",
            "progress.no_verification",
            "progress.md",
            "progress.md does not record verification state.",
            "Add `Last verified` or an explicit validation gap.",
        )


def resolve_markdown_target(repo: Path, source: Path, target: str) -> Path | None:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if "://" in target or target.startswith("#") or target.startswith("mailto:"):
        return None
    clean = unquote(target.split("#", 1)[0].strip())
    if not clean:
        return None
    if clean.startswith("/"):
        return (repo / clean.lstrip("/")).resolve()
    return (source.parent / clean).resolve()


def check_markdown_links(repo: Path, findings: list[Finding]) -> None:
    for path in iter_markdown(repo):
        text = read_text(path)
        for match in LOCAL_LINK_RE.finditer(text):
            target_path = resolve_markdown_target(repo, path, match.group(1))
            if target_path is None:
                continue
            try:
                target_path.relative_to(repo)
            except ValueError:
                add_finding(
                    findings,
                    "fail",
                    "link.escapes_repo",
                    rel(repo, path),
                    f"Local link escapes repo: {match.group(1)}",
                    "Use a repo-local relative link.",
                )
                continue
            if not target_path.exists():
                add_finding(
                    findings,
                    "fail",
                    "link.broken",
                    rel(repo, path),
                    f"Broken local link: {match.group(1)}",
                    "Update or remove the stale link.",
                )


def looks_like_path(value: str) -> bool:
    value = value.strip().strip(".,;:")
    if not value or value.startswith(("http://", "https://", "mailto:", "#", "$", "~", "-")):
        return False
    if any(ch in value for ch in (" ", "|", ">", "<", "*", "?", "{", "}", "$")):
        return False
    if value.endswith(PATH_SUFFIXES):
        return True
    return "/" in value and not value.startswith("/")


def check_inline_paths(repo: Path, findings: list[Finding]) -> None:
    for path in iter_harness_markdown(repo):
        future_section = False
        for line in read_text(path).splitlines():
            lowered_line = line.lower()
            heading = re.match(r"^#+\s+(.+?)\s*$", line)
            if heading:
                heading_text = heading.group(1).lower()
                future_section = any(marker in heading_text for marker in ("add later", "later", "future", "roadmap"))
            future_context = future_section or any(
                marker in lowered_line
                for marker in ("once ", "after ", "future", "add later", "not configured", "not created", "will be")
            )
            for match in INLINE_CODE_RE.finditer(line):
                value = match.group(1).strip()
                if not looks_like_path(value):
                    continue
                source_relative = (path.parent / value).resolve()
                repo_relative = (repo / value).resolve()
                target = source_relative if source_relative.exists() else repo_relative
                try:
                    target.relative_to(repo)
                except ValueError:
                    continue
                if not target.exists():
                    add_finding(
                        findings,
                        "info" if future_context else "warn",
                        "path.future" if future_context else "path.missing",
                        rel(repo, path),
                        f"Inline path reference does not exist: `{value}`",
                        "Update stale path references or mark future paths as not created yet.",
                    )


def load_package_scripts(repo: Path) -> dict[str, str]:
    package_json = repo / "package.json"
    if not package_json.exists():
        return {}
    try:
        data = json.loads(read_text(package_json))
    except json.JSONDecodeError:
        return {}
    scripts = data.get("scripts", {})
    return scripts if isinstance(scripts, dict) else {}


def make_targets(repo: Path) -> set[str]:
    makefile = repo / "Makefile"
    if not makefile.exists():
        return set()
    targets: set[str] = set()
    for line in read_text(makefile).splitlines():
        if line.startswith(("\t", " ", "#", ".")):
            continue
        match = re.match(r"^([A-Za-z0-9_.-]+):", line)
        if match:
            targets.add(match.group(1))
    return targets


def command_from_value(value: str) -> str:
    value = value.strip()
    backtick = re.search(r"`([^`]+)`", value)
    if backtick:
        return backtick.group(1).strip()
    return re.split(r"\s+-\s+|\s+#", value, maxsplit=1)[0].strip()


def is_gap(value: str) -> bool:
    lowered = value.lower()
    return any(marker in lowered for marker in GAP_MARKERS)


def command_support(repo: Path, command: str) -> tuple[str, str]:
    try:
        tokens = shlex.split(command)
    except ValueError:
        tokens = command.split()
    if not tokens:
        return ("unknown", "Empty command.")

    first = tokens[0]
    package_scripts = load_package_scripts(repo)

    if first in {"npm", "pnpm", "bun"}:
        if len(tokens) >= 3 and tokens[1] == "run":
            script = tokens[2]
        elif len(tokens) >= 2 and tokens[1] not in {"install", "i", "add"}:
            script = tokens[1]
        else:
            return ("unknown", "Install/setup command is not treated as validation.")
        if not (repo / "package.json").exists():
            return ("missing", "No package.json found at repo root.")
        if script not in package_scripts:
            return ("missing", f"package.json does not define script `{script}`.")
        return ("supported", f"package.json defines script `{script}`.")

    if first == "yarn":
        if len(tokens) < 2:
            return ("unknown", "Yarn command has no script name.")
        script = tokens[1] if tokens[1] != "run" or len(tokens) < 3 else tokens[2]
        if not (repo / "package.json").exists():
            return ("missing", "No package.json found at repo root.")
        if script not in package_scripts:
            return ("missing", f"package.json does not define script `{script}`.")
        return ("supported", f"package.json defines script `{script}`.")

    if first == "make":
        if len(tokens) < 2:
            return ("unknown", "Make command has no target.")
        target = tokens[1]
        targets = make_targets(repo)
        if not (repo / "Makefile").exists():
            return ("missing", "No Makefile found at repo root.")
        if target not in targets:
            return ("missing", f"Makefile does not define target `{target}`.")
        return ("supported", f"Makefile defines target `{target}`.")

    if first == "pytest" or tokens[:3] == ["python", "-m", "pytest"] or tokens[:3] == ["python3", "-m", "pytest"]:
        if any((repo / name).exists() for name in ("pytest.ini", "pyproject.toml", "setup.cfg", "tox.ini")) or (repo / "tests").exists():
            return ("supported", "Python test config or tests directory exists.")
        return ("missing", "No pytest config or tests directory found.")

    if first == "cargo" and len(tokens) >= 2 and tokens[1] == "test":
        if (repo / "Cargo.toml").exists():
            return ("supported", "Cargo.toml exists.")
        return ("missing", "No Cargo.toml found at repo root.")

    if first == "go" and len(tokens) >= 2 and tokens[1] == "test":
        if (repo / "go.mod").exists():
            return ("supported", "go.mod exists.")
        return ("missing", "No go.mod found at repo root.")

    if first == "uv" and len(tokens) >= 3 and tokens[1] == "run":
        nested = " ".join(tokens[2:])
        return command_support(repo, nested)

    if first in {"python", "python3"} and len(tokens) >= 2 and tokens[1].endswith(".py"):
        script = Path(tokens[1])
        if script.is_absolute():
            return ("unknown", "Python script is outside the audited repo.")
        if (repo / script).exists():
            return ("supported", f"Python script `{script.as_posix()}` exists.")
        return ("missing", f"Python script `{script.as_posix()}` does not exist.")

    return ("unknown", "Command type is not statically verified yet.")


def check_validation_commands(repo: Path, findings: list[Finding]) -> None:
    checked_any = False
    for path in iter_harness_markdown(repo):
        text = read_text(path)
        for match in COMMAND_LABEL_RE.finditer(text):
            value = match.group(1).strip()
            checked_any = True
            if is_gap(value):
                add_finding(
                    findings,
                    "pass",
                    "validation.explicit_gap",
                    rel(repo, path),
                    f"Validation gap is explicit: {value}",
                )
                continue
            command = command_from_value(value)
            status, detail = command_support(repo, command)
            if status == "supported":
                add_finding(
                    findings,
                    "pass",
                    "validation.supported",
                    rel(repo, path),
                    f"Validation command `{command}` has static support. {detail}",
                )
            elif status == "missing":
                add_finding(
                    findings,
                    "warn",
                    "validation.unsupported",
                    rel(repo, path),
                    f"Validation command `{command}` is not supported by repo config. {detail}",
                    "Fix the command or add the missing config/script.",
                )
            else:
                add_finding(
                    findings,
                    "info",
                    "validation.unchecked",
                    rel(repo, path),
                    f"Validation command `{command}` was not statically checked. {detail}",
                    "Manually verify this command and record evidence in progress.md.",
                )

    if not checked_any:
        add_finding(
            findings,
            "warn",
            "validation.missing",
            ".",
            "No labeled validation command or explicit validation gap found.",
            "Add `Primary check: ...` or `Local command: not configured yet` to AGENTS.md/docs/index.md.",
        )


def pack_signal(repo: Path) -> str:
    seed = all((repo / path).exists() for path in ("AGENTS.md", "docs/index.md", "progress.md"))
    working = any(
        (repo / path).exists()
        for path in ("docs/architecture.md", "docs/exec-plans", "docs/decisions")
    )
    mature = any(
        (repo / path).exists()
        for path in (".github/workflows", "docs/runbook.md", "docs/harness.md")
    )
    if seed:
        extras: list[str] = []
        if working:
            extras.append("working docs")
        if mature:
            extras.append("CI/runbook signals")
        if extras:
            return f"Seed harness + {', '.join(extras)}"
        return "Seed harness"
    return "Needs Seed harness"


def score(findings: list[Finding]) -> int:
    value = 100
    for finding in findings:
        if finding.severity == "fail":
            value -= 15
        elif finding.severity == "warn":
            value -= 7
    return max(0, value)


def audit(repo: Path) -> dict[str, object]:
    repo = repo.resolve()
    findings: list[Finding] = []
    check_core_files(repo, findings)
    check_agents(repo, findings)
    check_docs_index(repo, findings)
    check_progress(repo, findings)
    check_markdown_links(repo, findings)
    check_inline_paths(repo, findings)
    check_validation_commands(repo, findings)
    result_score = score(findings)
    return {
        "repo": repo.as_posix(),
        "score": result_score,
        "pack": pack_signal(repo),
        "summary": {
            "pass": sum(1 for item in findings if item.severity == "pass"),
            "info": sum(1 for item in findings if item.severity == "info"),
            "warn": sum(1 for item in findings if item.severity == "warn"),
            "fail": sum(1 for item in findings if item.severity == "fail"),
        },
        "findings": [asdict(item) for item in findings],
    }


def print_text(result: dict[str, object]) -> None:
    summary = result["summary"]
    assert isinstance(summary, dict)
    print("Vibe Harness Audit")
    print(f"Repo: {result['repo']}")
    print(f"Score: {result['score']}/100")
    print(f"Pack: {result['pack']}")
    print(
        "Findings: "
        f"{summary['pass']} pass, {summary['info']} info, {summary['warn']} warn, {summary['fail']} fail"
    )
    print()

    findings = result["findings"]
    assert isinstance(findings, list)
    order = {"fail": 0, "warn": 1, "info": 2, "pass": 3}
    for item in sorted(findings, key=lambda entry: (order.get(entry["severity"], 9), entry["path"], entry["code"])):
        prefix = item["severity"].upper()
        print(f"{prefix:4} {item['code']} [{item['path']}] {item['message']}")
        if item.get("suggestion"):
            print(f"     fix: {item['suggestion']}")

    next_fixes = [item for item in findings if item["severity"] in {"fail", "warn"}]
    if next_fixes:
        print()
        print("Next smallest fixes:")
        for index, item in enumerate(next_fixes[:5], start=1):
            suggestion = item.get("suggestion") or item["message"]
            print(f"{index}. {suggestion}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit a repo for Vibe Harness readiness.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path to audit.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when warnings or failures are found.")
    args = parser.parse_args(argv)

    repo = Path(args.repo)
    if not repo.exists():
        print(f"FAIL: repo path does not exist: {repo}", file=sys.stderr)
        return 2
    if not repo.is_dir():
        print(f"FAIL: repo path is not a directory: {repo}", file=sys.stderr)
        return 2

    result = audit(repo)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_text(result)

    summary = result["summary"]
    assert isinstance(summary, dict)
    if args.strict and (summary["fail"] or summary["warn"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
