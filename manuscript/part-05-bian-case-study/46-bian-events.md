---
title: "Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting"
chapter: 46
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 46. Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting

## Chapter purpose

Explain how a full-service bank turns product and transaction activity into controlled accounting records, reconciled books, tax positions and approved reports. The chapter makes the boundaries between business events, accounting events, subledgers, the General Ledger and reporting datasets explicit.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish a business occurrence, an accounting event, a subledger entry and a General Ledger journal;
- explain why subledgers, the General Ledger, reconciliation, tax and reporting need different authorities;
- trace finance processing through Horizon Bank's applications, interfaces, controls and reconciliations;
- model correction, close and attestation without losing the original evidence;
- review reporting lineage from a reported value back to governed sources; and
- identify finance-related BIAN mapping work that remains unverified.

## Prerequisites and dependencies

- Chapter 35: Horizon Bank Information and Data Architecture
- Chapter 45: Treasury, Markets, Funding, Liquidity, ALM and Capital
- Familiarity with events, interfaces and systems of record

## Required models and artefacts

- Governed finance domain, capability, process, organisation and application records
- Accounting-event chain, reconciliation specifications and report-lineage trace
- Scenario trace for `HB-SCN-16 Close the Books and Submit a Regulatory Return`

## Worked examples

- Horizon Bank financial-close and regulatory-return scenario

## Source requirements

Accounting, risk-data and BIAN claims use official primary sources. The chapter separates official principles from Horizon Bank design recommendations and does not infer jurisdictional applicability.

## The question this architecture answers

Finance architecture answers: **How can the bank explain every material financial result from the originating activity through accounting, reconciliation, close, tax and reporting?**

The answer is not `send everything to the General Ledger`. Product systems understand customer agreements and transaction lifecycles. Accounting policy determines how economic effects are classified and measured. Subledgers retain product-level accounting detail. The General Ledger maintains approved books by legal entity, account, currency and period. Reconciliation tests whether records that should agree actually agree. Reporting transforms approved sources for a defined audience and purpose.

The International Financial Reporting Standards (IFRS) Conceptual Framework separates recognition, measurement, presentation and disclosure concerns, and states that the framework is not itself an IFRS Accounting Standard [IFRS-CONCEPTUAL-FRAMEWORK-2018]. For architecture, this supports separating the occurrence of an event from the governed accounting treatment applied to it. Horizon Bank remains fictional, so the chapter does not prescribe accounting policy or claim that a particular standard or return applies.

## Governed responsibility model

`HB-DOM-110 Finance, Accounting, Tax and Reporting` is the Level 1 business domain. Its Level 2 responsibilities are:

| Domain | Responsibility | Evidence expected |
|---|---|---|
| `HB-DOM-111 Accounting Policy and Event Governance` | Chart of accounts, accounting rules and event-to-accounting mapping | Approved rule versions, effective dates and decision owners |
| `HB-DOM-112 Subledger and General Ledger` | Product detail, journals, periods and legal-entity books | Balanced entries, accepted journals and controlled periods |
| `HB-DOM-113 Reconciliation and Financial Close` | Matching, substantiation, exception resolution and close | Complete populations, breaks, approvals and attestations |
| `HB-DOM-114 Management and Regulatory Reporting` | Governed internal and external reports | Source lineage, transformations, adjustments, approval and submission evidence |
| `HB-DOM-115 Tax Management` | Tax positions, calculation, reporting and payment evidence | Source-to-calculation-to-filing trace |

These are supported by `HB-CAP-110 Finance, Accounting, Tax and Reporting` and `HB-CAP-111` to `HB-CAP-119`. `HB-PROC-05 Record, Reconcile and Report` is the Level 1 process. Detailed work is divided among `HB-PROC-143 Govern Accounting Policy, Chart and Events`, `HB-PROC-144 Maintain Subledgers and General Ledger`, `HB-PROC-145 Reconcile, Substantiate and Close`, `HB-PROC-146 Produce Management and External Reports` and `HB-PROC-147 Manage Tax Positions and Obligations`.

`HB-ORG-12 Finance, Accounting, Tax and Reporting` owns the function. `HB-ORG-105 Chief Financial Officer Role` has executive accountability and `HB-ORG-115 Group Financial Controller Role` owns financial control. Product owners remain accountable for complete, correct source activity. Finance does not become the business owner of a loan, payment or trade merely because it records its financial effects.

## Follow the accounting chain

### Business occurrence

A business occurrence is something that happened in a product or operational lifecycle. A loan was advanced, a payment settled, interest accrued or a trade was revalued. The originating application owns the event's business state and identity.

