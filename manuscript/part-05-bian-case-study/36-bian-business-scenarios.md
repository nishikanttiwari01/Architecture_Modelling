---
title: "Technology, Security, Resilience and Operating Architecture"
chapter: 36
part: "part-05-bian-case-study"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-13"
---

# 36. Technology, Security, Resilience and Operating Architecture

## Chapter purpose

Explain how Horizon Bank's application and data estate runs securely, reliably and accountably across hybrid technology and third-party services.

## Reader outcomes

By the end of this chapter, the reader should be able to classify placement and trust boundaries, distinguish identity types, connect observability to business control, and map a critical operation through availability, recovery and third-party dependencies.

## Prerequisites and dependencies

- Chapter 35: Enterprise Information and Data Architecture

## Required models and artefacts

- Technology, control, non-functional requirement and critical-operation catalogues

## Worked examples

- Horizon Bank time-critical payment and regional-cloud-outage scenarios

## Source requirements

- Use official security, continuity, resilience and observability sources; do not invent quantitative targets.

## Planned chapter structure

The following sections establish the secure and resilient operating baseline.

## Start with the operation, not the platform

Technology architecture answers where and how workloads run. Operating architecture answers who keeps them safe and useful, under what controls, and how service continues through disruption. A cloud or mainframe diagram alone answers neither question.

Horizon Bank uses a hybrid estate: mainframe and distributed on-premises systems, private and public cloud platforms, software as a service and external financial networks. Placement is based on workload, data, latency, resilience, vendor, legal, skills and exit considerations. No platform is automatically preferred.

## Placement and trust zones

Important zones include public access, customer-channel edge, partner connectivity, application services, restricted data, administration, security management and external networks. A boundary states where trust assumptions or control requirements change. Network location alone does not grant trust.

Every flow across a boundary records initiator, destination, purpose, protocol, identity, authorisation, data classification, encryption, monitoring and failure behaviour.

## Identity and access

Customer identity proves and manages access for external users. Workforce identity manages employees and contractors. Machine identity authenticates workloads, devices and automated agents. Privileged access governs elevated administrative actions.

Authentication establishes confidence in an identity. Authorisation decides whether that identity may perform an action on a resource. Entitlements, mandates and transaction approval can require business rules beyond technical role checks.

Secrets, certificates and cryptographic keys require controlled issuance, storage, rotation, revocation, monitoring and recovery. Hard-coded secrets and shared privileged accounts prevent reliable accountability.

## Protecting applications and data

Controls include secure design, threat modelling, code and dependency checks, environment separation, vulnerability and patch management, encryption, tokenisation, masking, data-loss controls and auditable administration. Cardholder-data environments require explicit segmentation based on the applicable card-industry scope; the book does not declare a universal boundary.

API security covers client and workload identity, authorisation, input validation, throttling, sensitive-data handling and monitoring. Event security covers publishers, subscribers, schema access, integrity, replay and retained payloads. Batch and file channels require equivalent attention to origin, completeness, confidentiality and repair.

Fraud and cyber security interact but are not the same function. A compromised credential can create both a cyber incident and fraudulent transactions. Shared signals and coordinated cases are useful, while ownership and evidence remain explicit.

## Secure delivery and change

Secure software delivery connects source control, peer review, build provenance, testing, artefact integrity, deployment approval and production evidence. Separation of duties is risk-based; automation can strengthen evidence but does not remove accountability.

Release patterns include rolling, blue-green, canary, feature control and controlled batch deployment. The correct pattern depends on state, compatibility, reversibility and operational timing. Rollback is not always safe when data or external obligations have changed, so roll-forward and repair plans are also needed.

## Observability and business telemetry

Logs record events, metrics quantify behaviour and traces connect work across components. Business telemetry adds outcomes such as accepted payments, screening referrals, posting failures and reconciliation breaks. Technical health without business outcome monitoring can conceal a failed service.

Telemetry must protect sensitive information, use consistent correlation identifiers and have retention and access controls. Alerts need an owner, response action and escalation path. More telemetry is not automatically better.

## Service operations

Production ownership covers monitoring, incident, problem, change, capacity, configuration, release and service management. Runbooks explain diagnosis, degraded operation, repair and escalation. Major incidents require business, technology, security, communications and supplier coordination.

Batch operations add calendars, cut-offs, dependencies, control totals, restart points, late processing and business-day transitions. A system can be technically available while the bank cannot complete its accounting or settlement day.

