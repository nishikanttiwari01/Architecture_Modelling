# Chapter 6 Quality Gate: BPMN: Business Process Model and Notation

## Gate Summary

- **Chapter:** 6, BPMN: Business Process Model and Notation
- **Review date:** 2026-06-29
- **Reviewer:** Codex, using author-supplied Camunda Desktop Modeler validation results
- **Camunda Modeler version:** 5.48.0, recorded from the Camunda-saved BPMN XML exporter metadata
- **Status recommendation:** Ready for Author Approval
- **Current gate:** Corrected prose, specifications, BPMN XML sources, BPMNDI layout, SVG exports and PNG previews are present. Manual Camunda Modeler validation found that all three BPMN files opened without repair or parsing warnings and rendered as editable native BPMN elements. Repository and diagram validations pass.
- **Diagram status:** `FIG-06-01` through `FIG-06-03` remain `Review`. No Chapter 6 diagram is marked `Approved`.

## Scorecard

| Category | Score | Notes |
|---|---:|---|
| Scope coverage | 9.1 | Covers BPMN purpose, notation, process diagrams, collaboration diagrams, event waiting, exceptions, comparison, mistakes, exercise and checklist. |
| Beginner clarity | 9.1 | Explains BPMN through questions and simple examples. Explanations cover event-based gateways, intermediate message catch events, boundary timers and boundary errors. |
| Technical accuracy | 9.2 | Corrects the message start event, black-box pools, message-flow boundaries, event-based waiting, guarded decisions, BPMNDI layout and source/export equivalence. |
| Expert depth | 9.0 | Gives practical BPMN precision without reproducing the full OMG specification. |
| Exercise usefulness | 8.9 | Exercise remains appropriate for beginners and reinforces participant, gateway and exclusion choices. |
| Diagram quality | 9.0 | All three figures have BPMN XML with BPMNDI, SVG exports and PNG previews. Manual Camunda validation confirmed native editable BPMN elements. Publication exports now show parent participant names and avoid the reported label overlaps. |
| Source quality | 9.0 | Uses the official OMG BPMN 2.0.2 source note and original teaching examples. |
| Consistency with rest of book | 9.1 | Keeps BPMN distinct from UML activity and C4 dynamic views, and uses existing Simple Online Store and Horizon Bank examples. |

**Average:** 9.1

## Manual Camunda Modeler Validation

| Figure | Opened successfully | Warnings | Editable native BPMN elements | Layout compared with committed export | Manual issue recorded | Correction made |
|---|---|---|---|---|---|---|
| FIG-06-01 | Yes | None | Yes | Broadly matched | Parent participant name `Online Store` not visible | Publication renderer now shows parent participant label. |
| FIG-06-02 | Yes | None | Yes | Broadly matched | Parent participant name `Horizon Bank` not visible; screening labels crowded; Application received wrapped awkwardly | Publication renderer now shows parent participant label; Camunda-saved BPMNDI coordinates and label bounds improve the screening exchange and application label. |
| FIG-06-03 | Yes | None | Yes | Broadly matched | Parent participant name `Horizon Bank` not visible; correction labels crowded; spacing above Validate correction needed | Publication renderer now shows parent participant label; BPMNDI label bounds move correction message labels into inter-pool whitespace. |

The author also confirmed that FIG-06-02 and FIG-06-03 message flows crossed participant boundaries correctly and sequence flows stayed within the owning participant. FIG-06-03 rendered its event-based gateway, intermediate message catch event and intermediate timer catch event correctly.

Codex could not independently reopen the corrected files in Camunda Modeler because the application is not available in this execution environment. The final corrections after manual validation were non-semantic BPMNDI label-bound and publication-renderer changes. XML structural checks were rerun after those edits.

## Mandatory Gate Checks

| Requirement | Result | Evidence |
|---|---|---|
| Average score at least 9.0 | Pass | Current average is 9.1. |
| No category below 8.5 | Pass | Lowest category is 8.9. |
| All BPMN XML files open correctly in Camunda Modeler | Pass | Manual validation reported successful opens, no visible repair or parsing warnings, and editable native BPMN elements for all three files. |
| XML, SVG and PNG represent the same model | Pass | SVG exports were regenerated from BPMN XML and BPMNDI using `scripts/render-bpmn-diagrams.py`; PNG previews were regenerated from SVG exports. |
| All repository validation passes | Pass | `check-structure`, `check-links`, `check-terminology`, `validate-diagrams`, `check-diagram-register` and `word-count` passed on 2026-06-29. |
| No unresolved critical review issue | Pass | Manual Camunda validation issues were layout concerns and have been corrected or explicitly resolved in publication output. |

## Review Notes

`FIG-06-01` uses a message start event named Order received and remains a single Online Store process.

`FIG-06-02` keeps Retail Customer and Financial Crime Platform as black-box external pools. Horizon Bank requests screening, receives the screening result through an intermediate message catch event, then evaluates Screening clear?. Review screening exception flows into a guarded exclusive gateway.

`FIG-06-03` places Retail Customer in a separate black-box pool. Payments Platform and Operations Analyst are lanes inside Horizon Bank. The correction wait uses an event-based gateway followed by a message catch event and a timer catch event.

## Recommendation

Chapter 6 meets the revised quality-gate threshold and may return to `Ready for Author Approval`. Chapter 6 diagrams remain `Review` until final publication-layout approval.
