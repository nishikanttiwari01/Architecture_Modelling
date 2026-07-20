---
title: "Full Bank Application and Integration Landscape"
chapter: 34
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 34. Full Bank Application and Integration Landscape

## Chapter purpose

Present the complete governed application taxonomy for Horizon Bank and explain how enterprise and domain views connect. The landscape is a logical model of responsibilities and exchanges, not a vendor inventory or deployment diagram.

## Reader outcomes

By the end of this chapter, you should be able to:

- distinguish a capability, logical application, deployable service and technology platform;
- navigate a realistic full-bank application portfolio without reducing it to a few core systems;
- distinguish engagement, orchestration, record, processing, insight and control responsibilities;
- select an integration style from the business timing, ownership and failure semantics;
- trace a customer or transaction outcome across applications, interfaces, external networks and operational controls;
- review lifecycle, authority, resilience and rationalisation decisions without assuming that one Banking Industry Architecture Network (BIAN) Service Domain equals one application.

## Prerequisites and dependencies

- Chapter 33: Enterprise Business Architecture of Horizon Bank
- The governed Horizon Bank application, interface and external-network catalogues

## Required models and artefacts

This chapter uses `applications.md`, `interfaces.md`, `external-networks.md`, `systems-of-record.md`, `technology-resilience.md` and the master coverage matrix. At this checkpoint they contain 90 logical applications, 106 typed interfaces and 17 logical external-network classes.

`FIG-34-01 Horizon Bank application and integration landscape` is registered and specified. Diagram source remains deferred because the specification has not been approved by the author.

## Worked examples

- Customer onboarding across channel, identity, party, workflow, screening and evidence responsibilities
- A cross-border payment across initiation, control, foreign exchange, clearing, correspondent banking, settlement and reconciliation

## Source requirements

The portfolio structure and application boundaries are a Horizon Bank author model. Basel Committee guidance supports the need to map dependencies, third parties and technology across critical operations, but it does not prescribe this application decomposition. [BCBS-OPERATIONAL-RESILIENCE-2021]

BIAN 14.0 is a reference for banking responsibilities. It does not determine the number of applications, interfaces, teams, databases or deployable services in this fictional bank. [BIAN-SERVICE-LANDSCAPE-14]

## Planned chapter structure

The chapter starts with the application boundary, covers the complete portfolio and integration estate, and then demonstrates how to navigate it through end-to-end traces.

## What an application landscape answers

An application landscape answers: **which logical software responsibilities support the bank, who owns them, what information do they govern, and how do they interact?** It gives enterprise architects broad coverage, while allowing a solution architect to follow a smaller path into a domain chapter.

It does not answer detailed process order, physical deployment, database schema or recovery topology. Business Process Model and Notation (BPMN), sequence, information and deployment views answer those questions. Trying to put them all on the same landscape produces a diagram that is dense but unhelpful.

### Capability is not application

A capability says what Horizon Bank must be able to do. An application allocates logical software responsibility. `HB-CAP-050 Payment Management`, for example, is supported by several applications from `HB-APP-033 Payment Initiation Service` through `HB-APP-039 Foreign Exchange Pricing and Booking`. None of those applications is the capability itself.

The reverse is also true. `HB-APP-076 Enterprise Event Streaming Platform` supports several domains, but it does not own their business events. The producing domain owns the event meaning; the platform owns transport, subscription, schema-registry and replay responsibilities within its governed scope.

### Logical is not physical

Each `HB-APP-*` record represents a coherent logical responsibility. One vendor package could realise several records. One record could be realised by several deployable services and stores. A retained mainframe program, a purchased platform and a group of cloud services can all fulfil logical application responsibilities.

This separation keeps the model useful during modernisation. Procurement changes, service decomposition and deployment placement can evolve without erasing business ownership and data authority.

## The complete logical application estate

The catalogue deliberately represents more than customer-facing channels and product processors. Finance, control, integration, data, security and operations are part of the bank. The following portfolio index includes every governed logical application.

