# Chapter 5 C4 Prototype Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete Chapter 5, **The C4 Model**, as the prototype chapter for manuscript quality, source discipline, diagram workflow and repository updates.

**Architecture:** Treat the chapter as one production unit with supporting research notes, diagram specifications, PlantUML sources, SVG exports and a quality-gate review. Keep all C4 facts traceable to official sources, and keep all diagram dependencies local and version-pinned.

**Tech Stack:** Markdown manuscript, PlantUML 1.2024.3 from `jebbs.plantuml`, extracted C4-PlantUML 2.9.0 standard library, repository Python validation scripts.

---

## File Structure

- Modify: `.gitignore`, keep `.superpowers/` ignored for visual-companion session files.
- Modify: `manuscript/part-02-modelling-languages/05-c4-model.md`, replace stub prose with the complete Chapter 5 draft.
- Create: `research/c4/c4-model-official.md`, source note for the official C4 model documentation.
- Create: `research/c4/structurizr-c4-documentation.md`, source note for Structurizr documentation where used.
- Create: `research/c4/c4-plantuml-2.9.0.md`, source note for the local C4-PlantUML library.
- Modify: `SOURCE_REGISTER.md`, update C4 source rows.
- Modify: `DIAGRAM_REGISTER.md`, add Chapter 5 figure rows.
- Create: `diagrams/specifications/FIG-05-01-c4-levels-of-zoom.md`.
- Create: `diagrams/specifications/FIG-05-02-online-store-system-context.md`.
- Create: `diagrams/specifications/FIG-05-03-online-store-container-view.md`.
- Create: `diagrams/specifications/FIG-05-04-horizon-bank-payments-platform-view.md`.
- Create: `diagrams/specifications/FIG-05-05-payment-submission-dynamic-view.md`.
- Modify: `diagrams/lib/C4-PlantUML/README.md`, record local dependency status.
- Create: `diagrams/lib/C4-PlantUML/*.puml` and `diagrams/lib/C4-PlantUML/themes/*.puml`, copied from the inspected PlantUML stdlib extraction of C4-PlantUML 2.9.0.
- Create: `diagrams/source/plantuml/FIG-05-01-c4-levels-of-zoom.puml`.
- Create: `diagrams/source/plantuml/FIG-05-02-online-store-system-context.puml`.
- Create: `diagrams/source/plantuml/FIG-05-03-online-store-container-view.puml`.
- Create: `diagrams/source/plantuml/FIG-05-04-horizon-bank-payments-platform-view.puml`.
- Create: `diagrams/source/plantuml/FIG-05-05-payment-submission-dynamic-view.puml`.
- Create: `diagrams/exported/svg/FIG-05-01-c4-levels-of-zoom.svg`.
- Create: `diagrams/exported/svg/FIG-05-02-online-store-system-context.svg`.
- Create: `diagrams/exported/svg/FIG-05-03-online-store-container-view.svg`.
- Create: `diagrams/exported/svg/FIG-05-04-horizon-bank-payments-platform-view.svg`.
- Create: `diagrams/exported/svg/FIG-05-05-payment-submission-dynamic-view.svg`.
- Create: `reviews/chapter-gates/CH-05-quality-gate.md`.
- Create or modify: `RESUME.md`.
- Modify: `STATUS.md`.
- Modify: `CHANGELOG.md`.

### Task 1: Verify Baseline and Local Diagram Tooling

- [ ] **Step 1: Confirm the working tree before edits**

Run: `git status --short`

Expected: existing changes are only `.gitignore`, `docs/superpowers/specs/2026-06-28-chapter-5-c4-prototype-design.md` and this plan.

- [ ] **Step 2: Confirm PlantUML runtime**

Run: `java -jar C:\Users\nishi\.vscode\extensions\jebbs.plantuml-2.18.1\plantuml.jar -version`

Expected: PlantUML runs and reports version `1.2024.3`.

- [ ] **Step 3: Confirm C4 stdlib version**

Run: `rg -n "C4Version|2.9.0" .superpowers\stdlib-extract\stdlib\c4\C4.puml`

Expected: the extracted C4 stdlib reports C4-PlantUML version `2.9.0`.

### Task 2: Pin Local C4-PlantUML Library

- [ ] **Step 1: Copy extracted C4 files into the repository library folder**

Copy the inspected files from `.superpowers/stdlib-extract/stdlib/c4/` into `diagrams/lib/C4-PlantUML/`, preserving the `themes/` folder.

- [ ] **Step 2: Update `diagrams/lib/C4-PlantUML/README.md`**

State that the library is locally pinned from PlantUML stdlib, C4-PlantUML version `2.9.0`, extracted from PlantUML `1.2024.3`, and used only for reproducible book diagrams.

- [ ] **Step 3: Verify local include path with a smoke test**

Create a temporary ignored PlantUML file under `.superpowers/` that includes:

```plantuml
@startuml
!include ../diagrams/lib/C4-PlantUML/C4_Context.puml
Person(reader, "Reader")
System(book, "Architecture Modelling Handbook")
Rel(reader, book, "Reads")
@enduml
```

Run PlantUML against it and expect an SVG to render without include errors.

