#!/usr/bin/env python3
"""Convenience entrypoint for the bundled Vibe Harness audit script."""

from __future__ import annotations

import runpy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "vibe-harness" / "scripts" / "audit.py"

if __name__ == "__main__":
    runpy.run_path(SCRIPT.as_posix(), run_name="__main__")
