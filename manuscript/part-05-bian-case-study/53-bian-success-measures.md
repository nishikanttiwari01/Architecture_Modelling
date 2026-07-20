---
title: "Legacy Modernisation, Data Migration and Transition Architecture"
chapter: 53
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 53. Legacy Modernisation, Data Migration and Transition Architecture

## Chapter purpose

Modernisation is the controlled movement of business responsibilities, data and operations from one architecture state to another. It is not a mass renaming of old systems and it is rarely a single cutover.

This chapter answers: **How can a bank change a live estate without losing financial integrity, customer service, control evidence or a credible route back?** It provides a practical transition method for Horizon Bank, using its governed catalogues as an author model rather than claiming one universal migration sequence.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish current, transition and target architecture states;
- select a modernisation seam using business responsibility and dependency evidence;
- design data migration as reconciliation-backed state transfer;
- explain coexistence, cutover, rollback and decommissioning decisions;
- build a transition work package from governed Horizon Bank records; and
- review a migration without inventing performance or recovery targets.

## Prerequisites and dependencies

- Chapter 49, for traceability and BIAN mapping;
- Chapter 50, for application, software-service and team boundaries;
- Chapter 51, for interaction styles and external networks; and
- Chapter 52, for deployment, security, resilience and operational ownership.

## Required models and artefacts

A credible transition needs more than a roadmap. The minimum set is:

- current, transition and target responsibility views;
- application and interface catalogues with architecture state;
- authoritative-data assignments and lineage;
- a migration inventory with record counts, states and exceptions;
- a dependency and critical-operation view;
- reconciliation, cutover, rollback and decommissioning plans;
- an architecture decision record for each material trade-off; and
- evidence that every temporary component has an owner and an exit condition.

The governed sources are the Horizon Bank application, interface, system-of-record, reconciliation, control, critical-operation, technology-resilience and scenario catalogues.

## Worked examples

The main example modernises payment execution around current applications `HB-APP-033 Payment Initiation Service`, `HB-APP-035 Payment Routing and Clearing` and `HB-APP-036 Settlement and Nostro Management`, while introducing target application `HB-APP-034 Payment Orchestration`. This is a fictional design choice. It does not imply that a real bank should use the same boundary.

## Source requirements

The chapter uses Basel Committee guidance to establish that material technology change belongs inside operational-risk and resilience governance [BCBS-OP-RISK-2021] [BCBS-OPERATIONAL-RESILIENCE-2021]. The transition method, wave structure and Horizon Bank decisions are author recommendations. Banking Industry Architecture Network (BIAN) mappings remain candidates under version 14.0 and do not prescribe deployment units [BIAN-SERVICE-LANDSCAPE-14].

## Start with business continuity, not replacement technology

The modernisation question is often phrased as, “What replaces the legacy platform?” That is too narrow. A bank must first ask which customer or business outcome must continue, which records prove that outcome, and which controls make it safe.

For a time-critical payment, `HB-CRIT-02 Make a Time-Critical Payment` is the outcome boundary. It depends on identity, entitlement, funds control, screening, routing, clearing, settlement, accounting, reconciliation and investigation. Replacing only a routing engine does not modernise that operation if the surrounding responsibilities remain opaque.

A useful assessment therefore starts with five linked questions:

1. Which governed responsibility is changing?
2. Which applications currently perform it?
3. Which data is authoritative at each lifecycle stage?
4. Which interfaces, controls and operational dependencies surround it?
5. What evidence permits traffic, data authority and support ownership to move?

The answers define a migration seam. A seam is a boundary across which responsibility can move while contracts and outcomes remain testable. A BIAN Service Domain candidate may help clarify the responsibility, but it is not automatically the seam, application or microservice.

## Describe three architecture states explicitly

**Current state** records what operates now, including duplication, manual intervention and uncertainty. It must be evidence-based enough to support change, not an idealised diagram of what people think exists.

**Target state** records the intended allocation of responsibility after the change. It should state the target owner, authoritative data, interfaces, controls and operational classification, not only new application names.