### Task 3: Create C4 Source Notes

- [ ] **Step 1: Create `research/c4/c4-model-official.md`**

Use `templates/source-note-template.md` and record the official C4 model documentation, access date `2026-06-28`, and claims supported: C4 levels, people, software systems, containers, components, code, dynamic diagrams and deployment diagrams.

- [ ] **Step 2: Create `research/c4/structurizr-c4-documentation.md`**

Use `templates/source-note-template.md` and record Structurizr documentation where the chapter uses practical C4 tooling or diagrams-as-code guidance.

- [ ] **Step 3: Create `research/c4/c4-plantuml-2.9.0.md`**

Use `templates/source-note-template.md` and record C4-PlantUML version `2.9.0`, source project `plantuml-stdlib/C4-PlantUML`, MIT licence, and local extraction path.

- [ ] **Step 4: Update `SOURCE_REGISTER.md`**

Mark `C4-OFFICIAL` and `C4-PLANTUML` as recorded, with note-file paths and access date `2026-06-28`.

### Task 4: Specify and Register Chapter 5 Diagrams

- [ ] **Step 1: Update `DIAGRAM_REGISTER.md`**

Ensure rows exist for `FIG-05-01` through `FIG-05-05`, with source files under `diagrams/source/plantuml/`, export files under `diagrams/exported/svg/`, status `Drafting` before rendering and not `Approved`.

- [ ] **Step 2: Create five diagram specifications**

Create one specification file per figure under `diagrams/specifications/`, using `templates/diagram-specification-template.md` headings and adding a note that the author authorised the Chapter 5 prototype production with the instruction `go` on `2026-06-28`; this does not mark diagrams `Approved`.

### Task 5: Draft Chapter 5

- [ ] **Step 1: Replace stub prose in `05-c4-model.md`**

Draft approximately 3,500 to 4,500 words. Preserve front matter, chapter number and approved section intent.

- [ ] **Step 2: Include source keys**

Use source keys such as `[C4-OFFICIAL]`, `[STRUCTURIZR-C4]` and `[C4-PLANTUML-2.9.0]` where factual claims depend on sources.

- [ ] **Step 3: Include figure references and captions**

Add figure references for `FIG-05-01` through `FIG-05-05`, using the caption pattern from `STYLE_GUIDE.md`.

- [ ] **Step 4: Ensure teaching sequence**

Check that simple explanation comes before formal terminology, the Simple Online Store comes before Horizon Bank, and C4 versus UML is balanced.

### Task 6: Create and Render Diagram Sources

- [ ] **Step 1: Create five `.puml` files**

Use local includes such as:

```plantuml
!include ../../lib/C4-PlantUML/C4_Context.puml
```

or the matching local C4 file for each view.

- [ ] **Step 2: Render SVGs**

Run:

```powershell
java -jar C:\Users\nishi\.vscode\extensions\jebbs.plantuml-2.18.1\plantuml.jar -tsvg diagrams\source\plantuml\FIG-05-01-c4-levels-of-zoom.puml
```

Repeat for all five files or use a batch render command if available.

- [ ] **Step 3: Move rendered SVGs if needed**

PlantUML may render beside the source file. Move outputs to `diagrams/exported/svg/` with the exact registered names.

- [ ] **Step 4: Inspect SVGs**

Open or read the SVGs and verify no clipped text, overlapping labels, unreadable font sizes, excessive line crossings, incorrect arrow direction, weak contrast or terminology mismatch.

### Task 7: Quality Gate and Project Records

- [ ] **Step 1: Create `reviews/chapter-gates/CH-05-quality-gate.md`**

Score scope coverage, beginner clarity, technical accuracy, expert depth, logical flow, examples and exercises, diagram quality, source quality, consistency and editorial quality.

- [ ] **Step 2: Update `STATUS.md`**

Move Chapter 5 only to the status justified by the work completed. Use `Ready for Author Approval` only if all quality gates pass. Do not use `Approved`.

- [ ] **Step 3: Update `CHANGELOG.md`**

Add a concise entry for Chapter 5 prototype production.

- [ ] **Step 4: Update `RESUME.md`**

Record last completed work, current commit if available, next action and remaining risks.

### Task 8: Run Verification and Review Diff

- [ ] **Step 1: Run required checks**

Run:

```powershell
python scripts/check-structure.py
python scripts/check-links.py
python scripts/check-terminology.py
python scripts/validate-diagrams.py
python scripts/check-diagram-register.py
python scripts/word-count.py
python scripts/build-book.py
```

Expected: all checks pass.

- [ ] **Step 2: Review changes**

Run: `git diff`

Expected: changes are scoped to Chapter 5 prototype production and supporting records.

- [ ] **Step 3: Commit if checks pass**

Run:

```powershell
git add .gitignore docs/superpowers/specs docs/superpowers/plans manuscript/part-02-modelling-languages/05-c4-model.md research/c4 SOURCE_REGISTER.md DIAGRAM_REGISTER.md diagrams reviews/chapter-gates STATUS.md CHANGELOG.md RESUME.md
git commit -m "docs(ch05): complete C4 prototype chapter"
```

Expected: commit succeeds. Do not push unless explicitly authorised.
