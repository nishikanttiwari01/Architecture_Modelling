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

- [31. BIAN Essentials and the Case-Study Method](manuscript/part-05-bian-case-study/31-introduction-to-bian.md)
- [32. How a Full-Service Bank Works](manuscript/part-05-bian-case-study/32-bian-and-modelling-techniques.md)
- [33. Enterprise Business Architecture of Horizon Bank](manuscript/part-05-bian-case-study/33-full-banking-operating-model.md)
- [34. Full Bank Application and Integration Landscape](manuscript/part-05-bian-case-study/34-bank-business-process-architecture.md)
- [35. Enterprise Information and Data Architecture](manuscript/part-05-bian-case-study/35-bank-value-streams.md)
- [36. Technology, Security, Resilience and Operating Architecture](manuscript/part-05-bian-case-study/36-bian-business-scenarios.md)
- [37. Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing](manuscript/part-05-bian-case-study/37-customer-onboarding-scenario.md)
- [38. Deposits, Accounts, Term Deposits, Interest, Fees, Statements and Correspondence](manuscript/part-05-bian-case-study/38-current-account-opening-scenario.md)
- [39. Lending and Credit: Consumer, Mortgage, SME and Corporate](manuscript/part-05-bian-case-study/39-cross-border-payment-scenario.md)
- [40. Collateral, Limits, Exposure, Collections, Recovery and the Credit-Risk Lifecycle](manuscript/part-05-bian-case-study/40-consumer-loan-origination-scenario.md)
- [41. Payments, Clearing, Settlement, Correspondent Banking and Foreign Exchange](manuscript/part-05-bian-case-study/41-card-fraud-investigation-scenario.md)
- [42. Cards and Merchant Acquiring](manuscript/part-05-bian-case-study/42-corporate-cash-management-scenario.md)
- [43. Corporate Banking, Cash Management and Trade Finance](manuscript/part-05-bian-case-study/43-mapping-bian-to-applications.md)
- [44. Wealth, Investments, Securities, Custody and Asset Servicing](manuscript/part-05-bian-case-study/44-bian-aligned-software-services.md)
- [45. Treasury, Markets, Funding, Liquidity, ALM and Capital](manuscript/part-05-bian-case-study/45-bian-semantic-apis.md)
- [46. Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting](manuscript/part-05-bian-case-study/46-bian-events.md)
- [47. Risk, Compliance, Financial Crime, Fraud, Audit and Legal](manuscript/part-05-bian-case-study/47-bian-data-architecture.md)
- [48. Channels, Communications, Documents, Workflow, Case Management and Shared Services](manuscript/part-05-bian-case-study/48-bian-security-control-architecture.md)
- [49. BIAN Mapping Method and Full-Stack Traceability](manuscript/part-05-bian-case-study/49-bian-deployment-operations.md)
- [50. BIAN-Aligned Application, Software-Service and Team Boundaries](manuscript/part-05-bian-case-study/50-legacy-to-bian-migration.md)
- [51. APIs, Events, Commands, Batch, Files, Workflow and External Networks](manuscript/part-05-bian-case-study/51-bian-adoption-roadmap.md)
- [52. Deployment, Security, Resilience, Observability and Operations](manuscript/part-05-bian-case-study/52-bian-governance.md)
- [53. Legacy Modernisation, Data Migration and Transition Architecture](manuscript/part-05-bian-case-study/53-bian-success-measures.md)
- [54. Governance, Ownership and the Architecture Repository](manuscript/part-05-bian-case-study/54-bian-common-mistakes.md)
- [55. Measures, Quality Gates and the Full-Bank Coverage Audit](manuscript/part-05-bian-case-study/55-bian-review-checklist.md)
- [56. Integrated End-to-End Scenarios and Practitioner Reference](manuscript/part-05-bian-case-study/56-bian-quick-reference.md)

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
- Appendix G: Integrated End-to-End Scenarios and Practitioner Reference
- Appendix H: Glossary and Source Notes

## Detailed planning authority

`BOOK_PLAN.md` is the authoritative scope plan for the book. Chapter files may contain fuller drafting notes, but their section structure must not contradict this plan. Before a chapter moves from `Planned` to `Outlined`, the detailed subsection plan for that chapter must be synchronised here, in the chapter file and in the table of contents where applicable.

The subsection structure below records the approved 63-chapter plan currently represented by the manuscript files. It replaces the compressed scope index and must be maintained whenever a chapter outline changes.

## Detailed 63-chapter subsection structure

### Part I: Understanding Architecture Modelling

#### 1. What Is Architecture Modelling?

- Manuscript file: `manuscript/part-01-fundamentals/01-what-is-architecture-modelling.md`
- Scope: Explain why architecture needs models, what a model is, how models differ from diagrams, views, viewpoints, notations and frameworks, who uses architecture models, and why a diagram must answer a clear question.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Why architecture needs models
  - Architecture, model, diagram, view, viewpoint, notation and framework
  - A model is a deliberate simplification
  - Stakeholders and their information needs
  - Structural and behavioural models
  - Conceptual, logical and physical levels
  - Current, transition and target states
  - How to choose the first model
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 2. Model, View and Viewpoint

- Manuscript file: `manuscript/part-01-fundamentals/02-model-view-viewpoint.md`
- Scope: Explain model, view, viewpoint, stakeholder concern, abstraction, notation and framework. Show how one model can support several views for different audiences.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Why these terms are often confused
  - What is a model?
  - What is a view?
  - What is a viewpoint?
  - Practical viewpoint specification template
  - Expert note: ISO 42010 terminology
  - Stakeholders, concerns and viewpoints
  - Abstraction and decomposition
  - Consistency between views
  - Viewpoint catalogue
  - Worked mapping exercise
  - Chapter summary and knowledge check
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 3. How to Read Architecture Diagrams

