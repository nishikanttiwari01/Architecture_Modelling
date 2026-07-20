---
title: "Enterprise Business Architecture of Horizon Bank"
chapter: 33
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 33. Enterprise Business Architecture of Horizon Bank

## Chapter purpose

Establish the governed business architecture baseline that later domain chapters will refine.

The Banking Industry Architecture Network (BIAN) provides the industry reference used for qualified mappings in this chapter.

## Reader outcomes

By the end of this chapter, the reader should be able to distinguish stakeholder outcomes, value streams, capabilities, processes, products and organisation; navigate Horizon Bank's business coverage; and explain how ownership and candidate BIAN mappings are recorded.

## Prerequisites and dependencies

- Chapter 32: How a Full-Service Bank Works

## Required models and artefacts

- controlled business-line, segment, product and value-stream catalogues
- hierarchical business-domain, capability, process and organisation catalogues
- ownership and candidate BIAN mapping records
- the `FIG-33-01` specification

## Worked examples

- Horizon Bank customer-management architecture thread
- Horizon Bank transaction-execution architecture thread

## Source requirements

Official business-architecture guidance supports the use of capability and value-stream views. BIAN 14.0 supplies a separate banking reference architecture. Horizon Bank's taxonomy, identifiers, boundaries and ownership choices are fictional author models. [OPEN-GROUP-BIZARCH-GUIDES-2022] [BIAN-SERVICE-LANDSCAPE-14]

## Planned chapter structure

The chapter establishes modelling distinctions, introduces the governed portfolio, explains how to navigate it and demonstrates two cross-catalogue traces.

## Enterprise business architecture is a connected model

An enterprise business architecture explains what outcomes matter, what value the organisation delivers, what abilities it needs, how work proceeds, what it offers and who is accountable. Its purpose is not to make one large organisation chart.

The central question is: **how does Horizon Bank organise responsibility to deliver controlled customer, financial and regulatory outcomes across the whole group?** The answer requires several related model types because no single hierarchy can represent value, ability, sequence, commercial terms and accountability accurately.

Horizon Bank stores those types in governed catalogues. Stable identifiers connect them without pretending they are equivalent. The catalogues are the source of truth; tables in this chapter are navigation views over them.

## Keep the business concepts separate

| Concept | Plain-language meaning | Question answered | Example |
|---|---|---|---|
| Stakeholder outcome | A result that matters to a person or organisation | Why does this architecture matter? | A customer can move eligible funds safely and understand the result |
| Value stream | Progression of value towards an outcome | How does value move from trigger to outcome? | `HB-VS-04 Execute and Settle Transaction` |
| Business domain | A coherent area of business responsibility and knowledge | Where does this responsibility belong in the bank model? | `HB-DOM-050 Payments` |
| Capability | An ability the bank needs | What must the bank be able to do? | `HB-CAP-054 Payment Settlement` |
| Process | Ordered work triggered to produce an outcome | How does the work proceed? | `HB-PROC-121 Clear, Settle and Manage Correspondent Payments` |
| Product | A governed commercial proposition or service family | What does the bank offer under defined terms? | `HB-PRD-07 Payment and Cash Management` |
| Organisation | An accountable or performing structure or role | Who owns, decides or performs? | `HB-ORG-111 Payments Director Role` |
| BIAN mapping | A qualified link to a versioned industry reference | Which reference responsibility may help compare this local element? | `HB-BIAN-02 Payment Responsibility Candidate` |

A capability is not a department. A process is not a value stream. A product is not its processor. An organisation unit is not automatically a software boundary. A BIAN Service Domain is not any of these local elements.

The Open Group's public business-architecture guidance treats capabilities and value streams as related business-architecture elements and supports mapping them to other viewpoints. Horizon Bank follows that principle, while its exact taxonomy remains an author model. [OPEN-GROUP-BIZARCH-GUIDES-2022]

## Stakeholder outcomes provide direction

The business architecture begins with outcomes rather than catalogue completeness. Horizon Bank considers at least six stakeholder perspectives:

