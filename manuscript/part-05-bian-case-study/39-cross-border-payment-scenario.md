---
title: "Lending and Credit: Consumer, Mortgage, SME and Corporate"
chapter: 39
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 39. Lending and Credit: Consumer, Mortgage, SME and Corporate

## Chapter purpose

Explain the lending domain from financing need through application, assessment, decision, contracting, disbursement and servicing. The chapter compares consumer, mortgage, small and medium-sized enterprise (SME), and corporate credit while preserving one governed credit lifecycle.

## Reader outcomes

By the end of this chapter, you should be able to:

- distinguish a credit application, decision, offer, facility, loan and exposure;
- identify what is common across lending and what differs by product and segment;
- allocate origination, decisioning, servicing, accounting and external-information responsibilities;
- trace a lending outcome through interfaces, data authority, controls, reconciliation and resilience;
- explain how lending relates to, but remains distinct from, collateral, limits, collections and recovery.

## Prerequisites and dependencies

- Chapter 37: Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing
- Chapter 38: Deposits, Accounts, Term Deposits, Interest, Fees, Statements and Correspondence
- Chapter 40: Collateral, Limits, Exposure, Collections, Recovery and the Credit-Risk Lifecycle

## Required models and artefacts

The governing thread is `HB-DOM-040 Lending and Credit`, `HB-CAP-040 Lending and Credit Management`, `HB-PRD-04 Credit`, `HB-VS-05 Provide and Manage Credit` and `HB-PROC-03 Originate and Manage Credit`. This chapter concentrates on `HB-DOM-041 Credit Origination and Decisioning`, `HB-DOM-042 Credit Agreements and Servicing`, `HB-CAP-041 Credit Origination`, `HB-CAP-042 Credit Assessment and Decisioning`, `HB-CAP-043 Credit Agreement and Facility Management` and `HB-CAP-044 Loan Servicing`.

Chapter 40 develops `HB-DOM-043 Limits, Collateral and Exposure`, `HB-DOM-044 Collections, Restructuring and Recovery`, `HB-CAP-045 Limit Management`, `HB-CAP-046 Collateral Management`, `HB-CAP-047 Credit Exposure Management`, `HB-CAP-048 Collections Management` and `HB-CAP-049 Restructuring and Recovery Management`.

The organisational trace separates portfolio and control responsibilities. `HB-ORG-08 Retail Banking` owns retail lending outcomes, while `HB-ORG-09 Business and Corporate Banking` owns SME and corporate relationship outcomes. `HB-ORG-29 Credit, Collateral and Recovery Operations` performs fulfilment and servicing work. `HB-ORG-110 Chief Credit Officer Role` holds accountability for credit policy, authorities and origination standards, and `HB-ORG-12 Finance, Accounting, Tax and Reporting` owns the resulting books and financial controls.

No new diagram source is produced. Candidate process, decision, state, information and interaction views are expressed in text pending the normal specification approval.

## Worked examples

The main scenario follows a retail customer applying for an unsecured instalment loan. Comparison sections show how the same architecture must support a property-backed mortgage and an SME or corporate facility without forcing every case through one identical workflow.

### Governed scenario traces

Two catalogue scenarios anchor the comparison:

| Scenario | Outcome trace used in this chapter |
|---|---|
| `HB-SCN-06 Originate and Disburse Consumer or Mortgage Credit` | Product `HB-PRD-05`; value stream `HB-VS-05`; process `HB-PROC-03`; origination `HB-APP-023` or `HB-APP-024`; decisioning `HB-APP-026`; authority `HB-SOR-03`; event `HB-ACC-02`; reconciliation `HB-REC-008`; control `HB-CTRL-10`; critical operation `HB-CRIT-08`; classification `HB-TECH-007` |
| `HB-SCN-07 Approve and Manage a Corporate Credit Facility` | Product `HB-PRD-06`; value stream `HB-VS-05`; process `HB-PROC-03`; origination `HB-APP-025`; decisioning `HB-APP-026`; servicing `HB-APP-027`; authority `HB-SOR-03`; reconciliation `HB-REC-010`; control `HB-CTRL-12`; critical operation `HB-CRIT-09`; classification `HB-TECH-008` |

