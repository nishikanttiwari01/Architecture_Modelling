---
title: "Technology, Security, Resilience and Operating Architecture"
chapter: 36
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 36. Technology, Security, Resilience and Operating Architecture

## Chapter purpose

Explain how Horizon Bank's application and information estate runs securely, reliably and accountably across hybrid technology and third-party services. The chapter starts with critical operations and traces the technology, identity, control, observability, recovery and operating responsibilities needed to sustain them.

## Reader outcomes

By the end of this chapter, you should be able to:

- distinguish logical application, technology classification, physical deployment and operating views;
- navigate all 30 technology and resilience classifications and 20 critical operations;
- classify placement and trust boundaries without assuming that an internal network is trusted;
- separate customer, workforce, service and privileged identity responsibilities;
- connect security controls, observability and incident response to business outcomes;
- distinguish availability, recovery, data-loss tolerance and impact tolerance;
- map a critical operation through people, applications, data, interfaces, external networks and recovery evidence;
- avoid inventing quantitative service targets or treating a BIAN Service Domain as a runtime unit.

## Prerequisites and dependencies

- Chapter 35: Enterprise Information and Data Architecture
- The governed Horizon Bank technology, application, interface, external-network, control and critical-operation catalogues

## Required models and artefacts

This chapter uses `technology-resilience.md`, `critical-operations.md`, `applications.md`, `interfaces.md`, `external-networks.md`, `controls.md`, `reconciliations.md` and `scenario-catalogue.md`.

`FIG-36-01 Horizon Bank critical-operation dependency map` is registered and specified. Diagram source remains deferred because the specification has not been approved by the author.

## Worked examples

- Delivery of `HB-CRIT-02 Make a Time-Critical Payment`
- Recovery of payment service after a material cyber disruption using `HB-SCN-19`

## Source requirements

Basel Committee guidance supports critical-operation dependency mapping, third-party management, business continuity, incident management and resilient information and communication technology. Horizon Bank's classes and dependencies remain an author model. [BCBS-OPERATIONAL-RESILIENCE-2021]

National Institute of Standards and Technology (NIST) sources support cybersecurity risk-management, zero-trust and historical contingency-planning concepts. They are not presented as jurisdiction-neutral banking obligations. [NIST-CSF-2.0] [NIST-SP-800-207] [NIST-SP-800-34R1]

OpenTelemetry documentation supplies current terminology for traces, metrics, logs and telemetry pipelines. Horizon Bank's platform choice remains fictional. [OPENTELEMETRY-DOCS-2026]

## Planned chapter structure

The chapter moves from operating outcomes to technology classes, trust and identity, secure change, observability, critical-operation mapping and dependency-aware recovery.

## Start with the operation, not the platform

Technology architecture answers where and how software and data run. Security architecture answers how identities, resources and information are protected. Resilience architecture answers how acceptable service continues or recovers through disruption. Operating architecture assigns people, processes, tools and evidence to keep the service useful.

The first question is therefore: **what customer or bank outcome must continue, degrade safely or recover, and what does it depend on end to end?** A platform diagram drawn before this question can show redundancy while omitting the only settlement network, manual queue or identity service that actually stops the operation.

Horizon Bank uses a hybrid author model. Logical responsibilities may be realised on retained mainframe and distributed systems, private or public cloud platforms, software as a service, managed technology and external financial networks. The catalogue does not invent regions, availability zones, node counts, vendors or contractual service levels.

## Keep four architecture levels separate

| Level | Question | Example |
|---|---|---|
| Logical application | Which software responsibility exists? | `HB-APP-034 Payment Orchestration` |
| Technology classification | What consequence, control and recovery concern applies? | `HB-TECH-009 Payments Processing Classification` |
| Physical deployment | Where do runtime units, stores and networks run? | Pending physical topology and location decisions |
| Operating view | Who monitors, decides, repairs and evidences the service? | Payment Operations, service owner, security and recovery roles |

