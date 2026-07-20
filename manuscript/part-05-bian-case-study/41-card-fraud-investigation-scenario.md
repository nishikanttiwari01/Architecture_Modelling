---
title: "Payments, Clearing, Settlement, Correspondent Banking and Foreign Exchange"
chapter: 41
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 41. Payments, Clearing, Settlement, Correspondent Banking and Foreign Exchange

## Chapter purpose

A payment is not complete merely because a customer has pressed **Send**. The bank must accept an instruction, establish authority, control financial-crime risk, route the instruction, exchange it with other institutions, settle the resulting obligation, post the financial outcome and resolve exceptions. This chapter shows how to model those responsibilities without hiding them inside one box called `Payments`.

The central architecture question is: **which business and application responsibility owns each state of a payment, and what evidence proves that money and status remain consistent?** Horizon Bank is fictional. Its catalogue is an author model, not a statement about a particular country's payment schemes or settlement law.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish initiation, execution, clearing and settlement;
- explain the roles of correspondent banking and payment-related foreign exchange (FX);
- trace an instruction through capabilities, processes, applications, data authorities, interfaces, accounting events, controls and reconciliations;
- choose useful models for payment structure, behaviour and exception handling;
- recognise where network, legal-entity and jurisdiction assumptions remain unresolved; and
- review a payment architecture without assuming that a BIAN Service Domain equals an application or deployable service.

## Prerequisites and dependencies

- Chapter 34, for the full-bank application and integration landscape.
- Chapter 35, for data authority and lineage.
- Chapter 36, for critical operations and resilience.
- Chapter 40, for limits and exposure concepts used at payment and correspondent boundaries.

## Required models and artefacts

- Governed payment domain, capability and process records.
- Logical application, interface and external-network catalogues.
- Payment-state, data-authority, accounting-event and reconciliation views.
- Control, critical-operation and technology-resilience records.

The governed operating trace starts with `HB-ORG-111 Payments Director Role` for payment propositions and network participation. `HB-ORG-28 Payment and Card Operations` performs clearing, settlement and investigation work. `HB-ORG-14 Compliance, Financial Crime and Conduct` provides independent financial-crime oversight, while `HB-ORG-12 Finance, Accounting, Tax and Reporting` owns accounting policy, books and financial control. These responsibilities meet at controlled hand-offs; none owns the whole payment lifecycle.

No new diagram source is required in this drafting pass. A later visual must follow the specification-first approval workflow.

## Worked examples

- Horizon Bank cross-border payment with payment-related FX.
- Horizon Bank immediate domestic payment as an exercise alternative.

## Source requirements

Payment terminology uses official CPMI material. Banking Industry Architecture Network (BIAN) statements use the governed BIAN 14.0 note. Network, finality, legal and accounting choices remain Horizon Bank assumptions until verified for the applicable arrangement.

## What is the payment domain?

In plain language, the payment domain moves value according to an authorised instruction and maintains trustworthy evidence of the outcome. It serves retail customers, businesses, the bank's own operations and other financial institutions. Product teams, payment operations, financial-crime teams, settlement operations, finance controllers, technology teams and customer-service staff all use its models for different decisions.

The governed Level 1 domain is `HB-DOM-050 Payments`. It is decomposed into four Level 2 domains:

| Domain | Question answered |
|---|---|
| `HB-DOM-051 Payment Initiation and Execution` | How is an instruction captured, controlled and routed? |
| `HB-DOM-052 Clearing, Settlement and Correspondent Banking` | How are obligations exchanged, calculated and completed? |
| `HB-DOM-053 Payment Liquidity and Foreign Exchange` | How are funding, cut-offs and currency conversion coordinated? |
| `HB-DOM-054 Payment Investigations and Reporting` | How are failures, returns, enquiries and evidence resolved? |

These domains support `HB-PRD-07 Payment and Cash Management` and `HB-VS-04 Execute and Settle Transaction`. The Level 1 process `HB-PROC-04 Execute and Settle Payments` supplies the behavioural backbone. This is a capability and process decomposition, not a deployment design.

### Payment roles and artefacts

A **payer** requests that value be transferred, while a **payee** is the intended recipient. Message standards and rulebooks may instead use **debtor** and **creditor** for the parties whose obligations or accounts are affected. These terms are not always perfect synonyms, especially when an initiating party acts for an account owner or an intermediary participates. A model should therefore name the role used by the applicable arrangement rather than replace every role with `customer`.