### Accounting event

An accounting event is a governed statement that an occurrence has a financial effect requiring accounting treatment. Horizon Bank assigns stable IDs such as `HB-ACC-02 Loan Principal Advanced`, `HB-ACC-14 Payment Settlement Recognised`, `HB-ACC-24 Treasury Trade Settled` and `HB-ACC-25 Treasury Valuation Changed`.

The event should contain or reference the originating transaction, legal entity, product, accounting date, value date, currency, amount, event type and rule version. It should not carry an uncontrolled debit and credit selected by the source application. `HB-CTRL-28 Accounting-Event Completeness and Mapping` tests event coverage and mapping governance.

### Simplified accounting examples

The following entries are teaching examples, not Horizon Bank accounting policy. Exact recognition, measurement, account names, timing and presentation depend on the agreement, legal entity and approved framework. `Debit` and `credit` show the direction of a balanced entry, while the accounting-event ID preserves the business meaning that caused it.

| Business occurrence | Governed event | Simplified illustrative entry | Essential architecture check |
|---|---|---|---|
| Customer funds a deposit account | `HB-ACC-05 Deposit Principal Received` | Debit cash or settlement asset; credit customer deposit liability | Match cash receipt, account posting and subledger entry |
| Bank disburses a loan | `HB-ACC-02 Loan Principal Advanced` | Debit loan asset; credit cash, settlement asset or disbursement payable as policy requires | Link approved agreement, drawdown, beneficiary and settlement result |
| Loan interest accrues | `HB-ACC-08 Loan Interest Accrued` | Debit accrued interest receivable or loan asset; credit interest income | Use the effective rule, balance, rate, dates and accrual basis |
| Bank charges a payment fee | `HB-ACC-03 Payment Fee Charged` | Debit customer account or fee receivable; credit fee income | Preserve tariff, waiver, tax and customer-notification evidence |
| Card purchase clears and creates settlement effects | `HB-ACC-17 Issuer Card Purchase Cleared`; `HB-ACC-18 Merchant Settlement Payable Recognised` where acquiring is in scope | Recognise the cardholder or deposit-account effect and the applicable scheme or merchant settlement obligation | Keep authorisation, presentment, clearing, merchant funding and settlement states distinct |
| Expected credit loss changes | `HB-ACC-11 Credit Loss Allowance Changed` | Debit or credit impairment result; credit or debit loss allowance | Preserve exposure population, model version, scenario, approval and prior allowance |
| Credit exposure is written off | `HB-ACC-12 Credit Exposure Written Off` | Debit loss allowance or approved write-off expense; credit loan asset | Require authority, recovery status and continued memorandum tracking where policy requires it |
| A nostro difference is found | `HB-ACC-30 Suspense Item Established or Released`, only when approved | Use a controlled suspense entry rather than forcing agreement; release it when the cause is resolved | Link `HB-REC-015 Correspondent Cash and Nostro` and `HB-REC-036 Suspense and Unapplied Cash` to owner and ageing |

A break is not automatically an accounting event. A missing statement, timing difference or duplicate feed may require investigation but no journal. `HB-ACC-30` is appropriate only after an authorised accounting decision. A suspense balance must have a reason, owner, ageing, evidence and exit condition.

### Product subledger

`HB-APP-058 Product Subledger Platform` records product-level accounting entries and balances. It receives `HB-INT-040 Loan Accounting Message`, `HB-INT-041 Recovery Accounting Event` and `HB-INT-081 Treasury Accounting Event`, among other governed inputs. The catalogue marks it as a target application because Horizon Bank's product-engine and subledger boundary remains to be completed.

A subledger preserves detail that would be unsuitable or too voluminous as the primary model of the General Ledger. It can apply effective-dated accounting rules, create balanced entries, retain links to the source event and support reversal or correction. It must not become an ungoverned parallel ledger whose totals cannot be reconciled.

### General Ledger

`HB-APP-059 General Ledger` receives balanced product-subledger journals through `HB-INT-082 Subledger Journal Batch`. It is linked to `HB-SOR-04 General Ledger Authority`, the authority for approved legal-entity ledger balances. The General Ledger controls chart accounts, legal entities, currencies, periods and journals.

`HB-CTRL-29 Manual Journal and Adjustment Approval` applies where a person or controlled process creates an adjustment. The model should retain the reason, preparer, approver, evidence, effective period and relationship to any superseded entry. Deleting the original journal to make a balance look correct destroys traceability.

### Reconciliation and close

