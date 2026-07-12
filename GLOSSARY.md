# Working Glossary

This file controls terminology across the manuscript. Add a term when it first becomes important, and link it to the chapter that provides the full explanation.

| Term | Working definition | Preferred usage / caution |
|---|---|---|
| Banking Industry Architecture Network (BIAN) | Industry association and name commonly used for its banking reference architecture and semantic standard. | Define the acronym at first use in each standalone chapter. |
| Business Area | Broad grouping used to organise the BIAN Service Landscape. | Do not assume it is an organisational division. |
| Business Domain | Focused grouping within a BIAN Business Area. | Use as a navigation grouping, not an application boundary. |
| Service Operation | Logical business service exposed by a Service Domain. | Do not equate it automatically with a physical endpoint or topic. |
| Semantic API | Interface reference whose operations and information have consistent banking meaning. | Physical protocol and operational design remain implementation choices. |
| Operating model | A governed set of connected models explaining how an organisation creates outcomes through capabilities, processes, responsibilities, people, information, technology, controls and measures. | Do not present one organisation chart or architecture diagram as the complete operating model. |
| Traceability register | A governed record of qualified links between model elements, including scope, owner, version, rationale and evidence. | Prefer precise relationship verbs; do not imply unlike elements are equal. |
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
| Capability levelling | The decomposition of a capability into lower-level capabilities, recording level and parent so scope is explicit. | Do not double count a parent capability together with its children; distinguish decomposition from contribution and dependency. |
| Value stream to capability cross-map | A matrix that maps each value-stream stage to the capabilities that enable it, often marking primary and supporting enablers. | Keep it at value-stage level; it is not a process model, customer journey map or Lean value-stream map. |
| Business process | An ordered set of activities that produces a business outcome. | BPMN is commonly used to model it. |
| Process architecture | A high-level view or catalogue of the major business processes, their triggers, outcomes, owners and relationships. | Use to select process scope before drawing detailed BPMN; do not confuse it with a capability map. |
| Process hierarchy | A controlled decomposition from enterprise process landscape through process families and end-to-end processes to selected subprocess or procedure detail. | Define each level and parent scope; do not mix unrelated abstraction levels in one flow. |
| Process owner | The role accountable for a defined process outcome, boundary, performance and governed improvement across contributing teams. | Accountability does not mean performing every activity or owning every contributing application or control. |
| Control process | A process that sets constraints, monitors adherence, tests evidence or responds to risk. | A control may also operate within a customer-facing or support process, so use classification as an attribute rather than an exclusive inventory. |
| Process level | The chosen degree of process detail, from landscape-level process selection through operational flow to procedure or automation detail. | Keep one level of abstraction in a diagram unless the viewpoint explains the mix. |
| Swimlane | A visual responsibility partition used to show who performs or owns work in a process-style view. | In BPMN use the formal terms pool and lane; do not turn swimlanes into a software structure diagram. |
| Process metric | A measure used to evaluate process performance, control evidence or outcome quality. | Define the metric, owner and scope; do not add metrics as decoration. |
| Straight-through processing | Completion of a process or case without manual intervention within the measured scope. | Useful for measuring automation, but not every case should flow straight through; high-risk cases may need deliberate review. |
| Business Process Model and Notation (BPMN) | A standard notation for modelling business processes, collaborations and process behaviour. | Use for business-process flow, participants, events, decisions and exceptions; do not treat it as a software structure diagram. |
| ArchiMate | The Open Group enterprise architecture modelling language for describing relationships across strategy, business, application, technology, motivation and migration concerns. | Use ArchiMate 4 as the current source for Chapter 7; do not use it as a replacement for BPMN process detail or C4 software design views. |
| The Open Group Architecture Framework (TOGAF) | An enterprise architecture framework and method from The Open Group. | Distinguish from ArchiMate, which is a modelling language. |
| Domain (ArchiMate) | A formal ArchiMate 4 grouping of related concepts, replacing the older layer framing in current terminology. | It is acceptable to explain older practitioner wording such as business layer, but use domain for current ArchiMate 4 terminology. |
| Strategy domain (ArchiMate) | ArchiMate concepts for organisational abilities, resources, value streams and courses of action. | Use for capability and strategic direction questions, not detailed process flow. |
| Role (ArchiMate) | A responsibility performed by an actor. | Actors may perform several roles, and roles may be performed by different actors. |
| Motivation element (ArchiMate) | An ArchiMate concept that explains why an architecture exists or what shapes it, such as a stakeholder, driver, assessment, goal, outcome, requirement or principle. | Keep goals concrete enough to trace to architecture choices; do not use the removed ArchiMate 3.2 Constraint element as current ArchiMate 4 notation. |
| Course of Action (ArchiMate) | A strategy-domain concept for an approach or plan the organisation chooses to achieve a goal. | Use for the chosen strategic approach; distinguish it from the funded change that delivers it. |
| Work Package (ArchiMate) | An implementation-and-migration concept for a set of change actions with a defined start and end, often shown with a familiar initiative name. | Use `Work Package` when formal notation is claimed; `initiative` is business language, not a formal element. |
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
| User journey | A view of the steps, channels, waits and pain points a user experiences while pursuing an outcome. | Use for user experience and channel movement; do not treat it as a complete system or process design. |
| Service blueprint | A view that connects user-visible steps with backstage work, supporting systems and responsibilities. | Useful when experience and operational support must be connected; keep detailed BPMN or API behaviour separate when needed. |
| Wireframe | A low-detail representation of a screen or interface layout. | Use for visible interface structure and feedback, not for system architecture by itself. |
| Screen flow | A view of how a user moves between screens or interface states. | Use for navigation and visible user flow; do not hide process, data or API ownership questions inside it. |
| Class | A UML classifier that describes a set of objects with common features, such as attributes, operations and relationships. | Keep analysis classes separate from physical database tables unless that mapping is intentional. |
| Lifeline | A participant in an interaction, usually shown in a UML sequence diagram. | Use for roles or system parts in one scenario; avoid turning it into an organisational chart. |
| State | A condition in the lifecycle of an entity or system where particular behaviour or rules apply. | Use state machines for meaningful lifecycle changes, not simple linear task lists. |
| Interface | A defined point of interaction between elements. | Label protocol and responsibility where relevant. |
| API | An application programming interface that exposes defined operations or resources. | An API is an interface, not the implementation itself. |
| API interaction view | A view that shows how a channel or service calls an API, including direction, request, response, error or later status behaviour. | Use when channel-to-service or service-to-service behaviour is the interaction concern; defer wider integration design to integration views. |
| Integration context view | A focused view of the systems that exchange information and the broad integration styles between them. | Label direction, style and ownership; do not leave relationships as vague "integrates with" lines. |
| Synchronous interaction | An interaction where the caller expects a response before it can continue within the modelled scenario. | Do not imply the business outcome is complete unless the contract actually guarantees it. |
| Asynchronous interaction | An interaction where sender and receiver do not need to proceed at the same time, often through a queue, event platform or later status update. | Include delivery expectation, ordering, duplicate handling and operational ownership where relevant. |
| Interface catalogue | A managed list of interfaces, owners, consumers, contracts, versions and operational responsibilities. | Use alongside diagrams; do not treat a runtime drawing as the complete interface record. |
| Idempotency | A property of an operation or consumer where repeating the same request or message does not apply the business effect more than once. | Important for retries and duplicate message delivery. |
| Dead-letter queue | A queue or holding area for messages that cannot be processed successfully after the configured handling path. | It needs monitoring, ownership and repair rules; it is not a disposal bin. |
| Domain model | A model of the concepts, rules and language used in a business or problem domain. | Do not reduce it to a database schema or class diagram too early. |
| Domain-Driven Design (DDD) | An approach to software and architecture design that keeps the model close to the business domain and its language. | Treat DDD as a design approach, not a standards-body notation. |
| Strategic Domain-Driven Design | DDD guidance focused on subdomains, bounded contexts, ubiquitous language and relationships between contexts. | Use for architecture boundaries, ownership and language differences. |
| Tactical Domain-Driven Design | DDD guidance focused on entities, value objects, aggregates, aggregate roots, repositories, domain services and domain events inside a bounded context. | Use after the bounded context is clear; do not apply patterns as boilerplate. |
| Ubiquitous language | The shared language used by domain experts and delivery teams within a bounded context. | It is context-specific; the same word may have different meanings in different contexts. |
| Subdomain | A part of the wider business domain with its own problem area and business importance. | Distinguish core, supporting and generic concerns where useful. |
| Core subdomain | A subdomain that creates distinctive business advantage or carries high strategic value. | Do not label every important function as core. |
| Supporting subdomain | A business-specific subdomain that is necessary but not the main differentiator. | Custom design may be justified, but keep investment proportionate. |
| Generic subdomain | A common subdomain that many organisations need and can often standardise, buy or outsource. | Avoid unnecessary custom design. |
| Event | A record that something of business or technical significance happened. | Use past-tense names for facts, such as `PaymentAuthorised`. |
| Command | A request for a system or domain to perform an action. | A command may be rejected; an event records an occurrence. |
| Domain event | An event that records something meaningful in the domain, using business language. | Do not confuse it with every technical message emitted by a system. |
| EventStorming | A collaborative workshop method for exploring a domain through events and related concepts. | Use it for discovery and shared understanding; it is not a publication notation by itself. |
| Event-driven architecture | An architecture style in which systems publish and react to events. | Distinguish domain events, integration events and technical notifications. |
| Event catalogue | A managed inventory of event definitions, owners, schemas and consumers. | Useful for governance; it should not be only a message-broker topic list. |
| Entity | A domain or data object distinguished by identity over time. | Do not confuse with every database table. |
| Value object | A domain object defined by its values rather than an enduring identity. | Common in domain-driven design. |
| Aggregate | A consistency boundary around related domain objects. | It is not automatically a database table, API resource or microservice. |
| Aggregate root | The object through which outside code accesses and changes an aggregate. | Do not bypass it when enforcing aggregate rules. |
| Repository (DDD) | A domain-facing way to retrieve and store aggregates without exposing storage detail. | Do not treat every data-access class as a DDD repository. |
| Domain service | Domain behaviour that does not naturally belong to one entity or value object. | Use sparingly; avoid empty entities with all behaviour in services. |
| Bounded context | A boundary within which a domain model and its language are consistent. | It is a design boundary, not automatically a deployment unit. |
| Upstream context | A context whose model, API or event language influences another context. | State who is downstream and what language or contract is consumed. |
| Downstream context | A context that consumes, conforms to or translates another context's model. | Identify where translation or dependency risk exists. |
| Anti-Corruption Layer | A translation boundary that protects one model from another model's language or assumptions. | Useful around legacy systems, vendor systems and mismatched external models. |
| Open Host Service | A stable service exposed by an upstream context for other contexts to use. | Pair with a clear published language where shared meaning matters. |
| Published Language | A shared integration language or contract used between contexts. | Keep it versioned and governed. |
| Event Sourcing | A design approach where state changes are stored as an ordered event history and current state is rebuilt from those events. | Do not assume every event-driven architecture uses Event Sourcing. |
| Command Query Responsibility Segregation (CQRS) | A design approach that separates write models from read models. | It can be used with or without Event Sourcing. |
| CloudEvents | A specification for common event envelope and context metadata across services, platforms and transports. | It standardises metadata such as `id`, `source`, `specversion` and `type`, not the business meaning of the payload. |
| Idempotent consumer | An event consumer that can process the same event more than once without applying the business effect twice. | Important when delivery is at least once or retries are possible. |
| Service Domain (BIAN) | A logical, discrete banking responsibility defined by BIAN. | Do not map automatically to one microservice or application. |
| Business Scenario (BIAN) | An archetypal representation of Service Domain interactions in response to a business event or objective. | Do not present it as a mandatory bank process; complement it with BPMN when human and process detail is needed. |
| Semantic API (BIAN) | An API specification aligned to BIAN service semantics. | Adaptation and governance are still required. |
| Business Object Model (BIAN) | BIAN's conceptual semantic reference model for shared banking vocabulary used in exchanges. | Do not treat it as a ready-made physical database schema. |
| Qualified mapping | A recorded relationship between model elements that states the relationship, scope, rationale, owner, version and evidence. | Prefer precise relationships such as `supports in part`; do not use `equals` for unlike model elements. |
| Current state | The architecture as it exists now. | Also called as-is or baseline architecture. |
| Target state | The intended future architecture. | Also called to-be architecture. |
| Architecture Decision Record (ADR) | A concise record of an important architecture decision, context and consequences. | Use stable identifiers and retain superseded records. |
| Trust boundary | A boundary across which the basis for trust changes, such as administrative authority, identity authority, security policy, data custody, execution environment, network enforcement or organisational responsibility. | Do not use external, internal and trusted as synonyms. Make the boundary basis explicit in security diagrams. |
| Conceptual data model | A data model that describes important business information concepts and their relationships without implementation detail. | Use before logical or physical design when meaning is still being agreed. |
| Logical data model | A data model that defines entities, attributes, keys and relationships independently of a specific storage technology. | Do not include vendor-specific physical database choices. |
| Physical data model | A data model that describes how data is implemented in a particular database, storage technology or platform. | Keep it traceable to conceptual and logical meaning. |
| Entity relationship diagram (ERD) | A diagram that shows entities, attributes and relationships, often with keys, cardinality and optionality. | Distinguish from a data flow diagram. |
| Attribute | A fact recorded about an entity. | Avoid adding attributes that do not answer the model question. |
| Key | A value or set of values used to identify an entity instance. | State whether the key is business meaning, technical implementation or both. |
| Cardinality | A rule that describes how many instances may participate in a relationship. | Use precise markers such as one, zero or more, or one or more. |
| Optionality | A rule that describes whether a relationship must exist. | Important for lifecycle timing, incomplete data and exception cases. |
| Data flow diagram (DFD) | A diagram that shows data movement and transformation between external entities, processes and data stores. | Do not use as a database schema or BPMN process model. |
| Data lineage | Traceability of data from origin through movement and transformation to use. | Distinguish from a general data-flow diagram. |
| Data lifecycle | The sequence of states and governance responsibilities data passes through from capture to retention, archive or disposal. | Use for ownership, authoritative status, retention and disposal concerns, not detailed process sequence. |
| Data owner | The accountable business role for decisions about the meaning and acceptable use of a defined data area. | Distinguish from application ownership and technical custody. Exact authority is organisation-specific. |
| Data steward | A role that helps maintain data definitions, quality rules, issue handling and appropriate use on behalf of governance arrangements. | Do not imply that the title or authority is universal across organisations. |
| Master data | Shared data describing relatively stable business subjects, such as Party or Product, that requires controlled meaning and governance. | Classification depends on scope; it does not require one physical master database. |
| Reference data | Controlled values used to classify or constrain other data, such as currency or status codes. | Record the authoritative source, version and change control where relevant. |
| Transaction data | Data recording a business activity or event, such as an Order, Payment or Payment Instruction. | Distinguish from master and reference data according to the modelled scope. |
| Data catalogue | A governed record of data definitions, classifications, ownership, sources, quality expectations and related metadata. | A catalogue complements diagrams; it is not automatically an authoritative data store. |
| Authoritative status | The status value treated as the trusted source for a particular purpose at a particular point in the lifecycle. | State which system or owner establishes it; do not assume one system is authoritative for every status. |
| Canonical data model | A shared model that defines common meaning for data exchanged or interpreted across several systems or domains. | Useful for shared meaning, but it should not become too broad to change. |
| Local data model | A model used within one application, system or bounded area for its internal responsibilities. | Keep mapped to shared terms where cross-system meaning matters. |
| Decision Model and Notation (DMN) | An Object Management Group standard for modelling repeatable business decisions, decision requirements and decision logic. | Use the current formal OMG DMN source for normative terminology; distinguish decision logic from process flow. |
| Decision table | A tabular decision model that maps input conditions to outputs according to stated rules and a hit policy. | Useful for explainable rules; do not hide complex process sequence inside it. |
| Decision Requirements Diagram (DRD) | A DMN diagram that shows decisions, input data, knowledge sources and business knowledge models and how they depend on each other. | Use for decision dependencies, not for BPMN task sequence. |
| Decision Requirements Graph (DRG) | The underlying network of DMN decision requirements relationships in a decision model. | A DRD is a diagram view over selected DRG content. |
| Decision logic | The expression, table or model that derives a decision result from inputs and rules. | Keep separate from the downstream process action. |
| Decision result | The output produced by a decision. | A result such as `Manual Review` is not the same as the human review process that follows. |
| Policy | A governing statement or constraint approved by an authority. | Distinguish from the specific business rules derived from it. |
| Business rule | A specific condition or rule derived from policy or operating practice. | Use in decision logic when it is stable enough to model. |
| Hit policy | A DMN decision-table indicator that states how matching rules are handled. | Do not leave implicit when more than one rule may match. |
| Friendly Enough Expression Language (FEEL) | The expression language used by DMN for decision logic. | Handle missing or null inputs deliberately. |
| Input Data (DMN) | A DMN element representing information supplied to a decision. | Use business-level input names before implementation column names. |
| Business Knowledge Model (DMN) | A reusable DMN element for decision logic or functions. | Useful when shared rules need governance. |
| Knowledge Source (DMN) | A DMN element representing an authority for decisions or knowledge models. | Use for policy, rulebook, regulatory or governance authority. |
| Decision Service (DMN) | A DMN element that can expose one or more decisions for use. | Mention as an optional beginner concept; do not imply every decision needs a service boundary. |
| Semantic repository tool | A modelling tool that stores reusable model concepts and relationships rather than only drawing shapes. | Useful when governance, reuse, reporting and impact analysis matter. |
| Diagrams as code | A diagramming approach where editable diagram source is stored as text and rendered into publication formats. | Good for reproducibility and version control; not automatically a governed model repository. |
| Deployment diagram | A model or view that shows where software runs and how runtime elements are placed on infrastructure or execution environments. | Distinguish logical deployment from detailed physical infrastructure. |
| Logical deployment view | A deployment view that shows runtime responsibilities and dependencies without fixing every physical implementation detail. | Do not treat it as proof of a particular region, subnet, product or node count. |
| Physical deployment view | A deployment view that shows concrete implementation placement, such as regions, zones, node pools, networks, runtime services and managed platform choices. | Use when the audience needs implementation, operations, capacity or resilience evidence. |
| Node (UML) | A computational resource that can host deployed artefacts, including Device and ExecutionEnvironment specialisations. | Do not confuse a UML node with a Kubernetes node unless the diagram is deliberately mapping between the two meanings. |
| Device (UML) | A UML node representing physical or virtual hardware that can host deployed artefacts or execution environments. | Do not use it for software responsibility by itself. |
| ExecutionEnvironment (UML) | A UML node representing a runtime environment that hosts deployed software, such as an application server, container runtime or database runtime. | Do not treat it as the same thing as a physical server. |
| Artifact (UML) | A physical piece of implementation, such as a deployable package, executable or container image. | In prose, keep the UML term clear even where the book otherwise uses British English. |
| Runtime environment | The execution setting in which software runs, such as a virtual machine, container platform, database platform or managed cloud service. | State whether the model is logical, platform-specific or physical. |
| Network topology | A view of network segments, connectivity, traffic paths and boundaries. | Use for connectivity and routing concerns, not application responsibility. |
| Cloud deployment model | A way of placing cloud services, such as public, private or hybrid cloud. | Use NIST terminology where a formal cloud definition is needed. |
| Kubernetes Deployment | A Kubernetes workload object that manages declarative updates and usually manages ReplicaSets. | Do not use the word deployment casually when a Kubernetes object is meant. |
| ReplicaSet (Kubernetes) | A Kubernetes workload object that maintains a stable set of replica Pods. | Usually let a Deployment manage ReplicaSets unless the design has a specific reason to manage them directly. |
| StatefulSet (Kubernetes) | A Kubernetes workload object for stateful applications that need stable identity, ordered behaviour or persistent storage behaviour. | Do not use Deployment for workloads that depend on stable Pod identity without explaining the design trade-off. |
| Pod (Kubernetes) | The basic Kubernetes runtime unit for one or more containers. | Treat Pods as replaceable runtime instances, not permanent servers. |
| Kubernetes Service | A Kubernetes abstraction that exposes stable network access to a logical set of endpoints, usually Pods. | Distinguish it from a business service, application service or C4 container. |
| Node (Kubernetes) | A worker machine in a Kubernetes cluster. | Do not confuse it with a UML node unless the diagram explicitly maps between notations. |
| Namespace (Kubernetes) | A Kubernetes mechanism for grouping resources within a cluster. | Do not present a namespace as a complete security boundary by itself. |
| Gateway API (Kubernetes) | A Kubernetes API family for extensible, role-oriented and protocol-aware traffic routing. | Show the relevant GatewayClass, Gateway and route resources when routing is the modelling concern. |
| HTTPRoute (Kubernetes Gateway API) | A Gateway API route resource that maps HTTP requests from a Gateway listener to backend endpoints such as Services. | Use it for HTTP routing rules rather than treating Gateway as the whole route. |
| Ingress (Kubernetes) | A Kubernetes API for exposing HTTP and HTTPS routes from outside a cluster to Services inside a cluster. | It remains generally available, but the Kubernetes project recommends Gateway API for new designs. |
| Capacity | The amount of work a design can handle within acceptable limits. | Name assumptions and indicators rather than saying the system has enough capacity. |
| Capacity headroom | Spare capacity kept above expected workload so the system can absorb peaks, failures or operational variation. | State the assumed peak and the reason for the reserve. |
| Scalability | The ability to increase capacity without redesigning the whole system. | Identify bottlenecks such as databases, connection pools, shared storage and external dependencies. |
| Autoscaling | Automatic capacity adjustment based on measured signals or declared policies. | State the scaling signal, limit and owner. |
| Horizontal scaling | Increasing capacity by adding more instances, replicas or nodes. | Check whether shared databases, queues or external dependencies can also handle the extra load. |
| Vertical scaling | Increasing capacity by giving an existing instance more CPU, memory, storage or input/output capacity. | Useful within limits, but it can create larger single points of failure. |
| Resource request (Kubernetes) | A declared amount of CPU or memory a container needs for scheduling. | Do not confuse it with a maximum limit. |
| Resource limit (Kubernetes) | A declared maximum amount of CPU or memory a container is allowed to use. | Limits can protect shared platforms, but incorrect values can cause throttling or failures. |
| Queue depth | The amount of work waiting in a queue or event stream. | Useful as a backlog and scaling signal when latency matters. |
| Immutable artifact | A built software artefact, such as a package or container image, that is promoted unchanged between environments. | Environment differences should come from configuration and secrets, not rebuilding the artefact. |
| Secret | Sensitive configuration value such as a password, token or key. | Manage separately from source code and deployable artefacts. |
| Availability | The ability of a system or service to be usable when needed. | Express expected availability in terms the audience can review, such as service hours, dependency assumptions and recovery behaviour. |
| Resilience | The ability to absorb, recover from or adapt to disruption while continuing to provide acceptable service. | Model failure modes and recovery paths, not only duplicate components. |
| Disaster recovery | The planned restoration of service after a serious disruption. | Include recovery objectives, responsibilities and failback, not only standby infrastructure. |
| Warm standby | A recovery pattern where a secondary environment is prepared and partially running but needs activation before it serves live traffic. | State what is already running, what must be activated and what data may need reconciliation. |
| Failover | The controlled movement of service from a failed or impaired environment to an alternate environment. | Identify the trigger, traffic route, dependency readiness and operational owner. |
| Failback | The controlled return of service from a recovery environment to the normal primary environment. | Include validation and reconciliation, not only traffic switching. |
| Data reconciliation | The comparison and correction of data after disruption, replication delay or recovery. | Needed when RPO, asynchronous replication or failed integrations may leave differences. |
| Backup | A separate recoverable copy of data or configuration kept for restore purposes. | Replication is not a backup by itself. |
| Recovery Time Objective (RTO) | The target maximum time to restore a service after disruption. | Define at first use in each chapter and avoid promising an RTO without supporting design and operations. |
| Recovery Point Objective (RPO) | The target maximum acceptable data loss measured as time. | Link to data replication, backup, restore and reconciliation design. |
| Observability | The ability to understand system behaviour from telemetry such as traces, metrics and logs. | Do not reduce it to dashboards; include instrumentation, collection, processing and ownership. |
| OpenTelemetry Collector | A vendor-neutral telemetry component that can receive, process and export traces, metrics and logs. | Show processing and export separately when they affect privacy, routing or operations. |
| Sensitive-data redaction | The removal or masking of sensitive values before data is stored, shared or analysed. | Apply before telemetry reaches broad observability stores when privacy or secrecy is a concern. |
| Observability backend | A system that stores, indexes or analyses telemetry for operational use. | Avoid naming a vendor unless the diagram question requires a specific product. |
| Dashboard | A visual operational view that presents selected measures, trends or states. | A dashboard is not a substitute for alerting, ownership or incident response. |
| Alert routing | The routing of alerts to the team or owner expected to act on them. | Include severity, ownership and actionability in detailed operational designs. |
| Service owner | The role accountable for the health, change and operational outcomes of a service. | Distinguish from the operations team that may monitor or respond across several services. |
| Trace | Telemetry that follows one request or transaction through multiple components. | Useful for runtime flow and dependency diagnosis. |
| Metric | Numeric telemetry measured over time. | Useful for service health, capacity, saturation and service-level monitoring. |
| Log | A timestamped event or message emitted by software or infrastructure. | Useful for investigation, but it needs retention, privacy and correlation rules. |
| Authentication | The act of establishing or proving the identity of a user, system, service or device. | Distinguish from authorisation, which decides what the authenticated subject may do. |
| Authorisation | The decision about whether a subject may perform an action on a resource under stated conditions. | Use British spelling in prose; preserve source titles such as OWASP Authorization Cheat Sheet when citing them. When ambiguity is possible, use access authorisation. |
| Access authorisation | A security permission decision about whether a user, service or device may perform an action on a resource under stated conditions. | Distinguish from business approval and payment-provider authorisation. |
| Business approval | A business decision or policy approval that allows an activity to proceed. | Do not treat it as the same thing as access authorisation, even when both are required. |
| Payment-provider authorisation | A transaction-level authorisation from a payment provider, payment network or similar external payment party. | Use only when the payment-provider decision is meant, not for general access control. |
| Security objective | A stated security property or outcome that the model is trying to protect. | Link it to an asset and threat scenario where possible. |
| Threat scenario | A concrete way a threat could cause harm to an asset or objective. | Keep it reviewable without turning it into exploit instructions. |
| Threat | A potential cause of harm to an asset, system, process or organisation. | Link threats to assets, flows, boundaries and mitigations rather than listing them abstractly. |
| Vulnerability | A weakness that could be exploited by a threat. | Do not use as a synonym for every risk or missing control. |
| Security control | A safeguard or countermeasure that reduces likelihood, impact or exposure. | Record the control intent, location, owner and evidence where practical. |
| Residual risk | Risk that remains after selected controls are applied. | Record as an open question or accepted exposure where it matters. |
| Threat model | A structured representation of assets, flows, trust boundaries, threats, mitigations and open questions. | It is not the same as penetration testing or a list of security products. |
| STRIDE | A threat-category mnemonic covering Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service and Elevation of Privilege. | Use as a review prompt, not as a complete security architecture by itself. |
| Attack tree | A tree-shaped model that shows alternative or combined paths to a harmful goal. | Keep branches concrete enough to review and avoid exploit instructions. |
| Policy decision point | The place or component that evaluates policy and decides whether an action should be allowed. | Distinguish from the place that enforces the decision. |
| Policy enforcement point | The place or component that applies an access decision at a boundary or service. | Make enforcement visible when the security question is about authorisation. |
| Data classification | The labelling of data according to sensitivity, handling needs or organisational policy. | Do not use colour as the only classification indicator. |
| Privacy modelling | Modelling data processing, purpose, access, sharing, retention and minimisation concerns that may create privacy risk. | Do not reduce privacy review to data classification alone. |
| Systems Modeling Language (SysML) | An OMG general-purpose modelling language for systems engineering and model-based systems engineering. | Use for requirements, structure, behaviour, analysis and verification traceability when that rigour is needed; do not use it merely to make a simple software diagram look formal. |
| Requirement traceability | The relationship between a requirement and the design, implementation or verification evidence that addresses it. | Keep the link reviewable; do not claim a requirement is satisfied without evidence. |
| Quality attribute scenario | A measurable account of how a system should respond to a stimulus in a stated environment. | Record the source, stimulus, environment, affected artefact, response and response measure. |
| Stakeholder need | An outcome or concern expressed from a stakeholder's perspective. | Refine it into testable requirements without disguising a preferred solution as the need. |
| Verification | Assessment of whether a specified requirement has been implemented correctly. | Distinguish it from validation, which asks whether the result meets stakeholder needs in context. |
| Verification case | A defined check, test, analysis or review used to evaluate whether a requirement has been addressed. | Keep distinct from the evidence produced by running the check. |
| Verification evidence | The result, record or artefact produced by a verification case. | Treat evidence as review support, not automatic proof. |
| Application landscape | A view of the major applications or software systems in an estate and their high-level relationships. | Use for estate understanding and rationalisation, not detailed process flow or interface catalogues. |
| Integration landscape | A view of how systems exchange information through APIs, events, files, messages, adapters or integration platforms. | Label the integration style where it matters; avoid vague "integrates with" arrows. |
| Architecture roadmap | A model of intended architecture change across current, transition and target states. | Treat it as an assumption-based planning view unless governance makes it a delivery commitment. |
| Current-state baseline | A dated, evidence-based view of the architecture relevant to a change decision. | State scope, ownership, constraints and assumptions; do not use `legacy` as a substitute for analysis. |
| Target architecture | An intended future architecture that supports stated outcomes under recorded assumptions. | Treat it as direction for review, not a guaranteed delivery commitment. |
| Transition architecture | A coherent intermediate architecture that can operate while change is incomplete. | Show coexistence, authority, temporary controls, support ownership and exit criteria. |
| Migration wave | A governed grouping of users, products, data, locations or capabilities intended to move together. | Record entry, exit, evidence, support and fallback criteria; a wave is not merely a calendar period. |
| Cutover | The controlled transfer of service, data or operational responsibility from one arrangement to another. | Show proceed or stop authority, verification, recoverable boundary and fallback where relevant. |
| Decommissioning | The governed retirement of an architecture element and its remaining data, interface, access, support and contractual obligations. | Removing a box from a target view is not evidence that retirement is complete. |
| Heat map | A view that overlays a rating such as risk, maturity, cost, pain or priority onto a stable structure. | State the scoring basis, date, owner and meaning of ratings; do not rely on colour alone. |
| Wardley map | A strategic map that relates user need, value-chain components, dependencies and component evolution. | Treat component positions as assumptions for discussion, not objective facts. |

## Terms requiring future decision

- Final distinction between `client` and `customer` in banking chapters
- Preferred use of `artefact` versus `artifact` in technical file names
- Final publication convention for `as-is` and `to-be`
