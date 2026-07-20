---
title: "Governance, Ownership and the Architecture Repository"
chapter: 54
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 54. Governance, Ownership and the Architecture Repository

## Chapter purpose

Architecture governance makes design information usable for decisions. It assigns authority, records evidence, controls change and makes exceptions visible. A repository supports that work, but a folder or modelling tool cannot govern itself.

This chapter answers: **Who is accountable for the full-bank architecture model, how do records change, and what makes the repository trustworthy?** It applies those questions to Horizon Bank's controlled catalogues.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish accountability, stewardship, service ownership and control ownership;
- assign decision rights across group, legal-entity, jurisdiction and product scopes;
- operate a governed change and exception workflow;
- explain how stable identifiers, typed relationships and validation support trust;
- recognise recurring BIAN and repository governance mistakes; and
- design a practical review cadence without confusing approval with file editing.

## Prerequisites and dependencies

- Chapter 49, for full-stack traceability and mapping confidence;
- Chapter 50, for implementation-boundary decisions;
- Chapter 52, for operational ownership; and
- Chapter 53, for transition and migration governance.

## Required models and artefacts

- ownership and decision-rights matrix;
- controlled vocabularies and catalogue schemas;
- change, review, exception and retirement workflow;
- relationship and coverage rules;
- architecture decision records;
- source, status and diagram registers; and
- automated validation plus human review evidence.

## Worked examples

The chapter uses a proposed change to `HB-APP-034 Payment Orchestration` and an update to candidate mapping `HB-BIAN-02 Payment Responsibility Candidate`. It also uses the product-and-price scenario `HB-SCN-20 Change a Product and Price Safely` to show that repository governance must connect business approval and technology adoption.

## Source requirements

Basel Committee guidance supports clear governance responsibilities, board and senior-management oversight, risk governance and independent control functions [BCBS-CORPORATE-GOVERNANCE-2015]. The exact Horizon Bank roles, forums, record types and workflow are fictional author-model choices. Banking Industry Architecture Network (BIAN) Service Landscape 14.0 is the version baseline for candidate mappings [BIAN-SERVICE-LANDSCAPE-14].

## Governance is a decision system

Governance answers four plain questions:

1. Who may propose a change?
2. Who decides whether it is acceptable?
3. What evidence must support that decision?
4. Who checks that the recorded and implemented outcomes still agree?

The architecture board is only one participant. Product owners decide product outcomes, business-process owners govern end-to-end work, data owners decide information meaning and permitted use, application service owners govern service health and change, and control owners decide whether control intent and evidence remain adequate. Legal-entity management and independent assurance retain their own responsibilities.

Good governance makes overlaps explicit. It does not give the central architecture team ownership of every business concept.

## Keep ownership types distinct

Horizon Bank's controlled vocabulary separates four ownership types:

| Ownership type | Governing question | Horizon Bank example |
|---|---|---|
| Accountable owner | Who answers for the business definition or outcome? | `HB-ORG-111 Payments Director Role` for payment direction |
| Steward | Who maintains the controlled information and resolves data-quality issues? | A designated steward working under `HB-ORG-122 Data Owner Role` |
| Service owner | Who answers for an application's service health and controlled change? | Owner of `HB-APP-034 Payment Orchestration` |
| Control owner | Who answers for control design, operation and evidence? | `HB-ORG-124 Control Owner Role` for `HB-CTRL-15 Payment Duplicate and Idempotency Control` |

One person may perform several roles in a small unit, but the responsibilities remain different. “Technology owns it” is not a sufficient owner value because it does not name a decision role.

Ownership must also state scope. A group definition may be implemented by several legal entities, and a country rule may differ by jurisdiction. The separate fields for organisational scope, legal-entity scope, jurisdiction scope and customer-segment scope prevent one vague `Scope` field from hiding those differences.

## Use federated decision rights

A practical bank model combines group consistency with domain expertise and legal-entity accountability.

### Group architecture governance

`HB-ORG-24 Strategy, Architecture and Transformation` maintains enterprise principles, catalogue conventions and cross-domain traceability. It challenges duplicated responsibilities and records material architecture decisions. It does not approve a product, accept a regulatory obligation or operate a payment.

### Domain and product governance

Business domains and product owners decide definitions, lifecycle outcomes and priorities. For example, `HB-DOM-050 Payments` and `HB-PRD-07 Payment and Cash Management` provide the business context for payment changes.

### Data governance

`HB-ORG-17 Data and Analytics` supports common definitions, quality, lineage and authority decisions. A system-of-record assignment is purpose-specific. It must not be interpreted as ownership of every copy or use of the data.

### Technology and service governance

