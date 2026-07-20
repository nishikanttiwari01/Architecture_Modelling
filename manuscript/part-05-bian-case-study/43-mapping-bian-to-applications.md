---
title: "Corporate Banking, Cash Management and Trade Finance"
chapter: 43
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 43. Corporate Banking, Cash Management and Trade Finance

## Chapter purpose

Corporate banking is not retail banking with larger balances. A corporate customer can contain many legal entities, accounts, authorised users, approval mandates, cash structures and cross-border obligations. Trade finance adds instruments, documents, contingent exposure and claims. This chapter explains how those responsibilities connect without treating trade finance as deposit acquisition.

The central architecture question is: **how does the bank preserve corporate authority, liquidity visibility and trade obligations across organisations, applications and external parties?** Horizon Bank is fictional. Its cash structures and trade lifecycle are an author model, not legal, tax or documentary-credit advice.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- model corporate groups, service structures, mandates and authorised users;
- distinguish account reporting, payment execution and corporate liquidity services;
- explain cash concentration, sweeping, pooling and virtual-account responsibilities without assuming a particular legal arrangement;
- trace a trade-finance instrument from request through closure;
- connect applications, interfaces, data authority, exposure, accounting, reconciliation, control and resilience; and
- apply BIAN as a candidate responsibility mapping rather than a physical solution template.

## Prerequisites and dependencies

- Chapter 37, for party, beneficial-owner and customer due-diligence concerns.
- Chapter 38, for account and deposit servicing.
- Chapters 39 and 40, for corporate credit, limits, collateral and exposure.
- Chapter 41, for payment execution and foreign exchange.

## Required models and artefacts

- Governed corporate, cash-management and trade-finance domain records.
- Corporate relationship, mandate, cash-structure and instrument-lifecycle views.
- Logical applications, typed interfaces and external-network records.
- Exposure, accounting-event, reconciliation, control and resilience records.

The governed operating trace assigns corporate propositions and relationship outcomes to `HB-ORG-09 Business and Corporate Banking`. `HB-ORG-113 Trade Finance Director Role` is accountable for trade-finance products and instruments. `HB-ORG-30 Trade, Treasury and Securities Operations` performs document, settlement and asset-servicing work, while `HB-ORG-28 Payment and Card Operations` executes the related payment lifecycle. Product pricing remains governed through `HB-ORG-27 Product, Proposition and Pricing`.

No new diagram source is required in this drafting pass. A later visual must follow the specification-first approval workflow.

## Worked examples

- Horizon Bank corporate cash structure with governed sweep instructions.
- Horizon Bank trade instrument from request through closure.

## Source requirements

Documentary-credit practice uses official International Chamber of Commerce (ICC) guidance where cited. Banking Industry Architecture Network (BIAN) claims use the governed BIAN 14.0 note. Instrument rules, law, tax, pooling and network decisions remain unverified Horizon Bank assumptions.

## What is the corporate banking domain?

`HB-DOM-070 Corporate Banking, Cash Management and Trade Finance` is the governed Level 1 domain. Its capability counterpart is `HB-CAP-070 Corporate Banking, Cash Management and Trade Finance`, and it is decomposed into:

| Domain | Main responsibility |
|---|---|
| `HB-DOM-071 Corporate Coverage and Mandates` | Corporate groups, coverage, service structures and authorities |
| `HB-DOM-072 Cash and Liquidity Management` | Balances, collections, disbursements, sweeping, pooling and liquidity information |
| `HB-DOM-073 Trade Finance Origination and Instruments` | Eligibility, limits, issuance and amendment |
| `HB-DOM-074 Trade Documents, Exposure and Settlement` | Presentations, discrepancies, claims, financing, settlement and closure |

These responsibilities serve `HB-BL-02 Business and Corporate Banking`. Cash management uses `HB-PRD-07 Payment and Cash Management`; trade finance uses `HB-PRD-09 Trade Finance`. The latter maps to `HB-VS-10 Provide and Manage Trade Finance` and relates to `HB-VS-04 Execute and Settle Transaction`. It does not map to `HB-VS-03 Acquire and Service Deposit or Account`.

## Corporate relationship and mandate model

A corporate customer model must distinguish the group, each legal person, ownership and control relationships, accounts, service agreements, authorised users and approval mandates. `HB-CAP-071 Corporate Relationship and Structure Management` manages the relationship structure. `HB-CAP-074 Corporate Mandate and Bulk Instruction Management` governs who may submit, approve or release actions.