A technology classification is not a deployment node or service-level agreement. A `Tier 1` application is a qualitative flag pending approved objectives. Physical design must later prove that its dependencies, recovery path and operating model meet the business requirement.

## The 30 technology and resilience classifications

The catalogue classifies the whole logical estate by the kind of technology responsibility and consequence involved.

| Area | Governed classifications |
|---|---|
| Identity and channels | `HB-TECH-001 Customer Identity and Access Classification`; `HB-TECH-002 Digital and Partner Channel Classification`; `HB-TECH-003 Assisted Channel Classification`; `HB-TECH-004 Party, CRM, Onboarding and KYC Classification` |
| Deposits, lending and credit | `HB-TECH-005 Deposit and Account Servicing Classification`; `HB-TECH-006 Statement and Correspondence Classification`; `HB-TECH-007 Lending Origination and Servicing Classification`; `HB-TECH-008 Credit Risk Lifecycle Classification` |
| Payments, foreign exchange and cards | `HB-TECH-009 Payments Processing Classification`; `HB-TECH-010 Foreign-Exchange Processing Classification`; `HB-TECH-011 Card Issuing and Processing Classification`; `HB-TECH-012 Merchant Acquiring Classification` |
| Corporate, trade, wealth and securities | `HB-TECH-013 Corporate Cash Management Classification`; `HB-TECH-014 Trade Finance Classification`; `HB-TECH-015 Wealth and Portfolio Management Classification`; `HB-TECH-016 Securities, Custody and Asset Servicing Classification` |
| Treasury, finance and reporting | `HB-TECH-017 Treasury and Markets Classification`; `HB-TECH-018 Finance, Subledger and General Ledger Classification`; `HB-TECH-019 Reconciliation and Finance-Control Classification`; `HB-TECH-020 Regulatory and Management Reporting Classification` |
| Risk, assurance and shared work | `HB-TECH-021 Enterprise Risk Classification`; `HB-TECH-022 Financial Crime, Fraud and Compliance Classification`; `HB-TECH-023 Audit, Legal and Records Classification`; `HB-TECH-024 Document, Workflow, Rules and Case Platform Classification` |
| Integration, data and security | `HB-TECH-025 Integration and External Connectivity Classification`; `HB-TECH-026 Operational and Analytical Data Platform Classification`; `HB-TECH-027 Cybersecurity and Secrets Control-Plane Classification`; `HB-TECH-028 Observability and Service Operations Classification` |
| Enterprise support and recovery | `HB-TECH-029 Workforce and Enterprise Support Classification`; `HB-TECH-030 Backup, Recovery and Continuity Services Classification` |

Each record states a technology class, resilience class, service owner, technology owner, scope, relationships and gap. All 30 are `Target`, `Proposed` classifications because business impact analysis, quantitative objectives, physical dependencies and tested recovery evidence remain to be established. The applications they classify can still be current or target.

### Technology and resilience classes answer different questions

The controlled technology classes describe customer interaction, financial transaction processing, business record and workflow, control and decisioning, integration and external connectivity, data, accounting and reporting, security and the technology control plane, and enterprise support.

The resilience classes describe whether a responsibility is directly performing a critical operation, supporting one, performing time-sensitive financial processing, supplying a controlled business service or supporting the enterprise. This is a classification of consequence, not a ranking of prestige.

## The 20 critical operations

A critical operation is an end-to-end outcome that the bank needs to deliver through disruption within approved tolerances. It is broader than one application or process step.

