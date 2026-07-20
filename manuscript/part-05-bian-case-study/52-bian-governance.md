---
title: "Deployment, Security, Resilience, Observability and Operations"
chapter: 52
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 52. Deployment, Security, Resilience, Observability and Operations

## Chapter purpose

Explain how Horizon Bank turns logical applications and interfaces into an operable architecture. The chapter connects deployment, identity, security, resilience, observability, incident response, recovery and service ownership without claiming unsupported physical products or numerical objectives.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish logical application, software service, deployment unit, runtime environment and infrastructure node;
- model deployment placement and trust without assuming that cloud, containers or internal networks are secure by default;
- trace a critical operation through applications, data, interfaces, external networks and supporting services;
- define useful observability from business outcomes, traces, metrics and logs;
- connect alerts, incidents, runbooks, recovery, reconciliation and accountable ownership; and
- identify evidence needed before assigning impact tolerances, service objectives, Recovery Time Objectives or Recovery Point Objectives.

## Prerequisites and dependencies

- Chapter 11: Infrastructure and Deployment Modelling
- Chapter 12: Security Modelling
- Chapter 29: Operations and Support
- Chapter 34: Full Bank Application and Integration Landscape
- Chapter 50: BIAN-Aligned Application, Software-Service and Team Boundaries
- Chapter 51: APIs, Events, Commands, Batch, Files, Workflow and External Networks

## Required models and artefacts

- `examples/horizon-bank/technology-resilience.md`
- `examples/horizon-bank/critical-operations.md`
- Logical application, interface, external-network and system-of-record catalogues
- Control and reconciliation catalogues
- Deployment, trust-boundary, observability, dependency and recovery views
- Operational ownership, service objectives, runbooks and exercise evidence

## Worked examples

- `HB-SCN-19 Recover Payment Service after Cyber Disruption`

## Source requirements

Security, observability, Kubernetes and operational-resilience claims use official sources. Horizon Bank deployment classifications and recovery choices are fictional author models. No architecture record invents a physical product, region, node count, impact tolerance, Recovery Time Objective (RTO) or Recovery Point Objective (RPO) [NIST-ZERO-TRUST-PV52] [OPENTELEMETRY-PV52-2026] [KUBERNETES-DEPLOYMENT-PV52-2026] [BCBS-RESILIENCE-PV52].

## The question this architecture answers

This architecture answers: **Where and how does a banking service run, how is access controlled, how do operators know its condition, and how is the customer outcome protected through disruption?**

A deployment diagram alone cannot answer the whole question. It can show placement and connectivity, but it does not establish data authority, security policy, incident ownership or recovery evidence. An operational architecture combines focused views and governed records.

## Who uses the operating architecture

Solution, infrastructure, cloud, data and security architects use it to design runtime placement and controls. Application-service owners, platform engineers and operations teams use it for monitoring, change and incident response. Business-service, control and resilience owners use it to set priorities, degraded modes and recovery evidence. Internal assurance functions use the trace to review whether stated outcomes are supported.

## Keep logical and physical levels separate

Horizon Bank's `HB-APP-*` records are logical applications. They define responsibility, owner, information relationships, interfaces, architecture state and qualitative resilience tier. They do not identify a vendor product, executable, database instance or runtime location.

| Element | Meaning | Example question |
|---|---|---|
| Logical application | Governed software responsibility in the estate | Which application owns payment orchestration? |
| Software service | Invokable software behaviour behind a contract | Which service validates and advances payment state? |
| Deployment unit | Independently built or released artefact | Which artefact can be promoted or rolled back? |
| Runtime instance | One executing copy of a deployment | How many healthy instances are serving now? |
| Runtime environment | Execution setting such as a virtual machine or container platform | Which controls and platform services apply? |
| Infrastructure node | Physical or virtual compute, network or storage resource | Where is the runtime placed and connected? |

One logical application can use several deployment units and data stores. One deployment unit can have many runtime instances. A shared platform can host several applications. These relationships need explicit IDs in a physical design; they must not be inferred from similar names.

## Deployment architecture begins with requirements

Before selecting placement, record:

- the critical operation and customer outcome;
- service hours, workload and latency evidence;
- authoritative data and consistency needs;
- trust boundaries, identities and information classification;
- external-network and supplier dependencies;
- failure modes and degraded operations;
- approved recovery and data-loss objectives;
- release, support and incident ownership; and
- jurisdiction, legal entity and data-location constraints.

An on-premises, public-cloud or hybrid label is not a design. Each can be secure or insecure, resilient or fragile. A hybrid design can retain a core processing application in a controlled environment while placing digital channels on a different platform, but the model must show identity, connectivity, latency, failure, data movement and operational ownership across the boundary.

## Environments and release flow

Development, test, pre-production, production and recovery environments serve different purposes. The model should show which artefact moves between them, which configuration changes, who approves promotion and which data may be used.

Promote an immutable artefact where feasible. Environment-specific configuration and secrets should be supplied through governed mechanisms rather than rebuilding the code. `HB-APP-089 Secrets and Cryptographic Key Management` protects secret and key lifecycles. `HB-CTRL-39 Technology Change and Release Control` governs change evidence, approval and rollback.

Production data should not be copied into lower environments without an approved purpose and protection. Test identities, keys, external endpoints and message profiles should be distinct. A pre-production success does not prove production capacity or external-network readiness unless the material differences are recorded.

## Container platforms are implementation choices

Kubernetes is one possible runtime platform. Its Pods, Deployments, StatefulSets, Services, Nodes and Gateway API resources have distinct meanings. A C4 container, logical application or Banking Industry Architecture Network (BIAN) Service Domain is not automatically one Kubernetes object [KUBERNETES-DEPLOYMENT-PV52-2026].

Use a Kubernetes Deployment for workloads whose instances can be replaced under that controller's semantics. Use StatefulSet only where stable identity, ordered behaviour or persistent-storage semantics are required. A Kubernetes Service supplies stable network access to selected endpoints; it is not a business service.

Horizon Bank has not selected Kubernetes for all applications. A physical design must justify cluster, namespace, workload, service networking, storage, identity, policy, capacity and recovery choices. The logical catalogue remains portable until those decisions are governed.

## Data placement and recovery

Application availability without authoritative data is not service recovery. For each store, record the data purpose, authority, consistency model, encryption and key dependency, replication, backup, restore, retention and reconciliation.

Replication provides another copy of current state. It is not automatically a backup because corruption or deletion may replicate. A backup is not adequate until restoration is tested. Recovery must also restore schema, configuration, keys, reference data and interface checkpoints at compatible versions.

RTO is the target maximum time to restore a service after disruption. RPO is the target maximum acceptable data loss measured as time. Neither value should be guessed by a technology team. Derive them from the critical operation, impact tolerance, legal and customer consequences, transaction behaviour, recovery capability and approved risk decision.

`HB-TECH-030 Backup, Recovery and Continuity Services Classification` keeps protected recovery copies, tested restore paths, dependency-aware recovery, failback and reconciliation in scope. Its current gap explicitly leaves service inventory, impact tolerances, RTOs and RPOs pending.

## Security follows identities and resources

Trust changes at internet, partner, workforce, service, platform, data-custody, administrative and recovery boundaries. Label the basis of each boundary. `internal` is not a security property.

NIST Special Publication 800-207 describes Zero Trust Architecture (ZTA) as removing implicit trust based only on network location or ownership and focusing protection on resources, identities and explicit access decisions [NIST-ZERO-TRUST-PV52]. Horizon Bank uses that as vendor-neutral guidance, not as a claim of compliance with a particular government profile.

A deployable service needs:

- a governed service identity;
- authenticated caller or workload identity;
- access authorisation at a policy enforcement point;
- least-privilege data and interface permissions;
- protected secrets and keys;
- encrypted and integrity-protected communication where required;
- approved software artefact and configuration provenance;
- audit evidence for material actions; and
- revocation, rotation and break-glass procedures.

