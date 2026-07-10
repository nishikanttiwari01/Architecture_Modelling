# Remaining Manuscript Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete and validate Chapters 19 to 63 and Appendices A to H, then integrate, commit and push the verified manuscript to GitHub.

**Architecture:** Treat every chapter as an editorial unit with its own context reading, primary-source research, prose draft, four review passes, validation loop and focused commit. Close each book part with a cross-chapter consistency pass, then perform a full-manuscript validation and build before pushing. Diagram specifications may be prepared, but diagram source remains deferred unless the author has approved the specification.

**Tech Stack:** Markdown, repository Python validation scripts, PlantUML/Mermaid/Camunda/Draw.io according to repository policy, Git and GitHub.

---

## File map

- `manuscript/part-03-diagram-selection/19-*.md` to `23-*.md`: remaining diagram-selection chapters.
- `manuscript/part-04-architecture-lifecycle/24-*.md` to `30-*.md`: architecture-lifecycle chapters.
- `manuscript/part-05-bian-case-study/31-*.md` to `56-*.md`: BIAN foundations, scenarios, implementation and reference chapters.
- `manuscript/part-06-practical-reference/57-*.md` to `63-*.md`: practical reference chapters.
- `manuscript/appendices/appendix-a-*.md` to `appendix-h-*.md`: publication appendices.
- `research/<topic>/*.md` and `SOURCE_REGISTER.md`: primary-source evidence and registration.
- `diagrams/specifications/*.md` and `DIAGRAM_REGISTER.md`: figure specifications and lifecycle state.
- `reviews/{technical-review,beginner-review,consistency-review,final-review}/`: chapter review evidence.
- `reviews/chapter-gates/CH-<NN>-quality-gate.md`: quality-gate result for each numbered chapter.
- `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, `GLOSSARY.md`: progress, history, significant decisions and controlled terminology.
- `manuscript/00-front-matter/table-of-contents.md`: final contents alignment.

## Reusable chapter procedure

Apply these exact steps to every numbered chapter task below.

- [ ] Read `BOOK_PLAN.md`, `STATUS.md`, `WORKFLOW.md`, `STYLE_GUIDE.md`, `SOURCE_POLICY.md`, `DECISIONS.md`, `GLOSSARY.md`, the target chapter, its immediate neighbours, relevant `research/` notes, examples and `DIAGRAM_REGISTER.md` entries.
- [ ] Confirm the chapter purpose and every reader outcome against `BOOK_PLAN.md` and the target file.
- [ ] Verify missing or unstable facts using official primary sources; add one note per meaningful source from `templates/source-note-template.md` and register major sources in `SOURCE_REGISTER.md`.
- [ ] Replace the outline and drafting notes with complete beginner-first prose, worked examples, comparisons, common mistakes, key takeaways, exercise, review checklist and references appropriate to the chapter.
- [ ] Define each acronym at first use and use British English, glossary terms, short paragraphs and no em dashes.
- [ ] Add or update each required figure in `DIAGRAM_REGISTER.md` and create its specification from `templates/diagram-specification-template.md`; do not create source for an unapproved specification.
- [ ] Create technical, beginner, consistency and final review files using the established Chapter 18 review structure; record concrete findings and repair every actionable finding.
- [ ] Create or update `reviews/chapter-gates/CH-<NN>-quality-gate.md` and record author-only diagram or decision dependencies honestly.
- [ ] Run `python scripts/check-structure.py`, `python scripts/check-links.py`, `python scripts/check-terminology.py`, `python scripts/validate-diagrams.py`, and `python scripts/check-diagram-register.py`; repair chapter-caused failures and rerun until clean.
- [ ] Run `python scripts/word-count.py` and compare the chapter with its target range in `BOOK_PLAN.md`; revise material that is materially thin, repetitive or overlong.
- [ ] Update `STATUS.md`, append a concise `CHANGELOG.md` entry, update `GLOSSARY.md` for new controlled terms and add only significant choices to `DECISIONS.md`.
- [ ] Run `git diff --check`, inspect `git diff`, stage only the coherent chapter batch and commit with `Complete Chapter <NN> <short title>`.

### Task 1: Complete Part III

**Files:** Chapters 19 to 23 and their associated research, sources, diagrams, reviews and repository registers.

- [ ] Complete Chapter 19, *Modelling Data Architecture*, using the reusable chapter procedure.
- [ ] Complete Chapter 20, *Modelling Infrastructure and Deployment*, using the reusable chapter procedure.
- [ ] Complete Chapter 21, *Modelling Security Architecture*, using the reusable chapter procedure.
- [ ] Complete Chapter 22, *Modelling Transformation and Migration*, using the reusable chapter procedure.
- [ ] Complete Chapter 23, *Modelling Decisions and Business Rules*, using the reusable chapter procedure.
- [ ] Re-read Chapters 14 to 23 as Part III; repair duplicated selection advice, conflicting terminology and broken transitions.
- [ ] Rerun all six repository checks and commit the Part III consistency corrections as `Review Part III consistency`.

### Task 2: Complete Part IV

**Files:** Chapters 24 to 30 and their associated research, sources, diagrams, reviews and repository registers.

- [ ] Complete Chapters 24, 25, 26, 27, 28, 29 and 30 in order, applying the reusable chapter procedure separately to each chapter.
- [ ] Re-read Chapters 24 to 30 as one lifecycle; verify that artefacts flow coherently from discovery through change and migration without implying a mandatory linear method.
- [ ] Rerun all six repository checks and commit the Part IV consistency corrections as `Review Part IV consistency`.

### Task 3: Complete BIAN foundations

**Files:** Chapters 31 to 36, `research/bian/`, BIAN source records, glossary, diagram specifications and reviews.

- [ ] Verify current BIAN primary materials and record their versions, access dates and licences where relevant.
- [ ] Complete Chapters 31, 32, 33, 34, 35 and 36 in order, applying the reusable chapter procedure separately to each chapter.
- [ ] Audit every use of `Service Domain`, `Business Scenario`, `Service Operation`, `Business Object Model`, semantic API and event terminology against recorded BIAN sources.
- [ ] Rerun all six repository checks and commit the BIAN-foundation consistency corrections as `Review BIAN foundations`.

### Task 4: Complete BIAN scenarios

**Files:** Chapters 37 to 42, `examples/horizon-bank/`, scenario research, source records, specifications and reviews.

- [ ] Complete Chapters 37, 38, 39, 40, 41 and 42 in order using `templates/bian-scenario-template.md` and the reusable chapter procedure.
- [ ] Ensure every scenario separates business purpose, participating roles, process, Service Domain collaboration, information, application mapping, security, deployment and open design decisions.
- [ ] Cross-check shared Horizon Bank actors, capabilities and landscape names against `examples/horizon-bank/` and repair drift.
- [ ] Rerun all six repository checks and commit the scenario consistency corrections as `Review BIAN scenarios`.

### Task 5: Complete BIAN implementation guidance

**Files:** Chapters 43 to 56 and their associated research, sources, examples, diagrams, reviews and registers.

- [ ] Complete Chapters 43 through 56 in numerical order, applying the reusable chapter procedure separately to each chapter.
- [ ] Audit for the prohibited one-Service-Domain-equals-one-microservice simplification and correct every unjustified physical mapping.
- [ ] Verify that APIs, events, data, controls, deployment, migration, governance and measures are described as design choices with owners and evidence, not automatic consequences of BIAN alignment.
- [ ] Re-read Chapters 31 to 56 as Part V; repair contradictions, version drift, example drift and unnecessary repetition.
- [ ] Rerun all six repository checks and commit the Part V consistency corrections as `Review Part V consistency`.

### Task 6: Complete Part VI

**Files:** Chapters 57 to 63 and their associated research, sources, diagrams, reviews and registers.

- [ ] Complete Chapters 57 through 63 in numerical order, applying the reusable chapter procedure separately to each chapter.
- [ ] Cross-check all quick-selection advice against Chapters 4 to 23 so the reference section does not contradict the detailed teaching chapters.
- [ ] Re-read Chapters 57 to 63 as a practical reference; remove duplication and make checklists directly usable.
- [ ] Rerun all six repository checks and commit the Part VI consistency corrections as `Review Part VI consistency`.

### Task 7: Complete Appendices A to H

**Files:** `manuscript/appendices/appendix-a-diagram-selector.md` through `appendix-h-glossary-sources.md`, plus necessary glossary, source and contents updates.

- [ ] Complete Appendix A and validate every selector recommendation against Parts II and III.
- [ ] Complete Appendices B to F and validate notation names and element summaries against the book's official source notes.
- [ ] Complete Appendix G and validate every BIAN term against the primary BIAN sources recorded during Tasks 3 to 5.
- [ ] Complete Appendix H from `GLOSSARY.md` and `SOURCE_REGISTER.md`, preserving controlled definitions and source traceability.
- [ ] Run all six repository checks, inspect appendix links and commit as `Complete manuscript appendices`.

### Task 8: Full-manuscript integration review

**Files:** Entire manuscript, reviews, registers, front matter and build artefacts permitted by repository policy.

- [ ] Update `manuscript/00-front-matter/table-of-contents.md` to match the final chapter and appendix headings and order.
- [ ] Scan the manuscript for unfinished-marker tokens, drafting notes, placeholder text, unexplained acronyms, em dashes and inconsistent chapter references; repair all unintended results.
- [ ] Audit all chapter statuses against `WORKFLOW.md`; do not mark any chapter or diagram `Approved`.
- [ ] Run the full required validation set:

```powershell
python scripts/check-structure.py
python scripts/check-links.py
python scripts/check-terminology.py
python scripts/validate-diagrams.py
python scripts/check-diagram-register.py
python scripts/word-count.py
```

- [ ] Repair every actionable failure and rerun the complete set from the first command until all commands exit successfully.
- [ ] Run `python scripts/build-book.py`; inspect the result, repair integration failures and rerun until successful.
- [ ] Run `git diff --check`, inspect the complete diff and commit final integration corrections as `Complete remaining manuscript integration`.

### Task 9: Deliver to GitHub

**Files:** Git history and remote branch only.

- [ ] Run `git status --short --branch` and confirm no intended change is unstaged or uncommitted.
- [ ] Run the six required checks and book build again, fresh, immediately before delivery.
- [ ] Run `git fetch origin` and compare `main` with `origin/main`.
- [ ] If the remote advanced, run `git pull --ff-only`, resolve only through a non-destructive workflow, and rerun the complete validation set.
- [ ] Run `git push origin main` without force.
- [ ] Confirm the pushed commit with `git status --short --branch` and `git log -1 --oneline`.
- [ ] Report files changed, completed work, checks and results, sources, decisions, remaining author-only approvals, commits and push result.
