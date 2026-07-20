---
title: "BIAN-Aligned Application, Software-Service and Team Boundaries"
chapter: 50
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 50. BIAN-Aligned Application, Software-Service and Team Boundaries

## Chapter purpose

Explain how Horizon Bank turns business and Banking Industry Architecture Network (BIAN) responsibilities into defensible application, software-service, deployment and team boundaries. The chapter keeps these boundaries separate, then shows how they can be aligned without assuming a one-to-one relationship.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish a BIAN Service Domain, logical application, software service, deployment unit and team;
- use business lifecycle, information authority, consistency, security, scale, change and operational factors to propose boundaries;
- recognise valid one-to-many and many-to-one mappings;
- assign business, product, data, control, application-service and operational accountability without inventing one universal owner;
- assess a proposed service split against end-to-end behaviour and failure; and
- avoid a distributed monolith disguised as BIAN alignment.

## Prerequisites and dependencies

- Chapter 10: Domain and Event Modelling
- Chapter 34: Full Bank Application and Integration Landscape
- Chapter 49: BIAN Mapping Method and Full-Stack Traceability

## Required models and artefacts

- Governed domain, capability, process and organisation catalogues
- `examples/horizon-bank/applications.md`
- `examples/horizon-bank/interfaces.md`
- Data-domain and system-of-record catalogues
- Control, critical-operation and technology/resilience catalogues
- A boundary decision record with alternatives and consequences

## Worked examples

- Payment initiation, orchestration, clearing, settlement and investigation across `HB-APP-033` to `HB-APP-039`

## Source requirements

BIAN concepts use official BIAN sources. The Horizon Bank logical estate and all proposed implementation choices are fictional author models. BIAN material can inform responsibility boundaries, but it does not establish the bank's physical application, service, database, deployment or team structure [BIAN-14-MAPPING-PV49-52].

## The question this architecture answers

This architecture answers: **Which responsibilities should change, run, scale, recover and be owned together, and which should remain separate?**

The question cannot be answered by counting boxes in the BIAN Service Landscape. A responsibility boundary is semantic. An application boundary is a governed logical estate choice. A software-service boundary is an implementation choice. A deployment boundary controls release and runtime placement. A team boundary distributes people and decision rights. They influence one another, but none automatically determines the others.

## Who uses boundary decisions

Business, enterprise and solution architects use boundary decisions to preserve responsibility and target-state coherence. Software, data, integration, security and resilience practitioners test whether the proposed split can work safely. Product, data, control and application-service owners confirm decision rights. Delivery and operations leads use the same decision to define change, support and escalation without assuming that their team boundary is the business boundary.

## Five boundaries that must not be confused

| Boundary | Plain-language meaning | Main question |
|---|---|---|
| BIAN Service Domain | A logical banking responsibility in the BIAN reference model | What banking purpose and lifecycle are controlled? |
| Logical application | A governed software responsibility in the enterprise estate | Which coherent application responsibility is owned and managed over time? |
| Software service | An invokable unit of software behaviour behind a contract | Which runtime behaviour and state can be changed with controlled coupling? |
| Deployment unit | An artefact or runtime unit released and placed independently | What can be built, released, scaled, isolated and recovered independently? |
| Team | A group of people with agreed decision rights and work | Who designs, changes, operates or assures the responsibility? |

One logical application can contain several software services. Several logical applications can be implemented by a packaged platform. One service can have several replicas. One team can own several related services. Several teams can contribute to one application under explicit component and operational ownership.

BIAN's reference semantics remain useful precisely because they do not force these choices. The BIAN Practitioner Guide relates Service Domains to application modules as a design aid, but Horizon Bank still evaluates its own lifecycle, authority and implementation constraints [BIAN-14-MAPPING-PV49-52].

## Start with responsibility, not technology

Begin with a capability and process responsibility. Describe the business state it controls, its beginning and end, policies, invariants, information and accountable owner. Then identify interactions with other responsibilities.

For example, payment initiation captures and validates a customer's instruction. Payment clearing exchanges that instruction with a clearing mechanism. Settlement controls the discharge and financial position. Investigation handles an exception or enquiry. These behaviours participate in one customer outcome, but their authority, external dependencies and operational clocks differ.

Starting with a preferred platform usually reverses the reasoning. A proposal such as `one microservice per Service Domain` gives a box count before it understands transactions, data, failure or ownership.

## Boundary factors

No single factor decides a boundary. The architect records the evidence and trade-offs across several lenses.

### Business purpose and lifecycle

Keep behaviour together when it controls one coherent business state and changes under the same policies. Separate behaviour when it owns a materially different lifecycle or outcome.