`HB-ORG-16 Technology Architecture, Engineering and Operations` governs implementation, runtime and service-management concerns. Application service ownership remains explicit per application, including `HB-APP-075 API Management Platform`, where API means application programming interface, and `HB-APP-076 Enterprise Event Streaming Platform`.

### Risk, compliance and assurance

`HB-ORG-04 Risk, Compliance and Assurance`, the relevant control owners and `HB-ORG-22 Internal Audit` provide challenge or assurance according to their mandates. Independent assurance does not become the owner of the design it reviews.

## Make the repository a governed model

The repository is more than diagrams. At Horizon Bank it joins controlled records across business, application, information, integration, accounting, control, resilience and scenario dimensions.

Each governed record needs:

- a stable identifier and controlled name;
- a concise definition;
- a named owner and ownership type;
- architecture state and record status;
- separate scope dimensions;
- explicit relationships to other governed identifiers;
- source type, confidence and verification status where applicable; and
- an explicit gap when evidence or coverage is incomplete.

The identifier gives a concept continuity while its attributes evolve. Renaming `HB-APP-034` does not create a new responsibility by itself. Conversely, reusing one identifier for a materially different responsibility destroys history and traceability.

### Catalogue, view and evidence

A **catalogue** stores governed records and relationships. A **view** selects records for a stakeholder question. **Evidence** supports a claim or decision. A diagram may be an effective view, but it is not automatically the authoritative catalogue or proof that the design operates as shown.

The master coverage matrix is a cross-catalogue audit view. It should reference source records rather than duplicate their definitions. `Pending` means a relationship is unresolved. It must be paired with a useful gap, not treated as a passing value.

## Operate a controlled change workflow

A lightweight workflow can still be rigorous.

### 1. Propose

The proposer states the decision, reason, affected IDs, scope and intended architecture state. New records use the correct prefix and schema. Existing records retain their identifiers unless their identity truly changes.

### 2. Analyse impact

Trace inbound and outbound relationships. A proposed change to `HB-APP-034` can affect `HB-INT-036 Accepted Payment Command`, `HB-CTRL-15`, `HB-SOR-08`, `HB-CRIT-02`, `HB-TECH-009` and scenarios `HB-SCN-02` and `HB-SCN-09`. Search results are an impact hypothesis, not the final analysis.

### 3. Review by concern

Business, data, integration, security, operations, finance and risk reviewers evaluate only the concerns relevant to the change. Review evidence should state unresolved assumptions and jurisdiction limits.

### 4. Decide

The authorised owner approves, rejects, defers or requests revision. Significant trade-offs are recorded in an architecture decision record. Automation may report conformance, but it does not replace the accountable decision.

### 5. Implement and verify

The delivery change must reference the governed decision. Verification compares implemented interfaces, data authority, controls and operations with the accepted architecture.

### 6. Publish and monitor

Merge the approved record change, update derived views, run validation and monitor whether later evidence contradicts an assumption. A version-control merge records a change, not an authorisation unless the governance process deliberately makes it one.

## Define conformance without pretending all differences are equal

A practical conformance scale can distinguish:

- **Conformant:** required relationships and controls are implemented with current evidence.
- **Conformant with condition:** the design is accepted subject to a dated, owned action.
- **Approved exception:** a stated rule is not met, but an authorised owner accepts the bounded exposure and review date.
- **Non-conformant:** a required condition is absent and no valid exception exists.
- **Not assessed:** evidence has not yet been reviewed.

These are author recommendations, not current values in the Horizon Bank controlled-vocabulary catalogue. The integration owner should add them only if the repository adopts a dedicated conformance field and validation rule.

## Govern exceptions as temporary decisions

An exception record should include:

- the rule or requirement not met;
- affected IDs, populations and scopes;
- business reason and alternatives considered;
- risk and customer impact;
- compensating controls and evidence;
- accountable approver;
- start, review and expiry conditions; and
- remediation or retirement path.

An exception without an expiry or review trigger is an undocumented target-state change. Repeated exceptions may show that the standard is wrong or that investment is missing. Governance should be able to tell which.

## Version the right things

Git versions repository files, but architecture also has semantic versions and effective times. Product terms, interface contracts, event schemas, reference data and BIAN mappings may each change on different schedules.

For candidate `HB-BIAN-02`, the repository must record BIAN 14.0, source, confidence and verification status. An application relationship to that candidate does not become verified merely because the application record is current. When BIAN changes, assess the mapping. Do not silently change the source version under an existing conclusion.

Superseded records and decisions should remain discoverable. Their status and replacement should be explicit so readers can reconstruct why the current model exists.

## Validate structure and review meaning

Automation is well suited to checking:

