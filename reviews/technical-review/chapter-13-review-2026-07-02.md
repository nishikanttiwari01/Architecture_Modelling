# Chapter 13 Technical Review, 2026-07-02

Reviewed baseline: `21c66d430c42eb1c1a404fcbcf2d1e827d59c455`

| ID | Severity | Affected file/section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH13-TECH-01 | High | `manuscript/part-02-modelling-languages/13-other-modelling-approaches.md`, SysML | Requirement trace used broad prose and did not distinguish requirement, design response, verification case and evidence. | Add stable requirement IDs, testable wording and neutral trace labels. | Resolved in manuscript and `FIG-13-01` specification. |
| CH13-TECH-02 | High | Chapter 13 value stream and `FIG-13-02` | Stages such as internal collection and assessment read as tasks. | Reframe stages as stakeholder-value outcomes and distinguish value stream from BPMN, customer journey and Lean value stream mapping. | Resolved in manuscript and specification. |
| CH13-TECH-03 | Medium | Chapter 13 integration landscape | Narrative used relationship wording without a structured exchange view. | Add exchange table with precise integration styles and review concerns. | Resolved in manuscript. |
| CH13-TECH-04 | Medium | Chapter 13 roadmap and `FIG-13-04` | Generic transition labels hid architecture meaning and exit evidence. | Rename states and add dependency, risk, assumption, decision and exit evidence requirements. | Resolved in manuscript and specification. |
| CH13-TECH-05 | High | Chapter 13 heat map and `FIG-13-05` | The heat-map basis combined several dimensions into one rating. | Separate Current pain, Strategic importance and Delivery risk; require criteria, date, owner and version. | Resolved in manuscript, specification and heat-map convention note. |
| CH13-TECH-06 | Medium | Chapter 13 Wardley map and `FIG-13-06` | Screening/fraud and platform components were collapsed too coarsely. | Split components and clarify dependency lines as value-chain dependencies. | Resolved in manuscript and specification. |
| CH13-TECH-07 | Medium | Chapter 13 ADR section | ADR guidance risked over-attributing alternatives to the original Nygard pattern. | Add original example and clarify alternatives as a local extension. | Resolved in manuscript and source note. |

Open technical issue: diagram source and exports are intentionally not created until author approval of `FIG-13-01` through `FIG-13-06` specifications.
