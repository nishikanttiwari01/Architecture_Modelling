---
title: "BIAN Essentials and the Case-Study Method"
chapter: 31
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 31. BIAN Essentials and the Case-Study Method

## Chapter purpose

Introduce the Banking Industry Architecture Network (BIAN) concepts needed in Part V and explain how Horizon Bank will combine them with business, application, data and technology models.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- explain why BIAN provides a banking reference architecture;
- distinguish Service Landscape, Business Area, Business Domain, Service Domain, Business Scenario and Service Operation;
- explain why a Service Domain is not automatically a microservice, application or team;
- combine BIAN with ArchiMate, Business Process Model and Notation (BPMN), C4, Unified Modeling Language (UML), Decision Model and Notation (DMN) and data models;
- assess a proposed Horizon Bank mapping by evidence, status and confidence.

## Prerequisites and dependencies

- Chapter 30: Change and Migration
- Chapters 4 to 10 for the modelling languages used in the case study

## Required models and artefacts

- BIAN 14.0 source notes
- the governed Horizon Bank catalogues
- the candidate BIAN mapping register
- the `FIG-31-01` specification

## Worked examples

- Horizon Bank payment-initiation traceability thread

## Source requirements

Every exact BIAN object must be verified against official BIAN 14.0 material. The mapping record must preserve the source, version, rationale, record status, confidence and verification status. BIAN statements in this chapter use the official Service Landscape page, BIAN 14.0 release material and the current BIAN repository. [BIAN-SERVICE-LANDSCAPE-14] [BIAN-14-CORE-CONCEPTS-PV31]

## Planned chapter structure

The chapter first explains the reference architecture, then separates it from Horizon Bank's bank-owned model, and finally applies a repeatable traceability method.

## The problem is shared meaning, not a shortage of diagrams

Two teams can both draw a box called `Payment Service` while meaning different things. One may mean customer instruction capture, another clearing connectivity, and a third the application that performs both. The apparent agreement disappears when they discuss ownership, information or failure handling.

BIAN helps architects ask a more stable question: **which recognisable banking responsibility is involved, and which industry reference concept can help describe it?** A versioned reference vocabulary makes comparison easier. It does not decide how Horizon Bank should organise people, purchase software or deploy technology.

This distinction is the foundation of Part V. The bank model starts with customer and stakeholder outcomes, then connects value streams, capabilities, processes, organisation, information, applications, interactions, controls and operations. BIAN is one reference within that connected model.

## What BIAN is

The Banking Industry Architecture Network is an industry association that publishes a banking reference architecture and semantic assets. The **Service Landscape** organises a peer set of **Service Domains** for navigation. Official BIAN material also covers Business Scenarios, Service Operations, semantic application programming interfaces (APIs), events and information concepts. [BIAN-SERVICE-LANDSCAPE-14] [BIAN-14-CORE-CONCEPTS-PV31]

The current case-study baseline is BIAN Service Landscape 14.0, published in February 2026. The release rationalised definitions, removed unnecessary Service Operations, increased links to ISO 20022 and changed some Service Domains, particularly in payments. Exact names from older versions cannot be carried forward without checking them. [BIAN-SERVICE-LANDSCAPE-14]

BIAN is useful because it provides:

- an industry reference set of banking responsibilities;
- a way to compare local responsibility boundaries;
- semantic material for analysing information exchanges;
- example collaborations through Business Scenarios;
- a common starting vocabulary across banks and suppliers.

It is not a complete enterprise design. It does not supply Horizon Bank's legal entities, product catalogue, organisation chart, application inventory, deployment topology, controls, recovery design or migration roadmap.

## The core concepts and the questions they answer

