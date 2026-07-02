# Chapter 12 Final Review Record, 2026-07-01

## Scope

- Chapter: `manuscript/part-02-modelling-languages/12-security-modelling.md`
- Status after review: `Revision Required`
- Gate status: No passing chapter quality gate created.

## Review coverage

| Area | Finding | Required action | Resolution status |
|---|---|---|---|
| Educational flow | The initial draft needed a clearer progression from security ingredients to viewpoints and examples. | Add foundation and depth-boundary sections before detailed viewpoints. | Resolved, pending author judgement. |
| Technical accuracy | Trust, authentication, access authorisation and control mapping needed stricter wording. | Align with NIST, OWASP and Microsoft sources and separate overloaded terms. | Resolved, pending author judgement. |
| Example consistency | The Online Store Identity Service should not silently rewrite the stable case study. | Label it as an external supporting security service introduced only for the security view. | Resolved. |
| Source quality | Privacy modelling and attack-tree semantics needed direct source notes. | Add NIST Privacy Framework 1.0 and Schneier attack-tree notes. | Resolved. |
| Diagram accessibility | The specifications needed text labels and explicit boundary basis. | Update figure specs to avoid colour-only meaning and ambiguous trust labels. | Resolved. |
| Terminology | Access authorisation, business approval and payment-provider authorisation needed separation. | Update chapter and glossary. | Resolved. |
| Privacy and security wording | Data classification was too narrow for privacy review. | Add privacy modelling table covering purpose, storage, access, retention, logs and analytics. | Resolved. |
| Copyright and attribution | Standards and guidance must be paraphrased, not copied. | Use source-key citations and source notes; do not reproduce standard tables. | Resolved. |
| Threat traceability | Duplicate and mismatched threat IDs made the DFD, attack tree and control map inconsistent. | Give each distinct threat scenario one unique ID and align `T12-01` through `T12-08`. | Resolved. |
| Attack-tree causality | The attack tree included `T12-04` and `T12-06`, which do not directly cause the stated payment-release goal. | Keep `T12-04` and `T12-06` in DFD/control mapping only, outside `FIG-12-05`. | Resolved. |
| Example consistency | `Customer Support Agent` was used in Chapter 12 before being registered as a Horizon Bank role. | Add the role to `examples/horizon-bank/actors.md`. | Resolved. |
| Privacy and security wording | The DFD wording implied trusted identity context came directly from the Retail Customer. | Use session reference from customer to channel, then validated subject and entitlement context from channel to Payments Platform. | Resolved. |
| Copy-editing | Draft contained wording that could confuse authorisation types, boundary meaning and identity-context source. | Revise prose and run terminology and em-dash searches. | Resolved. |

## Remaining work

- Author review is required for the revised Chapter 12 prose and four remaining figure specifications.
- Diagram source and exports must not be created until the author approves the relevant specifications.
- A passing chapter quality gate must not be created until the review cycle is complete.

## Diagram-production update, 2026-07-02

The author approved `DEC-020` and the four remaining figure specifications. Diagram source and exports have now been created for `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05`.

Updated remaining work:

- Complete final author and page-layout review for Chapter 12.
- Keep `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` at `Review` until the author approves them.
- Run the repository quality gates after diagram integration and before any final author-approval recommendation.

## Final diagram-correction update, 2026-07-02

The final diagram correction pass has been applied to `FIG-12-01`, `FIG-12-04` and `FIG-12-05`, with corresponding manuscript, specification, register and review evidence updates.

Focused follow-up correction: `FIG-12-04` now shows the Operations Analyst receiving the assigned repair case and permitted payment context through the authorised operations interface before submitting the controlled repair action through that same interface.

Updated remaining work:

- Final page-layout approval remains pending.
- The author approved Chapter 12 on 2026-07-02.
- Keep Chapter 12 figures at `Review`, not `Approved`, until final page-layout review.
