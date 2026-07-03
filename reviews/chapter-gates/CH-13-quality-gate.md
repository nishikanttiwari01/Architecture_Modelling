# Chapter 13 Quality Gate

Current status: `Diagramming`

Reviewed baseline: `21c66d430c42eb1c1a404fcbcf2d1e827d59c455`

Focused correction baseline: `4e5b90d7fbf355ae9ade5772fbc40e9218c3513b`

Diagram-production baseline: `1aaf6504dd64d3efc9cf1843ec6c9ef7a18fc944`

This gate remains open. It is not a passing author-approval gate. The author approved the revised `FIG-13-01` through `FIG-13-06` specifications for diagram production, and the diagrams now exist and are recorded as `Review`. Author approval of the chapter and the figures is still pending, and a Draw.io graphical review plus final book-page layout review are still required.

## Diagram production pass, 2026-07-03

### Specification compliance

| Figure | Source type | Specification points checked | Result |
|---|---|---|---|
| FIG-13-01 | PlantUML | Left-to-right Requirement, Design response, Verification case, Evidence; `addressed by`, `verified by` (requirement to case, direct), `evidenced by`; labelled simplified, non-normative teaching view; no proof implication; no Design response to Verification case link. | Compliant |
| FIG-13-02 | Draw.io | Five stakeholder-value outcome stages; triggering Retail Customer; final outcome; enabling controlled capabilities beneath each stage; legend/note; no BPMN tasks, systems, APIs or departments. | Compliant |
| FIG-13-03 | Draw.io | Controlled systems and precise relationship labels; exactly one lifecycle marker per system; visible lifecycle legend; limitation note; not an integration diagram. | Compliant |
| FIG-13-04 | Draw.io | Four named architecture states; configuration, dependency, risk, assumption, decision point, exit evidence; deliberate coexistence; no dates, budgets, staffing or vendor commitments; target as direction. | Compliant |
| FIG-13-05 | Draw.io | Controlled capabilities; three separate dimensions; visible High, Medium, Low text; scoring definitions, date, owner, version, illustrative statement; grouping and legend; no composite score; greyscale-safe. | Compliant |
| FIG-13-06 | Draw.io | Nine separate components; visibility and evolution axes with the four evolution stages; value-chain dependency lines only; positions marked as assumptions; screening and fraud kept separate; compute, storage and network kept separate. | Compliant |

### Source-file validity

- `FIG-13-01` PlantUML source renders successfully with the pinned PlantUML runtime.
- `FIG-13-02` through `FIG-13-06` Draw.io sources are well-formed mxGraph XML and contain editable vertices and connectors (vertex/edge counts: 33/6, 14/10, 31/3, 52/0, 28/13; the heat map correctly has no connectors).
- Each figure has exactly one editable source. No duplicate source formats exist.
- Draw.io graphical open in the Draw.io application was not performed in this environment. The sources conform to the Draw.io schema and parse cleanly; a Draw.io graphical review is still recommended before `Approved`.

### Export validity

- One SVG and one PNG exist for each of `FIG-13-01` through `FIG-13-06`.
- `FIG-13-01` SVG and PNG were produced by the PlantUML runtime from the `.puml` source.
- `FIG-13-02` through `FIG-13-06` SVG and PNG were produced by `scripts/render-drawio-diagrams.py` from the editable `.drawio` source (see `DEC-021`). No export is a screenshot.
- `python scripts/check-diagram-register.py` and `python scripts/validate-diagrams.py` pass.

### Human visual-review findings

Each rendered PNG was opened and inspected for clipping, overlap, connector crossings, readability, title consistency, legend readability, colour-independent meaning and page-width suitability.

| Figure | Finding |
|---|---|
| FIG-13-01 | Readable; four columns correct; relationship labels correct; caution note present. Landscape width is acceptable for the required left-to-right layout; confirm at final page layout. |
| FIG-13-02 | Readable after decluttering progression labels; stages, capabilities, trigger and outcome clear. |
| FIG-13-03 | Readable after relationship-label repositioning; all ten labels clear of boxes; four lifecycle markers distinct in text and border style. Wide landscape; confirm at final page layout. |
| FIG-13-04 | Readable; four states with all six categories; state headers clear; no invented delivery facts. |
| FIG-13-05 | Readable; greyscale-safe shading with visible High, Medium, Low text; grouping, scoring definitions and metadata present. |
| FIG-13-06 | Readable after axis-label fix and dependency routing; no line passes through a component box; a few value-chain lines cross in open space, which is normal for a Wardley map. |