The customer instruction, payment order, external message, clearing obligation, settlement movement, account posting, General Ledger effect and customer notification are also distinct artefacts. One can exist without all the later artefacts. The architecture must preserve their identifiers and relationships so a status enquiry can say what has happened, not merely return `complete`.

## Initiation, clearing and settlement are different

**Payment initiation** captures what the payer wants the bank to do. `HB-CAP-051 Payment Initiation` and `HB-CAP-052 Payment Validation and Routing` cover authentication, instruction validation, entitlement, screening, enrichment and route selection. Their Level 2 process is `HB-PROC-120 Initiate, Validate and Route a Payment`.

**Clearing** establishes and exchanges the information needed to calculate obligations. It can involve individual instructions, files, responses, returns and control totals. `HB-CAP-053 Payment Clearing` and `HB-APP-035 Payment Routing and Clearing` own this concern in the Horizon model.

**Settlement** completes the transfer of the settlement asset between the relevant institutions or accounts. It can be gross or net, immediate or scheduled, and finality depends on the applicable arrangement and law. `HB-CAP-054 Payment Settlement` and `HB-APP-036 Settlement and Nostro Management` record obligations, positions and evidence. The Committee on Payments and Market Infrastructures (CPMI) glossary is the terminology baseline, not proof that any particular mechanism applies to Horizon Bank [CPMI-PAYMENT-GLOSSARY-2016].

The distinction matters during failure. An instruction can be accepted but not cleared, cleared but not yet settled, or settled externally while an internal customer posting is delayed. A single `Success` flag cannot represent these states safely.

## Operating model and end-to-end process

The payment operating model separates product authority from execution and control. The Payments Product Director owns customer propositions and initiation outcomes. Payments Operations owns orchestration and clearing. Settlement Operations owns settlement obligations and nostro positions. Financial Crime owns screening dispositions. Finance Control owns accounting and reconciliation. Investigations owns unresolved cases.

The normal path is:

1. A channel submits an instruction to `HB-APP-033 Payment Initiation Service`.
2. `HB-CTRL-14 Payment Instruction, Entitlement and Funds Validation` checks identity, authentication, consent where applicable, mandate, account state, limits and funds. A reservation is distinct from both a balance enquiry and a final posting.
3. `HB-APP-034 Payment Orchestration` coordinates `HB-APP-018 Name and Sanctions Screening`, fraud assessment where the approved payment type requires it, funds control and route selection.
4. `HB-CTRL-15 Payment Duplicate and Idempotency Control` prevents a retry from creating a second financial effect.
5. `HB-APP-035 Payment Routing and Clearing` exchanges the instruction with the selected logical network.
6. `HB-APP-036 Settlement and Nostro Management` records the settlement obligation and evidence.
7. Product processors and finance consume the result, and `HB-ACC-14 Payment Settlement Recognised` describes the accounting consequence.
8. `HB-APP-037 Payment Investigations and Exceptions` receives repairs, returns, recalls, cancellation requests and enquiries.
9. The originating domain supplies an accurate outcome to customer communications. A notification reports governed status; it does not create settlement finality.

This is an architecture sequence, not a substitute for a jurisdiction-specific Business Process Model and Notation (BPMN) collaboration. A detailed BPMN model would add human roles, time-outs, message events and repair gateways. A runtime sequence view would instead show call order, retries, correlation and time budgets.

## Application responsibilities and interactions

The application catalogue deliberately avoids one large payment engine:

| Application | Distinct responsibility |
|---|---|
| `HB-APP-033 Payment Initiation Service` | Instruction validation and pre-acceptance status |
| `HB-APP-034 Payment Orchestration` | Cross-system execution state and coordination |
| `HB-APP-035 Payment Routing and Clearing` | Rail selection, message transformation and clearing exchange |
| `HB-APP-036 Settlement and Nostro Management` | Settlement obligations, cash positions and completion evidence |
| `HB-APP-037 Payment Investigations and Exceptions` | Repair, return, recall and enquiry cases |
| `HB-APP-038 Correspondent Banking Management` | Correspondent relationships, accounts, terms and routing eligibility |
| `HB-APP-039 Foreign Exchange Pricing and Booking` | FX quotation, acceptance and trade booking |

The split is logical. A retained platform could implement several responsibilities, or one logical application could use several deployable services. The boundaries remain useful because ownership, data authority, recovery and change differ.