| Responsibility area | Governed logical applications |
|---|---|
| Channels | `HB-APP-001 Public Banking Web`; `HB-APP-002 Retail Mobile Banking`; `HB-APP-003 Branch Service Workbench`; `HB-APP-004 Contact Centre Workbench`; `HB-APP-005 Relationship Manager Workbench`; `HB-APP-006 Corporate Digital Banking`; `HB-APP-007 Partner and Open Banking Portal` |
| Identity, consent and entitlement | `HB-APP-008 Customer Identity and Access Management`; `HB-APP-009 Consent and Privacy Preference Service`; `HB-APP-010 Customer Entitlement and Mandate Service`; `HB-APP-011 Workforce Identity Governance` |
| Customer, sales, product and onboarding | `HB-APP-012 Customer Relationship Management`; `HB-APP-013 Enterprise Product Catalogue`; `HB-APP-014 Pricing and Fee Management`; `HB-APP-015 Party Master and Customer Information`; `HB-APP-016 Customer Onboarding Orchestrator`; `HB-APP-017 Know Your Customer Case Management`; `HB-APP-018 Name and Sanctions Screening`; `HB-APP-019 Customer Service Management` |
| Deposits and communications | `HB-APP-020 Deposit Account Processing`; `HB-APP-021 Interest and Fee Accrual`; `HB-APP-022 Statement and Correspondence Management` |
| Lending and credit-risk lifecycle | `HB-APP-023 Consumer Loan Origination`; `HB-APP-024 Mortgage Origination`; `HB-APP-025 Business and Corporate Credit Origination`; `HB-APP-026 Credit Decision Management`; `HB-APP-027 Loan and Facility Servicing`; `HB-APP-028 Collateral Management`; `HB-APP-029 Limit and Covenant Management`; `HB-APP-030 Credit Exposure Aggregation`; `HB-APP-031 Collections Management`; `HB-APP-032 Recovery and Workout Management` |
| Payments and foreign exchange | `HB-APP-033 Payment Initiation Service`; `HB-APP-034 Payment Orchestration`; `HB-APP-035 Payment Routing and Clearing`; `HB-APP-036 Settlement and Nostro Management`; `HB-APP-037 Payment Investigations and Exceptions`; `HB-APP-038 Correspondent Banking Management`; `HB-APP-039 Foreign Exchange Pricing and Booking` |
| Cards and merchant acquiring | `HB-APP-040 Card Issuing Management`; `HB-APP-041 Card Authorisation`; `HB-APP-042 Card Processing and Clearing`; `HB-APP-043 Card Fraud Decisioning`; `HB-APP-044 Card Disputes and Chargebacks`; `HB-APP-045 Merchant Acquiring Management`; `HB-APP-046 Merchant Transaction Gateway` |
| Corporate banking and trade finance | `HB-APP-047 Corporate Cash Management`; `HB-APP-048 Trade Finance Processing` |
| Wealth, securities and custody | `HB-APP-049 Portfolio and Advisory Management`; `HB-APP-050 Investment Order Management`; `HB-APP-051 Securities Processing`; `HB-APP-052 Custody and Safekeeping`; `HB-APP-053 Corporate Actions and Asset Servicing` |
| Treasury and markets | `HB-APP-054 Treasury Trading and Position Management`; `HB-APP-055 Market and Counterparty Risk`; `HB-APP-056 Funding and Liquidity Management`; `HB-APP-057 Asset Liability and Capital Management` |
| Finance, reporting and assurance | `HB-APP-058 Product Subledger Platform`; `HB-APP-059 General Ledger`; `HB-APP-060 Enterprise Reconciliation`; `HB-APP-061 Tax Management and Reporting`; `HB-APP-062 Regulatory Reporting`; `HB-APP-063 Management Reporting and Performance`; `HB-APP-064 Enterprise Risk Management`; `HB-APP-065 Anti-Money Laundering Transaction Monitoring`; `HB-APP-066 Enterprise Fraud Management`; `HB-APP-067 Financial Crime Investigation Case Management`; `HB-APP-068 Internal Audit Management`; `HB-APP-069 Legal Matter and Obligation Management` |
| Documents, workflow, rules and cases | `HB-APP-070 Enterprise Document and Content Management`; `HB-APP-071 Enterprise Workflow Platform`; `HB-APP-072 Enterprise Business Rules Platform`; `HB-APP-073 Notification and Communications Hub`; `HB-APP-074 Enterprise Case Management` |
| Integration platforms | `HB-APP-075 API Management Platform`; `HB-APP-076 Enterprise Event Streaming Platform`; `HB-APP-077 Enterprise Messaging Platform`; `HB-APP-078 Managed File Transfer Platform`; `HB-APP-079 Enterprise Batch Scheduler` |
| Data and information governance | `HB-APP-080 Operational Data Store`; `HB-APP-081 Enterprise Analytical Data Platform`; `HB-APP-082 Regulatory Data Platform`; `HB-APP-083 Metadata and Data Lineage Platform`; `HB-APP-084 Data Quality Management` |
| Security, observability and operations | `HB-APP-085 Security Operations Platform`; `HB-APP-086 Enterprise Observability Platform`; `HB-APP-087 Information Technology Service Management`; `HB-APP-088 Configuration and Service Inventory`; `HB-APP-089 Secrets and Cryptographic Key Management`; `HB-APP-090 Resilience Orchestration and Recovery` |

