---
title: "Enterprise Information and Data Architecture"
chapter: 35
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 35. Enterprise Information and Data Architecture

## Chapter purpose

Establish Horizon Bank's bank-wide information concepts, authority decisions and data movement before the domain chapters add detail. The chapter connects operational facts to accounting, reconciliation, risk, analytics and reporting without treating one data platform as authoritative for everything.

## Reader outcomes

By the end of this chapter, you should be able to:

- distinguish conceptual, logical and physical data models;
- navigate the bank's 20 governed data domains and 25 qualified authority decisions;
- distinguish a source record, working copy, authoritative record, consolidated view and analytical publication;
- qualify authority by purpose, lifecycle, legal entity and effective time;
- trace operational information through accounting, reconciliation, analytics and reporting;
- review identifiers, provenance, quality, protection, retention and correction paths;
- explain why the BIAN Business Object Model can inform semantic comparison but is not a physical bank database design.

## Prerequisites and dependencies

- Chapter 34: Full Bank Application and Integration Landscape
- The governed Horizon Bank data-domain, system-of-record, accounting-event and reconciliation catalogues

## Required models and artefacts

This chapter uses `data-domains.md`, `systems-of-record.md`, `applications.md`, `interfaces.md`, `accounting-events.md`, `reconciliations.md`, `controls.md` and the master coverage matrix.

`FIG-35-01 Horizon Bank data-domain and authority map` is registered and specified. Diagram source is deferred because the specification has not been approved by the author.

## Worked examples

- Deposit-interest lineage from governed terms and balances to customer communication and the general ledger
- Cross-border-payment lineage from instruction through settlement, accounting, reconciliation and reporting

## Source requirements

BCBS 239 supplies an official reference for governance, data architecture, aggregation, risk reporting, reconciliation and validation. Its original scope is not assumed for every fictional Horizon Bank entity. [BCBS-239]

World Wide Web Consortium (W3C) provenance concepts support the distinction between an entity, the activity that produced or transformed it, and the responsible agent. This chapter uses the general provenance idea, not the full PROV notation. [W3C-PROV-DM-2013]

BIAN 14.0 supplies versioned reference semantics. Horizon Bank remains accountable for its local concepts, authority and physical implementation. [BIAN-SERVICE-LANDSCAPE-14]

## Planned chapter structure

The chapter moves from meaning and model level to authority, movement, quality, control and two end-to-end information traces.

## Data architecture is an accountability model

Bank data represents identity, rights, obligations, transactions, balances, positions, decisions and evidence. If the meaning or authority is wrong, technically successful processing can still produce a customer, financial, risk or regulatory error.

The primary architecture question is: **what information does the bank govern, which responsibility may establish it for a stated purpose, and how can later use be traced back to that authority?** Storage products matter later. Meaning, ownership and lifecycle come first.

### Three model levels answer different questions

A **conceptual data model** identifies important business concepts and relationships. It can show that a party holds a role in an agreement, that an account records balances, and that a payment instruction progresses through processing and settlement.

A **logical data model** adds identifiers, attributes, cardinality, optionality, lifecycle states and rules without committing to a database technology. It can distinguish one party from several customer relationships or one trade instrument from several amendments and document presentations.

A **physical data model** describes implementation structures such as tables, indexes, event schemas, message fields, files and retention partitions. It is specific enough to build or configure.

Moving directly from an enterprise noun to a physical table hides meaning and ownership. Conversely, a conceptual model is insufficient for proving uniqueness, effective dating or message compatibility. The levels complement one another.

## The 20 governed data domains

A data domain groups related information by business meaning and accountability. It is not automatically a database, application, bounded context or organisational unit. Horizon Bank's full-bank baseline is:

| Group | Governed data domains |
|---|---|
| Customer, product and interaction | `HB-DATA-01 Party and Customer`; `HB-DATA-02 Product and Agreement`; `HB-DATA-20 Customer Interaction and Communication` |
| Accounts and transactions | `HB-DATA-03 Account and Transaction`; `HB-DATA-08 Payments, Clearing and Settlement`; `HB-DATA-09 Cards and Merchant Acquiring` |
| Credit and trade | `HB-DATA-04 Credit and Collateral`; `HB-DATA-07 Trade Finance` |
| Wealth, securities and treasury | `HB-DATA-10 Wealth, Advice and Portfolio`; `HB-DATA-11 Securities, Custody and Asset Servicing`; `HB-DATA-12 Treasury, Markets, Funding, Liquidity and Capital` |
| Finance, risk and reporting | `HB-DATA-05 Finance and Accounting`; `HB-DATA-13 Enterprise Risk and Models`; `HB-DATA-16 Regulatory, Statutory, Tax and Management Reporting` |
| Compliance and evidence | `HB-DATA-06 Case, Document and Evidence`; `HB-DATA-14 Compliance, Financial Crime and Fraud` |
| Shared reference and enterprise information | `HB-DATA-15 Reference and Market Data`; `HB-DATA-17 Workforce, Supplier and Facilities` |
| Technology and security | `HB-DATA-18 Technology Service, Configuration and Observability`; `HB-DATA-19 Security, Identity and Access` |

The first seven records were the preliminary foundation. The expanded baseline separates payments, cards, wealth, securities, treasury, risk, compliance, reference data, reporting, enterprise support, technology, security and customer interactions. This matters because a generic `Transaction` or `Case` domain is too broad to allocate authority and control for a full-service bank.

### Key conceptual distinctions

Several terms that appear similar have different lifecycles:

- A **party** is a person or organisation. A **customer** is a party in a governed relationship with a legal entity.
- A **product definition** describes an approved offering. An **agreement** records the terms accepted for a particular relationship.
- An **account** records a governed product or settlement position. A **balance** is a value at a time under stated inclusion rules.
- An **instruction** requests an action. A **transaction** records processing. **Settlement** discharges or changes an obligation under the applicable arrangement.
- A **case** coordinates work and evidence. It does not become authoritative for every business fact referenced in the case.
- An **accounting event** states a recognised financial consequence. It is not every technical event on the event platform.

These distinctions give later chapters a stable language. They also prevent one enormous canonical schema from absorbing incompatible meanings.

## Information categories can overlap

Master data identifies relatively persistent subjects such as parties and products. Reference data supplies governed classifications such as currencies, calendars and instrument codes. Transactional data records business activity and state changes. Event data communicates facts. Analytical data is organised for measurement and decision support. Documents preserve content and evidence.

One information item can participate in more than one category without losing its authority. A signed trade-finance document is retained content in `HB-DATA-06`, evidence for an instrument in `HB-DATA-07`, and an input to a control decision. Extracted fields do not automatically become authoritative merely because they are easier to query.

## Authority must be qualified

The phrase **system of record** is useful only when the record says what is authoritative, at which lifecycle stage, for which legal entity, under what conditions and from what effective time. Horizon Bank records these decisions separately from application names.

The 25 authority records are organised as follows:

| Authority area | Governed records |
|---|---|
| Customer, product and onboarding | `HB-SOR-01 Party Identity Authority`; `HB-SOR-05 Product Definition and Price Authority`; `HB-SOR-06 Consent and Preference Authority`; `HB-SOR-07 Onboarding and Due-Diligence Case Authority` |
| Deposits and credit | `HB-SOR-02 Deposit Account Authority`; `HB-SOR-03 Credit Exposure Authority` |
| Payments, cards and merchants | `HB-SOR-08 Payment Instruction and Processing Authority`; `HB-SOR-09 Settlement and Correspondent Position Authority`; `HB-SOR-10 Card Product and Credential Authority`; `HB-SOR-11 Card Authorisation and Clearing Authority`; `HB-SOR-12 Merchant and Acquiring Authority` |
| Trade, wealth, securities and treasury | `HB-SOR-13 Trade Finance Instrument Authority`; `HB-SOR-14 Wealth Mandate and Portfolio Authority`; `HB-SOR-15 Investment Order Authority`; `HB-SOR-16 Custody Holding Authority`; `HB-SOR-17 Corporate Action and Entitlement Authority`; `HB-SOR-18 Treasury Trade and Position Authority` |
| Finance, risk and control | `HB-SOR-04 General Ledger Authority`; `HB-SOR-19 Enterprise Risk Position Authority`; `HB-SOR-20 Financial-Crime and Fraud Case Authority`; `HB-SOR-22 Reconciliation Break Authority` |
| Records and reporting | `HB-SOR-21 Enterprise Document and Record Authority`; `HB-SOR-23 Tax Position and Filing Authority`; `HB-SOR-24 Regulatory Return Authority` |
| Technology | `HB-SOR-25 Technology Service and Configuration Authority` |

