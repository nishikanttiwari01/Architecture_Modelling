---
title: "Deposits, Accounts, Term Deposits, Interest, Fees, Statements and Correspondence"
chapter: 38
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 38. Deposits, Accounts, Term Deposits, Interest, Fees, Statements and Correspondence

## Chapter purpose

Explain the complete non-credit deposit and account lifecycle, from product selection and agreement creation through funding, balance servicing, interest, fees, statements, maturity and closure. The chapter shows how a bank keeps the customer agreement, operational account record and financial books consistent.

## Reader outcomes

By the end of this chapter, you should be able to:

- distinguish a deposit product, agreement, account, balance, posting and statement;
- model transaction accounts and term deposits without mixing them with credit facilities;
- allocate account processing, accrual, correspondence, subledger and general-ledger responsibilities;
- trace deposit events through interfaces, accounting consequences, reconciliation and controls;
- identify resilience and transition requirements for an account-processing estate.

## Prerequisites and dependencies

- Chapter 37: Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing
- Chapter 35: Enterprise Information and Data Architecture
- Chapter 36: Technology, Security, Resilience and Operating Architecture

## Required models and artefacts

This chapter uses `HB-DOM-030 Deposits and Accounts`, `HB-CAP-030 Deposit and Account Management`, `HB-PRD-01 Deposits and Accounts`, `HB-VS-03 Acquire and Service Deposit or Account` and `HB-PROC-02 Originate and Service Deposits`. Detailed records are drawn from the application, interface, data, authority, accounting, reconciliation, control, critical-operation and resilience catalogues.

The organisational trace starts with `HB-ORG-08 Retail Banking` for retail deposit outcomes and `HB-ORG-27 Product, Proposition and Pricing` for governed product terms. `HB-ORG-15 Banking Operations` performs account fulfilment and exception repair, while `HB-ORG-12 Finance, Accounting, Tax and Reporting` owns the books and financial-control responsibilities. These responsibilities meet at controlled hand-offs; none of the four organisations is the sole owner of the complete lifecycle.

No new diagram source is generated. Candidate state, process, information and accounting views remain textual until a Chapter 38 diagram specification is approved.

## Worked examples

The main example opens and services a retail transaction account. A second thread shows why a term deposit needs additional placement, maturity, rollover and early-termination states. Both are fictional Horizon Bank designs whose terms and accounting policies require legal-entity approval.

### Governed scenario traces

The worked threads use two catalogue scenarios rather than an unnamed generic account journey:

| Scenario | Outcome trace used in this chapter |
|---|---|
| `HB-SCN-04 Open and Fund a Transaction Account` | Product `HB-PRD-02`; value stream `HB-VS-03`; process `HB-PROC-02`; application `HB-APP-020`; authority `HB-SOR-02`; interface `HB-INT-019`; event `HB-ACC-05`; reconciliation `HB-REC-003`; control `HB-CTRL-08`; critical operation `HB-CRIT-01`; classification `HB-TECH-005` |
| `HB-SCN-05 Place, Accrue and Mature a Term Deposit` | Product `HB-PRD-03`; value stream `HB-VS-03`; process `HB-PROC-02`; application `HB-APP-021`; authority `HB-SOR-02`; interface `HB-INT-028`; event `HB-ACC-01`; reconciliation `HB-REC-004`; control `HB-CTRL-09`; classification `HB-TECH-005` |

The entries are architectural traceability fields, not a single runtime sequence. The transaction-account thread tests agreement creation, initial funding and account-to-ledger consistency. The term-deposit thread adds rate agreement, accrual, maturity instruction and early-break or rollover exceptions.

## Source requirements

This is primarily a governed case-study design. It does not prescribe deposit-insurance eligibility, disclosure wording, tax treatment, interest conventions or consumer rules. Those matters depend on jurisdiction and product contract. Banking Industry Architecture Network (BIAN) mappings remain candidates under Service Landscape 14.0. [BIAN-SERVICE-LANDSCAPE-14]

## Planned chapter structure

The chapter follows the lifecycle from product definition to closure, then connects it to applications, information, accounting, controls and operations.