This is a navigable portfolio, not a claim that ninety packages must be bought or ninety teams created. It is detailed enough to expose authority and lifecycle differences. It also records honest gaps. Teller cash, telephony, workforce, procurement, payroll and some physical platform responsibilities need further governed application records before the estate can claim those areas are fully decomposed.

## Classify application roles precisely

An application can perform more than one role, but the role must be qualified by information and lifecycle.

| Role | Question | Horizon Bank example |
|---|---|---|
| Engagement | Where does a person or partner interact? | `HB-APP-002` provides authenticated retail journeys |
| Orchestration | What coordinates a multi-step outcome? | `HB-APP-034` coordinates payment execution; `HB-APP-016` coordinates onboarding |
| Processing | What changes product or transaction state? | `HB-APP-020` books deposit-account state; `HB-APP-042` processes card clearing |
| Record authority | What establishes a governed fact for a defined purpose? | `HB-APP-015` supports `HB-SOR-01 Party Identity Authority` |
| Decision and control | What evaluates a governed decision or control? | `HB-APP-026` records credit decisions; `HB-APP-018` records screening results and dispositions |
| Insight | What produces a governed analytical view? | `HB-APP-081` supplies analytical data but does not replace operational authority |
| Platform | What provides reusable technical behaviour? | `HB-APP-075` manages APIs; `HB-APP-077` carries durable messages |

The phrase system of record is not assigned to a whole application without qualification. `HB-APP-034` can be authoritative for payment execution state while `HB-APP-036` is authoritative for settlement obligations and nostro positions. Chapter 35 develops this distinction.

## Integration is a portfolio of contracts

The interface catalogue contains 106 logical exchanges. An interface record identifies type, direction, producer, consumer, information, classification, owner, architecture state and gap. It is not a physical endpoint. The governed types and current counts are:

