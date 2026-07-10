# Chapter 21 Technical Review

- Chapter: 21, Modelling Security Architecture
- Review date: 2026-07-11
- Reviewer: Codex
- Outcome: Pass for author review

## Findings

- Critical: none.
- Major: none.
- Minor: none unresolved.

Security context, trust boundaries, authentication, access authorisation, threats,
controls, privacy, audit and monitoring remain distinct. Authentication, access
authorisation, business approval and payment-provider authorisation are separated.
Registered NIST, OWASP, Microsoft and attack-tree sources support the factual framing.
The corrected Horizon Bank example starts after authentication in Horizon Digital
Channels. It models the identity context received and validated by the Payments Platform
for access authorisation, without claiming that customer identity is established inside
the stated scope. It also distinguishes the Payments Platform boundary from the wider
review scope containing external participating systems.

`FIG-21-01` uses explicit labelled directional arrows. Original PNG inspection at
541 by 727 pixels found no clipping, overlap, unreadable text, excessive crossings or
ambiguous direction. Dark text and lines on white or pale backgrounds provide sufficient
contrast. Terminology agrees with the chapter and the portrait layout is readable at
book-page width. The figure remains `Review`, not `Approved`.
