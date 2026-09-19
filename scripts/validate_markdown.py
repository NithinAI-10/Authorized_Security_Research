#!/usr/bin/env python3
"""Check public Markdown for basic structure and sensitive-data patterns."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SENSITIVE = (
    ("private key", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
    ("authorization value", re.compile(r"(?i)authorization:\s*(?:bearer|basic)\s+(?!\[REDACTED\])\S+")),
    ("email address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
)


def validate_file(path: Path) -> list[str]:
    """Return validation errors for one Markdown file."""
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.strip():
        errors.append("file is empty")
    if text.strip() and not re.search(r"^#\s+\S", text, re.MULTILINE):
        errors.append("missing level-one heading")
    for label, pattern in SENSITIVE:
        if pattern.search(text):
            errors.append(f"possible {label}")
    return errors


def markdown_files(root: Path) -> list[Path]:
    """Return Markdown files under a file or directory path."""
    return [root] if root.is_file() else sorted(root.rglob("*.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate public Markdown files.")
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    args = parser.parse_args()

    failures = 0
    for path in markdown_files(args.root):
        for error in validate_file(path):
            failures += 1
            print(f"{path}: {error}")
    if failures:
        return 1
    print("Markdown validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
