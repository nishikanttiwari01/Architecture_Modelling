# Chapter 15 Consistency, Diagram Reuse and Source Review, 2026-07-07

## Evidence Commits

Baseline reviewed for content:

- Commit: `54a84e0 Refine Chapter 15 business process modelling draft`
- Purpose: reviewed Chapter 15 after the focused refinement pass.

Completion evidence for Chapter 15 review and diagram workflow:

- Commit: `4b9f068 Complete Chapter 15 review and diagram assets`
- Purpose: added FIG-15-01, formal review records, the quality gate and status updates.

## Scope

- Chapter 15 manuscript
- `GLOSSARY.md`
- `DIAGRAM_REGISTER.md`
- `SOURCE_REGISTER.md`
- `DECISIONS.md`
- Neighbouring Chapters 14 and 16
- Registered research notes for the source keys used by Chapter 15

## Terminology and Cross-Chapter Consistency

| Check | Result | Evidence |
|---|---|---|
| Controlled process terms | Pass | Business process, process architecture, process level, swimlane, process metric and straight-through processing match the glossary. |
| Chapter 14 bridge | Pass | Chapter 15 correctly follows Chapter 14 by moving from capabilities and value streams to process sequence, responsibility, waits and exceptions. |
| Chapter 16 boundary | Pass | Chapter 15 points to Chapter 16 for software structure views without starting Chapter 16. |
| British spelling | Pass | The chapter uses British spelling such as modelling and organisation. |
| No em dashes | Pass | No em dash or en dash was found in the Chapter 15 manuscript. |
| DEC-023 status | Pass | `DEC-023` remains `Proposed`; it was not changed or marked `Approved`. |

## Diagram Reuse and Accessibility

| Figure | Register status | Review result |
|---|---|---|
| FIG-06-01 | Registered, `Review` | Suitable reuse for the Online Store order fulfilment BPMN process. |
| FIG-06-02 | Registered, `Review` | Suitable reuse for Horizon Bank customer onboarding BPMN collaboration. |
| FIG-06-03 | Registered, `Review` | Suitable reuse for payment repair exception collaboration. |
| FIG-04-05 | Registered, `Review` | Suitable reuse for UML activity scoped to Payments Platform validation. |
| FIG-09-04 | Registered, `Review` | Suitable reuse for the BPMN and DMN responsibility split. |
| FIG-13-02 | Registered, `Review` | Suitable reuse for the Horizon Bank customer onboarding value stream. |
| FIG-15-01 | Registered, `Review` | Suitable original selection guide for choosing the process-related model by question. |

`FIG-15-01` was added after author direction to complete the diagram work. It
remains a selection guide and does not introduce notation teaching or a new
process example.

## Source and Copyright Verification

| Source key | Registered | Use in Chapter 15 | Result |
|---|---|---|---|
| OMG-BPMN | Yes | BPMN process, collaboration, pools, lanes, sequence flows, message flows, events and gateways. | Pass |
| OMG-UML | Yes | UML activity and UML sequence diagram family references at selection level. | Pass |
| OMG-DMN-1.5 | Yes | Separation of repeatable decision logic from process flow. | Pass |
| OPEN-GROUP-BIZARCH-GUIDES-2022 | Yes | Value stream framing reused from Chapters 13 and 14. | Pass |

The chapter does not reproduce standards text, metamodels, official tables or
official diagrams. It uses short source keys and original prose.

## Findings

| Severity | Count | Notes |
|---|---:|---|
| Critical | 0 | No consistency, source or copyright blocker found. |
| Major | 0 | No unregistered source, unregistered figure or cross-chapter conflict found. |
| Minor | 0 | No unresolved minor issue remains. |

## Recommendation

Terminology, cross-chapter consistency, diagram reuse, `FIG-15-01`
registration and source verification pass. Chapter 15 can proceed to author
review once the quality gate and validation checks pass.
