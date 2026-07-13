---
title: "Full Bank Application and Integration Landscape"
chapter: 34
part: "part-05-bian-case-study"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-13"
---

# 34. Full Bank Application and Integration Landscape

## Chapter purpose

Present the complete application taxonomy for Horizon Bank and explain how enterprise and domain views connect.

## Reader outcomes

By the end of this chapter, the reader should be able to classify application responsibilities, distinguish engagement, orchestration, record, processing, insight and control roles, and review application criticality, integration and rationalisation decisions.

## Prerequisites and dependencies

- Chapter 33: Enterprise Business Architecture of Horizon Bank

## Required models and artefacts

- Controlled application and interface catalogues and enterprise landscape specification

## Worked examples

- Horizon Bank onboarding and payment application responsibilities

## Source requirements

- Use official resilience, integration and technology sources; treat application taxonomy as an author recommendation.

## Planned chapter structure

The following sections establish enterprise application coverage and navigation.

## Applications are not capabilities

A capability states what the bank can do. An application supplies software responsibilities that help people and processes perform it. One capability can use several applications, and one application can support several capabilities. This distinction prevents application names from silently defining the operating model.

## Horizon Bank application layers

| Layer | Illustrative application families |
|---|---|
| Channels and experience | Mobile and web banking, branch, contact centre, corporate portal, host-to-host and partner channels |
| Engagement and orchestration | Customer relationship management, sales, onboarding, journey orchestration, workflow, cases, documents and correspondence |
| Party, product and agreement | Party and Customer Platform, Product Catalogue, pricing, consent, entitlement and agreement services |
| Product and transaction processing | Deposits, lending, collateral, limits, collections, payments, cards, trade, wealth, custody and treasury processors |
| Risk and control | Financial crime, fraud, credit risk, market and liquidity risk, operational risk, compliance, model risk and control evidence |
| Finance and support | Subledgers, general ledger, reconciliation, tax, regulatory reporting, procurement and people systems |
| Integration | API management, Enterprise Integration Platform, Event Platform, managed file transfer, workflow and clearing adapters |
| Data and insight | Operational data stores, Enterprise Data Platform, warehouse or lakehouse, data marts, metadata, lineage, analytics and model platforms |
| Technology and operations | Runtime platforms, mainframe, cloud, network, observability, configuration and service management |
| Security and identity | Customer and workforce identity, privileged access, key management, security monitoring and data protection |
| External ecosystem | Payment and card networks, correspondent banks, market infrastructures, identity providers, bureaus, regulators and suppliers |

These are governed families. Product names and vendors are added only when the application catalogue has an owner and lifecycle record.

## Application roles

- A **system of engagement** manages interaction with a person or partner.
- A **system of orchestration** coordinates work but should not become the accidental owner of all rules.
- A **system of record** is authoritative for a defined entity or attribute scope.
- A **system of processing** performs product or transaction behaviour.
- A **system of insight** supports analysis and decision information.
- A **system of control** provides independent checks, limits, alerts or evidence.

An application can have more than one role, but each role and authority boundary must be stated.

## Current, target and transition

Horizon Bank's current state includes duplicate customer data, product silos and point-to-point integration. The target direction introduces governed party data, modular responsibilities, reusable interfaces and better control traceability. A transition application may be necessary for coexistence, but it needs an exit condition.

The existing `Enterprise Integration Platform` is marked `Transitional`. That does not mean integration disappears. It means adapters and routing should not become permanent substitutes for clear domain contracts and ownership.

## Regional, legal-entity and sourcing variants

An application record states business and legal-entity scope, deployment regions, owner, vendor, build or buy decision and support model. Software as a service may reduce local operation but does not transfer accountability for access, data, continuity or exit.

Regional variants are justified by product, language, infrastructure or legal need. Unexplained variants become duplication.

## Integration styles

| Style | Suitable when | Important design questions |
|---|---|---|
| Synchronous API | An immediate response is needed | Timeout, retry, idempotency, authorisation and degraded behaviour |
| Event | Consumers react to a completed fact | Ownership, schema evolution, ordering, duplication and replay |
| Queue or asynchronous command | Work can complete later | Acceptance, correlation, dead-letter handling and status |
| Batch or file | Volume, schedule or external convention requires it | Cut-off, completeness, restart, control totals and repair |
| Workflow | Human or long-running work needs coordination | Ownership, timers, evidence, escalation and cancellation |

No style is universally modern or superior. External payment and market infrastructures may require specific protocols, windows and fallback arrangements.

## Application relationships

Every application must link to supported capabilities, processes, authoritative or consumed data, interfaces, controls, critical operations and production ownership. Orphan applications and orphan interfaces are architecture findings.

For example, `Customer Onboarding Platform` orchestrates onboarding but does not become authoritative for all party data. It uses the `Party and Customer Platform` for governed party identity and the `Financial Crime Platform` for screening and cases. The exact write authority is defined in Chapter 35's system-of-record matrix.

## Criticality and operations

Criticality considers customer, financial, regulatory and operational impact. It does not equal availability. A critical application needs explicit service hours, recovery class, data-loss tolerance, dependencies, support ownership, monitoring and degraded mode. Numerical targets require evidence.

Operational resilience also requires mapping shared technology and third-party dependencies across critical operations. [BCBS-OPERATIONAL-RESILIENCE-2021]

## Rationalisation

Horizon Bank assesses applications against functional fit, strategic fit, data authority, control effectiveness, technical condition, cost, vendor risk, resilience and change demand. Disposition values are `Invest`, `Tolerate`, `Migrate`, `Replace` and `Retire`, each with evidence and transition dependencies.

Adding another integration layer is not rationalisation. A façade can support migration, but it requires an owner, measurable purpose and retirement or steady-state decision.

## Common mistakes

- Drawing only digital channels and calling it the bank landscape.
- Treating every database as a system of record.
- Mixing current and target systems without lifecycle markers.
- Omitting finance, reconciliation, security, support and external networks.
- Calling asynchronous integration an event architecture without event ownership.
- Marking an application for retirement without sequencing data and interface migration.

## Key takeaways

- The enterprise landscape covers every major application family and external ecosystem.
- Application roles and data authority must be qualified.
- Integration style follows business timing and failure semantics.
- Criticality requires end-to-end dependency and operating information.
- Rationalisation needs evidence, transition states and decommissioning criteria.

## Practical exercise

Classify the `Payments Platform`, `Financial Crime Platform`, `Core Deposit System`, `Event Platform` and `Enterprise Data Platform` by application role. Identify one data authority question and one failure dependency for each.

## Review checklist

- [x] All required application layers are represented.
- [x] Application roles, lifecycle and sourcing variants are explained.
- [x] Integration styles include APIs, events, batch, files and workflow.
- [x] Criticality and rationalisation use controlled criteria.
- [ ] The complete application catalogue and figures remain governed deliverables.

## References and further reading

- [BCBS-OPERATIONAL-RESILIENCE-2021]

## Drafting notes

- Complete application ownership, lifecycle, criticality and interface records before formal review.
