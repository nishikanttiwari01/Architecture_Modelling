# Master Instruction for Codex: Redesign Part V as a Complete Full-Service Bank Architecture Case Study

## Purpose of this instruction

This document is the authoritative execution brief for redesigning the entire section:

```text
manuscript/part-05-bian-case-study/
```

in the repository:

```text
https://github.com/nishikanttiwari01/Architecture_Modelling
```

Target branch at the time this instruction was prepared:

```text
codex/remaining-manuscript
```

The redesign must not be treated as a minor editing pass. It is a controlled re-architecture of Part V so that it fulfils the promise already made by the book plan: a practical, complete business-and-technology implementation for a fictional full-service bank, using BIAN as a banking reference architecture without reducing banking architecture to a list of Service Domains or a microservices exercise.

The author’s goal is clear:

> A reader who completes Part V should understand how a full-service bank works, how its business capabilities and end-to-end processes connect, which application families support the work, which data is authoritative, how accounting and settlement happen, how controls are embedded, how systems integrate, how the technology operates, and how BIAN can be applied responsibly across that complete picture.

This goal takes precedence over the current chapter structure. Existing chapter numbers, titles and content are inputs, not constraints. Preserve useful material, but rethink the structure wherever needed.

---

# 1. Role and standard of work

Act simultaneously as:

- a principal enterprise architect;
- a banking business architect;
- a banking application and integration architect;
- a banking information and data architect;
- a technology, security and resilience architect;
- a senior banking operations and transformation consultant;
- a BIAN practitioner who understands the difference between a reference model and a local implementation;
- an experienced technical author who can teach a complex subject to aspiring architects without making it simplistic or generic.

Assume the work will be reviewed by experienced practitioners from retail banking, corporate banking, payments, lending, cards, treasury, finance, risk, data, security and operations.

Do not write like a general-purpose content generator. Do not produce broad claims followed by shallow lists. Every major concept must be connected to a real banking responsibility, process, application, information object, control or operational concern.

The standard is not “technically plausible”. The standard is:

- internally coherent;
- comprehensive at enterprise level;
- detailed enough at domain level to teach real banking architecture;
- traceable across business, application, data and technology viewpoints;
- honest about jurisdictional variation and uncertainty;
- grounded in current primary sources;
- consistent with repository conventions;
- useful to a working enterprise architect.

---

# 2. Non-negotiable outcome

Part V must become a navigable model of a full-service bank.

It must begin with the whole bank, then progressively drill down.

The reader must first see:

1. how a bank creates value and earns money;
2. its customer segments, products, business lines, legal entities and support functions;
3. its enterprise value streams, capabilities and process families;
4. its complete application and integration landscape;
5. its information and data domains, systems of record and major data flows;
6. its technology, security, resilience and operating architecture.

Only after this enterprise baseline is established should the manuscript move into domain-level detail.

Each major domain must then be explained from the same connected perspectives:

```text
business purpose
→ products and customer outcomes
→ organisation and roles
→ value streams
→ capabilities
→ end-to-end processes and decisions
→ candidate BIAN reference responsibilities
→ applications and ownership
→ information and systems of record
→ APIs, events, batch, files and external networks
→ accounting and financial effects
→ risks, controls and evidence
→ non-functional and operational requirements
→ current-state problems, target state and migration
```

The final chapters must show how to convert this model into governed application boundaries, semantic interfaces, events, deployment, modernisation, architecture governance and measurable transformation.

A reader should not finish Part V with only an understanding of BIAN terminology. The reader should be able to explain how a bank works.

---

# 3. Diagnosis of the current section

Before changing the manuscript, verify this diagnosis against the repository.

The current Part V contains Chapters 31 to 56. Chapters 31 to 35 contain substantial explanatory prose, while many later chapters are still planned or skeletal. The opening chapters correctly explain several important distinctions, especially that:

- a BIAN Service Domain is not automatically a microservice;
- a Business Scenario is not automatically the bank’s mandatory process;
- the Business Object Model is not a physical enterprise schema;
- a Service Operation is not automatically an endpoint or event;
- one application may support multiple BIAN responsibilities;
- one BIAN responsibility may be realised by multiple applications.

Keep these principles. State them clearly once, encode them in the mapping method, and enforce them throughout the case study.

Do not let them dominate every chapter.

The current section has four structural weaknesses that must be corrected.

## 3.1 It teaches modelling cautions more than it models a bank

The manuscript repeatedly explains what BIAN is not, but gives insufficient space to:

- how deposits operate;
- how loan origination differs from loan servicing;
- how collateral, limits and exposure interact;
- how payment initiation, clearing, settlement and posting differ;
- how cards are authorised, cleared, settled and billed;
- how statements and customer communications are generated;
- how general ledger, subledgers and reconciliation work;
- how treasury, liquidity and asset-liability management work;
- how trade finance, wealth and custody work;
- how controls, finance and operations span all domains.

The revised section must reverse that balance.

## 3.2 The enterprise baseline is selective rather than complete

The existing Horizon Bank application and capability catalogues are too small for a full-service bank. They are suitable for a limited onboarding example, not for the complete case study promised by the book.

Expand the controlled catalogues before repeatedly using names in chapters.

## 3.3 Scenarios are isolated instead of forming domain architecture

The current scenario plan covers a few useful journeys, such as onboarding, account opening, cross-border payment, consumer lending, card fraud and corporate cash management. Those scenarios are valuable, but they do not substitute for domain coverage.

A scenario shows one thread. A domain chapter must explain the complete lifecycle, capabilities, processes, applications, data, accounting, controls and operating characteristics surrounding that thread.

## 3.4 Business, application, data and technology coverage is not yet balanced

Part V must not become an application catalogue with BIAN labels. It must also not become a business capability map with technology added at the end.

The business, application, information/data, integration, security, technology, operations and transformation perspectives must be designed together and kept traceable.

---

# 4. Repository rules that remain mandatory

Before editing anything, read the repository in the order required by `AGENTS.md`.

At minimum read:

1. `BOOK_PLAN.md`
2. `STATUS.md`
3. `WORKFLOW.md`
4. `STYLE_GUIDE.md`
5. `SOURCE_POLICY.md`
6. `DECISIONS.md`
7. `GLOSSARY.md`
8. all current Part V chapters
9. the preceding and following chapter where relevant
10. all Horizon Bank example files
11. `DIAGRAM_REGISTER.md`
12. relevant source notes and review records
13. relevant scripts and templates

Follow the repository’s current rules unless this instruction explicitly changes the Part V structure.

Mandatory writing and governance rules include:

- use British English;
- do not use em dashes;
- define acronyms at first use in every standalone chapter;
- explain simply first, then introduce formal terminology, then demonstrate it;
- use controlled terminology from `GLOSSARY.md`;
- use primary sources for standards and current claims;
- record source versions and access dates;
- do not copy copyrighted standards diagrams or substantial source text;
- create original diagrams;
- never mark a chapter or diagram `Approved`;
- do not use destructive Git commands;
- do not push, merge or release unless explicitly instructed;
- use focused commits;
- update `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, `BOOK_PLAN.md`, cross-references and registers when the structure changes.

For this redesign, change Chapters 31 to 35 from `Ready for Author Approval` to `Revision Required` before substantive editing. Any newly restructured or rewritten chapters must remain `Drafting`, `Diagramming`, `Under Review` or `Revision Required` until the complete Part V coverage audit has passed and the author has reviewed the result.

---

# 5. Research policy

## 5.1 Use current primary sources

Do not rely on memory for:

- BIAN version-sensitive names or definitions;
- regulatory or accounting standards;
- payment messaging;
- card security standards;
- operational resilience guidance;
- current architecture framework versions;
- API or event guidance presented as normative;
- jurisdiction-specific obligations.

Use the original publisher whenever possible.

## 5.2 Minimum authoritative source set

The research baseline must include, as relevant:

### Banking reference architecture

- BIAN Service Landscape 14.0 and official 14.0 release notes
  `https://bian.org/deliverables/service-landscape/`
- BIAN Portal and official 14.0 repository views
  `https://bian.org/bian-portal/`
- BIAN Semantic API Practitioner Guide, current registered version
- BIAN metamodel, information architecture, Business Object Model and Business Scenario material
- BIAN Service Domain, Behaviour Qualifier and Service Operation pages used in mappings

### Prudential, risk data and operational resilience

- Basel Committee consolidated Basel Framework
  `https://www.bis.org/basel_framework/`
- Basel III overview and applicable official publications
  `https://www.bis.org/bcbs/basel3.htm`
- BCBS 239, Principles for effective risk data aggregation and risk reporting
  `https://www.bis.org/publ/bcbs239.pdf`
- Principles for operational resilience
  `https://www.bis.org/bcbs/publ/d516.pdf`
- Sound management of operational risk
- current official principles for third-party risk where used

### Financial crime and customer due diligence

- FATF Recommendations
  `https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html`
- FATF risk-based approach for the banking sector
  `https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Risk-based-approach-banking-sector.html`
- other FATF official guidance only where relevant to a specific domain
- jurisdiction-specific rules only if clearly labelled as examples

### Payments and cards

- ISO 20022 official standard and message catalogue
  `https://www.iso20022.org/iso-20022`
- SWIFT official CBPR+ and messaging guidance, where cross-border payments are described
- PCI Security Standards Council, current PCI DSS material
  `https://www.pcisecuritystandards.org/standards/pci-dss/`
- EMVCo official material for chip, tokenisation or 3-D Secure where needed
- payment scheme rules only when public, necessary and properly attributed
- do not reproduce proprietary scheme rulebooks

### Accounting and impairment

- IFRS Foundation, IFRS 9 material and official supporting resources where the case study uses an IFRS baseline
  `https://www.ifrs.org/issued-standards/list-of-standards/`
- clearly state that accounting treatment varies by applicable reporting framework and jurisdiction
- do not present simplified journal entries as legal or accounting advice

### Security, continuity and architecture notation

- NIST Cybersecurity Framework 2.0
  `https://www.nist.gov/cyberframework`
- ISO 22301 overview where business continuity principles are discussed
- official OMG sources for UML, BPMN and DMN
- The Open Group official sources for ArchiMate and TOGAF concepts
- official C4 documentation
- official vendor-neutral sources for OpenAPI, AsyncAPI, CloudEvents or OAuth only where those standards are used

### Securities, markets and infrastructure

Use official sources as relevant, for example:

- CPMI-IOSCO Principles for Financial Market Infrastructures;
- official market infrastructure documentation;
- ISO 20022 securities messages;
- central securities depository or exchange documentation used only as examples;
- regulatory sources for market, liquidity and capital concepts.

## 5.3 Source note requirements

Create one source note per meaningful source using the repository template. Record:

- source title;
- issuing organisation;
- version or release;
- publication date;
- access date;
- URL;
- why it is authoritative;
- exact claims it supports;
- limitations;
- whether it is normative, explanatory or illustrative;
- affected chapters, figures and catalogue entries.

Do not cite a search-results page when the original document exists.

## 5.4 Research discipline for BIAN mappings

Do not invent, approximate or modernise BIAN Service Domain names.

For every BIAN object used, record:

- BIAN release, normally 14.0 for this manuscript;
- exact official name;
- object type;
- Business Area and Business Domain where applicable;
- official source location;
- relevant responsibility;
- why it is a candidate for the local element;
- local scope and exclusions;
- mapping confidence;
- reviewer;
- status: `Candidate`, `Verified`, `Accepted`, `Rejected`, `Partial` or `Transitional`;
- date verified.

A name match is not sufficient evidence.

Where BIAN 14.0 renamed, removed or changed a Service Domain, do not silently use an older name. Record the change when it materially affects the teaching.

---

# 6. Horizon Bank case-study baseline

Create a stable fictional bank baseline before rewriting domain chapters.

Horizon Bank is a fictional, internationally active full-service banking group used only for teaching. It must be realistic enough to connect the architecture views, but it must not imply one country’s law is universal.

## 6.1 Suggested business profile

Document and control the following assumptions:

