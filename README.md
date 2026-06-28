# Architecture Modelling: A Practical Beginner’s Handbook

This repository is the source of truth for a complete beginner-to-practitioner handbook covering UML, C4, BPMN, ArchiMate, data, decision, domain, event, security and deployment modelling, followed by a full BIAN implementation case study for a fictional full-service bank.

## Current state

The repository contains the approved book structure, Codex instructions, chapter stubs, templates, research folders, diagram registers, review folders and quality scripts. Chapter files are intentionally structured as drafting briefs rather than finished prose.

## Start here

1. Read `AGENTS.md` before using Codex.
2. Read `BOOK_PLAN.md` for scope and chapter order.
3. Read `STATUS.md` before selecting work.
4. Follow `WORKFLOW.md` for the chapter lifecycle.
5. Use `STYLE_GUIDE.md`, `SOURCE_POLICY.md` and `GLOSSARY.md` while drafting.
6. Record material decisions in `DECISIONS.md`.
7. Update `STATUS.md` and `CHANGELOG.md` after every meaningful task.

## Recommended local setup

```powershell
# Clone the repository
git clone https://github.com/nishikanttiwari01/Architecture_Modelling.git
cd Architecture_Modelling
code .

# Run repository checks
python scripts/word-count.py
python scripts/check-structure.py
python scripts/check-links.py
python scripts/check-terminology.py

# Build a combined Markdown manuscript
.\scripts\build-book.ps1
# Cross-platform alternative: python scripts/build-book.py
```

## Repository principles

- The files in this repository are the permanent project memory.
- Git history is the recovery and audit trail.
- Codex must not rely on chat memory when project files contain the answer.
- No chapter becomes `Approved` without explicit author approval.
- Primary and official sources are preferred for standards and current frameworks.
- BIAN Service Domains are logical business capability boundaries, not automatic microservice boundaries.

## Author

Nishikant Tiwari

## Automated validation

The GitHub Actions workflow in `.github/workflows/validate.yml` runs structural, link and terminology checks, builds the combined Markdown manuscript and reports word counts on each push to `main` and on pull requests.
