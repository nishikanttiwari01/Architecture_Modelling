# Horizon Bank Illustrative Capability Catalogue

This catalogue provides controlled capability names for teaching examples. These are illustrative business abilities, not process steps, organisation units, applications or BIAN Service Domains.

| Capability | Plain-language meaning | Notes |
|---|---|---|
| Customer Onboarding | Ability to establish a new customer relationship from initial intent to usable banking services. | Do not decompose into BPMN tasks in Chapter 13. |
| Relationship Management | Ability to understand and manage customer relationships across products and channels. | Business capability, not a sales team. |
| Digital Servicing | Ability to provide customer self-service through digital channels. | Enabled by systems, but not itself an application. |
| Document Capture | Ability to collect and retain required customer documents. | Capability name is broader than one upload step. |
| Identity Verification | Ability to confirm customer identity to the required assurance level. | Keep separate from broader financial-crime controls. |
| Financial Crime Screening | Ability to screen customers and transactions against financial-crime controls. | Not a BIAN Service Domain mapping. |
| Risk Assessment | Ability to assess relevant onboarding, product or transaction risk. | Used only at introductory level in Chapter 13. |
| Party Management | Ability to maintain party identity and relationship records. | Capability, not the Party and Customer Platform application. |
| Account Opening | Ability to establish deposit-account records and access rights. | Distinct from later account servicing. |
| Product Management | Ability to define and manage product propositions and eligibility. | Capability, not the Product Catalogue system. |
| Payment Initiation | Ability to accept and start outgoing payment instructions. | Distinct from payment orchestration implementation. |
| Payment Screening | Ability to check payment instructions against screening obligations. | Used in the heat-map example. |
| Account Servicing | Ability to support account enquiries, status and servicing actions. | Distinct from Core Deposit System implementation. |
| Fraud Management | Ability to detect, decide and manage fraud risk. | Keep separate from financial-crime screening where useful. |
| Notification Management | Ability to send customer and operational notifications. | Cross-cutting capability. |
| Data Governance | Ability to set and enforce data ownership, quality and access rules. | Used in the heat-map example. |
| Event Governance | Ability to define, approve and manage reusable enterprise events. | Used in the heat-map and roadmap examples. |

## Controlled capability levelling (teaching example)

Chapter 14 uses a small, explicit levelling example. Levels and parents below are teaching decisions for this book, not an authoritative bank taxonomy. Only the decompositions recorded here are treated as parent-and-child; every other capability in the catalogue above is a level-one capability with no parent unless a later decision adds one.

| Capability | Level | Parent capability | Plain-language meaning |
|---|---|---|---|
| Customer Onboarding | 1 | (none) | Establish a new customer relationship from initial intent to usable services. |
| Document Capture | 2 | Customer Onboarding | Collect and retain required customer documents during onboarding. |
| Identity Verification | 2 | Customer Onboarding | Confirm customer identity to the required assurance level during onboarding. |
| Risk Assessment | 2 | Customer Onboarding | Assess relevant onboarding risk. |
| Financial Crime Screening | 1 | (none) | Screen customers and transactions against financial-crime controls. |
| Payment Screening | 1 | (none) | Check payment instructions against screening obligations at payment initiation. |

Three relationships must not be confused:

- **Decomposition (parent and child):** `Document Capture`, `Identity Verification` and `Risk Assessment` are children of `Customer Onboarding`. A parent's scope is the sum of its children; do not also count a child separately at level one.
- **Contribution to a value stage:** a capability can enable a value-stream stage without being a child of that stage's headline capability. For example, `Financial Crime Screening` contributes to the onboarding "Identity and eligibility confirmed" stage but is a level-one peer of `Customer Onboarding`, not a child of it.
- **Dependency:** one capability may depend on another (for example, screening depends on party data) without either being a parent or child of the other.

`Financial Crime Screening` and `Payment Screening` are kept as separate level-one peers, not parent and child. To avoid double counting, each is scoped to a distinct control point: `Financial Crime Screening` covers customer and onboarding screening obligations, while `Payment Screening` covers screening of payment instructions at payment initiation. If a later decision chooses to treat `Payment Screening` as a specialised child of `Financial Crime Screening`, that decomposition must be recorded here explicitly and the peer scoping removed to prevent overlap.