The fields show responsibility and evidence traceability, not one synchronous call chain. The first trace branches between consumer and mortgage origination. The second continues beyond approval into facility booking, utilisation and exposure monitoring.

## Source requirements

The Basel Committee on Banking Supervision's 2025 principles describe credit-risk management across the risk environment, credit granting, administration, measurement and monitoring, and controls. This supports the chapter's lifecycle view but does not prescribe Horizon Bank's applications. [BCBS-CREDIT-RISK-PRINCIPLES-2025]

The International Financial Reporting Standards (IFRS) 9 source supports the distinction between contractual financial assets and expected credit loss accounting where the standard applies. Horizon Bank's detailed accounting policy remains a legal-entity decision. [IFRS-9-2026]

## Planned chapter structure

The chapter starts with common lending concepts, compares portfolio types, then follows origination into servicing, accounting, operation and transition.

## Lending is a lifecycle, not a decision API

A borrower wants access to funds under understandable terms. The bank must decide whether to accept credit risk, document the obligation, release value only under approved conditions, administer the account and understand the exposure until it is repaid, sold, written off or otherwise resolved.

The central architecture question is: **how does the bank make, fulfil and service an authorised credit commitment while retaining an explainable view of risk and financial state?** A scoring interface answers only a small part of that question.

The Basel Committee's current principles explicitly connect credit granting with administration, measurement, monitoring and control. [BCBS-CREDIT-RISK-PRINCIPLES-2025] Horizon Bank therefore uses `HB-VS-05 Provide and Manage Credit` for the whole lifecycle, not only origination.

## Core credit concepts

Credit terminology becomes confusing when an application screen uses the word `loan` for everything. A conceptual model should separate:

| Concept | Meaning in the Horizon Bank model |
|---|---|
| Credit application | A request and supporting evidence under assessment |
| Credit proposal | A structured financing request, often used for complex SME or corporate cases |
| Credit decision | An authorised result, reasons, conditions, limits and validity period |
| Offer | Terms presented to the customer following an approved decision |
| Facility | A governed commitment or framework under which credit may be used |
| Loan | A booked credit exposure with repayment and servicing state |
| Drawdown | Use of an approved facility or release of loan principal |
| Schedule | Expected principal, interest, fee and date obligations |
| Exposure | The bank's current or potential credit amount at risk under governed measures |

A decision does not create a loan by itself. Acceptance, documentation, conditions precedent, booking and disbursement may still be required. Similarly, disbursement does not mean every accounting, collateral or limit update completed successfully.

## What is common and what differs

`HB-PRD-05 Consumer and Mortgage Credit` covers retail lending, while `HB-PRD-06 Business and Corporate Credit` covers SME and corporate facilities and loans. Both contribute to `HB-VS-05`, but their processes differ.

| Portfolio | Typical architecture emphasis | Do not assume |
|---|---|---|
| Consumer unsecured | High-volume capture, affordability, fraud controls, consistent decisions and rapid fulfilment | That a score alone is the decision |
| Mortgage | Property, valuation, legal work, conditions, staged completion and long servicing life | That collateral value replaces affordability or repayment analysis |
| SME | Owner and business relationships, financial evidence, guarantees, cash flow and mixed automation | That every SME is a small consumer |
| Corporate | Group structures, facilities, covenants, limits, delegated approvals, legal documents and multiple drawdowns | That one application equals one loan |

The common architecture provides shared party, product, decision, document, accounting and exposure concepts. Product-specific workflows and rules remain explicit rather than becoming hidden branches in one enormous application.

## Customer journey and origination process

For the retail instalment-loan example, the stages are:

1. establish the customer's financing need and select an eligible product;
2. capture requested amount, purpose, term and applicant information;
3. retrieve current customer, relationship and existing exposure data;
4. obtain permitted external credit information where applicable;
5. assess completeness, affordability, creditworthiness, fraud and policy conditions;
6. make an automated, human or combined decision under delegated authority;
7. present approved terms and required disclosures;
8. record acceptance and complete documentation;
9. book the agreement and loan account;
10. release funds only when fulfilment conditions are satisfied;
11. establish schedule, servicing, accounting and monitoring state;
12. communicate the outcome and retain evidence.

A Business Process Model and Notation (BPMN) model should show requests for information, referral, timeout, withdrawal, conditional approval, decline, expired offer, failed documentation, failed booking and failed disbursement. A straight line from `Apply` to `Paid` conceals most control and operational risk.