No figure passed visual review merely because it rendered. Findings above were fixed and re-inspected.

### Open author-approval items

- Author approval of Chapter 13 and of `FIG-13-01` through `FIG-13-06` (Codex must not mark these `Approved`).
- Draw.io graphical open and export-fidelity confirmation for the five Draw.io figures.
- Final book-page layout review, particularly the wider landscape figures `FIG-13-01` and `FIG-13-03`.

## Revised interim assessment

| Category | Score | Evidence | Gate result |
|---|---:|---|---|
| Purpose and reader outcomes | 8.8 | Purpose, outcomes, classification tables and figure integration present. | Conditional pass |
| Technical accuracy | 8.6 | SysML verification semantics, precise landscape labels, roadmap categories, separated heat-map dimensions and Wardley positions realised in the figures. | Conditional pass |
| Beginner clarity | 8.6 | Plain classifications, captions and accessibility text for every figure. | Conditional pass |
| Source support | 8.4 | Source notes for SysML, Open Group business architecture guides, Wardley maps, ADRs and heat-map convention. | Conditional pass |
| Example consistency | 8.5 | Controlled Horizon Bank capability, system, lifecycle and Wardley names used exactly; FIG-13-02 spec aligned with the manuscript capability set. | Conditional pass |
| Diagram readiness | 8.2 | Six figures produced with editable source, SVG and PNG at `Review`; Draw.io graphical review and page layout still pending. | Conditional pass |
| Review evidence | 8.5 | Technical, beginner, consistency and final review records plus this gate updated. | Conditional pass |

Interim average: `8.5/10`.

Gate decision: open. Keep Chapter 13 at `Diagramming` and all six figures at `Review` until the author reviews the rendered figures and either approves them or records revisions. Do not mark Chapter 13 or any figure `Approved`.

## Focused correction pass, 2026-07-03

This pass did not change figure content or redesign figures. It corrected one placement issue and hardened the diagram workflow. The gate remains open.

- **FIG-13-02 trigger label:** the `triggers` label was repositioned to sit clearly above the single Retail Customer to Need understood connector, touching no box, heading or boundary. The connector count is exactly one and its arrowhead is visible. SVG and PNG were regenerated and visually inspected. The `FIG-13-02` specification now lists `examples/horizon-bank/capabilities.md` as a controlled source reference.
- **Renderer syntax check:** CI now runs `python -m compileall -q scripts`, which covers `render-drawio-diagrams.py` and any future script without a hard-coded list.
- **Dependency:** the Pillow dependency is declared and pinned in `requirements-diagrams.txt` and installed in CI before rendering.
- **Workflow invocation:** `scripts/render-all-diagrams.ps1` invokes the Draw.io renderer and fails when it fails; CI runs the complete render script.
- **Stale-export detection:** CI runs `git diff --exit-code -- diagrams/exported/svg diagrams/exported/png` after rendering; CI does not auto-commit regenerated exports.
- **Font portability:** the renderer selects a font deterministically (Arial preferred, DejaVu Sans fallback), reports the selection and fails loudly if none is available. Windows Arial output is unchanged, so exports remain byte-stable.
- **Governance:** `DEC-021` is now `Proposed`, not `Approved`. Native Draw.io graphical-open and export-fidelity comparison remain pending. The previews are reproducible teaching exports, not verified native Draw.io exports.
- **Ownership:** the Owner of `FIG-13-01` through `FIG-13-06` was set to `Claude`.

Open items unchanged by this pass: native Draw.io graphical-open and export-fidelity review; final 6 by 9 book-page layout review; author approval of Chapter 13 and the six figures. Chapter 13 remains `Diagramming`; all six figures remain `Review`; nothing is `Approved`.

## History

The prior interim gate (2026-07-02) recorded an interim average of `8.2/10` with diagram readiness blocked because the figure specifications were unapproved and no diagram source or exports existed. That block is now cleared: the author approved the specifications for production, and the sources and exports exist and are in `Review`.
