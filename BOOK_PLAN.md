# Book Plan

## Working title

**Architecture Modelling: A Practical Beginner’s Handbook**

## Subtitle

**UML, C4, BPMN, ArchiMate, Data Models, BIAN and Essential Architecture Techniques**

## Author

Nishikant Tiwari

## Purpose

Create a practical reference that teaches readers how to select, read and create architecture models. The book starts with fundamental concepts, introduces the major modelling languages, groups diagrams by the problem they solve, applies them through the architecture lifecycle and then demonstrates a complete business-and-technology BIAN implementation for a fictional full-service bank.

## Primary readers

- Aspiring enterprise, solution and software architects
- Business analysts and process designers
- Developers moving into architecture
- Data, integration, security and infrastructure practitioners
- Banking professionals who need a structured introduction to BIAN

## Reader promise

By the end of the book, a reader should be able to:

1. Explain the difference between a model, view, viewpoint, notation and framework.
2. Choose an appropriate diagram based on the question, audience and abstraction level.
3. Read and review UML, C4, BPMN, ArchiMate and common data models.
4. Combine business, application, data, integration, security and deployment viewpoints.
5. Model architecture work across discovery, design, implementation, review and migration.
6. Apply BIAN to a bank without reducing it to an IT-only or microservices-only exercise.
7. Build a maintainable architecture repository with traceable decisions and sources.

## Pedagogical pattern

Every major modelling topic follows this sequence:

```text
Simple explanation
→ Formal terminology
→ Question answered
→ Core elements
→ Simple example
→ Banking example
→ Comparison
→ Common mistakes
→ Review checklist
→ Cheat sheet
```

## Case studies

### Simple Online Store

Used to introduce techniques without banking complexity.

### Horizon Bank 

A fictional full-service bank used to connect strategy, capabilities, business processes, BIAN Service Domains, information, applications, APIs, events, controls, deployment and migration.

## Scope guardrails

- Teach the most useful UML diagrams rather than reproduce the entire UML specification.
- Treat ArchiMate as an enterprise architecture language and TOGAF as a method/framework.
- Treat BPMN as a process notation, not a complete enterprise architecture language.
- Treat C4 as a software architecture communication model.
- Treat BIAN as a banking reference architecture and semantic standard, not a deployable product.
- Model all major banking process families at catalogue level and selected scenarios at detailed level.
- Use original explanatory diagrams rather than copied standards diagrams.

## Manuscript outline

## Part I: Understanding Architecture Modelling

- [1. What Is Architecture Modelling?](manuscript/part-01-fundamentals/01-what-is-architecture-modelling.md)
- [2. Model, View and Viewpoint](manuscript/part-01-fundamentals/02-model-view-viewpoint.md)
- [3. How to Read Architecture Diagrams](manuscript/part-01-fundamentals/03-reading-architecture-diagrams.md)

## Part II: Major Modelling Languages and Approaches

- [4. UML: Unified Modeling Language](manuscript/part-02-modelling-languages/04-uml.md)
- [5. The C4 Model](manuscript/part-02-modelling-languages/05-c4-model.md)
- [6. BPMN: Business Process Model and Notation](manuscript/part-02-modelling-languages/06-bpmn.md)
- [7. ArchiMate](manuscript/part-02-modelling-languages/07-archimate.md)
- [8. Data Modelling](manuscript/part-02-modelling-languages/08-data-modelling.md)
- [9. Decision Modelling and DMN](manuscript/part-02-modelling-languages/09-decision-modelling.md)
- [10. Domain and Event Modelling](manuscript/part-02-modelling-languages/10-domain-event-modelling.md)
- [11. Infrastructure and Deployment Modelling](manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md)
- [12. Security Modelling](manuscript/part-02-modelling-languages/12-security-modelling.md)
- [13. Other Useful Modelling Approaches](manuscript/part-02-modelling-languages/13-other-modelling-approaches.md)

## Part III: Choosing Diagrams by Architecture Need