For complex credit, `HB-INT-010 Managed Credit Proposal` transfers a structured proposal from `HB-APP-005 Relationship Manager Workbench` to `HB-APP-025 Business and Corporate Credit Origination`. Draft ownership must be explicit so two users do not unknowingly approve different versions.

## Credit decisioning and explainability

`HB-CAP-042 Credit Assessment and Decisioning` includes affordability, creditworthiness, risk assessment, conditions and decision. Horizon Bank allocates governed decision execution to `HB-APP-026 Credit Decision Management` and deterministic policy rules to `HB-APP-072 Enterprise Business Rules Platform` through `HB-INT-061 Credit Rule Decision`.

A Decision Model and Notation (DMN) requirements model can show how eligibility, affordability, credit risk, fraud indicators, policy exceptions and delegated authority contribute to a decision. Statistical or machine-learning model results may be inputs, but model governance, human authority and reasons remain visible.

`HB-INT-029 Consumer Credit Decision` returns the decision, conditions and rationale from `HB-APP-026 Credit Decision Management` to `HB-APP-023 Consumer Loan Origination`. The governed `HB-INT-030 Secured and Corporate Credit Assessment` record also starts at `HB-APP-026`, but names `HB-APP-025 Business and Corporate Credit Origination` as its consumer. Although `HB-APP-024 Mortgage Origination` lists `HB-INT-030` among its related interfaces, the interface record says that the mortgage consumer split is pending. A solution must therefore treat the mortgage return route as an explicit catalogue gap, not draw a confirmed `HB-APP-026` to `HB-APP-024` interface. These decision interfaces should distinguish:

- `Approved` from `Offer issued`;
- `Refer` from `Declined`;
- policy exception from model override;
- conditions before offer from conditions before drawdown;
- decision expiry from application abandonment.

`HB-CTRL-10 Credit Decision and Delegated Authority` requires traceable inputs, rule or model version, rationale, approver, override and conditions. The evidence supports review; it does not guarantee that the decision was correct.

## External credit information

`HB-EXT-013 Credit Information Connectivity` and `HB-INT-102 Credit Bureau Exchange` represent logical connectivity to eligible credit-information services. The catalogue intentionally does not claim a provider, membership, data field or universal legal basis.

An external response is an input with provenance and effective time. It is not Horizon Bank's party master, the final credit decision or an error-free truth. The design needs consent or other permitted-purpose evidence where applicable, request and response correlation, restricted access, data-quality handling, expiry rules and a dispute or correction path.

## Origination and servicing applications

The application estate distinguishes product workflow from enduring account servicing:

| Application | Responsibility |
|---|---|
| `HB-APP-023 Consumer Loan Origination` | Unsecured retail application through decision and offer |
| `HB-APP-024 Mortgage Origination` | Property-backed application, valuation, offer and completion |
| `HB-APP-025 Business and Corporate Credit Origination` | SME and corporate proposals, structure, approval and documentation |
| `HB-APP-026 Credit Decision Management` | Affordability, score, rating, policy and authority decisions |
| `HB-APP-027 Loan and Facility Servicing` | Booked facilities, loans, schedules, balances, interest and repayments |
| `HB-APP-028 Collateral Management` | Collateral, valuations, liens and release |
| `HB-APP-029 Limit and Covenant Management` | Limits, utilisations and covenants |
| `HB-APP-030 Credit Exposure Aggregation` | Drawn, undrawn and other exposure components |
| `HB-APP-058 Product Subledger Platform` | Lending accounting positions |
| `HB-APP-070 Enterprise Document and Content Management` | Offers, agreements and evidence |

An origination case ends, but the credit agreement may last for years. `HB-APP-027` therefore owns booked servicing state rather than leaving it inside the workflow. A mortgage may use a separate origination application because property and completion work differ, while still sharing decision and servicing responsibilities.

## Information model and authority

`HB-DATA-04 Credit and Collateral` groups applications, decisions, facilities, loans, schedules, limits, collateral, covenants and exposures. `HB-SOR-03 Credit Exposure Authority` assigns qualified authority across `HB-APP-027`, `HB-APP-029` and `HB-APP-030`; it explicitly recognises that one application is not authoritative for every attribute.

