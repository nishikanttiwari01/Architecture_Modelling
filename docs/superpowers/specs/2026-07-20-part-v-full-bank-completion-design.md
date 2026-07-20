# Part V Full-Bank Completion Design

## Objective

Complete the governed redesign and substantive writing of Chapters 31 to 56 of *Architecture Modelling: A Practical Beginner's Handbook*. The finished Part V must describe a credible full-service bank through mutually consistent business, application, information, integration, technology, security, control, operational and transformation viewpoints.

This programme stops at Chapter 56. Chapters 57 to 63 remain outside scope.

## Governing constraints

- The repository is the source of truth.
- Preserve the Chapter 31 to 56 titles and purposes in `BOOK_PLAN.md` unless the author explicitly approves a structural change.
- Do not mark a chapter or diagram `Approved`.
- Do not move any chapter beyond `Under Review` during this programme.
- Do not generate diagram source until its specification has been approved by the author.
- Use British English and the terminology in `GLOSSARY.md`.
- Use primary, official sources for unstable or normative claims and record them according to `SOURCE_POLICY.md`.
- Label fictional Horizon Bank structures and choices as author models.
- Do not equate a BIAN Service Domain with one application, deployable service, microservice, team or database.
- Use stable identifiers and explicit, typed relationships. Do not use prose ranges, abbreviated identifiers or uncontrolled names.

## Architecture of the work

The work uses four governed layers:

1. **Foundation:** controlled vocabularies, catalogues, relationship rules, validation and the master coverage matrix.
2. **Domain content:** Chapters 37 to 48, covering customer, product, transaction and control domains.
3. **Cross-cutting content:** Chapters 49 to 56, covering mapping, software boundaries, integration, operations, modernisation, governance, audit and scenarios.
4. **Integration and review:** Chapters 31 to 36 are reconciled with the completed foundation and later chapters, followed by full-book Part V consistency and source review.

The foundation is a hard dependency. Domain prose must not invent elements that are absent from, or intentionally pending in, the governed catalogues.

## Full-bank foundation

### Business architecture catalogues

The foundation will contain validated catalogues for:

- banking business domains and subdomains;
- business lines and customer segments;
- products at family, product and variant levels;
- value streams;
- Level 1 and Level 2 processes, with selected Level 3 processes for scenarios;
- capabilities at stable hierarchical levels;
- organisations, roles, owners and operating responsibilities;
- legal entities and organisational, jurisdiction and segment scope.

The catalogue must cover retail banking, business and corporate banking, payments, cards, merchant acquiring, trade finance, wealth and investments, securities and custody, treasury and markets, finance, risk, compliance, financial crime, fraud, audit, legal, operations and enterprise shared services.

### Application and integration catalogues

The application landscape must model a credible logical estate rather than a few illustrative systems. It must cover at least these responsibility families:

- public web, mobile, branch, contact-centre, relationship-manager and partner channels;
- identity, consent, customer access and entitlement management;
- customer relationship management, sales, product catalogue and pricing;
- party master, customer information, onboarding, KYC, screening and customer servicing;
- current accounts, savings, term deposits, interest, fees, statements and correspondence;
- consumer, mortgage, SME and corporate lending;
- collateral, limits, exposure, collections and recovery;
- payment initiation, orchestration, routing, clearing, settlement, investigations and liquidity;
- card issuing, authorisation, processing, fraud, disputes and merchant acquiring;
- corporate cash management and trade finance;
- portfolio, investment, securities, custody, corporate actions and asset servicing;
- treasury, trading, funding, liquidity, asset and liability management and capital;
- subledger, general ledger, reconciliation, tax, regulatory and management reporting;
- enterprise risk, compliance, anti-money laundering, sanctions, fraud, audit and legal casework;
- document, content, workflow, business rules, notification and case-management platforms;
- integration, API management, event streaming, messaging, managed file transfer and batch scheduling;
- operational data, analytical data, regulatory data, metadata, data quality and lineage platforms;
- security, observability, service management, configuration, secrets and resilience services.

Each logical application record must state a stable ID, name, definition, owner, business responsibilities, product or domain relationships, architecture state, record status, scope, data authority where applicable, interfaces, deployment or resilience classification, and gap. Vendor products and unsupported quantitative estate claims are excluded unless sourced and explicitly required.

The interface catalogue will distinguish synchronous APIs, commands, events, messages, files, batch, workflow hand-offs and external-network exchanges. The external-network catalogue will cover relevant payment, card, market, identity, screening and regulatory connectivity at a logical level without fabricating providers or memberships.

### Information, accounting, control and operations catalogues

The foundation will include:

- data domains and key information concepts;
- authoritative-data and system-of-record assignments by purpose and lifecycle stage;
- accounting events and subledger or ledger consequences;
- reconciliation points and exception ownership;
- preventive, detective and corrective controls;
- critical operations and impact-tolerance assumptions;
- technology and resilience classifications;
- BIAN mapping candidates with source, confidence and verification status;
- end-to-end scenarios;
- a master coverage matrix joining all governed dimensions.