- Manuscript file: `manuscript/part-01-fundamentals/03-reading-architecture-diagrams.md`
- Scope: Teach readers to inspect title, purpose, boundary, actors, systems, symbols, arrows, labels, legends, ownership, trust boundaries and review questions.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Start with title, purpose and audience
  - Find the scope and boundary
  - Identify actors, systems and responsibilities
  - Read relationships and direction
  - Understand legends and notation
  - Distinguish logical and physical elements
  - Look for trust and ownership boundaries
  - Check omissions and assumptions
  - Review questions
  - Worked banking review
  - Guided practice: Online Store
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

### Part II: Major Modelling Languages and Approaches

#### 4. UML: Unified Modeling Language

- Manuscript file: `manuscript/part-02-modelling-languages/04-uml.md`
- Scope: Cover UML purpose, structural and behavioural diagram families, use case, class, component, sequence, activity, state machine and deployment diagrams, when UML helps, when it is too detailed, and common mistakes.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - What UML is and is not
  - Structural, behavioural and interaction diagrams
  - Use case diagrams
  - Class diagrams
  - Component diagrams
  - Sequence diagrams
  - Activity diagrams
  - State machine diagrams
  - Deployment diagrams
  - Less commonly used UML diagrams
  - UML diagram selection guide
  - UML versus other approaches
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 5. The C4 Model

- Manuscript file: `manuscript/part-02-modelling-languages/05-c4-model.md`
- Scope: Cover context, container, component and code levels, C4 people, software systems, containers and components, dynamic diagrams, deployment diagrams, system landscapes, C4 versus UML, and the container versus Docker distinction.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - What C4 is
  - Core concepts: person, system, container and component
  - Level 1: System Context
  - Level 2: Container
  - Level 3: Component
  - Level 4: Code
  - Horizon Bank payments platform example
  - Dynamic diagrams
  - Deployment diagrams
  - System landscape diagrams
  - C4 versus UML
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 6. BPMN: Business Process Model and Notation

- Manuscript file: `manuscript/part-02-modelling-languages/06-bpmn.md`
- Scope: Cover BPMN purpose, events, activities, gateways, sequence flows, message flows, pools, lanes, collaboration diagrams, BPMN versus UML activity diagrams, and process-modelling mistakes.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - What BPMN is and is not
  - Events
  - Activities and task types
  - Gateways
  - Sequence flows and message flows
  - Pools and lanes
  - Data objects and annotations
  - Subprocesses
  - Exceptions, timers and escalations
  - BPMN collaboration diagrams
  - BPMN versus UML Activity
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 7. ArchiMate

- Manuscript file: `manuscript/part-02-modelling-languages/07-archimate.md`
- Scope: Cover ArchiMate purpose, relationship to TOGAF, strategy, business, application, technology, motivation and implementation elements, common relationships, useful viewpoints, ArchiMate versus C4, and appropriate abstraction.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - What ArchiMate is
  - ArchiMate and TOGAF
  - Strategy layer
  - Business layer
  - Application layer
  - Technology layer
  - Physical layer
  - Motivation elements
  - Implementation and migration elements
  - Core relationships
  - Common viewpoints
  - ArchiMate versus C4
  - ArchiMate versus BPMN
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 8. Data Modelling

- Manuscript file: `manuscript/part-02-modelling-languages/08-data-modelling.md`
- Scope: Cover conceptual, logical and physical data models, entity relationship diagrams, data flow diagrams, data lineage, data lifecycle, ownership, cardinality and ERD versus DFD.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Why data needs separate models
  - Conceptual data model
  - Logical data model
  - Physical data model
  - Entities, attributes and keys
  - Relationships, cardinality and optionality
  - Data Flow Diagrams
  - Data lineage
  - Data lifecycle
  - Canonical and local models
  - ERD versus DFD
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 9. Decision Modelling and DMN

- Manuscript file: `manuscript/part-02-modelling-languages/09-decision-modelling.md`
- Scope: Cover why decisions are modelled separately, decision tables, decision trees, Decision Model and Notation (DMN), decision requirements diagrams, DMN with BPMN, and separation of process from decision logic.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Why model decisions separately
  - Decision tables
  - Decision trees
  - Introduction to DMN
  - Decision Requirements Diagrams
  - Inputs, decisions and knowledge models
  - Hit policies
  - DMN with BPMN
  - Decision governance
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 10. Domain and Event Modelling

- Manuscript file: `manuscript/part-02-modelling-languages/10-domain-event-modelling.md`
- Scope: Cover domain model, strategic and tactical Domain-Driven Design concepts, bounded contexts, subdomain types, entities, value objects, aggregates, aggregate roots, repositories, domain services, commands, events, EventStorming, context maps, event-driven architecture diagrams, runtime event concerns, Event Sourcing, CQRS, modelling tools and event catalogues.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Why domain and event modelling matter
  - Domain models
  - Domain-Driven Design vocabulary
  - Strategic DDD: subdomains, language and boundaries
  - Context maps
  - Tactical DDD: aggregates, entities and value objects
  - Domain events
  - EventStorming
  - Commands, events, policies and read models
  - Event-driven architecture diagrams
  - Runtime guidance for event-driven systems
  - Event-driven architecture, Event Sourcing and CQRS
  - Event catalogues
  - How to create domain and event models in practice
  - How domain and event modelling compare with nearby techniques
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 11. Infrastructure and Deployment Modelling

- Manuscript file: `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`
- Scope: Cover infrastructure diagrams, network topology, cloud architecture, Kubernetes deployment, environments, resilience, availability, deployment diagrams and the difference between logical deployment and physical infrastructure.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Infrastructure versus deployment views
  - UML and C4 deployment diagrams
  - Network topology
  - Cloud architecture
  - Kubernetes deployment
  - Environment views
  - Availability and resilience
  - Disaster recovery
  - Observability architecture
  - Deployment versus infrastructure diagrams
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 12. Security Modelling

