#!/usr/bin/env python3
"""Sanitize text evidence before it enters a public research repository."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPLACEMENTS = (
    (re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----.*?-----END [A-Z0-9 ]*PRIVATE KEY-----", re.DOTALL), "[REDACTED PRIVATE KEY]"),
    (re.compile(r"(?i)(authorization:\s*(?:bearer|basic)\s+)[^\s]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)((?:api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[REDACTED EMAIL]"),
    (re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), "[REDACTED IP]"),
)


def sanitize_text(text: str) -> str:
    """Return a copy with common sensitive values replaced."""
    result = text
    for pattern, replacement in REPLACEMENTS:
        result = pattern.sub(replacement, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanitize text evidence for portfolio use.")
    parser.add_argument("input", type=Path, help="Text file to sanitize")
    parser.add_argument("-o", "--output", type=Path, help="Write sanitized text to this file")
    args = parser.parse_args()

    source = args.input.read_text(encoding="utf-8")
    sanitized = sanitize_text(source)

    if args.output:
        args.output.write_text(sanitized, encoding="utf-8")
    else:
        print(sanitized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