| Outcome group | Governed critical operations |
|---|---|
| Customer access and deposits | `HB-CRIT-01 Access Funds and Account Information`; `HB-CRIT-03 Authenticate and Authorise Customer Access`; `HB-CRIT-04 Maintain Deposit Account Posting Integrity`; `HB-CRIT-20 Deliver Material Customer Communications` |
| Payments and cards | `HB-CRIT-02 Make a Time-Critical Payment`; `HB-CRIT-05 Clear and Settle Payment Obligations`; `HB-CRIT-06 Authorise and Control Card Activity`; `HB-CRIT-07 Process Card Clearing and Merchant Funding` |
| Credit and corporate services | `HB-CRIT-08 Disburse and Service Credit`; `HB-CRIT-09 Maintain Credit Limits and Exposure`; `HB-CRIT-10 Operate Corporate Cash and Liquidity Services`; `HB-CRIT-11 Issue and Honour Trade-Finance Instruments` |
| Securities, treasury and finance | `HB-CRIT-12 Safeguard Client Assets and Positions`; `HB-CRIT-13 Settle Securities and Service Entitlements`; `HB-CRIT-14 Manage Intraday Liquidity and Funding`; `HB-CRIT-15 Maintain Authoritative Financial Books`; `HB-CRIT-17 Produce and Submit Material Regulatory Returns` |
| Control and recovery | `HB-CRIT-16 Perform Mandatory Screening and Financial-Crime Intervention`; `HB-CRIT-18 Contain and Recover from a Material Cyber Incident`; `HB-CRIT-19 Coordinate Enterprise Service Recovery` |

These records are broad enough to include people, premises, data, applications, interfaces, external networks, suppliers and manual work. They are specific enough to assign owners and test scenarios. [BCBS-OPERATIONAL-RESILIENCE-2021]

## Placement follows evidence

Workload placement considers state, latency, data sensitivity, external connectivity, operational skills, vendor support, resilience, cost, legal constraints and exit. No platform is automatically strategic for every workload.

A physical placement view should identify:

- runtime units and stateful stores;
- regions, sites, zones and network boundaries where relevant;
- inbound, outbound and administrative paths;
- identity, secret and key dependencies;
- replication, backup, restore and reconciliation paths;
- operational ownership and supplier boundaries;
- current, transition and target state.

An application can use several deployment patterns. A channel may scale horizontally while a ledger remains carefully partitioned. A recovery environment may be warm, cold or active, but the label is insufficient without data, activation, validation and failback behaviour.

## Trust boundaries and identity

A trust boundary is where the basis for trust or control changes. Useful Horizon Bank boundaries include public access, customer-channel edge, partner connectivity, workforce access, application services, restricted data, administration, security management and external financial networks.

Network location does not grant trust. NIST zero-trust guidance supports reducing implicit trust and making resource access decisions explicit. [NIST-SP-800-207]

Four identity responsibilities must remain visible:

| Identity | Governed responsibilities |
|---|---|
| Customer | `HB-APP-008 Customer Identity and Access Management` authenticates customers; `HB-APP-010 Customer Entitlement and Mandate Service` supplies business permission decisions |
| Workforce | `HB-APP-011 Workforce Identity Governance` manages identity lifecycle, roles and reviews |
| Service or machine | `HB-APP-089 Secrets and Cryptographic Key Management` protects secrets and keys used by workloads |
| Privileged administrator | `HB-CTRL-37 Workforce and Privileged Access Governance` requires controlled elevation, segregation, review and evidence |

Authentication proves identity to an appropriate confidence. Access authorisation evaluates whether that identity may act on a resource. A mandate or business approval establishes whether a banking action is permitted. One successful login does not satisfy all three.

Every flow across a trust boundary should state initiator, destination, purpose, identity, access decision, information classification, encryption, logging and failure behaviour. A firewall line without those details is not a complete security model.

## Security is a system of controls

Horizon Bank separates domain controls from security-platform responsibilities. `HB-CTRL-38 Security Monitoring and Incident Response` governs detection, triage, containment, recovery and evidence. `HB-APP-085 Security Operations Platform` correlates security telemetry and manages detections. Neither replaces payment screening, credit approval or card fraud controls.

Important shared controls include:

- `HB-CTRL-36 Privacy, Retention and Legal-Hold Enforcement`;
- `HB-CTRL-37 Workforce and Privileged Access Governance`;
- `HB-CTRL-38 Security Monitoring and Incident Response`;
- `HB-CTRL-39 Technology Change and Release Control`;
- `HB-CTRL-40 Backup, Restore and Recovery Test`;
- `HB-CTRL-41 Supplier and Outsourcing Due Diligence`.

