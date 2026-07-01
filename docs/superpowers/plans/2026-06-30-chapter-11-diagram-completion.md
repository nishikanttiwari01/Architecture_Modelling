# Chapter 11 Diagram Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the remaining Chapter 11 diagram source, export, chapter integration and project-control work.

**Architecture:** Treat the five approved Chapter 11 diagram specifications as the design source. Create original PlantUML teaching figures, render SVG and PNG assets, embed the figures in the manuscript, and move the chapter to `Ready for Author Approval` only if the repository checks pass.

**Tech Stack:** Markdown manuscript and project-control files, PlantUML, repository PowerShell rendering scripts, repository Python validation scripts.

---

## Tasks

### Task 1: Create Chapter 11 PlantUML Sources

**Files:**
- Create: `diagrams/source/plantuml/FIG-11-01-online-store-uml-deployment-view.puml`
- Create: `diagrams/source/plantuml/FIG-11-02-online-store-network-topology-view.puml`
- Create: `diagrams/source/plantuml/FIG-11-03-online-store-kubernetes-deployment-view.puml`
- Create: `diagrams/source/plantuml/FIG-11-04-horizon-bank-hybrid-infrastructure-placement-view.puml`
- Create: `diagrams/source/plantuml/FIG-11-05-horizon-bank-payment-resilience-view.puml`

- [x] **Step 1: Write PlantUML source from each specification**

Use `diagrams/styles/plantuml-theme.puml`, keep labels short, and avoid colour-only meaning.

- [x] **Step 2: Confirm all source files exist**

Run: `Get-ChildItem diagrams/source/plantuml/FIG-11-*.puml`

Expected: five Chapter 11 `.puml` files are listed.

### Task 2: Render and Validate Diagram Assets

**Files:**
- Create: `diagrams/exported/svg/FIG-11-01-online-store-uml-deployment-view.svg`
- Create: `diagrams/exported/svg/FIG-11-02-online-store-network-topology-view.svg`
- Create: `diagrams/exported/svg/FIG-11-03-online-store-kubernetes-deployment-view.svg`
- Create: `diagrams/exported/svg/FIG-11-04-horizon-bank-hybrid-infrastructure-placement-view.svg`
- Create: `diagrams/exported/svg/FIG-11-05-horizon-bank-payment-resilience-view.svg`
- Create: `diagrams/exported/png/FIG-11-01-online-store-uml-deployment-view.png`
- Create: `diagrams/exported/png/FIG-11-02-online-store-network-topology-view.png`
- Create: `diagrams/exported/png/FIG-11-03-online-store-kubernetes-deployment-view.png`
- Create: `diagrams/exported/png/FIG-11-04-horizon-bank-hybrid-infrastructure-placement-view.png`
- Create: `diagrams/exported/png/FIG-11-05-horizon-bank-payment-resilience-view.png`

- [x] **Step 1: Render SVG assets**

Run: `powershell -ExecutionPolicy Bypass -File scripts/render-plantuml.ps1 -InputPath diagrams/source/plantuml/FIG-11-01-online-store-uml-deployment-view.puml -OutputPath diagrams/exported/svg -Required`

Repeat for `FIG-11-02` through `FIG-11-05`.

- [x] **Step 2: Render PNG previews**

Run PlantUML with `-tpng` for each `FIG-11` source and output to `diagrams/exported/png`.

- [x] **Step 3: Check diagram repository rules**

Run: `python scripts/validate-diagrams.py`

Expected: exit code `0`.

### Task 3: Integrate Chapter 11 Figures

**Files:**
- Modify: `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`
- Modify: `DIAGRAM_REGISTER.md`
- Modify: `STATUS.md`
- Modify: `CHANGELOG.md`
- Modify: `RESUME.md`

- [x] **Step 1: Replace deferred-figure wording with rendered-figure references**

Embed each SVG with a caption and accessibility text in the relevant section.

- [x] **Step 2: Update project-control files**

Move Chapter 11 to `Ready for Author Approval`, keep figure statuses at `Review`, and record the change in the changelog and resume note.

- [x] **Step 3: Run required repository checks**

Run:

```powershell
python scripts/check-structure.py
python scripts/check-links.py
python scripts/check-terminology.py
python scripts/validate-diagrams.py
python scripts/check-diagram-register.py
python scripts/word-count.py
```

Expected: every command exits with code `0`.

### Task 4: Commit and Push

**Files:**
- Stage only files changed for Chapter 11 completion.

- [x] **Step 1: Review the diff**

Run: `git diff`

Expected: only Chapter 11 diagram completion, control-file and generated asset changes are present.

- [ ] **Step 2: Commit**

Run: `git add <changed files>` and `git commit -m "complete chapter 11 infrastructure modelling"`

- [ ] **Step 3: Push**

Run: `git push`

Expected: `main` is up to date with `origin/main` after push.