- Manuscript file: `manuscript/part-02-modelling-languages/12-security-modelling.md`
- Scope: Cover security viewpoints, security modelling foundations, trust boundaries, authentication flows, access authorisation models, threat modelling, STRIDE, attack trees, threat-model data-flow diagrams, security control mapping, privacy modelling and data classification.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Why security needs its own models
  - The security modelling foundation
  - Depth boundary for this chapter
  - Security viewpoints
  - Trust-boundary diagrams
  - Authentication flows
  - Access authorisation models
  - Threat modelling
  - STRIDE
  - Attack trees
  - Threat-model Data Flow Diagrams
  - Security control mapping
  - Privacy modelling and data classification
  - Security modelling versus nearby approaches
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 13. Other Useful Modelling Approaches

- Manuscript file: `manuscript/part-02-modelling-languages/13-other-modelling-approaches.md`
- Scope: Cover SysML, capability maps, value-stream maps, application landscapes, integration landscapes, roadmaps, heat maps, Wardley maps and Architecture Decision Records (ADRs).
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - SysML
  - Capability maps
  - Value streams
  - Application landscapes
  - Integration landscapes
  - Architecture roadmaps
  - Heat maps
  - Wardley maps
  - Architecture Decision Records
  - When to use specialised approaches
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

### Part III: Choosing Diagrams by Architecture Need

#### 14. Modelling Business Strategy and Capabilities

- Manuscript file: `manuscript/part-03-diagram-selection/14-business-strategy-capabilities.md`
- Scope: Cover capability maps, value streams, motivation models, strategy viewpoints, heat maps, investment questions and the distinction between capability and process.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Goals, drivers and outcomes
  - Stakeholder concerns
  - Capability maps
  - Value streams
  - Heat maps
  - Traceability to initiatives
  - Recommended notation combinations
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 15. Modelling Business Processes

- Manuscript file: `manuscript/part-03-diagram-selection/15-business-processes.md`
- Scope: Cover BPMN, activity diagrams, swimlanes, value-stream maps, responsibilities, handovers, decisions, parallel work, delays and process-level review questions.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Process architecture
  - Process levels
  - BPMN selection
  - Swimlanes and responsibilities
  - Exceptions and controls
  - Process metrics
  - Process-to-capability traceability
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 16. Modelling Software Structure

- Manuscript file: `manuscript/part-03-diagram-selection/16-software-structure.md`
- Scope: Cover C4 container and component diagrams, UML component, package and class diagrams, dependencies, module responsibilities and abstraction-level consistency.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - System landscape
  - Context view
  - Container view
  - Component view
  - Package and class views
  - Dependency management
  - Logical versus physical structure
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 17. Modelling User and System Interaction

- Manuscript file: `manuscript/part-03-diagram-selection/17-user-system-interaction.md`
- Scope: Cover use case diagrams, user journeys, BPMN, sequence diagrams, actors, goals, system boundaries, external systems and interaction review.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Actors and personas
  - Use cases
  - Customer journeys
  - Interaction flows
  - Sequence diagrams
  - Accessibility and channel concerns
  - Traceability to requirements
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 18. Modelling Integration and Runtime Behaviour

- Manuscript file: `manuscript/part-03-diagram-selection/18-integration-runtime-behaviour.md`
- Scope: Cover sequence diagrams, C4 dynamic diagrams, message flows, event flows, data flows, interface catalogues, synchrony, failure paths, retries and event publication.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Integration context
  - API interactions
  - Message flows
  - Sequence diagrams
  - C4 dynamic diagrams
  - Events and queues
  - Error and retry behaviour
  - Interface catalogue
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 19. Modelling Data Architecture

- Manuscript file: `manuscript/part-03-diagram-selection/19-data-architecture.md`
- Scope: Cover conceptual, logical and physical data views, ERDs, data flow, data lineage, ownership, data stores, movement, retention and data-quality implications.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Conceptual information architecture
  - Logical and physical models
  - Data flows
  - Lineage
  - Ownership and stewardship
  - Master and reference data
  - Privacy and retention
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 20. Modelling Infrastructure and Deployment

- Manuscript file: `manuscript/part-03-diagram-selection/20-infrastructure-deployment.md`
- Scope: Cover UML and C4 deployment diagrams, cloud views, network topology, Kubernetes, environment views, traffic routing, failover and operational clarity.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Runtime nodes
  - Network zones
  - Cloud services
  - Kubernetes
  - Environment differences
  - Availability
  - Recovery
  - Operational ownership
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 21. Modelling Security Architecture

- Manuscript file: `manuscript/part-03-diagram-selection/21-security-architecture.md`
- Scope: Cover trust-boundary diagrams, authentication sequences, authorisation models, threat-model data-flow diagrams, attack trees and security-control maps.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Security context
  - Trust boundaries
  - Authentication
  - Authorisation
  - Threats
  - Control mapping
  - Audit and monitoring
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 22. Modelling Transformation and Migration

- Manuscript file: `manuscript/part-03-diagram-selection/22-transformation-migration.md`
- Scope: Cover current state, target state, transition architecture, ArchiMate plateau and gap, roadmaps, dependencies, sequencing and temporary states.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - As-is baseline
  - Target architecture
  - Gap analysis
  - Transition states
  - Roadmaps
  - Dependencies
  - Benefits and measures
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 23. Modelling Decisions and Business Rules

- Manuscript file: `manuscript/part-03-diagram-selection/23-decisions-business-rules.md`
- Scope: Cover DMN, decision tables, decision trees, BPMN business-rule tasks, ADRs, decision inputs, outcomes and traceability.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Operational decisions
  - Business rules
  - DMN
  - Architecture decisions
  - Trade-off matrices
  - Governance
  - Traceability
  - Selection table
  - Worked example
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

### Part IV: Architecture Modelling Through the Lifecycle

#### 24. Discovery and Problem Definition

- Manuscript file: `manuscript/part-04-architecture-lifecycle/24-discovery-problem-definition.md`
- Scope: Cover stakeholder maps, system context, capability maps, current-state views, business processes, problem statements and motivation models.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Problem framing
  - Stakeholder map
  - Current-state context
  - Capability assessment
  - Business process discovery
  - Constraints and assumptions
  - Discovery deliverables
  - Recommended model set
  - Worked example
  - Stage-gate checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 25. Requirements and Analysis