An approval matrix adds amount, account, product, currency, role combination and effective dates to that authority. It may require one approver, two independent approvers or a sequence of roles. The matrix must show delegation, expiry and emergency treatment. Authentication identifies the user; it does not prove that the user may release this instruction.

`HB-PROC-128 Manage Corporate Coverage, Structures and Mandates` begins with a prospect or relationship change and ends with a governed operating mandate. It must accommodate group changes, user movement, authority expiry and product-specific approval conditions. A static list of signatories is not sufficient for multi-account and multi-entity services.

`HB-APP-005 Relationship Manager Workbench` supports proposals and service requests. `HB-APP-006 Corporate Digital Banking` provides customer journeys. `HB-APP-010 Customer Entitlement and Mandate Service` is the decision authority for account and corporate permissions. `HB-CTRL-06 Consent, Mandate and Entitlement Enforcement` requires the identity, policy version, purpose, account, action and outcome to remain traceable.

The workbench and channel consume relationship information; they are not automatically the party or mandate source of truth. This separation makes revocation and approval evidence consistent across payments, trade instruments and merchant services.

Corporate access can use an interactive portal, host-to-host connection or governed file exchange. `HB-APP-006 Corporate Digital Banking` and `HB-INT-025 Corporate Payment Initiation` cover the current portal and bulk-file boundary. `HB-APP-007 Partner and Open Banking Portal` represents managed partner access, but the catalogue has no dedicated host-to-host or corporate managed-file interface. File encryption, signing, control totals, partial acceptance, resubmission and technical-client identity must therefore remain explicit design gaps.

## Cash management and liquidity services

Cash management helps a corporate customer see and control operating cash. `HB-CAP-072 Corporate Cash Management` covers collections, disbursements, balance information and cash-position services. `HB-CAP-073 Corporate Liquidity Structures` covers sweeping, pooling and concentration arrangements. `HB-PROC-129 Establish and Operate Corporate Cash and Liquidity Services` connects setup and daily operation.

`HB-APP-047 Corporate Cash Management` is authoritative for cash structures and virtual-account allocation rules. It consumes governed balances from `HB-APP-020 Deposit Account Processing` through `HB-INT-039 Deposit Balance and Transaction Feed`. It sends an approved movement through `HB-INT-072 Cash Structure Payment Command` to `HB-APP-033 Payment Initiation Service`.

This boundary prevents a cash-management application from directly altering a booked deposit balance. It calculates a sweep or concentration instruction; the payment and account applications authorise and post the movement.

Common service patterns include:

- **cash visibility**, which presents governed balances and transaction status;
- **physical sweeping**, which creates actual account movements under a schedule or threshold;
- **pooling**, which calculates a combined liquidity position under an approved legal and tax arrangement;
- **virtual accounts**, which allocate receipts or reporting identifiers while preserving the authority of the underlying account; and
- **bulk instruction processing**, which validates files, totals, duplicates, mandates and approvals before release.

Collections and receivables services help identify incoming cash and allocate it to invoices or customer references. Virtual accounts may support that allocation, but the underlying booked account and payment remain authoritative. Payroll is a specialised bulk-payment use case whose confidentiality, approval and cut-off requirements should be stated rather than hidden in a generic file label.

Bank account management (BAM) governs the lifecycle of accounts included in the corporate service: request, approval, opening dependency, mandate, structure membership, restriction and closure. It is not the same as processing the account balance. Client implementation coordinates connectivity, users, accounts, file formats, testing and operational readiness before service activation.

Service pricing must link the approved product and price version to the corporate agreement. `HB-APP-014 Pricing and Fee Management` can provide governed rates and fees, while `HB-APP-047` applies the service arrangement. Waivers, bespoke prices and later changes require approval and effective dates.

A service-level agreement (SLA), its operational timers and cut-offs belong to the product and network context. A bulk file accepted before a channel cut-off may still contain items that miss a currency, payment or correspondent cut-off. Cash-position reporting must identify source time, balance type and unavailable or stale feeds.

The chapter does not assume that cross-entity or cross-border pooling is permissible. Legal ownership, set-off, tax, currency and reporting decisions remain gaps in `HB-APP-047`, `HB-PROC-129`, `HB-SCN-12` and `HB-TECH-013`.