The NIST Cybersecurity Framework (CSF) 2.0 provides a high-level risk-management structure. Horizon Bank still needs specific control intent, implementation responsibility and evidence. A framework category is not proof that a control operates effectively. [NIST-CSF-2.0]

### Protect different interaction styles

API security includes client and service identity, access authorisation, input validation, throttling, sensitive-data handling and observability. Event and message security includes authorised publishers and subscribers, schema access, integrity, duplicate or replay handling and retained payloads. File and batch security includes origin, encryption, completeness, cut-off, restart and evidence.

External interfaces also depend on membership, certificates, keys, counterparties, message profiles and fallback. The `HB-EXT-*` records keep these gaps visible rather than relying on network names as security evidence.

## Secure delivery and change

Secure delivery connects source control, peer review, dependency and code checks, build provenance, artefact integrity, environment separation, deployment approval and production evidence. Automation can strengthen evidence, but it does not remove accountability.

`HB-CTRL-39` requires authorised and assessed production change, including later review of emergency change. `HB-APP-087 Information Technology Service Management` holds incident, problem and change records. `HB-SOR-25 Technology Service and Configuration Authority` assigns governed service and configuration responsibility to `HB-APP-087` and `HB-APP-088 Configuration and Service Inventory` within their defined scope.

Release patterns such as rolling, blue-green, canary and feature control depend on compatibility and reversibility. A software rollback cannot always reverse an externally settled payment or posted accounting event. The design also needs roll-forward, compensating business action and reconciliation.

## Observability connects telemetry to action

Observability uses traces, metrics and logs to understand system behaviour. Instrumentation, collection, processing, export, storage and operational use are separate responsibilities. [OPENTELEMETRY-DOCS-2026]

`HB-APP-086 Enterprise Observability Platform` collects and analyses service telemetry. It emits `HB-INT-096 Security-Relevant Observability Event` to `HB-APP-085` and `HB-INT-098 Operational Alert to Incident` to `HB-APP-087`. `HB-APP-088` supplies governed service and dependency context, while `HB-APP-090 Resilience Orchestration and Recovery` coordinates recovery plans and exercise evidence.

Technical telemetry should be joined to business outcomes. Useful payment signals include accepted instructions, rejected or duplicate commands, screening referrals, clearing acknowledgements, settlement breaks, posting delays and repair queues. A healthy processor with a growing unowned investigation queue is not a healthy payment service.

Telemetry needs correlation identifiers, controlled access, retention and sensitive-data processing. It should not copy account, identity, payment or case content into broadly accessible logs. Alerts need an owner, action, severity model and escalation path.

## Availability, recovery and impact tolerance differ

**Availability** asks whether a service can be used when needed. **Recovery Time Objective (RTO)** is a target maximum time to restore a service after disruption. **Recovery Point Objective (RPO)** is a target maximum acceptable data loss measured as time. **Impact tolerance** expresses an approved limit on disruption to an operation under the relevant governance regime.

The repository deliberately records no numerical values. NIST SP 800-34 Revision 1 is a historical official source for RTO and RPO terminology and contingency-planning concepts, not a current banking regulation. [NIST-SP-800-34R1]

High availability handles expected component failure. Disaster recovery handles a larger loss of capability. Backup supplies a recoverable copy; replication supplies another current copy under a replication model. Neither proves successful restore, clean recovery or business correctness.

A recovery design must cover:

1. detection and accountable declaration;
2. containment and preservation of evidence;
3. dependency readiness and recovery order;
4. trusted data restore or failover;
5. replay boundaries and duplicate protection;
6. reconciliation and business validation;
7. controlled customer or counterparty communication;
8. failback and post-incident learning.

## Worked dependency map: a time-critical payment

`HB-CRIT-02 Make a Time-Critical Payment` begins with an eligible customer instruction and ends with governed settlement, posting, status and evidence. It also depends on `HB-CRIT-03`, `HB-CRIT-05`, `HB-CRIT-14`, `HB-CRIT-16` and, during disruption, `HB-CRIT-19`.

