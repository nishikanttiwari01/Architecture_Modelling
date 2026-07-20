---
title: "How a Full-Service Bank Works"
chapter: 32
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 32. How a Full-Service Bank Works

## Chapter purpose

Give readers the commercial and operational foundation needed to understand the architecture of Horizon Bank.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- describe the main customer segments, product families and enterprise functions of a full-service bank;
- explain, at a conceptual level, how interest, fees, capital, liquidity and risk affect architecture;
- distinguish customer, product, transaction, case, accounting and reporting lifecycles;
- explain why channels, processors, customer, risk, finance, integration and data platforms have different responsibilities;
- identify critical operations and their people, technology and third-party dependencies.

## Prerequisites and dependencies

- Chapter 31: BIAN Essentials and the Case-Study Method

## Required models and artefacts

- the Horizon Bank profile, assumptions, legal-entity, segment, product and business-line catalogues
- the full-service bank operating-model and lifecycle-view specifications
- the critical-operation, application, interface, control and reconciliation catalogues

## Worked examples

- Horizon Bank deposit-interest posting
- Horizon Bank time-critical payment

## Source requirements

Official banking, accounting, prudential and resilience sources support the general concepts. Jurisdiction-specific rules remain outside this author model unless a legal entity and jurisdiction are stated. [BCBS-CORE-PRINCIPLES-2024-PV32] [IFRS-CONCEPTUAL-FRAMEWORK-2018] [BCBS-OPERATIONAL-RESILIENCE-2021]

## Planned chapter structure

The chapter moves from customer and commercial purpose through products, financial mechanics, operating responsibilities, lifecycles, applications and critical operations.

## Start with obligations, not applications

A full-service bank does more than provide screens for moving money. It enters contracts, holds and safeguards assets, owes money to depositors, extends credit, exchanges financial obligations, records financial consequences and demonstrates that risks are controlled.

The first architecture question is therefore: **what obligation or outcome must the bank fulfil, for which party, through which legal entity, and with what evidence?** Technology becomes understandable only after these business facts are explicit.

Horizon Bank is `HB-BANK-01 Horizon Bank Group`, a fictional full-service banking group. Its catalogues use plausible banking responsibilities, but not fabricated volumes, balance-sheet figures, recovery times or regulatory thresholds. They are teaching decisions, not advice for a real bank.

## The governed scope of Horizon Bank

The group contains three illustrative legal entities:

- `HB-LE-01 Horizon Bank Group Holdings`, the group holding entity;
- `HB-LE-02 Horizon Bank Country Bank`, a licensed banking-entity placeholder;
- `HB-LE-03 Horizon Shared Services`, a service-entity placeholder.

These placeholders demonstrate why group, legal-entity and jurisdiction scopes must be separate. A group platform may support several entities, but the contract, accounting entry, liquidity position or regulatory submission still belongs to a defined legal entity. Shared performance of work does not transfer accountability without an explicit arrangement.

The operating baseline also assumes that the current architecture contains duplicate party data, product silos, point-to-point interfaces and manual reconciliation (`HB-ASM-02`). The target direction favours governed party data, modular responsibilities and managed APIs, events, files and workflow (`HB-ASM-03`). This direction does not mandate microservices or public cloud.

## Customer segments are service contexts

Horizon Bank uses five governed customer segments. A small and medium-sized enterprise (SME) is kept distinct from the larger commercial and corporate segment, while the exact threshold remains jurisdiction-specific.

| ID | Segment | Typical needs | Important architecture variation |
|---|---|---|---|
| `HB-SEG-01` | Retail | Everyday accounts, payments, savings, cards, mortgages and personal credit | Accessible high-volume journeys, customer authentication, fraud intervention and understandable communication |
| `HB-SEG-02` | SME | Accounts, payments, cards, cash-flow support and credit | Business ownership, mandates, mixed digital-assisted service and exposure across related facilities |
| `HB-SEG-03` | Commercial and Corporate | Cash management, bulk payments, financing, trade and foreign exchange | Complex legal structures, delegated authorities, files, host connectivity, limits and relationship coverage |
| `HB-SEG-04` | Private Banking | Advice, investment, financing and consolidated service | Suitability, confidentiality, portfolio views and managed relationships |
| `HB-SEG-05` | Institutional | Markets, custody, settlement and financing | Positions, collateral, market connectivity, asset segregation and time-sensitive operations |

