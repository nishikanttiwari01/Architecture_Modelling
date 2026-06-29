# Chapter 6 Quality Gate: BPMN: Business Process Model and Notation

## Gate Summary

- **Chapter:** 6, BPMN: Business Process Model and Notation
- **Review date:** 2026-06-29
- **Reviewer:** Codex
- **Status recommendation:** Revision Required
- **Current gate:** Corrected prose, specifications, BPMN XML sources, BPMNDI layout, SVG exports and PNG previews are present. Repository and diagram validations pass. Camunda Modeler validation is not complete because Camunda Modeler is not available in this environment.
- **Diagram status:** `FIG-06-01` through `FIG-06-03` remain `Review`. No Chapter 6 diagram is marked `Approved`.

## Scorecard

| Category | Score | Notes |
|---|---:|---|
| Scope coverage | 9.1 | Covers BPMN purpose, notation, process diagrams, collaboration diagrams, event waiting, exceptions, comparison, mistakes, exercise and checklist. |
| Beginner clarity | 9.0 | Explains BPMN through questions and simple examples. New explanations cover event-based gateways, intermediate message catch events, boundary timers and boundary errors. |
| Technical accuracy | 9.1 | Corrects the message start event, black-box pools, message-flow boundaries, event-based waiting, guarded decisions and source/export equivalence. |
| Expert depth | 8.9 | Gives practical BPMN precision without reproducing the full OMG specification. |
| Exercise usefulness | 8.8 | Exercise remains appropriate for beginners and reinforces participant, gateway and exclusion choices. |
| Diagram quality | 8.4 | All three figures render from BPMN XML with BPMNDI, SVG and PNG previews. Visual inspection found no critical clipping or cross-boundary sequence-flow issue. The score is capped below 8.5 because Camunda Modeler open/edit verification is incomplete. |
| Source quality | 9.0 | Uses the official OMG BPMN 2.0.2 source note and original teaching examples. |
| Consistency with rest of book | 9.1 | Keeps BPMN distinct from UML activity and C4 dynamic views, and uses existing Simple Online Store and Horizon Bank examples. |

**Average:** 8.9

## Mandatory Gate Checks

| Requirement | Result | Evidence |
|---|---|---|
| Average score at least 9.0 | Fail | Current average is 8.9. |
| No category below 8.5 | Fail | Diagram quality is 8.4 because Camunda Modeler validation is incomplete. |
| All BPMN XML files open correctly in Camunda Modeler | Not verified | Camunda Modeler was not found in the usual Windows install paths and was not available on PATH. |
| XML, SVG and PNG represent the same model | Pass | SVG exports were regenerated from BPMN XML and BPMNDI using `scripts/render-bpmn-diagrams.py`; PNG previews were regenerated from SVG exports. |
| All repository validation passes | Pass | `check-structure`, `check-links`, `check-terminology`, `validate-diagrams`, `check-diagram-register` and `word-count` passed on 2026-06-29. |
| No unresolved critical review issue | Fail | Camunda Modeler open/edit verification remains unresolved. |

## Review Notes

`FIG-06-01` now uses a message start event named Order received. It remains a single Online Store process.

`FIG-06-02` now keeps Retail Customer and Financial Crime Platform as black-box external pools. Horizon Bank requests screening, receives the screening result through an intermediate message catch event, then evaluates Screening clear?. Review screening exception now flows into a guarded exclusive gateway instead of having uncontrolled outgoing flows.

`FIG-06-03` now places Retail Customer in a separate black-box pool. Payments Platform and Operations Analyst are lanes inside Horizon Bank. The correction wait uses an event-based gateway followed by a message catch event and a timer catch event.

## Remaining Issue

Open each Chapter 6 BPMN file in Camunda Modeler and confirm:

- the model opens without repair warnings;
- the displayed layout matches the publication diagram;
- pools, lanes, events, tasks, gateways and flows are selectable and editable;
- no element exists only in the SVG or PNG.

## Recommendation

Do not keep Chapter 6 at `Ready for Author Approval`. The content and exports have been corrected, but the revised gate does not pass until Camunda Modeler validation is completed.