## A deposit is both a customer service and a bank obligation

A customer sees an account that can receive funds, show balances, support payments and provide statements. The bank must also maintain a contract, control who may act, calculate interest and fees, preserve an ordered transaction record, recognise financial consequences and reconcile its books.

The central modelling question is: **how does an approved deposit agreement remain operationally and financially correct throughout its life?** That question is broader than opening a current account and narrower than the complete customer relationship.

Decision `DEC-029` separates `HB-VS-03 Acquire and Service Deposit or Account` from `HB-VS-05 Provide and Manage Credit`. A deposit account can support payment execution through `HB-VS-04`, but it is not therefore a credit facility. An overdraft, if offered, would need an explicit credit agreement and exposure relationship rather than being hidden inside the deposit record.

## Product, agreement and account

The governed product family is `HB-PRD-01 Deposits and Accounts`. `HB-PRD-02 Transaction Account` supports day-to-day balance and payment services. `HB-PRD-03 Term Deposit` represents a time-bound placement with governed interest conditions.

These terms answer different questions:

| Concept | Question answered | Example authority |
|---|---|---|
| Product | What can the bank offer under approved terms? | `HB-APP-013 Enterprise Product Catalogue` |
| Price plan | Which rates, fees, bands and effective dates apply? | `HB-APP-014 Pricing and Fee Management` |
| Agreement | What did this customer and legal entity contract to? | Product and agreement authority in `HB-DATA-02` |
| Account | Where is the agreement serviced and its operational state maintained? | `HB-APP-020 Deposit Account Processing` |
| Posting | What accepted financial movement changed the account? | Ordered account journal in `HB-APP-020` |
| Statement | What governed account activity was communicated for a period? | `HB-APP-022 Statement and Correspondence Management` |

A product definition can change prospectively without rewriting existing agreements. A price may be variable, fixed for a period or customer-specific. The booked agreement therefore needs a version or effective-dated reference to the terms actually applied.

## Account opening process

The opening process begins only when the customer and product context is understood. Its main stages are:

1. identify the customer, legal entity, segment and requested product;
2. retrieve the effective product definition and eligibility rules;
3. confirm relationship, Know Your Customer (KYC) status, consent, mandate and signatories;
4. evaluate product eligibility and permitted exceptions;
5. present and accept the applicable terms;
6. establish the agreement and account with a unique identifier;
7. configure mandate, channel access, limits or restrictions;
8. accept or await initial funding where required;
9. activate the account only after fulfilment controls complete;
10. notify the customer and hand the account to normal servicing.

A Business Process Model and Notation (BPMN) model should show referred, abandoned, duplicate, failed-fulfilment and delayed-funding outcomes. It should also show which work belongs to customer onboarding and which belongs to account fulfilment. Repeating all KYC work inside every product process creates inconsistent decisions and poor customer experience.

`HB-CAP-031 Deposit Account Opening` owns the account-establishment ability. It depends on `HB-CAP-024 Product Eligibility Management`, `HB-CAP-038 Mandate and Signatory Management`, `HB-CAP-013 Customer Onboarding` and `HB-CAP-149 Operational Control Evidence Management`.

## Eligibility is a governed decision

Eligibility answers whether a defined product can be offered to this customer, through this channel and legal entity, at this time. It is not the same as CDD approval, and it is not the same as a credit decision.

A Decision Model and Notation (DMN) model can combine approved inputs such as segment, age or organisation type, residency, channel, relationship status and product availability. The result might be `Eligible`, `Refer` or `Not eligible`, with reasons. Product owners govern the rule. Customer and compliance functions provide source facts and constraints.

`HB-CTRL-07 Product and Price Approval` prevents sale of an unauthorised definition or price. The decision evidence should record product version, rule version, input references, outcome, effective time and any approved exception.

## Account lifecycle and state

A state model answers **which account conditions are meaningful and which transitions are permitted?** A useful conceptual lifecycle is:

```text
Pending fulfilment
-> Awaiting funding, when applicable
-> Active
-> Restricted or Dormant, when governed conditions apply
-> Closing
-> Closed
-> Retained record
```

