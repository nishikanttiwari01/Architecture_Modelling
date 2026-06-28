# Scripts

All scripts use only standard tools unless noted.

- `word-count.py`: reports word counts for every manuscript file.
- `check-links.py`: validates repository-local Markdown links and image references.
- `check-terminology.py`: checks selected style and terminology rules.
- `check-diagram-register.py`: validates figure IDs, register statuses and required source/export files for reviewed or exported diagrams.
- `validate-diagrams.py`: validates diagram folders, templates, style files and source conventions.
- `render-plantuml.ps1`: renders PlantUML `.puml` files to SVG when PlantUML tooling is available.
- `render-mermaid.ps1`: renders Mermaid `.mmd` files to SVG when Mermaid CLI tooling is available.
- `render-all-diagrams.ps1`: runs the available diagram renderers.
- `build-book.ps1`: combines the manuscript in order and can optionally call Pandoc to create DOCX.

Run from the repository root:

```powershell
python scripts/word-count.py
python scripts/check-links.py
python scripts/check-terminology.py
python scripts/validate-diagrams.py
python scripts/check-diagram-register.py
.\scripts\build-book.ps1
```

Diagram rendering is optional in environments where PlantUML or Mermaid CLI is unavailable:

```powershell
.\scripts\render-all-diagrams.ps1
```

If local PowerShell policy blocks unsigned scripts, use:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\render-all-diagrams.ps1
```

Use `-Required` when a task must prove rendering success:

```powershell
.\scripts\render-all-diagrams.ps1 -Required
```

## `check-structure.py`

Validates required files and directories, chapter numbering, frontmatter, standard chapter sections, duplicate headings, and consistency among the book plan, status tracker, table of contents and chapter titles.

## `build-book.py`

Builds a combined Markdown manuscript in explicit publication order. This is the cross-platform canonical builder.

## `build-book.ps1`

Windows PowerShell wrapper for `build-book.py`. With `-UsePandoc`, it also creates DOCX when Pandoc is installed.

## Diagram scripts

The rendering scripts do not download third-party tools. They use installed tools when available and skip rendering otherwise, unless `-Required` is passed.
