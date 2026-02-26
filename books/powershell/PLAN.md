# Book plan — PowerShell: From Zero to Toolmaker

This is the *high-level* plan for the PowerShell book. The canonical chapter order lives in `OUTLINE.yaml`.

## Audience

- Readers comfortable with a command line but new to PowerShell
- Readers who want to grow from “one-liners” into maintainable tools/modules

## Guiding principles

1. **Object-first**: teach object inspection early, avoid text-parsing habits as defaults.
2. **Discovery-driven**: `Get-Command`, `Get-Help`, `Get-Member` as core skills.
3. **Scale-aware**: every topic eventually points toward repeatability, testability, and safe ops.
4. **Version-aware**: any behavior that varies across editions should be tagged with “Windows PowerShell 5.1 vs PowerShell 7+”.

## Part-level arc

- **Part I (1–6):** foundations and day-one productivity
- **Part II (7–12):** providers, regex, structured data, CIM/WMI, .NET, scripting basics
- **Part III (13–18):** toolmaking patterns, modules, custom objects, classes/DSL
- **Part IV (19–28):** concurrency and ops: jobs, runspaces, remoting, security, debugging, reporting
- **Part V (29–38):** DSC, Pester, CI/CD, and real-world automation domains
- **Part VI (39–45):** platform breadth, signing, error patterns, future, capstone
- **Appendices (46–50):** references and resources

## Per-chapter “contract” (recommended)

When you revise chapters, consider making the opening consistent:

- **Prereqs** (1–3 bullets)
- **Learning outcomes** (3–7 bullets)
- **Key terms** (short list)
- **Examples** labeled as:
  - *Illustrative* (concept)
  - *Tested on*: OS + PowerShell version + module versions, where relevant

## Markdown Authoring Notes (recommended)

- Prefer heading depth up to `####` for navigational structure.
- If a subsection would require `#####` or deeper, use a **bold lead-in** sentence instead of another heading level to reduce TOC noise and improve ebook rendering.
- Keep Markdown heading text plain (do not wrap headings in `**...**`); headings are already emphasized by renderers.

## Chapter Review Workflow (recommended)

- Before promoting a chapter from `draft` to `stable`, run a review pass using `CHAPTER_DRAFT_REVIEW_CHECKLIST.md`.
- Record findings with severity, file/line references, and concrete fixes so revisions are easy to apply and verify.

## Outline maintenance workflow

- Edit `OUTLINE.yaml` for:
  - chapter order, status (stable/draft), and section headings
- Run scripts (optional) to regenerate TOCs:
  - `scripts/build_catalog.py`
  - `scripts/build_book_readme.py`