| Interface type | Count | What it communicates | Examples |
|---|---:|---|---|
| Application programming interface (API) | 37 | Request and response where the consumer needs an immediate result | `HB-INT-015 Payment Entitlement Decision`; `HB-INT-038 Foreign Exchange Quote` |
| Command | 10 | A directed request for another responsibility to act | `HB-INT-020 Onboarded Party Establishment`; `HB-INT-036 Accepted Payment Command` |
| Event | 19 | A completed or observed fact made available to consumers | `HB-INT-021 Party Master Change Event`; `HB-INT-066 Intraday Settlement Position Event` |
| Message | 20 | An asynchronous exchange not classified as a command or event | `HB-INT-037 Payment Clearing Instruction`; `HB-INT-073 Trade Finance Network Message` |
| Workflow | 9 | A case or work hand-off requiring ownership, deadlines and evidence | `HB-INT-035 Collections to Recovery Handover`; `HB-INT-058 Due-Diligence Investigation Handoff` |
| Batch | 7 | Scheduled or grouped processing | `HB-INT-082 Subledger Journal Batch`; `HB-INT-087 Regulatory Dataset Batch` |
| File | 4 | A governed file exchange with completeness and receipt controls | `HB-INT-071 Card Dispute Network File`; `HB-INT-088 Regulatory Return Submission` |

These labels are not a maturity ranking. A synchronous API can be the wrong choice for long-running work. A file can be the correct contractual form for an external authority. The design follows the outcome, cut-off, failure and evidence requirements.

### Complete interface portfolio index

The catalogue is the detailed authority for direction, producer, consumer, information, classification and gaps. This chapter still provides an explicit enterprise index so no domain is hidden behind a generic `integration` arrow.