- [14. Modelling Business Strategy and Capabilities](manuscript/part-03-diagram-selection/14-business-strategy-capabilities.md)
- [15. Modelling Business Processes](manuscript/part-03-diagram-selection/15-business-processes.md)
- [16. Modelling Software Structure](manuscript/part-03-diagram-selection/16-software-structure.md)
- [17. Modelling User and System Interaction](manuscript/part-03-diagram-selection/17-user-system-interaction.md)
- [18. Modelling Integration and Runtime Behaviour](manuscript/part-03-diagram-selection/18-integration-runtime-behaviour.md)
- [19. Modelling Data Architecture](manuscript/part-03-diagram-selection/19-data-architecture.md)
- [20. Modelling Infrastructure and Deployment](manuscript/part-03-diagram-selection/20-infrastructure-deployment.md)
- [21. Modelling Security Architecture](manuscript/part-03-diagram-selection/21-security-architecture.md)
- [22. Modelling Transformation and Migration](manuscript/part-03-diagram-selection/22-transformation-migration.md)
- [23. Modelling Decisions and Business Rules](manuscript/part-03-diagram-selection/23-decisions-business-rules.md)

## Part IV: Architecture Modelling Through the Lifecycle

- [24. Discovery and Problem Definition](manuscript/part-04-architecture-lifecycle/24-discovery-problem-definition.md)
- [25. Requirements and Analysis](manuscript/part-04-architecture-lifecycle/25-requirements-analysis.md)
- [26. Solution Design](manuscript/part-04-architecture-lifecycle/26-solution-design.md)
- [27. Detailed Design and Implementation](manuscript/part-04-architecture-lifecycle/27-detailed-design-implementation.md)
- [28. Architecture Review](manuscript/part-04-architecture-lifecycle/28-architecture-review.md)
- [29. Operations and Support](manuscript/part-04-architecture-lifecycle/29-operations-support.md)
- [30. Change and Migration](manuscript/part-04-architecture-lifecycle/30-change-migration.md)

## Part V: Practical BIAN Implementation for a Full-Service Bank

- [31. Introduction to BIAN](manuscript/part-05-bian-case-study/31-introduction-to-bian.md)
- [32. How BIAN Relates to Other Modelling Techniques](manuscript/part-05-bian-case-study/32-bian-and-modelling-techniques.md)
- [33. Defining the Full Banking Operating Model](manuscript/part-05-bian-case-study/33-full-banking-operating-model.md)
- [34. Complete Bank Business Process Architecture](manuscript/part-05-bian-case-study/34-bank-business-process-architecture.md)
- [35. Modelling Bank Value Streams with BIAN](manuscript/part-05-bian-case-study/35-bank-value-streams.md)
- [36. Creating BIAN-Aligned Business Scenarios](manuscript/part-05-bian-case-study/36-bian-business-scenarios.md)
- [37. Practical Scenario 1: Customer Onboarding](manuscript/part-05-bian-case-study/37-customer-onboarding-scenario.md)
- [38. Practical Scenario 2: Open a Current Account](manuscript/part-05-bian-case-study/38-current-account-opening-scenario.md)
- [39. Practical Scenario 3: Execute a Cross-Border Payment](manuscript/part-05-bian-case-study/39-cross-border-payment-scenario.md)
- [40. Practical Scenario 4: Consumer Loan Origination](manuscript/part-05-bian-case-study/40-consumer-loan-origination-scenario.md)
- [41. Practical Scenario 5: Card Fraud Investigation](manuscript/part-05-bian-case-study/41-card-fraud-investigation-scenario.md)
- [42. Practical Scenario 6: Corporate Cash Management](manuscript/part-05-bian-case-study/42-corporate-cash-management-scenario.md)
- [43. Mapping BIAN to Applications](manuscript/part-05-bian-case-study/43-mapping-bian-to-applications.md)
- [44. Designing BIAN-Aligned Software Services](manuscript/part-05-bian-case-study/44-bian-aligned-software-services.md)
- [45. Implementing BIAN Semantic APIs](manuscript/part-05-bian-case-study/45-bian-semantic-apis.md)
- [46. Implementing BIAN with Events](manuscript/part-05-bian-case-study/46-bian-events.md)
- [47. BIAN Information and Data Architecture](manuscript/part-05-bian-case-study/47-bian-data-architecture.md)
- [48. BIAN Security and Control Architecture](manuscript/part-05-bian-case-study/48-bian-security-control-architecture.md)
- [49. BIAN Deployment and Operational Architecture](manuscript/part-05-bian-case-study/49-bian-deployment-operations.md)
- [50. Migrating from Legacy Architecture to BIAN](manuscript/part-05-bian-case-study/50-legacy-to-bian-migration.md)
- [51. BIAN Adoption Roadmap](manuscript/part-05-bian-case-study/51-bian-adoption-roadmap.md)
- [52. BIAN Governance Model](manuscript/part-05-bian-case-study/52-bian-governance.md)
- [53. Measuring BIAN Implementation Success](manuscript/part-05-bian-case-study/53-bian-success-measures.md)
- [54. Common BIAN Implementation Mistakes](manuscript/part-05-bian-case-study/54-bian-common-mistakes.md)
- [55. BIAN Implementation Review Checklist](manuscript/part-05-bian-case-study/55-bian-review-checklist.md)
- [56. BIAN Quick Reference](manuscript/part-05-bian-case-study/56-bian-quick-reference.md)