A segment is not a separate bank architecture. Shared party identity, product governance, accounting, control and technology capabilities can support several segments. Variants are introduced where customer need, agreement, legal duty, channel or operating model genuinely differs.

## Business lines, products and legal entities answer different questions

Horizon Bank has four business lines:

- `HB-BL-01 Retail Banking`;
- `HB-BL-02 Business and Corporate Banking`;
- `HB-BL-03 Wealth and Securities`;
- `HB-BL-04 Treasury and Markets`.

A **business line** organises commercial and managerial accountability. A **product** defines a proposition, terms and customer promise. A **legal entity** enters the contract, holds assets or liabilities and carries applicable obligations. Treating these as one hierarchy creates serious gaps.

For example, `HB-PRD-07 Payment and Cash Management` is used by Retail Banking and Business and Corporate Banking. A corporate customer may contract with `HB-LE-02`, use `HB-APP-006 Corporate Digital Banking`, and be served by the Business and Corporate Banking line. None of those facts makes the product, channel and legal entity the same element.

Horizon Bank's main product families are:

- `HB-PRD-01 Deposits and Accounts`, with transaction-account and term-deposit products;
- `HB-PRD-04 Credit`, with consumer, mortgage, SME and corporate credit;
- `HB-PRD-07 Payment and Cash Management`;
- `HB-PRD-08 Cards and Merchant Services`, decomposed into issuing, acquiring and processing responsibilities;
- `HB-PRD-09 Trade Finance`;
- `HB-PRD-10 Investment, Advisory and Custody`.

Each product needs controlled eligibility, pricing, agreement, lifecycle, processor, information authority, accounting treatment, controls and servicing. A product catalogue entry is not enough to prove that these responsibilities are implemented.

## How a bank earns, spends and absorbs loss

A simplified bank balance sheet has **assets**, **liabilities** and **equity**. Loans and securities are examples of assets. Customer deposits and wholesale funding are examples of liabilities. Equity represents the residual interest after liabilities and provides loss-absorbing capacity in the prudential framework.

Interest earned on assets and interest paid on deposits or funding contribute to net interest income. Fees may arise from account services, payments, cards, lending, trade finance, advice or custody. Costs include staff, technology, premises, suppliers, operations and losses. The accounting treatment of a real instrument depends on facts and the applicable reporting framework. [IFRS-CONCEPTUAL-FRAMEWORK-2018]

Architecture affects whether the bank can explain these results. `HB-APP-014 Pricing and Fee Management` governs price plans and effective dates. A product processor applies the governed terms. `HB-APP-058 Product Subledger Platform` records product-level accounting detail. `HB-APP-059 General Ledger` holds approved legal-entity balances. `HB-APP-060 Enterprise Reconciliation` identifies and manages breaks. Combining these responsibilities in a diagram labelled `Core Banking` hides important authorities.

### Capital and liquidity are different

Capital is concerned with loss absorbency and the relationship between the bank's risk profile and available qualifying resources. Liquidity is concerned with the ability to meet obligations when due. A profitable bank can still face a liquidity problem, while a bank holding liquid assets can still have insufficient capital for its risk.

The Basel Core Principles connect supervision to capital adequacy, liquidity, large exposures, risk management and group structure. The exact requirements depend on applicable law, supervisor and scope. [BCBS-CORE-PRINCIPLES-2024-PV32]

For architecture, this means that exposure, collateral, funding, cashflow, settlement timing, market position and legal-entity transfer constraints must remain traceable. `HB-APP-030 Credit Exposure Aggregation`, `HB-APP-056 Funding and Liquidity Management`, `HB-APP-057 Asset Liability and Capital Management` and `HB-APP-064 Enterprise Risk Management` answer different questions.

### Risk is part of every lifecycle

Risk is not a final approval box. Credit risk arises when a borrower or counterparty may not fulfil an obligation. Market risk concerns losses from market movements. Liquidity risk concerns the ability to meet obligations. Operational risk includes failures of processes, people, systems or external events. Conduct, legal, model, cyber and financial-crime concerns introduce further decisions and evidence.

Business management owns the risks arising from its activities. Independent risk and compliance functions set frameworks, challenge and oversee within their mandates. Internal audit provides independent assurance. The precise structure varies, so the Horizon Bank organisation catalogue names accountable roles rather than relying only on a `three lines` label.

