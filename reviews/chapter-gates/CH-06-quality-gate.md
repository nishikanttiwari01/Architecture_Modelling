# Chapter 6 Quality Gate: BPMN: Business Process Model and Notation

## Gate Summary

- **Chapter:** 6, BPMN: Business Process Model and Notation
- **Review date:** 2026-06-30
- **Reviewer:** Codex
- **Status recommendation:** Under Review
- **Current gate:** Chapter 6 now includes practical tool guidance distinguishing semantic BPMN modellers from generic drawing tools. The existing BPMN XML sources, BPMNDI layout, SVG exports and PNG previews remain present and unchanged in this revision.
- **Diagram status:** `FIG-06-01` through `FIG-06-03` remain `Review`. No Chapter 6 diagram is marked `Approved`.

## Scorecard

| Category | Score | Notes |
|---|---:|---|
| Scope coverage | 9.2 | Covers BPMN purpose, notation, process diagrams, collaboration diagrams, event waiting, exceptions, tool guidance, comparison, mistakes, exercise and checklist. |
| Beginner clarity | 9.1 | Explains BPMN through questions, examples and a practical distinction between semantic BPMN modellers and drawing tools. |
| Technical accuracy | 9.2 | Keeps BPMN XML as the editable source of truth, distinguishes sequence flow from message flow and recommends semantic BPMN tooling when interoperability or execution semantics matter. |
| Expert depth | 9.1 | Adds practical tool selection guidance without turning the chapter into a vendor catalogue. |
| Exercise usefulness | 8.9 | Exercise remains appropriate for beginners and reinforces participant, gateway and exclusion choices. |
| Diagram quality | 9.0 | Existing figures remain based on BPMN XML with BPMNDI, SVG exports and PNG previews. No diagram semantics changed in this revision. |
| Source quality | 9.0 | Uses the official OMG BPMN source note and the new official tool source note `[BPMN-TOOL-GUIDANCE-2026]`. |
| Consistency with rest of book | 9.1 | Keeps BPMN distinct from UML activity and C4 dynamic views, and aligns with the repository source/export workflow. |

**Average:** 9.1

Minimum category score: 8.9.

## Tool Guidance Review

The new tool section states that Camunda Desktop Modeler is the recommended free tool when BPMN XML interoperability and execution semantics matter. It also states that diagrams.net is suitable for illustrations but does not replace a semantic BPMN modeller. The repository workflow is explicit: `.bpmn` files are editable source, SVG is the primary publication export and PNG is a review preview.

## Mandatory Gate Checks

| Requirement | Result | Evidence |
|---|---|---|
| Tool claims supported by official sources | Pass | `[BPMN-TOOL-GUIDANCE-2026]` added and registered. |
| No vendor collage or copied product graphic | Pass | Chapter uses an original neutral comparison table. |
| BPMN source/export workflow explained | Pass | Chapter states `.bpmn` is editable source and SVG/PNG are publication or review exports. |
| Diagrams remain Review | Pass | Diagram register still keeps Chapter 6 figures at `Review`. |

## Recommendation

Chapter 6 should remain `Under Review` because new prose has been added after prior author approval. The existing diagram set remains technically stable.