| Stakeholder | Illustrative desired outcome | Architecture evidence needed |
|---|---|---|
| Customer | Receive suitable, reliable and understandable financial service | Journey, agreement, transaction status, communication, complaint and redress evidence |
| Business customer | Control cash, financing and risk across authorised users and entities | Party structure, mandate, entitlement, product, limit, position and channel models |
| Board and shareholders | Operate a sustainable, controlled and transparent banking group | Strategy, risk, finance, control, assurance and performance traceability |
| Regulator and central bank | Receive reliable evidence about obligations, positions and risk | Legal-entity scope, lineage, reconciliation, approval and submission records |
| Employee | Perform accountable work using appropriate information and tools | Role, work queue, decision authority, access and service-ownership models |
| Market or payment participant | Exchange obligations accurately and on time | Interface, external-network, clearing, settlement, liquidity and repair models |

These outcomes are teaching assumptions, not controlled catalogue IDs or legal definitions. They should be linked to governed elements in a motivation or traceability view, not inserted into relationship fields as uncontrolled identifiers.

## The value-stream portfolio

Horizon Bank defines ten enterprise value streams.

| ID | Value stream | Trigger | Outcome and boundary |
|---|---|---|---|
| `HB-VS-01` | Establish and Manage Relationship | Customer or bank interest | Relationship established, serviced or exited |
| `HB-VS-02` | Design and Manage Product | Identified need | Product launched, changed and retired |
| `HB-VS-03` | Acquire and Service Deposit or Account | Deposit or non-credit account need | Account agreement serviced and closed |
| `HB-VS-04` | Execute and Settle Transaction | Valid instruction or event | Transaction settled, posted and communicated |
| `HB-VS-05` | Provide and Manage Credit | Financing need | Exposure repaid, restructured or recovered |
| `HB-VS-06` | Safeguard and Service Assets | Asset received or acquired | Asset serviced, transferred or returned |
| `HB-VS-07` | Manage Financial Position | Position or forecast change | Funding, liquidity, market, asset-liability and capital position remains within governed decisions |
| `HB-VS-08` | Resolve Exception | Alert, failure, dispute or complaint | Case resolved with evidence |
| `HB-VS-09` | Record, Reconcile and Report | Business or accounting event | Approved report and retained evidence |
| `HB-VS-10` | Provide and Manage Trade Finance | Product or instrument request | Instrument issued, serviced, settled and closed with contingent exposure resolved |

The boundaries are deliberate. Deposit acquisition and servicing remain in `HB-VS-03`; the complete credit lifecycle remains in `HB-VS-05`. Trade finance has its own lifecycle because issuance, amendment, documentary handling, discrepancies, contingent exposure, claims, settlement and closure cannot be represented accurately as deposit acquisition. Its transaction consequences can also participate in `HB-VS-04`.

`HB-VS-08 Resolve Exception` and `HB-VS-09 Record, Reconcile and Report` are cross-cutting streams. They do not remove exception and accounting responsibilities from domain processes. They provide enterprise traceability across them.

## Navigate the bank through business domains

The business-domain catalogue has Level 1 domains for whole-bank navigation and Level 2 subdomains for coherent responsibility areas. A Level 2 record has one governed parent. The hierarchy is not an organisation chart or process sequence. Asset and liability management (ALM) appears in the treasury domain as a distinct balance-sheet responsibility.