| BIAN concept | Plain-language purpose | Question it helps answer | What it does not decide |
|---|---|---|---|
| Service Landscape | Navigates the reference set | Where can a related responsibility be found? | Horizon Bank's organisation or application layers |
| Business Area | Groups parts of the landscape | Which broad region of the reference set is relevant? | A business line or legal entity |
| Business Domain | Groups related Service Domains | Which related responsibilities can be considered together? | A Horizon Bank domain, team or bounded context |
| Service Domain | Defines a discrete logical banking responsibility | What coherent banking responsibility is being performed? | A deployable service, application or team |
| Business Scenario | Illustrates collaboration for a business outcome | Which responsibilities may interact for this outcome? | The bank's complete process and exception design |
| Service Operation | Describes an offered interaction | What behaviour can another responsibility request or use? | Protocol, runtime topology or production service level |
| Control Record | Organises information used to govern a responsibility instance | What information tracks the responsibility's lifecycle? | One database record or physical schema |
| Business Object Model | Provides semantic reference concepts | What shared business meaning can inform a mapping? | Horizon Bank's complete logical or physical data model |

The word `domain` occurs in both BIAN and Horizon Bank catalogues. It does not mean the records are interchangeable. `HB-DOM-050 Payments` is a bank-owned business domain used to organise local accountabilities. A BIAN Business Domain is part of BIAN's reference classification. Their relationship must be recorded as a mapping, never inferred from similar names.

## A Service Domain is a logical responsibility

A BIAN Service Domain identifies a discrete business function or purpose within the BIAN peer set. It can involve people, procedures and systems. It is therefore more useful to read a Service Domain as a **logical responsibility boundary** than as a software prescription. [BIAN-14-CORE-CONCEPTS-PV31]

One Horizon Bank application may realise parts of several candidate Service Domains. For example, `HB-APP-034 Payment Orchestration` coordinates entitlement, screening, funds control, routing, posting and status. Those responsibilities are wider than one unverified BIAN name. Conversely, one candidate BIAN responsibility may be supported by a channel, a processor, an operations team, a control application and several interfaces.

The relationship is normally many-to-many:

```text
BIAN responsibility candidates
        many ↕ many
bank capabilities and processes
        many ↕ many
logical applications and people
        many ↕ many
software services and deployments
```

An architect may eventually choose a one-to-one boundary, but only after assessing cohesion, information authority, transaction integrity, security, scale, change cadence, supplier constraints and operating ownership. Name matching is not sufficient evidence.

## Business Scenarios show collaboration, not the complete process

A BIAN Business Scenario presents an archetypal interaction between responsibilities for a bounded business outcome. It is useful for discovering dependencies and discussing semantics. It should not be treated as a mandatory process sequence or an exhaustive description of every exception.

Horizon Bank's scenario catalogue serves a different purpose. Records such as `HB-SCN-02 Execute Cross-Border Payment` and `HB-SCN-19 Recover Payment Service after Cyber Disruption` are bank-owned traceability threads. They connect local products, processes, applications, information, interfaces, controls and critical operations. A Horizon Bank scenario can reference a BIAN scenario or candidate Service Domains, but it is not automatically a BIAN Business Scenario.

Use BPMN when the question concerns tasks, events, messages, gateways, timers, hand-offs and repair paths. Use a BIAN-style responsibility interaction when the question concerns which logical banking responsibilities collaborate. A serious design may need both views.

## Service Operations, semantic APIs and events

Service Operations describe interactions associated with a Service Domain. BIAN semantic API material can help architects analyse the business meaning of those interactions. It does not remove implementation work.

For each Horizon Bank API, command, event, message, batch, file or workflow exchange, the interface catalogue records the producer, consumer, information, security classification and lifecycle state. The design must still define:

- authentication and authorisation;
- request, response or message schema;
- validation and business rejection;
- timeout, retry and idempotency behaviour;
- ordering, duplication and replay where relevant;
- confidentiality, retention and audit evidence;
- operational ownership and service expectations.

`HB-INT-036 Accepted Payment Command`, for example, is a directed request from payment initiation to orchestration. `HB-INT-066 Intraday Settlement Position Event` announces a completed or observed fact. Similar business words do not make a command and an event equivalent.

## Control Records and bank-owned information

