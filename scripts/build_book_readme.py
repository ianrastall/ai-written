#!/usr/bin/env python3
"""Generate a book README.md TOC from books/<book>/OUTLINE.yaml.

Usage:
  python scripts/build_book_readme.py books/powershell
"""

from pathlib import Path
import sys
import yaml

def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/build_book_readme.py books/<book>")

    book_dir = Path(sys.argv[1]).resolve()
    outline_path = book_dir / "OUTLINE.yaml"
    readme_path = book_dir / "README.md"

    outline = yaml.safe_load(outline_path.read_text(encoding="utf-8"))
    title = outline["book"]["title"]

    chapters = {c["id"]: c for c in outline.get("chapters", [])}

    lines = [
        f"# {title}",
        "",
        "This folder contains the book source and its canonical outline.",
        "",
        "- `OUTLINE.yaml` is the source of truth for chapter order and section map.",
        "- `chapters/` contains the chapter Markdown files.",
        "",
        "## Table of contents",
        "",
    ]

    for part in outline.get("parts", []):
        lines.append(f"### {part['title']}")
        lines.append("")
        if part.get("description"):
            lines.append(part["description"])
            lines.append("")
        for cid in part.get("chapters", []):
            c = chapters[cid]
            lines.append(f"- **{int(c['num']):02d}.** [{c['title']}]({c['file']}) — *{c['status']}*")
        lines.append("")
    readme_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