| Level 1 ID | Business domain | Representative Level 2 scope |
|---|---|---|
| `HB-DOM-001` | Enterprise Direction and Governance | Strategy, corporate governance, portfolio, architecture and transformation |
| `HB-DOM-010` | Customer, Party, Sales and Service | Party, onboarding, relationship, sales, service and exit |
| `HB-DOM-020` | Product, Proposition and Pricing | Portfolio, product lifecycle, pricing, catalogue and eligibility |
| `HB-DOM-030` | Deposits and Accounts | Origination, account servicing, interest, fees, statements and term deposits |
| `HB-DOM-040` | Lending and Credit | Origination, agreements, servicing, limits, collateral, exposure and recovery |
| `HB-DOM-050` | Payments | Initiation, execution, clearing, settlement, correspondent banking, foreign exchange and investigation |
| `HB-DOM-060` | Cards and Merchant Acquiring | Issuing, processing, fraud, disputes and acquiring |
| `HB-DOM-070` | Corporate Banking, Cash Management and Trade Finance | Coverage, mandates, cash structures and trade instruments |
| `HB-DOM-080` | Wealth and Investments | Advice, suitability, portfolio, orders and client reporting |
| `HB-DOM-090` | Securities, Custody and Asset Servicing | Custody, settlement, safekeeping, corporate actions and financing |
| `HB-DOM-100` | Treasury, Markets, Funding, Liquidity, ALM and Capital | Funding, liquidity, asset and liability management, capital, markets and operations |
| `HB-DOM-110` | Finance, Accounting, Tax and Reporting | Accounting policy, ledgers, reconciliation, close, tax and reports |
| `HB-DOM-120` | Enterprise Risk | Framework, financial and non-financial risk, models and risk data |
| `HB-DOM-130` | Compliance, Financial Crime and Fraud | Obligations, customer controls, transaction monitoring, investigations and conduct |
| `HB-DOM-140` | Banking Operations and Service Management | Operational work, planning, exceptions, quality and control evidence |
| `HB-DOM-150` | Channels, Communications, Documents and Workflow | Digital and assisted channels, communications, content, workflow and cases |
| `HB-DOM-160` | Data, Analytics and Model Management | Governance, architecture, master data, quality, lineage, analytics and models |
| `HB-DOM-170` | Technology, Cyber Security and Resilience | Engineering, platforms, infrastructure, integration, cyber security and operations |
| `HB-DOM-180` | People, Suppliers and Facilities | Workforce, sourcing, suppliers, facilities and physical services |
| `HB-DOM-190` | Legal, Audit and Corporate Secretariat | Legal advice, contracts, disputes, corporate records and internal audit |

This portfolio prevents the enterprise landscape from stopping at retail products and digital channels. Finance, operations, legal, workforce, supplier and resilience responsibilities are part of a real bank architecture.

## Capabilities describe abilities

The capability catalogue uses a parallel Level 1 navigation structure, then decomposes each area into Level 2 abilities. The exact hierarchy is governed and machine validated.

For example, `HB-CAP-050 Payment Management` decomposes into:

- `HB-CAP-051 Payment Initiation`;
- `HB-CAP-052 Payment Validation and Routing`;
- `HB-CAP-053 Payment Clearing`;
- `HB-CAP-054 Payment Settlement`;
- `HB-CAP-055 Correspondent Banking`;
- `HB-CAP-056 Payment Foreign-Exchange Coordination`;
- `HB-CAP-057 Payment Investigation and Repair`;
- `HB-CAP-058 Payment Liquidity and Cut-Off Management`;
- `HB-CAP-059 Payment Status and Reporting`.

These capabilities state what the bank needs to be able to do. They do not state task order or assign one application each. `HB-CAP-054 Payment Settlement`, for example, can be used by domestic, immediate, correspondent and card-payment processes, supported by several applications and operations teams.

Capabilities are useful for strategic comparison, investment planning, gap assessment and impact analysis. They are less suitable for showing exact work sequence, interaction timing or runtime design.

## Processes describe ordered work

The process catalogue has 21 Level 1 process families and detailed Level 2 processes. It spans direction, products, customers, deposits, credit, payments, cards, corporate banking, trade, wealth, securities, treasury, finance, risk, compliance, operations, channels, data, technology, shared services and assurance.

| Process family | Representative Level 2 processes |
|---|---|
| `HB-PROC-01 Acquire and Manage Customers` | `HB-PROC-105`; `HB-PROC-106`; `HB-PROC-107`; `HB-PROC-108`, covering party records, onboarding, relationship management, service, complaints and exit |
| `HB-PROC-03 Originate and Manage Credit` | `HB-PROC-116`; `HB-PROC-117`; `HB-PROC-118`; `HB-PROC-119`, covering decision, agreement, limits, collateral, exposure and recovery |
| `HB-PROC-04 Execute and Settle Payments` | `HB-PROC-120`; `HB-PROC-121`; `HB-PROC-122`; `HB-PROC-123`, covering initiation, settlement, correspondent work, liquidity, foreign exchange and investigation |
| `HB-PROC-06 Originate and Service Trade Finance` | `HB-PROC-130` and `HB-PROC-131`, covering instrument issue, amendment, documents, discrepancy and exposure |
| `HB-PROC-17 Govern, Deliver and Operate Technology` | `HB-PROC-166`; `HB-PROC-167`; `HB-PROC-168`; `HB-PROC-169`, covering architecture, engineering, platforms, identity, cyber security, services and resilience |