BIAN's Control Record concept organises the business information associated with fulfilling a Service Domain responsibility. It helps an analyst ask which state, identifiers, terms, activity and evidence matter through a lifecycle. It does not instruct Horizon Bank to create one table called `ControlRecord`.

Horizon Bank retains its own information governance. `HB-DATA-08 Payments, Clearing and Settlement` groups payment information. `HB-SOR-08 Payment Instruction and Processing Authority` identifies qualified authority for the payment instruction and processing lifecycle. `HB-SOR-09 Settlement and Correspondent Position Authority` identifies a different authority boundary. Chapter 35 develops these distinctions.

A BIAN Business Object Model concept may inform a semantic mapping, but Horizon Bank must still govern local identifiers, cardinalities, privacy classification, temporal history, lineage, retention and physical storage.

## BIAN works with other modelling techniques

Each technique in Part V answers a different question.

| Technique | Main question | Use with BIAN | Misuse to avoid |
|---|---|---|---|
| ArchiMate | How do strategy, business, application and technology elements relate? | Place candidate responsibilities in enterprise views | Treating every BIAN element as an ArchiMate application service |
| BPMN | How does work proceed, including exceptions? | Detail behaviour across responsibilities | Copying a scenario as a mandatory process |
| C4 | How is software structured and deployed? | Show the software that realises mapped responsibilities | Renaming Service Domains as C4 containers |
| UML | How do components, interactions, states or data structures behave? | Add selected design precision | Mixing every abstraction on one diagram |
| DMN | How is repeatable decision logic derived? | Make policy decisions explicit within a responsibility | Treating a decision result as the following process |
| Data models | What information exists, relates and is authoritative? | Map reference semantics to bank-owned concepts | Using a reference object model as a physical schema |
| Interface catalogue | Which systems exchange what, how and under whose ownership? | Record implementation-facing semantic alignment | Calling a similar API operation BIAN-conformant without evidence |

BIAN adds industry semantics to this model set. It does not replace the model set.

## The governed Horizon Bank case-study baseline

Horizon Bank is a fictional full-service banking group. Its catalogues are author models with stable identifiers. They cover business lines, segments, products, value streams, business domains, capabilities, processes, organisation, applications, information, accounting, controls, resilience and scenarios.

The baseline includes:

- four business lines: `HB-BL-01 Retail Banking`, `HB-BL-02 Business and Corporate Banking`, `HB-BL-03 Wealth and Securities` and `HB-BL-04 Treasury and Markets`;
- five customer segments: `HB-SEG-01 Retail`, `HB-SEG-02 SME` (small and medium-sized enterprise), `HB-SEG-03 Commercial and Corporate`, `HB-SEG-04 Private Banking` and `HB-SEG-05 Institutional`;
- product families and products, including `HB-PRD-01 Deposits and Accounts`, `HB-PRD-04 Credit`, `HB-PRD-07 Payment and Cash Management`, `HB-PRD-09 Trade Finance` and `HB-PRD-10 Investment, Advisory and Custody`;
- ten value streams, including the distinct deposit, credit, transaction, asset-service and trade-finance lifecycles;
- a hierarchical business-domain and capability catalogue;
- 90 logical applications and 106 governed interfaces;
- systems of record, accounting events, reconciliations, controls, critical operations and 20 integrated scenarios.

These counts describe the current teaching baseline, not a recommended size for a real bank. The stable IDs matter more than the counts because they permit validation and impact analysis.

The candidate BIAN register deliberately contains only four unverified records: `HB-BIAN-01 Deposit Responsibility Candidate`, `HB-BIAN-02 Payment Responsibility Candidate`, `HB-BIAN-03 Credit Responsibility Candidate` and `HB-BIAN-04 Trade Finance Responsibility Candidate`. This is honest incompleteness. Later chapters must not invent exact BIAN objects to make the matrix look finished.

## The Part V method

The case study applies the following method.

### 1. State the outcome and scope

Name the stakeholder outcome, customer segment, product, legal entity, jurisdiction and architecture state. A payment for a retail customer is not automatically the same scope as a corporate bulk-payment file.