- group holding company with regulated banking and selected non-bank legal entities;
- retail, small and medium-sized enterprise, commercial, corporate and private-banking customer segments;
- domestic and cross-border operations;
- multi-currency products;
- branch, contact-centre, automated teller machine, web, mobile, relationship-manager and partner channels;
- current and savings accounts;
- term and fixed deposits;
- consumer loans;
- mortgages;
- small-business and corporate lending;
- revolving facilities and overdrafts;
- cards and merchant acquiring;
- domestic and cross-border payments;
- cash management;
- trade finance;
- wealth management;
- securities and custody;
- treasury, markets, liquidity and funding;
- financial crime, fraud, risk, finance and regulatory functions;
- a mixed legacy and modern technology estate;
- a target direction that uses modular services, governed APIs, events and data products where justified, without assuming that every legacy core must be immediately replaced.

Label the bank’s countries, currencies, legal entities and reporting regimes as teaching assumptions. Avoid unnecessary invented detail that later creates contradictions.

## 6.2 Business model and economics

Part V must explain, in beginner-friendly but accurate terms:

- a bank’s balance sheet;
- assets, liabilities and equity;
- deposits as liabilities of the bank;
- loans and many securities positions as assets;
- interest income and interest expense;
- net interest margin;
- fee and commission income;
- trading and investment income where relevant;
- operating expense;
- credit loss provisions and write-offs;
- capital and liquidity constraints;
- off-balance-sheet commitments and contingent liabilities;
- the difference between product balance, accounting balance, available balance and ledger balance where relevant;
- why reconciliation and settlement are essential;
- how product events become accounting entries;
- why profitability, liquidity, capital, risk and customer outcomes can pull in different directions.

Use illustrative numbers only. Clearly mark simplified examples.

## 6.3 Current-state architecture assumption

Use a credible mixed estate:

- a mature core banking platform supporting deposits and selected posting;
- separate loan, mortgage, card, payment, trade finance, treasury and wealth platforms;
- regional or product-specific duplication;
- channel-specific point-to-point interfaces;
- batch and end-of-day dependencies;
- enterprise service bus and managed file transfer;
- newer application programming interface gateway and event platform;
- operational data stores and enterprise data warehouse;
- increasing use of cloud services where permitted;
- manual operations and spreadsheets in exception-heavy processes;
- inconsistent customer and product identifiers;
- multiple copies of data;
- reconciliation breaks;
- technical debt and vendor concentration;
- strong availability demands around critical services.

This allows the section to teach current state, target state and transition rather than pretending the bank is greenfield.

## 6.4 Target-state architecture direction

The target direction may include:

- clearer business and application responsibility boundaries;
- governed domain ownership;
- reduced point-to-point integration;
- canonical or semantically governed exchanges where useful;
- versioned APIs and events;
- event-driven processing where it fits the consistency and control requirements;
- retained batch where operationally appropriate;
- authoritative data ownership and data lineage;
- modularisation of selected legacy capabilities;
- stronger observability and resilience;
- automated control evidence;
- consistent identity and access controls;
- measurable decommissioning and simplification.

Do not prescribe microservices, cloud or event-driven architecture everywhere. Each target choice must be justified by business change rate, consistency needs, latency, volume, operational criticality, data authority, team boundaries, vendor constraints and migration risk.

---

# 7. Required redesign of Part V

The current sequence should be replaced by a structure that moves from enterprise understanding, through domain architectures, to implementation and transformation.

Keep the total chapter range at 31 to 56 unless the author explicitly approves a different count. Update file names, links, navigation, `BOOK_PLAN.md`, `STATUS.md`, cross-references and build inputs together.

The following structure is the preferred baseline. Small refinements are allowed only when they improve coherence without reducing coverage.

## Chapter 31. BIAN Essentials and the Case-Study Method

### Purpose

Introduce only the BIAN concepts required to navigate the remainder of Part V, then explain how they will be combined with business, application, data and technology models.

### Must cover

- why BIAN exists;
- Service Landscape;
- Business Areas and Business Domains;
- Service Domains;
- Business Scenarios;
- Service Operations;
- Behaviour Qualifiers where relevant;
- Business Object Model and Control Record Model at an appropriate introductory level;
- semantic APIs and events;
- BIAN 14.0 version discipline;
- what BIAN does and does not prescribe;
- the many-to-many mapping principle;
- the relationship to ArchiMate, BPMN, C4, UML, DMN and data modelling;
- how the Horizon Bank case study will use BIAN;
- the evidence and status model for mappings.

### Editing direction

Retain the strongest material from current Chapters 31 and 32, but remove repetition. The warning that a Service Domain is not automatically a microservice should appear prominently once, then be enforced through the mapping register and examples.

### Required figure

A Part V navigation and traceability figure:

```text
banking outcome
→ value stream
→ capability
→ process
→ BIAN candidate responsibility
→ application responsibility
→ information
→ interface
→ deployment and operation
```

Use qualified relationship labels, never `equals`.

---

## Chapter 32. How a Full-Service Bank Works

### Purpose

Give the reader the commercial and operational foundation required to understand all later architecture.

### Must cover

- bank purpose and stakeholder groups;
- retail, SME, commercial, corporate, private-banking and institutional segments;
- product families and customer needs;
- business lines and legal entities;
- channels and distribution;
- front office, middle office, back office and control functions;
- revenue and cost drivers;
- balance-sheet structure;
- interest and fee mechanics;
- capital, liquidity and risk at a conceptual level;
- accounting flow from business event to subledger and general ledger;
- business-day processing, value date, booking date and settlement date;
- customer lifecycle;
- product lifecycle;
- transaction lifecycle;
- case and exception lifecycle;
- three lines model and independent assurance;
- group versus country responsibilities;
- shared-service and outsourcing models;
- critical operations and third-party dependencies.

### Required figures

- full-service bank business model;
- business lines and enterprise functions;
- simplified bank balance sheet and income model;
- front-to-back operating model;
- legal-entity and group operating relationship;
- lifecycle map connecting customer, product, transaction, accounting and reporting.

### Teaching requirement

A reader with software experience but limited banking knowledge should finish this chapter understanding why banking systems are separated into product processors, channels, customer platforms, risk systems, finance systems, integration platforms and data platforms.

---

## Chapter 33. Enterprise Business Architecture of Horizon Bank

### Purpose

Establish the complete business architecture baseline.

### Must cover

- stakeholder outcomes;
- value-stream portfolio;
- full capability map;
- process architecture from Level 0 to Level 2, with selected Level 3 examples;
- business lines, departments and roles;
- governance and decision rights;
- product and service catalogue;
- operating-model variations by segment, geography and legal entity;
- capability ownership, process ownership, product ownership, data ownership and control ownership;
- maturity and pain-point heat maps;
- relationship between capability, process, organisation and BIAN;
- enterprise controls and measures.

### Required deliverables

- complete Level 1 capability map;
- governed Level 2 capability catalogue;
- Level 0 and Level 1 process landscape;
- value-stream portfolio;
- organisation and role view;
- capability-to-process matrix;
- capability heat map with explicit scoring;
- business architecture glossary and controlled identifiers.

### Coverage rule

The enterprise maps may use landscape pages or two-page spreads. Do not avoid a complete overview merely because detail cannot fit on one portrait page. The overview establishes coverage. Separate drill-down views establish readability.

---

## Chapter 34. Full Bank Application and Integration Landscape

### Purpose

Present the complete enterprise application landscape, then explain how the reader should navigate domain views.

### Structural inspiration

Use the application landscape supplied by the author only as inspiration for the idea of layered coverage:

- channels and user experience;
- digital and customer functions;
- workflow and integration;
- core and product-processing systems;
- external parties and networks;
- enterprise data;
- security as a cross-cutting concern.

Do not copy proprietary acronyms, names, colouring or layout.

### Required application layers

1. **Channels and experience**
2. **Customer engagement and journey orchestration**
3. **Customer, party, product and agreement platforms**
4. **Product-processing and transaction systems**
5. **Risk, compliance and control systems**
6. **Finance and enterprise support**
7. **Integration and external connectivity**
8. **Data, analytics, reporting and artificial intelligence**
9. **Technology platforms and operations**
10. **Security and identity**
11. **External ecosystems and market infrastructures**

### Must explain

- application responsibility versus business capability;
- system of engagement, orchestration, record, processing, insight and control;
- enterprise platforms versus domain systems;
- current, target and transitional applications;
- regional and legal-entity variants;
- buy, build, software-as-a-service and external-service distinctions;
- technology obsolescence, duplication and strategic fit;
- application criticality;
- service ownership and support;
- integration styles;
- external network dependencies;
- application-to-capability and application-to-data relationships;
- application rationalisation principles.

### Required figures

- complete layered application landscape;
- current-state application context;
- target-state application context;
- application-to-capability heat map;
- application integration overview;
- external ecosystem map;
- strategic application disposition view using controlled criteria.

---

## Chapter 35. Enterprise Information and Data Architecture

### Purpose

Establish the bank-wide data model, data authority and data movement before detailed domain discussions.

### Must cover

- conceptual, logical and physical data models;
- data domains;
- business terms;
- master, reference, transactional, event, analytical and document data;
- systems of record and authoritative-source decisions;
- golden record versus source record;
- identifiers and cross-reference management;
- legal entity, customer, account, contract and transaction identifiers;
- data ownership and stewardship;
- metadata and lineage;
- quality dimensions and controls;
- reconciliations;
- privacy, confidentiality and data classification;
- retention and legal hold;
- data residency;
- data sharing and purpose limitation;
- operational stores, lakehouse, data warehouse and data marts;
- data products where justified;
- reporting and analytics;
- risk data aggregation and BCBS 239 principles;
- model and artificial-intelligence data considerations;
- BIAN information concepts as semantic references, not mandatory physical schemas.

### Required figures and matrices

- enterprise data-domain map;
- system-of-record matrix;
- conceptual relationship model;
- operational-to-analytical data-flow view;
- lineage from business transaction to management, risk and regulatory reporting;
- data ownership model;
- critical data-element example;
- reconciliation and data-quality control loop.

---

## Chapter 36. Technology, Security, Resilience and Operating Architecture

### Purpose

Explain how the application and data estate runs securely and reliably.

### Must cover

- on-premises, mainframe, private cloud, public cloud and software-as-a-service placement;
- network zones and trust boundaries;
- identity, authentication, authorisation and privileged access;
- customer identity versus workforce identity;
- machine identity;
- secrets, certificates and key management;
- encryption and tokenisation;
- cardholder-data segmentation;
- application, API, event and data security;
- fraud and cyber-security interaction;
- secure software delivery;
- vulnerability and patch management;
- observability, logs, metrics, traces and business telemetry;
- operations, incident, problem, change and service management;
- batch operations and business-day controls;
- high availability;
- disaster recovery;
- backup and restoration;
- cyber recovery;
- operational resilience;
- critical operations, impact tolerance and scenario testing;
- capacity, performance and scaling;
- vendor and third-party dependencies;
- cloud concentration and exit planning;
- production support ownership;
- service level objectives and error budgets where appropriate;
- release, rollback and feature-control patterns;
- records and evidence needed for assurance.

### Required figures

- hybrid deployment reference architecture;
- security trust-zone view;
- identity and access flow;
- observability and operational-control view;
- critical-service dependency map;
- high-availability and disaster-recovery view;
- third-party dependency and exit view.

---

## Chapter 37. Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing

### Scope

Cover the complete relationship lifecycle, not only initial onboarding.

### Must cover

- prospect, party, customer and counterparty distinctions;
- natural person, organisation and related-party structures;
- household and corporate-group relationships;
- lead, opportunity and relationship management;
- suitability and eligibility at a conceptual level;
- customer due diligence;
- know your customer;
- beneficial ownership;
- tax and regulatory classifications;
- identity verification;
- sanctions, politically exposed person and adverse-media screening;
- risk rating;
- onboarding;
- periodic and event-driven review;
- customer data maintenance;
- consent and preferences;
- mandates, powers and authorised signatories;
- complaints, enquiries and service requests;
- dormancy, restrictions, exit and offboarding;
- privacy and record retention;
- omnichannel servicing;
- relationship profitability and service segmentation.

### Applications

Include at least:

- customer relationship management;
- onboarding and journey orchestration;
- party and customer master;
- identity verification;
- document capture and management;
- financial crime screening;
- case management;
- consent and preference;
- product catalogue;
- digital and assisted channels;
- notification and correspondence.