### Authority can move during a lifecycle

`HB-SOR-08` illustrates lifecycle-qualified authority. `HB-APP-033 Payment Initiation Service` is authoritative for instruction content before acceptance. `HB-APP-034 Payment Orchestration` becomes authoritative for governed execution status. `HB-SOR-09` then assigns settlement and correspondent-position authority to `HB-APP-036 Settlement and Nostro Management` and `HB-APP-038 Correspondent Banking Management` under their stated conditions.

No conflict exists if the boundaries are explicit. A conflict arises when two applications claim the same attribute, purpose, legal entity and effective time, or when neither is authorised to establish it.

`HB-SOR-22 Reconciliation Break Authority` is intentionally narrow. `HB-APP-060 Enterprise Reconciliation` owns the comparison result, break state, assignment and evidence. It does not gain authority to alter a customer account, payment, custody position or ledger. Correction returns to the relevant domain authority with approval and traceability.

### Source, authoritative record and consolidated view

A **source record** is where an item first enters or is generated for a particular occurrence. An **authoritative record** is the record accepted for a defined purpose and lifecycle. A **consolidated view** combines qualified values from several sources. An **analytical publication** applies governed transformation for a stated decision or report.

`HB-APP-080 Operational Data Store` and `HB-APP-081 Enterprise Analytical Data Platform` hold derived copies. They do not replace operational authorities. `HB-APP-082 Regulatory Data Platform` can be authoritative for a governed dataset prepared for a return, while `HB-SOR-24` makes `HB-APP-062 Regulatory Reporting` authoritative for the approved submitted return version. The underlying customer, transaction and ledger records retain their own authority.

## Identifiers, time and provenance

Identifiers need an issuer, scope, uniqueness rule, lifecycle and resolution method. A legal-entity ID, party ID, customer-relationship ID, agreement ID, account ID, payment ID, settlement reference and journal ID answer different questions. Reusing an account number as the universal key obscures role, privacy and lifecycle differences.

Cross-reference management links identifiers without overwriting their origin. A corrected party record should retain which value supported an earlier due-diligence decision. A rebooked payment should link the original instruction, rejected or returned attempt, corrected instruction and accounting consequences.

Effective time answers when a fact applies in the business. Recording time answers when the bank captured it. Processing time answers when a system acted on it. Reporting cut-off establishes which version entered an approved view. These times can differ, especially for late adjustments and externally received events.

Provenance connects an information entity to the activity that created or transformed it and the accountable agent. A useful lineage record therefore states more than `source A flows to report B`. It records source version, transformation, rule or model version, adjustment, approver and use. [W3C-PROV-DM-2013]

## Data ownership and stewardship

A data owner is accountable for meaning, permitted use, quality and decision rights. A steward maintains definitions, classifications and quality practices. An application service owner operates the logical service. A producer creates information, while a consumer uses it under a contract.

These roles should not be collapsed. The Customer Data Owner governs `HB-DATA-01`; the service owner of `HB-APP-015 Party Master and Customer Information` operates the logical application; onboarding and screening applications produce evidence; channels consume governed attributes. One team can hold several roles, but each accountability remains reviewable.