Key interactions are typed. `HB-INT-036 Accepted Payment Command` transfers an accepted instruction into orchestration. `HB-INT-037 Payment Clearing Instruction` is a message to clearing. `HB-INT-038 Foreign Exchange Quote` is an application programming interface (API) response with an expiry. `HB-INT-065 Correspondent Settlement Instruction` and `HB-INT-105 Cross-Border Financial Message` cross governed external boundaries. A label such as `integrates with` would hide direction, information and failure responsibility.

## Domestic rails and external networks

Horizon's network catalogue uses logical placeholders because membership and jurisdiction are unverified. `HB-EXT-001 High-Value Payment Network`, `HB-EXT-002 Retail Payment Clearing Network` and `HB-EXT-003 Immediate Payment Network` represent distinct operating models. They connect through `HB-INT-063`, `HB-INT-062` and `HB-INT-064` respectively.

The architecture must not infer that an immediate network is always irrevocable, that a high-value network always uses real-time gross settlement, or that a retail clearing network always uses deferred net settlement. Those are scheme and legal decisions. The network record must eventually supply participation, operating window, message profile, finality, liquidity and exception evidence.

Payment products also behave differently even when they reuse applications. An internal book transfer may avoid an external clearing network but still needs authority, posting and duplicate control. A wire or high-value payment may be handled individually. An automated clearing house (ACH) arrangement may exchange individual or batched obligations. Direct debits begin from a creditor-initiated collection under a governed mandate, while standing orders are recurring payer instructions. Bulk and payroll files require file-level and item-level totals, approval, partial-acceptance and duplicate semantics. Request-to-pay, where supported, is a request for a later payment decision, not the payment itself.

`HB-INT-025 Corporate Payment Initiation` supports payment and bulk-file initiation from `HB-APP-006 Corporate Digital Banking`, but the catalogue does not yet define a separate host-file contract for every product above. Their detailed rules, return rights and network applicability remain pending.

Message syntax does not determine the complete business lifecycle. ISO 20022 can provide structured financial-message semantics where an applicable network profile selects it. Cross-border profiles such as the Society for Worldwide Interbank Financial Telecommunication (SWIFT) Cross-Border Payments and Reporting Plus (CBPR+) must be verified for the selected connectivity before use. Horizon Bank's `HB-INT-105` intentionally leaves the message profile pending, so this chapter does not claim universal ISO 20022 or SWIFT applicability.

Cut-off time, value date, settlement date, time zone, currency and holiday calendar affect whether an accepted instruction can be processed as requested. These attributes belong in governed routing and customer-status decisions. They must not be hidden in a scheduler configuration or assumed identical across correspondents and rails.

## Correspondent banking is a relationship and an account service

Correspondent banking enables one institution to provide account and payment services to another. A cross-border chain may involve several banks and accounts [CPMI-CORRESPONDENT-BANKING-2016]. The architecture therefore separates three things:

- the customer payment instruction in `HB-SOR-08 Payment Instruction and Processing Authority`;
- the correspondent relationship and routing eligibility in `HB-APP-038`; and
- settlement obligations and nostro positions in `HB-SOR-09 Settlement and Correspondent Position Authority`.

A **nostro account** is the bank's view of an account it holds with another institution. It is not interchangeable with the external correspondent's statement. `HB-REC-015 Correspondent Cash and Nostro` compares external statements and advices with internal cash, payment, fee and FX postings. Breaks belong to a governed investigation and correction process, not to an analyst editing a balance.

A **vostro account** is the corresponding `your account with us` view from the account-servicing bank's perspective. Whether Horizon Bank holds a nostro, services a vostro or participates through another arrangement must be stated per relationship and legal entity.

In a **serial payment**, settlement instructions progress through the correspondent chain. A **cover payment** separates the customer-payment information from a related interbank funding path. These are arrangement-specific patterns, not drawing styles. Agent roles, message linkage, screening, funding and reconciliation must be verified before either label appears in a solution model.

`HB-EXT-004 Cross-Border Financial Messaging Network` and `HB-EXT-005 Correspondent Banking Connectivity` are also different. Secure messages may carry instructions, but a message does not itself prove account funding, settlement or legal finality.

## Foreign exchange linked to a payment