`HB-APP-008 Customer Identity and Access Management`, `HB-APP-011 Workforce Identity Governance` and `HB-APP-089` have different subjects and lifecycles. `HB-CTRL-06 Consent, Mandate and Entitlement Enforcement`, `HB-CTRL-37 Workforce and Privileged Access Governance`, `HB-CTRL-38 Security Monitoring and Incident Response` and `HB-CTRL-39` provide complementary controls. A successful login does not prove transaction authority, and a service certificate does not prove business permission.

## Security telemetry and sensitive data

Security-relevant telemetry crosses another trust and privacy boundary. `HB-INT-097 Cryptographic Audit Event` publishes high-risk key and secret lifecycle activity from `HB-APP-089` to `HB-APP-085 Security Operations Platform`. The event should carry a protected reference, identity, action, outcome and time, not the secret itself.

`HB-INT-096 Security-Relevant Observability Event` sends a detection from `HB-APP-086 Enterprise Observability Platform` to security operations. The contract needs severity, evidence link, correlation and redaction rules. Security teams need enough context to act, but broad telemetry stores should not receive credentials, full payment messages or restricted investigation evidence.

## Resilience begins with the critical operation

Operational resilience is the ability to continue or restore an acceptable customer or market outcome through disruption. It is not a count of redundant servers. Basel Committee guidance connects critical operations with governance, dependency mapping, business continuity, incident management, third parties and resilient information and communication technology [BCBS-RESILIENCE-PV52].

Horizon Bank's critical-operation catalogue starts from outcomes such as:

- `HB-CRIT-02 Make a Time-Critical Payment`;
- `HB-CRIT-05 Clear and Settle Payment Obligations`;
- `HB-CRIT-18 Contain and Recover from a Material Cyber Incident`; and
- `HB-CRIT-19 Coordinate Enterprise Service Recovery`.

Trace each operation through people, processes, applications, data authorities, interfaces, external networks, facilities, suppliers and control-plane services. Identify single points of failure, common dependencies and resource contention. An application marked Tier 1 is only a qualitative classification until objectives and evidence are approved.

## Degraded operation is a business decision

Resilience design should consider whether work can queue, move to an alternate channel, use a restricted rail, switch to assisted processing or stop safely. The business and control owners decide what is acceptable.

For a payment service, accepting instructions while settlement is unavailable may increase customer and liquidity risk. A safe degraded mode needs visible status, capacity bounds, duplicate protection, cut-off handling, customer communication and a controlled release of queued work. `service available` is not true if requests disappear into an unobservable backlog.

## Dependency-aware recovery

Recovery sequence follows authority and dependency, not application number. A typical controlled sequence is:

1. establish incident command and business priorities;
2. contain the threat or failure and preserve evidence;
3. restore trusted workforce and service identities;
4. restore keys, secrets, network policy and time services;
5. recover authoritative data and configuration at compatible versions;
6. activate integration and external connectivity;
7. restore application behaviour in dependency order;
8. validate business state and control operation;
9. release restricted traffic gradually;
10. reconcile instructions, positions, accounting and external acknowledgements; and
11. communicate status, fail back where appropriate and retain evidence.

Failover is the controlled move to an alternate environment. Failback is the controlled return. Both require validation and reconciliation. Restoring a process is not enough if an external network still sees the old endpoint or a consumer replays already-settled work.

## Observability explains system behaviour

Observability is the ability to understand behaviour from telemetry and context. OpenTelemetry distinguishes traces, metrics and logs and separates instrumentation, collection, processing and export [OPENTELEMETRY-PV52-2026].

| Signal | Useful question | Payment example |
|---|---|---|
| Trace | Where did one request or transaction spend time or fail? | Follow one governed payment reference across orchestration and screening |
| Metric | Is workload, latency, error or saturation changing? | Accepted-payment rate, queue age or settlement break count |
| Log | What discrete action or decision occurred? | Route rejected with a governed reason and correlation reference |
| Business outcome | Is the customer or financial result being delivered? | Payments accepted but not reaching final or repairable status |

Business outcome monitoring is not another OpenTelemetry signal; it is the bank's governed interpretation of application, transaction, accounting and reconciliation evidence. A healthy processor-utilisation metric cannot prove that customer funds were posted correctly.