### Key data

Party, customer, organisation, relationship, beneficial owner, identity, address, contact, classification, consent, preference, tax status, screening result, risk rating, document, mandate, complaint and case.

### Worked scenario

A corporate customer onboarding with beneficial owners, multiple authorised signatories, screening referrals and product fulfilment. Include happy path, referral, rejection, duplicate-party resolution and post-onboarding review obligations.

---

## Chapter 38. Deposits, Accounts, Term Deposits, Interest, Fees, Statements and Correspondence

### Scope

Cover deposit product manufacture, sales, fulfilment and servicing.

### Must cover

- current and transaction accounts;
- savings accounts;
- term or fixed deposits;
- notice deposits where used;
- overdraft linkage;
- product definition and pricing;
- eligibility;
- account opening and agreement establishment;
- account and balance models;
- ledger, available, cleared and projected balance;
- debit and credit posting;
- holds, blocks and reservations;
- interest calculation, accrual, capitalisation and payment;
- fees, waivers and charges;
- maturity and rollover;
- early withdrawal;
- dormancy;
- account restrictions;
- account closure;
- tax withholding as a jurisdiction-specific concern;
- statements, advices and confirmations;
- correspondence generation, delivery, preference and evidence;
- product accounting and reconciliation;
- deposit insurance as a jurisdiction-specific concept;
- end-of-day and business-day processing.

### Applications

- deposit product catalogue;
- core deposit or core banking system;
- term-deposit engine;
- interest and fee engine;
- account servicing;
- statement generation;
- correspondence and notification;
- general ledger interface;
- reconciliation;
- channels and workflow.

### Worked scenario

Open and fund a fixed deposit, accrue interest, issue advice and statement, handle early break, calculate penalty, settle proceeds and post accounting entries.

---

## Chapter 39. Lending and Credit: Consumer, Mortgage, SME and Corporate

### Scope

Cover credit products from proposition through repayment and closure.

### Must cover

- unsecured consumer credit;
- mortgages;
- vehicle or asset finance at a conceptual level;
- overdrafts and revolving credit;
- SME and corporate term loans;
- working-capital and revolving facilities;
- bilateral versus syndicated lending at an introductory level;
- product configuration and pricing;
- application capture;
- bureau and internal data;
- affordability and serviceability;
- credit scoring and rating;
- underwriting;
- approval authorities;
- offer and documentation;
- conditions precedent;
- booking and disbursement;
- repayment schedules;
- principal, interest, fees and penalties;
- floating and fixed rates;
- rate reset;
- drawdown;
- servicing;
- payment allocation;
- restructuring;
- settlement and closure;
- delinquency hand-off;
- accounting and impairment integration.

### Distinguish clearly

- loan origination;
- credit assessment;
- credit approval;
- facility management;
- loan contract;
- drawdown;
- loan account servicing;
- collateral;
- limits;
- exposure;
- collections;
- impairment.

### Worked scenario

A small-business revolving facility with approval conditions, collateral dependency, partial drawdown, interest accrual, covenant monitoring and later limit review.

---

## Chapter 40. Collateral, Limits, Exposure, Collections, Recovery and Credit Risk Lifecycle

### Scope

Explain the responsibilities that surround and continue beyond loan origination.

### Must cover

- collateral type and eligibility;
- valuation;
- haircut;
- lien, charge, pledge or mortgage as jurisdiction-dependent legal mechanisms;
- perfection and documentation;
- collateral allocation to facilities;
- shared and cross-collateral;
- collateral substitution and release;
- insurance and covenant monitoring;
- limit hierarchy;
- customer, group, product, country and settlement limits;
- utilisation and available headroom;
- exposure aggregation;
- connected counterparties;
- early-warning indicators;
- arrears and delinquency;
- collections strategy;
- promise to pay;
- forbearance and restructuring;
- recovery;
- repossession or enforcement at a conceptual level;
- write-off;
- impairment and expected credit loss integration;
- non-performing exposure treatment as a jurisdiction-specific concern;
- audit evidence and segregation of duties.

### Worked scenario

A secured corporate facility experiences a covenant breach and missed payment. Show exposure aggregation, collateral revaluation, collections, restructuring decision, impairment update and controlled release or enforcement options.

---

## Chapter 41. Payments, Clearing, Settlement, Correspondent Banking and Foreign Exchange

### Scope

Explain the full payment lifecycle across domestic and cross-border rails.

### Must cover

- payer, payee, debtor, creditor and account roles;
- payment initiation;
- consent and authentication;
- validation;
- balance and limit checks;
- reservation;
- duplicate detection;
- screening;
- fraud assessment;
- routing;
- fee and foreign-exchange calculation;
- messaging;
- clearing;
- settlement;
- posting;
- notification;
- reconciliation;
- rejects, returns, recalls, cancellations and investigations;
- instant, real-time gross settlement, automated clearing house, wire, internal book transfer and batch payments;
- direct debits;
- standing orders;
- bulk and payroll payments;
- request-to-pay where appropriate;
- correspondent banking and nostro/vostro concepts;
- cover and serial payments at an appropriate level;
- cut-off, value date and holiday calendars;
- ISO 20022;
- SWIFT CBPR+ where relevant;
- liquidity and intraday positions;
- operational resilience of payment services.

### Distinguish clearly

- customer payment instruction;
- payment order;
- payment message;
- clearing obligation;
- settlement movement;
- account posting;
- general-ledger effect;
- customer notification.

### Worked scenario

A cross-border corporate payment with foreign exchange, sanctions screening, correspondent routing, reject and repair path, settlement, nostro reconciliation and customer status updates.

---

## Chapter 42. Cards and Merchant Acquiring

### Scope

Cover issuing and acquiring as separate but connected businesses.

### Must cover

- card product and account;
- physical and virtual cards;
- tokenisation;
- personal identification number and credential management;
- authorisation;
- stand-in processing;
- holds and reversals;
- clearing;
- settlement;
- billing and statement;
- minimum payment and revolving balance;
- interest and fees;
- rewards;
- merchant, terminal and acquirer;
- merchant onboarding;
- transaction routing;
- interchange and scheme fees at a conceptual level;
- dispute;
- chargeback;
- fraud detection and investigation;
- card replacement, block and closure;
- PCI DSS scope;
- strong customer authentication and 3-D Secure as jurisdiction or scheme-dependent examples;
- reconciliation and accounting.

### Worked scenario

An e-commerce card transaction proceeds through authentication, authorisation, token use, clearing and settlement, then becomes a disputed transaction with chargeback and fraud-investigation paths.

---

## Chapter 43. Corporate Banking, Cash Management and Trade Finance

### Scope

Show how corporate products differ from retail products and how complex mandates, legal entities and operational controls shape the architecture.

### Must cover

- corporate relationship structures;
- account hierarchies;
- mandates and authorised signatories;
- entitlements and approval matrices;
- host-to-host and file channels;
- bulk payments;
- payroll;
- collections;
- receivables;
- virtual accounts;
- sweeping and pooling;
- liquidity concentration;
- cash-position reporting;
- bank account management;
- service pricing;
- implementation and client onboarding;
- service-level and cut-off management;
- letters of credit;
- guarantees;
- documentary collections;
- trade loans;
- supply-chain finance at a conceptual level;
- document examination and discrepancy;
- sanctions and goods or vessel screening where relevant;
- contingent liabilities;
- fees and commissions;
- trade-event accounting;
- integration with payments and limits.

### Worked scenario

A corporate customer uses host-to-host connectivity for bulk payments and liquidity sweeping, while separately issuing an import letter of credit that creates a contingent obligation and document workflow.

---

## Chapter 44. Wealth, Investments, Securities, Custody and Asset Servicing

### Scope

Cover advisory, execution, portfolio and post-trade servicing without turning the chapter into a capital-markets textbook.

### Must cover

- client segmentation;
- investment profile;
- objectives and risk appetite;
- suitability and appropriateness as jurisdiction-dependent concepts;
- advice and recommendation;
- model portfolios;
- discretionary and advisory services;
- order capture;
- pre-trade controls;
- execution;
- allocation;
- confirmation;
- settlement;
- custody;
- safekeeping;
- positions;
- valuations;
- fees;
- corporate actions;
- income collection;
- tax-lot or cost-basis concerns;
- performance reporting;
- statements;
- market and reference data;
- product governance;
- restricted instruments;
- surveillance and conduct controls;
- reconciliation with brokers, custodians and depositories.

### Worked scenario

A private-banking client accepts an investment recommendation, places an order, receives an allocation, settles through a custodian, receives a corporate-action entitlement and sees the result in a portfolio statement.

---

## Chapter 45. Treasury, Markets, Funding, Liquidity, ALM and Capital

### Scope

Explain the bank’s own balance-sheet and market activities.

### Must cover

- treasury dealing;
- foreign exchange;
- money market;
- fixed income and derivatives at a conceptual level;
- trade capture;
- confirmation;
- valuation;
- market data;
- limit checks;
- settlement;
- position and profit and loss;
- counterparty exposure;
- collateral or margin for treasury transactions at a conceptual level;
- funding;
- liquidity buffer;
- intraday liquidity;
- liquidity coverage and stable funding concepts;
- funds transfer pricing;
- interest-rate risk in the banking book;
- asset-liability management;
- hedging;
- capital planning;
- stress testing;
- regulatory and management reporting;
- front-office, risk, operations and finance separation;
- reconciliation.

### Worked scenario

The bank forecasts a liquidity shortfall, raises short-term funding, executes a foreign-exchange swap, updates positions and limits, settles cash flows, posts accounting and reports the effect to treasury and risk.

---

## Chapter 46. Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting

### Scope

Explain how operational events become controlled financial records and reports.

### Must cover

- chart of accounts;
- product subledger;
- accounting rules;
- journal generation;
- event-to-accounting mapping;
- debit and credit at a teaching level;
- suspense and control accounts;
- general ledger;
- legal-entity and branch books;
- multi-currency accounting;
- accruals;
- fee and interest recognition;
- impairment;
- expected credit loss where IFRS 9 is used as the case-study baseline;
- provisions and write-offs;
- intercompany;
- reconciliation;
- substantiation;
- month-end and year-end close;
- management accounting;
- profitability;
- transfer pricing;
- tax;
- statutory, prudential and regulatory reporting;
- data lineage;
- adjustments;
- maker-checker and journal approval;
- audit trail;
- financial controls.

### Required teaching aid

Include several simplified, clearly labelled accounting examples:

- customer deposit;
- loan disbursement;
- interest accrual;
- payment fee;
- card settlement;
- expected-credit-loss provision;
- write-off;
- nostro reconciliation break.

### Worked scenario

Trace one customer loan from approval and disbursement through subledger postings, interest accrual, repayment, impairment update, general-ledger aggregation, reconciliation and financial reporting.

---

## Chapter 47. Risk, Compliance, Financial Crime, Fraud, Audit and Legal

### Scope

Present enterprise control functions and embedded first-line controls.

### Must cover

- risk taxonomy;
- risk appetite;
- credit, market, liquidity, operational, model, cyber, conduct, compliance and reputational risk;
- first line, second line and independent assurance;
- control objectives, activities and evidence;
- anti-money laundering;
- counter-terrorist financing;
- proliferation-financing considerations where relevant;
- sanctions;
- customer and transaction screening;
- transaction monitoring;
- fraud prevention, detection, case management and recovery;
- regulatory change;
- compliance monitoring;
- operational-risk events;
- key risk indicators;
- issues and remediation;
- legal matters;
- records and legal hold;
- audit planning, testing and evidence;
- regulatory examinations;
- model governance;
- data and artificial-intelligence risk;
- enterprise risk aggregation and reporting.

### Worked scenario

A payment triggers both sanctions screening and fraud signals. Show first-line decisioning, second-line policy, alert handling, escalation, customer communication constraints, control evidence, reporting and model-performance feedback.

---

## Chapter 48. Channels, Communications, Documents, Workflow, Case Management and Shared Services

### Scope

Explain cross-domain services that make customer journeys and operations possible.

### Must cover