A process architecture record needs a trigger, outcome, owner, participants, inputs, outputs, controls, exceptions and supporting capabilities. Use BPMN only where the audience needs task, event, gateway, message and exception detail. Enterprise process maps establish coverage; they are not readable substitutes for detailed models.

## Products connect commercial promise to fulfilment

The product catalogue uses three hierarchy fields: level, parent ID and the distinct concepts of product family, product and product variant. Horizon Bank currently models families and representative products. Variant-level country and segment definitions remain a visible gap.

The cards hierarchy illustrates why this matters:

- `HB-PRD-08 Cards and Merchant Services` is the Level 1 family;
- `HB-PRD-11 Card Issuing`, `HB-PRD-12 Merchant Acquiring` and `HB-PRD-13 Card Processing Services` are separate Level 2 products.

Issuing manages the cardholder proposition and credential lifecycle. Acquiring manages merchant agreements, acceptance and funding. Processing supports authorisation, message switching, clearing and settlement. They can share external schemes and transaction capabilities without becoming one product or owner.

Business-line relationships are explicit. `HB-BL-01 Retail Banking` includes card issuing. `HB-BL-02 Business and Corporate Banking` includes small and medium-sized enterprise (SME) and corporate credit, payments and cash management, trade finance, card issuing and merchant acquiring. `HB-BL-03 Wealth and Securities` is not assigned trade finance.

## Organisation records accountability and performance

The organisation catalogue separates structures and roles. At the top level:

- `HB-ORG-01 Group Board and Executive Governance` directs and oversees the group;
- `HB-ORG-02 Product and Business Management` owns propositions and commercial outcomes;
- `HB-ORG-03 Banking Operations and Corporate Services` performs operational and enterprise services;
- `HB-ORG-04 Risk, Compliance and Assurance` provides independent oversight;
- `HB-ORG-05 Finance and Treasury` owns financial control and position responsibilities;
- `HB-ORG-06 Technology, Data and Cyber Security` owns enabling technology, data and cyber responsibilities.

Level 2 units such as `HB-ORG-15 Banking Operations`, `HB-ORG-17 Data and Analytics` and `HB-ORG-28 Payment and Card Operations` make performance responsibilities more specific. Role records such as `HB-ORG-111 Payments Director Role` identify accountability without naming an individual.

### Ownership is multidimensional

One lifecycle can require several owners:

| Ownership concern | Accountable question | Governed role example |
|---|---|---|
| Product | Who owns the proposition, terms and lifecycle? | `HB-ORG-121 Product Owner Role` |
| Process | Who owns end-to-end definition, control and improvement? | `HB-ORG-120 Business Process Owner Role` |
| Data | Who owns meaning, use, quality and authority decisions? | `HB-ORG-122 Data Owner Role` |
| Application service | Who owns service health, lifecycle and operational outcomes? | `HB-ORG-123 Application Service Owner Role` |
| Control | Who owns design, operation, evidence and remediation? | `HB-ORG-124 Control Owner Role` |

One person may hold several responsibilities, but the model should not collapse them into a generic `Owner` where the distinction matters. Chapter 54 develops governance and decision rights.

## Candidate BIAN mappings remain qualified references

The local business model comes first. A candidate BIAN mapping is then attached to a defined local responsibility, with a source, rationale, status, confidence and verification status.

The current register contains four unverified candidates:

| Candidate | Local scope | Governed gap |
|---|---|---|
| `HB-BIAN-01 Deposit Responsibility Candidate` | `HB-PRD-01`; `HB-VS-03` | Exact BIAN 14.0 object and confidence pending |
| `HB-BIAN-02 Payment Responsibility Candidate` | `HB-PRD-07`; `HB-VS-04` | Exact BIAN 14.0 objects and many-to-many rationale pending |
| `HB-BIAN-03 Credit Responsibility Candidate` | `HB-PRD-04`; `HB-VS-05` | Exact BIAN 14.0 objects and confidence pending |
| `HB-BIAN-04 Trade Finance Responsibility Candidate` | `HB-PRD-09`; `HB-VS-10`; `HB-PROC-06` | Exact BIAN 14.0 objects and confidence pending |