**Transition architecture** is a coherent intermediate operating state. It contains temporary responsibilities and controls required while current and target elements coexist. “Partly migrated” is not an adequate definition. A transition must state which population follows which route, which record is authoritative, how exceptions are handled and how the bank exits that state.

| Concern | Current | Transition | Target |
|---|---|---|---|
| Payment coordination | Rail-specific flows across `HB-APP-033`, `HB-APP-035` and retained processors | Selected payment types use `HB-APP-034`; other types retain current routing | `HB-APP-034` coordinates only the approved responsibility set |
| External exchange | Existing clearing and file paths | Old and new paths are controlled by explicit routing and `HB-INT-036 Accepted Payment Command` contracts | Each approved rail has one governed exchange path |
| Execution state | Distributed current records | A correlation record links both routes; duplicate financial effect is prevented | The approved processing authority is recorded in `HB-SOR-08` |
| Accounting | Existing product and payment postings | Both routes emit controlled accounting events and reconcile before close | Governed event-to-subledger mappings feed `HB-APP-058` |
| Operations | Current support queues | Joint routing, alert and rollback runbooks | One accepted service model with named owners |

This table is a responsibility view, not a delivery schedule. Dates, volumes and quantitative recovery objectives need approved business evidence and are intentionally absent.

## Select a modernisation strategy by responsibility

Several strategies can coexist in one programme:

- **Retain:** Keep an application where its responsibility is understood, supportable and proportionate.
- **Encapsulate:** Place a governed interface around a retained function to control consumers and semantics.
- **Re-platform:** Change runtime or infrastructure while keeping the responsibility substantially stable.
- **Rebuild or replace:** Move a responsibility to a new implementation when rules, maintainability or control needs justify it.
- **Extract:** Move one coherent responsibility behind an explicit contract while the remainder stays in place.
- **Retire:** Remove an application only after consumers, records, obligations and operational evidence have moved or been retained lawfully.

The strangler pattern is one extraction technique. It redirects selected interactions to a new implementation and reduces the old responsibility over time. It is useful when requests can be partitioned safely. It is unsuitable when both implementations would update an indivisible financial state without a sound authority and reconciliation design.

An application programming interface (API) façade can stabilise access to a current application, but a façade alone does not modernise semantics, data authority or operations. Event interception can support parallel observation, yet an event copied from a legacy log is not automatically an authoritative business event. Each strategy must be judged against the complete traceability chain.

## Slice change into controlled work packages

A migration wave should be small enough to observe and reverse, but large enough to deliver a coherent outcome. Useful partition keys include product, customer segment, legal entity, jurisdiction, channel, transaction type and lifecycle stage.

For Horizon Bank payments, a first work package might cover `HB-SCN-09 Execute an Immediate Domestic Payment`, not every product in `HB-PRD-07 Payment and Cash Management`. Its scope can be traced to:

- `HB-APP-033`, `HB-APP-034`, `HB-APP-035` and `HB-APP-036`;
- `HB-INT-023 Retail Payment Initiation`, `HB-INT-036 Accepted Payment Command` and `HB-INT-064 Immediate Payment Exchange`;
- `HB-SOR-08 Payment Instruction and Processing Authority`;
- `HB-ACC-14 Payment Settlement Recognised`;
- `HB-CTRL-14 Payment Instruction, Entitlement and Funds Validation` and `HB-CTRL-15 Payment Duplicate and Idempotency Control`;
- `HB-REC-012 Payment Instruction to Processing Status`, `HB-REC-013 Payment Clearing Submission and Response` and `HB-REC-014 Settlement Account and Payment Ledger`; and
- `HB-TECH-009 Payments Processing Classification`.

This scope still needs country rules, network finality, exception paths and quantitative recovery objectives before implementation. The catalogue's gaps are inputs to planning, not inconvenient fields to remove.

## Treat data migration as governed state transfer

Copying tables is only one technical step. A data migration transfers business state and responsibility. It must preserve identity, meaning, balances, lifecycle status, relationships, evidence and retention obligations.