- mobile and internet banking;
- corporate portal;
- branch workstation;
- relationship-manager workbench;
- contact centre;
- automated teller machine;
- open-banking or partner APIs;
- assisted versus self-service;
- authentication and session management;
- channel entitlements;
- consistent customer context;
- journey orchestration;
- workflow;
- business process management;
- human tasks;
- work queues;
- service-level timers;
- case management;
- document capture;
- optical character recognition as an implementation option;
- document management;
- electronic signature;
- statements;
- notices;
- advices;
- templates;
- language and accessibility;
- communication preferences;
- email, short-message service, push, secure mailbox and paper;
- notification delivery and retry;
- evidence of delivery;
- enterprise search;
- shared reference data;
- scheduler, managed file transfer and enterprise integration services;
- customer analytics and next-best-action with governance;
- avoiding over-centralised “god platforms”.

### Worked scenario

A customer changes an address through mobile banking. Show authentication, validation, workflow, party-master update, downstream propagation, document evidence, risk triggers, notification and reconciliation of failed consumers.

---

## Chapter 49. BIAN Mapping Method and Full-Stack Traceability

### Purpose

Turn the enterprise and domain content into a repeatable method.

### Must cover

- local business concepts versus reference concepts;
- mapping from business outcome to capability, process and responsibility;
- candidate and verified BIAN mappings;
- mapping confidence and gaps;
- many-to-many relationships;
- scope qualifiers;
- versioning;
- current, target and transitional mappings;
- mapping to applications, data and interfaces;
- semantic mapping;
- traceability queries;
- impact analysis;
- review workflow;
- anti-patterns;
- worked examples from at least three domains.

### Required artefact

A complete coverage and traceability matrix, not merely a diagram.

---

## Chapter 50. BIAN-Aligned Application, Service and Team Boundaries

### Purpose

Explain how BIAN informs, but does not dictate, software and organisational design.

### Must cover

- application boundary;
- component boundary;
- service boundary;
- domain boundary;
- team ownership;
- modular monolith;
- microservices;
- vendor package;
- platform;
- software-as-a-service;
- adapter and anti-corruption layer;
- transaction boundary;
- consistency;
- data ownership;
- change coupling;
- latency and volume;
- availability;
- regulatory segregation;
- operational ownership;
- build versus buy;
- bounded-context comparison;
- BIAN Service Domain comparison;
- current-state and target-state mapping;
- decomposition and consolidation;
- service catalogue;
- deprecation and decommissioning.

### Worked example

Compare three valid target options for modernising deposit servicing or payments. Show why one Service Domain per microservice is not the decision rule.

---

## Chapter 51. APIs, Events, Batch, Files, Workflow and External Networks

### Purpose

Provide an integrated interaction architecture rather than separate fashionable chapters.

### Must cover

- interaction selection based on business semantics and quality attributes;
- synchronous APIs;
- asynchronous commands and events;
- request and reply messaging;
- streaming;
- batch;
- managed files;
- workflow and human tasks;
- database integration as a legacy constraint, not a preferred default;
- external networks;
- schema and contract governance;
- semantic alignment;
- identity and authorisation;
- idempotency;
- retries;
- duplicate detection;
- ordering;
- concurrency;
- timeout;
- compensation;
- reconciliation;
- dead-letter and repair handling;
- versioning and compatibility;
- observability;
- consumer-driven impact;
- data privacy;
- interface ownership;
- canonical models and their limits;
- ISO 20022 mapping where relevant;
- BIAN semantic API use and limits;
- event taxonomy;
- business event versus technical event;
- batch-control totals;
- file acknowledgements;
- operational runbooks.

### Required examples

Use at least:

- customer update API;
- payment event flow;
- overnight interest batch;
- corporate bulk-payment file;
- human approval workflow;
- SWIFT or payment-rail interaction;
- reconciliation after partial failure.

---

## Chapter 52. Deployment, Security, Resilience, Observability and Operations

### Purpose

Apply Chapter 36’s enterprise principles to deployable architecture and operations.

### Must cover

- logical versus physical deployment;
- environment topology;
- multi-region and multi-zone considerations;
- mainframe and distributed coexistence;
- container and non-container workloads;
- cloud landing zones;
- data-store selection;
- caching;
- queue and event-platform operation;
- API gateway and service mesh where justified;
- network and identity controls;
- secrets and key rotation;
- security monitoring;
- operational telemetry;
- batch monitoring;
- business transaction tracing;
- capacity;
- failover;
- recovery point and recovery time objectives;
- impact tolerance;
- backup, restoration and cyber recovery;
- active-active versus active-passive choices;
- consistency during failover;
- third-party outage;
- degraded modes;
- incident command;
- production support;
- service ownership;
- runbooks;
- resilience testing;
- chaos testing only where safe and governed;
- evidence and auditability.

### Worked example

Deploy and operate a critical payments service across legacy core, modern payment hub, sanctions screening, external network and data platforms. Include failure modes and recovery.

---

## Chapter 53. Legacy Modernisation, Data Migration and Transition Architecture

### Purpose

Show how a bank moves from the current state without creating unacceptable business or operational risk.

### Must cover

- current-state assessment;
- capability and application heat maps;
- domain sequencing;
- strangler patterns;
- façade and adapter;
- coexistence;
- dual run;
- parallel accounting;
- shadow processing;
- data migration;
- data cleansing;
- identifier mapping;
- reconciliation;
- cutover;
- rollback;
- product migration;
- customer and contract migration;
- historical data;
- document migration;
- interface transition;
- organisational readiness;
- operational readiness;
- control validation;
- regulatory and stakeholder engagement;
- vendor exit;
- technical decommissioning;
- data retention;
- benefit tracking;
- transition states and architecture debt.

### Worked example

Modernise term deposits or loan servicing from a legacy core to a target platform while channels, statements, general ledger, data warehouse and regulatory reporting continue to operate.

---

## Chapter 54. Governance, Ownership and the Architecture Repository

### Purpose

Show how the model set remains trustworthy.

### Must cover

- architecture principles;
- decision rights;
- enterprise, domain, solution, data and security architecture roles;
- product, process, capability, application, service, data and control ownership;
- architecture review;
- BIAN mapping governance;
- catalogue governance;
- interface governance;
- data governance;
- model governance;
- standards and exceptions;
- lifecycle status;
- versioning;
- evidence;
- waivers;
- technical debt;
- repository structure;
- relationships and queryability;
- diagrams as views of controlled data;
- change impact;
- review cycle;
- ownership transfer;
- audit and assurance;
- keeping the case study itself consistent.

### Required artefact

A Horizon Bank architecture governance and responsibility model with explicit decision rights.

---

## Chapter 55. Measures, Quality Gates and the Full-Bank Coverage Audit

### Purpose

Provide objective tests for completeness and quality.

### Must cover

- business outcome measures;
- customer measures;
- process measures;
- straight-through processing;
- exception and rework;
- risk and control measures;
- data-quality measures;
- technology and reliability measures;
- cost and simplification;
- architecture fitness;
- service ownership;
- decommissioning;
- mapping completeness;
- source freshness;
- diagram quality;
- chapter quality;
- traceability completeness;
- residual risks and gaps.

### Required deliverables

- full Part V coverage audit;
- domain completeness matrix;
- application coverage matrix;
- data coverage matrix;
- control coverage matrix;
- BIAN verification report;
- diagram audit;
- source audit;
- terminology audit;
- unresolved-gap register.

No chapter may be moved to `Ready for Author Approval` until this audit passes for its declared scope.

---

## Chapter 56. Integrated End-to-End Scenarios and Practitioner Reference

### Purpose

Finish Part V by connecting domains rather than repeating definitions.

### Required integrated scenarios

At minimum include concise but complete traceability across:

1. retail customer onboarding and current-account opening;
2. fixed-deposit placement and maturity;
3. secured lending with collateral and later delinquency;
4. domestic or instant payment;
5. cross-border corporate payment;
6. card purchase, clearing, statement and dispute;
7. corporate cash-management and trade-finance interaction;
8. wealth order through settlement and custody;
9. treasury funding and liquidity response;
10. month-end close and risk or regulatory reporting;
11. major service disruption affecting a critical operation.

Each scenario must connect:

- stakeholder outcome;
- value stream;
- capabilities;
- process;
- BIAN candidates;
- applications;
- authoritative information;
- APIs, events, batch, files and external networks;
- accounting;
- controls;
- deployment and operational concerns;
- metrics;
- failure and exception paths.

### Practitioner reference

Finish with:

- mapping checklist;
- domain checklist;
- application checklist;
- data checklist;
- integration checklist;
- security and resilience checklist;
- migration checklist;
- common mistakes;
- glossary pointers;
- figure index;
- coverage-matrix navigation.

Do not turn the last chapter into a loose collection of definitions already taught earlier.


---

# 8. Mandatory full-bank business coverage

The following is the minimum enterprise business taxonomy. Codex may refine names after research, but no material area may disappear.

## 8.1 Strategy, governance and product management

- corporate strategy;
- portfolio strategy;
- market and customer-segment strategy;
- legal-entity strategy;
- capital and funding strategy;
- product strategy;
- product design;
- product approval;
- product catalogue;
- pricing;
- fee and rate management;
- proposition and offer management;
- product performance;
- conduct and product-governance review;
- change portfolio;
- merger, acquisition and divestment support;
- architecture and technology strategy.

## 8.2 Customer, party and relationship

- prospect and lead;
- party identification;
- customer establishment;
- organisation and group hierarchy;
- relationship management;
- customer due diligence;
- customer risk rating;
- onboarding;
- periodic review;
- beneficial ownership;
- mandate and signatory;
- customer profile;
- consent and preferences;
- service request;
- complaint;
- retention;
- exit and offboarding.

## 8.3 Channels and distribution

- mobile;
- web;
- corporate portal;
- branch;
- relationship manager;
- contact centre;
- automated teller machine;
- point of sale where relevant;
- merchant channel;
- agent or partner;
- open-banking and embedded-finance interfaces;
- assisted service;
- self-service;
- campaign and digital engagement;
- authentication and entitlement;
- channel analytics.

## 8.4 Deposits and account services

- current accounts;
- savings accounts;
- term and fixed deposits;
- notice deposits where relevant;
- account opening;
- account maintenance;
- interest;
- fees;
- statements;
- restrictions;
- dormancy;
- closure;
- cash deposit and withdrawal where relevant;
- cheque services where retained;
- deposit insurance reporting where applicable.

## 8.5 Lending and credit

- consumer lending;
- mortgage;
- credit card lending;
- vehicle or asset finance at catalogue level;
- SME lending;
- corporate lending;
- overdraft;
- revolving facility;
- trade loan;
- syndicated facility at catalogue level;
- origination;
- underwriting;
- approval;
- documentation;
- disbursement;
- servicing;
- repricing;
- repayment;
- restructuring;
- settlement;
- closure.

## 8.6 Collateral, limits and collections

- collateral capture;
- legal interest;
- valuation;
- eligibility;
- allocation;
- monitoring;
- substitution;
- release;
- limit establishment;
- limit hierarchy;
- utilisation;
- exposure;
- concentration;
- covenant;
- early warning;
- collections;
- recovery;
- repossession or enforcement;
- write-off;
- impairment linkage.

## 8.7 Payments

- internal transfer;
- domestic credit transfer;
- instant payment;
- real-time gross settlement;
- automated clearing house;
- cross-border payment;
- direct debit;
- standing order;
- bulk payment;
- payroll;
- request to pay where relevant;
- payment initiation;
- validation;
- screening;
- routing;
- clearing;
- settlement;
- posting;
- investigation;
- return and recall;
- reconciliation;
- correspondent banking.

## 8.8 Cards and acquiring

- card product;
- card issuance;
- card account;
- card and token lifecycle;
- credential and personal identification number;
- authorisation;
- clearing;
- settlement;
- billing;
- interest;
- rewards;
- dispute;
- chargeback;
- fraud;
- merchant onboarding;
- terminal and gateway;
- acquiring;
- merchant settlement;
- scheme reconciliation.

## 8.9 Corporate transaction banking

- corporate onboarding;
- complex mandates;
- entitlements and approvals;
- account structures;
- virtual accounts;
- bulk payment;
- host-to-host;
- cash-position reporting;
- receivables;
- liquidity sweeping;
- pooling;
- implementation and service management;
- pricing and billing.

## 8.10 Trade finance