### People and decisions

The customer or authorised corporate user initiates the instruction. Payment Operations owns execution and repair. Settlement Operations owns settlement and nostro completion. Financial Crime Operations owns referred screening cases. Treasury manages intraday liquidity. Customer Service coordinates communication. Technology and security teams restore technical service, but the business owner decides whether a degraded mode is acceptable.

### Applications and interfaces

The principal chain is:

```text
HB-APP-002 or HB-APP-006
  consumes HB-INT-023 or HB-INT-025 from HB-APP-033
HB-APP-033 --HB-INT-036--> HB-APP-034
HB-APP-010 --HB-INT-015--> HB-APP-034
HB-APP-018 --HB-INT-026--> HB-APP-034
HB-APP-020 --HB-INT-027--> HB-APP-034
HB-APP-039 --HB-INT-038--> HB-APP-034, when foreign exchange is required
HB-APP-034 --HB-INT-037--> HB-APP-035
HB-APP-035 exchanges through an applicable HB-EXT-* payment network
HB-APP-036 completes governed settlement and emits HB-INT-066 to HB-APP-056
HB-APP-037 owns investigation and repair
```

The applicable external dependency can be `HB-EXT-001`, `HB-EXT-002`, `HB-EXT-003`, `HB-EXT-004` or `HB-EXT-005`, depending on route. Each remains subject to verified membership, contract, operating window and fallback.

### Data, authority and control

The chain uses `HB-DATA-01`, `HB-DATA-02`, `HB-DATA-03`, `HB-DATA-08`, `HB-DATA-12` and `HB-DATA-14`. Authority moves through `HB-SOR-08` and `HB-SOR-09` rather than staying with the channel.

Key controls include `HB-CTRL-02 Transaction Screening and Referral`, `HB-CTRL-06 Consent, Mandate and Entitlement Enforcement`, `HB-CTRL-14 Payment Instruction, Entitlement and Funds Validation`, `HB-CTRL-15 Payment Duplicate and Idempotency Control` and `HB-CTRL-16 Payment Clearing, Settlement and Nostro Break Control`.

Reconciliation uses `HB-REC-012`, `HB-REC-013`, `HB-REC-014`, `HB-REC-015` and, when foreign exchange is involved, `HB-REC-016`. Those comparisons are part of safe restart. They are not optional after infrastructure failover.

### Technology and operating dependencies

The direct classification is `HB-TECH-009 Payments Processing Classification`. Supporting classifications include `HB-TECH-001`, `HB-TECH-002` or `HB-TECH-003`, `HB-TECH-005`, `HB-TECH-010`, `HB-TECH-022`, `HB-TECH-025`, `HB-TECH-027`, `HB-TECH-028` and `HB-TECH-030`.

The operation also depends on qualified staff, service inventories, runbooks, certificates and keys, customer communication, external-network availability and manual exception capacity. This is why recovery cannot be demonstrated by showing two runtime instances.

## Worked recovery: payment service after cyber disruption

`HB-SCN-19 Recover Payment Service after Cyber Disruption` joins `HB-CRIT-18 Contain and Recover from a Material Cyber Incident`, `HB-CRIT-19 Coordinate Enterprise Service Recovery` and the payment operation.

An illustrative response sequence is:

1. `HB-APP-085` receives a governed detection, and authorised responders assess scope.
2. The bank contains affected identities, keys, channels or workloads without silently bypassing `HB-CTRL-02` or `HB-CTRL-14`.
3. Business owners decide whether to stop, queue, restrict or reroute eligible instructions.
4. `HB-APP-090` coordinates a dependency-aware recovery plan using service records from `HB-APP-088` and operational work in `HB-APP-087`.
5. `HB-CTRL-40` requires protected recovery copies, restore testing, data validation and evidence.
6. Payment, settlement, account and finance owners establish a replay boundary and run `HB-REC-012` to `HB-REC-016` as applicable.
7. `HB-APP-073 Notification and Communications Hub` supports approved communications with delivery evidence.
8. The bank validates normal service, controls failback and retains incident and recovery evidence.