## Availability and recoverability

High availability reduces interruption from expected component failures. Disaster recovery restores service after a larger loss of capability. Backup protects recoverable data; restoration testing proves that data can be used. Cyber recovery considers trusted restoration after compromise.

Recovery time objective and recovery point objective are design inputs, not synonyms for availability or impact tolerance. Horizon Bank uses qualitative classes until evidence supports numbers:

| Attribute | Illustrative classes |
|---|---|
| Criticality | Critical, High, Medium, Low |
| Service hours | Continuous, Extended hours, Business hours |
| Recovery | Immediate failover, Rapid restore, Scheduled restore |
| Data recovery | No committed loss, Bounded loss, Reconstructable |

Every class needs a definition and owner before use in a catalogue.

## Operational resilience

Operational resilience concerns delivery of critical operations through disruption. Official Basel guidance connects governance, operational risk, continuity, dependency mapping, third parties, incidents and resilient information and communication technology. [BCBS-OPERATIONAL-RESILIENCE-2021]

For `Make a time-critical payment`, Horizon Bank maps:

```text
customer and staff
→ identity and channel
→ payment validation and orchestration
→ screening and decision
→ account balance and posting
→ clearing, liquidity and settlement
→ status, repair and communication
→ reconciliation and evidence
```

Each step links to applications, data, facilities, technology, people and third parties. Severe but plausible scenarios test the chain and its degraded modes. A component recovery test is necessary but insufficient.

## Capacity, performance and scaling

Capacity models consider normal volume, peaks, concurrency, message size, batch window, settlement cut-offs and recovery backlog. Scaling stateless channel components does not solve a constrained ledger, external network or manual repair queue.

Performance targets must be linked to customer or operational outcomes. A low API latency is not useful if downstream posting completes after the business deadline.

## Third parties, concentration and exit

External providers and market infrastructures can be essential dependencies. Horizon Bank records service owner, contractual scope, data location, controls, subcontractors, monitoring, continuity, concentration, fallback and exit.

An exit plan is more than data export. It considers replacement capability, knowledge, interfaces, licences, keys, records, parallel operation, customer impact and safe decommissioning. Some financial networks cannot be substituted quickly; the architecture must state that constraint.

## Service levels and error budgets

Service-level objectives can guide reliability decisions where measurable service indicators and accountable consumers exist. Error budgets can support change decisions for suitable digital services, but they do not replace regulatory, financial, safety or settlement obligations. A critical accounting control cannot be waived because an aggregate availability budget remains.

## Assurance evidence

Evidence includes approved designs, access decisions, deployment records, test results, vulnerability decisions, incident timelines, recovery tests, reconciliations, control attestations and supplier reviews. Evidence has an owner, retention rule and integrity protection.

## Common mistakes

- Treating cloud placement as the target architecture without workload evidence.
- Drawing network zones without identities and data flows.
- Equating backup with tested recovery.
- Monitoring infrastructure while ignoring business outcomes.
- Assigning one recovery target to every application in a critical operation.
- Omitting manual work, facilities and third parties from resilience maps.
- Assuming rollback can reverse settled financial activity.

## Key takeaways

- Placement, security, operations and resilience are connected but distinct concerns.
- Customer, workforce, machine and privileged identities require different governance.
- Observability must connect technical behaviour to business outcomes.
- Critical operations are mapped end to end, including people and third parties.
- Availability, recovery and impact tolerance answer different questions.
- Assurance depends on retained, trustworthy evidence.

## Practical exercise

Map `Access account balance during a regional cloud outage`. Identify trust boundaries, authoritative data, degraded behaviour, monitoring, people, supplier dependencies and recovery evidence. Do not invent numerical targets.

## Review checklist

- [x] Hybrid placement, trust boundaries and identity types are covered.
- [x] Security includes applications, APIs, events, data and delivery.
- [x] Operations include batch, incidents, observability and support ownership.
- [x] Resilience includes critical operations, recovery, third parties and degraded modes.
- [ ] Required figure specifications need author approval before source creation.

## References and further reading

- [BCBS-OPERATIONAL-RESILIENCE-2021]
- [NIST-CSF-2.0]
- [NIST-SP-800-207]
- [NIST-SP-800-34R1]
- [OPENTELEMETRY-DOCS-2026]

## Drafting notes

- Complete critical-operation dependencies, qualitative class definitions and operating ownership before formal review.