- import letter of credit;
- export letter of credit;
- guarantee;
- standby instrument;
- documentary collection;
- trade loan;
- supply-chain finance at catalogue level;
- document presentation and checking;
- discrepancy;
- amendment;
- claim;
- settlement;
- contingent liability;
- fee;
- sanctions and trade-control checks.

## 8.11 Wealth and investments

- client profiling;
- investment risk;
- advice;
- discretionary portfolio;
- order;
- execution;
- allocation;
- position;
- valuation;
- performance;
- fees;
- statement;
- tax reporting at a conceptual level;
- product governance.

## 8.12 Securities and custody

- instrument and market reference data;
- order and trade;
- confirmation;
- clearing and settlement;
- custody account;
- safekeeping;
- position;
- corporate action;
- income;
- asset servicing;
- reconciliation;
- depository and custodian connectivity.

## 8.13 Treasury, markets and balance-sheet management

- foreign exchange;
- money market;
- securities dealing;
- derivatives at catalogue level;
- confirmation;
- settlement;
- position;
- valuation;
- market risk;
- counterparty risk;
- collateral or margin;
- funding;
- liquidity;
- intraday liquidity;
- asset-liability management;
- funds transfer pricing;
- interest-rate risk;
- capital planning;
- stress testing.

## 8.14 Finance

- accounting policy;
- chart of accounts;
- accounting rule;
- subledger;
- general ledger;
- journal;
- accrual;
- allocation;
- intercompany;
- reconciliation;
- suspense;
- close;
- consolidation;
- impairment;
- tax;
- management reporting;
- statutory reporting;
- prudential reporting;
- profitability and cost.

## 8.15 Risk and control

- credit risk;
- market risk;
- liquidity risk;
- operational risk;
- model risk;
- cyber risk;
- third-party risk;
- conduct risk;
- compliance risk;
- risk appetite;
- control design;
- control operation;
- control testing;
- issue and remediation;
- scenario and stress testing;
- risk aggregation and reporting.

## 8.16 Financial crime and fraud

- customer screening;
- payment screening;
- transaction monitoring;
- customer risk;
- sanctions;
- politically exposed persons;
- adverse media;
- alert;
- investigation;
- suspicious-activity reporting as jurisdiction-dependent;
- fraud assessment;
- fraud alert;
- investigation;
- recovery;
- model and rule management;
- typology;
- intelligence.

## 8.17 Enterprise operations and support

- workflow;
- case management;
- document management;
- records management;
- statements and correspondence;
- notifications;
- enterprise integration;
- scheduling;
- managed file transfer;
- identity and access;
- security operations;
- service management;
- procurement;
- supplier management;
- outsourcing and third-party management;
- human resources;
- legal;
- audit;
- facilities and physical security;
- business continuity;
- data and analytics;
- artificial-intelligence governance.

---

# 9. Mandatory process architecture

Create a controlled Level 0 to Level 2 process catalogue. Use Level 3 and Level 4 only where the chapter needs behavioural detail.

## 9.1 Suggested Level 0 process groups

1. Set direction and govern the bank
2. Understand markets and manage products
3. Acquire and manage customers
4. Originate and manage deposits
5. Originate and manage credit
6. Manage collateral, limits and collections
7. Execute and service payments
8. Issue and acquire cards
9. Deliver corporate banking and cash management
10. Deliver trade finance
11. Deliver wealth, investment and custody services
12. Manage treasury, markets, funding, liquidity and capital
13. Manage risk, compliance, financial crime and fraud
14. Manage accounting, finance, tax and reporting
15. Manage channels, communications and service operations
16. Manage data, technology, security and resilience
17. Manage people, suppliers, legal matters and assurance

## 9.2 Process catalogue fields

Every controlled process must include:

- process ID;
- Level 0, Level 1, Level 2 and optional Level 3 hierarchy;
- name;
- definition;
- trigger;
- intended outcome;
- start and end boundaries;
- customer or stakeholder;
- business owner;
- operating unit;
- roles;
- products;
- capabilities exercised;
- important decisions;
- principal information;
- applications;
- external parties;
- controls;
- measures;
- upstream and downstream processes;
- BIAN scenario or responsibility references where relevant;
- status and version;
- chapter and figure references.

## 9.3 Behavioural modelling rules

- Use BPMN when sequence, roles, exceptions, timers, messages or compensation matter.
- Do not place every application as a BPMN pool merely to show technology.
- Use business roles and participants in business process views.
- Add application interaction in a separate sequence, collaboration or traceability view.
- Include failure and exception paths, not only happy paths.
- Include manual work, queues, service levels, repair and evidence.
- Use DMN for material decision logic such as eligibility, credit approval, pricing, routing, fraud referral or document discrepancy, where it improves clarity.
- Do not encode real jurisdiction-specific policy as universal rules.
- For critical financial processes, show reconciliation and accounting consequences.

---

# 10. Mandatory capability architecture

Create a complete Level 1 capability map and controlled Level 2 catalogue.

## 10.1 Capability categories

At minimum include:

### Direction and governance

- Strategy Management
- Enterprise Governance
- Legal Entity Management
- Architecture Management
- Portfolio and Change Management
- Policy Management
- Regulatory Change Management

### Market, product and pricing

- Market and Customer Insight
- Product Management
- Product Catalogue Management
- Proposition and Offer Management
- Pricing and Rate Management
- Product Governance
- Campaign Management

### Customer and relationship

- Party Management
- Customer Relationship Management
- Customer Onboarding
- Customer Due Diligence
- Identity Verification
- Customer Risk Assessment
- Mandate and Signatory Management
- Consent and Preference Management
- Customer Servicing
- Complaint Management
- Customer Offboarding

### Channels and engagement

- Mobile Banking
- Internet Banking
- Corporate Digital Banking
- Branch Banking
- Contact Centre
- Relationship Manager Enablement
- Automated Teller Machine Services
- Partner and Open API Banking
- Authentication and Entitlement
- Journey Orchestration
- Customer Communication

### Deposits and accounts

- Deposit Product Fulfilment
- Current Account Management
- Savings Account Management
- Term Deposit Management
- Account Balance Management
- Interest Management
- Fee and Charge Management
- Account Restriction and Dormancy
- Statement and Advice Management
- Cash and Cheque Services where applicable

### Credit and lending

- Credit Application Management
- Credit Assessment
- Credit Decisioning
- Loan Origination
- Facility Management
- Consumer Loan Management
- Mortgage Management
- SME Loan Management
- Corporate Loan Management
- Loan Servicing
- Repayment Management
- Credit Pricing
- Covenant Management
- Restructuring

### Collateral, limits and collections

- Collateral Management
- Collateral Valuation
- Security Interest Management
- Limit Management
- Exposure Management
- Credit Monitoring
- Early Warning
- Collections Management
- Recovery Management
- Write-off Management

### Payments

- Payment Initiation
- Payment Validation
- Payment Authentication
- Payment Screening
- Payment Fraud Assessment
- Payment Routing
- Payment Orchestration
- Clearing
- Settlement
- Account Posting
- Payment Investigation
- Payment Reconciliation
- Correspondent Banking
- Direct Debit Management
- Standing Order Management

### Cards and merchant services

- Card Product Management
- Card Issuing
- Card Lifecycle Management
- Card Authorisation
- Card Clearing and Settlement
- Card Billing
- Card Dispute and Chargeback
- Card Fraud Management
- Rewards Management
- Merchant Onboarding
- Merchant Acquiring
- Merchant Settlement

### Corporate banking and trade

- Corporate Relationship Management
- Corporate Entitlement Management
- Cash Management
- Virtual Account Management
- Liquidity Sweeping and Pooling
- Corporate Payment Services
- Receivables Management
- Trade Finance
- Letter of Credit Management
- Guarantee Management
- Documentary Collection
- Supply-Chain Finance

### Wealth, markets and securities

- Wealth Advisory
- Investment Suitability
- Portfolio Management
- Order Management
- Trade Execution
- Investment Product Management
- Securities Settlement
- Custody
- Position Management
- Corporate Action Management
- Asset Servicing
- Investment Performance Reporting

### Treasury and balance sheet

- Treasury Dealing
- Market Data Management
- Trade Capture
- Position and Valuation
- Market Risk Management
- Counterparty Exposure Management
- Funding Management
- Liquidity Management
- Intraday Liquidity Management
- Asset-Liability Management
- Funds Transfer Pricing
- Capital Management
- Stress Testing

### Finance

- Accounting Rules Management
- Product Accounting
- Subledger Management
- General Ledger
- Journal Management
- Reconciliation
- Financial Close
- Consolidation
- Impairment and Expected Credit Loss
- Tax Management
- Management Accounting
- Profitability Management
- Statutory Reporting
- Regulatory Reporting

### Risk, compliance and assurance

- Enterprise Risk Management
- Credit Risk Management
- Market Risk Management
- Liquidity Risk Management
- Operational Risk Management
- Model Risk Management
- Compliance Management
- Financial Crime Management
- Sanctions Management
- Transaction Monitoring
- Fraud Management
- Control Management
- Issue and Remediation Management
- Legal Management
- Audit Management
- Third-Party Risk Management

### Data, technology and operations

- Data Governance
- Master and Reference Data Management
- Data Quality Management
- Metadata and Lineage Management
- Data Integration
- Analytics and Reporting
- Artificial Intelligence and Model Management
- API Management
- Event Management
- File and Batch Management
- Workflow and Case Management
- Document and Record Management
- Identity and Access Management
- Cyber Security
- Technology Platform Management
- Service Management
- Observability
- Capacity Management
- Resilience and Continuity
- Supplier and Outsourcing Management

## 10.2 Capability catalogue fields

- capability ID;
- Level 1 and Level 2 hierarchy;
- stable name;
- definition;
- outcome;
- scope and exclusions;
- owner;
- stakeholders;
- products and value streams supported;
- processes that exercise it;
- applications that support it;
- principal data;
- controls;
- maturity;
- pain;
- strategic importance;
- change demand;
- target maturity;
- measures;
- candidate BIAN mapping references;
- evidence and version.

Do not name an application, team or department as a capability.

---

# 11. Mandatory application architecture

Create an expanded, controlled `system-landscape.md` or a successor catalogue. The name “system” must be used consistently with the glossary.

## 11.1 Application taxonomy

Every application or platform must be classified by role, such as:

- system of engagement;
- journey-orchestration platform;
- system of record;
- system of processing;
- system of control;
- system of insight;
- integration platform;
- technology platform;
- external service;
- transitional adapter.

One application may have more than one qualified role, but the scope must be explicit.

## 11.2 Minimum application families

### Channels

- Retail Mobile Banking
- Retail Internet Banking
- Corporate Banking Portal
- Branch Workstation
- Contact Centre Desktop
- Relationship Manager Workbench
- Automated Teller Machine Platform
- Merchant Portal
- Partner and Open API Gateway
- Host-to-Host Corporate Gateway

### Engagement and orchestration

- Customer Relationship Management Platform
- Customer Onboarding Platform
- Digital Journey Orchestration
- Service Request and Case Management
- Workflow and Business Process Management
- Document Capture
- Document Management
- Electronic Signature
- Notification Platform
- Correspondence and Template Management
- Statement Generation
- Customer Consent and Preference
- Customer Analytics and Next-Best-Action

### Customer, party and product

- Party and Customer Master
- Customer Relationship Repository
- Organisation and Hierarchy Management
- Mandate and Signatory Management
- Product Catalogue
- Pricing and Rate Management
- Agreement and Contract Repository where separate
- Reference Data Management

### Deposits and accounts

- Core Deposit System
- Current and Savings Account Engine
- Term and Fixed Deposit System
- Interest and Fee Engine
- Account Balance and Posting Engine where separate
- Cheque and Cash Service Platform where retained
- Deposit Insurance Reporting Adapter where applicable

### Lending

- Loan Origination System
- Credit Decisioning Platform
- Bureau Integration
- Consumer Loan Management System
- Mortgage Platform
- SME and Corporate Lending Platform
- Facility and Limit Management
- Loan Servicing System
- Covenant Monitoring
- Collections and Recovery Platform
- Collateral Management System
- Impairment and Expected-Credit-Loss Platform where separate

### Payments

