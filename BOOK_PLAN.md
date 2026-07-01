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
- Scope: Cover security viewpoints, trust boundaries, authentication flows, authorisation models, threat modelling, STRIDE, attack trees, threat-model data-flow diagrams, security control mapping, privacy and data classification.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Security viewpoints
  - Trust-boundary diagrams
  - Authentication flows
  - Authorisation models
  - Threat modelling
  - STRIDE
  - Attack trees
  - Threat-model Data Flow Diagrams
  - Security control mapping
  - Privacy and data classification
  - Security modelling versus nearby approaches
  - Common mistakes
  - Chapter cheat sheet
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes
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

#### 31. Introduction to BIAN

- Manuscript file: `manuscript/part-05-bian-case-study/31-introduction-to-bian.md`
- Scope: Explain BIAN as a banking reference architecture and semantic standard, not a product, and separate reference concepts from Horizon Bank implementation choices.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Why BIAN exists
  - Service Landscape
  - Business Areas and Business Domains
  - Service Domains
  - Business Scenarios
  - Service Operations
  - Business Object Model
  - Semantic APIs and events
  - What BIAN does not prescribe
  - Logical reference versus physical implementation
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 32. How BIAN Relates to Other Modelling Techniques

- Manuscript file: `manuscript/part-05-bian-case-study/32-bian-and-modelling-techniques.md`
- Scope: Map BIAN to capability, process, information, application, API, event and deployment views without reducing Service Domains to microservices.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - BIAN and ArchiMate
  - BIAN and BPMN
  - BIAN and C4
  - BIAN and UML
  - BIAN and data modelling
  - BIAN and DMN
  - BIAN and event modelling
  - Cross-reference matrix
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 33. Defining the Full Banking Operating Model

- Manuscript file: `manuscript/part-05-bian-case-study/33-full-banking-operating-model.md`
- Scope: Establish Horizon Bank's operating model, major customer groups, channels, product families, operational capabilities and modelling boundaries.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Bank vision and objectives
  - Stakeholder model
  - Organisation model
  - Capability map
  - Capability heat map
  - Operating model choices
  - Governance and ownership
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 34. Complete Bank Business Process Architecture

- Manuscript file: `manuscript/part-05-bian-case-study/34-bank-business-process-architecture.md`
- Scope: Catalogue strategy, market, product, party, onboarding, origination, deposits, lending, payments, cards, corporate banking, trade finance, wealth, treasury, fraud, compliance, risk, reporting, finance, operations, collections, channels, HR, procurement, legal, audit, support and technology process families.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Strategy and governance
  - Market and business development
  - Product and pricing
  - Party and customer management
  - Onboarding and KYC
  - Sales and origination
  - Deposits and accounts
  - Lending
  - Payments
  - Cards
  - Corporate banking and cash management
  - Trade finance
  - Wealth and investments
  - Treasury and capital markets
  - Fraud
  - Financial crime compliance
  - Enterprise risk
  - Regulatory reporting
  - Finance and accounting
  - Banking operations
  - Collections and recovery
  - Channels
  - Human resources
  - Procurement and suppliers
  - Legal, audit and support
  - Technology management
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 35. Modelling Bank Value Streams with BIAN

- Manuscript file: `manuscript/part-05-bian-case-study/35-bank-value-streams.md`
- Scope: Connect value streams to capabilities, Service Domains, customer outcomes, products, channels and process scenarios.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Capability versus value stream versus process
  - Customer acquisition
  - Product acquisition
  - Payment
  - Lending
  - Customer servicing
  - Risk management
  - Mapping stages to BIAN Service Domains
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 36. Creating BIAN-Aligned Business Scenarios

- Manuscript file: `manuscript/part-05-bian-case-study/36-bian-business-scenarios.md`
- Scope: Explain business events, participating Service Domains, interaction paths, information exchanged, process complements and scenario review criteria.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Business Scenario definition
  - Scenario versus BPMN process
  - Trigger and outcome
  - Participating Service Domains
  - Interaction levels
  - Human activities
  - Decisions
  - Technical interactions
  - Events
  - Scenario template
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 37. Practical Scenario 1: Customer Onboarding

- Manuscript file: `manuscript/part-05-bian-case-study/37-customer-onboarding-scenario.md`
- Scope: Model onboarding scope, actors, channels, KYC, AML, customer data, identity checks, exceptions, Service Domain interactions and controls.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Business objective
  - Customer journey
  - BIAN Service Domains
  - ArchiMate capability view
  - BPMN process
  - DMN risk classification
  - Business Scenario interaction map
  - C4 architecture
  - UML sequence
  - Party data model
  - Security and privacy
  - Events and metrics
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 38. Practical Scenario 2: Open a Current Account

