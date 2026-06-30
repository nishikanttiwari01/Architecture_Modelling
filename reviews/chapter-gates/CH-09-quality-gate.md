# Chapter 9 Quality Gate: Decision Modelling and DMN

## Gate summary

- **Chapter:** 9, Decision Modelling and DMN
- **Manuscript:** `manuscript/part-02-modelling-languages/09-decision-modelling.md`
- **Status:** Approved
- **Current gate:** Chapter 9 has complete prose, source notes, diagram specifications, PlantUML sources, SVG exports, PNG previews, glossary updates, register updates and repository checks.
- **Final quality score:** 9.1
- **Diagram status:** `FIG-09-01` through `FIG-09-04` remain `Review`, not `Approved`.

## Scorecard

| Category | Score | Evidence |
|---|---:|---|
| Scope coverage | 9.2 | Covers decision separation, policy/rule/decision vocabulary, DMN requirements and logic levels, FEEL, decision tables, hit policies, DRDs, BPMN integration, governance and tools. |
| Technical accuracy | 9.2 | Preserves OMG DMN 1.5 as normative baseline, records Camunda DMN 1.3 tooling caution, corrects FEEL list literals and avoids claiming DMN 1.5 conformance from Camunda. |
| Beginner comprehension | 9.1 | Uses simple Online Store and Horizon Bank examples, defines terms before formal use and explains modelling choices in plain language. |
| Educational flow | 9.0 | Follows the teaching sequence from plain explanation to formal terms, examples, comparison, mistakes, checklist and references. |
| Diagram quality | 9.1 | Four figures render to SVG and PNG, are readable, use restrained colour, correct the final decision-logic and DRD relationship issues and keep all Chapter 9 diagrams at `Review`. |
| Source and copyright discipline | 9.2 | Uses official OMG, Camunda and Trisotech sources, paraphrases source material and uses original teaching diagrams. |
| Repository tracking | 9.2 | `STATUS.md`, `RESUME.md`, `CHANGELOG.md`, `SOURCE_REGISTER.md`, `DIAGRAM_REGISTER.md`, `GLOSSARY.md` and `DECISIONS.md` have been updated. |

Average score: 9.1

No category is below 8.5.

## Required gate checks

| Check | Result | Evidence |
|---|---|---|
| Required sections complete | Pass | Chapter includes purpose, outcomes, prerequisites, artefacts, examples, source requirements, main sections, checklist and references. |
| OMG DMN 1.5 retained as baseline | Pass | `[OMG-DMN-1.5]` remains the normative source; beta material is not used as compliance baseline. |
| Current tool-source versions recorded | Pass | Camunda documentation is recorded as current DMN 1.3 modelling guidance; Trisotech source note records current public product documentation. |
| Corrected delivery decision table | Pass | `FIG-09-01` and chapter prose use Unique hit policy and non-overlapping rules. |
| Dash notation explained | Pass | Chapter prose and figure note explain that `-` means any value. |
| Decision-table gaps and overlaps checked | Pass | The four-rule delivery table covers the simplified stock, destination and order-value domain without overlapping Unique-rule matches. |
| FEEL introduction present | Pass | Chapter includes comparisons, ranges, lists, strings, dates and missing/null-value caution. |
| Final FEEL list-literal correction | Pass | FEEL list examples use square brackets, and prose distinguishes list literals from comma-separated unary-test alternatives in decision-table input entries. |
| DMN table structure explained | Pass | Chapter covers hit-policy indicator, input clauses, input expressions, unary tests, output clauses, output values, rules and annotations. |
| Formal hit-policy summary present | Pass | Chapter covers U, A, P, F, R, O, C, C+, C<, C> and C#. |
| Decision tree distinction present | Pass | Chapter explicitly states that a decision tree is not a formal DMN DRD element. |
| `FIG-09-02` stock branch corrected | Pass | Restricted products now check destination eligibility and stock before returning restricted delivery; unrestricted products also check stock. |
| DRD guidance strengthened | Pass | Chapter covers DRG, DRD, information, knowledge and authority requirements, direction, Decision, Input Data, Business Knowledge Model, Knowledge Source and Decision Service. |
| `FIG-09-03` direct information arrows restored | Pass | Four input data elements point directly to `Determine Payment Route`; no invented information-requirements connector remains. |
| BPMN and DMN integration corrected | Pass | Chapter states that BPMN Business Rule Task to DMN invocation is platform-specific, not standardised directly by OMG. |
| `FIG-09-04` cross-boundary labels added | Pass | The BPMN-to-DMN invocation arrow and DMN-to-BPMN result arrow are labelled. |
| Diagrams registered | Pass | `DIAGRAM_REGISTER.md` includes `FIG-09-01` through `FIG-09-04` at `Review`. |
| Diagrams rendered | Pass | SVG and PNG outputs exist for all four Chapter 9 PlantUML figures. |
| Diagram visual review | Pass | PNG previews inspected for clipping, overlap, font size, arrow direction, contrast and page-width readability. `FIG-09-03` is wider than the simplest figures and should receive final layout review. |
| Semantic DMN validation record | Pass | No `.dmn` files were created. PlantUML teaching sources were selected per `DEC-015`; therefore DMN modeller validation is not applicable for this chapter asset set. |

## DMN modeller validation record

| Field | Record |
|---|---|
| Tool | Not used for Chapter 9 source files |
| Tool version | Not applicable |
| DMN file version | Not applicable, no `.dmn` files created |
| Warnings | Not applicable |
| Elements remain editable | PlantUML elements remain editable as text source; semantic DMN XML editability not applicable |
| FEEL expressions parse successfully | Not engine-validated; FEEL examples were checked manually against `[OMG-DMN-1.5]` beginner usage |

## Figure review notes

`FIG-09-01` uses Unique hit policy and non-overlapping delivery rules. The dash means any value.

`FIG-09-02` is a general decision tree and is explicitly not presented as a formal DMN DRD element. It checks stock for both restricted and unrestricted product paths.

`FIG-09-03` shows a DMN-style decision requirements teaching view. Its input data elements point directly to `Determine Payment Route` as information requirements. It is not semantic `.dmn` XML.

`FIG-09-04` separates BPMN process responsibility from DMN decision responsibility, labels the platform-specific invocation and payment route result, and states that technical binding is vendor-specific.

## Remaining risks

- Final book-page layout review remains pending for all Chapter 9 diagrams, particularly `FIG-09-03`.
- If executable or repository-grade DMN assets are needed later, create semantic `.dmn` files in a DMN-aware modeller and record tool version, DMN file version, warnings and FEEL parse results.

## Gate decision

Chapter 9 is `Approved` by the author. The final quality score is 9.1, no category is below 8.5, all required figures render, source versions are recorded, decision-table gaps and overlaps are checked, and repository checks pass. Chapter 9 diagrams remain at `Review`.