Suspension, restriction and dormancy should not be treated as synonyms. Each state needs allowed transactions, customer visibility, approval authority and exit conditions. A closure request cannot erase unresolved postings, accrued interest, fees, holds, disputes or retention duties.

For a term deposit, `HB-CAP-036 Term Deposit Administration` adds placement, fixed or governed rate conditions, maturity instruction, rollover, repayment and possible early termination. A rollover is not merely changing a date. It may create a new agreement version, price and accounting period.

## Application architecture

The logical estate deliberately separates stable responsibilities:

| Application | Deposit responsibility |
|---|---|
| `HB-APP-002 Retail Mobile Banking` | Customer self-service and instruction capture |
| `HB-APP-003 Branch Service Workbench` | Assisted opening and maintenance |
| `HB-APP-010 Customer Entitlement and Mandate Service` | Account-action and mandate decisions |
| `HB-APP-013 Enterprise Product Catalogue` | Approved product and eligibility definitions |
| `HB-APP-014 Pricing and Fee Management` | Effective rates, fees and waivers |
| `HB-APP-020 Deposit Account Processing` | Account state, balances, holds and booked postings |
| `HB-APP-021 Interest and Fee Accrual` | Scheduled calculations and accrual results |
| `HB-APP-022 Statement and Correspondence Management` | Reproducible statements and notices |
| `HB-APP-058 Product Subledger Platform` | Product-level accounting positions |
| `HB-APP-059 General Ledger` | Approved legal-entity books |
| `HB-APP-060 Enterprise Reconciliation` | Matching and break management |
| `HB-APP-073 Notification and Communications Hub` | Delivery through approved channels |

This is not an argument for eleven purchased products. Some responsibilities may share a platform. The logical boundaries remain valuable because `HB-APP-020` can be authoritative for booked account state while `HB-APP-059` is authoritative for the legal-entity general ledger. Combining the boxes on a deployment diagram would not combine their accounting responsibilities.

## Interfaces and event behaviour

`HB-INT-019 Deposit Price Retrieval` supplies applicable rate and fee rules from pricing to account processing. The booked account needs enough information to reproduce why a rate or charge applied. A later price change must not silently alter historical calculations.

`HB-INT-027 Funds and Account Control` exposes account state, available funds, reservations and posting results to transaction execution. The design must define the atomicity boundary. A payment orchestrator cannot assume a successful balance enquiry also guarantees a later posting.

`HB-INT-028 Deposit Accrual Event` publishes completed interest and fee calculations. It needs a stable business-event identifier, period, calculation version, correction semantics and duplicate handling. Delivery more than once must not create more than one financial effect.

`HB-INT-052 Customer Communication Request` and `HB-INT-094 Communication Delivery Event` separate creation of an approved communication from its delivery status. In the governed interface catalogue, `HB-APP-073 Notification and Communications Hub` produces `HB-INT-094` for `HB-APP-004 Contact Centre Workbench`; the event is not a generic broadcast to every service channel. A delivered message is not proof that the customer read or agreed to a change.

Batch remains important. Interest runs, statements, product-subledger aggregation and general-ledger posting may be scheduled work. `HB-APP-079 Enterprise Batch Scheduler` records dependencies and execution status, while the domain applications remain responsible for business completeness and restart behaviour.

## Data model and authority

`HB-SOR-02 Deposit Account Authority` assigns qualified authority for deposit account state, balances, holds and accepted postings to `HB-APP-020`. Pending payment instructions are not booked account postings. General-ledger balances remain separately authoritative in `HB-SOR-04`.

The conceptual account model includes:

```text
Product Definition -> Agreement -> Deposit Account
Party -> Account Role -> Deposit Account
Deposit Account -> Balance Type
Deposit Account -> Hold or Reservation
Deposit Account -> Posting
Agreement -> Price Plan Snapshot or Effective Reference
Deposit Account -> Statement Period -> Statement
```

Balance types need names and definitions. `Booked balance`, `available balance`, `held amount` and `accrued interest` can differ. The model must state currency, effective time and source. A single field called `balance` is not sufficient for payment, statement and accounting use.