## Operating a corporate cash structure

`HB-SCN-12 Operate a Corporate Cash Structure` traces a controlled daily cycle:

1. `HB-APP-006` authenticates the corporate user through the customer identity service.
2. `HB-APP-010` evaluates mandate, account and approval policy.
3. `HB-APP-047` obtains balances and calculates the configured sweep.
4. The authorised instruction crosses `HB-INT-072` into payment initiation.
5. Chapter 41's payment applications screen, route, settle and post the movement.
6. Cash management receives current status and presents liquidity information.
7. Exceptions remain visible and are reconciled rather than overwritten.

`HB-CRIT-10 Operate Corporate Cash and Liquidity Services` identifies the critical outcome: customers can manage time-sensitive cash under authorised structures. A safe disruption response may pause a sweep or bulk file when duplicate protection and status cannot be assured. It must not guess balances or repeat prior instructions.

## Trade finance is a complete instrument lifecycle

`HB-VS-10 Provide and Manage Trade Finance` begins with an instrument request and ends when the obligation, exposure and evidence are closed. It includes eligibility, limits, issuance, amendment, presentation, discrepancy, financing, claim, settlement and closure. Account opening is a dependency where relevant, not the value stream itself.

The Level 1 process is `HB-PROC-06 Originate and Service Trade Finance`. Two Level 2 processes separate lifecycle concerns:

- `HB-PROC-130 Originate, Issue and Amend Trade Instruments` covers request, eligibility, limit, approval and changes.
- `HB-PROC-131 Examine Trade Documents and Resolve Exposure` covers presentations, discrepancies, claims, financing, settlement and closure.

The capability model is equally explicit. `HB-CAP-075` covers origination, `HB-CAP-076` issuance and amendment, `HB-CAP-077` document and discrepancy management, `HB-CAP-078` contingent exposure and claims, and `HB-CAP-079` financing, settlement and closure.

### Instrument families and related finance

A letter of credit records a bank undertaking subject to its terms and any incorporated rules. A guarantee records a different undertaking and claim basis. A documentary collection coordinates documents and instructions without silently becoming the same obligation as a documentary credit. A trade loan creates funded credit with repayment and servicing state. Supply-chain finance is a family of buyer-, supplier- or receivable-linked financing arrangements whose exact legal and credit structure must be defined before modelling.

These instruments can share customer, mandate, limit, document, fee, screening, payment and accounting services, but their states and obligations are not interchangeable. The Horizon catalogue currently groups them under `HB-PRD-09` and `HB-APP-048`; instrument-specific variants remain a governed gap.

Uniform Customs and Practice for Documentary Credits (UCP 600) guidance demonstrates why documentary-credit presentations, discrepancies and refusal or acceptance decisions need governed evidence [ICC-UCP600-GUIDANCE-2023]. UCP 600 does not apply automatically to every instrument. The instrument terms, other applicable rules and law must be verified.

## Trade-finance applications and external interaction

`HB-APP-048 Trade Finance Processing` owns accepted instrument, amendment, presentation, discrepancy, claim and closure state through `HB-SOR-13 Trade Finance Instrument Authority`. The corporate channel accesses it through `HB-INT-047 Trade Finance Service`. Contingent exposure is published to `HB-APP-030 Credit Exposure Aggregation` through `HB-INT-048 Trade Contingent Exposure Event`.

`HB-INT-073 Trade Finance Network Message` exchanges instrument and presentation information through `HB-EXT-016 Trade Finance Messaging Network`. The network record is a logical boundary only. It does not assert membership, counterparty reach or a message standard.

Documents also require content, malware, access, retention and originality controls. `HB-DATA-07 Trade Finance` holds the instrument semantics, while `HB-DATA-06 Case, Document and Evidence` covers document and decision evidence. A document repository is not the instrument authority merely because it stores a file.

Customer and transaction sanctions controls apply according to governed scope. Goods, ports, vessels and transport-document screening may also be relevant for an instrument or jurisdiction, but `HB-APP-018 Name and Sanctions Screening` does not by itself prove that this specialist coverage exists. Horizon Bank has no governed goods or vessel screening responsibility, list source or interface, so those checks remain explicit gaps rather than an implied feature of `HB-APP-048`.

## Exposure, accounting and reconciliation

