---
title: "Measures, Quality Gates and the Full-Bank Coverage Audit"
chapter: 55
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 55. Measures, Quality Gates and the Full-Bank Coverage Audit

## Chapter purpose

Measures make architecture claims testable. Quality gates stop work from advancing when essential evidence is absent. A coverage audit asks whether the bank model connects every required viewpoint, not whether the repository contains many files.

This chapter answers: **How can reviewers test that Horizon Bank's full-bank architecture is complete enough, internally consistent and useful for a decision?** It defines a reproducible audit method without inventing performance targets or claiming that an unresolved record is complete.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish activity, coverage, quality, outcome and risk measures;
- define a measure with scope, owner, calculation and evidence;
- apply quality gates across business, data, application, integration, control and operations;
- audit the master coverage matrix against the governed catalogues;
- recognise false completeness and misleading percentages; and
- record findings so that remediation can be verified.

## Prerequisites and dependencies

- Chapter 49, for traceability rules;
- Chapters 50 to 52, for implementation and operational evidence;
- Chapter 53, for transition evidence; and
- Chapter 54, for decision rights and repository governance.

## Required models and artefacts

- controlled catalogue schemas and vocabularies;
- master coverage matrix;
- scenario catalogue;
- metric definitions and evidence register;
- quality-gate record;
- review findings and decision log; and
- automated validation results.

## Worked examples

The chapter audits `HB-SCN-09 Execute an Immediate Domestic Payment` and compares it with the present master coverage matrix. It also samples `HB-SCN-16 Close the Books and Submit a Regulatory Return` to show why accounting, reconciliation and reporting lineage need their own evidence.

## Source requirements

The Basel Committee on Banking Supervision (BCBS) principles numbered 239 support attention to governance, data architecture, accuracy, completeness, timeliness, reconciliation and validation in risk data aggregation and reporting [BCBS-239]. Basel operational-resilience guidance supports mapping critical operations and dependencies and testing continuity [BCBS-OPERATIONAL-RESILIENCE-2021]. Corporate-governance guidance supports clear decision rights and independent challenge [BCBS-CORPORATE-GOVERNANCE-2015]. The measures, gates and audit procedure below are author recommendations for Horizon Bank. Banking Industry Architecture Network (BIAN) mappings are governed separately.

## Measure what the architecture is meant to improve

A measure needs a decision. “Number of APIs” can be counted, but it does not show that interfaces are understandable, controlled or reusable. “Number of BIAN mappings” can reward speculative mapping. “Percentage modernised” is meaningless until the denominator and evidence of completion are defined.

Use five measure families together:

| Family | Question | Example |
|---|---|---|
| Activity | What work was performed? | Catalogue records reviewed this period |
| Coverage | Which required scope is represented? | Scenarios with an explicit control and reconciliation |
| Quality | Is the representation valid and useful? | References that resolve and mappings with evidence |
| Outcome | Did a customer, business or operational result improve? | Payment exceptions resolved within an approved service objective |
| Risk | What exposure or uncertainty remains? | Critical-operation dependencies without tested recovery evidence |

Activity is useful for managing work, not proving value. Coverage shows reach, not correctness. Quality shows trustworthiness, not business benefit. Outcome and risk measures connect architecture to operation, but need baselines and approved targets outside the architecture repository.

## Define every measure before using it

A measure record should state:

- name and decision supported;
- population and exclusions;
- numerator and denominator, where applicable;
- data sources and authority;
- calculation and treatment of `Pending`;
- frequency and effective time;
- owner and reviewer;
- baseline and approved target;
- quality limitations; and
- action when the result breaches its threshold.

For example, **scenario reconciliation coverage** can be defined as:

```text
governed scenarios with at least one applicable reconciliation
--------------------------------------------------------------
governed scenarios for which financial or state alignment applies
```

The denominator must exclude scenarios where reconciliation is genuinely not applicable, but not scenarios where the relationship is merely unknown. `Pending` belongs in the gap population. The repository does not currently hold an approved target percentage, so the chapter does not invent one.

## Use balanced architecture measures

### Business measures

Business measures relate to the outcome represented by a scenario or value stream. Examples include completed journeys, exception outcomes, customer communication completeness and product adoption. The architecture must link to the operational source rather than duplicating results manually.

### Architecture measures

Useful architecture measures include resolved-reference rate, owned-record rate, verified-mapping rate, relationship coverage, exception age and view freshness. They reveal repository fitness. They do not prove that the business service performs well.

### Technology and operations measures

Operational evidence can include service availability, change failure, recovery exercise outcomes, alert actionability and unresolved dependency gaps. Targets require an approved service context. `Tier 1` in the application catalogue is a qualitative resilience classification, not a promised recovery time.

### Risk and compliance measures

These may include controls without evidence, overdue findings, unverified source mappings, data-quality exceptions and critical-operation dependencies without tested arrangements. Regulatory applicability and thresholds must be determined by the relevant jurisdiction and legal entity.

## Build quality gates around evidence