## Interest, fees and correspondence

`HB-CAP-034 Deposit Interest Management` covers accrual, capitalisation, posting and correction. Inputs can include balance populations, rates, day-count conventions, value dates, tiers and tax treatment. This chapter does not prescribe those rules. It requires them to be versioned, approved and reproducible.

`HB-CAP-035 Account Fee and Charge Management` distinguishes assessment, waiver, posting, reversal and refund. A waiver is a governed commercial decision, not deletion of an accounting record. `HB-CTRL-09 Deposit Interest and Fee Calculation` expects the product version, calculation inputs, output, exceptions and posting totals.

`HB-CAP-037 Statement and Account Correspondence Management` covers generation, delivery and retention. `HB-CTRL-43 Customer Statement and Communication Completeness` checks that governed source transactions, balances, terms and notices are represented. `HB-REC-006 Customer Statement Completeness` compares the source population with the produced communication.

## Accounting events and reconciliation

Accounting begins with a governed business event, not with a user-interface status. Horizon Bank defines these deposit events:

- `HB-ACC-05 Deposit Principal Received`;
- `HB-ACC-06 Deposit Principal Withdrawn or Repaid`;
- `HB-ACC-01 Deposit Interest Accrued`;
- `HB-ACC-07 Deposit Fee Charged`.

The catalogue states expected consequences but deliberately leaves detailed debit, credit, day-count, tax, reversal and subledger rules pending. That is appropriate. The applicable accounting framework, product contract and legal entity must determine the posting rules.

Three different comparisons are needed:

| Reconciliation | Question |
|---|---|
| `HB-REC-003 Deposit Account to Product Subledger` | Do account postings and principal agree with product accounting? |
| `HB-REC-004 Deposit Interest Accrual` | Do rates, balances and calculations agree with accrual events and postings? |
| `HB-REC-005 Deposit Fees and Charges` | Do assessments, waivers, refunds and postings agree with fee income? |

`HB-CTRL-03 Ledger Reconciliation` governs completeness and unresolved breaks. A reconciliation application may identify a difference, but it must not silently correct `HB-APP-020`, `HB-APP-058` or `HB-APP-059`. Correction uses authorised domain and accounting processes.

## Controls and operational handling

`HB-CTRL-08 Deposit Posting and Available-Funds Control` protects account state, holds and posting order. Expected evidence includes the instruction, balance before and after, hold decision, sequence and failure outcome. Important exceptions include duplicate requests, backdating, reversals, offline capture and insufficient funds.

`HB-CTRL-06 Consent, Mandate and Entitlement Enforcement` protects who may act. `HB-CTRL-07` protects product and price publication. `HB-CTRL-09` protects calculations. `HB-CTRL-43` protects statements and material communications. Together they show why one generic `account validation` control is too vague.

Operational work includes returned communications, deceased-customer handling, disputed postings, account restrictions, unclaimed funds, failed interest runs and closure breaks. Exact procedures depend on jurisdiction. The architecture must name the case owner and evidence even when detailed policy remains pending.

## Resilience and critical operations

`HB-TECH-005 Deposit and Account Servicing Classification` classifies account processing as direct support for a critical operation. `HB-CRIT-01 Access Funds and Account Information` protects the customer outcome, while `HB-CRIT-04 Maintain Deposit Account Posting Integrity` protects the ordered and recoverable financial record.

A degraded channel may provide a qualified read-only balance or queue an instruction, but only if authority, staleness, customer communication and later reconciliation are defined. An off-system spreadsheet must not become an ungoverned balance authority.

Recovery design must preserve:

- accepted instruction and posting identifiers;
- posting order and duplicate decisions;
- balances, holds and restrictions;
- product and price versions;
- incomplete accrual and batch checkpoints;
- reconciliation populations and unresolved breaks;
- notification and statement status.

Recovery Time Objective (RTO) and Recovery Point Objective (RPO) values remain pending. The chapter does not fabricate them.

## BIAN candidate mapping