### 2. Find the bank-owned business responsibility

Select governed value streams, business domains, capabilities and processes. Do this before searching BIAN names. The bank must understand its own responsibility before comparing it with a reference.

### 3. Trace information and control

Identify the data domain, qualified system of record, decision, accounting event, reconciliation and control. This reveals responsibilities that a customer-journey view may omit.

### 4. Trace application and interaction responsibilities

Identify channels, orchestrators, processors, control systems, finance systems, integration platforms and external networks. Use explicit interface IDs rather than an unlabelled `integrates with` arrow.

### 5. Assess BIAN candidates

Compare the local responsibility with the versioned BIAN definition. Record the type of relationship and why it is useful. Record overlaps, exclusions and uncertainty.

### 6. Design physical boundaries separately

Use C4, UML and deployment views to decide software-service, data and runtime boundaries. Preserve the evidence for any decision to combine or split responsibilities.

### 7. Test scenarios and exceptions

Exercise the model with normal flow, rejection, timeout, duplicate, manual repair, degraded service and recovery. A responsibility map that supports only the happy path is incomplete.

### 8. Validate and govern

Run catalogue validation, review the semantics with business and technical owners, and version the decision. A syntactically valid mapping can still be semantically wrong.

## Worked traceability: payment initiation

Consider a retail customer submitting an outgoing payment in `HB-APP-002 Retail Mobile Banking`.

| View | Governed element | Why it belongs in the trace |
|---|---|---|
| Stakeholder outcome | Access and move funds safely | States the customer's intended result |
| Product | `HB-PRD-07 Payment and Cash Management` | Identifies the commercial service family |
| Value stream | `HB-VS-04 Execute and Settle Transaction` | Follows value from valid instruction to settled, posted communication |
| Business domain | `HB-DOM-051 Payment Initiation and Execution` | Locates local responsibility |
| Capability | `HB-CAP-051 Payment Initiation` | States the ability used |
| Process | `HB-PROC-120 Initiate, Validate and Route a Payment` | Describes the ordered business work |
| Channel | `HB-APP-002 Retail Mobile Banking` | Captures customer interaction |
| Initiation responsibility | `HB-APP-033 Payment Initiation Service` | Validates and records the instruction before execution |
| Orchestration responsibility | `HB-APP-034 Payment Orchestration` | Coordinates entitlement, screening, funds control and routing |
| Interactions | `HB-INT-023 Retail Payment Initiation`; `HB-INT-026 Transaction Sanctions Screening`; `HB-INT-027 Funds and Account Control`; `HB-INT-036 Accepted Payment Command` | Makes each dependency and interaction style reviewable |
| Information | `HB-DATA-08 Payments, Clearing and Settlement`; `HB-SOR-08 Payment Instruction and Processing Authority` | Qualifies the information and authority scope |
| Control | `HB-CTRL-14 Payment Instruction, Entitlement and Funds Validation`; `HB-CTRL-15 Payment Duplicate and Idempotency Control` | Identifies preventive and processing controls |
| Critical operation | `HB-CRIT-02 Make a Time-Critical Payment` | Connects the flow to operational resilience |
| BIAN candidate | `HB-BIAN-02 Payment Responsibility Candidate` | Records that exact 14.0 objects and rationale remain unverified |

The trace does not claim that `HB-BIAN-02` equals `HB-APP-033` or `HB-APP-034`. It identifies where reference assessment is still required. Clearing, settlement, accounting, reconciliation and customer communication extend the trace beyond initiation and are developed in Chapters 41 and 49.

## Evidence, status and confidence

The BIAN register separates three questions that are often collapsed:

- **Source type:** Is the record based on an official source, an author model or a derivation?
- **Verification status:** Has the asserted reference been checked against its governed source?
- **Confidence:** How closely and unambiguously does the candidate align with the local responsibility?

Record status is separate again. `Proposed` means the mapping awaits governance. `Active` would mean the record is governed and in use. Verification does not automatically make a mapping active, and high confidence does not remove the need for review.