Issuing or amending an undertaking can change contingent exposure before cash moves. `HB-CTRL-21 Trade Instrument Authority and Limit Control` prevents issuance, amendment, claim acceptance or financing without mandate, authority and limit evidence. `HB-INT-048` ensures exposure aggregation receives the lifecycle change.

`HB-ACC-04 Trade Contingent Obligation Recognised` represents the contingent accounting or memorandum consequence. `HB-ACC-20 Trade Finance Fee Charged` covers approved issuance, amendment, document, commitment, financing or service fees. `HB-ACC-21 Trade Finance Claim or Settlement Paid` covers accepted payment, reimbursement or financing settlement. The catalogue intentionally leaves detailed debit, credit, provisioning, tax and currency treatments pending.

Two reconciliations protect different populations:

- `HB-REC-021 Trade-Finance Contingent Obligation` compares instruments and amendments with limit, exposure and accounting records.
- `HB-REC-022 Trade-Finance Documents, Fees and Cash` compares presentation, discrepancy, fee and settlement records with the instrument and finance outcome.

Closing an instrument therefore requires more than changing an application status. The bank must resolve remaining exposure, fees, cash, claims, documents and external messages.

## Controls, resilience and exception ownership

`HB-CTRL-04 Trade Document and Discrepancy Review` requires examination evidence and an authorised acceptance or refusal. `HB-CTRL-21` protects mandate, limit and commitment decisions. Transaction screening and payment controls also apply where the approved scope requires them.

`HB-CRIT-11 Issue and Honour Trade-Finance Instruments` defines the critical business outcome. During disruption, new issuance might pause while claims and time-sensitive presentations receive priority. That decision requires instrument rules, legal time limits, customer communication and operational capacity. `HB-TECH-014 Trade Finance Classification` leaves Recovery Time Objective (RTO), Recovery Point Objective (RPO) and impact tolerance pending until those dependencies are known.

The architecture must name exception owners. Document examiners resolve discrepancies under authority. Credit Risk resolves limit exceptions. Payment Investigations resolves payment status. Reconciliation Operations owns breaks. Technology restores service but does not decide a documentary discrepancy or waive a customer obligation.

## BIAN alignment

`HB-BIAN-04 Trade Finance Responsibility Candidate` is related to `HB-PRD-09`, `HB-VS-10` and `HB-PROC-06`. Exact BIAN 14.0 objects and confidence remain pending. A useful mapping will probably be many-to-many because origination, document work, exposure, fees, payments and servicing cross several logical responsibilities.

The register has no separate governed candidate for corporate cash management. That is a shared-catalogue request, not a reason to invent a Service Domain. The application, process and capability catalogues remain valid author models while verification proceeds.

## Choosing the right models

| Model | Corporate or trade question |
|---|---|
| Party and relationship model | Which entities, owners and authorised relationships exist? |
| Mandate decision model | Who may submit, approve and release an action? |
| Account-structure model | How do physical and virtual accounts participate? |
| BPMN collaboration | How do customer, bank and external parties manage documents and exceptions? |
| State machine | Which instrument, presentation or claim states are permitted? |
| Data lineage | How do instrument, exposure, cash and accounting records connect? |
| Critical-operation dependency map | Which services and external parties must recover first? |

An account hierarchy is not a process, and a BPMN flow is not a legal-ownership model. Use complementary views and state the question each answers. No diagram source is created in this pass.

## Worked traceability: issue and settle a trade instrument

`HB-SCN-03 Issue and Settle Trade Instrument` begins when an authorised corporate customer requests a supported instrument. The channel and mandate service establish authority. `HB-APP-048` checks product, limit and approvals, then records issuance and sends the governed external message. `HB-ACC-04` and `HB-REC-021` establish traceability to contingent exposure.

A later presentation enters the document examination path. `HB-CTRL-04` preserves discrepancies and the authorised disposition. An accepted claim or financing outcome uses the payment domain for cash execution. `HB-ACC-20` or `HB-ACC-21` records the relevant financial event, and `HB-REC-022` checks documents, fees and settlement. Closure occurs only after exposure and exceptions are resolved.

The scenario leaves instrument variants, applicable ICC rules, law, message standards, time limits and document originality pending. A real implementation must resolve them per product and legal entity.

### Combined corporate scenario: bulk payments, sweep and import letter of credit