Reconciliation compares two defined populations under a rule. It is not the same as `the totals look plausible`. `HB-APP-060 Enterprise Reconciliation` receives ledger data through `HB-INT-083 General Ledger Reconciliation Feed` and scheduled work through `HB-INT-085 Scheduled Reconciliation Run`. It owns reconciliation results and break cases, not the source transactions or the General Ledger.

`HB-REC-030 Subledger to General Ledger` tests product accounting totals against legal-entity ledger balances. `HB-REC-031 General Ledger to Consolidation and Intercompany` tests entity books, intercompany positions, eliminations and group balances. `HB-REC-036 Suspense and Unapplied Cash` tracks unresolved cash to allocations, returns, write-offs and residual balances. Each has different sources, timing, owners and permitted break treatments.

Close is a governed decision that required activities for a period have completed or that exceptions have been explicitly accepted. `HB-CTRL-30 Financial Close and Consolidation Attestation` should point to the reconciliation population, unresolved breaks, approved journals, consolidation status and sign-off. A green close dashboard without those links is presentation, not evidence.

## Tax is more than a filing interface

`HB-APP-061 Tax Management and Reporting` calculates and records governed tax obligations and filing evidence. `HB-INT-084 Ledger Tax Feed` supplies ledger information, while `HB-INT-086 Tax Filing Exchange` sends approved filings through `HB-EXT-014 Tax Authority Reporting Gateway`.

Tax architecture must distinguish source transaction attributes, accounting carrying values, tax classifications, calculations, adjustments, payments and filings. IAS 12, for example, distinguishes current and deferred tax concerns [IFRS-IAS-12-INCOME-TAXES]. The specific rules and authorities are jurisdiction-dependent. Horizon Bank therefore uses `HB-ACC-27 Tax Liability or Recoverable Recognised`, `HB-CTRL-31 Tax Calculation, Approval and Filing` and `HB-REC-032 Tax Source to Filing` without inventing country rules.

A filing acknowledgement proves receipt, not necessarily acceptance of every reported position. The application must retain both the submitted version and the response, together with later corrections or resubmissions.

## Management and external reporting

Management reporting and regulatory reporting can consume overlapping data, but their purpose and authority differ.

`HB-APP-063 Management Reporting and Performance` consumes `HB-INT-089 Management Reporting Dataset`. It publishes governed business and performance views. It does not replace product, finance or risk authorities. Metrics need definitions, owners, dimensions, effective periods, allocation rules and correction policies.

`HB-APP-082 Regulatory Data Platform` curates traceable datasets and adjustments. `HB-INT-087 Regulatory Dataset Batch` transfers an attested dataset to `HB-APP-062 Regulatory Reporting`. The reporting application validates, approves and sends the return using `HB-INT-088 Regulatory Return Submission` through `HB-EXT-015 Prudential and Conduct Reporting Gateway`. `HB-SOR-24 Regulatory Return Authority` preserves the approved return and submission evidence.

`HB-REC-033 Regulatory Report to Governed Source` traces report cells through transformations and adjustments to governed records. `HB-REC-034 Management Report to Finance and Risk Sources` provides a similar test for management measures. These reconciliations are stronger than comparing two final reports because they reveal where classifications, transformations or adjustments diverge.

The Basel Committee's principles for risk data aggregation and reporting emphasise governance, architecture, accuracy, completeness, timeliness and adaptability, while their original direct scope is not universal [BCBS-239]. Horizon Bank uses the principles as architecture discipline, not as an unsupported claim of regulatory scope.

## Data architecture and lineage

The principal data domains are `HB-DATA-05 Finance and Accounting` and `HB-DATA-16 Regulatory, Statutory, Tax and Management Reporting`. Finance also consumes product-specific domains. The distinction matters: a report dataset is not automatically an authoritative product or ledger record.

For every reported value, lineage should answer:

1. What report, version, period, entity and cell is this?
2. Which approved dataset and transformation produced it?
3. Which adjustments were applied, by whom and under what authority?
4. Which subledger, ledger, risk or product records supplied the input?
5. What data-quality or reconciliation exceptions remained?
6. Which approval and submission evidence applies?

`HB-APP-083 Metadata and Data Lineage Platform` and `HB-APP-084 Data Quality Management` support this trace. They catalogue lineage and quality evidence; they do not become the owner of every underlying value.

## Commands, events, files and batch

Finance uses several interaction styles because the semantics differ. An accounting event communicates an occurrence. A command requests a governed action. A batch transfers a complete population for a cut-off. A file may be required for an external reporting gateway. None is automatically better.