A quality gate is a decision point with explicit entry evidence, pass conditions, approver and failed-gate action. It is not a score that can hide a blocking defect.

### Gate 1: Catalogue integrity

Pass when required files and columns exist, identifiers and prefixes are valid, definitions and owners are present, controlled values are valid, hierarchy rules hold and references resolve. Automated validation supplies most of this evidence.

Fail when a record has a duplicate ID, orphan parent, unknown reference, uncontrolled name or invalid scope. `Pending` is allowed only where the schema permits it and the gap explains what is unresolved.

### Gate 2: Semantic and BIAN integrity

Pass when business responsibilities are distinguishable, mapping sources and versions are recorded, confidence and verification are visible, and no text equates a Service Domain with a microservice, application, team or database.

Fail when a BIAN name is inferred from memory, a reference-model term replaces the bank's actual responsibility, or a candidate mapping is presented as verified.

### Gate 3: Scenario completeness

Pass when the scenario has a trigger, observable outcome, accountable business owner, applications, information, interfaces, controls and operational consequences. Add accounting and reconciliation whenever the scenario creates or changes financial or governed state.

Fail when the “happy path” ends at an application programming interface (API) response, or exceptions and customer communication are omitted.

### Gate 4: Information and financial integrity

Pass when authoritative data is assigned by purpose and lifecycle stage, transformations are traceable, accounting consequences are explicit and reconciliations have owners and break treatment.

Fail when a reporting platform is assumed to be authoritative merely because it aggregates data, or when record counts substitute for balance and state reconciliation.

### Gate 5: Security, resilience and operations

Pass when identity, access, sensitive-data handling, monitoring, support, recovery, external dependencies and critical operations have named responsibilities and review evidence.

Fail when resilience is claimed from duplicate components alone, or when no operator can describe degraded operation and recovery.

### Gate 6: Transition readiness

Pass when current, transition and target states are explicit; coexistence and authority are unambiguous; migration is rehearsable; and cutover, rollback, forward recovery and decommissioning have owners.

Fail when a temporary bridge has no exit condition or the target assumes unavailable shared platforms.

### Gate 7: Governance and publication

Pass when decisions, sources, status, exceptions and review findings are current and all required checks succeed. Author and diagram approval remain manual gates.

Fail when a merged file is treated as approved without the authorised review.

## Audit the full-bank coverage matrix reproducibly

The master matrix joins the dimensions that a reviewer needs to follow across the bank. Its required columns include business domain, business line, legal entity, segment, product, value stream, capability, process, organisation, application, authoritative data or system of record, interface, external network, accounting event, reconciliation, control, critical operation, technology or resilience classification, BIAN mapping, scenario, chapter, status and gap.

The audit should use this sequence.

### Step 1: Freeze the audit basis

Record the repository revision, catalogue versions, BIAN version and audit date. A changing working tree cannot provide reproducible evidence.

### Step 2: Validate the structure

Run the catalogue validator. Stop the audit if schemas, identifiers or references fail. Coverage calculations built on invalid relationships are misleading.

### Step 3: Establish the required population

Select the domain families, products, critical operations and scenarios that the audit must cover. Do not use the existing matrix rows as their own denominator. That would report perfect coverage whenever missing rows are absent from both numerator and denominator.

For Part V, the governed scenario catalogue contains 20 separately identified scenario records. At this chapter's audit date, the coverage matrix has 26 rows and references all 20 scenario records. Three enabling rows have no single scenario because they cover enterprise, shared or domain-level responsibilities. This establishes breadth across the governed scenario population, but it does not make every relationship complete or verified.

### Step 4: Test breadth

For every required business-domain family and scenario, test whether at least one row exists and whether the row points to the appropriate chapter. Report missing rows as coverage gaps.

### Step 5: Test depth

For each row, test whether every applicable dimension contains a governed ID of the correct type. `Pending` is counted separately. A populated but semantically wrong ID is a defect, not coverage.

### Step 6: Test coherence

Check whether the linked records can belong to the same scenario. A payment scenario that links a card product, trade process and deposit-only value stream may contain valid IDs but still be incoherent.

### Step 7: Sample source-to-outcome traceability

Select high-risk and representative rows. Trace them from business outcome through application and interface to data authority, accounting, reconciliation, control and operations. Inspect supporting evidence rather than relying only on the matrix.

### Step 8: Classify findings

Use a small severity scheme:

- **Blocking:** the model cannot support the decision or contains a material false claim;
- **Important:** a significant relationship, owner, control or evidence item is absent or inconsistent;
- **Routine:** a local clarity or maintenance issue; and
- **Observation:** an improvement that does not prevent the present decision.

Every finding needs an affected ID, owner, action and verification method. Severity is not a substitute for risk acceptance.

### Step 9: Re-run after repair

Repeat the same validation and audit query. Close a finding only when fresh evidence satisfies its acceptance condition.

## Worked audit: immediate domestic payment

`HB-SCN-09 Execute an Immediate Domestic Payment` provides a compact audit sample.