## Part VI: Practical Architecture Reference Guide

- [57. How to Choose the Right Diagram](manuscript/part-06-practical-reference/57-choose-the-right-diagram.md)
- [58. Minimum Diagram Sets](manuscript/part-06-practical-reference/58-minimum-diagram-sets.md)
- [59. Diagram Quality Guidelines](manuscript/part-06-practical-reference/59-diagram-quality-guidelines.md)
- [60. Common Modelling Mistakes](manuscript/part-06-practical-reference/60-common-modelling-mistakes.md)
- [61. Modelling Tools and Diagrams as Code](manuscript/part-06-practical-reference/61-modelling-tools-diagrams-as-code.md)
- [62. Architecture Review Checklists](manuscript/part-06-practical-reference/62-architecture-review-checklists.md)
- [63. Building and Maintaining an Architecture Repository](manuscript/part-06-practical-reference/63-architecture-repository-practice.md)

## Appendices

- Appendix A: One-Page Diagram Selector
- Appendix B: UML Quick Reference
- Appendix C: BPMN Quick Reference
- Appendix D: ArchiMate Quick Reference
- Appendix E: C4 Quick Reference
- Appendix F: Data Modelling Quick Reference
- Appendix G: BIAN Quick Reference
- Appendix H: Glossary and Source Notes

## Detailed planning authority

`BOOK_PLAN.md` is the authoritative scope plan for the book. Chapter files may contain fuller drafting notes, but their section structure must not contradict this plan. Before a chapter moves from `Planned` to `Outlined`, the detailed subsection plan for that chapter must be synchronised here, in the chapter file and in the table of contents where applicable.

The previously discussed full subsection plan was referenced in project notes, but the replacement file is not present in this repository. Until that file is supplied or reconstructed through explicit review, this section records the current approved chapter-level scope and the minimum subsection coverage expected before drafting.

## Detailed chapter scope index

### Part I: Understanding Architecture Modelling

1. **What Is Architecture Modelling?** Explain why architecture needs models, what a model is, how models differ from diagrams, views, viewpoints, notations and frameworks, who uses architecture models, and why a diagram must answer a clear question.
2. **Model, View and Viewpoint.** Explain model, view, viewpoint, stakeholder concern, abstraction, notation and framework. Show how one model can support several views for different audiences.
3. **How to Read Architecture Diagrams.** Teach readers to inspect title, purpose, boundary, actors, systems, symbols, arrows, labels, legends, ownership, trust boundaries and review questions.

### Part II: Major Modelling Languages and Approaches