A business term needs a definition, owner, permitted values, synonyms, related concepts and source. Terms such as `party`, `customer`, `client`, `account holder`, `beneficial owner` and `authorised signatory` must be distinguished rather than reconciled by spelling alone.

## Quality, metadata and lineage services

`HB-APP-083 Metadata and Data Lineage Platform` is authoritative for governed metadata and lineage records within its scope. `HB-APP-084 Data Quality Management` holds rule definitions, measurement results, issues and remediation tracking. Their `HB-INT-095 Data Quality Metadata Exchange` connects definitions and results.

A data-quality rule should state:

- the population and data element;
- the dimension being assessed, such as validity, completeness, uniqueness, consistency or timeliness;
- the measurement point and effective time;
- the owner and permitted threshold or severity;
- the action, exception route and retained evidence.

The catalogue does not invent thresholds. A target such as 99.9 per cent complete is meaningless without population, cut-off, exclusions, materiality and approval.

BCBS 239 connects governance, architecture and infrastructure, aggregation and reporting. It also supports reconciliation and validation of risk reports. Horizon Bank uses that discipline across its model while retaining an explicit gap for jurisdiction and entity applicability. [BCBS-239]

## Accounting events are part of information architecture

Financial consequence is not an afterthought. Horizon Bank records 30 accounting-event types, from `HB-ACC-01 Deposit Interest Accrued` and `HB-ACC-14 Payment Settlement Recognised` to `HB-ACC-30 Suspense Item Established or Released`.

An accounting-event record identifies the triggering business state, debit and credit consequence at a conceptual level, timing, owner and relationships. It does not replace approved accounting policy, chart-of-accounts mapping or ledger configuration. The same business lifecycle may produce several events, reversals and adjustments.

`HB-APP-058 Product Subledger Platform` records governed product-level accounting. `HB-APP-059 General Ledger` maintains approved legal-entity journals and balances under `HB-SOR-04`. `HB-INT-082 Subledger Journal Batch` connects the two in the current logical catalogue. Manual journals remain subject to `HB-CTRL-29 Manual Journal and Adjustment Approval` rather than bypassing source gaps.

## Reconciliation is a controlled comparison

The reconciliation catalogue contains 38 defined comparisons. It spans party and account alignment, deposits, credit, payments, cards, trade finance, investments, custody, treasury, finance, reporting, financial crime, suspense, cash devices and enterprise payments.

Reconciliation asks whether two independently meaningful populations agree under a governed rule. A break can reveal timing, missing data, duplication, classification or a genuine financial difference. The comparison does not decide automatically which source is correct.

Every reconciliation needs:

- named source populations and cut-off;
- keys, tolerances and rule version;
- completeness controls and control totals;
- break owner, ageing and escalation;
- correction authority and evidence;
- rerun or certification outcome.

`HB-REC-030 Subledger to General Ledger` protects the accounting boundary. `HB-REC-033 Regulatory Report to Governed Source` protects report lineage. `HB-REC-035 Financial-Crime Case to Source Evidence` protects investigation traceability. They are different control objectives and should not be compressed into one generic data-quality check.

## Worked lineage: deposit interest

The deposit product and approved price plan are governed under `HB-SOR-05 Product Definition and Price Authority`, supported by `HB-APP-013 Enterprise Product Catalogue` and `HB-APP-014 Pricing and Fee Management`. `HB-INT-019 Deposit Price Retrieval` supplies the approved price plan to `HB-APP-020 Deposit Account Processing`.

`HB-APP-020` is the logical authority for deposit account state and booked balance under `HB-SOR-02`. `HB-APP-021 Interest and Fee Accrual` calculates scheduled results. It emits `HB-INT-028 Deposit Accrual Event` through `HB-APP-076 Enterprise Event Streaming Platform`; the platform carries the event but does not own its meaning.