Unknown or not-yet-governed elements must use an explicit permitted pending value and gap, never an empty implication.

## Chapter execution waves

### Wave 1: foundation and validation

Create and validate the complete catalogue baseline. This wave may use parallel research and catalogue-design agents, but a single integration owner will merge relationship-bearing records. Wave 1 is complete only when duplicate IDs, prefixes, required fields, controlled values, reference types, hierarchy, ownership, definitions and master coverage all validate.

### Wave 2: domain chapters

After Wave 1 passes, four non-overlapping chapter streams may run in parallel:

- Chapters 37 to 40: customer and party, deposits, lending, collateral and credit risk;
- Chapters 41 to 44: payments, cards, corporate banking, trade finance, wealth and custody;
- Chapters 45 to 48: treasury, finance, accounting, risk, compliance, financial crime, channels and shared services;
- Chapter 31 to 36 reconciliation preparation: identify catalogue-backed corrections without overwriting domain work.

Each domain chapter must explain the business purpose first, then operating model, capabilities and processes, applications, information, interfaces, accounting, controls, resilience, BIAN mapping, current-to-target considerations, common mistakes and a worked traceability example. Each chapter must remain readable independently.

### Wave 3: cross-cutting chapters

After domain chapters reach a consistent baseline:

- Chapters 49 and 50 define BIAN mapping and application, software-service and team boundaries;
- Chapters 51 and 52 define integration, deployment, security, resilience, observability and operations;
- Chapters 53 and 54 define modernisation, migration, governance, ownership and repository practice;
- Chapters 55 and 56 define quality gates, coverage audit, integrated scenarios and practitioner reference.

These pairs may run in parallel where their files and research areas do not overlap. Chapter 56 is the final integration consumer and starts after the scenario and coverage baselines are stable.

### Wave 4: integration and review

Reconcile Chapters 31 to 36 with the full catalogue and later chapters. Then run technical, beginner, terminology, consistency and source reviews across all Chapters 31 to 56. Update `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, research notes and registers only when their governance conditions are met.

## Parallel-agent boundaries

Agents receive exclusive file ownership for each task. Chapter agents may edit only their assigned chapter files and dedicated research notes. They must propose catalogue changes in a hand-off report rather than editing shared catalogues during parallel drafting.

The integration owner exclusively edits shared Horizon Bank catalogues, the coverage matrix, controlled vocabularies, validation scripts, `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, source registers and diagram registers. This prevents lost updates and conflicting identifiers.

Every implementation task receives two reviews:

1. specification compliance, checking the assigned scope and catalogue traceability;
2. quality review, checking accuracy, beginner readability, consistency, sources and unintended edits.

Open review findings return to the same implementer before the task is accepted.

## Research and source strategy

Research is routed by claim type:

- BIAN definitions and mappings: official BIAN material for the governed version;
- UML, BPMN, DMN and ArchiMate terms: official standards bodies or official documentation;
- prudential, accounting, payments, operational resilience and financial-crime claims: relevant primary international or official authorities;
- Horizon Bank organisation, application choices and target-state recommendations: clearly labelled author models.

Research agents produce one source note per meaningful source, record access date and version, and avoid copying standards prose or diagrams. No source may be cited from a search-results page when the original is available.

## Chapter quality contract

Every completed chapter must:

- fulfil its stated purpose and reader outcomes;
- define acronyms on first use;
- explain simply before introducing formal language;
- separate fact, interpretation and recommendation;
- answer the standard modelling questions from `AGENTS.md` where applicable;
- use exact governed IDs and names;
- include explicit application, data, integration, accounting, control and operational relationships when relevant;
- include comparison, common mistakes, practical exercise, review checklist and references;
- document intentionally deferred diagrams or source gaps;
- avoid em dashes, vague claims, marketing language and fabricated precision.

Chapter status may advance only when `WORKFLOW.md` requirements are demonstrably met and never beyond `Under Review` in this programme.

## Validation and completion criteria

The programme is complete when:

- all governed foundation catalogues form a coherent validated baseline;
- the logical application catalogue credibly covers every major full-service-bank responsibility family listed above;
- Chapters 31 to 56 contain substantive, catalogue-backed content consistent with their approved purposes;
- the master coverage matrix contains explicit coverage or a governed gap for every required dimension;
- all new and existing catalogue-validator tests pass;
- all required repository checks pass;
- local links, terminology and diagram registers are valid;
- no unapproved diagram source has been generated;
- source and consistency reviews contain no unresolved blocking findings;
- remaining risks and author decisions are explicitly recorded.

Completion does not mean author approval or publication readiness. Those remain author-controlled decisions.

## Out of scope

- Chapters 57 to 63;
- publication approval;
- unapproved diagram source or exports;
- vendor selection or procurement recommendations;
- fabricated system counts, transaction volumes, recovery objectives or regulatory applicability;
- a one-to-one BIAN-to-application, BIAN-to-service or BIAN-to-team decomposition.