A degraded mode is a business decision. Queuing a payment may be safe before a cut-off and unacceptable after it. Operating without screening or duplicate protection is not a valid degraded mode merely because transaction throughput resumes.

## Batch, close and business-day operation

Continuous customer access is only one operating pattern. `HB-APP-079 Enterprise Batch Scheduler` coordinates timed and dependency-based workloads. `HB-APP-058`, `HB-APP-059` and `HB-APP-060` depend on complete accounting populations, controlled reruns and close sequencing.

Batch architecture records calendars, cut-offs, control totals, restart points, late arrivals, duplicate handling and business-day transition. A system can be technically available while `HB-CRIT-15 Maintain Authoritative Financial Books` cannot complete because a source batch, reconciliation or approval is missing.

Recovery backlog needs capacity. Restoring nominal throughput can still miss a settlement or reporting deadline if queued work cannot be processed safely in time.

## Third parties, concentration and exit

External networks, cloud or managed platforms, data sources and service providers can be essential dependencies. `HB-CTRL-41 Supplier and Outsourcing Due Diligence` covers selection, obligations, ongoing performance, concentration, continuity and exit.

For each material third party, record:

- business and service owner;
- legal entities, data and activities in scope;
- subcontracting and concentration;
- identity, connectivity and control boundaries;
- monitoring, incident communication and recovery evidence;
- fallback, portability and exit constraints.

An exit plan is not a file export. It covers replacement capability, knowledge, records, interfaces, licences, keys, parallel operation, reconciliation and safe decommissioning. Some external financial networks cannot be replaced quickly, and the dependency model should state that constraint.

## Service operations and ownership

Operating ownership includes monitoring, incident, problem, change, configuration, capacity, release, continuity and recovery. A service owner remains accountable for outcome and lifecycle. Operations teams may monitor and respond across many services. Domain teams own business repair. Security teams own cyber response responsibilities. Suppliers own only what contracts and operating arrangements explicitly allocate.

Runbooks should explain diagnosis, decision authority, degraded operation, repair, escalation, recovery and evidence. They should link to the exact service, application, interface and critical operation. A generic restart procedure is inadequate for a financial service with externally visible obligations.

Useful measures include outcome completion, rejected and unresolved work, control referrals, reconciliation breaks, backlog age, recovery exercise findings and alert-to-action flow. Every measure needs population, calculation, owner and decision use. This chapter does not invent targets.

## BIAN and runtime architecture

BIAN helps classify banking responsibilities and semantic interactions. It does not specify Horizon Bank's runtime platform, trust zones, deployment units, database topology, recovery design or operational teams. [BIAN-SERVICE-LANDSCAPE-14]

A safe design sequence is:

```text
critical operation and business tolerance
-> business responsibility and controls
-> logical applications and information authority
-> interfaces and external dependencies
-> candidate BIAN mapping
-> software-service and deployment decisions
-> operating ownership and tested evidence
```

Chapter 50 covers boundary decisions, Chapter 51 covers interaction contracts and Chapter 52 expands deployment, security, resilience, observability and operations.

## Current, transition and target considerations

Horizon Bank's 30 classifications are a proposed target governance model. The application estate contains current and target responsibilities. Physical topology, quantitative tolerances and tested recovery evidence remain gaps.

A transition architecture should state which current controls and recovery paths remain active while new channels, orchestration, integration, data or observability services are introduced. Parallel operation needs monitoring and reconciliation across both paths. Retirement needs proof that dependencies, records, keys, alerts, runbooks and supplier obligations have moved or ended.

Modernisation must not centralise every dependency. A shared integration, identity or data platform can reduce duplication, but it can also increase concentration. Scenario testing and graceful degradation decide whether the shared design is acceptable.

## Common mistakes