4. **UML: Unified Modeling Language.** Cover UML purpose, structural and behavioural diagram families, use case, class, component, sequence, activity, state machine and deployment diagrams, when UML helps, when it is too detailed, and common mistakes.
5. **The C4 Model.** Cover context, container, component and code levels, C4 people, software systems, containers and components, dynamic diagrams, deployment diagrams, system landscapes, C4 versus UML, and the container versus Docker distinction.
6. **BPMN: Business Process Model and Notation.** Cover BPMN purpose, events, activities, gateways, sequence flows, message flows, pools, lanes, collaboration diagrams, BPMN versus UML activity diagrams, and process-modelling mistakes.
7. **ArchiMate.** Cover ArchiMate purpose, relationship to TOGAF, strategy, business, application, technology, motivation and implementation elements, common relationships, useful viewpoints, ArchiMate versus C4, and appropriate abstraction.
8. **Data Modelling.** Cover conceptual, logical and physical data models, entity relationship diagrams, data flow diagrams, data lineage, data lifecycle, ownership, cardinality and ERD versus DFD.
9. **Decision Modelling and DMN.** Cover why decisions are modelled separately, decision tables, decision trees, Decision Model and Notation (DMN), decision requirements diagrams, DMN with BPMN, and separation of process from decision logic.
10. **Domain and Event Modelling.** Cover domain model, Domain-Driven Design concepts, bounded contexts, entities, value objects, aggregates, commands, events, event storming, context maps, event-driven architecture diagrams and event catalogues.
11. **Infrastructure and Deployment Modelling.** Cover infrastructure diagrams, network topology, cloud architecture, Kubernetes deployment, environments, resilience, availability, deployment diagrams and the difference between logical deployment and physical infrastructure.
12. **Security Modelling.** Cover trust boundaries, authentication flows, authorisation models, threat modelling, STRIDE, attack trees, security data-flow diagrams and control mapping.
13. **Other Useful Modelling Approaches.** Cover SysML, capability maps, value-stream maps, application landscapes, integration landscapes, roadmaps, heat maps, Wardley maps and Architecture Decision Records (ADRs).

### Part III: Choosing Diagrams by Architecture Need

14. **Modelling Business Strategy and Capabilities.** Cover capability maps, value streams, motivation models, strategy viewpoints, heat maps, investment questions and the distinction between capability and process.
15. **Modelling Business Processes.** Cover BPMN, activity diagrams, swimlanes, value-stream maps, responsibilities, handovers, decisions, parallel work, delays and process-level review questions.
16. **Modelling Software Structure.** Cover C4 container and component diagrams, UML component, package and class diagrams, dependencies, module responsibilities and abstraction-level consistency.
17. **Modelling User and System Interaction.** Cover use case diagrams, user journeys, BPMN, sequence diagrams, actors, goals, system boundaries, external systems and interaction review.
18. **Modelling Integration and Runtime Behaviour.** Cover sequence diagrams, C4 dynamic diagrams, message flows, event flows, data flows, interface catalogues, synchrony, failure paths, retries and event publication.
19. **Modelling Data Architecture.** Cover conceptual, logical and physical data views, ERDs, data flow, data lineage, ownership, data stores, movement, retention and data-quality implications.
20. **Modelling Infrastructure and Deployment.** Cover UML and C4 deployment diagrams, cloud views, network topology, Kubernetes, environment views, traffic routing, failover and operational clarity.
21. **Modelling Security Architecture.** Cover trust-boundary diagrams, authentication sequences, authorisation models, threat-model data-flow diagrams, attack trees and security-control maps.
22. **Modelling Transformation and Migration.** Cover current state, target state, transition architecture, ArchiMate plateau and gap, roadmaps, dependencies, sequencing and temporary states.
23. **Modelling Decisions and Business Rules.** Cover DMN, decision tables, decision trees, BPMN business-rule tasks, ADRs, decision inputs, outcomes and traceability.

### Part IV: Architecture Modelling Through the Lifecycle

