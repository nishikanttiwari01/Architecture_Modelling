# Part V Full-Service Bank Redesign Implementation Plan

> **For agentic workers:** Execute this plan task-by-task with review checkpoints. Do not create diagram source until the relevant specification is explicitly approved by the author.

**Goal:** Redesign Chapters 31 to 56 as a governed, traceable and beginner-friendly architecture of Horizon Bank, using BIAN 14.0 as a verified reference rather than a deployable target architecture.

**Architecture:** Controlled Horizon Bank catalogues and a master coverage matrix will be the source of truth. Chapters and diagrams will present governed views over those artefacts. Work proceeds from research and taxonomy, through structural synchronisation and enterprise baselines, into domain groups and implementation chapters, followed by a full-bank audit.

**Formats and tools:** Markdown and Git; CSV or YAML plus generated/readable Markdown where validation benefits; PlantUML as the primary diagram tool; Draw.io for enterprise landscapes; Camunda Modeler for formal BPMN and DMN; Python repository checks.

---

## Old-to-new chapter migration map

| New | New chapter | Principal reusable old material | Migration action |
|---:|---|---|---|
| 31 | BIAN Essentials and the Case-Study Method | 31, 32, 36, 54, 56 | Merge essentials and cautions; remove repetition |
| 32 | How a Full-Service Bank Works | 33, 34, 35 | Expand operating model, economics, lifecycles and interdependencies |
| 33 | Enterprise Business Architecture of Horizon Bank | 33, 34, 35 | Rebuild around governed domains, capabilities, processes, roles and value streams |
| 34 | Full Bank Application and Integration Landscape | 43, 45, 46 | Expand from BIAN mapping to full application and interaction landscape |
| 35 | Enterprise Information and Data Architecture | 47 | Expand into governed domains, authority, lineage and analytical separation |
| 36 | Technology, Security, Resilience and Operating Architecture | 48, 49 | Merge enterprise technology, security, critical operations and support model |
| 37 | Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing | 37 | Broaden scenario into a domain architecture |
| 38 | Deposits, Accounts, Term Deposits, Interest, Fees, Statements and Correspondence | 38 | Broaden account opening into full deposit lifecycle |
| 39 | Lending and Credit | 40 | Broaden consumer origination across products and servicing |
| 40 | Collateral, Limits, Exposure, Collections, Recovery and Credit Risk Lifecycle | 40, 47, 48 | Create new domain architecture from fragments |
| 41 | Payments, Clearing, Settlement, Correspondent Banking and FX | 39 | Broaden cross-border scenario into the payments domain |
| 42 | Cards and Merchant Acquiring | 41 | Broaden fraud scenario into issuing and acquiring, retain fraud drill-down |
| 43 | Corporate Banking, Cash Management and Trade Finance | 42 | Broaden cash-management scenario and add trade finance |
| 44 | Wealth, Investments, Securities, Custody and Asset Servicing | none | New domain chapter |
| 45 | Treasury, Markets, Funding, Liquidity, ALM and Capital | none | New domain chapter |
| 46 | Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting | fragments in 38 to 42, 47 | New enterprise finance backbone |
| 47 | Risk, Compliance, Financial Crime, Fraud, Audit and Legal | 41, 48 | Expand controls into an enterprise domain |
| 48 | Channels, Communications, Documents, Workflow, Case Management and Shared Services | 37, 48 | Consolidate shared capabilities and channels |
| 49 | BIAN Mapping Method and Full-Stack Traceability | 32, 35, 36, 43, 56 | Turn cautions into a governed many-to-many method |
| 50 | BIAN-Aligned Application, Service and Team Boundaries | 43, 44 | Merge application mapping and software-service boundary guidance |
| 51 | APIs, Events, Batch, Files, Workflow and External Networks | 45, 46 | Expand interaction styles and external ecosystem |
| 52 | Deployment, Security, Resilience, Observability and Operations | 48, 49 | Merge operational implementation concerns |
| 53 | Legacy Modernisation, Data Migration and Transition Architecture | 50, 51 | Merge migration and roadmap material |
| 54 | Governance, Ownership and the Architecture Repository | 52 | Expand governance into controlled repository practice |
| 55 | Measures, Quality Gates and the Full-Bank Coverage Audit | 53, 54, 55 | Consolidate measures, mistakes and review gates |
| 56 | Integrated End-to-End Scenarios and Practitioner Reference | 36 to 42, 56 | Reuse scenarios as integrated threads and consolidate reference material |

## Phase 0: Baseline and author checkpoint

- [x] Record branch, working-tree state and baseline commit.
- [x] Inspect all Part V chapters and controlled Horizon Bank files.
- [x] Inspect Part V diagram register, specifications, sources and exports.
- [x] Inspect BIAN and banking research notes and source registers.
- [x] Produce the current-state audit and full-domain gap matrix.
- [x] Produce the old-to-new migration map and phased redesign plan.
- [x] Mark Chapters 31 to 56 as `Revision Required` without marking anything approved.
- [ ] Author reviews the chapter structure, filename strategy, scope assumptions, principles and diagram priorities.