The minimum relationships are:

```text
Party -> Credit Application -> Credit Decision
Credit Decision -> Offer -> Credit Agreement
Credit Agreement -> Facility -> Drawdown or Loan
Loan -> Repayment Schedule -> Servicing Event
Facility -> Limit -> Utilisation
Facility or Loan -> Collateral Allocation
Facility or Loan -> Exposure Position
```

Versioning matters. A restructured schedule must not erase the original agreement and prior schedule. A new valuation must preserve the source and date of the former value. A decision snapshot must retain the input references used at decision time.

## Loan state and servicing

A conceptual loan state model may include:

```text
Approved
-> Documentation pending
-> Ready for drawdown
-> Active
-> Delinquent or Modified, when applicable
-> Repaid, Recovered or Written off
-> Closed and retained
```

The states are not universal accounting or regulatory classifications. Their transition rules must be defined for each product and legal entity. `Delinquent` may trigger collections, but it does not automatically mean default, impairment stage or write-off.

`HB-CAP-044 Loan Servicing` covers schedules, balances, interest, fees, repayments and servicing events. Servicing also includes rate changes, overpayments, payment holidays, corrections, payoff quotations and closure. These actions need customer communication and accounting consequences, not only balance updates.

## Accounting events and financial control

Horizon Bank records several lending events:

- `HB-ACC-02 Loan Principal Advanced`;
- `HB-ACC-08 Loan Interest Accrued`;
- `HB-ACC-09 Loan Repayment Received`;
- `HB-ACC-10 Lending Fee Charged`.

`HB-INT-040 Loan Accounting Message` sends booked consequences from servicing to `HB-APP-058 Product Subledger Platform`. The message needs a business-event identifier, amount, currency, effective date, accounting-rule version and replay decision. `HB-REC-007 Loan Account to Lending Subledger` compares loan and subledger positions. `HB-REC-008 Loan Disbursement and Settlement` checks that the authorised advance agrees with the receivable and cash movement.

The chapter does not prescribe journal entries. IFRS 9 covers recognition and measurement of financial instruments and includes expected credit loss requirements where it applies. [IFRS-9-2026] Product classification, fees, modifications, impairment and tax require approved accounting policy. Prudential exposure and accounting carrying amount must not be treated as the same measure merely because both use currency.

## Controls through fulfilment

Important controls include:

- `HB-CTRL-07 Product and Price Approval` for approved terms;
- `HB-CTRL-10 Credit Decision and Delegated Authority` for the lending decision;
- `HB-CTRL-11 Collateral Eligibility, Valuation and Lien Control` for secured lending;
- `HB-CTRL-12 Limit, Covenant and Exposure Monitoring` for use of approved capacity;
- `HB-CTRL-28 Accounting-Event Completeness and Mapping` for downstream financial effects.

Conditions before disbursement deserve their own evidence. The application should not send `Disburse` merely because the customer accepted the offer. Required documents, cooling-off or completion conditions where applicable, collateral state, limit reservation, destination, fraud checks and delegated release must all have clear owners.

## Resilience and operation

`HB-TECH-007 Lending Origination and Servicing Classification` covers origination, fulfilment, servicing and repayment technology. `HB-CRIT-08 Disburse and Service Credit` protects the outcome that approved credit is booked and serviced with correct contractual and financial records.

Origination can often tolerate a different disruption pattern from servicing. A new application might wait, while an accepted disbursement, scheduled collection or payoff instruction may be time-sensitive. Recovery design should preserve:

- application, decision and offer versions;
- outstanding conditions and approvals;
- agreement and servicing state;
- schedules, balances and accepted payments;
- accounting-event and interface replay boundaries;
- document and communication evidence;
- reconciliation status and manual work queues.

No off-system spreadsheet becomes a balance authority during disruption. If manual evidence supports delayed fulfilment, later booking and independent reconciliation are required. Quantitative recovery targets remain pending business impact analysis.

## BIAN candidate mapping

`HB-BIAN-03 Credit Responsibility Candidate` links `HB-PRD-04` and `HB-VS-05` to a candidate Banking Industry Architecture Network (BIAN) mapping. Exact BIAN 14.0 objects, confidence and many-to-many rationale remain pending. The mapping needs to distinguish product design, origination, decision, agreement, servicing, collateral, limits and recovery responsibilities where the official model supports them.