A useful mapping record includes:

- local element ID and exact name;
- BIAN object type, exact name and version;
- relationship type;
- local scope and exclusions;
- rationale and official evidence;
- record status, verification status and confidence;
- owner, reviewer and review date;
- unresolved questions and superseded mappings.

## When to use BIAN

Use BIAN when an architecture question benefits from banking-specific responsibility or semantic comparison. Examples include assessing overlapping product processors, aligning acquisition teams after a merger, reviewing payment responsibility coverage, shaping an API vocabulary or discussing supplier capability.

Do not start with BIAN when the immediate question is screen layout, detailed database indexing, infrastructure capacity or a jurisdiction-specific legal rule. Use the model suited to that concern, then trace it to the broader responsibility where useful.

BIAN is also a poor substitute for discovery. If nobody can explain the local outcome, owner, data authority or exception path, attaching a Service Domain name does not solve the problem.

## Common mistakes

- Starting with Service Domain names before understanding the customer or business outcome.
- Treating the Service Landscape as Horizon Bank's organisation chart.
- Treating one Service Domain as one application, microservice, bounded context or team.
- Treating a Business Scenario as a complete executable BPMN process.
- Calling a local API BIAN-aligned because an operation name looks similar.
- Implementing Control Record or Business Object Model structures as physical schemas without local data design.
- Omitting the BIAN version, source, rationale or scope exclusions.
- Marking a mapping verified when only the spelling of its name was checked.
- Hiding uncertainty by inventing an exact Service Domain name.

## Chapter summary

BIAN contributes a versioned banking responsibility and semantic reference. Horizon Bank contributes the operating model, catalogue, controls and implementation. The case-study method connects them through qualified, evidence-backed relationships and then uses complementary models to answer process, software, data, decision and deployment questions.

## Completion checklist

- [x] BIAN's role and limits are explained.
- [x] Core BIAN concepts are separated from bank-owned concepts.
- [x] The many-to-many implementation principle is explicit.
- [x] The case-study method uses governed Horizon Bank IDs.
- [x] Unverified BIAN candidates remain visibly unverified.
- [ ] `FIG-31-01` source remains deferred until its specification is author-approved.

## Key takeaways

- BIAN is a reference architecture and semantic standard, not a deployable banking product.
- Service Domains describe logical banking responsibilities, not compulsory software or team boundaries.
- Business Scenarios illustrate collaboration; process and implementation models add necessary detail.
- Horizon Bank owns its products, controls, information authority, applications and operating decisions.
- A useful mapping records source, version, relationship, rationale, status, confidence and verification.

## Practical exercise

Extend the payment-initiation trace to clearing and settlement. Use `HB-CAP-053 Payment Clearing`, `HB-CAP-054 Payment Settlement`, `HB-APP-035 Payment Routing and Clearing`, `HB-APP-036 Settlement and Nostro Management`, `HB-INT-037 Payment Clearing Instruction`, `HB-ACC-14 Payment Settlement Recognised` and `HB-REC-014 Settlement Account and Payment Ledger`.

For every arrow, write one relationship phrase such as `uses`, `produces`, `is controlled by` or `is a candidate mapping to`. Identify which relationship still requires official BIAN verification.

## Review checklist

- [ ] Does every exact BIAN object have a BIAN 14.0 source?
- [ ] Are BIAN facts separated from Horizon Bank author-model decisions?
- [ ] Are logical responsibility and physical implementation shown as separate questions?
- [ ] Does every mapping include rationale, status, confidence and verification status?
- [ ] Does the example include process, information, control and operation as well as applications?
- [ ] Are uncertainty and gaps visible rather than replaced with invented precision?

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14]
- [BIAN-14-CORE-CONCEPTS-PV31]

## Drafting notes

- The prose is catalogue-backed. Exact Horizon Bank Service Domain mappings remain intentionally pending in `bian-mapping-register.md` and must be completed through the Chapter 49 governance method.
- `FIG-31-01` is registered and specified, but no diagram source may be created before author approval.