## Front, middle and back office are responsibility patterns

The **front office** engages customers and counterparties, originates business and provides service or advice. The **middle office** independently measures, challenges or controls risk and financial position where separation is needed. The **back office** confirms, settles, records, reconciles and services activity.

This pattern helps beginners understand separation of duties, but it is not a universal organisation chart. A straight-through digital payment can cross all three responsibility types without a person touching it. An exception may bring payment operations, financial crime, treasury, finance and customer service into the same case.

Horizon Bank makes the actual owners explicit. `HB-ORG-02 Product and Business Management` owns propositions and outcomes. `HB-ORG-03 Banking Operations and Corporate Services` performs controlled fulfilment and repair. `HB-ORG-04 Risk, Compliance and Assurance` provides independent oversight. `HB-ORG-05 Finance and Treasury` manages financial control and position. `HB-ORG-06 Technology, Data and Cyber Security` provides enabling and operational responsibilities.

## Connected lifecycles explain the bank

Several lifecycles run at once. An architecture that models only the customer journey will miss financial and operational consequences.

| Lifecycle | Typical start | Typical states or decisions | End or continuing outcome |
|---|---|---|---|
| Party and customer | A person or organisation is identified | Resolve identity, establish roles, perform due diligence, review relationship | Relationship serviced or exited with retained evidence |
| Product | A market or customer need is identified | Design, approve, publish, change, monitor | Product retired with obligations resolved |
| Agreement | An offer is accepted | Establish parties, terms, limits, mandates and status | Amended, transferred, matured or closed |
| Transaction | An instruction or business event occurs | Validate, authorise, execute, clear, settle, post, reverse or reject | Final or repairable status communicated |
| Position | Transactions and market events change a balance or exposure | Aggregate, value, limit, fund and monitor | Current controlled position carried forward |
| Case or exception | An alert, complaint or failure occurs | Triage, investigate, decide, repair, redress or escalate | Closed with evidence and follow-up |
| Accounting | A recognised business event occurs | Derive balanced entries, post, adjust, reconcile and close | Approved books and retained lineage |
| Reporting | A decision need or reporting obligation exists | Source, transform, validate, attest and submit | Governed report retained and corrected if required |

The intersections matter. Customer onboarding establishes a party and customer relationship but does not itself create every product agreement. A payment uses an account and entitlement, creates a transaction, may open a screening case, changes cash and accounting positions, and contributes to customer and regulatory reporting.

## Dates and the banking day

Financial activity often has several relevant dates:

- the **instruction date** records when a request was made;
- the **booking date** records when an entry was recognised by a system;
- the **value date** affects when financial value or interest takes effect;
- the **settlement date** records when obligations are exchanged or discharged;
- the **reporting date** defines the position represented in a report.

These dates may differ. A card transaction can be authorised on one day and presented, cleared and settled later. A foreign-exchange trade can be agreed before its settlement date. An interest accrual can be recognised before cash is paid.

The banking day includes intraday and scheduled responsibilities. Cut-offs, liquidity monitoring, clearing windows, accruals, statements, batch postings, reconciliation, close and opening the next business date may all coexist with real-time interfaces. `Real time` at the channel does not mean that every downstream obligation settles immediately.

## Worked example: deposit interest posting

Consider interest accrued on a transaction or savings account. The customer sees one amount, but the architecture must preserve a complete chain.

| Responsibility | Governed record | Role in the example |
|---|---|---|
| Product terms | `HB-APP-013 Enterprise Product Catalogue`; `HB-APP-014 Pricing and Fee Management` | Provide approved product, rate-plan and effective-date context |
| Deposit balance | `HB-APP-020 Deposit Account Processing`; `HB-SOR-02 Deposit Account Authority` | Maintains the account balance and product agreement state |
| Calculation | `HB-APP-021 Interest and Fee Accrual` | Calculates governed interest and produces the accrual result |
| Interaction | `HB-INT-028 Deposit Accrual Event` | Carries the governed accrual consequence |
| Accounting event | `HB-ACC-01 Deposit Interest Accrued` | Identifies the financial consequence independently of transport |
| Product accounting | `HB-APP-058 Product Subledger Platform` | Records product-level accounting detail |
| Legal-entity accounting | `HB-APP-059 General Ledger`; `HB-SOR-04 General Ledger Authority` | Records approved legal-entity balances |
| Reconciliation | `HB-REC-004 Deposit Interest Accrual`; `HB-REC-030 Subledger to General Ledger` | Tests calculation-to-posting and subledger-to-ledger completeness |
| Control | `HB-CTRL-09 Deposit Interest and Fee Calculation`; `HB-CTRL-28 Accounting-Event Completeness and Mapping` | Checks rule use, completeness and mapping |

