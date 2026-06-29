# Chapter 6 Quality Gate: BPMN: Business Process Model and Notation

## Metadata

- **Chapter:** 6, BPMN: Business Process Model and Notation
- **Review date:** 2026-06-29
- **Reviewer:** Codex
- **Status recommendation:** Ready for Author Approval
- **Current gate:** Prose, official source note, diagram specifications, BPMN XML sources, SVG exports, PNG previews and visual review are complete. Chapter 6 diagrams remain `Review`.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.1 | Covers BPMN purpose, core notation, events, activities, gateways, flows, pools, lanes, data objects, subprocesses, exceptions, collaboration, comparison, mistakes, exercise and checklist. |
| Beginner clarity | 9.0 | Explains BPMN through process questions before formal notation and uses simple Online Store and Horizon Bank examples. |
| Technical accuracy | 9.0 | Uses OMG BPMN 2.0.2 as the normative source and distinguishes sequence flow from message flow, pools from lanes and BPMN from software structure diagrams. |
| Expert depth | 8.9 | Gives enough notation detail for practical architecture reading without reproducing the full BPMN specification. |
| Logical flow | 9.0 | Follows the Chapter 5 prototype pattern and moves from plain explanation to notation, examples, comparison and review guidance. |
| Examples and exercises | 9.0 | Uses Online Store fulfilment for first exposure and Horizon Bank onboarding and payment repair for enterprise process examples. |
| Diagram quality | 8.9 | Three figures have specifications, BPMN XML sources, SVG exports and PNG previews. Visual inspection found readable labels, clear sequence/message-flow distinction and no clipping. Final Camunda Modeler layout review remains useful before publication. |
| Source quality | 9.0 | Official OMG BPMN 2.0.2 source note and source-register entry are recorded. The chapter paraphrases and uses original teaching diagrams. |
| Consistency with rest of book | 9.1 | Keeps BPMN separate from C4, UML, ArchiMate and data modelling while linking cleanly to Chapter 4 and Chapter 5. |
| Writing and editorial quality | 9.0 | Uses British English, concise paragraphs, practical cautions and no reader-facing draft scaffolding. |

**Average score:** 9.0

## Review perspectives

### Beginner reader

The chapter explains BPMN as a way to read business process behaviour, not as a general architecture drawing tool. It introduces each core notation element by the question it answers.

### Solution architect

The chapter gives practical guidance for when BPMN fits: ownership, flow, collaboration, decisions, waiting and exceptions. It also explains when C4 or UML is a better fit.

### Enterprise architect

The chapter avoids presenting BPMN as an enterprise architecture framework. It positions BPMN as a process notation that can complement C4, UML, ArchiMate, data and BIAN views.

### Technical editor

The reader-facing draft scaffolding has been removed. Captions and surrounding prose explain what each figure communicates and what it deliberately excludes.

### Diagram reviewer

All three Chapter 6 figures have specifications, editable BPMN XML sources, SVG exports and PNG previews. Visual inspection checked clipping, overlap, sequence-flow direction, message-flow direction, lane readability, gateway conditions, timer notation and page-width suitability. The collaboration figure is wider than the process figures and should be checked again during final publication layout.

### Source and copyright checker

The chapter relies on the official OMG BPMN 2.0.2 specification for terminology and notation. It paraphrases source material and uses original teaching diagrams.

### Consistency reviewer

The chapter uses repository-controlled Simple Online Store and Horizon Bank names. It keeps BPMN process flow separate from software structure diagrams and prepares the reader for Chapter 7 without beginning it.

## Open issues

- No critical review issues remain.
- Final Camunda Modeler layout review is recommended before publication-layout approval.
- Wider figures should receive another scaling check during final page-layout production.

## Gate decision

Chapter 6 meets the quality-gate threshold: average score is 9.0, no category is below 8.5, all three figures are rendered, repository validations pass, and no unresolved critical review issue remains. The chapter may move to `Ready for Author Approval`. Chapter 6 diagrams remain `Review`.
