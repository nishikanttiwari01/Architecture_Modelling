# Scripts

All scripts use only standard tools unless noted.

- `word-count.py`: reports word counts for every manuscript file.
- `check-links.py`: validates repository-local Markdown links and image references.
- `check-terminology.py`: checks selected style and terminology rules.
- `build-book.ps1`: combines the manuscript in order and can optionally call Pandoc to create DOCX.

Run from the repository root:

```powershell
python scripts/word-count.py
python scripts/check-links.py
python scripts/check-terminology.py
.\scripts\build-book.ps1
```

## `check-structure.py`

Validates required files and directories, chapter numbering, frontmatter, standard chapter sections, duplicate headings, and consistency among the book plan, status tracker, table of contents and chapter titles.

## `build-book.py`

Builds a combined Markdown manuscript in explicit publication order. This is the cross-platform canonical builder.

## `build-book.ps1`

Windows PowerShell wrapper for `build-book.py`. With `-UsePandoc`, it also creates DOCX when Pandoc is installed.