`HB-APP-033 Payment Initiation Service` and `HB-APP-036 Settlement and Nostro Management` both support `HB-VS-04 Execute and Settle Transaction`, but they control different states. A captured instruction and a settled correspondent position should not be made indistinguishable for convenience.

### Information authority and consistency

Identify which application is authoritative for each purpose and lifecycle stage. `HB-SOR-08 Payment Instruction and Processing Authority` differs from `HB-SOR-09 Settlement and Correspondent Position Authority`. Separate authorities may exchange identifiers and facts, but they should not both silently update the same authoritative state.

Keep rules requiring immediate consistency within an appropriate transaction boundary. Split only when the business can tolerate an explicit intermediate state, asynchronous completion or compensation. Eventual consistency is not a general licence to expose customers to contradictory balances.

### Security, privacy and control

Different information classifications, access models, segregation requirements or control ownership can justify separation. The card-fraud decision in `HB-APP-043 Card Fraud Decisioning` and the restricted evidence in `HB-APP-044 Card Disputes and Chargebacks` need narrower access than a general channel view.

Security separation must have enforcement and operational evidence. Creating another network namespace without distinct identity, policy or ownership does not establish a meaningful trust boundary.

### Change, coupling and reuse

Group behaviour that changes together for the same business reason. Separate behaviour when independent change is valuable and contracts can remain stable. Reuse is strongest for genuinely common capability, not for superficially similar code.

An Application Programming Interface (API) exposes a contract; it does not determine the boundary or own the behaviour behind it.

`HB-APP-075 API Management Platform` is a shared platform because publishing, policy enforcement and developer access are common concerns. It must not absorb payment validation or credit policy merely because many applications call through it.

### Scale, latency and workload

A service may need independent scaling when its workload profile differs materially. Card authorisation is time-sensitive and high-frequency; end-of-day regulatory batches have a different operating pattern. This can support separate deployment, but only after state, contract and failure implications are understood.

Avoid using expected scale as unsupported precision. Horizon Bank records qualitative resilience tiers and gaps until measured workload and approved service objectives exist.

### Resilience and operations

Ask whether the responsibility needs a distinct recovery sequence, fault-containment boundary, support skill or external coordination path. `HB-CRIT-02 Make a Time-Critical Payment` depends on identity, entitlement, screening, routing, clearing, settlement, keys and external networks. A boundary that can be deployed independently but cannot be restored in dependency order is not operationally independent.

Operational ownership includes monitoring, alert response, incident command, reconciliation, recovery and change. It is broader than `the team wrote the code`.

### Legacy and commercial constraints

A retained core or vendor platform may implement several logical applications in one product. That is not a modelling failure if logical responsibilities, authorities and interfaces remain visible. Conversely, several products may jointly implement one logical application during transition.

The model should state the constraint rather than rename a legacy system after a Service Domain. Chapter 53 covers the transition architecture needed to change such boundaries safely.

## A practical boundary decision method

Use a boundary decision record for each material split or merge.

1. Name the governed responsibility and scenario.
2. Identify the authoritative business state and owner.
3. List consistency rules that must hold immediately.
4. Classify data and access needs.
5. Record consumers, contracts and failure expectations.
6. Describe workload, latency and recovery evidence.
7. Compare at least `keep together`, `split logically` and `split deployment` alternatives.
8. Assign business, data, control, application-service and operational decision rights.
9. Walk the normal, duplicate, timeout, partial-failure and recovery paths.
10. Record the choice, consequences, measures and re-evaluation trigger.

The method often produces a logical separation before a physical one. A modular boundary inside one deployable application can be the correct first step when data coupling or operational maturity makes distributed deployment unsafe.

## Common mapping patterns

### One Service Domain candidate to several applications

A logical responsibility may be distributed across channel, system-of-record, decision and operational applications. The mapping should identify which part each application performs. It should not call every participant an implementation of the complete Service Domain.

### Several Service Domain candidates to one application

A packaged application or retained core can support several responsibilities. Keep the candidate relationships many-to-one and expose internal authority in a function matrix. This allows later rationalisation without pretending the package has already been decomposed.

### One logical application to several software services

A target application can contain several services where independent release, load or fault isolation is justified. Those services still share the application's accountable service owner and architecture record unless the governance model creates separate logical applications.

### Several logical applications on one platform

Shared workflow, database, integration or runtime technology can host several logical applications. Platform ownership and tenant boundaries must be explicit. Shared infrastructure does not merge business responsibility.

### One team to several related applications