For events, use a stable event identifier, originating record, effective time and schema version. Consumers must detect duplicates. Corrections should reference the original event and state whether they reverse, replace or supplement it. For batch, record the population definition, cut-off, sequence, count, totals and completeness status. For external files, retain content hashes, approvals, encryption state, transmission receipts and acknowledgements where policy requires them.

`Exactly once` is not a useful unqualified promise across multiple systems. A practical design uses idempotent acceptance, immutable event identity, balanced accounting rules, replay boundaries and reconciliation to detect missing or duplicated financial effect.

## Worked trace: close the books and submit a return

`HB-SCN-16 Close the Books and Submit a Regulatory Return` begins at a legal-entity or group reporting cut-off. A catalogue-backed trace is:

1. Product applications complete source activity and emit governed accounting events.
2. `HB-APP-058` applies effective accounting mappings and sends balanced journals over `HB-INT-082`.
3. `HB-APP-059` accepts journals into an open period and remains the authority for approved ledger balances.
4. `HB-APP-060` runs `HB-REC-030` and other applicable reconciliations. Owners resolve or explicitly approve breaks.
5. `HB-CTRL-30` records close and consolidation attestation.
6. `HB-APP-082` assembles a governed dataset with lineage and adjustments.
7. `HB-APP-062` validates and approves the return, sends it through `HB-INT-088` and retains the acknowledgement under `HB-SOR-24`.
8. `HB-REC-033` confirms the report-to-source trace. Any correction creates a new governed version and resubmission path.

The scenario is not complete merely because a file left the bank. Completion includes accepted books, governed exceptions, approval, transmission evidence and an observable response or escalation.

### End-to-end loan accounting trace

A consumer-loan disbursement demonstrates how product and finance authorities cooperate without merging.

1. `HB-APP-023 Consumer Loan Origination` coordinates the application, and `HB-APP-026 Credit Decision Management` records the governed decision. Neither application posts the General Ledger.
2. After acceptance and fulfilment, `HB-APP-027 Loan and Facility Servicing` establishes the loan and authorised drawdown. `HB-SOR-03 Credit Exposure Authority` governs the qualified exposure boundary.
3. Disbursement creates `HB-ACC-02 Loan Principal Advanced`. `HB-INT-040 Loan Accounting Message` carries the governed loan accounting message from `HB-APP-027` to `HB-APP-058 Product Subledger Platform`.
4. `HB-APP-058` applies the effective accounting rule, creates balanced product-level entries and retains the loan, event and rule references.
5. `HB-INT-082 Subledger Journal Batch` carries balanced journals from `HB-APP-058` to `HB-APP-059 General Ledger`. `HB-SOR-04` remains the authority for approved legal-entity ledger balances.
6. `HB-REC-007 Loan Account to Lending Subledger` checks servicing balances against accounting detail. `HB-REC-008 Loan Disbursement and Settlement` checks the drawdown against cash settlement. `HB-REC-030 Subledger to General Ledger` checks accepted product totals against ledger balances.
7. Later servicing can create `HB-ACC-08 Loan Interest Accrued` and `HB-ACC-09 Loan Repayment Received`. Credit deterioration may create `HB-ACC-11`; an authorised write-off may later create `HB-ACC-12` without erasing recovery history.
8. `HB-CTRL-10 Credit Decision and Delegated Authority`, `HB-CTRL-28` and `HB-CTRL-30` preserve the decision, accounting mapping and close evidence. A manual correction also requires `HB-CTRL-29` and a reference to the original event.

This trace keeps customer agreement state, exposure, cash settlement, product accounting and legal-entity books distinct. The reconciliations prove that the boundaries agree for defined populations and dates.

## Controls and resilience

The main technology classifications are `HB-TECH-018 Finance, Subledger and General Ledger Classification`, `HB-TECH-019 Reconciliation and Finance-Control Classification` and `HB-TECH-020 Regulatory and Management Reporting Classification`. `HB-CRIT-15 Maintain Authoritative Financial Books` and `HB-CRIT-17 Produce and Submit Material Regulatory Returns` express business outcomes that depend on them.

Recovery design must preserve ordered events, period states, journal identities, reconciliation populations, approvals and report versions. After recovery, finance may need to replay events, detect duplicates, re-run reconciliations and re-establish close or submission state. Application recovery without financial-state verification is incomplete. Numerical Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs) remain owner-approved gaps rather than invented facts.

## Current-to-target considerations

The catalogue records `HB-APP-059`, `HB-APP-061`, `HB-APP-062` and `HB-APP-063` as current, while `HB-APP-058`, `HB-APP-060` and `HB-APP-082` are proposed target applications. The distinction signals a transition problem, not permission for a big-bang ledger replacement.

