# Chapter 13 Beginner Review, 2026-07-02

Reviewed baseline: `21c66d430c42eb1c1a404fcbcf2d1e827d59c455`

Focused correction baseline: `4e5b90d7fbf355ae9ade5772fbc40e9218c3513b`

| ID | Severity | Affected file/section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH13-BEG-01 | Medium | Chapter introduction | The chapter listed many approaches without grouping them for a beginner. | Add a classification table that explains the role of each family of approaches. | Resolved in manuscript. |
| CH13-BEG-02 | Medium | `SysML` section | Beginners could read traceability as proof. | Explain that traceability links are navigable claims supported by evidence. | Resolved in manuscript and source note. |
| CH13-BEG-03 | Medium | `Capability maps` section | The banking capability examples needed a controlled catalogue. | Add an illustrative Horizon Bank capability catalogue and warn against confusing capabilities with process steps, applications, organisation units or BIAN Service Domains. | Resolved in manuscript and `examples/horizon-bank/capabilities.md`. |
| CH13-BEG-04 | Medium | `Value streams` section | Value stream, BPMN, customer journey and Lean value stream mapping were not separated enough. | Add explicit comparison and outcome-based stage names. | Resolved in manuscript and specification. |
| CH13-BEG-05 | Low | `When to use specialised approaches` | The selection table lacked audience guidance. | Add audience column. | Resolved in manuscript. |
| CH13-BEG-06 | Medium | Chapter introduction | Existing grouping did not classify approaches by standards status, practitioner origin or local convention. | Add a concise approach-classification table with classification, notation status and typical audience. | Resolved in manuscript. |
| CH13-BEG-07 | Medium | Wardley map section | Component positions were discussed as assumptions but not concrete enough for beginners to challenge. | Add a positioning table for every component, including visibility, evolution stage, rationale and confidence or open question. | Resolved in manuscript. |

Open beginner issue: readers could not inspect completed Chapter 13 diagrams while diagram assets were deferred pending author approval of specifications.

## Diagram production update, 2026-07-03

The six figures now exist and are embedded in the manuscript with plain-language captions, accessibility text and a limitation note for each. Each figure keeps colour-independent meaning (stereotype text, lifecycle marker text, High/Medium/Low words and axis labels), which supports beginner readability. The figures are at `Review`.

## Focused correction pass, 2026-07-03

The `FIG-13-02` `triggers` label was moved off the Retail Customer box and stage so that the trigger relationship reads clearly for a beginner. No other figure content changed.
