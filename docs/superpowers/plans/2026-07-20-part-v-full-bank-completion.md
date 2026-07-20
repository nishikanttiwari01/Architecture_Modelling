# Part V Full-Bank Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete Chapters 31 to 56 against a validated, realistic full-service-bank architecture foundation.

**Architecture:** Work proceeds through a hard-gated foundation, parallel domain-writing streams, parallel cross-cutting streams and final integration. Shared catalogues and registers have one integration owner; parallel agents receive exclusive chapter and research-note files and return proposed shared changes for integration.

**Tech Stack:** Markdown, CSV, Python 3 catalogue validators and repository checks, Git, official primary-source research.

---

## File ownership map

- Foundation integration owner: `examples/horizon-bank/`, `scripts/validate_horizon_bank.py`, `scripts/test_validate_horizon_bank.py`.
- Domain stream A: Chapters 37–40 and dedicated notes under `research/banking/part-v-37-40/`.
- Domain stream B: Chapters 41–44 and dedicated notes under `research/banking/part-v-41-44/`.
- Domain stream C: Chapters 45–48 and dedicated notes under `research/banking/part-v-45-48/`.
- Cross-cutting stream A: Chapters 49–52 and dedicated notes under `research/bian/part-v-49-52/`.
- Cross-cutting stream B: Chapters 53–56 and dedicated notes under `research/banking/part-v-53-56/`.
- Final integration owner: Chapters 31–36, `BOOK_PLAN.md`, `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, registers and Part V review reports.

Parallel chapter agents must not edit shared catalogues or registers. They record proposed additions in their hand-off report using full IDs or clearly described ID requests.

### Task 1: Establish isolated execution and baseline

**Files:**
- Read: `AGENTS.md`, `BOOK_PLAN.md`, `STATUS.md`, `WORKFLOW.md`, `STYLE_GUIDE.md`, `SOURCE_POLICY.md`, `DECISIONS.md`, `GLOSSARY.md`
- Read: `docs/superpowers/specs/2026-07-20-part-v-full-bank-completion-design.md`
- Test: all commands below

- [ ] Detect whether the workspace is already isolated with `git rev-parse --git-dir`, `git rev-parse --git-common-dir`, `git branch --show-current` and the submodule guard.
- [ ] Preserve unrelated user changes. If the normal checkout is clean and worktree creation is permitted, create an ignored `.worktrees/part-v-completion` worktree on `part-v-completion`; otherwise work in place because the author explicitly authorised execution.
- [ ] Run `python -m unittest scripts.test_validate_horizon_bank` and expect all tests to pass.
- [ ] Run `python scripts/validate_horizon_bank.py` and expect `Horizon Bank catalogue validation passed.`
- [ ] Run the six required repository checks and record the baseline.

### Task 2: Expand validator contracts before catalogues

**Files:**
- Modify: `scripts/test_validate_horizon_bank.py`
- Modify: `scripts/validate_horizon_bank.py`
- Modify: `.github/workflows/validate.yml` only if new validation commands are introduced

- [ ] Add failing tests requiring the business-domain, capability, application, interface, external-network, reconciliation, technology/resilience and scenario catalogues.
- [ ] Add failing tests for expected prefixes, required columns, controlled fields, typed references, hierarchy rules and coverage-matrix reference types for every new catalogue.
- [ ] Run `python -m unittest scripts.test_validate_horizon_bank` and confirm failures identify missing contracts.
- [ ] Implement schema and relationship validation without weakening existing checks.
- [ ] Run the unit tests and live validator until both pass after Task 3 catalogue creation.

### Task 3: Build the full governed foundation

**Files:**
- Create: `examples/horizon-bank/business-domains.md`
- Replace governed content: `examples/horizon-bank/capabilities.md`
- Create: `examples/horizon-bank/applications.md`
- Create: `examples/horizon-bank/interfaces.md`
- Create: `examples/horizon-bank/external-networks.md`
- Create: `examples/horizon-bank/reconciliations.md`
- Create: `examples/horizon-bank/technology-resilience.md`
- Modify: all existing governed catalogues under `examples/horizon-bank/`
- Modify: `examples/horizon-bank/coverage-matrix.csv`
- Modify: `examples/horizon-bank/README.md`, `coverage-summary.md`, `controlled-vocabularies.md`

- [ ] Catalogue all business domains and subdomains listed in the approved design with stable IDs, definitions, owners and explicit relationships.
- [ ] Create a hierarchical capability baseline spanning customer, products, transactions, finance, risk, compliance, operations and shared services.
- [ ] Create a realistic logical-application estate covering every responsibility family in the design. Use separate applications where lifecycle, owner, data authority or operational boundary differs; do not inflate the estate with vendor modules or duplicate aliases.
- [ ] Catalogue typed APIs, events, messages, files, batch, workflow and external exchanges, including direction, producer, consumer, information, security classification and lifecycle state.
- [ ] Complete process, organisation, data, authoritative-source, accounting-event, reconciliation, control, critical-operation, technology/resilience, BIAN and scenario relationships.
- [ ] Expand the coverage matrix so every domain family has at least one complete traceability row and every unresolved dimension uses `Pending` plus a gap.
- [ ] Run validator tests and the live validator. Repair duplicate, orphan, malformed, unknown, mistyped and hierarchy errors until clean.
- [ ] Record material taxonomy decisions in `DECISIONS.md` and a concise entry in `CHANGELOG.md`.

### Task 4: Draft Chapters 37–40

**Files:**
- Modify: `manuscript/part-05-bian-case-study/37-customer-onboarding-scenario.md`
- Modify: `manuscript/part-05-bian-case-study/38-current-account-opening-scenario.md`
- Modify: `manuscript/part-05-bian-case-study/39-cross-border-payment-scenario.md`
- Modify: `manuscript/part-05-bian-case-study/40-consumer-loan-origination-scenario.md`
- Create: source notes under `research/banking/part-v-37-40/`

- [ ] Read each target chapter, its immediate neighbours, relevant catalogue records and research notes.
- [ ] Research missing customer/party/KYC, deposit, lending, collateral, limits, exposure, collections and recovery facts from primary sources.
- [ ] Write complete chapter prose following each approved outline and the chapter quality contract.
- [ ] Trace applications, information, interfaces, accounting events, controls, resilience and BIAN candidates using governed IDs.
- [ ] Run terminology and link checks; self-review for beginner clarity, factual separation and unsupported precision.
- [ ] Return shared-catalogue requests without editing shared files.

### Task 5: Draft Chapters 41–44

**Files:**
- Modify: `manuscript/part-05-bian-case-study/41-card-fraud-investigation-scenario.md`
- Modify: `manuscript/part-05-bian-case-study/42-corporate-cash-management-scenario.md`
- Modify: `manuscript/part-05-bian-case-study/43-mapping-bian-to-applications.md`
- Modify: `manuscript/part-05-bian-case-study/44-bian-aligned-software-services.md`
- Create: source notes under `research/banking/part-v-41-44/`

- [ ] Research and draft complete payment, cards/acquiring, corporate/trade and wealth/custody chapters.
- [ ] Distinguish payment initiation, clearing, settlement, correspondent banking and foreign exchange.
- [ ] Distinguish card issuing, processing, schemes, disputes, fraud and merchant acquiring.
- [ ] Cover cash management and the complete trade-finance lifecycle without mapping it to deposit acquisition.
- [ ] Cover investment, portfolio, securities, custody, corporate actions and asset servicing responsibilities.
- [ ] Use only governed IDs and return shared-catalogue requests to the integration owner.
- [ ] Run terminology and link checks and complete the chapter quality self-review.

### Task 6: Draft Chapters 45–48

**Files:**
- Modify: `manuscript/part-05-bian-case-study/45-bian-semantic-apis.md`
- Modify: `manuscript/part-05-bian-case-study/46-bian-events.md`
- Modify: `manuscript/part-05-bian-case-study/47-bian-data-architecture.md`
- Modify: `manuscript/part-05-bian-case-study/48-bian-security-control-architecture.md`
- Create: source notes under `research/banking/part-v-45-48/`

- [ ] Research and draft complete treasury/markets, finance/accounting, risk/compliance and shared-service chapters.
- [ ] Keep general ledger, subledger, accounting event and reconciliation responsibilities explicit.
- [ ] Separate enterprise risk, compliance, AML, sanctions, fraud, audit and legal responsibilities.
- [ ] Cover channels, communications, documents, workflow and case management as distinct shared capabilities and applications.
- [ ] Use governed IDs, return shared changes to the integration owner, and run chapter checks.

### Task 7: Integrate domain findings and review Chapters 37–48

**Files:**
- Modify: affected files under `examples/horizon-bank/`
- Create: `reviews/part-05/chapters-37-48-spec-review.md`
- Create: `reviews/part-05/chapters-37-48-quality-review.md`

- [ ] Evaluate every catalogue request from Tasks 4–6 against the governed taxonomy and assign stable IDs only where the responsibility is distinct.
- [ ] Update explicit relationships and coverage rows, then run all catalogue tests.
- [ ] Review every chapter against the approved design and its repository outline; list and repair omissions.
- [ ] Review accuracy, sources, beginner readability, terminology and cross-chapter duplication; repair all Critical and Important findings.
- [ ] Confirm Chapters 37–48 do not contradict the catalogues.

### Task 8: Draft Chapters 49–52

**Files:**
- Modify: `manuscript/part-05-bian-case-study/49-bian-deployment-operations.md`
- Modify: `manuscript/part-05-bian-case-study/50-legacy-to-bian-migration.md`
- Modify: `manuscript/part-05-bian-case-study/51-bian-adoption-roadmap.md`
- Modify: `manuscript/part-05-bian-case-study/52-bian-governance.md`
- Create: source notes under `research/bian/part-v-49-52/`

- [ ] Explain a defensible BIAN mapping method with source, confidence and verification status.
- [ ] Define application, software-service, deployment and team boundaries without one-to-one BIAN assumptions.
- [ ] Cover API, event, command, batch, file, workflow and external-network patterns using catalogue examples.
- [ ] Cover deployment, identity, security, resilience, observability, incident and operational ownership.
- [ ] Run chapter checks and return shared-catalogue changes to the integration owner.

### Task 9: Draft Chapters 53–56

**Files:**
- Modify: `manuscript/part-05-bian-case-study/53-bian-success-measures.md`
- Modify: `manuscript/part-05-bian-case-study/54-bian-common-mistakes.md`
- Modify: `manuscript/part-05-bian-case-study/55-bian-review-checklist.md`
- Modify: `manuscript/part-05-bian-case-study/56-bian-quick-reference.md`
- Create: source notes under `research/banking/part-v-53-56/`

- [ ] Draft modernisation, data migration and transition architecture using current, transition and target states.
- [ ] Draft governance, ownership and repository operation tied to the controlled catalogues.
- [ ] Define measurable quality gates and a reproducible full-bank coverage audit without invented performance targets.
- [ ] Build integrated scenarios spanning party, products, transactions, accounting, controls, applications, interfaces and operations.
- [ ] Run chapter checks and return shared changes to the integration owner.

### Task 10: Reconcile and complete Chapters 31–36

**Files:**
- Modify: all Chapter 31–36 files under `manuscript/part-05-bian-case-study/`
- Create: dedicated source notes under `research/bian/part-v-31-36/` and `research/banking/part-v-31-36/`

- [ ] Replace preliminary or sparse passages with complete catalogue-backed explanations.
- [ ] Ensure Chapter 34 represents the realistic application and integration landscape created in Task 3.
- [ ] Ensure Chapters 35 and 36 represent full information, technology, security, resilience and operating architectures.
- [ ] Cross-reference later domain and cross-cutting chapters without duplicating their detailed teaching.
- [ ] Run chapter checks and quality review.

### Task 11: Final source, consistency and governance integration

**Files:**
- Modify: `SOURCE_REGISTER.md`, `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, `GLOSSARY.md` only where evidence requires it
- Create: `reviews/part-05/part-v-final-technical-review.md`
- Create: `reviews/part-05/part-v-final-beginner-review.md`
- Create: `reviews/part-05/part-v-final-consistency-review.md`
- Create: `reviews/part-05/part-v-final-source-review.md`