No candidate replaces a capability or process owner. No candidate proves an application boundary. Chapter 49 gives the full mapping method.

## Worked thread 1: establish and manage a customer relationship

The customer-management thread starts with the outcome that an eligible person or organisation establishes a serviceable relationship with the correct legal entity.

| View | Governed elements | Meaning |
|---|---|---|
| Segment | `HB-SEG-01 Retail` | Establishes the illustrative customer context |
| Value stream | `HB-VS-01 Establish and Manage Relationship` | Follows relationship establishment, service and exit |
| Business domains | `HB-DOM-011 Party and Customer Management`; `HB-DOM-012 Customer Acquisition and Onboarding`; `HB-DOM-014 Customer Servicing and Exit` | Separates identity, onboarding and continuing service responsibilities |
| Capabilities | `HB-CAP-011 Party Identity Management`; `HB-CAP-013 Customer Onboarding`; `HB-CAP-014 Customer Due-Diligence Coordination`; `HB-CAP-018 Customer Servicing` | States the required abilities |
| Processes | `HB-PROC-105 Establish and Maintain Party and Customer Records`; `HB-PROC-106 Onboard a Customer`; `HB-PROC-108 Service, Resolve Complaints and Exit Customers` | Describes ordered work across the lifecycle |
| Organisation | `HB-ORG-07 Customer, Sales, Channels and Service`; `HB-ORG-14 Compliance, Financial Crime and Conduct`; `HB-ORG-15 Banking Operations` | Assigns commercial, oversight and fulfilment responsibilities |
| Scenario | `HB-SCN-01 Establish Retail Customer Relationship` | Provides the integrated trace used in Chapter 37 |

The capability `Customer Onboarding` does not imply that one team or application owns party authority, screening and product fulfilment. Later application, data and control views refine the same stable IDs.

## Worked thread 2: execute and settle a transaction

The transaction thread starts with a valid instruction or event and ends when the transaction is settled, posted and communicated, or has entered a governed repair path.

| View | Governed elements | Meaning |
|---|---|---|
| Product | `HB-PRD-07 Payment and Cash Management` | Identifies the service family |
| Value streams | `HB-VS-04 Execute and Settle Transaction`; `HB-VS-08 Resolve Exception`; `HB-VS-09 Record, Reconcile and Report` | Covers primary value, repair and financial evidence |
| Business domains | `HB-DOM-051 Payment Initiation and Execution`; `HB-DOM-052 Clearing, Settlement and Correspondent Banking`; `HB-DOM-054 Payment Investigations and Reporting` | Separates coherent responsibility areas |
| Capabilities | `HB-CAP-051 Payment Initiation`; `HB-CAP-053 Payment Clearing`; `HB-CAP-054 Payment Settlement`; `HB-CAP-057 Payment Investigation and Repair` | States the abilities involved |
| Processes | `HB-PROC-120 Initiate, Validate and Route a Payment`; `HB-PROC-121 Clear, Settle and Manage Correspondent Payments`; `HB-PROC-123 Investigate, Repair and Report Payments` | Describes the main work and exception path |
| Organisation | `HB-ORG-111 Payments Director Role`; `HB-ORG-28 Payment and Card Operations`; `HB-ORG-12 Finance, Accounting, Tax and Reporting` | Assigns business, operations and financial-control responsibility |
| BIAN candidate | `HB-BIAN-02 Payment Responsibility Candidate` | Records an unverified industry-reference mapping, not an implementation boundary |
| Scenario | `HB-SCN-02 Execute Cross-Border Payment` | Carries the thread into Chapters 41, 49 and 56 |

This view already exposes more than a `Payments` department box. It still does not show applications, information, interfaces, controls or deployment. Chapters 34 to 36 connect those layers.

## Heat maps, measures and evidence

A capability heat map can compare business importance, current effectiveness, risk or change urgency. It is a decision aid, not an objective fact. Every rating needs a scale definition, date, owner, evidence and comment. Colour must not be the only carrier of meaning.

Business-architecture measures can include completion, failure and repair rates, time to decision, manual intervention, reconciliation breaks, complaints and control exceptions. A useful measure states its population, formula, source, owner, frequency and decision use. An attractive dashboard with ambiguous denominators is not governance evidence.