`HB-APP-086` collects and analyses telemetry and routes actionable alerts. `HB-TECH-028 Observability and Service Operations Classification` connects service-health visibility, alert routing, incidents, configuration and runbooks. The classification remains a target author model with service-level coverage and access gaps.

## From telemetry to action

An alert must be actionable. Define signal, threshold or condition, severity, affected service, business impact, owner, evidence and runbook. Suppress duplicates without hiding a spreading failure.

`HB-INT-098 Operational Alert to Incident` creates or updates an incident in `HB-APP-087 Information Technology Service Management`. The correlation key prevents a flood of duplicate incidents. `HB-APP-088 Configuration and Service Inventory` supplies service, owner and dependency context through `HB-INT-054 Service and Ownership Inventory`.

A Service-Level Objective (SLO) is a target for a measured service outcome over a stated period. Define the indicator, population, exclusions, measurement source and owner. Do not publish a percentage without workload and business evidence. Horizon Bank leaves quantitative SLOs pending rather than inventing numbers.

## Operational ownership and runbooks

`HB-ORG-123 Application Service Owner Role` is accountable for application-service health and change. Product, data and control owners retain their separate accountabilities. `HB-ORG-16 Technology Architecture, Engineering and Operations`, `HB-ORG-25 Cyber Security and Identity` and `HB-ORG-26 Operational Resilience` support different parts of the operating model.

A runbook should state trigger, authority, safety checks, dependencies, steps, expected evidence, rollback, escalation and reconciliation. It should use governed service and interface IDs. A list of shell commands without business checks is not a recovery runbook.

`HB-APP-090 Resilience Orchestration and Recovery` coordinates recovery tasks and evidence through `HB-INT-099 Recovery Workflow Handoff`. It does not decide which customer harm or financial exposure is acceptable. Business and resilience owners retain that decision.

## Worked recovery trace: payment service after cyber disruption

`HB-SCN-19 Recover Payment Service after Cyber Disruption` begins when a material cyber event threatens or disrupts payment processing. It ends when payment service is restored or restricted with verified identity, data integrity, reconciled transactions, customer communication and retained incident evidence.

1. `HB-APP-085` receives security evidence through `HB-INT-096` and `HB-INT-097`. `HB-CTRL-38` governs triage, containment and response.
2. Incident command assesses `HB-CRIT-02`, `HB-CRIT-18` and `HB-CRIT-19`. The business may restrict payment acceptance while evidence is incomplete.
3. Recovery uses protected identities and keys from `HB-APP-011` and `HB-APP-089`. Compromised credentials are not restored blindly.
4. `HB-APP-090` creates dependency-aware work through `HB-INT-099`; `HB-APP-087` records incident and action evidence.
5. Payment data under `HB-SOR-08` and settlement data under `HB-SOR-09` are restored or validated at compatible points. `HB-CTRL-40 Backup, Restore and Recovery Test` provides control evidence.
6. `HB-APP-075` to `HB-APP-079` are activated as required before domain traffic. External endpoints and participant status are checked.
7. `HB-APP-034`, `HB-APP-035` and `HB-APP-036` resume in controlled order under `HB-TECH-009 Payments Processing Classification`.
8. Traffic is released gradually. Duplicate keys, backlog age, screening state and settlement capacity are observed.
9. `HB-REC-012` and `HB-REC-014` compare accepted instructions, processing status, settlement and ledger evidence. Unknown outcomes enter investigation rather than automatic replay.
10. Customer communication uses governed source status. Failback and post-incident review retain decisions and residual risks.

The scenario does not state a region, clean-room product, RTO or RPO. Those remain gaps until physical design and owner approval provide evidence.

## Selecting the right operational model

Use a logical deployment view to show runtime responsibilities without fixing products. Use a physical deployment view for regions, zones, clusters, networks, nodes and stores. Use a trust-boundary view for identity and policy changes, an observability view for telemetry pipelines, a dependency map for critical operations and a recovery sequence for order and authority.

Do not combine all of these into one unreadable diagram. Use stable IDs to keep the views consistent.

## Current-to-target considerations

