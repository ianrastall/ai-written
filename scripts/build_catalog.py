#!/usr/bin/env python3
"""Generate CATALOG.md from CATALOG.yaml.

Usage:
  python scripts/build_catalog.py
"""

from pathlib import Path
import yaml
from datetime import date

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    catalog_path = ROOT / "CATALOG.yaml"
    md_path = ROOT / "CATALOG.md"

    data = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    lines = [
        "# Catalog",
        "",
        "This repo is a library of programming textbooks/tutorial notes (Markdown-first).",
        "",
        "| Book | Status | Maturity | Path |",
        "|---|---:|---:|---|",
    ]

    for b in data.get("books", []):
        lines.append(f"| **{b['title']}** | {b['status']} | {b['maturity']} | `{b['path']}` |")

    lines += ["", f"_Generated {date.today().isoformat()} from `CATALOG.yaml`._"]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