- Payment Initiation Service
- Enterprise Payment Hub
- Payment Gateway
- Payment Routing and Orchestration
- Real-Time Payment Switch
- Automated Clearing House Gateway
- Real-Time Gross Settlement Gateway
- Cross-Border Payment Gateway
- SWIFT Connectivity
- Payment Screening
- Payment Fraud Decisioning
- Payment Investigation
- Nostro Management
- Payment Reconciliation

### Cards and acquiring

- Card Management System
- Card Authorisation Switch
- Card Token and Credential Service
- Card Clearing and Settlement
- Card Billing and Statement
- Card Dispute and Chargeback
- Card Fraud Platform
- Rewards Platform
- Merchant Management System
- Acquiring Switch or Gateway
- Merchant Settlement
- Scheme Connectivity

### Corporate banking and trade finance

- Corporate Cash Management Platform
- Virtual Account Platform
- Liquidity Sweeping and Pooling Engine
- Corporate Billing and Pricing
- Host-to-Host File Gateway
- Trade Finance Platform
- Letter of Credit and Guarantee Processing
- Trade Document Management
- Supply-Chain Finance Platform where in scope

### Wealth, securities and custody

- Wealth Management Platform
- Advisory and Suitability Platform
- Portfolio Management System
- Order Management System
- Execution Management or Broker Connectivity
- Securities Processing Platform
- Custody Platform
- Corporate Actions Platform
- Position and Valuation Platform
- Market Data Platform
- Investment Performance and Client Reporting

### Treasury and markets

- Treasury Management System
- Front-Office Trading Platform
- Trade Capture and Confirmation
- Market and Counterparty Risk Platform
- Treasury Settlement
- Liquidity Management
- Intraday Liquidity
- Asset-Liability Management
- Funds Transfer Pricing
- Collateral and Margin Platform where separate

### Finance and enterprise reporting

- Product Accounting Engine
- Finance Subledger
- General Ledger
- Accounting Rules Engine
- Journal Management
- Reconciliation Platform
- Financial Close and Consolidation
- Management Accounting
- Profitability and Cost Allocation
- Tax Platform
- Regulatory Reporting Platform
- Risk Reporting Platform

### Risk, compliance and control

- Customer Screening
- Payment and Transaction Screening
- Transaction Monitoring
- Fraud Management
- Enterprise Risk Platform
- Credit Risk Platform
- Market Risk Platform
- Operational Risk and Loss Event
- Model Inventory and Validation
- Governance, Risk and Compliance Platform
- Audit Management
- Regulatory Change
- Legal Matter and Hold Management
- Control Evidence Repository

### Integration

- API Gateway
- API Management Platform
- Enterprise Service Bus or Integration Platform
- Event Streaming Platform
- Message Broker
- Managed File Transfer
- Batch Scheduler
- Workflow Engine
- Service Registry and Catalogue
- Schema Registry
- Business Rules or Decision Platform where used
- External Network Gateways

### Data and analytics

- Master Data Management
- Operational Data Store
- Change Data Capture Platform
- Enterprise Data Lakehouse
- Enterprise Data Warehouse
- Finance Data Mart
- Risk Data Mart
- Customer 360
- Metadata Catalogue
- Data Lineage Platform
- Data Quality Platform
- Business Intelligence Platform
- Regulatory Data Platform
- Feature Store where justified
- Model Development and Serving Platform
- Data Privacy and Masking Service

### Security and operations

- Customer Identity and Access Management
- Workforce Identity and Access Management
- Privileged Access Management
- Key and Certificate Management
- Secrets Management
- Security Information and Event Management
- Security Orchestration and Response
- Fraud and Cyber Intelligence Integration
- Endpoint and Network Security
- Observability Platform
- Central Logging
- Application Performance Monitoring
- IT Service Management
- Configuration Management Database
- Backup and Recovery
- Cyber-Recovery Vault
- Release and Deployment Platform

### Enterprise support

- Human Resources
- Finance and Procurement
- Supplier and Contract Management
- Learning
- Facilities
- Enterprise Content
- Collaboration
- Legal and Audit systems

## 11.3 Application catalogue fields

For every controlled application:

- application ID;
- name;
- definition and responsibility;
- application role;
- business owner;
- application owner;
- service owner;
- support team;
- vendor or build classification;
- deployment model;
- legal entities and regions;
- products and customer segments;
- capabilities supported;
- processes supported;
- candidate BIAN mappings;
- authoritative data;
- data copied;
- inbound and outbound interfaces;
- external dependencies;
- accounting relevance;
- control relevance;
- confidentiality, integrity and availability classification;
- criticality;
- recovery time objective;
- recovery point objective;
- peak volume and latency class;
- lifecycle status;
- strategic disposition;
- target replacement or retention;
- technical debt;
- source and evidence;
- chapter and figure references.

Do not create names merely to fill boxes. A name must be controlled before repeated manuscript use.

---

# 12. Mandatory information and data architecture

## 12.1 Data domains

At minimum define:

1. Party
2. Customer
3. Organisation and Legal Entity
4. Relationship and Household or Group
5. Identity and Contact
6. Beneficial Ownership
7. Consent and Preference
8. Mandate, Signatory and Entitlement
9. Product
10. Offer, Price, Rate and Fee
11. Agreement and Contract
12. Account
13. Deposit
14. Balance, Hold and Posting
15. Credit Application
16. Facility and Limit
17. Loan
18. Repayment Schedule
19. Collateral and Valuation
20. Exposure and Credit Risk
21. Payment Instruction
22. Payment Transaction
23. Clearing and Settlement
24. Correspondent Account and Nostro Position
25. Card
26. Card Account and Token
27. Merchant and Terminal
28. Trade-Finance Instrument
29. Security and Financial Instrument
30. Order and Trade
31. Portfolio, Position and Valuation
32. Corporate Action
33. Treasury Position and Cash Flow
34. Market and Reference Data
35. Accounting Entry
36. Subledger and General Ledger
37. Balance and Reconciliation
38. Impairment and Provision
39. Statement, Advice and Communication
40. Document and Record
41. Case, Alert, Investigation and Complaint
42. Risk Assessment
43. Control and Evidence
44. Regulatory and Management Report
45. Employee, Supplier and Third Party
46. Technical Service, Configuration and Telemetry
47. Metadata, Lineage and Data Quality
48. Model, Feature and Decision Output

## 12.2 Data-domain catalogue fields

For every domain:

- data-domain ID;
- name and definition;
- conceptual entities;
- business owner;
- data owner;
- steward;
- authoritative application;
- permitted systems of entry;
- downstream copies;
- primary identifiers;
- cross-reference rules;
- lifecycle states;
- creation and update events;
- quality rules;
- critical data elements;
- classification;
- privacy considerations;
- residency;
- retention;
- legal hold;
- lineage;
- reconciliation;
- interfaces;
- reporting use;
- analytical use;
- model use;
- controls;
- BIAN information references;
- chapter and figure references.

## 12.3 System-of-record rules

Do not call an application a system of record without defining:

- which entity or attribute it is authoritative for;
- which lifecycle stage;
- which legal entity or geography;
- which transaction timing;
- which exceptions;
- how conflicting updates are resolved;
- how downstream copies are synchronised;
- how reconciliation proves completeness and accuracy.

There may be one authoritative source per attribute or lifecycle stage, not necessarily one application for the entire business concept.

## 12.4 Data quality and lineage

At minimum cover:

- accuracy;
- completeness;
- timeliness;
- consistency;
- validity;
- uniqueness;
- integrity;
- traceability;
- ownership;
- issue management;
- control totals;
- source-to-report lineage;
- reconciliation with accounting where appropriate;
- manual adjustments;
- end-user computing risk;
- lineage through transformations and models.

## 12.5 Operational and analytical separation

Explain the roles and trade-offs of:

- transaction database;
- operational data store;
- cache;
- search index;
- event log;
- data lakehouse;
- enterprise data warehouse;
- data mart;
- semantic layer;
- report store;
- feature store;
- archive;
- document repository.

Do not imply that copying all operational data into a lake automatically creates trusted enterprise data.

---

# 13. Mandatory accounting and financial mechanics

Banking architecture cannot be taught comprehensively without accounting and settlement.

For each product domain, identify:

- balance-sheet classification at a conceptual level;
- income and expense;
- fees;
- accrual;
- principal;
- settlement account;
- product subledger;
- general-ledger interface;
- suspense and exception accounts;
- reconciliation;
- impairment or provision where relevant;
- off-balance-sheet commitment where relevant;
- valuation where relevant;
- financial and regulatory reporting consumers.

Include a controlled event-to-accounting register with fields such as:

- business event;
- source application;
- accounting rule;
- debit account category;
- credit account category;
- amount basis;
- currency;
- value date;
- booking date;
- legal entity;
- product;
- reversal rule;
- source reference;
- subledger;
- general-ledger posting;
- reconciliation key;
- approval and evidence.

All journal examples must be labelled as simplified educational illustrations. They must not claim universal accounting treatment.

---

# 14. Mandatory integration architecture

## 14.1 Interaction styles

The manuscript must teach when and why to use:

- synchronous request-response API;
- asynchronous command;
- business event;
- message queue;
- event stream;
- scheduled batch;
- managed file;
- workflow and human task;
- external network message;
- database view or replication as a controlled legacy pattern;
- user-interface integration;
- robotic automation only as a temporary or controlled solution.

## 14.2 Interface catalogue fields

- interface ID;
- business purpose;
- producer or caller;
- consumer or provider;
- owner;
- contract;
- business semantic;
- interaction style;
- protocol and transport;
- authentication;
- authorisation;
- encryption;
- data classification;
- frequency or trigger;
- volume;
- latency;
- availability;
- ordering;
- delivery guarantee;
- idempotency;
- duplicate handling;
- timeout;
- retry;
- compensation;
- error and repair;
- reconciliation;
- schema version;
- compatibility;
- monitoring;
- retention and replay;
- external dependency;
- BIAN Service Operation or ISO 20022 reference where applicable;
- current, target or transitional status.

## 14.3 External ecosystem

Include controlled entries for:

- central bank;
- domestic clearing house;
- real-time gross settlement;
- instant-payment network;
- SWIFT;
- correspondent banks;
- card schemes;
- payment processors;
- automated teller machine networks;
- credit bureaus;
- identity providers;
- government and tax services;
- sanctions and screening data providers;
- market-data providers;
- exchanges;
- brokers;
- central counterparties;
- central securities depositories;
- custodians;
- registrars;
- payment service providers;
- fintech partners;
- cloud and software-as-a-service providers;
- document, communication and postal providers.

For each, show responsibility, trust boundary, data exchange, operational dependency, contractual concern, fallback and exit consideration.

---

# 15. Mandatory security, control and resilience architecture

## 15.1 Security viewpoints

Cover:

- customer identity;
- workforce identity;
- privileged access;
- machine and workload identity;
- authentication;
- adaptive authentication;
- authorisation;
- entitlements;
- segregation of duties;
- maker-checker;
- consent;
- session and device trust;
- network zones;
- data classification;
- encryption in transit and at rest;
- tokenisation;
- key and certificate lifecycle;
- secrets;
- secure coding;
- software supply chain;
- vulnerability;
- logging;
- detection;
- response;
- recovery;
- fraud and cyber collaboration;
- privacy;
- records;
- third-party access;
- administrative and break-glass access.

## 15.2 Control catalogue fields

- control ID;
- risk or obligation;
- control objective;
- control activity;
- preventive, detective or corrective;
- automated, manual or hybrid;
- process stage;
- application;
- data;
- owner;
- operator;
- evidence;
- frequency;
- threshold;
- exception;
- escalation;
- test method;
- assurance owner;
- issue linkage;
- source;
- jurisdiction;
- chapter and figure references.

## 15.3 Resilience model

For every critical operation:

- customer or market outcome;
- legal entities;
- products;
- process;
- people;
- applications;
- data;
- locations;
- third parties;
- infrastructure;
- upstream and downstream dependencies;
- maximum tolerable disruption or impact tolerance where the concept is used;
- recovery time;
- recovery point;
- manual workaround;
- degraded service;
- communications;
- recovery sequence;
- test scenarios;
- unresolved vulnerabilities.

Critical-operation mapping must be business-led. Do not begin with servers and infer business criticality afterwards.