- [ ] Register every meaningful new source note and verify access dates, versions and primary URLs.
- [ ] Check every Chapter 31–56 purpose, reader outcome, prerequisite and planned section against the manuscript.
- [ ] Check every governed ID in prose against the live catalogues and remove uncontrolled aliases.
- [ ] Check BIAN statements for verified source, candidate status and non-equivalence guardrails.
- [ ] Repair all Critical and Important review findings and rerun reviews.
- [ ] Set chapter statuses no higher than `Under Review`, and only where `WORKFLOW.md` conditions are met.

### Task 12: Final verification, commit and push

**Files:**
- Verify: entire repository

- [ ] Run `python -m compileall -q scripts`.
- [ ] Run `python -m unittest scripts.test_validate_horizon_bank`.
- [ ] Run `python scripts/validate_horizon_bank.py`.
- [ ] Run `python scripts/check-structure.py`.
- [ ] Run `python scripts/check-links.py`.
- [ ] Run `python scripts/check-terminology.py`.
- [ ] Run `python scripts/validate-diagrams.py`.
- [ ] Run `python scripts/check-diagram-register.py`.
- [ ] Run `python scripts/word-count.py`.
- [ ] Run `git diff --check` and inspect all changed files for scope violations, placeholders, generated diagram sources and secrets.
- [ ] Repeat repair and verification until every required command exits zero.
- [ ] Commit focused implementation checkpoints, push the authorised branch, and verify the remote commit hash.
