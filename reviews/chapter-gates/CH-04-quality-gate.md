# Chapter 4 Quality Gate: UML: Unified Modeling Language

## Metadata

- **Chapter:** 4, UML: Unified Modeling Language
- **Review date:** 2026-06-29
- **Reviewer:** Codex
- **Status recommendation:** Ready for Author Approval
- **Current gate:** Prose, source note, diagram specifications, PlantUML sources, SVG exports, PNG previews and visual review are complete. Chapter 4 diagrams remain `Review`.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.1 | Covers UML purpose, structure and behaviour families, seven core diagram types, notation-reading guidance, examples, selection guidance, comparison, mistakes, exercise and checklist. |
| Beginner clarity | 9.0 | Explains each diagram by question first, then notation, then example. Figure explanations state what to notice and what is excluded. |
| Technical accuracy | 9.1 | Uses OMG UML 2.5.1 as the normative source, corrects UML component semantics and separates components, interfaces, artefacts and deployment nodes. |
| Expert depth | 8.9 | Gives enough notation detail for practical architecture reading without reproducing the full UML specification. |
| Logical flow | 9.0 | Follows the Chapter 5 prototype pattern and adds a consistent notation-reading subsection for each core diagram. |
| Examples and exercises | 9.0 | Uses Simple Online Store for first exposure and Horizon Bank for realistic sequence, activity, state and deployment examples. |
| Diagram quality | 8.9 | Seven figures have specifications, PlantUML sources, SVG exports and PNG previews. Visual inspection found no clipping, no unreadable font sizes and correct arrow semantics. The sequence, component and deployment diagrams are relatively wide, so final page-layout scaling should be checked. |
| Source quality | 9.0 | Official OMG UML 2.5.1 source note and source-register entry are recorded. The chapter paraphrases and does not copy official diagrams or tables. |
| Consistency with rest of book | 9.0 | Uses controlled example names, keeps UML separate from C4, BPMN, ArchiMate, data modelling and BIAN, and leaves all diagrams at `Review`. |
| Writing and editorial quality | 9.0 | British English, concise paragraphs and no reader-facing draft scaffolding. |

**Average score:** 9.0

## Review perspectives

### Beginner reader

The chapter gives a practical entry point into UML without requiring the reader to learn the whole specification. Each core diagram now has a short notation-reading subsection and a figure that demonstrates the purpose of the notation.

### Solution architect

The chapter provides usable guidance for choosing among use case, class, component, sequence, activity, state machine and deployment diagrams. It now distinguishes logical component structure from artefact packaging and runtime deployment.

### Enterprise architect

The chapter avoids presenting UML as a complete enterprise architecture framework. It points readers to C4, BPMN, ArchiMate, data modelling and BIAN where those approaches answer a better question.

### Technical editor

The reader-facing `Planned chapter structure` and `Drafting notes` sections have been removed. Captions and surrounding prose explain what each figure communicates and what it deliberately excludes.

### Diagram reviewer

All seven Chapter 4 figures have specifications, editable PlantUML sources, SVG exports and PNG review previews. Visual inspection checked clipping, overlap, arrowheads, UML relationship semantics, multiplicities, guards, font size and page-width suitability. `FIG-04-04`, `FIG-04-03` and `FIG-04-07` are wider than the simpler figures and should be checked again during final page-layout production.

### Source and copyright checker

The chapter relies on the official OMG UML 2.5.1 specification for terminology and taxonomy. It paraphrases source material and uses original teaching diagrams.

### Consistency reviewer

The chapter uses repository-controlled Simple Online Store and Horizon Bank names. It keeps UML component guidance distinct from C4 component guidance in Chapter 5 and does not begin Chapter 6.

## Open issues

- No critical review issues remain.
- Wider figures should receive another scaling check during final page-layout production.
- Chapter 5's C4 versus UML comparison may be reviewed during later whole-book consistency work, but it is not blocking Chapter 4.

## Gate decision

Chapter 4 meets the quality-gate threshold: average score is at least 9.0, no category is below 8.5, all seven figures are rendered, repository validations pass, and no unresolved critical review issue remains. The chapter may move to `Ready for Author Approval`. Chapter 4 diagrams remain `Review`.