- duplicate or malformed identifiers;
- unexpected prefixes;
- missing definitions and owners;
- invalid controlled values;
- unknown or mistyped references;
- hierarchy cycles and invalid parents;
- incomplete table schemas; and
- forbidden abbreviated or ranged identifiers.

Automation cannot decide whether a definition is useful, a boundary is sensible, a BIAN interpretation is sound or a control is effective. Human review must test meaning, completeness and fitness for the decision.

## Use event-driven maintenance as well as a calendar

A quarterly or annual review can catch ageing records, but important architecture changes happen between scheduled reviews. The repository should also react to events: product approval, legal-entity change, interface version, critical incident, control finding, migration cutover, application retirement and a new BIAN release. Each event should identify the catalogue owners who must assess impact.

The calendar remains useful for sampling records that received no event. Review proposed records, long-running exceptions, low-confidence mappings, stale sources and critical-operation dependencies. Record the review date and conclusion even when no change is needed. This distinguishes an actively confirmed record from one that merely survived because nobody inspected it.

## Common governance failures

### BIAN as an information-technology exercise

This omits business ownership, product outcomes, processes, controls and finance. Require business-domain and scenario traceability.

### API-first without capability understanding

An interface can make the wrong boundary easier to consume. Establish responsibility and information semantics first.

### Service Domain equals microservice

This confuses a logical reference boundary with a deployment decision. Record the mapping as many-to-many unless evidence justifies otherwise.

### Big-bang adoption

It increases simultaneous uncertainty across data, controls and operations. Use bounded transition outcomes and explicit coexistence.

### Renaming legacy systems

New terminology does not change responsibility, coupling or authority. Track the underlying change.

### Copying a reference data model or API unchanged

A reference supplies shared semantics, not local legal, product, security or operational decisions. Govern adaptations and provenance.

### Missing ownership

Committee names and generic departments make decisions unactionable. Name accountable roles and scope.

### An unmaintained repository

Stale records create false confidence. Assign review triggers, validation and retirement rules.

### Measuring volume instead of quality

Counts of diagrams, APIs or mappings do not prove coverage or correctness. Chapter 55 defines evidence-based measures and gates.

## Chapter summary

Governance links authority, evidence and change. The repository makes those relationships durable through stable identifiers, controlled fields, explicit references and version history. It remains trustworthy only when owners review meaning, exceptions expire, source versions stay visible and automation checks the rules it can actually prove.

## Completion checklist

- [ ] Every governed record has a definition, owner, status, state and scope.
- [ ] Decision rights distinguish business, data, service, control and assurance roles.
- [ ] Changes identify affected IDs and relationship impact.
- [ ] Material trade-offs have decision records.
- [ ] Exceptions have scope, compensating controls, approver and expiry conditions.
- [ ] BIAN mappings record source version, confidence and verification.
- [ ] Derived views do not compete with authoritative catalogues.
- [ ] Automated checks and human semantic review are both used.
- [ ] Superseded records remain traceable.

## Key takeaways

- Governance is a decision system, not a meeting or tool.
- Accountability, stewardship, service ownership and control ownership answer different questions.
- Stable identifiers preserve meaning across change.
- A repository stores controlled concepts; diagrams present selected views.
- Automation validates structure, while people review meaning and fitness.
- Exceptions need owners, evidence and exit conditions.
- BIAN version and verification must remain visible at the mapping record.

## Practical exercise

Propose a change that makes `HB-APP-034 Payment Orchestration` the coordinator for `HB-SCN-09`. Prepare a one-page governance record with affected IDs, decision owners, required evidence, scope, architecture state, control impact and one possible exception.

A strong answer will distinguish the Payments Director, application service owner, data owner and control owner; retain `HB-SOR-08`; include `HB-CTRL-15`; and avoid treating `HB-BIAN-02` as either a verified mapping or a deployable service.

## Review checklist

- [ ] Is the decision authority named and scoped?
- [ ] Are governance roles distinct from implementation teams?
- [ ] Do record states and source confidence remain visible?
- [ ] Are all relationships explicit governed IDs?
- [ ] Can a reviewer find the evidence and reconstruct the decision?
- [ ] Are exceptions bounded and reviewable?
- [ ] Does repository validation complement rather than replace semantic review?

## References and further reading

- [BCBS-CORPORATE-GOVERNANCE-2015], source note: `research/banking/part-v-53-56/bcbs-corporate-governance-2015.md`.
- [BCBS-OP-RISK-2021], source note: `research/banking/part-v-53-56/bcbs-operational-risk-2021.md`.
- [BIAN-SERVICE-LANDSCAPE-14], source note: `research/bian/bian-service-landscape-14.0.md`.