---

# 16. BIAN mapping rules

These rules are mandatory throughout Part V.

## 16.1 Never use automatic equivalence

Do not write:

```text
Service Domain = capability
Service Domain = process
Service Domain = department
Service Domain = application
Service Domain = microservice
Service Domain = database
Service Domain = API
Service Operation = endpoint
Business Scenario = mandatory process
Business Object Model = physical schema
```

Use qualified relationships such as:

- informs;
- is a candidate reference for;
- overlaps with;
- is partially realised by;
- contributes to;
- participates in;
- supports;
- exchanges information with;
- maps to for the stated scope;
- is implemented through;
- is authoritative for;
- runs on;
- is constrained by.

## 16.2 Mapping register

Create a controlled BIAN mapping register with:

- mapping ID;
- local source element;
- local element type;
- local definition;
- BIAN target object;
- BIAN object type;
- BIAN version;
- official URL;
- mapping relation;
- scope;
- exclusions;
- rationale;
- evidence;
- confidence;
- owner;
- reviewer;
- status;
- current, target or transitional;
- effective date;
- review date;
- affected applications, data and interfaces;
- chapter and figure references.

## 16.3 Conformance language

Do not casually claim “BIAN compliant”.

Prefer precise statements:

- uses BIAN 14.0 as a reference;
- maps selected local responsibilities to verified BIAN Service Domains;
- uses BIAN semantics for selected exchanges;
- adapts a BIAN Business Scenario;
- preserves a BIAN-informed logical boundary;
- differs from BIAN in the following documented ways.

If a formal BIAN conformance scheme applies, research and cite it before using the term.

## 16.4 BIAN and local architecture

The case study must show three separate views:

1. **Official reference view**
   What BIAN defines.

2. **Horizon Bank logical view**
   How Horizon Bank interprets responsibilities, processes and information.

3. **Horizon Bank physical view**
   How applications, interfaces, data stores, teams and deployments realise the design.

Trace them. Do not collapse them.

---

# 17. Standard domain-chapter template

Every domain chapter from 37 to 48 must use this structure unless a documented reason requires a variation.

## 17.1 Front matter

- chapter title;
- status;
- purpose;
- reader outcomes;
- prerequisites;
- scope;
- explicit exclusions;
- assumptions;
- required models;
- worked scenario;
- source requirements.

## 17.2 Domain content

1. **Plain-language explanation**
2. **Why the domain matters to the bank and customer**
3. **Products and services**
4. **Customer segments and channels**
5. **Departments, roles and decision rights**
6. **Economics, balance-sheet and accounting relevance**
7. **Value streams and customer journeys**
8. **Capabilities**
9. **Process hierarchy**
10. **Detailed happy path**
11. **Exceptions, repairs, reversals and manual work**
12. **Important decisions and rules**
13. **Candidate BIAN responsibilities**
14. **Application architecture**
15. **Information and systems of record**
16. **APIs, events, batch, files and external networks**
17. **Accounting events and reconciliation**
18. **Risks, controls and evidence**
19. **Security and privacy**
20. **Volumes, latency, availability and operational criticality**
21. **End-of-day, cut-off or scheduling concerns**
22. **Observability and support**
23. **Current-state pain points**
24. **Target-state options**
25. **Migration considerations**
26. **Integrated worked scenario**
27. **Common mistakes**
28. **Completion checklist**
29. **Key takeaways**
30. **Practical exercise**
31. **Review checklist**
32. **References and further reading**

## 17.3 Minimum domain diagrams

Each domain must have, where relevant:

- one domain context diagram;
- one capability or responsibility view;
- one Level 1 or Level 2 process view;
- one application collaboration or C4 view;
- one information or lifecycle view;
- one end-to-end sequence;
- one control or decision view;
- one accounting or reconciliation view for financial domains;
- one current-to-target view where transformation is discussed.

Do not create diagrams merely to meet a number. Each must answer a distinct reader question.

---

# 18. Diagram programme

## 18.1 Enterprise diagrams required before domain completion

At minimum register specifications for:

- `FIG-31-01`: Part V navigation and traceability method
- `FIG-32-01`: Full-service bank business model
- `FIG-32-02`: Business lines, legal entities and enterprise functions
- `FIG-32-03`: Simplified bank balance sheet and income flows
- `FIG-32-04`: Front-to-back operating model
- `FIG-33-01`: Full bank capability landscape
- `FIG-33-02`: Enterprise value-stream portfolio
- `FIG-33-03`: Level 0 and Level 1 process landscape
- `FIG-33-04`: Organisation, roles and decision rights
- `FIG-33-05`: Capability-to-process heat map
- `FIG-34-01`: Complete layered application landscape
- `FIG-34-02`: Application-to-capability heat map
- `FIG-34-03`: Application integration and external ecosystem
- `FIG-34-04`: Current, target and transition application views
- `FIG-35-01`: Enterprise data-domain map
- `FIG-35-02`: System-of-record matrix
- `FIG-35-03`: Operational-to-analytical data flow
- `FIG-35-04`: Source-to-report lineage
- `FIG-36-01`: Hybrid technology reference architecture
- `FIG-36-02`: Security trust zones
- `FIG-36-03`: Critical-service dependency and resilience map
- `FIG-36-04`: Identity and access architecture
- `FIG-36-05`: Observability and operational-control architecture
- `FIG-49-01`: BIAN mapping metamodel
- `FIG-53-01`: Current-to-target transition roadmap
- `FIG-54-01`: Architecture governance model
- `FIG-55-01`: Full-bank coverage dashboard
- `FIG-56-01`: Integrated full-bank scenario map

Use chapter-consistent IDs if files are renamed. Avoid duplicate IDs.

## 18.2 Tool choice

Follow repository policy:

- PlantUML for UML, C4, sequence, state, component, deployment and simple entity-relationship diagrams;
- Draw.io for the large capability map, heat maps, complex application landscape and roadmaps where manual placement is necessary;
- Camunda Modeler for formal BPMN and DMN;
- Mermaid only for simple diagrams where it adds value.

Do not use Mermaid merely because it is quick if it produces an unreadable banking landscape.

## 18.3 Specification-first workflow

For every diagram:

1. create or update the specification;
2. define question, purpose and audience;
3. define scope and exclusions;
4. define notation;
5. list controlled elements;
6. list relationships;
7. define legend;
8. define intended page size;
9. identify source and copyright considerations;
10. identify accessibility needs;
11. request author review of the specification;
12. only then create source;
13. render to SVG;
14. inspect visually;
15. validate;
16. add caption and textual explanation;
17. update register status to no higher than `Review`.

## 18.4 Visual quality

The complete enterprise landscape may be a landscape page or two-page spread. It must remain readable when rendered in the book.

Check:

- no clipped text;
- no overlapping boxes;
- no unreadably small type;
- no excessive line crossings;
- clear hierarchy;
- consistent controlled names;
- explicit arrow direction;
- a legend that explains colour and line style;
- sufficient contrast;
- colour not used as the sole carrier of meaning;
- labels for current, target, external and transitional elements;
- no unexplained acronyms;
- correspondence between figure, caption and chapter prose.

---

# 19. Controlled repository artefacts to create or expand

Do not rely only on prose. Create controlled artefacts under the existing Horizon Bank example structure or a repository-consistent successor.

At minimum create or substantially expand:

```text
examples/horizon-bank/
├── bank-profile.md
├── assumptions.md
├── business-lines.md
├── legal-entities.md
├── customer-segments.md
├── products.md
├── value-streams.md
├── capabilities.md
├── processes.md
├── organisation-and-roles.md
├── actors.md
├── systems.md or system-landscape.md
├── application-interfaces.md
├── external-parties-and-networks.md
├── data-domains.md
├── systems-of-record.md
├── accounting-events.md
├── controls.md
├── critical-operations.md
├── technology-platforms.md
├── non-functional-requirements.md
├── bian-mapping-register.md
├── scenario-catalogue.md
├── coverage-matrix.md
└── README.md
```

Use existing file names when that avoids needless duplication. If a catalogue is better maintained as CSV or YAML for validation, provide both:

- a machine-readable source;
- a readable Markdown view or generated summary.

Do not create two competing sources of truth.

## 19.1 Master coverage matrix

The coverage matrix is central. It must include at least:

- coverage ID;
- business domain;
- business line;
- legal entity or scope;
- customer segment;
- product or service;
- value stream;
- capability Level 1;
- capability Level 2;
- process Level 0;
- process Level 1;
- process Level 2;
- process owner;
- organisation and roles;
- candidate BIAN Business Area;
- candidate BIAN Business Domain;
- candidate BIAN Service Domain;
- BIAN version;
- mapping status and confidence;
- application;
- application role;
- authoritative data;
- important data objects;
- API;
- event;
- batch or file;
- external network;
- accounting event;
- risk;
- control;
- criticality;
- availability;
- recovery time;
- recovery point;
- current, target or transitional;
- chapter;
- figure;
- source;
- owner;
- status;
- gap or action.

Create validation checks that identify blank mandatory fields and orphaned elements.

---

# 20. Architecture principles for the case study

Record these as proposed Horizon Bank principles, then refine through repository decision governance.

1. **Start from customer and stakeholder outcomes.**
2. **Model the whole bank before optimising one system.**
3. **Separate business, application, data and technology concerns, then connect them through traceability.**
4. **Use BIAN as a reference, not as a copied target architecture.**
5. **Do not infer physical service boundaries from Service Domain names.**
6. **Assign explicit ownership to capabilities, processes, applications, data, interfaces, controls and services.**
7. **Keep one qualified authoritative source for each critical datum or attribute scope.**
8. **Treat accounting, reconciliation and control evidence as first-class architecture concerns.**
9. **Choose synchronous, asynchronous, batch, file or workflow interaction based on business need and failure semantics.**
10. **Design for exceptions, repair, reversal and human judgement, not only straight-through happy paths.**
11. **Protect customer and payment data by design.**
12. **Map critical operations end to end, including people, technology, data and third parties.**
13. **Prefer simplification over adding another integration layer.**
14. **Modernise incrementally with controlled coexistence and measurable decommissioning.**
15. **Automate controls and evidence where it improves reliability, but retain accountable human decisions where needed.**
16. **Do not centralise every capability into an enterprise platform.**
17. **Do not duplicate common functions simply to preserve domain autonomy.**
18. **Make current, target and transitional states explicit.**
19. **Make assumptions, uncertainty and mapping confidence visible.**
20. **A diagram is a view of governed architecture information, not the source of truth by itself.**

---

# 21. Non-functional requirements framework

Every major application and domain must be assessed across:

- business criticality;
- customer impact;
- financial impact;
- regulatory impact;
- data sensitivity;
- availability;
- latency;
- throughput;
- concurrency;
- scalability;
- consistency;
- durability;
- recoverability;
- recovery time;
- recovery point;
- impact tolerance;
- security;
- privacy;
- auditability;
- traceability;
- non-repudiation where applicable;
- data retention;
- interoperability;
- maintainability;
- testability;
- portability;
- vendor lock-in;
- operability;
- observability;
- support hours;
- batch window;
- cut-off;
- peak calendar events;
- localisation;
- accessibility;
- third-party dependency;
- cost.

Do not assign numbers without evidence. Use illustrative classes where actual values are unavailable, for example:

```text
Criticality: Critical, High, Medium, Low
Latency: Real time, Near real time, Deferred, Batch
Consistency: Strong, Bounded, Eventual
Availability: Continuous, Extended hours, Business hours
Data class: Public, Internal, Confidential, Highly Restricted
```

Define each class.

---

# 22. Writing requirements

## 22.1 Voice

Write in the existing book’s practical teaching voice:

- direct;
- precise;
- calm;
- non-promotional;
- beginner-friendly without being childish;
- technically credible;
- grounded in examples.

Avoid:

- generic “in today’s rapidly evolving banking landscape” openings;
- empty statements that architecture “enhances efficiency and innovation”;
- repeated warnings with no new application;
- excessive bullet dumps without explanation;
- unexplained jargon;
- fictional precision;
- management-consulting slogans;
- claims that one tool or framework solves banking transformation.

## 22.2 Teaching pattern

For every major subject:

```text
plain explanation
→ formal term
→ question answered
→ real banking example
→ model or diagram
→ limitation
→ common mistake
→ practical exercise
```

## 22.3 Depth

Enterprise catalogues should be comprehensive. Detailed behavioural modelling should be selective and pedagogically useful.

Do not attempt to model every Level 4 procedure in the bank. Do model every major domain at catalogue level and enough detailed scenarios to teach how the architecture works.

## 22.4 Cross-domain links

Explicitly link domains. Examples:

- onboarding creates party, customer, agreement and entitlement data used by deposits, lending, payments and wealth;
- deposits provide accounts and balances used by payments and cards;
- payments affect account posting, liquidity, screening, reconciliation and statements;
- lending depends on customer, credit, collateral, limits, accounting and collections;
- cards depend on customer, credit or deposit accounts, payments, fraud, statements and finance;
- trade finance creates contingent obligations, fees, documents, limits and payments;
- wealth relies on customer profiling, market data, order management, settlement, custody and reporting;
- treasury consumes payment, deposit, loan and market cash-flow information;
- finance and risk aggregate all product domains;
- communications, workflow, documents, identity, integration and data span all domains.

The reader must see a bank as an interconnected operating system, not independent verticals.

---

# 23. Execution plan

Do not rewrite all chapters immediately. Work in controlled phases.

## Phase 0. Repository safety and baseline

1. Confirm branch and working-tree state.
2. Read mandatory repository files.
3. Inventory Part V files, statuses, links, figures, sources and controlled Horizon Bank artefacts.
4. Do not overwrite unrelated work.
5. Record the baseline commit.
6. Change Part V chapters incorrectly marked ready back to `Revision Required`.
7. Add a decision record that the Part V structure is being redesigned to fulfil the full-service-bank promise.

### Deliverable

```text
reviews/part-05/part-v-current-state-audit.md
```

The audit must state:

- what exists;
- what is reusable;
- what is repetitive;
- what is missing;
- which links and figures will be affected;
- which controlled names are insufficient;
- which current claims require source refresh;
- risks of restructuring.

## Phase 1. Research and architecture taxonomy

1. Research current BIAN 14.0 official material.
2. Research banking business and control concepts from primary sources.
3. Create source notes.
4. Define Horizon Bank assumptions.
5. Create the business, capability, process, application, data, integration, control and technology taxonomies.
6. Build the master coverage matrix.
7. Identify gaps before drafting chapters.

### Deliverables

- source notes;
- expanded Horizon Bank catalogues;
- BIAN mapping register;
- coverage matrix;
- glossary update proposals;
- source register updates.

## Phase 2. Redesign the book structure

1. Compare the current chapter structure with the proposed structure in this instruction.
2. Produce a mapping from old chapters and reusable sections to new chapters.
3. Identify content to move, merge, rewrite or remove.
4. Update `BOOK_PLAN.md`.
5. Update links and status planning.
6. Record structural decisions.
7. Create chapter purpose, reader outcomes and detailed outlines for Chapters 31 to 56.

### Deliverable

```text
reviews/part-05/part-v-redesign-plan.md
```

Do not begin full prose until the structure and catalogues are coherent.

## Phase 3. Enterprise baseline chapters

Draft Chapters 31 to 36.

For each chapter:

1. confirm purpose and dependencies;
2. use controlled catalogue names;
3. create source notes;
4. register diagram specifications;
5. draft prose;
6. add traceability;
7. run reviews;
8. update status.

Do not create diagram source before author approval of specifications, according to repository policy.

## Phase 4. Domain chapters

Draft Chapters 37 to 48 in coherent groups:

### Group A

- customer and party;
- deposits;
- lending;
- collateral, limits and collections.

### Group B

- payments;
- cards;
- corporate banking and trade finance.

### Group C

- wealth and securities;
- treasury and balance sheet;
- finance and accounting.

### Group D

- risk and compliance;
- channels and shared services.

After each group, run a cross-domain consistency review before proceeding.

## Phase 5. Implementation and transformation chapters

Draft Chapters 49 to 56.

Ensure these chapters reuse the governed case-study material rather than inventing new examples or names.

## Phase 6. Full-bank audit

Run all quality passes and close or document every gap.

Only after the audit may a chapter be considered for `Ready for Author Approval`.

---

# 24. Required review passes

Every substantial chapter or group must pass these reviews.

## 24.1 Banking-domain review

Check:

- product lifecycle;
- department and role realism;
- front-to-back process;
- exceptions;
- settlement;
- accounting;
- reconciliation;
- controls;
- operational timing;
- cross-domain dependencies.

## 24.2 Enterprise-architecture review

Check:

- correct abstraction level;
- separation of viewpoints;
- traceability;
- controlled catalogues;
- ownership;
- current, target and transition distinctions;
- no false equivalences;
- decision records.

## 24.3 BIAN review

Check:

- exact BIAN 14.0 names;
- official sources;
- mapping rationale;
- many-to-many relationships;
- version;
- scenario limits;
- BOM and Service Operation interpretation;
- no invented conformance.

## 24.4 Application and integration review

Check:

- application responsibilities;
- systems of record;
- interface semantics;
- failure handling;
- idempotency;
- compatibility;
- external dependencies;
- vendor and legacy constraints;
- support and ownership.

## 24.5 Data and accounting review

Check:

- entity definitions;
- identifiers;
- authority;
- lineage;
- quality;
- reconciliation;
- accounting flow;
- balance and value-date consistency;
- reporting impact;
- retention and privacy.

## 24.6 Risk, security and control review

Check:

- risk ownership;
- embedded controls;
- evidence;
- segregation of duties;
- identity;
- data protection;
- fraud and financial crime;
- operational resilience;
- third-party risk;
- auditability.

## 24.7 Technology and operations review

Check:

- deployment;
- availability;
- capacity;
- observability;
- recovery;
- batch and cut-off;
- incident handling;
- runbooks;
- service ownership;
- production support;
- degraded operation.

## 24.8 Pedagogical review

Check:

- beginner comprehension;
- term definitions;
- logical sequencing;
- useful examples;
- diagram readability;
- exercises;
- lack of unnecessary repetition;
- no generic filler.

## 24.9 Source and copyright review

Check:

- primary sources;
- versions and access dates;
- source notes;
- careful paraphrasing;
- no copied standards diagrams;
- no excessive quotation;
- clear separation between fact, interpretation and recommendation.

## 24.10 Naming and consistency review

Check:

- every reused name exists in a controlled catalogue;
- no near-duplicate capability or application names;
- glossary alignment;
- consistent spelling;
- consistent chapter links;
- consistent figure IDs;
- no obsolete old chapter references.

---

# 25. Acceptance criteria

Part V is not complete until all of the following are true.

## 25.1 Reader-outcome criteria

A reader can explain:

- how a full-service bank is organised;
- how it creates revenue and manages balance-sheet constraints;
- the major product families;
- the major end-to-end processes;
- the difference between customer, product, transaction, accounting and reporting lifecycles;
- how core banking, lending, collateral, payments, cards, trade, wealth, treasury and finance systems work together;
- how statements, communications, documents, workflow and cases fit;
- which data is authoritative;
- how information moves;
- how accounting and reconciliation work;
- where risks and controls operate;
- how security and resilience are designed;
- how BIAN informs architecture;
- why BIAN does not mechanically define microservices;
- how to move from current state to target state.

## 25.2 Coverage criteria

- every mandatory business domain appears in the coverage matrix;
- every Level 1 capability has definition, owner and relationships;
- every Level 1 process family has trigger and outcome;
- every major product family has a lifecycle;
- every major application family appears in the controlled landscape;
- every major data domain has an owner and authority model;
- every critical financial process has accounting and reconciliation consideration;
- every critical operation has a resilience dependency map;
- every external network has an owner and fallback consideration;
- every used BIAN name is verified against the recorded release;
- every chapter has declared scope and exclusions;
- every figure has a specification and register entry;
- no unexplained “other areas may include” statement is used to hide missing scope.

## 25.3 Quality criteria

- no chapter is generic filler;
- no major domain is represented only by a one-line catalogue entry;
- no scenario is happy-path only;
- no application landscape is limited to onboarding systems;
- no data chapter is limited to conceptual definitions;
- no technology chapter assumes cloud-native microservices everywhere;
- no security chapter is an afterthought;
- no finance or accounting flow is omitted from product architecture;
- no BIAN Service Domain is automatically mapped one-to-one;
- no invented regulatory obligation is presented as universal;
- no diagram is unreadable at publication size;
- no source or link check fails;
- no orphaned catalogue element remains unexplained.

---

# 26. Validation and checks

Run at least:

```text
python scripts/check-structure.py
python scripts/check-links.py
python scripts/check-terminology.py
python scripts/validate-diagrams.py
python scripts/check-diagram-register.py
python scripts/word-count.py
python scripts/build-book.py
```

Run any additional repository tests and GitHub Actions required by the branch.

Create validation for the master coverage matrix if one does not exist. It should detect:

- duplicate IDs;
- missing definitions;
- missing owners;
- unverified BIAN names;
- invalid chapter references;
- invalid figure references;
- applications absent from the controlled catalogue;
- data domains absent from the controlled catalogue;
- orphaned interfaces;
- capabilities with no process or application relationship;
- critical applications without resilience attributes;
- domain chapters with no accounting consideration;
- domain chapters with no exception path;
- source notes without source-register entries.

Do not suppress a check merely to make the build green. Correct the source or document the justified exception.

---

# 27. Commit and reporting discipline

Use logical commits by phase or coherent chapter group.

Suggested commit pattern:

```text
Redesign Part V structure and coverage model
Expand Horizon Bank business and application catalogues
Add enterprise data and integration catalogues
Rewrite Part V enterprise baseline chapters
Add customer, deposit and lending domain architecture
Add payments, cards and corporate banking domain architecture
Add wealth, treasury and finance domain architecture
Add risk, channels and shared services domain architecture
Complete BIAN implementation and migration chapters
Run full Part V coverage and quality audit
```

Do not push unless the author explicitly asks.

At the end of every task, report:

## Files changed

List each file.

## Work completed

State exactly which chapters, catalogues, diagrams or validations were completed.

## Banking coverage added

List domains, products, capabilities, processes and roles added.

## Application coverage added

List application families and important relationships added.

## Data and accounting coverage added

List domains, authorities, flows, accounting events and reconciliations added.

## BIAN work

List verified BIAN objects, version, mappings added, mappings rejected and unresolved questions.

## Sources added

List official sources and source notes.

## Diagrams

List specifications, sources, exports, validation and review status.

## Checks run

Give exact commands and results.

## Decisions recorded

List decision IDs and summaries.

## Remaining work and risks

Do not state “none” unless the coverage audit proves it.

---

# 28. Immediate first task for Codex

Do not begin by rewriting Chapter 31.

Perform the following first:

1. read all mandatory repository files;
2. inspect every current Part V chapter;
3. inspect all Horizon Bank controlled example files;
4. inspect all Part V figure specifications, sources and exports;
5. inspect source notes and registers;
6. create the current-state audit;
7. create the full-domain gap matrix;
8. propose the old-to-new chapter migration map;
9. expand the master Part V redesign plan;
10. update statuses to reflect that the section is under revision;
11. report findings before bulk drafting.

The first report must explicitly answer:

- Which existing sections are worth preserving?
- Which sections repeat the same caution?
- Which chapters are only stubs?
- Which banking domains are absent or shallow?
- Which applications are absent?
- Which data domains and systems-of-record decisions are absent?
- Which accounting and reconciliation flows are absent?
- Which controls and critical operations are absent?
- Which BIAN names need re-verification against 14.0?
- Which chapter links and figure IDs will change?
- What is the proposed migration sequence?
- What decisions require author approval before diagrams or structural renames proceed?

---

# 29. Final instruction

Do not optimise for preserving the current text.

Optimise for fulfilling the reader promise.

Part V must become an integrated architecture of a full-service bank, presented as a governed model set with readable enterprise landscapes and consistent domain drill-downs. It must connect business, applications, information, integration, accounting, controls, security, technology, operations and transformation.

BIAN is an important organising and semantic reference within that architecture. It is not the entire architecture.

The work is successful only when a reader can move from “How does a bank work?” to “How would I model, review and transform this bank?” without major gaps.