- Manuscript file: `manuscript/part-05-bian-case-study/38-current-account-opening-scenario.md`
- Scope: Model account opening, eligibility, product selection, party verification, account fulfilment, data creation, notifications and operational handover.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Business objective
  - BPMN process
  - Service Domain mapping
  - Eligibility decision
  - Agreement creation
  - Account state machine
  - C4 design
  - API and events
  - Data model
  - Accounting entries
  - Controls
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 39. Practical Scenario 3: Execute a Cross-Border Payment

- Manuscript file: `manuscript/part-05-bian-case-study/39-cross-border-payment-scenario.md`
- Scope: Model payment initiation, validation, sanctions screening, pricing, routing, account posting, messaging, exceptions and reconciliation.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Customer journey
  - End-to-end BPMN
  - Service Domains
  - Payment routing DMN
  - UML sequence
  - Payment state machine
  - ISO 20022 information
  - Events
  - C4 deployment
  - Exceptions and investigations
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 40. Practical Scenario 4: Consumer Loan Origination

- Manuscript file: `manuscript/part-05-bian-case-study/40-consumer-loan-origination-scenario.md`
- Scope: Model application capture, affordability, credit decisioning, offer, documentation, fulfilment, disbursement and risk controls.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Customer journey
  - BPMN process
  - Service Domain map
  - Credit DMN
  - Affordability and collateral
  - Loan state machine
  - C4 architecture
  - UML sequence
  - Loan data model
  - Events and accounting
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 41. Practical Scenario 5: Card Fraud Investigation

- Manuscript file: `manuscript/part-05-bian-case-study/41-card-fraud-investigation-scenario.md`
- Scope: Model alert intake, case triage, customer contact, transaction review, dispute handling, card controls, chargeback and closure.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Monitoring
  - Fraud evaluation
  - Alert generation
  - Case investigation
  - Customer contact
  - Blocking actions
  - BPMN process
  - DMN disposition
  - Event architecture
  - Case state machine
  - Service Domain map
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 42. Practical Scenario 6: Corporate Cash Management

- Manuscript file: `manuscript/part-05-bian-case-study/42-corporate-cash-management-scenario.md`
- Scope: Model corporate onboarding, account structures, liquidity services, payments, reporting, approvals, integration and service operations.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Corporate journey
  - Mandate management
  - Cash concentration
  - Virtual accounts
  - Bulk payments
  - Capability map
  - BPMN collaboration
  - C4 architecture
  - Data and liquidity models
  - Controls and reporting
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 43. Mapping BIAN to Applications

- Manuscript file: `manuscript/part-05-bian-case-study/43-mapping-bian-to-applications.md`
- Scope: Explain mapping from Service Domains and business capabilities to application components, packages, ownership and legacy constraints.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Application inventory
  - Map applications to Service Domains
  - Many-to-many mappings
  - Application-function matrix
  - Duplication heat map
  - Rationalisation decisions
  - ArchiMate application view
  - C4 landscape
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 44. Designing BIAN-Aligned Software Services

- Manuscript file: `manuscript/part-05-bian-case-study/44-bian-aligned-software-services.md`
- Scope: Explain service boundaries, API responsibilities, events, transactions, consistency, ownership, security and why logical BIAN boundaries do not mandate physical microservices.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Logical versus physical boundaries
  - Why Service Domain is not automatically a microservice
  - Boundary factors
  - Bounded contexts
  - Service components
  - Orchestration services
  - Platform services
  - C4 and UML models
  - Avoiding distributed monoliths
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 45. Implementing BIAN Semantic APIs

- Manuscript file: `manuscript/part-05-bian-case-study/45-bian-semantic-apis.md`
- Scope: Cover semantic API purpose, resource and operation design, adaptation, governance, versioning, service contracts and consumer usability.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Semantic API concepts
  - Service Domain operations
  - Action terms
  - REST mapping
  - Bank-specific adaptation
  - OpenAPI
  - Messages
  - Security
  - Error handling
  - Idempotency
  - Versioning
  - API gateway
  - Legacy adapters
  - Conformance
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 46. Implementing BIAN with Events

- Manuscript file: `manuscript/part-05-bian-case-study/46-bian-events.md`
- Scope: Cover business events, integration events, event schemas, producers, consumers, topics, ordering, idempotency, privacy and governance.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Commands, events and queries
  - Domain versus integration events
  - Ownership
  - Event catalogue
  - Schemas
  - Kafka topic design
  - Ordering
  - Duplicates
  - Versioning
  - Eventual consistency
  - Sagas
  - Lineage and audit
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 47. BIAN Information and Data Architecture

- Manuscript file: `manuscript/part-05-bian-case-study/47-bian-data-architecture.md`
- Scope: Cover Business Object Model usage, canonical information, logical data, ownership, lineage, data quality, reference data and physical implementation choices.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Business Object Model
  - Canonical versus local models
  - Party and customer
  - Product
  - Agreement
  - Account
  - Transaction and payment
  - Loan and collateral
  - Position and balance
  - Case and document
  - Conceptual architecture
  - Logical model
  - Physical model
  - Data ownership
  - Master and reference data
  - Lineage
  - Privacy and retention
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 48. BIAN Security and Control Architecture