A cross-currency payment may require a quote, an accepted FX deal and two currency legs. `HB-CAP-056 Payment Foreign-Exchange Coordination` obtains governed terms for the payment. `HB-APP-039` records the accepted deal, while `HB-INT-068 Treasury Foreign Exchange Booking` transfers it into treasury position management. Chapter 45 covers the wider treasury position and market-risk responsibilities.

The foreign-exchange model must distinguish quote time, trade time, value date, rate, margin, currency legs and settlement state. `HB-CTRL-17 Foreign-Exchange Price, Deal and Settlement Control` links the authorised price to the deal and both settlement legs. `HB-ACC-16 Foreign-Exchange Deal Recognised` records accounting consequences only after the bank's accounting policy and legal-entity rules are approved.

**Payment versus payment (PvP)** links final settlement of one currency to final settlement of the other. It reduces the risk of delivering one currency without receiving the other, but it is not available for every currency, instrument or participant [CPMI-PVP-2023]. The Horizon catalogue therefore leaves the mechanism pending rather than claiming universal PvP.

## Information authority, accounting and reconciliation

`HB-DATA-08 Payments, Clearing and Settlement` provides domain meaning for instruction, route, clearing, settlement, correspondent, FX leg and investigation data. It complements the broader `HB-DATA-03 Account and Transaction` and `HB-DATA-05 Finance and Accounting` domains.

Authority changes with lifecycle stage. `HB-APP-033` is authoritative for pre-acceptance instruction content. `HB-APP-034` owns orchestration state. `HB-APP-036` owns internal settlement evidence after governed confirmation. An external statement still requires reconciliation before its data becomes an accepted internal position.

Three reconciliations answer different questions:

- `HB-REC-012 Payment Instruction to Processing Status`: did every accepted instruction reach a visible outcome?
- `HB-REC-013 Payment Clearing Submission and Response`: did each external submission receive a governed response?
- `HB-REC-014 Settlement Account and Payment Ledger`: do settlement evidence and internal financial positions agree?

`HB-ACC-03 Payment Fee Charged`, `HB-ACC-14 Payment Settlement Recognised` and `HB-ACC-15 Correspondent Fee and Charge Recognised` represent distinct accounting events. Their records intentionally leave debit, credit, tax, reversal and suspense rules pending. Architecture establishes traceability; accounting policy determines the entries.

## Controls, security and operational resilience

Payments combine preventive, detective and corrective controls. `HB-CTRL-02 Transaction Screening and Referral` blocks or refers applicable activity. `HB-CTRL-14` protects instruction acceptance. `HB-CTRL-15` protects against duplicate effect. `HB-CTRL-16 Payment Clearing, Settlement and Nostro Break Control` detects unresolved financial differences.

`HB-CRIT-02 Make a Time-Critical Payment` states the critical business outcome. `HB-TECH-009 Payments Processing Classification` identifies the technology family that must preserve instructions, screening state, duplicate protection and settlement evidence during recovery. Recovery Time Objective (RTO), Recovery Point Objective (RPO), impact tolerance and degraded modes remain explicit gaps. Inventing attractive numbers would not make the design resilient.

A safe degraded mode might queue an instruction or restrict a rail while preserving status and customer communication. It must not silently bypass screening, duplicate controls or settlement evidence. The recovery scenario `HB-SCN-19 Recover Payment Service after Cyber Disruption` also requires identity, key, data-integrity and reconciliation checks before normal processing resumes.

## BIAN alignment and model choices

`HB-BIAN-02 Payment Responsibility Candidate` is the governed mapping placeholder. Exact BIAN 14.0 Service Domains and their many-to-many rationale remain unverified. The chapter therefore uses BIAN as a responsibility-analysis aid, not as a list of application names.

Useful complementary models answer different questions:

| Model | Best payment question |
|---|---|
| Capability map | What abilities must the bank maintain? |
| BPMN collaboration | Which parties perform work and exchange messages? |
| State machine | Which instruction states and transitions are valid? |
| Sequence or dynamic view | What is the runtime order and retry behaviour? |
| Data lineage | Where did status, amount and settlement evidence originate? |
| Reconciliation catalogue | Which populations are compared and who resolves breaks? |
| Deployment and resilience view | Where can failure occur and how is service recovered? |

No new diagram source is created in this chapter pass. Any later figure must first be registered and specified, then approved by the author before source production.

## Worked traceability: a cross-border payment with FX

