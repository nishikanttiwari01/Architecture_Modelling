# Build and Repository Validation

Validation date: 2026-06-28

## Scope verified

- Required project-control files
- Full manuscript structure
- Chapters 1 to 63
- Front matter and appendices
- BIAN business and technical sections
- Templates, research, diagram, example and review folders
- Python utilities and PowerShell wrapper
- GitHub Actions workflow
- Internal Markdown links
- Terminology and basic style rules
- Combined-manuscript build order
- ZIP integrity and Windows-compatible paths

## Repository structure

- Total repository files: 132
- Markdown files: 123
- Manuscript Markdown files: 75
- Numbered chapters: 63, consecutively numbered from 1 to 63
- Front-matter files: 4
- Appendix files: 8
- Empty files: 0
- Duplicate chapter headings: 0
- Invalid Windows paths: 0
- Maximum relative path length: 80 characters

`BOOK_PLAN.md`, `STATUS.md`, the table of contents and all chapter H1 titles agree on chapter numbers and names.

## Corrected during verification

- Removed duplicate `Practical exercise` headings from BIAN chapter stubs.
- Removed duplicate `Review checklist` headings from diagram-selection chapter stubs.
- Corrected the combined-manuscript front-matter order.
- Added a cross-platform Python manuscript builder.
- Added structural validation and GitHub Actions automation.
- Added missing research areas for DMN, domain/event modelling, infrastructure, modelling tools and banking.

## Automated checks

### `python scripts/check-structure.py`

Result: Passed

```text
Repository structure check passed.
Validated 63 numbered chapters (1 to 63).
BOOK_PLAN.md, STATUS.md, table of contents and chapter titles agree.
Required control files, directories, frontmatter and chapter sections exist.
No duplicate chapter headings were found.
```

### `python scripts/check-links.py`

Result: Passed

```text
Checked 126 local Markdown links.
All local links are valid.
```

### `python scripts/check-terminology.py`

Result: Passed

```text
Terminology and basic style checks passed.
```

### Python compilation

Result: Passed

```text
python -m py_compile scripts/*.py
```

### `python scripts/build-book.py`

Result: Passed

```text
Included 75 manuscript files in explicit book order.
```

Verified order:

1. Title
2. Preface
3. How to Use This Book
4. Table of Contents
5. Chapters 1 to 63
6. Appendices A to H

The test build contained 74 page breaks and produced a combined Markdown file of approximately 260 KB. Test build output was removed before packaging because `build/` is generated content.

### `python scripts/word-count.py`

Result: Passed

Current structured starter content: 34,260 words. This count includes chapter briefs, placeholders, front matter and appendices; it is not a finished-manuscript word count.

### GitHub Actions workflow

Result: YAML parsed successfully. The workflow runs structure, link and terminology checks, builds the combined Markdown file and reports word counts on pushes to `main` and pull requests.

## PowerShell note

The PowerShell wrapper could not be executed in the Linux validation environment because PowerShell was unavailable. Its core operation delegates to the tested `scripts/build-book.py` builder. The wrapper also checks the Python and optional Pandoc exit codes.

## Content-state clarification

The repository is a complete **book-production starter repository**, not a completed book. Chapter files contain detailed drafting briefs, planned subsections, expected diagrams, exercises and review criteria. Research folders and diagram folders contain instructions and placeholders; verified research notes and final diagrams are intentionally pending.