- Manuscript file: `manuscript/part-04-architecture-lifecycle/25-requirements-analysis.md`
- Scope: Cover use cases, BPMN processes, conceptual data models, context diagrams, quality attribute scenarios and domain models.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Business requirements
  - Use cases
  - Process requirements
  - Data requirements
  - Quality attributes
  - Traceability
  - Analysis deliverables
  - Recommended model set
  - Worked example
  - Stage-gate checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 26. Solution Design

- Manuscript file: `manuscript/part-04-architecture-lifecycle/26-solution-design.md`
- Scope: Cover C4 container diagrams, component diagrams, sequence diagrams, logical data models, integration diagrams, security architecture and deployment diagrams.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Design principles
  - Context and container views
  - Process and interaction views
  - Data architecture
  - Security architecture
  - Deployment architecture
  - Design deliverables
  - Recommended model set
  - Worked example
  - Stage-gate checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 27. Detailed Design and Implementation

- Manuscript file: `manuscript/part-04-architecture-lifecycle/27-detailed-design-implementation.md`
- Scope: Cover class diagrams, physical data models, API sequences, state machines, Kubernetes deployment, interface specifications and event schemas.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Component design
  - Class and package design
  - API specifications
  - Event schemas
  - Physical data models
  - Deployment manifests
  - Implementation traceability
  - Recommended model set
  - Worked example
  - Stage-gate checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 28. Architecture Review

- Manuscript file: `manuscript/part-04-architecture-lifecycle/28-architecture-review.md`
- Scope: Cover review viewpoints for functionality, security, data, integration, performance, availability, operations and compliance, plus minimum review diagram sets.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Review preparation
  - Functional review
  - Security review
  - Data review
  - Integration review
  - Performance and resilience
  - Operability
  - Decision and action tracking
  - Recommended model set
  - Worked example
  - Stage-gate checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 29. Operations and Support

- Manuscript file: `manuscript/part-04-architecture-lifecycle/29-operations-support.md`
- Scope: Cover runtime deployment, monitoring architecture, failure-flow diagrams, disaster recovery, support ownership, data lineage and incident sequences.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Operational context
  - Monitoring and observability
  - Incident flows
  - Problem management
  - Runbooks
  - Continuity and recovery
  - Operational metrics
  - Recommended model set
  - Worked example
  - Stage-gate checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 30. Change and Migration

- Manuscript file: `manuscript/part-04-architecture-lifecycle/30-change-migration.md`
- Scope: Cover current versus target diagrams, transition states, dependency maps, roadmaps, deployment strategy and data migration flow.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Change drivers
  - Transition architectures
  - Migration waves
  - Data migration
  - Parallel operation
  - Cutover
  - Decommissioning
  - Benefits realisation
  - Recommended model set
  - Worked example
  - Stage-gate checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

### Part V: Practical BIAN Implementation for a Full-Service Bank

#### 31. BIAN Essentials and the Case-Study Method

- Manuscript file: `manuscript/part-05-bian-case-study/31-introduction-to-bian.md`
- Scope: Introduce the Banking Industry Architecture Network (BIAN) concepts needed in Part V and explain how Horizon Bank will combine them with business, application, data and technology models.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - The problem is shared meaning, not a shortage of diagrams
  - What BIAN is
  - The core concepts and the questions they answer
  - A Service Domain is a logical responsibility
  - Business Scenarios show collaboration, not the complete process
  - Service Operations, semantic APIs and events
  - Control Records and bank-owned information
  - BIAN works with other modelling techniques
  - The governed Horizon Bank case-study baseline
  - The Part V method
  - Worked traceability: payment initiation
  - Evidence, status and confidence
  - When to use BIAN
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 32. How a Full-Service Bank Works

- Manuscript file: `manuscript/part-05-bian-case-study/32-bian-and-modelling-techniques.md`
- Scope: Give readers the commercial and operational foundation needed to understand the architecture of Horizon Bank.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Start with obligations, not applications
  - The governed scope of Horizon Bank
  - Customer segments are service contexts
  - Business lines, products and legal entities answer different questions
  - How a bank earns, spends and absorbs loss
  - Front, middle and back office are responsibility patterns
  - Connected lifecycles explain the bank
  - Dates and the banking day
  - Worked example: deposit interest posting
  - Why a full bank needs many application responsibilities
  - Group, country, shared service and supplier boundaries
  - Critical operations join the layers
  - Models to use, and models not to use
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 33. Enterprise Business Architecture of Horizon Bank

- Manuscript file: `manuscript/part-05-bian-case-study/33-full-banking-operating-model.md`
- Scope: Establish the governed business architecture baseline that later domain chapters will refine. The Banking Industry Architecture Network (BIAN) provides the industry reference used for qualified mappings in this chapter.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Enterprise business architecture is a connected model
  - Keep the business concepts separate
  - Stakeholder outcomes provide direction
  - The value-stream portfolio
  - Navigate the bank through business domains
  - Capabilities describe abilities
  - Processes describe ordered work
  - Products connect commercial promise to fulfilment
  - Organisation records accountability and performance
  - Candidate BIAN mappings remain qualified references
  - Worked thread 1: establish and manage a customer relationship
  - Worked thread 2: execute and settle a transaction
  - Heat maps, measures and evidence
  - When to use each business view
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 34. Full Bank Application and Integration Landscape

- Manuscript file: `manuscript/part-05-bian-case-study/34-bank-business-process-architecture.md`
- Scope: Present the complete governed application taxonomy for Horizon Bank and explain how enterprise and domain views connect. The landscape is a logical model of responsibilities and exchanges, not a vendor inventory or deployment diagram.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - What an application landscape answers
  - The complete logical application estate
  - Classify application roles precisely
  - Integration is a portfolio of contracts
  - External connectivity is inside the architecture boundary
  - Worked trace: establish a customer relationship
  - Worked trace: execute a cross-border payment
  - Current, target and transition views
  - Security and trust across the landscape
  - Criticality and operational ownership
  - BIAN alignment without false equivalence
  - Rationalisation uses evidence
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 35. Enterprise Information and Data Architecture