The business consequence is `HB-ACC-01 Deposit Interest Accrued`. `HB-REC-004 Deposit Interest Accrual` compares calculation inputs, event populations and subledger postings. Product accounting enters `HB-APP-058`, reaches `HB-APP-059` through `HB-INT-082`, and is compared by `HB-REC-030`.

Customer communication uses `HB-APP-022 Statement and Correspondence Management`, with completeness checked by `HB-REC-006 Customer Statement Completeness` and `HB-CTRL-43 Customer Statement and Communication Completeness`.

The current interface catalogue does not yet contain every event consumer between `HB-APP-076` and product accounting. The architecture records that gap rather than inventing a connection. Chapter 38 expands deposit behaviour and Chapter 46 expands accounting and close.

## Worked lineage: cross-border payment

The core information sits in `HB-DATA-08 Payments, Clearing and Settlement`, with party, agreement and account references from `HB-DATA-01`, `HB-DATA-02` and `HB-DATA-03`. A foreign-exchange leg also uses `HB-DATA-12 Treasury, Markets, Funding, Liquidity and Capital` and governed reference data from `HB-DATA-15`.

The authority moves from `HB-SOR-08 Payment Instruction and Processing Authority` to `HB-SOR-09 Settlement and Correspondent Position Authority` as the instruction is accepted, routed and settled. The primary logical applications are `HB-APP-033`, `HB-APP-034`, `HB-APP-035`, `HB-APP-036`, `HB-APP-038` and `HB-APP-039`.

Financial consequences can include `HB-ACC-03 Payment Fee Charged`, `HB-ACC-14 Payment Settlement Recognised`, `HB-ACC-15 Correspondent Fee and Charge Recognised` and `HB-ACC-16 Foreign-Exchange Deal Recognised`. The exact set depends on the product, route, legal entity and outcome.

The control chain includes:

- `HB-REC-012 Payment Instruction to Processing Status`;
- `HB-REC-013 Payment Clearing Submission and Response`;
- `HB-REC-014 Settlement Account and Payment Ledger`;
- `HB-REC-015 Correspondent Cash and Nostro`;
- `HB-REC-016 Foreign-Exchange Trade and Settlement`.

Risk, management and regulatory use should follow governed extracts to `HB-APP-081`, `HB-APP-082`, `HB-APP-063` or `HB-APP-062`. Their transformed outputs retain source lineage and adjustments. They do not become the original payment or settlement authority.

## Protection, retention and permitted use

The interface catalogue uses `Internal`, `Confidential` and `Restricted` security classifications. Data-domain descriptions also identify sensitivity in business terms. Classification influences access, encryption, masking, monitoring, sharing and operational repair.

`HB-CTRL-36 Privacy, Retention and Legal-Hold Enforcement` governs purpose, access, retention, deletion and holds. `HB-SOR-21 Enterprise Document and Record Authority` qualifies the role of `HB-APP-070`. A retained document can prove which information supported a decision without replacing the current operational fact.

Residency and cross-border transfer decisions require dataset, purpose, legal entity, jurisdiction and provider evidence. The `Cross-border` value in a catalogue identifies scope; it does not prove legal permission.

Derived and inferred data also need governance. A model score is not an authoritative identity fact. A machine-generated summary must not silently overwrite a case record. Training, validation and production datasets need reproducible lineage and accountable use.

## BIAN information concepts and local models

The BIAN Business Object Model can help compare banking terms and interfaces. It remains a semantic reference, not a ready-made Horizon Bank physical schema. Exact BIAN objects must be verified against version 14.0 before the book names them. [BIAN-SERVICE-LANDSCAPE-14]

A useful trace is:

```text
Horizon Bank business concept and owner
-> governed data domain
-> lifecycle-qualified authority
-> local logical model and contract
-> candidate BIAN semantic mapping
-> physical schema or message implementation
```

Chapter 49 governs the candidate mapping. Chapter 51 governs interface contracts. Domain chapters 37 to 48 apply the authority model to customer, deposit, credit, payment, card, trade, wealth, treasury, finance and control lifecycles.