| Interaction area | Governed interfaces |
|---|---|
| Customer access, sales, product and onboarding | `HB-INT-001 Public Lead Capture`; `HB-INT-002 Mobile Customer Authentication`; `HB-INT-003 Branch Customer Authentication`; `HB-INT-004 Contact Centre Customer Authentication`; `HB-INT-005 Relationship Manager Authentication`; `HB-INT-006 Public Product Publication`; `HB-INT-007 Retail Entitlement Check`; `HB-INT-008 Branch Customer View`; `HB-INT-009 Contact Centre Relationship View`; `HB-INT-010 Managed Credit Proposal`; `HB-INT-011 Corporate Customer Authentication`; `HB-INT-012 Partner Authentication`; `HB-INT-013 Consent Preference Change`; `HB-INT-014 Consent Evidence Archive`; `HB-INT-015 Payment Entitlement Decision`; `HB-INT-016 Workforce Identity Lifecycle`; `HB-INT-017 Product Availability for Sales`; `HB-INT-018 Product Price Plan Publication`; `HB-INT-019 Deposit Price Retrieval`; `HB-INT-020 Onboarded Party Establishment`; `HB-INT-021 Party Master Change Event`; `HB-INT-022 Screening Decision for Due Diligence` |
| Deposits, credit and payment initiation | `HB-INT-023 Retail Payment Initiation`; `HB-INT-024 Statement Retrieval`; `HB-INT-025 Corporate Payment Initiation`; `HB-INT-026 Transaction Sanctions Screening`; `HB-INT-027 Funds and Account Control`; `HB-INT-028 Deposit Accrual Event`; `HB-INT-029 Consumer Credit Decision`; `HB-INT-030 Secured and Corporate Credit Assessment`; `HB-INT-031 Card Servicing for Mobile`; `HB-INT-032 Credit Delinquency Event`; `HB-INT-033 Collateral and Limit Update`; `HB-INT-034 Exposure Position Event`; `HB-INT-035 Collections to Recovery Handover`; `HB-INT-036 Accepted Payment Command`; `HB-INT-037 Payment Clearing Instruction`; `HB-INT-038 Foreign Exchange Quote`; `HB-INT-039 Deposit Balance and Transaction Feed`; `HB-INT-040 Loan Accounting Message`; `HB-INT-041 Recovery Accounting Event` |
| Cards, corporate, trade, wealth and shared work | `HB-INT-042 Card Authorisation Message`; `HB-INT-043 Merchant Service Administration`; `HB-INT-044 Card Fraud Decision`; `HB-INT-045 Card Fraud Case Handover`; `HB-INT-046 Merchant Transaction Submission`; `HB-INT-047 Trade Finance Service`; `HB-INT-048 Trade Contingent Exposure Event`; `HB-INT-049 Approved Investment Order`; `HB-INT-050 Executed Investment Allocation`; `HB-INT-051 Settled Securities Position Event`; `HB-INT-052 Customer Communication Request`; `HB-INT-053 Service Case Exchange`; `HB-INT-054 Service and Ownership Inventory`; `HB-INT-055 Legal Document Hold`; `HB-INT-056 Partner API Publication`; `HB-INT-057 Onboarding Workflow Handoff`; `HB-INT-058 Due-Diligence Investigation Handoff`; `HB-INT-059 Screening Alert Event`; `HB-INT-060 Customer Service Workflow`; `HB-INT-061 Credit Rule Decision` |
| Clearing, correspondent, cards and securities ecosystems | `HB-INT-062 Domestic Retail Clearing Exchange`; `HB-INT-063 High-Value Payment Exchange`; `HB-INT-064 Immediate Payment Exchange`; `HB-INT-065 Correspondent Settlement Instruction`; `HB-INT-066 Intraday Settlement Position Event`; `HB-INT-067 Correspondent Investigation Exchange`; `HB-INT-068 Treasury Foreign Exchange Booking`; `HB-INT-069 Card Lifecycle Network Exchange`; `HB-INT-070 Card Clearing and Acquiring Exchange`; `HB-INT-071 Card Dispute Network File`; `HB-INT-072 Cash Structure Payment Command`; `HB-INT-073 Trade Finance Network Message`; `HB-INT-074 Portfolio Market Data Feed`; `HB-INT-075 Investment Venue Order Exchange`; `HB-INT-076 Securities Settlement Exchange`; `HB-INT-077 Corporate Action Exchange` |
| Treasury, accounting, reporting, data and operations | `HB-INT-078 Market Risk Position Feed`; `HB-INT-079 Treasury Liquidity Position Event`; `HB-INT-080 Balance-Sheet Analytical Feed`; `HB-INT-081 Treasury Accounting Event`; `HB-INT-082 Subledger Journal Batch`; `HB-INT-083 General Ledger Reconciliation Feed`; `HB-INT-084 Ledger Tax Feed`; `HB-INT-085 Scheduled Reconciliation Run`; `HB-INT-086 Tax Filing Exchange`; `HB-INT-087 Regulatory Dataset Batch`; `HB-INT-088 Regulatory Return Submission`; `HB-INT-089 Management Reporting Dataset`; `HB-INT-090 Risk and Assurance Finding Exchange`; `HB-INT-091 Financial Crime Alert Event`; `HB-INT-092 Workflow Document Service`; `HB-INT-093 Governed Rule Execution`; `HB-INT-094 Communication Delivery Event`; `HB-INT-095 Data Quality Metadata Exchange`; `HB-INT-096 Security-Relevant Observability Event`; `HB-INT-097 Cryptographic Audit Event`; `HB-INT-098 Operational Alert to Incident`; `HB-INT-099 Recovery Workflow Handoff` |
| Additional governed external exchanges | `HB-INT-100 Identity Verification Exchange`; `HB-INT-101 Screening Data Exchange`; `HB-INT-102 Credit Bureau Exchange`; `HB-INT-103 Open Banking Network Exchange`; `HB-INT-104 Merchant Acceptance Network Exchange`; `HB-INT-105 Cross-Border Financial Message`; `HB-INT-106 Market Data Distribution` |

For an API, the catalogue's producer provides the operation and the consumer invokes it. For commands, events, messages, batches, files and workflows, the producer initiates or emits the exchange. This rule makes arrows reviewable and prevents diagrams from reversing an interface merely because the business journey begins elsewhere.

### Contract questions apply to every style

Every interaction needs enough definition to answer:

- What business meaning and version does the information carry?
- Who can produce, invoke or consume it?
- How are identity, access authorisation and data protection applied?
- What makes a request, command or event duplicate?
- What ordering or effective-time assumptions exist?
- What happens on timeout, rejection, partial completion or replay?
- Who monitors failure, repairs state and closes the evidence trail?

An integration platform does not answer those questions for the domain. `HB-APP-075` can enforce an API policy, and `HB-APP-076` can support retention and replay, but the payment, customer or finance owner still governs business semantics.

## External connectivity is inside the architecture boundary

The bank's responsibilities extend to the point where an authorised exchange is handed to, or received from, another party. The external-network catalogue avoids invented providers and memberships while making dependency classes visible.

| Ecosystem | Governed external-network classes |
|---|---|
| Payments and correspondent banking | `HB-EXT-001 High-Value Payment Network`; `HB-EXT-002 Retail Payment Clearing Network`; `HB-EXT-003 Immediate Payment Network`; `HB-EXT-004 Cross-Border Financial Messaging Network`; `HB-EXT-005 Correspondent Banking Connectivity` |
| Cards and merchant acceptance | `HB-EXT-006 Card Scheme Network`; `HB-EXT-007 Merchant Acceptance Connectivity` |
| Securities and markets | `HB-EXT-008 Securities Trading Venue Connectivity`; `HB-EXT-009 Securities Depository and Custody Connectivity`; `HB-EXT-010 Market and Reference Data Connectivity` |
| Identity, screening and credit information | `HB-EXT-011 Identity Verification Connectivity`; `HB-EXT-012 Screening Data Connectivity`; `HB-EXT-013 Credit Information Connectivity` |
| Tax, regulatory, trade and ecosystem | `HB-EXT-014 Tax Authority Reporting Gateway`; `HB-EXT-015 Prudential and Conduct Reporting Gateway`; `HB-EXT-016 Trade Finance Messaging Network`; `HB-EXT-017 Open Banking and Ecosystem Connectivity` |

Each record is `Unverified` because a real legal entity, contract, jurisdiction, membership and message profile have not been selected. That is stronger governance than drawing a recognisable logo and implying a relationship exists.

## Worked trace: establish a customer relationship

Consider a prospect beginning on `HB-APP-001 Public Banking Web`. `HB-INT-001 Public Lead Capture` sends the enquiry to `HB-APP-012 Customer Relationship Management`. `HB-APP-016 Customer Onboarding Orchestrator` coordinates the case and issues `HB-INT-020 Onboarded Party Establishment` to `HB-APP-015 Party Master and Customer Information` only after the governed decision.

Independent responsibilities remain separate. `HB-APP-018 Name and Sanctions Screening` provides `HB-INT-022 Screening Decision for Due Diligence` to `HB-APP-017 Know Your Customer Case Management`. A specialist referral uses `HB-INT-058 Due-Diligence Investigation Handoff` to `HB-APP-067 Financial Crime Investigation Case Management`. Evidence can be retained by `HB-APP-070 Enterprise Document and Content Management`, while reusable work queues can be hosted by `HB-APP-071 Enterprise Workflow Platform`.

This path demonstrates why the landscape needs more than a channel and a customer database. Party identity, customer relationship management, orchestration, screening, decision evidence, documents and workflow have different authorities and failure modes. Chapter 37 expands the business lifecycle.

## Worked trace: execute a cross-border payment

A corporate customer uses `HB-APP-006 Corporate Digital Banking`. The channel consumes `HB-INT-025 Corporate Payment Initiation`, provided by `HB-APP-033 Payment Initiation Service`, and `HB-INT-011 Corporate Customer Authentication`, provided by `HB-APP-008 Customer Identity and Access Management`.

After acceptance, `HB-APP-033` sends `HB-INT-036 Accepted Payment Command` to `HB-APP-034 Payment Orchestration`. Orchestration consumes `HB-INT-015 Payment Entitlement Decision` from `HB-APP-010`, `HB-INT-026 Transaction Sanctions Screening` from `HB-APP-018`, `HB-INT-027 Funds and Account Control` from `HB-APP-020`, and, when needed, `HB-INT-038 Foreign Exchange Quote` from `HB-APP-039`.