- Manuscript file: `manuscript/part-05-bian-case-study/35-bank-value-streams.md`
- Scope: Establish Horizon Bank's bank-wide information concepts, authority decisions and data movement before the domain chapters add detail. The chapter connects operational facts to accounting, reconciliation, risk, analytics and reporting without treating one data platform as authoritative for everything.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Data architecture is an accountability model
  - The 20 governed data domains
  - Information categories can overlap
  - Authority must be qualified
  - Identifiers, time and provenance
  - Data ownership and stewardship
  - Quality, metadata and lineage services
  - Accounting events are part of information architecture
  - Reconciliation is a controlled comparison
  - Worked lineage: deposit interest
  - Worked lineage: cross-border payment
  - Protection, retention and permitted use
  - BIAN information concepts and local models
  - Current, transition and target considerations
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 36. Technology, Security, Resilience and Operating Architecture

- Manuscript file: `manuscript/part-05-bian-case-study/36-bian-business-scenarios.md`
- Scope: Explain how Horizon Bank's application and information estate runs securely, reliably and accountably across hybrid technology and third-party services. The chapter starts with critical operations and traces the technology, identity, control, observability, recovery and operating responsibilities needed to sustain them.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Start with the operation, not the platform
  - Keep four architecture levels separate
  - The 30 technology and resilience classifications
  - The 20 critical operations
  - Placement follows evidence
  - Trust boundaries and identity
  - Security is a system of controls
  - Secure delivery and change
  - Observability connects telemetry to action
  - Availability, recovery and impact tolerance differ
  - Worked dependency map: a time-critical payment
  - Worked recovery: payment service after cyber disruption
  - Batch, close and business-day operation
  - Third parties, concentration and exit
  - Service operations and ownership
  - BIAN and runtime architecture
  - Current, transition and target considerations
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 37. Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing

- Manuscript file: `manuscript/part-05-bian-case-study/37-customer-onboarding-scenario.md`
- Scope: Explain how a full-service bank establishes and maintains a governed relationship with a person or organisation. The chapter connects customer journeys to party identity, customer relationship management (CRM), sales, onboarding, Know Your Customer (KYC), customer due diligence, servicing, information authority, applications, controls and operations.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Start with the relationship, not the form
  - Business objective and customer journey
  - CRM, sales and relationship planning
  - Customer due diligence and KYC
  - Model the process and decisions separately
  - Application responsibilities
  - Interaction path and interface catalogue
  - Information authority and lifecycle
  - Security, privacy and control
  - Customer servicing and ongoing review
  - Resilience and operating ownership
  - BIAN candidate mapping
  - Current, transition and target considerations
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 38. Deposits, Accounts, Term Deposits, Interest, Fees, Statements and Correspondence

- Manuscript file: `manuscript/part-05-bian-case-study/38-current-account-opening-scenario.md`
- Scope: Explain the complete non-credit deposit and account lifecycle, from product selection and agreement creation through funding, balance servicing, interest, fees, statements, maturity and closure. The chapter shows how a bank keeps the customer agreement, operational account record and financial books consistent.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - A deposit is both a customer service and a bank obligation
  - Product, agreement and account
  - Account opening process
  - Eligibility is a governed decision
  - Account lifecycle and state
  - Application architecture
  - Interfaces and event behaviour
  - Data model and authority
  - Interest, fees and correspondence
  - Accounting events and reconciliation
  - Controls and operational handling
  - Resilience and critical operations
  - BIAN candidate mapping
  - Current, transition and target considerations
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 39. Lending and Credit: Consumer, Mortgage, SME and Corporate

- Manuscript file: `manuscript/part-05-bian-case-study/39-cross-border-payment-scenario.md`
- Scope: Explain the lending domain from financing need through application, assessment, decision, contracting, disbursement and servicing. The chapter compares consumer, mortgage, small and medium-sized enterprise (SME), and corporate credit while preserving one governed credit lifecycle.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Lending is a lifecycle, not a decision API
  - Core credit concepts
  - What is common and what differs
  - Customer journey and origination process
  - Credit decisioning and explainability
  - External credit information
  - Origination and servicing applications
  - Information model and authority
  - Loan state and servicing
  - Accounting events and financial control
  - Controls through fulfilment
  - Resilience and operation
  - BIAN candidate mapping
  - Current, transition and target considerations
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 40. Collateral, Limits, Exposure, Collections, Recovery and the Credit-Risk Lifecycle

- Manuscript file: `manuscript/part-05-bian-case-study/40-consumer-loan-origination-scenario.md`
- Scope: Complete the credit architecture begun in Chapter 39. This chapter follows approved credit through limit use, collateral, exposure monitoring, delinquency, collections, restructuring, recovery, impairment-related events, write-off and closure.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - The credit lifecycle continues after disbursement
  - Separate the key concepts
  - Limits and utilisation
  - Collateral is not merely a value field
  - Exposure aggregation
  - Monitoring and early action
  - Collections, restructuring and recovery
  - Applications and ownership boundaries
  - Data authority and history
  - Accounting events and expected credit loss
  - Control, challenge and segregation
  - Resilience across distressed credit
  - BIAN candidate mapping
  - Current, transition and target considerations
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 41. Payments, Clearing, Settlement, Correspondent Banking and Foreign Exchange

- Manuscript file: `manuscript/part-05-bian-case-study/41-card-fraud-investigation-scenario.md`
- Scope: A payment is not complete merely because a customer has pressed **Send**. The bank must accept an instruction, establish authority, control financial-crime risk, route the instruction, exchange it with other institutions, settle the resulting obligation, post the financial outcome and resolve exceptions. This chapter shows how to model those responsibilities without hiding them inside one box called `Payments`. The central architecture question is: **which business and application responsibility owns each state of a payment, and what evidence proves that money and status remain consistent?** Horizon Bank is fictional. Its catalogue is an author model, not a statement about a particular country's payment schemes or settlement law.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - What is the payment domain?
  - Initiation, clearing and settlement are different
  - Operating model and end-to-end process
  - Application responsibilities and interactions
  - Domestic rails and external networks
  - Correspondent banking is a relationship and an account service
  - Foreign exchange linked to a payment
  - Information authority, accounting and reconciliation
  - Controls, security and operational resilience
  - BIAN alignment and model choices
  - Worked traceability: a cross-border payment with FX
  - Current-to-target considerations
  - When should this model set be used?
  - Common mistakes
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 42. Cards and Merchant Acquiring