24. **Discovery and Problem Definition.** Cover stakeholder maps, system context, capability maps, current-state views, business processes, problem statements and motivation models.
25. **Requirements and Analysis.** Cover use cases, BPMN processes, conceptual data models, context diagrams, quality attribute scenarios and domain models.
26. **Solution Design.** Cover C4 container diagrams, component diagrams, sequence diagrams, logical data models, integration diagrams, security architecture and deployment diagrams.
27. **Detailed Design and Implementation.** Cover class diagrams, physical data models, API sequences, state machines, Kubernetes deployment, interface specifications and event schemas.
28. **Architecture Review.** Cover review viewpoints for functionality, security, data, integration, performance, availability, operations and compliance, plus minimum review diagram sets.
29. **Operations and Support.** Cover runtime deployment, monitoring architecture, failure-flow diagrams, disaster recovery, support ownership, data lineage and incident sequences.
30. **Change and Migration.** Cover current versus target diagrams, transition states, dependency maps, roadmaps, deployment strategy and data migration flow.

### Part V: Practical BIAN Implementation for a Full-Service Bank

31. **Introduction to BIAN.** Explain BIAN as a banking reference architecture and semantic standard, not a product, and separate reference concepts from Horizon Bank implementation choices.
32. **How BIAN Relates to Other Modelling Techniques.** Map BIAN to capability, process, information, application, API, event and deployment views without reducing Service Domains to microservices.
33. **Defining the Full Banking Operating Model.** Establish Horizon Bank's operating model, major customer groups, channels, product families, operational capabilities and modelling boundaries.
34. **Complete Bank Business Process Architecture.** Catalogue strategy, market, product, party, onboarding, origination, deposits, lending, payments, cards, corporate banking, trade finance, wealth, treasury, fraud, compliance, risk, reporting, finance, operations, collections, channels, HR, procurement, legal, audit, support and technology process families.
35. **Modelling Bank Value Streams with BIAN.** Connect value streams to capabilities, Service Domains, customer outcomes, products, channels and process scenarios.
36. **Creating BIAN-Aligned Business Scenarios.** Explain business events, participating Service Domains, interaction paths, information exchanged, process complements and scenario review criteria.
37. **Practical Scenario 1: Customer Onboarding.** Model onboarding scope, actors, channels, KYC, AML, customer data, identity checks, exceptions, Service Domain interactions and controls.
38. **Practical Scenario 2: Open a Current Account.** Model account opening, eligibility, product selection, party verification, account fulfilment, data creation, notifications and operational handover.
39. **Practical Scenario 3: Execute a Cross-Border Payment.** Model payment initiation, validation, sanctions screening, pricing, routing, account posting, messaging, exceptions and reconciliation.
40. **Practical Scenario 4: Consumer Loan Origination.** Model application capture, affordability, credit decisioning, offer, documentation, fulfilment, disbursement and risk controls.
41. **Practical Scenario 5: Card Fraud Investigation.** Model alert intake, case triage, customer contact, transaction review, dispute handling, card controls, chargeback and closure.
42. **Practical Scenario 6: Corporate Cash Management.** Model corporate onboarding, account structures, liquidity services, payments, reporting, approvals, integration and service operations.
43. **Mapping BIAN to Applications.** Explain mapping from Service Domains and business capabilities to application components, packages, ownership and legacy constraints.
44. **Designing BIAN-Aligned Software Services.** Explain service boundaries, API responsibilities, events, transactions, consistency, ownership, security and why logical BIAN boundaries do not mandate physical microservices.
45. **Implementing BIAN Semantic APIs.** Cover semantic API purpose, resource and operation design, adaptation, governance, versioning, service contracts and consumer usability.
46. **Implementing BIAN with Events.** Cover business events, integration events, event schemas, producers, consumers, topics, ordering, idempotency, privacy and governance.
47. **BIAN Information and Data Architecture.** Cover Business Object Model usage, canonical information, logical data, ownership, lineage, data quality, reference data and physical implementation choices.
48. **BIAN Security and Control Architecture.** Cover trust boundaries, access control, customer data protection, financial crime controls, audit, segregation of duties and operational resilience.
49. **BIAN Deployment and Operational Architecture.** Cover deployment models, environments, monitoring, resilience, incident support, service ownership and operational runbooks.
50. **Migrating from Legacy Architecture to BIAN.** Cover current-state assessment, target decomposition, strangler patterns, coexistence, data migration, service transition and risk management.
51. **BIAN Adoption Roadmap.** Cover adoption phases, capability sequencing, pilot selection, governance setup, training, tooling and measurable outcomes.
52. **BIAN Governance Model.** Cover decision rights, reference model stewardship, semantic API governance, architecture review, change control and exception handling.
53. **Measuring BIAN Implementation Success.** Cover metrics for business outcomes, reuse, integration quality, delivery speed, consistency, risk reduction and operating health.
54. **Common BIAN Implementation Mistakes.** Cover microservice over-mapping, ignoring business ownership, weak semantics, excessive technical focus, incomplete governance and poor migration sequencing.
55. **BIAN Implementation Review Checklist.** Provide structured review questions for business, process, information, application, API, event, security, operational and migration views.
56. **BIAN Quick Reference.** Provide compact definitions, mapping guidance, scenario patterns, artefact list, common cautions and review prompts.