A defensible sequence is to govern accounting-event identities and mappings, prove subledger-to-ledger totals, introduce a reconciliation inventory with common break ownership, then build attested reporting datasets. Current and target feeds should run in parallel for selected populations with agreed acceptance criteria. Cut-over requires balanced journals, explainable breaks, repeatable reports and a rollback route.

## Choose the model that matches the finance question

Use an event model to define economic occurrences and corrections, a logical data model to define journal and ledger structures, a process model to show close activities and approvals, a reconciliation specification to compare populations, and a lineage view to trace a report value. A process diagram should not be used as the chart of accounts, and a lineage graph should not be mistaken for close authority.

## BIAN alignment and limits

The governed BIAN register does not yet contain a finance, accounting, tax or reporting mapping. Service Landscape 14.0 is the current announced BIAN release at the access date [BIAN-SERVICE-LANDSCAPE-14-PV45-48], but a release announcement cannot validate a detailed mapping.

A later mapping exercise should compare each finance responsibility with versioned BIAN artefacts and record confidence and verification status. It must not assume that `HB-APP-059`, a subledger, an accounting event or an organisation unit equals one BIAN Service Domain.

## Common mistakes

- Sending uncontrolled debit and credit instructions from every product application.
- Treating an expected-credit-loss calculation, write-off decision or nostro break as a journal without governed approval and source evidence.
- Treating an accounting event as the journal or treating a journal as the original business event.
- Calling a reporting warehouse the source of product or ledger truth.
- Closing a period while material populations or breaks are unknown.
- Editing historical entries instead of using governed reversal or correction.
- Combining all reconciliations into one total without population definitions.
- Treating a filing receipt as proof that a return is correct.
- Hard-coding tax or reporting rules without jurisdiction and effective date.
- Claiming BIAN alignment from similar names alone.

## Chapter summary

Finance architecture provides an explainable chain from business activity to accounting events, subledgers, the General Ledger, reconciliations, close, tax and reporting. Horizon Bank uses separate applications and authorities because these responsibilities have different owners, records and controls. The scenario and reconciliation catalogues turn the chain into something reviewers can test. BIAN mapping and jurisdiction-specific obligations remain governed future work.

## Key takeaways

- A business event, accounting event, subledger entry and General Ledger journal are different artefacts.
- `HB-SOR-04` identifies the authority for approved ledger balances.
- Reconciliation needs explicit populations, timing, rules, owners and break treatment.
- Close is an attested control decision, not a dashboard colour.
- Tax links source activity, calculations, accounting positions, filings and acknowledgements.
- Report lineage must include transformations, adjustments, approvals and source quality.
- Recovery requires replay and reconciliation controls, not only restored infrastructure.
- Finance-related BIAN mappings are not claimed before verification.

## Practical exercise

A regulatory total differs from the General Ledger. The reporting team proposes a manual adjustment in the final return. Build a trace showing the records and approvals needed before submission.

### Suggested answer criteria

A strong answer identifies `HB-APP-059`, `HB-APP-060`, `HB-APP-082` and `HB-APP-062`; checks `HB-REC-030` and `HB-REC-033`; records the adjustment's reason, owner, evidence and effective version; applies `HB-CTRL-29`, `HB-CTRL-30` and `HB-CTRL-32 Regulatory Reporting Lineage and Submission`; and preserves both the original and corrected lineage. It does not overwrite the source or post a journal solely to force agreement without understanding the cause.

## Review checklist

- [ ] The accounting chain has explicit event and authority boundaries.
- [ ] Product applications remain responsible for source completeness.
- [ ] Subledger and General Ledger responsibilities are distinct.
- [ ] Manual adjustments preserve reason, evidence, maker and approver.
- [ ] Every reconciliation defines both populations and break ownership.
- [ ] Tax and reporting applicability is jurisdiction-specific.
- [ ] Report lineage reaches governed sources and transformations.
- [ ] Recovery includes event replay, duplicate control and reconciliation.
- [ ] All Horizon Bank references use exact governed IDs.
- [ ] No unverified BIAN equivalence is asserted.

## References and source notes

- [IFRS-CONCEPTUAL-FRAMEWORK-2018]
- [IFRS-IAS-12-INCOME-TAXES]
- [BCBS-239]
- [BIAN-SERVICE-LANDSCAPE-14-PV45-48]

## Deferred work

No diagram source is created in this pass. Horizon Bank still needs a product-accounting rule catalogue, complete subledger inventory, legal-entity close calendar, report inventory, jurisdiction-specific tax and regulatory applicability, verified finance BIAN candidates and owner-approved resilience objectives.
