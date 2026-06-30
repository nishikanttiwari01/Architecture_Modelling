# Working Glossary

This file controls terminology across the manuscript. Add a term when it first becomes important, and link it to the chapter that provides the full explanation.

| Term | Working definition | Preferred usage / caution |
|---|---|---|
| Architecture | The fundamental concepts, structures, relationships and principles that shape a system or enterprise. | Do not use as a synonym for one diagram. |
| Model | A purposeful abstraction of part of reality. | A model may be represented by several diagrams or views. |
| Diagram | A visual representation of selected model content. | A diagram is not automatically the complete model. |
| View | A representation of a system from the perspective of related stakeholder concerns. | Use with a stated purpose and audience. |
| Viewpoint | A reusable specification for constructing, interpreting, analysing and reviewing a type of view. | Distinguish from the individual view created for one system. |
| Notation | A defined set of visual or textual symbols and rules. | UML and BPMN are notations/languages. |
| Unified Modeling Language (UML) | A general-purpose modelling language for describing software-intensive systems with structural and behavioural diagrams. | Use UML when its notation helps answer a specific question; do not imply every UML diagram is needed. |
| Method | A defined way of carrying out architecture work through a sequence of activities and decisions. | A method explains how to work; a notation explains how to represent the result. |
| Framework | A structured body that can include concepts, guidance, roles, governance, methods, viewpoints and modelling languages. | TOGAF is a framework; ArchiMate is a modelling language. |
| Stakeholder | A person, group or organisation with an interest in the architecture. | Link stakeholders to concerns before choosing views. |
| Concern | An interest or question that an architecture description should address for a stakeholder. | Use concrete concerns such as security, cost, resilience or usability. |
| Capability | An ability an organisation possesses to achieve an outcome. | Avoid describing a sequence of tasks as a capability. |
| Value stream | A sequence of value-creating stages that delivers an outcome to a stakeholder. | Distinguish from detailed process flow. |
| Business process | An ordered set of activities that produces a business outcome. | BPMN is commonly used to model it. |
| Business Process Model and Notation (BPMN) | A standard notation for modelling business processes, collaborations and process behaviour. | Use for business-process flow, participants, events, decisions and exceptions; do not treat it as a software structure diagram. |
| ArchiMate | The Open Group enterprise architecture modelling language for describing relationships across strategy, business, application, technology, motivation and migration concerns. | Use ArchiMate 4 as the current source for Chapter 7; do not use it as a replacement for BPMN process detail or C4 software design views. |
| The Open Group Architecture Framework (TOGAF) | An enterprise architecture framework and method from The Open Group. | Distinguish from ArchiMate, which is a modelling language. |
| Domain (ArchiMate) | A formal ArchiMate 4 grouping of related concepts, replacing the older layer framing in current terminology. | It is acceptable to explain older practitioner wording such as business layer, but use domain for current ArchiMate 4 terminology. |
| Strategy domain (ArchiMate) | ArchiMate concepts for organisational abilities, resources, value streams and courses of action. | Use for capability and strategic direction questions, not detailed process flow. |
| Role (ArchiMate) | A responsibility performed by an actor. | Actors may perform several roles, and roles may be performed by different actors. |
| Motivation element (ArchiMate) | An ArchiMate concept that explains why an architecture exists or what shapes it, such as a stakeholder, driver, assessment, goal, outcome, requirement or principle. | Keep goals concrete enough to trace to architecture choices; do not use the removed ArchiMate 3.2 Constraint element as current ArchiMate 4 notation. |
| Plateau (ArchiMate) | A relatively stable architecture state in an implementation and migration view. | Use for current, transition or target states; do not turn it into a delivery schedule. |
| Gap (ArchiMate 3.2 historical) | A removed ArchiMate element formerly used for a difference between architecture states. | Do not use as current ArchiMate 4 notation in Chapter 7 diagrams. |
| Technology Node (ArchiMate) | A technology active structure element that can host, process, store or execute technology behaviour. | Do not treat every managed technology service as a node by default. |
| System Software (ArchiMate) | Software that provides an environment for applications or technology behaviour. | Distinguish from the business application being modelled. |
| Service in the Technology domain (ArchiMate) | Technology behaviour exposed for use by applications or other technology elements. | Use when the concern is consumed technology capability rather than runtime placement. |
| Artifact (ArchiMate) | A deployable or stored technology item. | The official ArchiMate spelling is `Artifact`; the book otherwise uses British English for ordinary prose. |
| BPMN pool | A participant in a BPMN process or collaboration. | Use for a process owner, organisation or major participant; do not use as a C4 container. |
| BPMN lane | A responsibility partition inside a BPMN pool. | Use only when it clarifies who performs work. |
| Sequence flow | A BPMN arrow showing the order of work inside one process. | Do not draw it across pool boundaries. |
| Message flow | A BPMN arrow showing communication between separate BPMN participants. | Use across pools, not for internal task order. |
| Gateway | A BPMN decision, merge, split or synchronisation point. | Label outgoing conditions when a branch is not self-evident. |
| Semantic BPMN modeller | A BPMN-aware tool that stores process elements and relationships as BPMN model content, often in BPMN XML. | Prefer for interoperable BPMN source, validation and execution-oriented semantics. |
| Business service | An externally visible unit of business behaviour that provides value. | Clarify the consumer. |
| Application service | Behaviour exposed by an application to support users or other applications. | Distinguish from an application component. |
| Application component | A modular, replaceable and encapsulated part of an application architecture. | ArchiMate and UML use related but not identical concepts. |
| Software system | A cohesive collection of software that delivers value to users or other systems. | C4 Level 1 concept. |
| Container (C4) | A separately runnable or deployable unit that executes code or stores data. | It does not automatically mean Docker or Kubernetes. |
| Component (C4) | A grouping of related functionality encapsulated behind an interface inside a container. | Do not use for individual classes. |
| System Context diagram | A C4 view that shows one software system, the people who use it and the external systems it interacts with. | Use to establish scope before internal design detail. |
| System Landscape diagram | A C4 view that shows multiple software systems in a wider organisational or enterprise landscape. | Use for estate-level relationships, not detailed process flow. |
| Actor | A person, role, organisation or system that interacts with a subject. | State which meaning is intended. |
| Use case | A goal-oriented interaction between actors and a subject system. | Use for scope and user goals, not for internal screen or code design. |
| Class | A UML classifier that describes a set of objects with common features, such as attributes, operations and relationships. | Keep analysis classes separate from physical database tables unless that mapping is intentional. |
| Lifeline | A participant in an interaction, usually shown in a UML sequence diagram. | Use for roles or system parts in one scenario; avoid turning it into an organisational chart. |
| State | A condition in the lifecycle of an entity or system where particular behaviour or rules apply. | Use state machines for meaningful lifecycle changes, not simple linear task lists. |
| Interface | A defined point of interaction between elements. | Label protocol and responsibility where relevant. |
| API | An application programming interface that exposes defined operations or resources. | An API is an interface, not the implementation itself. |
| Event | A record that something of business or technical significance happened. | Use past-tense names for facts, such as `PaymentAuthorised`. |
| Command | A request for a system or domain to perform an action. | A command may be rejected; an event records an occurrence. |
| Entity | A domain or data object distinguished by identity over time. | Do not confuse with every database table. |
| Value object | A domain object defined by its values rather than an enduring identity. | Common in domain-driven design. |
| Bounded context | A boundary within which a domain model and its language are consistent. | It is a design boundary, not automatically a deployment unit. |
| Service Domain (BIAN) | A logical, discrete banking capability partition defined by BIAN. | Do not map automatically to one microservice. |
| Business Scenario (BIAN) | A representation of Service Domain interactions in response to a business event or objective. | Complement with BPMN when human and process detail is needed. |
| Semantic API (BIAN) | An API specification aligned to BIAN service semantics. | Adaptation and governance are still required. |
| Business Object Model (BIAN) | A semantic reference model for banking information concepts. | Do not treat it as a ready-made physical database schema. |
| Current state | The architecture as it exists now. | Also called as-is or baseline architecture. |
| Target state | The intended future architecture. | Also called to-be architecture. |
| Transition architecture | A coherent intermediate state between current and target architectures. | State its duration and purpose. |
| Architecture Decision Record (ADR) | A concise record of an important architecture decision, context and consequences. | Use stable identifiers and retain superseded records. |
| Trust boundary | A boundary across which the level or basis of trust changes. | Make it explicit in security diagrams. |
| Data lineage | Traceability of data from origin through movement and transformation to use. | Distinguish from a general data-flow diagram. |
| Semantic repository tool | A modelling tool that stores reusable model concepts and relationships rather than only drawing shapes. | Useful when governance, reuse, reporting and impact analysis matter. |
| Diagrams as code | A diagramming approach where editable diagram source is stored as text and rendered into publication formats. | Good for reproducibility and version control; not automatically a governed model repository. |

## Terms requiring future decision

- Final distinction between `client` and `customer` in banking chapters
- Preferred use of `artefact` versus `artifact` in technical file names
- Final publication convention for `as-is` and `to-be`