## Current, transition and target considerations

The current author model contains duplicate customer data, product silos and point-to-point exchanges. The target direction introduces qualified party authority, governed product and price authority, managed interface contracts, richer metadata, data-quality control and traceable analytical use.

A safe transition identifies attribute groups, legal entities, effective dates, reconciliation and correction paths. It may publish a consolidated view before moving write authority. It may run two processors while batches migrate. It must define which record controls the business decision at every step.

Copying data into a new platform is not migration completion. Completion requires approved population, transformed meaning, reconciled totals, exception resolution, retained provenance, consumer cutover and retirement of the old authority or explicit coexistence.

## Common mistakes

- Naming an enterprise data platform as the source of truth for everything.
- Assigning authority to a whole application without information or lifecycle scope.
- Treating a golden record as permission to erase source history.
- Using one identifier for party, customer, agreement and account.
- Drawing lineage without transformations, adjustments, approvers or rejected records.
- Treating every technical event as an accounting event.
- Allowing reconciliation to alter an authoritative source without domain approval.
- Copying BIAN information concepts directly into physical tables.
- Using `Cross-border` scope as evidence that transfer is permitted.

## Chapter summary

Horizon Bank's information architecture governs 20 data domains and 25 lifecycle-qualified authority decisions. Operational facts remain separate from working copies, consolidated views, accounting records and analytical publications. Identifiers, effective time, provenance, quality, accounting, reconciliation, protection and correction make the architecture reviewable from customer event to report.

## Completion checklist

- [x] All 20 governed data domains are represented.
- [x] All 25 authority records are represented and authority is qualified.
- [x] Conceptual, logical and physical models are distinguished.
- [x] Operational, accounting, reconciliation, analytical and reporting responsibilities are connected.
- [x] Deposit-interest and cross-border-payment lineages use governed IDs.
- [x] Identifiers, effective time, provenance, protection and retention are covered.
- [x] BIAN semantics are not presented as a physical schema.
- [x] Diagram production is deferred under the specification-first workflow.

## Key takeaways

- Data architecture starts with meaning, authority and lifecycle, not a storage product.
- A system of record is authoritative only for a defined purpose, scope and time.
- Analytical and regulatory platforms preserve lineage to operational authorities.
- Accounting events and reconciliations are first-class information relationships.
- Provenance and correction history are essential in a regulated, multi-system estate.

## Practical exercise

Trace `HB-SCN-10 Authorise, Clear and Dispute a Card Purchase`. Identify the relevant `HB-DATA-*`, `HB-SOR-*`, `HB-APP-*`, `HB-ACC-*` and `HB-REC-*` records. Mark where authority changes between card lifecycle, authorisation, clearing, dispute, merchant, account and ledger information. Add one late-presentment case and explain how it changes effective time without rewriting history.

## Review checklist

- [ ] Does each model state its conceptual, logical or physical level?
- [ ] Are domain ownership and application ownership kept separate?
- [ ] Is authority qualified by information, purpose, lifecycle, legal entity and effective time?
- [ ] Are identifiers and cross-references governed?
- [ ] Does lineage include transformations, adjustments, approvals and rejected records?
- [ ] Are accounting events, reconciliation and correction authority explicit?
- [ ] Are operational authorities distinct from analytical copies and reporting publications?
- [ ] Are protection, retention, residency and permitted use reviewable?
- [ ] Are BIAN concepts treated as a versioned semantic reference only?

## References and further reading

- [BCBS-239](../../research/banking/bcbs-239-risk-data-aggregation.md)
- [W3C-PROV-DM-2013](../../research/data/w3c-prov-dm-2013.md)
- [BIAN-SERVICE-LANDSCAPE-14](../../research/bian/bian-service-landscape-14.0.md)

## Drafting notes

- `FIG-35-01` remains `Planned`; no diagram source has been created.
- Attribute-level authority, jurisdiction variants and several explicit event consumers remain governed gaps.