The customer account posting, expense recognition and customer communication are related but distinct. A rejected accounting message must not silently disappear after the customer balance changes. Repair ownership, replay rules and reconciliation are part of the design.

## Why a full bank needs many application responsibilities

Horizon Bank's 90 logical applications are not a target application count. They expose distinct responsibilities that a five-box `banking platform` picture would hide.

| Application family | Primary responsibility | Must not silently become |
|---|---|---|
| Channels | Customer, employee or partner interaction | The authority for every product and customer fact |
| Journey and workflow | Coordinate long-running work | The owner of every rule and record |
| Party and customer | Resolve identity and relationship context | Product agreement or financial ledger |
| Product catalogue and pricing | Govern offers, eligibility attributes and commercial terms | Transaction processor |
| Product processors | Execute product and agreement lifecycle behaviour | Enterprise reporting platform |
| Transaction processors | Validate, route, clear, settle and record transaction state | Customer relationship master |
| Risk and control | Assess, limit, screen, monitor and preserve decision evidence | General ledger |
| Finance | Derive, record, reconcile and report financial consequences | Operational product master |
| Integration | Transport and govern exchanges | Accidental owner of business semantics |
| Data and analytics | Curate data for analysis, modelling and reporting | Unqualified operational authority |
| Security and operations | Protect, observe, recover and operate services | Product decision owner |

Separate logical responsibilities do not require separate purchased products or deployments. Chapter 34 shows the application landscape, and Chapter 50 explains how to decide physical boundaries without inflating the estate.

## Group, country, shared service and supplier boundaries

A group function may set policy, operate a shared platform or consolidate reporting. A country bank may own the customer agreement, books, liquidity position and local submission. A shared-service entity may perform work under an agreement. An external provider may supply identity data, cloud runtime or market connectivity.

Every shared or external arrangement should identify:

- the contracting and accountable legal entity;
- the service and data owner;
- which decisions remain with the bank;
- access, confidentiality and evidence obligations;
- dependencies and concentration risk;
- continuity, recovery, substitution and exit arrangements;
- how incidents, changes and control failures are escalated.

Outsourcing changes the delivery model, not the bank's need to understand and govern the outcome.

## Critical operations join the layers

Operational resilience concerns the bank's ability to deliver critical operations through disruption. It includes governance, dependency mapping, third-party management, continuity, incident management and resilient information and communication technology. [BCBS-OPERATIONAL-RESILIENCE-2021]

Horizon Bank catalogues 20 critical operations. These range from `HB-CRIT-01 Access Funds and Account Information` and `HB-CRIT-02 Make a Time-Critical Payment` to `HB-CRIT-15 Maintain Authoritative Financial Books`, `HB-CRIT-18 Contain and Recover from a Material Cyber Incident` and `HB-CRIT-20 Deliver Material Customer Communications`.

A critical operation is not the same as a critical application. It follows an outcome through people, processes, information, applications, technology, facilities and third parties. Several operations may depend on `HB-APP-008 Customer Identity and Access Management`, while one operation may depend on dozens of application and external-network responsibilities.

### Worked trace: make a time-critical payment

`HB-CRIT-02 Make a Time-Critical Payment` depends on:

1. customer access through `HB-APP-002 Retail Mobile Banking` or another authorised channel;
2. authentication and entitlement through `HB-APP-008` and `HB-APP-010`;
3. payment capture and orchestration through `HB-APP-033` and `HB-APP-034`;
4. screening through `HB-APP-018 Name and Sanctions Screening`;
5. account and funds control through `HB-APP-020 Deposit Account Processing`;
6. clearing and settlement through `HB-APP-035` and `HB-APP-036`;
7. an external rail such as `HB-EXT-001 High-Value Payment Network`;
8. liquidity management, accounting, reconciliation and customer status;
9. repair through `HB-APP-037 Payment Investigations and Exceptions` when normal processing fails;
10. technology observation and recovery through `HB-APP-086 Enterprise Observability Platform`, `HB-APP-087 Information Technology Service Management` and `HB-APP-090 Resilience Orchestration and Recovery`.