### 1. Define the population

Specify which entities and records move, including dormant, blocked, closed, disputed and in-flight items. Define inclusion and exclusion rules in business language before expressing them as queries.

### 2. Assign source and target authority

For each data purpose and lifecycle stage, name the source authority before cutover, the authority during coexistence and the authority afterwards. `HB-SOR-08` is the governed authority assignment for payment instructions and processing, while `HB-APP-080 Operational Data Store` remains a derived operational copy. Moving a copy must not silently transfer authority.

### 3. Map meaning, not just fields

Record source concept, target concept, transformation, defaulting rule, precision, code translation, ownership and unresolved ambiguity. A value called `status` may mean acceptance, clearing, settlement or customer-visible completion in different applications. One-to-one column mapping can therefore be wrong even when every value loads.

### 4. Profile and cleanse under control

Measure invalid, missing, duplicated and contradictory records. Remediation needs an owner and an audit trail. The target platform should not hide source-quality problems by silently inventing defaults.

### 5. Rehearse extraction, transformation and loading

Use repeatable runs against controlled snapshots. Capture source counts, accepted records, rejected records, transformations and checksums where appropriate. Protect sensitive data in non-production environments.

### 6. Reconcile business outcomes

Technical row counts are necessary but insufficient. Reconcile balances, instructions, postings and lifecycle states through the applicable governed controls. For the payment example, `HB-REC-012` proves instruction and processing alignment, while `HB-REC-014` addresses settlement and ledger alignment. Breaks require classification, ownership and an authorised disposition.

### 7. Retain lineage and evidence

The migration record should link old and new identifiers, rule versions, execution time, approvals, exceptions and remediation. `HB-APP-083 Metadata and Data Lineage Platform` is a target application for governed lineage. Until it is available, the transition needs an explicit evidence store and owner rather than an undocumented spreadsheet.

## Design coexistence deliberately

Parallel operation can mean several different things:

- shadow reading, where the target observes but does not decide;
- shadow calculation, where results are compared without business effect;
- population split, where different records have different authorities;
- functional split, where lifecycle stages are allocated between applications; or
- dual processing, where both execute and results are compared.

Dual writing is especially risky. Two writers can create conflicting truth, ambiguous ordering and duplicate financial effects. If it cannot be avoided, the design must state the writer of record, conflict rule, idempotency key, repair owner and stopping condition.

Temporary interfaces must be catalogued like permanent ones. They need owners, security classification, observability and retirement criteria. A bridge that survives because nobody recorded its exit condition becomes the next legacy dependency.

## Prepare cutover, rollback and recovery together

A cutover plan answers who authorises the move, what is frozen, what is migrated, how readiness is tested, how traffic changes and who declares success. A rollback plan answers which actions are reversible, how authority returns, how new records are preserved and how financial effects are reconciled.

Rollback is not always a switch back. Once an external payment has been accepted or settled, reversing the technical route cannot erase the business event. The safe response may be forward recovery, exception processing and accounting adjustment. The decision must be made at the business-state level.

The operational rehearsal should include:

- partial migration and rejected records;
- duplicate or delayed messages;
- loss of an external-network connection;
- inconsistent settlement and ledger state;
- inaccessible identity or cryptographic services;
- target unavailability after some transactions complete; and
- recovery followed by reconciliation and controlled failback.

`HB-SCN-19 Recover Payment Service after Cyber Disruption` provides the broader recovery scenario. `HB-APP-086 Enterprise Observability Platform`, `HB-APP-087 Information Technology Service Management`, `HB-APP-088 Configuration and Service Inventory` and `HB-APP-090 Resilience Orchestration and Recovery` support the target operating model. `HB-APP-087` is a current record, while `HB-APP-086`, `HB-APP-088` and `HB-APP-090` are proposed target records. A transition cannot assume the proposed responsibilities already provide complete evidence.

## Decommission the old responsibility, not only the server

Decommissioning is complete when the old application no longer carries an ungoverned business, data, control or evidence responsibility. Before retirement, confirm:

- all live consumers have moved or been removed;
- data is migrated, retained or disposed under an approved rule;
- legal holds and audit evidence remain accessible;
- reconciliation breaks and in-flight cases are resolved;
- access, keys, certificates, jobs and network routes are revoked;
- monitoring and support obligations are closed;
- contracts and licences are handled by their owners; and
- the repository records the final state and superseding relationships.

Turning off compute while leaving a nightly file, regulatory extraction or dispute archive dependent on the platform is not decommissioning.

## Common mistakes

### Starting with a target technology

This hides the outcome, responsibility and data-authority questions. Start with the business seam and evidence.

### Calling every intermediate state a transition architecture

A list of partially delivered components is not coherent. Record population routing, authority, controls, ownership and exit conditions.

### Measuring only migrated records

Record counts do not prove balances, lifecycle state, accounting or customer outcomes. Use business reconciliations.

### Assuming a BIAN mapping selects a service boundary

BIAN can clarify logical banking responsibilities. Implementation boundaries still require transaction, data, risk, team and operational reasoning.

### Planning rollback after cutover design

Rollback and forward recovery affect data authority and contract design. They must be designed with the cutover.

### Keeping bridges without expiry

Every temporary adapter, copy and manual control needs an owner, measure and retirement condition.

## Chapter summary

Modernisation is a controlled transfer of responsibility. The architecture must describe current, transition and target states, choose a defensible seam, govern data authority, reconcile outcomes and prepare operations for coexistence and recovery. A roadmap becomes credible only when its work packages link to applications, interfaces, records, controls and critical operations.

## Completion checklist

- [ ] The business outcome and migration seam are explicit.
- [ ] Current, transition and target responsibilities are distinguishable.
- [ ] Every affected application, interface and external network has an owner.
- [ ] Data authority is defined before, during and after transition.
- [ ] In-flight, exceptional, dormant and historical records are covered.
- [ ] Accounting and reconciliation evidence is specified.
- [ ] Coexistence, cutover, rollback and forward-recovery paths are rehearsable.
- [ ] Temporary elements have exit conditions.
- [ ] Decommissioning covers records, consumers, access, operations and obligations.
- [ ] Remaining gaps are explicit and governed.

## Key takeaways

- Modernise responsibilities and outcomes, not system names.
- A transition architecture is an operable state, not an incomplete target diagram.
- Data migration transfers meaning, authority and evidence as well as values.
- Reconciliation is the proof of financial and lifecycle integrity.
- Coexistence needs one explicit authority for every purpose and stage.
- Rollback may require forward business recovery rather than technical reversal.
- BIAN mappings inform responsibility analysis but do not dictate deployment.

## Practical exercise

Choose `HB-SCN-04 Open and Fund a Transaction Account`. Draft one transition work package that introduces a target component while retaining `HB-APP-020 Deposit Account Processing` as the account authority.

Your answer should identify the population, current and target responsibility, interfaces, authoritative data, at least two reconciliations, a cutover gate, a rollback or forward-recovery rule and an exit condition. A strong answer will use `HB-SOR-02`, `HB-REC-002`, `HB-REC-003` and the relevant deposit controls without claiming that a candidate BIAN mapping is a deployable service.

## Review checklist

- [ ] Does each view answer a named migration question?
- [ ] Are current facts separated from target recommendations?
- [ ] Is every governed identifier exact and machine-checkable?
- [ ] Are financial effects, customer outcomes and control evidence preserved?
- [ ] Are quantitative targets absent unless approved evidence supports them?
- [ ] Can operators explain recovery from a partially completed cutover?
- [ ] Are source claims distinguished from Horizon Bank author-model choices?

## References and further reading

- [BCBS-OP-RISK-2021], source note: `research/banking/part-v-53-56/bcbs-operational-risk-2021.md`.
- [BCBS-OPERATIONAL-RESILIENCE-2021], source note: `research/banking/bcbs-operational-resilience-2021.md`.
- [BIAN-SERVICE-LANDSCAPE-14], source note: `research/bian/bian-service-landscape-14.0.md`.
