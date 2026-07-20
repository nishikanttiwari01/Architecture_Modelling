# Horizon Bank Governed Case Study

Horizon Bank is the fictional full-service bank used throughout the handbook. Controlled catalogues, not narrative lists in this README, define its architecture elements.

## Governed foundation

| Subject | Authoritative catalogue |
|---|---|
| Bank scope | `bank-profile.md` |
| Current and target assumptions | `assumptions.md` |
| Controlled values | `controlled-vocabularies.md` |
| Business lines | `business-lines.md` |
| Business domains and subdomains | `business-domains.md` |
| Legal entities | `legal-entities.md` |
| Customer segments | `customer-segments.md` |
| Products and hierarchy | `products.md` |
| Value streams | `value-streams.md` |
| Actors and roles | `organisation-and-roles.md` |
| Capabilities | `capabilities.md` |
| Logical applications | `applications.md` |
| Interfaces | `interfaces.md` |
| External networks | `external-networks.md` |
| Processes | `processes.md` |
| Organisation and roles | `organisation-and-roles.md` |
| Data domains | `data-domains.md` |
| Systems of record | `systems-of-record.md` |
| Accounting events | `accounting-events.md` |
| Reconciliations | `reconciliations.md` |
| Controls | `controls.md` |
| Critical operations | `critical-operations.md` |
| Technology and resilience classifications | `technology-resilience.md` |
| Candidate BIAN mappings | `bian-mapping-register.md` |
| Scenarios | `scenario-catalogue.md` |
| Coverage | `coverage-matrix.csv`; readable context in `coverage-summary.md` |

## Governance rules

- Reuse exact IDs and names from the catalogues.
- Use only values defined in `controlled-vocabularies.md`.
- Record relationships with explicit IDs, never prose ranges.
- Keep record status, architecture state, source, confidence, verification, ownership, organisational, legal-entity, jurisdiction and customer-segment dimensions separate.
- Treat source type `Author model` as a fictional teaching decision, not an industry fact.
- Do not start domain drafting until the Phase 1 catalogue set and coverage matrix form a coherent validated baseline.

## Phase 1 gaps

The governed baseline now includes business domains, capabilities, Level 1 and Level 2 processes, organisation and roles, 90 logical applications, typed interfaces, external networks, accounting events, reconciliations, controls, critical operations and technology/resilience classifications. Attribute-level authority, jurisdiction-specific variants, quantitative recovery objectives, verified BIAN mappings and complete scenario-level coverage remain governed gaps. `Pending` in the coverage matrix identifies an unresolved relationship rather than an implied one.