`HB-BIAN-01 Deposit Responsibility Candidate` links `HB-PRD-01` and `HB-VS-03` to a candidate BIAN mapping. Its exact BIAN 14.0 objects and confidence remain pending. This is an honest traceability state.

The candidate should eventually map distinct responsibilities for product definition, agreement, account fulfilment, position, interest, fees and service, where BIAN 14.0 supports them. It must not imply that `HB-APP-020`, `HB-APP-021` and `HB-APP-022` each equal one Service Domain or must be microservices.

## Current, transition and target considerations

The current author model may contain product silos and point-to-point interfaces. A target direction uses a governed product catalogue, explicit account authority and managed application programming interfaces (APIs), events and batch. Migration should proceed by product and legal entity, with reconciliation before authority changes.

A safe transition can:

1. inventory products, agreement variants and posting types;
2. define common account and balance semantics;
3. establish price-version and product-publication governance;
4. introduce managed interfaces around the current processor;
5. publish complete accounting-event populations;
6. reconcile current and target subledger results in parallel;
7. migrate accounts in controlled cohorts with rollback or repair criteria;
8. retain legacy access until statements, disputes and retention obligations are resolved.

Replacing the customer channel while leaving undocumented posting behaviour unchanged is not deposit modernisation.

## Common mistakes

- Treating a product, agreement and account as the same object.
- Using `facility` for both a deposit account and a credit commitment.
- Keeping only one undefined balance value.
- Recalculating historical interest with today's product rule.
- Treating a published event as proof that accounting posted successfully.
- Allowing reconciliation tooling to alter authoritative records without approval.
- Treating statement generation and message delivery as one status.
- Setting one recovery target for channels, account processing, statements and analytics without impact analysis.

## Chapter summary

Deposit architecture joins customer service to a controlled financial record. Product, price, agreement, account, posting, accounting event and statement each have a distinct meaning and authority. Horizon Bank uses explicit applications, interfaces, controls and reconciliations so the operational account and financial books can be explained and repaired.

## Completion checklist

- [x] Transaction accounts and term deposits are covered across their lifecycle.
- [x] Deposits remain separate from the credit value stream.
- [x] Product, agreement, account, balance, posting and statement are distinguished.
- [x] Applications, interfaces, accounting, controls, reconciliations and resilience use governed IDs.
- [x] BIAN mapping remains a versioned candidate rather than an application prescription.
- [x] Jurisdiction rules, quantitative targets and journal details remain explicit gaps.

## Key takeaways

- A deposit account is a customer service, contract and controlled financial obligation.
- Account processing, accrual, correspondence and financial books have different responsibilities.
- Effective-dated product and price rules are necessary for reproducible servicing.
- Events require correction and duplicate semantics before they can drive accounting.
- Reconciliation detects differences; authorised domain processes correct them.
- Resilience protects posting integrity and customer outcomes, not only application uptime.

## Practical exercise

Extend `HB-PRD-03 Term Deposit` with a fictional 12-month variant. Define its agreement attributes, lifecycle states, maturity choices, early-termination referral, interest event, customer communication and reconciliations. Use only existing governed IDs and label all new variant details as proposed.

A strong answer identifies which product and price versions are booked, how maturity differs from closure, what happens after a failed accrual run and why no BIAN-to-application equivalence is assumed.

## Review checklist

- [ ] Does the model separate customer relationship, product agreement and operational account?
- [ ] Are balance meanings, currencies and effective times explicit?
- [ ] Are eligibility, KYC and access-authorisation decisions kept separate?
- [ ] Are interest, fee, waiver, reversal and correction paths governed?
- [ ] Can each accounting event be traced to a source event and reconciliation?
- [ ] Are statement creation, delivery and reissue represented separately?
- [ ] Does recovery preserve posting order, duplicate safety and unfinished batches?
- [ ] Are jurisdiction, policy and numerical gaps visible?

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14](../../research/bian/bian-service-landscape-14.0.md)

## Drafting notes

- Exact deposit BIAN 14.0 object mappings and confidence remain pending in `HB-BIAN-01`.
- Deposit product variants, country rules and accounting policies require later governed expansion.
