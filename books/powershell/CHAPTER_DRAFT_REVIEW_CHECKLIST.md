# Chapter Draft Review Checklist

Use this checklist before promoting a chapter from `draft` to `stable`.

Goal: catch technical correctness errors, contract violations, outline drift, and Markdown/rendering issues early.

## How To Use

1. Review the chapter against `books/powershell/OUTLINE.yaml`, `books/powershell/PLAN.md`, and adjacent chapters.
2. Record findings by severity: `Critical`, `High`, `Medium`, `Low`.
3. For each finding, include:
   - exact file + line reference
   - what is wrong
   - why it matters (reader impact)
   - concrete fix
4. Re-run a quick validation pass after edits (searches, rendering checks, or command verification where applicable).

## Critical (Teach Readers Something Wrong)

- Does any code example contain invalid syntax?
- Does any example rely on nonexistent cmdlet parameters?
- Are example properties/methods valid for the object type used?
- Are pipeline semantics described correctly (`return`, `continue`, `$_`, formatting cmdlets, etc.)?
- Are examples portable across the versions they claim to support?
- Do sample commands produce the described result (especially benchmark and capstone code)?

## High (Structural / Contract / Severe Friction)

- Chapter frontmatter present and consistent:
  - `Prereqs`
  - `Learning Outcomes`
  - `Key Terms`
  - `Example Labels`
- Required synthesis section present (`Putting It Together`) when expected by chapter pattern.
- Heading hierarchy is valid (no rogue H1/H2 in the middle of deep sections).
- Heading depth follows authoring rule (prefer up to `####`; use bold lead-ins for deeper subtopics).
- Chapter content stays within scope for its place in the learning arc (no hard dependency on much later chapters without fallback).
- Beginner setup friction is addressed (prereqs, modules, permissions, edition differences).

## Medium (Versioning / Outline / Clarity)

- Version-aware callouts added for edition/runtime differences (`Windows PowerShell 5.1 vs PowerShell 7+`).
- 7+-only examples have explicit labels/tags (for example `<!-- Tested on: PowerShell 7.4 -->`).
- `OUTLINE.yaml` matches the chapter's actual major sections.
- Cross-references are added where concepts are shared with other chapters (avoid duplicate deep explanations).
- Capstone examples preserve properties needed by later pipeline stages.
- Anti-pattern examples are clearly labeled as wrong, limited, or illustrative.

## Low (Style / Polish / Rendering)

- Every fenced code block has an example label comment immediately above it.
- Fenced code blocks use explicit language identifiers (`powershell`, `bash`, `text`, etc.).
- Markdown tables render correctly (no blank lines between rows).
- Inline code/backticks render correctly.
- Terminology and property names are consistent within the chapter.
- `Write-Host` is avoided in reusable functions unless specifically teaching host-only output.

## Fast Validation Pass (Recommended)

- `rg -n \"^#####|^######\" <chapter>` (heading-depth violations)
- `rg -n \"^```$\" <chapter>` (blank-language fences)
- `rg -n \"^<!-- (Illustrative|Tested on:)\" <chapter>` and compare count to code fences
- Spot-run key examples in:
  - `powershell.exe` (Windows PowerShell 5.1), if supported by the chapter
  - `pwsh` (PowerShell 7+), if the chapter targets cross-version behavior

## Reviewer Output Template

```text
## [Severity] Short Title
- File/Line:
- Problem:
- Why it matters:
- Fix:
```

## Stable Promotion Gate (Short Form)

- Technical examples are valid and teach correct behavior
- Chapter matches `PLAN.md` contract and authoring rules
- Chapter aligns with `OUTLINE.yaml`
- Version-specific behavior is tagged
- Markdown renders cleanly (headings, tables, code fences)
- No unresolved blockers remain
