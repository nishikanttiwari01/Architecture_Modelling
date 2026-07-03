# Chapter 13 Technical Review, 2026-07-02

Reviewed baseline: `21c66d430c42eb1c1a404fcbcf2d1e827d59c455`

Focused correction baseline: `4e5b90d7fbf355ae9ade5772fbc40e9218c3513b`

| ID | Severity | Affected file/section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH13-TECH-01 | High | `manuscript/part-02-modelling-languages/13-other-modelling-approaches.md`, SysML | Requirement trace used broad prose and did not distinguish requirement, design response, verification case and evidence. | Add stable requirement IDs, testable wording and neutral trace labels. | Resolved in manuscript and `FIG-13-01` specification. |
| CH13-TECH-02 | High | Chapter 13 value stream and `FIG-13-02` | Stages such as internal collection and assessment read as tasks. | Reframe stages as stakeholder-value outcomes and distinguish value stream from BPMN, customer journey and Lean value stream mapping. | Resolved in manuscript and specification. |
| CH13-TECH-03 | Medium | Chapter 13 integration landscape | Narrative used relationship wording without a structured exchange view. | Add exchange table with precise integration styles and review concerns. | Resolved in manuscript. |
| CH13-TECH-04 | Medium | Chapter 13 roadmap and `FIG-13-04` | Generic transition labels hid architecture meaning and exit evidence. | Rename states and add dependency, risk, assumption, decision and exit evidence requirements. | Resolved in manuscript and specification. |
| CH13-TECH-05 | High | Chapter 13 heat map and `FIG-13-05` | The heat-map basis combined several dimensions into one rating. | Separate Current pain, Strategic importance and Delivery risk; require criteria, date, owner and version. | Resolved in manuscript, specification and heat-map convention note. |
| CH13-TECH-06 | Medium | Chapter 13 Wardley map and `FIG-13-06` | Screening/fraud and platform components were collapsed too coarsely. | Split components and clarify dependency lines as value-chain dependencies. | Resolved in manuscript and specification. |
| CH13-TECH-07 | Medium | Chapter 13 ADR section | ADR guidance risked over-attributing alternatives to the original Nygard pattern. | Add original example and clarify alternatives as a local extension. | Resolved in manuscript and source note. |
| CH13-TECH-08 | High | `FIG-13-01` required relationships | Specification incorrectly said design response to verification case was `verified by`. | Change verification semantics so Requirement to Verification case is `verified by`, while Requirement to Design response is `addressed by` and Verification case to evidence is `evidenced by`. | Resolved in manuscript and `FIG-13-01` specification. |
| CH13-TECH-09 | Medium | Chapter 13 integration landscape | Integration table lacked explicit source, destination, information exchanged, direction and contract ownership. | Replace the table with explicit exchange columns and named information objects. | Resolved in manuscript. |
| CH13-TECH-10 | Medium | `FIG-13-03` required relationships | Application-landscape relationships used generic `connects to` wording. | Replace generic relationships with precise landscape-level labels and require one visible lifecycle marker per system. | Resolved in `FIG-13-03` specification. |
| CH13-TECH-11 | Medium | `FIG-13-06` component positioning | Wardley component positions were not defined for every component. | Add explicit component positioning assumptions with visibility, evolution stage, rationale and confidence or open question. | Resolved in manuscript and `FIG-13-06` specification. |

Open technical issue: diagram source and exports were intentionally not created until author approval of `FIG-13-01` through `FIG-13-06` specifications.

## Diagram production update, 2026-07-03

The author approved the revised specifications for production. Diagram sources and exports now exist and are recorded as `Review`.

- CH13-TECH-08 verification semantics are realised in `FIG-13-01`: requirement to design response uses `addressed by`, requirement to verification case uses `verified by`, and verification case to evidence uses `evidenced by`. There is no design response to verification case relationship.
- CH13-TECH-10 precise application-landscape relationship labels and one lifecycle marker per system are realised in `FIG-13-03`.
- CH13-TECH-04 named roadmap states with dependency, risk, assumption, decision and exit evidence are realised in `FIG-13-04`.
- CH13-TECH-05 separated heat-map dimensions with no composite score are realised in `FIG-13-05`.
- CH13-TECH-06 and CH13-TECH-11 separated Wardley components and defined positions are realised in `FIG-13-06`.

Remaining technical item: a Draw.io graphical open and export-fidelity confirmation for the five Draw.io figures is recommended before author approval.