- Manuscript file: `manuscript/part-05-bian-case-study/48-bian-security-control-architecture.md`
- Scope: Cover trust boundaries, access control, customer data protection, financial crime controls, audit, segregation of duties and operational resilience.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Trust zones
  - Customer identity
  - Employee identity
  - Service identity
  - Customer entitlements
  - Employee entitlements
  - Segregation of duties
  - Consent
  - Transaction authorisation
  - Data protection
  - Audit
  - STRIDE
  - Fraud and financial-crime controls
  - Security diagrams
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 49. BIAN Deployment and Operational Architecture

- Manuscript file: `manuscript/part-05-bian-case-study/49-bian-deployment-operations.md`
- Scope: Cover deployment models, environments, monitoring, resilience, incident support, service ownership and operational runbooks.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Environments
  - Cloud, on-premises and hybrid
  - Kubernetes
  - Availability zones
  - Load balancing
  - Databases
  - Event platform
  - Disaster recovery
  - Observability
  - Business service monitoring
  - SLOs
  - Operational ownership
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 50. Migrating from Legacy Architecture to BIAN

- Manuscript file: `manuscript/part-05-bian-case-study/50-legacy-to-bian-migration.md`
- Scope: Cover current-state assessment, target decomposition, strangler patterns, coexistence, data migration, service transition and risk management.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Assess current architecture
  - Map legacy applications
  - Identify gaps and duplication
  - Select pilot
  - Transition architectures
  - Strangler pattern
  - API façade
  - Event interception
  - Data migration
  - Parallel operation
  - Decommissioning
  - Benefits
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 51. BIAN Adoption Roadmap

- Manuscript file: `manuscript/part-05-bian-case-study/51-bian-adoption-roadmap.md`
- Scope: Cover adoption phases, capability sequencing, pilot selection, governance setup, training, tooling and measurable outcomes.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Evaluate BIAN
  - Define pilot
  - Execute pilot
  - Establish adoption
  - Evolve architecture practice
  - Realise benefits
  - Roadmap artefacts
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 52. BIAN Governance Model

- Manuscript file: `manuscript/part-05-bian-case-study/52-bian-governance.md`
- Scope: Cover decision rights, reference model stewardship, semantic API governance, architecture review, change control and exception handling.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Architecture board
  - Capability owners
  - Service Domain owners
  - Data owners
  - API owners
  - Product owners
  - Review process
  - Exception process
  - Conformance levels
  - Repository management
  - Version management
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 53. Measuring BIAN Implementation Success

- Manuscript file: `manuscript/part-05-bian-case-study/53-bian-success-measures.md`
- Scope: Cover metrics for business outcomes, reuse, integration quality, delivery speed, consistency, risk reduction and operating health.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Business measures
  - Architecture measures
  - Technology measures
  - Risk and compliance measures
  - Baseline and targets
  - Benefits dashboard
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 54. Common BIAN Implementation Mistakes

- Manuscript file: `manuscript/part-05-bian-case-study/54-bian-common-mistakes.md`
- Scope: Cover microservice over-mapping, ignoring business ownership, weak semantics, excessive technical focus, incomplete governance and poor migration sequencing.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - BIAN as an IT-only exercise
  - API-first without capability understanding
  - Service Domain equals microservice
  - Big-bang implementation
  - Renaming legacy systems
  - Ignoring processes and journeys
  - Misusing the data model
  - Copying APIs unchanged
  - Missing ownership
  - Unmaintained repositories
  - Wrong success measures
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 55. BIAN Implementation Review Checklist

- Manuscript file: `manuscript/part-05-bian-case-study/55-bian-review-checklist.md`
- Scope: Provide structured review questions for business, process, information, application, API, event, security, operational and migration views.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Business review
  - BIAN alignment review
  - Process review
  - Information review
  - Application review
  - Technology review
  - Security review
  - Transformation review
  - Decision log
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

#### 56. BIAN Quick Reference

- Manuscript file: `manuscript/part-05-bian-case-study/56-bian-quick-reference.md`
- Scope: Provide compact definitions, mapping guidance, scenario patterns, artefact list, common cautions and review prompts.
- Subsections:
  - Chapter purpose
  - Reader outcomes
  - Prerequisites and dependencies
  - Required models and artefacts
  - Worked examples
  - Source requirements
  - Planned chapter structure
  - Hierarchy cheat sheet
  - BIAN-to-ArchiMate
  - BIAN-to-BPMN
  - BIAN-to-C4
  - BIAN-to-UML
  - BIAN-to-data
  - Service Domain assessment template
  - Business Scenario template
  - Application mapping template
  - Implementation decision tree
  - Chapter summary
  - Completion checklist
  - Key takeaways
  - Practical exercise
  - Review checklist
  - Drafting notes

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