## Phase 1: Research and governed taxonomy

- [ ] Record Horizon Bank legal-entity, geography, customer, product, channel and current-state assumptions.
- [ ] Create official BIAN 14.0 source notes and register the release sources.
- [ ] Add primary sources for prudential risk, resilience, financial crime, payments, cards, accounting, impairment, security and securities.
- [ ] Expand the controlled business-domain, product, capability, process, organisation and role catalogues.
- [ ] Expand the application, data-domain, system-of-record, interface, external-network, accounting-event, control, critical-operation and technology catalogues.
- [ ] Create the BIAN mapping register with exact names, version, rationale, status and confidence.
- [ ] Create the scenario catalogue.
- [ ] Create the machine-readable master coverage matrix and readable summary.
- [ ] Add validation for duplicate IDs, mandatory blanks, unknown catalogue references and orphaned relationships.
- [ ] Run validation and resolve or document every baseline gap.

## Phase 2: Structural redesign

- [ ] Confirm chapter purposes, outcomes, dependencies and exclusions for Chapters 31 to 56.
- [ ] Synchronise the approved detailed outlines in `BOOK_PLAN.md` and all Part V chapter files.
- [ ] Apply the author-approved filename strategy using `git mv` where renames are chosen.
- [ ] Update the table of contents, internal links, build order and status tracker.
- [ ] Record structural decisions and architecture principles in `DECISIONS.md`.
- [ ] Register enterprise diagram entries and create specifications only.
- [ ] Stop for author approval of every specification before source creation.

## Phase 3: Enterprise baseline, Chapters 31 to 36

- [ ] Draft Chapter 31 from verified BIAN 14.0 sources and the governed mapping method.
- [ ] Draft Chapter 32 with the whole-bank operating model, economics and lifecycle distinctions.
- [ ] Draft Chapter 33 from the business, capability, process, role and value-stream catalogues.
- [ ] Draft Chapter 34 from the application, interface and external-network catalogues.
- [ ] Draft Chapter 35 from data-domain, authority, lineage, quality and analytical architecture artefacts.
- [ ] Draft Chapter 36 from technology, security, control, critical-operation and operating-model artefacts.
- [ ] After author approval, create, render and visually validate enterprise figures.
- [ ] Run banking, enterprise-architecture, BIAN, application, data, control, operations, pedagogical, source and naming reviews.

## Phase 4: Domain groups

- [ ] Group A: draft and review Chapters 37 to 40.
- [ ] Run the Group A cross-domain consistency review.
- [ ] Group B: draft and review Chapters 41 to 43.
- [ ] Run the Group B cross-domain consistency review.
- [ ] Group C: draft and review Chapters 44 to 46.
- [ ] Run the Group C cross-domain consistency review.
- [ ] Group D: draft and review Chapters 47 and 48.
- [ ] Run the Group D cross-domain consistency review.
- [ ] For every domain, confirm lifecycle, exceptions, accounting, reconciliation, controls, critical operations, applications, data, interfaces and candidate BIAN mappings.

## Phase 5: Implementation and transformation, Chapters 49 to 56

- [ ] Draft Chapter 49 using the verified BIAN mapping register and coverage matrix.
- [ ] Draft Chapter 50 using governed application, service and team-boundary decisions.
- [ ] Draft Chapter 51 using the interface and external-network catalogues.
- [ ] Draft Chapter 52 using deployment, security, resilience, observability and operations catalogues.
- [ ] Draft Chapter 53 using current, transition and target states plus measurable decommissioning.
- [ ] Draft Chapter 54 using repository governance and ownership artefacts.
- [ ] Draft Chapter 55 using executable validation and quality gates.
- [ ] Draft Chapter 56 by reusing governed scenarios, without inventing new names.

## Phase 6: Full-bank audit and completion gate

- [ ] Run all ten required review passes.
- [ ] Run `python scripts/check-structure.py` and require success.
- [ ] Run `python scripts/check-links.py` and require success.
- [ ] Run `python scripts/check-terminology.py` and require success.
- [ ] Run `python scripts/validate-diagrams.py` and require success.
- [ ] Run `python scripts/check-diagram-register.py` and require success.
- [ ] Run `python scripts/word-count.py` and review the report.
- [ ] Run `python scripts/build-book.py` and require success.
- [ ] Run the coverage-matrix validation and resolve or justify every gap.
- [ ] Move a chapter to `Ready for Author Approval` only when the `WORKFLOW.md` definition and all Part V gates are met.

## Immediate approval requests

Before Phase 1 causes structural or diagram changes, the author should decide:

1. Whether to accept the redesigned Chapter 31 to 56 titles and scopes.
2. Whether filenames should be renamed immediately after outline approval or retained until prose migration is complete.
3. Whether Horizon Bank is modelled as one regulated bank in one primary jurisdiction with cross-border services, or as a multi-entity group.
4. Whether the 20 proposed architecture principles in the master instruction should be recorded individually or as one governing decision.
5. Which enterprise diagram specifications should be prepared first after catalogue coherence.
