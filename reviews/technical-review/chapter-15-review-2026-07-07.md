# Chapter 15 Technical Review, 2026-07-07

## Evidence Commits

Baseline reviewed for content:

- Commit: `54a84e0 Refine Chapter 15 business process modelling draft`
- Purpose: reviewed Chapter 15 after the focused refinement pass.

Completion evidence for Chapter 15 review and diagram workflow:

- Commit: `4b9f068 Complete Chapter 15 review and diagram assets`
- Purpose: added FIG-15-01, formal review records, the quality gate and status updates.

## Scope

- Manuscript: `manuscript/part-03-diagram-selection/15-business-processes.md`
- Source context: registered source notes for BPMN, UML, DMN and value streams
- Diagram context: reused figure entries in `DIAGRAM_REGISTER.md`
- Decision context: `DEC-023`

## Review Pass

Technical accuracy was reviewed against the chapter purpose, `DEC-023`, the
registered source notes, and the existing figure register.

| Check | Result | Evidence |
|---|---|---|
| Scope boundary | Pass | Chapter 15 stays focused on choosing and combining process-related models. It references Chapter 6 BPMN rather than re-teaching the notation. |
| BPMN usage | Pass | BPMN is used for process order, participants, messages, events, gateways and exceptions, supported by `[OMG-BPMN]`. |
| UML activity usage | Pass | UML activity is limited to compact internal system behaviour, consistent with Chapter 4 and `[OMG-UML]`. |
| DMN boundary | Pass | DMN is used for repeatable decision logic and kept separate from human task sequence, consistent with Chapter 9 and `[OMG-DMN-1.5]`. |
| Value stream boundary | Pass | Value streams are presented as stakeholder value progression, not process task sequence, supported by `[OPEN-GROUP-BIZARCH-GUIDES-2022]`. |
| Capability versus process | Pass | The chapter repeatedly distinguishes stable capabilities from time-ordered process activities. |
| No universal notation claim | Pass | The text says no model is universally better and explains switching models by question and audience. |

## Findings

| Severity | Count | Notes |
|---|---:|---|
| Critical | 0 | No standard, notation or source conflict found. |
| Major | 0 | No scope, model-selection or technical boundary issue found. |
| Minor | 0 | No minor technical correction required. |

## Recommendation

Technical accuracy passes for author review. The later author-requested
`FIG-15-01` selection guide reinforces the manuscript tables without changing
the chapter scope or re-teaching notation syntax.