A stable group may own a coherent set of related applications, especially where demand is modest and the knowledge overlaps. This can reduce hand-offs. It should not create an unreviewable `payments team` with every responsibility from channel to ledger.

### Several teams contributing to one application

Large applications may have component owners, an application-service owner and an operations function. Decision rights, integration testing and incident accountability must be explicit. Multiple contributors do not remove the need for one accountable application-service owner.

## Ownership is multidimensional

Horizon Bank separates ownership roles because they answer different questions:

- `HB-ORG-121 Product Owner Role` is accountable for product outcomes and lifecycle choices;
- `HB-ORG-122 Data Owner Role` is accountable for governed information meaning and use;
- `HB-ORG-123 Application Service Owner Role` is accountable for application-service health and change; and
- `HB-ORG-124 Control Owner Role` is accountable for a control's design, operation and evidence.

Operational units add further responsibilities. `HB-ORG-28 Payment and Card Operations` handles transaction operations, while `HB-ORG-16 Technology Architecture, Engineering and Operations` and `HB-ORG-25 Cyber Security and Identity` operate and control shared technology. `HB-ORG-24 Strategy, Architecture and Transformation` governs the target model.

These records do not yet define delivery teams. A future team catalogue must record mission, owned applications or services, on-call responsibility, skills, dependencies and escalation. It should not derive a team name by copying a Service Domain label.

## Worked boundary assessment: payments

Horizon Bank's payment estate deliberately contains several logical applications:

| Application | Controlled responsibility | Boundary evidence |
|---|---|---|
| `HB-APP-033 Payment Initiation Service` | Capture and initial instruction state | Channel-facing contracts and customer context |
| `HB-APP-034 Payment Orchestration` | End-to-end processing state and coordination | Cross-step lifecycle and exception status |
| `HB-APP-035 Payment Routing and Clearing` | Route selection and clearing exchange | Rail rules and external clearing dependencies |
| `HB-APP-036 Settlement and Nostro Management` | Settlement obligation and correspondent position | Financial position, cut-off and reconciliation |
| `HB-APP-037 Payment Investigations and Exceptions` | Investigation case and repair | Human evidence, external enquiry and variable path |
| `HB-APP-038 Correspondent Banking Management` | Correspondent relationship and exchange | Counterparty, account and network boundary |
| `HB-APP-039 Foreign Exchange Pricing and Booking` | Customer foreign-exchange quote and deal | Price authority, currency legs and treasury hand-off |

This is a logical estate, not a claim of seven microservices. A possible implementation could keep initiation and orchestration as modules in one deployable application while preserving their responsibilities. Routing might use separate adapter services for different rails, but the governed logical application remains `HB-APP-035` until lifecycle or ownership justifies a catalogue change. Settlement could use a retained platform with several runtime processes because its state and recovery requirements differ.

The split must be tested through `HB-SCN-02 Execute Cross-Border Payment` and `HB-SCN-09 Execute an Immediate Domestic Payment`. `HB-INT-036 Accepted Payment Command` passes from `HB-APP-033 Payment Initiation Service` to `HB-APP-034 Payment Orchestration`. Routing begins at `HB-INT-037 Payment Clearing Instruction`, which passes from `HB-APP-034` to `HB-APP-035 Payment Routing and Clearing`. The command needs an idempotency key, governed payment reference and acceptance response. `HB-INT-066 Intraday Settlement Position Event` publishes a settlement-position fact to liquidity management. These contracts show where immediate consistency ends and observable asynchronous state begins.

The external-network boundary matters. `HB-EXT-001` to `HB-EXT-005` represent distinct clearing, messaging and correspondent connectivity. Adapters can isolate message profiles and credentials, but they should not invent business status that belongs to `HB-APP-034`, `HB-APP-035` or `HB-APP-036`.

The ownership design also remains plural. The payments product owner sets service outcomes. Payments and settlement operations manage transaction flows and exceptions. Application-service owners manage software health. Finance owns accounting and reconciliation controls. Cyber security owns key controls. A single delivery team may coordinate several of these people, but it does not inherit every accountability.

## Avoiding a distributed monolith

A distributed monolith has many deployable parts but cannot change or recover them independently. Typical signs include synchronous call chains for every step, shared database tables, coordinated releases, circular dependencies, unclear authority and one incident requiring all teams.

Reduce this risk by:

- assigning each authoritative state to one application responsibility;
- using explicit contracts and stable identifiers;
- keeping immediate invariants within a suitable boundary;
- publishing facts only after the authoritative state change is durable;
- designing timeout, duplicate and replay behaviour;
- avoiding shared-database writes across services;
- testing partial failure and dependency loss; and
- measuring whether independent release and recovery are real.

