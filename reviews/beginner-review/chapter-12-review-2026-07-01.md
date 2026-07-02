# Chapter 12 Beginner Review, 2026-07-01

## Scope

- Chapter: `manuscript/part-02-modelling-languages/12-security-modelling.md`
- Review focus: beginner comprehension, sequencing and overloaded terminology.
- Status after review: `Revision Required`

## Findings

| ID | Severity | Evidence | Required action | Resolution status |
|---|---|---|---|---|
| CH12-BEG-01 | Major | Beginners could encounter trust boundaries, STRIDE and control mapping before seeing the basic ingredients of a security model. | Add a simple foundation table before the viewpoint catalogue. | Resolved. |
| CH12-BEG-02 | Major | The word authorisation appeared in multiple meanings without enough explanation. | Separate access authorisation, business approval and payment-provider authorisation. | Resolved. |
| CH12-BEG-03 | Major | The delegated login example risked being read as a complete protocol design. | Add a chapter depth boundary and keep identity-protocol detail out of scope. | Resolved. |
| CH12-BEG-04 | Minor | The former matrix-as-figure would be harder for beginners to interpret than a direct table. | Present it as `TABLE-12-01` with columns for subject, action, resource, condition and enforcement point. | Resolved. |
| CH12-BEG-05 | Major | Privacy and telemetry concerns were not concrete enough for beginners to inspect. | Add a data-handling table covering identity context, account reference, payment details, screening result, audit event, logs and analytics extracts. | Resolved. |

## Beginner conclusion

The revised chapter now follows a clearer learning path: purpose, foundation, viewpoints, boundary, identity, access, threats, controls and privacy. It remains in review because the author still needs to confirm whether the level of banking-security depth is right for Chapter 12.

## Diagram-production update, 2026-07-02

The rendered figures support the beginner sequence in the chapter:

- `FIG-12-01` shows trust-boundary changes before detailed identity and threat modelling.
- `FIG-12-02` makes the difference between authentication, session handling and access authorisation visible.
- `FIG-12-05` narrows the attack tree to one harmful goal and explains why some related threats are excluded.
- `FIG-12-04` shows data movement and threat-review points without turning the DFD into a BPMN process.

The figures include captions, accessibility text and limitation statements in the manuscript. They remain `Review`, not `Approved`.

## Final diagram-correction update, 2026-07-02

The final correction pass improves beginner interpretation:

- `FIG-12-01` avoids implying that reaching the public edge means the request is authenticated.
- `FIG-12-04` makes privileged-user information presentation visible, including the Operations Analyst receiving the assigned repair case and permitted payment context through the authorised operations interface before submitting a controlled repair action.
- `FIG-12-04` shows the Approved Event Consumer path, so `T12-06` is easier to understand as event-data exposure rather than payment release.
- `FIG-12-05` shows `T12-08` as an AND branch, so readers do not have to infer combined conditions from text inside one box.

Final author and page-layout review remain open.