- Starting with cloud or mainframe placement rather than the critical operation.
- Treating a technology class as an RTO, RPO or service-level agreement.
- Assuming network location grants trust.
- Combining authentication, access authorisation and business approval.
- Monitoring infrastructure while ignoring business outcomes and repair queues.
- Treating replication as backup or failover as complete recovery.
- Restoring applications without defining replay, duplicate control and reconciliation.
- Omitting people, premises, external networks and suppliers from dependency maps.
- Assuming rollback can reverse a settled transaction or posted accounting event.
- Mapping one BIAN Service Domain to one runtime, team or database.

## Chapter summary

Horizon Bank's operating architecture joins 30 technology and resilience classifications to 20 critical operations. Security follows identities, resources, trust boundaries and evidence. Observability connects telemetry to action. Resilience starts with an outcome and includes people, data, applications, interfaces, external networks, recovery, reconciliation and failback. Physical choices and numerical targets remain deliberately pending until evidence supports them.

## Completion checklist

- [x] All 30 governed technology and resilience classifications are represented.
- [x] All 20 critical operations are represented.
- [x] Logical application, classification, deployment and operating views are distinguished.
- [x] Customer, workforce, service and privileged identities are separated.
- [x] Security, delivery, observability, batch and third-party concerns are covered.
- [x] A time-critical payment is traced through business, technology and control dependencies.
- [x] Cyber recovery includes containment, degraded mode, replay, reconciliation and failback.
- [x] No quantitative target or physical topology is fabricated.
- [x] Diagram production is deferred under the specification-first workflow.

## Key takeaways

- Start resilience modelling with the critical operation and its business tolerance.
- A redundant component does not prove end-to-end resilience.
- Identity, access, business approval and domain controls remain separate decisions.
- Observability is a pipeline from telemetry to accountable action, not only a dashboard.
- Recovery includes trusted data, replay boundaries, reconciliation and failback.
- BIAN responsibilities do not determine runtime or team boundaries.

## Practical exercise

Model `HB-CRIT-11 Issue and Honour Trade-Finance Instruments` during loss of `HB-EXT-016 Trade Finance Messaging Network`. Use `HB-APP-006`, `HB-APP-048`, `HB-APP-038`, `HB-APP-070` and `HB-APP-090`; identify relevant `HB-TECH-*`, `HB-DATA-*`, `HB-CTRL-*` and `HB-REC-*` records. Define a safe degraded mode, decision owner, evidence and exit condition without inventing a duration.

## Review checklist

- [ ] Is the customer or bank outcome stated before technology choices?
- [ ] Are logical, physical, current, transition and target levels explicit?
- [ ] Do trust-boundary flows state identities, decisions, data and failure behaviour?
- [ ] Are domain controls distinct from security-platform responsibilities?
- [ ] Does observability connect technical signals to business outcomes and owners?
- [ ] Are availability, RTO, RPO and impact tolerance used accurately?
- [ ] Does recovery cover dependencies, data integrity, replay, reconciliation and failback?
- [ ] Are people, premises, external networks, suppliers and manual work included?
- [ ] Are quantitative targets and jurisdiction claims supported or left as gaps?
- [ ] Are BIAN, application, software-service, deployment and team boundaries separate?

## References and further reading

- [BCBS-OPERATIONAL-RESILIENCE-2021](../../research/banking/bcbs-operational-resilience-2021.md)
- [NIST-CSF-2.0](../../research/security/nist-csf-2.0.md)
- [NIST-SP-800-207](../../research/security/nist-sp-800-207-zero-trust.md)
- [NIST-SP-800-34R1](../../research/infrastructure/nist-sp-800-34r1-contingency-planning.md)
- [OPENTELEMETRY-DOCS-2026](../../research/infrastructure/opentelemetry-docs-2026.md)
- [BIAN-SERVICE-LANDSCAPE-14](../../research/bian/bian-service-landscape-14.0.md)

## Drafting notes

- `FIG-36-01` remains `Planned`; no diagram source has been created.
- Physical deployment, quantitative impact tolerances, RTOs, RPOs and verified supplier arrangements remain governed gaps.