An event platform does not remove coupling if every consumer must deploy for each producer change. An Application Programming Interface (API) gateway does not create autonomy if all calls depend on one shared transaction.

## When to use these boundary models

Use boundary analysis when defining a target application, decomposing a legacy platform, assigning data authority, proposing independently deployable services, reorganising ownership or reviewing operational risk. Use a logical application landscape for estate decisions, a C4 container or component view for software structure, a sequence or event-flow view for runtime coupling and a deployment view for physical placement.

Do not use a BIAN Service Landscape view as a deployment diagram. Do not use an organisation chart as proof of software modularity. Do not create physical services merely to make the application landscape look aligned.

## Current-to-target considerations

The Horizon Bank application catalogue includes current and target logical applications. Target integration and operational platforms such as `HB-APP-075`, `HB-APP-076`, `HB-APP-082`, `HB-APP-083`, `HB-APP-086`, `HB-APP-088` and `HB-APP-090` do not justify immediate decomposition of every domain application.

Establish contracts, authority, telemetry and ownership before increasing deployment independence. During coexistence, record which implementation owns each instance, how identifiers cross the boundary, how data is reconciled and which component can be retired. Chapter 53 develops this transition method.

## Common mistakes

- Defining one microservice for every Service Domain.
- Renaming a legacy module after BIAN without changing responsibility.
- Treating a logical application as one deployable process.
- Splitting data writes while leaving one hidden transaction.
- Using asynchronous messaging without an authoritative state or duplicate policy.
- Creating a shared platform that owns domain decisions.
- Assuming a namespace or subnet is a sufficient security boundary.
- Assigning product, data, control and service ownership to one generic team.
- Optimising for independent deployment without independent recovery.
- Drawing a target decomposition without a coexistence and reconciliation plan.

## Chapter summary

BIAN alignment begins with banking responsibility, but implementation boundaries require additional decisions. Horizon Bank separates logical applications where lifecycle, authority and operations differ, then evaluates software-service, deployment and team boundaries using consistency, security, change, scale, resilience and ownership evidence. The payment example demonstrates a many-to-many architecture: several applications support an end-to-end outcome, one application may contain several services, and accountability crosses business and technology roles.

## Key takeaways

- Service Domain, application, service, deployment and team are different boundaries.
- Start with controlled business state and lifecycle.
- Protect one authority for each purpose and lifecycle stage.
- Keep immediate invariants inside an appropriate consistency boundary.
- Treat independent recovery as seriously as independent release.
- Expect valid one-to-many and many-to-one mappings.
- Assign product, data, control, service and operations accountability explicitly.
- Decompose only when the evidence justifies the extra distributed-system cost.

## Practical exercise

Review whether `HB-APP-048 Trade Finance Processing` should become one service, several services or a modular application for `HB-SCN-03 Issue and Settle Trade Instrument`.

### Suggested answer criteria

A strong answer considers instrument issuance, amendments, document examination, discrepancy, contingent exposure, claims, financing, settlement and closure. It identifies `HB-SOR-13 Trade Finance Instrument Authority`, `HB-DATA-07`, `HB-INT-047`, `HB-INT-048` and `HB-INT-073`, accounting and reconciliation, `HB-CTRL-04`, `HB-CTRL-21` and `HB-CRIT-11`. It compares consistency, restricted evidence, external-message timing, specialist ownership and recovery. It may recommend modular boundaries before separate deployment. It does not create one service per guessed BIAN Service Domain.

## Review checklist

- [ ] The business responsibility and lifecycle are explicit.
- [ ] Service Domain, application, service, deployment and team are distinguished.
- [ ] Information authority is assigned by purpose.
- [ ] Immediate consistency rules are identified.
- [ ] Security and control boundaries have enforcement evidence.
- [ ] Change, scale and workload claims have evidence or a gap.
- [ ] Normal, duplicate, timeout and recovery paths were assessed.
- [ ] Product, data, control, service and operational owners are explicit.
- [ ] One-to-many and many-to-one relationships are retained.
- [ ] Transition and coexistence effects are recorded.
- [ ] No one-to-one BIAN implementation assumption is present.

## References and source notes

- [BIAN-14-MAPPING-PV49-52]

## Deferred work

No diagram source is created in this pass. Horizon Bank has no governed software-service, deployment-unit or delivery-team catalogue yet. Physical product modules, service contracts, database boundaries, runtime topology, team missions and quantitative workload evidence remain explicit gaps for later design and governance.