Many Horizon Bank domain and integration applications are current, while `HB-APP-086`, `HB-APP-088` and `HB-APP-090` are proposed target platforms. The transition should establish service ownership and dependency records before automating recovery. Telemetry onboarding should include redaction, retention, access and actionable alerts, not only agent installation.

Recovery automation starts with rehearsed, deterministic steps. High-risk business decisions and destructive actions retain explicit authority. Exercises should test external dependencies, stale data, unavailable identity, compromised keys, capacity loss, reconciliation and customer communication.

## Common mistakes

- Treating a logical application as one Pod, server or database.
- Calling cloud or an internal network secure without modelling identity and policy.
- Assuming replication is a backup.
- Inventing RTOs, RPOs or SLOs without business evidence.
- Restoring applications before identity, keys, data and connectivity.
- Monitoring infrastructure while ignoring customer and financial outcomes.
- Sending sensitive payloads into broad logs and traces.
- Creating alerts without an owner or action.
- Replaying unknown payment outcomes without reconciliation.
- Automating recovery before dependencies and authority are understood.
- Treating BIAN alignment as a deployment topology.
- Equating technical recovery with complete critical-operation recovery.

## Chapter summary

An operable bank architecture connects logical responsibility to physical placement, explicit identity, protected data, observable behaviour and dependency-aware recovery. Horizon Bank starts with critical operations, preserves authority through interfaces and stores, and uses qualitative resilience classifications until evidence supports numerical objectives. The cyber-disruption example shows that recovery includes containment, trusted identity, compatible data, controlled traffic, reconciliation, communication and failback, not only starting processes.

## Key takeaways

- Separate logical application, service, deployment, runtime and infrastructure.
- Derive placement and recovery from business and control needs.
- Grant no implicit trust from network location alone.
- Treat identity, keys, data and configuration as recovery dependencies.
- Monitor business outcomes as well as technical signals.
- Route actionable alerts to accountable owners.
- Reconcile unknown outcomes before replay.
- Approve impact tolerances and objectives from evidence, not convention.

## Practical exercise

Design an operational model for `HB-CRIT-20 Deliver Material Customer Communications` during loss of the primary notification path.

### Suggested answer criteria

A strong answer traces `HB-APP-022 Statement and Correspondence Management`, `HB-APP-073 Notification and Communications Hub`, `HB-INT-052 Customer Communication Request`, `HB-INT-094 Communication Delivery Event`, `HB-CTRL-43 Customer Statement and Communication Completeness` and `HB-REC-006 Customer Statement Completeness`. It distinguishes approved content, send, delivery and customer response. It includes identity, accessible fallback, capacity, pending-message recovery, duplicate prevention, service owner, observability and reconciliation. It leaves legal deadlines and numerical recovery objectives pending unless evidence is supplied.

## Review checklist

- [ ] Logical and physical elements are distinguished.
- [ ] Critical operation and customer outcome drive the design.
- [ ] Identity, policy enforcement, secrets and keys are explicit.
- [ ] Data authority, replication, backup, restore and reconciliation are separate.
- [ ] External-network and supplier dependencies are shown.
- [ ] Degraded operation has a business and control decision.
- [ ] Traces, metrics, logs and business outcomes have defined purposes.
- [ ] Telemetry redaction, access and retention are governed.
- [ ] Alerts have severity, owner, evidence and runbook.
- [ ] Incident, recovery, failback and reconciliation are connected.
- [ ] RTO, RPO, SLO and impact-tolerance claims have evidence or an explicit gap.
- [ ] No BIAN Service Domain is presented as a deployment unit.

## References and source notes

- [BIAN-14-MAPPING-PV49-52]
- [NIST-ZERO-TRUST-PV52]
- [OPENTELEMETRY-PV52-2026]
- [KUBERNETES-DEPLOYMENT-PV52-2026]
- [BCBS-RESILIENCE-PV52]

## Deferred work

No diagram source is created in this pass. Physical environments, products, regions, zones, deployment units, stores, service identities, network rules, supplier services, runbooks, quantitative workload evidence, impact tolerances, SLOs, RTOs and RPOs remain governed gaps. These must be added through approved physical-design and operational-governance work rather than inferred from the logical catalogue.