| Dimension | Expected governed evidence |
|---|---|
| Product and value | `HB-PRD-07`; `HB-VS-04` |
| Applications | `HB-APP-033`; `HB-APP-034`; `HB-APP-035` |
| Interfaces and network | `HB-INT-023`; `HB-INT-064`; `HB-EXT-003` |
| Authoritative information | `HB-DATA-08`; `HB-SOR-08` |
| Financial consequence | `HB-ACC-14` |
| Reconciliation | `HB-REC-012`; `HB-REC-013` |
| Controls | `HB-CTRL-14`; `HB-CTRL-15` |
| Critical operation and technology | `HB-CRIT-02`; `HB-TECH-009` |

Coverage row `HB-COV-010` joins `HB-SCN-09` to all required matrix dimensions using governed IDs. Its gap states that network-finality and recovery-replay detail remains pending in the scenario catalogue. The correct audit conclusion is “required dimensions populated, named scenario detail still pending”, not “the payment architecture is complete”.

## Review viewpoints

### Business review

Check stakeholder outcome, product, value stream, capability, process, owner and scope. Ask whether the model reflects the bank rather than an application menu.

### Information review

Check meaning, authority by lifecycle stage, quality, lineage, privacy, retention and reporting use. Distinguish source authority from derived copies.

### Application and integration review

Check responsibility boundaries, consumer and producer ownership, contract type, direction, versioning, duplicate handling, exception paths and external networks.

### Finance and control review

Check accounting events, subledger and ledger responsibilities, reconciliations, control ownership and evidence. A control name alone does not prove operation.

### Technology and security review

Check deployment assumptions, identity, access, secrets, telemetry, resilience, capacity, failure and recovery. Do not infer quantitative objectives from catalogue tiers.

### Transformation review

Check current, transition and target state, migration population, coexistence, temporary controls and decommissioning.

## Common measurement mistakes

- Using the rows already present as the denominator.
- Counting `Pending` as covered.
- Averaging away a blocking defect.
- Reporting mappings without verification status.
- Treating catalogue validity as proof of operational effectiveness.
- Choosing targets without a baseline, owner or business decision.
- Measuring output volume instead of outcome or risk.
- Closing findings without rerunning the evidence-generating check.

## Chapter summary

Measures and gates make architecture review repeatable. A full-bank audit starts from an independently defined required population, validates catalogue structure, tests row breadth and depth, checks semantic coherence and samples evidence from source to outcome. Horizon Bank's present matrix covers every governed scenario, while its row-level gaps keep unverified mappings and unresolved detail visible. Breadth must not be misreported as complete design evidence.

## Completion checklist

- [ ] Every measure states purpose, population, calculation, owner and evidence.
- [ ] Targets are approved rather than invented.
- [ ] Gate failures cannot be averaged away.
- [ ] The audit denominator comes from governed required scope.
- [ ] `Pending` is reported as a gap.
- [ ] Typed references and semantic coherence are both tested.
- [ ] Accounting, reconciliation, control and operational evidence are sampled.
- [ ] Findings have severity, affected ID, owner and verification method.
- [ ] Repairs are followed by fresh validation.

## Key takeaways

- Counts describe activity unless tied to a decision and denominator.
- Coverage and correctness are different qualities.
- A quality gate needs evidence, an approver and a failed-gate action.
- Never derive the denominator solely from rows that already exist.
- `Pending` is honest uncertainty, not completed coverage.
- Automation proves structural rules; semantic and operational evidence needs review.
- A failed full-bank audit should produce owned repairs, not a softened score.

## Practical exercise

Audit `HB-SCN-16 Close the Books and Submit a Regulatory Return`. Build one expected coverage row using the governed catalogues, then classify any missing or pending relationships.

A strong answer will include `HB-APP-058`, `HB-APP-059`, `HB-APP-060`, `HB-APP-062`, `HB-SOR-04`, `HB-SOR-24`, `HB-REC-030`, `HB-REC-033`, `HB-CTRL-28`, `HB-CTRL-30`, `HB-CTRL-32`, `HB-CRIT-15` and `HB-CRIT-17`. It will not invent the applicable regulatory return, deadline or materiality threshold.

## Review checklist

- [ ] Does the review use an independently defined required population?
- [ ] Are exact IDs used in every sampled trace?
- [ ] Are owner, scope, source and verification status visible?
- [ ] Are gaps separated from defects and accepted exceptions?
- [ ] Does the reviewer inspect evidence beyond the matrix?
- [ ] Are source guidance and author recommendations distinguished?
- [ ] Can another reviewer reproduce the result from the same revision?

## References and further reading

- [BCBS-239], source note: `research/banking/bcbs-239-risk-data-aggregation.md`.
- [BCBS-OPERATIONAL-RESILIENCE-2021], source note: `research/banking/bcbs-operational-resilience-2021.md`.
- [BCBS-CORPORATE-GOVERNANCE-2015], source note: `research/banking/part-v-53-56/bcbs-corporate-governance-2015.md`.