`HB-SCN-02 Execute Cross-Border Payment` begins when an authorised customer submits a supported instruction. The instruction enters `HB-APP-033`, passes authentication, entitlement, duplicate, sanctions and applicable fraud controls, and reaches `HB-APP-034`. If conversion is needed, `HB-INT-038` obtains an expiring quote from `HB-APP-039`. Clearing and correspondent routing use `HB-APP-035`, `HB-APP-038`, `HB-INT-105` and the logical external networks.

Settlement evidence reaches `HB-APP-036`; customer and finance postings follow the governed final status. `HB-REC-012`, `HB-REC-014`, `HB-REC-015` and `HB-REC-016 Foreign-Exchange Trade and Settlement` test different populations. A repairable reject, return, recall, cancellation request or missing correspondent response becomes a case in `HB-APP-037`. Customer notification distinguishes accepted, pending, rejected, returned and investigation states without claiming that delivery of a notice proves settlement.

The example is intentionally incomplete. Corridor rules, fee bearer, available currencies, cut-offs, legal finality, PvP coverage and correspondent agreements are pending. Those gaps are part of the model, not editorial omissions.

## Current-to-target considerations

Most rail, settlement, correspondent, investigation and FX applications are current. `HB-APP-034 Payment Orchestration` is the proposed target coordination responsibility, so migration must preserve the authority of existing rail processors while execution state moves gradually.

A safe transition establishes a common payment identity and status model, wraps current rail interfaces, moves selected payment types behind `HB-INT-036` and `HB-INT-037`, parallel-reconciles accepted instructions and financial effects, and only then retires duplicated orchestration. Cut-over criteria must include open investigations, scheduled and recurring instructions, file populations, correspondent acknowledgements and replay boundaries. A target event platform does not cure ambiguous finality or missing scheme rules.

## When should this model set be used?

Use this set when designing a new payment proposition, rationalising duplicated processing, changing a rail, separating data authority, planning recovery or investigating inconsistent status and financial positions. It helps product, operations, finance, risk and technology stakeholders see their shared outcome without erasing their separate responsibilities.

Do not use the catalogue-level view as a network implementation specification, settlement-finality opinion, sanctions rulebook or message schema. Those require the verified scheme, jurisdiction, contract, control and technical sources.

## Common mistakes

- Calling customer acceptance `settlement`.
- Treating a network acknowledgement as proof of final posting.
- Storing only one payment status and overwriting earlier evidence.
- Combining correspondent relationship, messaging and nostro position in one record.
- Retrying without an end-to-end business key and prior-outcome check.
- Treating FX quotation as the same event as trade booking or settlement.
- Omitting returns, repairs, recalls, suspense and reconciliation.
- Copying candidate BIAN names into an application diagram as if they were verified deployable services.

## Key takeaways

- Initiation, clearing and settlement are distinct responsibilities and lifecycle states.
- A payment architecture needs explicit data authority at each stage.
- Correspondent messaging does not itself prove settlement or account position.
- FX quotation, booking and currency-leg settlement require linked but separate controls.
- Accounting and reconciliation turn operational status into reviewable financial evidence.
- Critical-operation design must preserve safe status and duplicate protection during disruption.
- BIAN mappings remain candidates until exact 14.0 objects and rationale are verified.

## Practical exercise

Choose either an immediate domestic payment or a cross-border payment with FX. Create a one-page traceability table with one row for each lifecycle stage. Include the accountable capability, process, application, authoritative record, interface, control, accounting event, reconciliation and exception owner.

**Suggested review criteria:** The table must distinguish clearing from settlement, show at least one rejected or unresolved path, use full governed IDs, and mark all network, finality and currency assumptions as pending rather than guessing them.

## Review checklist

- [x] Initiation, clearing, settlement, correspondent banking and FX are distinguished.
- [x] Capabilities, processes, applications and interfaces use governed IDs.
- [x] Information authority, accounting, controls and reconciliation are explicit.
- [x] Network and legal assumptions are presented as gaps.
- [x] BIAN is not equated with an application or microservice.
- [x] Common mistakes and model-selection guidance are actionable.
- [ ] Exact BIAN 14.0 payment objects remain to be verified in the mapping register.
- [ ] Diagram production remains deferred pending author-approved specifications.

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14]
- [CPMI-PAYMENT-GLOSSARY-2016]
- [CPMI-CORRESPONDENT-BANKING-2016]
- [CPMI-PVP-2023]

## Drafting notes

- Before formal review, verify exact BIAN 14.0 payment mappings and the applicable network, finality and legal-entity decisions.
