# C4-PlantUML

This directory stores the local, version-pinned C4-PlantUML library used for publication diagrams in this book.

## Local version

- **C4-PlantUML version:** 2.9.0
- **Source project:** `plantuml-stdlib/C4-PlantUML`
- **Local source:** extracted from the PlantUML standard library bundled with `jebbs.plantuml` 2.18.1
- **PlantUML version used for extraction:** 1.2024.3
- **Extraction date:** 2026-06-28
- **Licence:** MIT, see `LICENSE`
- **Localisation:** Internal `!include <C4/...>` statements were changed to relative local includes so publication diagrams use this repository copy.

## Rules

- Do not use unversioned `!includeurl` statements in publication diagrams.
- Include these local files from diagram source files.
- Record source details in `SOURCE_REGISTER.md` and `research/c4/c4-plantuml-2.9.0.md`.
- Do not download or commit third-party binary files unless the author explicitly authorises them.
