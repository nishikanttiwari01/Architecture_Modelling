# Chapter 11 Technical Review, 2026-07-01

## Scope

- Chapter: 11, Infrastructure and Deployment Modelling
- Manuscript: `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`
- HEAD reviewed: `99837319de0a9aa00358e83662fa3b7270e764b1`
- Review type: Technical accuracy

## Findings

| ID | Severity | Affected file / section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH11-TECH-01 | Critical | `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`, Kubernetes deployment; `FIG-11-03` source/spec | Manuscript says Deployment manages desired state and updates for replicated Pods, and the figure nests Pods directly inside Deployment. Kubernetes documentation states Deployments provide declarative updates for Pods and ReplicaSets, and ReplicaSets maintain replica Pods. | Correct prose and figure to show Deployment, ReplicaSet and Pod responsibilities. | Resolved, manuscript and `FIG-11-03` now show Deployment to ReplicaSet to Pod responsibility. |
| CH11-TECH-02 | Major | Kubernetes deployment source guidance and `FIG-11-03` | Current source requirements and figure teach Ingress only. Kubernetes documentation recommends Gateway API over Ingress and states Ingress is frozen while not removed. | Update source note, manuscript and figure to teach Gateway API as the current option, while explaining Ingress remains common and supported. | Resolved, Gateway API, Gateway and HTTPRoute are included; Ingress is explained as common and supported but frozen. |
| CH11-TECH-03 | Major | `FIG-11-02` source/spec | Operations tooling connects directly to the Order Database as routine operational access. | Route operational data access through a controlled administration mechanism, backup mechanism or restricted database administration access, and keep customer and operations paths distinct. | Resolved, operations now flow through Administration Gateway and Backup and DBA Access Point. |
| CH11-TECH-04 | Major | UML deployment section and source note | Chapter wording says a UML node is a computational resource or execution environment, which can imply node and execution environment are equivalent. | Tighten UML terms: Node, Device, ExecutionEnvironment, Artifact, deployment relationship and communication path. | Resolved, UML terms are separated in manuscript, glossary and UML source note. |
| CH11-TECH-05 | Major | Cloud architecture | Cloud responsibility boundaries are under-explained for IaaS, PaaS, SaaS, managed database/platform and managed Kubernetes. | Add vendor-neutral responsibility guidance focused on what the architecture team models, configures, secures, monitors and recovers. | Resolved, cloud responsibility guidance added. |
| CH11-TECH-06 | Major | Capacity and resilience guidance | Capacity, scalability, horizontal/vertical scaling, autoscaling and queue-driven scaling are only implied. | Add explicit capacity versus scalability guidance, including assumptions, indicators and likely bottlenecks. | Resolved, capacity and scalability section added with scaling and bottleneck guidance. |
| CH11-TECH-07 | Major | `FIG-11-05` source/spec and observability section | Observability is shown mainly as telemetry collectors to platform. It does not clearly show workload/store/event emission to collectors, processing/export, backend, alerting and operational consumer. | Strengthen telemetry chain in prose and figure. | Resolved, prose and `FIG-11-05` now show emitters, collectors, processing/export, backend and operations. |
| CH11-TECH-08 | Minor | `FIG-11-04` title | Title `Horizon Bank Hybrid Deployment View` is broad for a placement-oriented diagram. | Decide whether to rename to `Horizon Bank Hybrid Infrastructure and Placement View` and apply consistently if changed. | Resolved, title and filenames renamed consistently. |

## Notes

- Official Kubernetes source pages checked on 2026-07-01: Deployments, ReplicaSet, Service, Ingress and Gateway API.
- No chapter, diagram or review item may be marked `Approved` by Codex.