### Part VI: Practical Architecture Reference Guide

57. **How to Choose the Right Diagram.** Provide decision guidance by question, stakeholder, abstraction level, notation, lifecycle stage and common alternatives.
58. **Minimum Diagram Sets.** Define practical minimum sets for small applications, microservices solutions, enterprise transformation, business-process change and banking scenarios.
59. **Diagram Quality Guidelines.** Cover purpose, audience, boundary, labels, relationship direction, legend, abstraction level, colour, accessibility, assumptions and update discipline.
60. **Common Modelling Mistakes.** Cover showing everything, undocumented arrows, colour-only meaning, mixed abstraction, missing boundaries, unlabeled interfaces, weak ownership and over-complex notation.
61. **Modelling Tools and Diagrams as Code.** Cover PlantUML, Mermaid, Draw.io, Camunda Modeler, Structurizr, visual tools, diagrams as code, version control and rendering workflow.
62. **Architecture Review Checklists.** Provide checklists by viewpoint, lifecycle stage, stakeholder and diagram type.
63. **Building and Maintaining an Architecture Repository.** Cover folder structure, naming, source notes, diagram registers, decision logs, version control, quality checks and maintenance rhythm.

### Appendices

- **Appendix A: One-Page Diagram Selector.** A compact decision tree for selecting a diagram by reader question.
- **Appendix B: UML Quick Reference.** One-page summaries for the main UML diagrams used in the book.
- **Appendix C: BPMN Quick Reference.** Core BPMN elements, flows, pools, lanes, events, tasks and gateways.
- **Appendix D: ArchiMate Quick Reference.** Layers, common elements, relationships and viewpoints.
- **Appendix E: C4 Quick Reference.** Context, container, component, code, dynamic and deployment views.
- **Appendix F: Data Modelling Quick Reference.** Conceptual, logical and physical data modelling, cardinality and ERD versus DFD.
- **Appendix G: BIAN Quick Reference.** BIAN concepts, scenario pattern, mapping cautions and implementation prompts.
- **Appendix H: Glossary and Source Notes.** Final glossary and consolidated source-note guidance.

## Target size

- Main manuscript: approximately 110,000 to 150,000 words
- Diagrams: approximately 120 to 180 original figures
- Tables and checklists: approximately 80 to 120
- Each major chapter: 2,000 to 4,000 words depending on scope
- Detailed BIAN scenario chapter: 3,500 to 6,000 words

## Definition of completion

The book is complete when every chapter is approved, required figures are present, cross-references are valid, sources are traceable, terminology is consistent, the combined manuscript builds successfully and a final whole-book review has no unresolved critical findings.