- Manuscript file: `manuscript/part-05-bian-case-study/42-corporate-cash-management-scenario.md`
- Scope: A card purchase joins two customer relationships. An issuer serves the cardholder, while an acquirer serves the merchant. Between them, processing and network responsibilities carry authorisation, clearing, settlement and dispute information. This chapter shows how to model those responsibilities without treating `Cards` as one product or one application. The central architecture question is: **who owns the cardholder, merchant, transaction and financial states from credential issuance to final settlement and dispute resolution?** The Horizon Bank catalogue is a fictional author model. Card-network participation, licences, rules and deadlines remain unverified.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - What is the card and acquiring domain?
  - Issuing and credential lifecycle
  - Authorisation is a decision, not settlement
  - Processing, presentment, clearing and settlement
  - Billing, statements and revolving credit
  - Fraud, customer claims and disputes
  - Merchant acquiring is a separate lifecycle
  - Information and security boundaries
  - Controls and resilience
  - BIAN alignment and model selection
  - Worked traceability: purchase and later dispute
  - Current-to-target considerations
  - When should this model set be used?
  - Common mistakes
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 43. Corporate Banking, Cash Management and Trade Finance

- Manuscript file: `manuscript/part-05-bian-case-study/43-mapping-bian-to-applications.md`
- Scope: Corporate banking is not retail banking with larger balances. A corporate customer can contain many legal entities, accounts, authorised users, approval mandates, cash structures and cross-border obligations. Trade finance adds instruments, documents, contingent exposure and claims. This chapter explains how those responsibilities connect without treating trade finance as deposit acquisition. The central architecture question is: **how does the bank preserve corporate authority, liquidity visibility and trade obligations across organisations, applications and external parties?** Horizon Bank is fictional. Its cash structures and trade lifecycle are an author model, not legal, tax or documentary-credit advice.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - What is the corporate banking domain?
  - Corporate relationship and mandate model
  - Cash management and liquidity services
  - Operating a corporate cash structure
  - Trade finance is a complete instrument lifecycle
  - Trade-finance applications and external interaction
  - Exposure, accounting and reconciliation
  - Controls, resilience and exception ownership
  - BIAN alignment
  - Choosing the right models
  - Worked traceability: issue and settle a trade instrument
  - Current-to-target considerations
  - When should this model set be used?
  - Common mistakes
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 44. Wealth, Investments, Securities, Custody and Asset Servicing

- Manuscript file: `manuscript/part-05-bian-case-study/44-bian-aligned-software-services.md`
- Scope: An investment journey does not end when an order is executed. The bank must preserve the client mandate, suitability evidence, order and allocation, settlement obligation, custody holding, income and corporate-action outcome. This chapter separates those responsibilities so that a portfolio view cannot be mistaken for the authoritative securities position. The central architecture question is: **which responsibility owns each client, order, position and entitlement state from advice through safekeeping and asset servicing?** Horizon Bank is fictional. Jurisdictional advice duties, client-asset rules, market memberships and custody chains remain explicit assumptions.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Two related domains, not one application
  - Advice, suitability and portfolio responsibility
  - Order capture, execution and allocation
  - Securities processing and settlement
  - Custody and safekeeping
  - Corporate actions and asset servicing
  - Information authority and lineage
  - Controls and operational resilience
  - BIAN alignment and software boundaries
  - Choosing the right models
  - Worked traceability: advice through settlement
  - Worked traceability: corporate action
  - Current-to-target considerations
  - When should this model set be used?
  - Common mistakes
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading
  - Drafting notes

#### 45. Treasury, Markets, Funding, Liquidity, ALM and Capital

- Manuscript file: `manuscript/part-05-bian-case-study/45-bian-semantic-apis.md`
- Scope: Show how to model the part of a full-service bank that manages funding, liquidity, market positions, balance-sheet structure and capital. The chapter separates business decisions from transaction execution, independent risk oversight, accounting and settlement, then traces those responsibilities through Horizon Bank's governed catalogues.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this architecture answers
  - Scope and responsibility boundaries
  - Model the four connected lifecycles
  - Applications and authoritative information
  - Interfaces, accounting and reconciliation
  - Controls, risk and resilience
  - Worked trace: liquidity shortfall
  - BIAN alignment without invented precision
  - Current-to-target considerations
  - When to use each model
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 46. Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting

- Manuscript file: `manuscript/part-05-bian-case-study/46-bian-events.md`
- Scope: Explain how a full-service bank turns product and transaction activity into controlled accounting records, reconciled books, tax positions and approved reports. The chapter makes the boundaries between business events, accounting events, subledgers, the General Ledger and reporting datasets explicit.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this architecture answers
  - Governed responsibility model
  - Follow the accounting chain
  - Tax is more than a filing interface
  - Management and external reporting
  - Data architecture and lineage
  - Commands, events, files and batch
  - Worked trace: close the books and submit a return
  - Controls and resilience
  - Current-to-target considerations
  - Choose the model that matches the finance question
  - BIAN alignment and limits
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 47. Risk, Compliance, Financial Crime, Fraud, Audit and Legal