Execution then uses `HB-INT-037 Payment Clearing Instruction` from `HB-APP-034` to `HB-APP-035 Payment Routing and Clearing`. A cross-border route can use `HB-INT-105 Cross-Border Financial Message` with `HB-EXT-004`, followed by correspondent and settlement responsibilities in `HB-APP-038 Correspondent Banking Management` and `HB-APP-036 Settlement and Nostro Management`. `HB-INT-066 Intraday Settlement Position Event` informs `HB-APP-056 Funding and Liquidity Management`. Exceptions belong in `HB-APP-037 Payment Investigations and Exceptions`, not in an unowned integration queue.

The interface path alone is still incomplete. The solution also needs payment and settlement authority, posting, accounting, reconciliation, customer status and operational recovery. Chapters 35, 36, 41, 46 and 51 supply those views.

## Current, target and transition views

The catalogue marks 68 applications as `Current` and 22 as `Target`. Target records include governed party mastering, onboarding orchestration, payment orchestration, enterprise product and pricing responsibilities, shared workflow and rules, managed APIs and event streaming, improved data governance, observability and recovery orchestration.

Those values do not promise implementation dates. A transition view must identify coexistence and exit conditions. For example, moving from country product catalogues to `HB-APP-013` needs definition ownership, effective dating, publication reconciliation and a safe way to identify which processor has adopted a version. Introducing `HB-APP-034` must not obscure rail-specific processing or create two competing payment-status authorities.

A façade or adapter can be a sound transition responsibility. It becomes technical debt when its owner, purpose, consumers, retirement condition and failure handling are not governed.

## Security and trust across the landscape

Authentication, access authorisation and business approval remain different decisions. `HB-APP-008` authenticates customers. `HB-APP-010` evaluates mandates and entitlements. A payment, credit or trade-finance application then applies its domain approval and controls.

Customer, workforce, service and privileged identities cross different trust boundaries. `HB-APP-011 Workforce Identity Governance` manages workforce access governance. `HB-APP-089 Secrets and Cryptographic Key Management` protects machine secrets and keys. `HB-APP-085 Security Operations Platform` handles security detections and evidence. None replaces controls in the product processor.

Information classification is recorded on every interface as `Internal`, `Confidential` or `Restricted`. The classification is not decorative. It informs permitted consumers, authentication strength, encryption, logging, retention and repair procedures.

## Criticality and operational ownership

Application resilience tiers are qualitative. `Tier 1`, `Tier 2` and `Tier 3` do not invent a Recovery Time Objective (RTO), Recovery Point Objective (RPO) or availability promise. Business impact analysis and scenario dependency mapping must set those expectations.

The catalogue gives every application a service owner and a gap. A critical operation normally depends on several applications and shared services. `HB-CRIT-02 Make a Time-Critical Payment`, for example, depends on channels, identity, entitlement, payment processing, screening, deposit posting, clearing, settlement, external networks, liquidity, communication, reconciliation, observability and people. Chapter 36 develops this operating view. [BCBS-OPERATIONAL-RESILIENCE-2021]

## BIAN alignment without false equivalence

BIAN can help compare responsibilities across payment, credit, deposits and other banking areas. The Horizon Bank register keeps mappings versioned, sourced, confidence-rated and many-to-many. [BIAN-SERVICE-LANDSCAPE-14]

The application portfolio remains an independent design. A Service Domain does not automatically become one `HB-APP-*` record, software service, team or database. Conversely, a shared application such as `HB-APP-070` may support many BIAN-aligned responsibilities without becoming a banking Service Domain itself. Chapter 49 defines the mapping method, and Chapter 50 separates application, software-service, deployment and team boundaries.

## Rationalisation uses evidence