A corporate group first configures users, accounts and a two-person approval matrix in `HB-APP-010`. Its host-to-host transport remains pending, so the governed baseline uses the bulk-file operation exposed over `HB-INT-025` to `HB-APP-006`. File totals, payroll confidentiality where applicable, item-level validation and approvals must complete before accepted instructions enter the Chapter 41 payment lifecycle.

Separately, `HB-APP-047` calculates an approved physical sweep from current `HB-INT-039` balances. It sends only the authorised movement over `HB-INT-072` to `HB-APP-033`; the cash application never edits a deposit balance. A missed cut-off or stale balance pauses the sweep and creates an owned exception.

The same customer then requests an import letter of credit through the service exposed by `HB-APP-048` over `HB-INT-047`. `HB-CTRL-21` checks mandate, authority and limit. Issuance creates the contingent consequence `HB-ACC-04`, publishes exposure through `HB-INT-048` and exchanges the permitted external message through `HB-INT-073`. Later document presentation, discrepancy, acceptance or refusal, claim, cash settlement and closure follow the instrument lifecycle and `HB-REC-021` and `HB-REC-022`.

The three threads share customer and authority context but retain different state owners. Host connectivity, UCP 600 incorporation, goods or vessel screening, correspondent reach, tax, service prices and all relevant cut-offs remain decisions, not assumed facts.

## Current-to-target considerations

The principal corporate channel, cash-management and trade-finance applications are current. Improvement should begin with common corporate-party and account identifiers, central mandate decisions, governed file acceptance and explicit instrument variants rather than a single replacement programme.

A safe transition moves one service and customer cohort at a time, parallel-runs balances, approvals, fees and external messages, and reconciles open files, sweep instructions, presentations, claims and contingent exposure before authority changes. Cross-entity structures require legal and tax approval before migration. Historical instruments and documents must remain accessible until obligations, disputes and retention duties end.

## When should this model set be used?

Use it for corporate-channel design, mandate consolidation, cash-management change, trade-platform replacement, exposure integration, operations redesign and resilience planning. It makes customer authority and financial outcomes visible across domain boundaries.

Do not use it as a pooling legal opinion, tax design, instrument rulebook, credit approval or network contract. Those decisions require specialist evidence and jurisdictional review.

## Common mistakes

- Representing a corporate group as one customer row.
- Letting channel roles replace product-specific mandates.
- Treating a virtual account as an independent booked account without defining its authority.
- Moving funds directly from the cash-management calculator rather than through governed payment controls.
- Mapping trade finance to deposit acquisition.
- Closing a trade instrument while contingent exposure, claims or accounting remain open.
- Treating document storage as document examination or instrument authority.
- Inventing BIAN names, network memberships or documentary-rule deadlines.

## Key takeaways

- Corporate structure and mandate are first-class architecture concerns.
- Cash management calculates and controls services but does not replace account or payment authority.
- Cross-entity liquidity structures require explicit legal, tax and jurisdiction decisions.
- Trade finance spans the complete instrument, document, exposure, fee, claim and settlement lifecycle.
- Accounting and reconciliation make contingent and cash outcomes reviewable.
- Critical operations require business-led prioritisation of issuance, claims and document work.
- BIAN mappings stay provisional until exact 14.0 verification.

## Practical exercise

Model a corporate group with two legal entities, three accounts and a two-person payment mandate. Add one cash sweep and one documentary-credit request. Produce a traceability table that identifies the relationship, mandate, application, payment instruction, trade instrument, exposure, accounting event, reconciliation and exception owner.

**Suggested review criteria:** The answer must distinguish group from legal person, show that the sweep becomes a governed payment command, map trade finance to `HB-VS-10`, and leave legal, tax and instrument-rule assumptions explicit.

## Review checklist

- [x] Corporate structure, mandate and service authority are explicit.
- [x] Cash management and payment execution are separated.
- [x] The complete trade-finance lifecycle is covered through closure.
- [x] Applications, interfaces, information, accounting and controls use governed IDs.
- [x] Legal, tax, network and instrument-rule assumptions are not fabricated.
- [ ] Add a governed BIAN candidate for corporate cash management after 14.0 verification.
- [ ] Diagram production remains deferred pending author-approved specifications.

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14]
- [ICC-UCP600-GUIDANCE-2023]
- [CPMI-CORRESPONDENT-BANKING-2016]

## Drafting notes

- Before formal review, verify exact BIAN 14.0 candidates and obtain instrument, legal, tax and network decisions for each in-scope legal entity.