- Manuscript file: `manuscript/part-05-bian-case-study/47-bian-data-architecture.md`
- Scope: Show how to model oversight, control, investigation, assurance and legal responsibilities without collapsing them into one `risk system`. The chapter separates enterprise risk, compliance, financial crime, fraud, internal audit and legal work and traces their different authorities through Horizon Bank.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this architecture answers
  - Three governed domain families
  - Responsibility comparison
  - Application boundaries
  - Alerts, cases, decisions and evidence
  - Risk data aggregation and model governance
  - Compliance and regulatory change
  - Financial-crime and fraud control chain
  - Audit, legal privilege and records
  - Accounting and financial-control boundary
  - Worked trace: investigate a financial-crime alert
  - Security, privacy and resilience
  - BIAN alignment without name matching
  - Current-to-target considerations
  - Choose the model that matches the oversight question
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 48. Channels, Communications, Documents, Workflow, Case Management and Shared Services

- Manuscript file: `manuscript/part-05-bian-case-study/48-bian-security-control-architecture.md`
- Scope: Explain the shared capabilities through which customers and colleagues interact with a full-service bank. The chapter separates channels, identity, entitlement, communications, documents, workflow, rules and case management, then shows how they support product domains without taking over product authority.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this architecture answers
  - Governed domains, capabilities and processes
  - Channels are views into bank responsibilities
  - Identity is not entitlement
  - Communications and notifications
  - Documents and content
  - Workflow and rules
  - Case management
  - Shared platform selection
  - Information and integration
  - Worked trace: complaint and redress
  - Accounting and settlement boundary
  - Security and trust boundaries
  - Resilience and operations
  - BIAN alignment and limits
  - Current-to-target considerations
  - When these models should and should not be used
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 49. BIAN Mapping Method and Full-Stack Traceability

- Manuscript file: `manuscript/part-05-bian-case-study/49-bian-deployment-operations.md`
- Scope: Explain how to map Horizon Bank responsibilities to the Banking Industry Architecture Network (BIAN) without turning a reference architecture into an implementation blueprint. The method connects a versioned BIAN candidate to business outcome, process, organisation, application, information, integration, accounting, control, resilience and operational evidence.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this method answers
  - Who uses the mapping
  - What a BIAN mapping is
  - Separate four questions before mapping
  - The mapping method
  - Worked trace: cross-border payment
  - How mapping supports architecture decisions
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 50. BIAN-Aligned Application, Software-Service and Team Boundaries

- Manuscript file: `manuscript/part-05-bian-case-study/50-legacy-to-bian-migration.md`
- Scope: Explain how Horizon Bank turns business and Banking Industry Architecture Network (BIAN) responsibilities into defensible application, software-service, deployment and team boundaries. The chapter keeps these boundaries separate, then shows how they can be aligned without assuming a one-to-one relationship.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this architecture answers
  - Who uses boundary decisions
  - Five boundaries that must not be confused
  - Start with responsibility, not technology
  - Boundary factors
  - A practical boundary decision method
  - Common mapping patterns
  - Ownership is multidimensional
  - Worked boundary assessment: payments
  - Avoiding a distributed monolith
  - When to use these boundary models
  - Current-to-target considerations
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 51. APIs, Events, Commands, Batch, Files, Workflow and External Networks

- Manuscript file: `manuscript/part-05-bian-case-study/51-bian-adoption-roadmap.md`
- Scope: Explain how Horizon Bank selects and governs interaction styles across a full-service-bank estate. The chapter distinguishes synchronous Application Programming Interfaces (APIs), commands, events, messages, batch, files, workflow hand-offs and external-network exchanges, then connects each style to semantics, security, failure, reconciliation and operations.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this architecture answers
  - Who uses interaction models
  - Interaction style is a design decision
  - A minimum governed contract
  - Synchronous APIs
  - BIAN Semantic APIs require adaptation
  - Commands
  - Events
  - General asynchronous messages
  - Batch and file exchange
  - Workflow hand-offs
  - External networks
  - Worked interaction trace: cross-border payment
  - Choosing the style
  - Current-to-target considerations
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 52. Deployment, Security, Resilience, Observability and Operations

- Manuscript file: `manuscript/part-05-bian-case-study/52-bian-governance.md`
- Scope: Explain how Horizon Bank turns logical applications and interfaces into an operable architecture. The chapter connects deployment, identity, security, resilience, observability, incident response, recovery and service ownership without claiming unsupported physical products or numerical objectives.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The question this architecture answers
  - Who uses the operating architecture
  - Keep logical and physical levels separate
  - Deployment architecture begins with requirements
  - Environments and release flow
  - Container platforms are implementation choices
  - Data placement and recovery
  - Security follows identities and resources
  - Security telemetry and sensitive data
  - Resilience begins with the critical operation
  - Degraded operation is a business decision
  - Dependency-aware recovery
  - Observability explains system behaviour
  - From telemetry to action
  - Operational ownership and runbooks
  - Worked recovery trace: payment service after cyber disruption
  - Selecting the right operational model
  - Current-to-target considerations
  - Common mistakes
  - Chapter summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and source notes
  - Deferred work

#### 53. Legacy Modernisation, Data Migration and Transition Architecture

- Manuscript file: `manuscript/part-05-bian-case-study/53-bian-success-measures.md`
- Scope: Modernisation is the controlled movement of business responsibilities, data and operations from one architecture state to another. It is not a mass renaming of old systems and it is rarely a single cutover. This chapter answers: **How can a bank change a live estate without losing financial integrity, customer service, control evidence or a credible route back?** It provides a practical transition method for Horizon Bank, using its governed catalogues as an author model rather than claiming one universal migration sequence.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Start with business continuity, not replacement technology
  - Describe three architecture states explicitly
  - Select a modernisation strategy by responsibility
  - Slice change into controlled work packages
  - Treat data migration as governed state transfer
  - Design coexistence deliberately
  - Prepare cutover, rollback and recovery together
  - Decommission the old responsibility, not only the server
  - Common mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 54. Governance, Ownership and the Architecture Repository