It must not produce rules such as `one Service Domain = one loan application`. Horizon Bank's three origination applications reflect segment and workflow differences, while shared decision and servicing responsibilities cross those boundaries.

## Current, transition and target considerations

A common current-state problem is separate product origination with inconsistent customer, decision and exposure data. A target direction can establish governed interfaces and shared semantics without forcing all products into one release train or database.

A staged transition can:

1. catalogue applications, decisions, facilities, loans and schedules;
2. define a common credit identifier and event vocabulary;
3. expose qualified party, product, limit and exposure views;
4. externalise governed rules where reuse and ownership justify it;
5. standardise accounting-event and reconciliation contracts;
6. migrate products and legal entities in controlled cohorts;
7. compare servicing and subledger outputs before authority changes;
8. retire legacy workflows only after documents, open cases and history remain accessible.

Moving decisions to a shared engine without improving source data, authority or override governance is not a complete target architecture.

## Common mistakes

- Treating application, decision, offer, facility and loan as one object.
- Designing only approval and ignoring documentation, disbursement and servicing.
- Applying a consumer straight-through flow unchanged to mortgage or corporate credit.
- Treating a bureau score as a credit decision.
- Allowing a rule engine to hide delegated authority and manual overrides.
- Mixing accounting impairment, prudential exposure and operational delinquency states.
- Publishing an accounting event without idempotency or correction semantics.
- Mapping BIAN Service Domains directly to applications, databases or teams.

## Chapter summary

Lending architecture connects a financing request to an authorised, documented, booked and serviced exposure. Product-specific origination can vary, while common party, decision, servicing, accounting and exposure semantics maintain coherence. The credit lifecycle continues into monitoring, collections and resolution, developed in Chapter 40.

## Completion checklist

- [x] Consumer, mortgage, SME and corporate differences are explicit.
- [x] Application, decision, offer, facility, loan and exposure are distinguished.
- [x] Origination, decisioning, servicing and accounting responsibilities use governed IDs.
- [x] Interfaces, authority, controls, reconciliations and resilience are traced.
- [x] Accounting and prudential concepts are not conflated.
- [x] BIAN remains a candidate reference mapping.

## Key takeaways

- Credit granting is one part of a longer controlled lifecycle.
- Product and segment differences justify different workflows, not incompatible meanings.
- Decision evidence includes inputs, version, reasons, authority, conditions and overrides.
- Origination workflow state and enduring loan-servicing state have different owners.
- Accounting, exposure and delinquency measures need explicit definitions and authority.
- Resilience must preserve accepted financial work and repair paths, not only application availability.

## Practical exercise

Compare a retail instalment loan with an SME revolving facility. For each, list the parties, application, decision, agreement, limit, drawdown, servicing and accounting records. Then create an interaction table using `HB-APP-023` or `HB-APP-025`, `HB-APP-026`, `HB-APP-027`, `HB-APP-029`, `HB-APP-030` and `HB-APP-058`.

A strong answer shows shared semantics and different workflow, identifies decision and disbursement controls, and avoids inventing a one-to-one BIAN mapping.

## Review checklist

- [ ] Does the model cover the complete credit lifecycle rather than only approval?
- [ ] Are product, segment and legal-entity variations stated?
- [ ] Are decision, offer, agreement, facility, loan and exposure separate?
- [ ] Are external data provenance and permitted use explicit?
- [ ] Are conditions, delegated authority and overrides retained as evidence?
- [ ] Are business, accounting and prudential states kept distinct?
- [ ] Are failed booking, disbursement, event and reconciliation paths shown?
- [ ] Are migration authority changes and coexistence controls reviewable?

## References and further reading

- [BCBS-CREDIT-RISK-PRINCIPLES-2025](../../research/banking/part-v-37-40/bcbs-credit-risk-principles-2025.md)
- [IFRS-9-2026](../../research/banking/part-v-37-40/ifrs-9-financial-instruments-2026.md)
- [BIAN-SERVICE-LANDSCAPE-14](../../research/bian/bian-service-landscape-14.0.md)

## Drafting notes

- Exact BIAN 14.0 credit mappings remain pending in `HB-BIAN-03`.
- Product-level policy, model, accounting and jurisdiction rules require governed expansion.