The current catalogues record gaps instead of invented scores. Country variants, product variants, decision authorities and exact BIAN mappings remain open where evidence is not ready.

## When to use each business view

Use an outcome map when agreement on purpose is missing. Use a value stream when the discussion concerns value progression across functions. Use a capability map for stable ability coverage and investment questions. Use a process model for sequence, hand-offs and exceptions. Use a product model for propositions, terms and lifecycle. Use an organisation model for accountability and performance.

Do not use a capability map to prescribe task order. Do not use a process map as the organisation chart. Do not use a value stream as a system interaction diagram. Connect focused views through identifiers rather than combining them into one unreadable model.

## Common mistakes

- Calling a department, process step, application or project a capability.
- Treating value-stream stages as detailed process tasks.
- Using unprefixed or abbreviated IDs that cannot be validated.
- Maintaining a presentation list that competes with the governed catalogue.
- Omitting finance, operations, data, legal, supplier and resilience domains from the `whole bank` view.
- Assigning a capability or process to one application by default.
- Recording one generic owner where product, process, data, service and control accountabilities differ.
- Adding maturity colours without evidence, scale, date and owner.
- Mapping a similar BIAN name before defining the local responsibility.

## Chapter summary

Horizon Bank's enterprise business architecture is a set of connected, governed viewpoints. Ten value streams describe value progression. Hierarchical domains and capabilities establish whole-bank coverage. Processes describe work, products describe commercial offers, and organisation records accountability. Candidate BIAN mappings remain qualified references.

## Completion checklist

- [x] Stakeholder outcomes, value streams, domains, capabilities, processes, products and organisation are distinguished.
- [x] The whole-bank domain portfolio is represented with governed IDs.
- [x] Product hierarchy and cards boundary decisions are explicit.
- [x] Process and capability hierarchies use the controlled catalogues.
- [x] Ownership types and candidate BIAN status are explicit.
- [x] Customer and transaction threads are catalogue-backed.
- [ ] `FIG-33-01` source remains deferred until its specification is author-approved.

## Key takeaways

- Enterprise business architecture uses several connected models because value, ability, sequence, product and ownership are different concerns.
- Stable IDs let focused views remain consistent without collapsing their meanings.
- Whole-bank coverage includes finance, risk, operations and shared enterprise responsibilities as well as products and channels.
- Ownership is multidimensional and belongs in the architecture model.
- BIAN mappings are versioned, evidence-backed references, not automatic local boundaries.

## Practical exercise

Build a trace for `HB-VS-10 Provide and Manage Trade Finance`. Include `HB-PRD-09 Trade Finance`, `HB-DOM-073 Trade Finance Origination and Instruments`, `HB-DOM-074 Trade Documents, Exposure and Settlement`, `HB-CAP-076 Trade Instrument Issuance and Amendment`, `HB-CAP-077 Trade Document and Discrepancy Management`, `HB-PROC-130 Originate, Issue and Amend Trade Instruments`, `HB-PROC-131 Examine Trade Documents and Resolve Exposure`, `HB-ORG-113 Trade Finance Director Role` and `HB-BIAN-04 Trade Finance Responsibility Candidate`.

For every connection, write the relationship in words. Explain why `HB-VS-04 Execute and Settle Transaction` contributes to the lifecycle without replacing `HB-VS-10`.

## Review checklist

- [ ] Does each model state the question it answers?
- [ ] Are all Horizon Bank IDs complete, governed and machine checkable?
- [ ] Are value streams, capabilities, processes, products and organisation kept distinct?
- [ ] Does the coverage include customer, product, transaction, finance, risk, operations and shared enterprise domains?
- [ ] Are parent-child and contributing relationships distinguished?
- [ ] Are all owners qualified by responsibility type?
- [ ] Are BIAN mappings versioned and visibly unverified where evidence is pending?
- [ ] Are scores and measures supported by definitions and evidence?

## References and further reading

- [OPEN-GROUP-BIZARCH-GUIDES-2022]
- [BIAN-SERVICE-LANDSCAPE-14]

## Drafting notes

- The business-domain, capability, process, product and organisation catalogues now provide the governed baseline required by this chapter. Exact BIAN mappings and country-specific product variants remain explicit gaps.
- `FIG-33-01` is registered and specified. No diagram source may be created before author approval.