- Manuscript file: `manuscript/part-05-bian-case-study/54-bian-common-mistakes.md`
- Scope: Architecture governance makes design information usable for decisions. It assigns authority, records evidence, controls change and makes exceptions visible. A repository supports that work, but a folder or modelling tool cannot govern itself. This chapter answers: **Who is accountable for the full-bank architecture model, how do records change, and what makes the repository trustworthy?** It applies those questions to Horizon Bank's controlled catalogues.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Governance is a decision system
  - Keep ownership types distinct
  - Use federated decision rights
  - Make the repository a governed model
  - Operate a controlled change workflow
  - Define conformance without pretending all differences are equal
  - Govern exceptions as temporary decisions
  - Version the right things
  - Validate structure and review meaning
  - Use event-driven maintenance as well as a calendar
  - Common governance failures
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 55. Measures, Quality Gates and the Full-Bank Coverage Audit

- Manuscript file: `manuscript/part-05-bian-case-study/55-bian-review-checklist.md`
- Scope: Measures make architecture claims testable. Quality gates stop work from advancing when essential evidence is absent. A coverage audit asks whether the bank model connects every required viewpoint, not whether the repository contains many files. This chapter answers: **How can reviewers test that Horizon Bank's full-bank architecture is complete enough, internally consistent and useful for a decision?** It defines a reproducible audit method without inventing performance targets or claiming that an unresolved record is complete.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Measure what the architecture is meant to improve
  - Define every measure before using it
  - Use balanced architecture measures
  - Build quality gates around evidence
  - Audit the full-bank coverage matrix reproducibly
  - Worked audit: immediate domestic payment
  - Review viewpoints
  - Common measurement mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

#### 56. Integrated End-to-End Scenarios and Practitioner Reference

- Manuscript file: `manuscript/part-05-bian-case-study/56-bian-quick-reference.md`
- Scope: An end-to-end scenario connects a business trigger to an observable outcome across responsibilities, applications, information, interfaces, financial consequences, controls and operations. It prevents each specialist view from appearing complete while the customer or bank outcome falls through the gaps. This final Part V chapter answers: **How does a practitioner assemble and review the minimum coherent model set for a full banking scenario?** It consolidates the Horizon Bank method, worked traces and reusable templates. It is not a substitute for the governed catalogues or for the technique guidance in earlier chapters.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - The integrated scenario contract
  - Hierarchy cheat sheet
  - Choose views by question
  - Scenario pattern 1: relationship to account to payment
  - Scenario pattern 2: corporate trade finance
  - Scenario pattern 3: investment through asset servicing
  - Scenario pattern 4: close, reporting and recovery
  - Service Domain assessment template
  - Business Scenario template
  - Application mapping template
  - Implementation decision tree
  - Common integrated-modelling mistakes
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - References and further reading

### Part VI: Practical Architecture Reference Guide

#### 57. How to Choose the Right Diagram

- Manuscript file: `manuscript/part-06-practical-reference/57-choose-the-right-diagram.md`
- Scope: Provide decision guidance by question, stakeholder, abstraction level, notation, lifecycle stage and common alternatives.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Start with the architecture question
  - Identify audience and decision
  - Select abstraction level
  - Choose one primary notation
  - Add complementary views
  - Decision tree
  - Selection matrix
  - Worked example
  - Quick-reference summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 58. Minimum Diagram Sets

- Manuscript file: `manuscript/part-06-practical-reference/58-minimum-diagram-sets.md`
- Scope: Define practical minimum sets for small applications, microservices solutions, enterprise transformation, business-process change and banking scenarios.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Small application
  - Microservices solution
  - Enterprise transformation
  - Business-process transformation
  - Data platform
  - Integration programme
  - Cloud migration
  - Regulated banking change
  - Worked example
  - Quick-reference summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 59. Diagram Quality Guidelines

- Manuscript file: `manuscript/part-06-practical-reference/59-diagram-quality-guidelines.md`
- Scope: Cover purpose, audience, boundary, labels, relationship direction, legend, abstraction level, colour, accessibility, assumptions and update discipline.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - One purpose per diagram
  - Consistent abstraction
  - Clear boundaries
  - Relationship labels
  - Legends and notation
  - Colour and accessibility
  - Naming
  - Versioning
  - Reviewability
  - Worked example
  - Quick-reference summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 60. Common Modelling Mistakes

- Manuscript file: `manuscript/part-06-practical-reference/60-common-modelling-mistakes.md`
- Scope: Cover showing everything, undocumented arrows, colour-only meaning, mixed abstraction, missing boundaries, unlabeled interfaces, weak ownership and over-complex notation.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Everything-on-one-page
  - Unlabelled arrows
  - Mixed abstraction
  - Decorative colour
  - Missing responsibilities
  - Missing protocols
  - No source of truth
  - Stale diagrams
  - Tool-driven modelling
  - Worked example
  - Quick-reference summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 61. Modelling Tools and Diagrams as Code

- Manuscript file: `manuscript/part-06-practical-reference/61-modelling-tools-diagrams-as-code.md`
- Scope: Cover PlantUML, Mermaid, Draw.io, Camunda Modeler, Structurizr, visual tools, diagrams as code, version control and rendering workflow.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - General diagramming tools
  - UML tools
  - C4 tools
  - BPMN tools
  - ArchiMate tools
  - Mermaid
  - PlantUML
  - Structurizr DSL
  - Version control
  - Generation and publishing
  - Worked example
  - Quick-reference summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 62. Architecture Review Checklists

- Manuscript file: `manuscript/part-06-practical-reference/62-architecture-review-checklists.md`
- Scope: Provide checklists by viewpoint, lifecycle stage, stakeholder and diagram type.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - General diagram review
  - Business architecture review
  - Application review
  - Data review
  - Integration review
  - Security review
  - Infrastructure review
  - Operational review
  - Migration review
  - Worked example
  - Quick-reference summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 63. Building and Maintaining an Architecture Repository

- Manuscript file: `manuscript/part-06-practical-reference/63-architecture-repository-practice.md`
- Scope: Cover folder structure, naming, source notes, diagram registers, decision logs, version control, quality checks and maintenance rhythm.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Repository structure
  - Naming and identifiers
  - Traceability
  - Decision records
  - Source management
  - Status and ownership
  - Review lifecycle
  - Automation
  - Archiving and deprecation
  - Worked example
  - Quick-reference summary
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

Last updated: 2026-06-29
