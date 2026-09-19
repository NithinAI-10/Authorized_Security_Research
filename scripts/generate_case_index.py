#!/usr/bin/env python3
"""Generate a Markdown index from sanitized case study files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def build_index(case_dir: Path) -> str:
    """Build an index using only local Markdown titles and file names."""
    rows = ["# Case Study Index", "", "Sanitized case studies prepared for public portfolio review.", ""]
    for path in sorted(case_dir.glob("case-*.md")):
        text = path.read_text(encoding="utf-8")
        match = TITLE.search(text)
        title = match.group(1).strip() if match else path.stem.replace("-", " ").title()
        rows.append(f"- [{title}]({path.name})")
    rows.append("")
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the sanitized case study index.")
    parser.add_argument("case_dir", nargs="?", type=Path, default=Path("case-studies"))
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    content = build_index(args.case_dir)
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