Rationalisation begins with responsibility and authority, not age or fashion. Review each application for:

- functional and strategic fit;
- duplicated or missing responsibility;
- data authority and interface ownership;
- control effectiveness and retained evidence;
- resilience, recoverability and third-party dependency;
- technical condition, cost and change demand;
- transition dependency and safe decommissioning.

A disposition such as invest, tolerate, migrate, replace or retire needs evidence. Retirement is complete only when data, interfaces, records, controls, operational ownership and recovery obligations have moved or ended safely.

## Common mistakes

- Drawing only web, mobile and core banking and calling it the full bank.
- Naming vendor suites while leaving logical responsibilities and owners unclear.
- Treating one database, application, software service, team and BIAN Service Domain as the same boundary.
- Calling every asynchronous message an event.
- Reversing API arrows because the user's journey begins at the consumer.
- Omitting external networks, repair work, reconciliation, security and operations.
- Treating an integration platform as the owner of business semantics.
- Mixing current and target elements without lifecycle markers.
- Retiring a system without migrating its records, interfaces and control evidence.

## Chapter summary

Horizon Bank's application architecture is a governed estate of 90 logical responsibilities connected by 106 typed interfaces and 17 logical external-network classes. The model covers customer interaction, products, transactions, finance, risk, control, data, integration, security and operations. Its purpose is not to prescribe ninety products. It preserves responsibilities and relationships so detailed domain, information, deployment and migration decisions can be made without losing enterprise coherence.

## Completion checklist

- [x] All 90 governed logical applications are represented in the portfolio index.
- [x] All seven governed interface types and their catalogue counts are explained.
- [x] All 17 external-network classes are represented without fabricated providers or memberships.
- [x] Authority, orchestration, processing, insight and platform roles are distinguished.
- [x] Onboarding and cross-border-payment traces use exact governed IDs.
- [x] Current and target states, rationalisation and operational dependencies are covered.
- [x] BIAN is not treated as an application or microservice decomposition.
- [x] Diagram production is explicitly deferred under the specification-first workflow.

## Key takeaways

- A full-bank landscape includes control, finance, data, integration, security and operations, not only channels and product processors.
- A logical application is a responsibility boundary, not automatically a package, deployable service or team.
- Interface style follows business timing, ownership, failure and evidence needs.
- External connectivity must be governed even when the provider or membership is still unknown.
- Current-to-target change needs coexistence, authority and exit decisions.

## Practical exercise

Trace a card purchase from `HB-APP-002 Retail Mobile Banking` and `HB-APP-040 Card Issuing Management` through authorisation, fraud, processing, the card network, clearing, dispute and finance responsibilities. Use at least six `HB-APP-*`, four `HB-INT-*` and one `HB-EXT-*` identifier. For each interaction, state whether the producer provides an API or emits a message, command, event, file or workflow hand-off. Then identify one authority question and one degraded-mode question.

## Review checklist

- [ ] Does the landscape state whether it is logical, physical, current, transition or target?
- [ ] Are application responsibilities and service owners explicit?
- [ ] Are record authority and working copies qualified by information and lifecycle?
- [ ] Are interface type, direction, security classification and failure ownership visible?
- [ ] Are external networks and third-party dependencies included without unsupported claims?
- [ ] Are finance, reconciliation, data, security and operations present?
- [ ] Can a reader trace from an enterprise family to a domain chapter?
- [ ] Are BIAN, application, software-service, deployment and team boundaries kept separate?

## References and further reading

- [BCBS-OPERATIONAL-RESILIENCE-2021](../../research/banking/bcbs-operational-resilience-2021.md)
- [BIAN-SERVICE-LANDSCAPE-14](../../research/bian/bian-service-landscape-14.0.md)

## Drafting notes

- `FIG-34-01` remains `Planned`; no diagram source has been created.
- Enterprise-support logical applications and physical deployment relationships remain governed gaps, not implied coverage.