The degraded mode cannot be `keep accepting payments` unless the bank can preserve entitlement, duplicate protection, liquidity, cut-off, status and later reconciliation. The catalogue therefore leaves quantitative recovery objectives and impact tolerances pending until evidence supports them.

## Models to use, and models not to use

Use a value stream to explain how value progresses towards an outcome. Use a capability map to show the abilities needed. Use BPMN for ordered work and exceptions. Use a conceptual data model for customer, agreement, transaction and position concepts. Use an application landscape for logical software responsibilities. Use a dependency map for critical operations.

Do not put all these concerns on one diagram. A single picture that mixes a customer journey, servers, data tables, control teams and settlement sequence usually answers none of the questions well. Connect several focused views through stable catalogue IDs instead.

## Common mistakes

- Treating a business line, legal entity, product and application as the same boundary.
- Modelling only customer-facing journeys and omitting settlement, accounting, reconciliation and repair.
- Assuming an authorised transaction has already cleared or settled.
- Assuming a real-time channel removes cut-offs, batch work and the banking-day cycle.
- Treating the data platform as authoritative for all operational information.
- Showing `Risk` as one approval step instead of lifecycle responsibilities and evidence.
- Calling one application critical without tracing the entire critical operation.
- Describing shared services or outsourcing without retained accountability and exit planning.
- Inventing ratios, recovery objectives or processing volumes for a fictional bank.

## Chapter summary

A full-service bank connects customer needs to contracts, positions, transactions, controls and financial records. Its business lines, products, segments and legal entities are different views. Its lifecycles intersect, and its operations depend on specialised application, information and ownership responsibilities.

## Completion checklist

- [x] The governed Horizon Bank scope, segments, products and legal entities are explicit.
- [x] Interest, fees, capital, liquidity and risk are explained at a conceptual level.
- [x] Customer, product, agreement, transaction, case, accounting and reporting lifecycles are separated.
- [x] Application families have distinct responsibilities.
- [x] Both worked examples use governed IDs and include controls and reconciliation.
- [x] Critical operations include people, information, technology and third parties.
- [ ] `FIG-32-01` source remains deferred until its specification is author-approved.

## Key takeaways

- Start with the bank's obligation and legal-entity scope, not its application names.
- Segment, product, business line and legal entity answer different questions.
- Capital, liquidity, profitability and accounting are connected but not interchangeable.
- Customer, transaction, case and financial lifecycles continue beyond the channel journey.
- A critical operation is an end-to-end outcome supported by many dependencies.

## Practical exercise

Trace a retail card purchase from `HB-APP-002 Retail Mobile Banking` and `HB-APP-040 Card Issuing Management` through `HB-APP-041 Card Authorisation`, `HB-APP-042 Card Processing and Clearing`, `HB-ACC-17 Issuer Card Purchase Cleared` and `HB-REC-018 Card Clearing and Settlement`.

Mark the authorisation, presentment, clearing, settlement and account-posting stages. Identify one fraud exception, one external-network dependency and one point where the booking and settlement dates could differ.

## Review checklist

- [ ] Are customer, product, business-line and legal-entity scopes explicit?
- [ ] Are common banking concepts distinguished from jurisdiction-specific requirements?
- [ ] Does each lifecycle state its beginning, governing decisions and outcome?
- [ ] Are processing, accounting, control and reporting authorities separated?
- [ ] Does every critical-operation view include people, process, information, applications, technology and third parties?
- [ ] Are all numerical targets either sourced or visibly pending?

## References and further reading

- [BCBS-CORE-PRINCIPLES-2024-PV32]
- [BCBS-OPERATIONAL-RESILIENCE-2021]
- [IFRS-CONCEPTUAL-FRAMEWORK-2018]

## Drafting notes

- The chapter uses a qualitative full-bank model. Jurisdiction-specific capital, liquidity, accounting, recovery and service thresholds remain intentionally outside the fictional baseline.
- `FIG-32-01` is registered and specified. No source may be produced before author approval.
