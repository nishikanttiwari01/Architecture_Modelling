# Chapter 11 Quality Gate: Infrastructure and Deployment Modelling

## Gate summary

- **Chapter:** 11, Infrastructure and Deployment Modelling
- **Manuscript:** `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`
- **Status:** Ready for Author Approval
- **Current gate:** Chapter 11 has complete prose, source notes, registered source keys, glossary coverage, diagram specifications, PlantUML sources, SVG exports, PNG previews, manuscript figure references, visual review and repository checks.
- **Final quality score:** 9.0
- **Diagram status:** `FIG-11-01` through `FIG-11-05` remain `Review`, not `Approved`.

## Scorecard

| Category | Score | Evidence |
|---|---:|---|
| Scope coverage | 9.0 | Covers deployment views, infrastructure views, UML and C4 deployment diagrams, network topology, cloud architecture, Kubernetes deployment, environment views, availability, resilience, disaster recovery and observability. |
| Technical accuracy | 9.0 | Uses `[OMG-UML]`, `[C4-OFFICIAL]`, `[NIST-SP-800-145]`, `[KUBERNETES-DOCS-2026]`, `[AWS-WA-RELIABILITY-2026]`, `[NIST-SP-800-34R1]` and `[OPENTELEMETRY-DOCS-2026]`. |
| Beginner comprehension | 9.0 | Explains each model through a question, plain-language purpose, simple Online Store examples, Horizon Bank examples, captions, reading guidance and accessibility text. |
| Educational flow | 8.9 | Moves from placement and topology to Kubernetes, cloud, environments, resilience, recovery and observability, then closes with comparison, mistakes and exercise. |
| Diagram quality | 8.9 | Five figures render to SVG and PNG, use labelled relationships, avoid colour-only meaning and keep scope focused. Wider infrastructure figures remain marked for final page-layout review. |
| Source and copyright discipline | 9.1 | Uses official or primary sources, paraphrases source material and uses original teaching diagrams. |
| Repository tracking | 9.1 | `STATUS.md`, `RESUME.md`, `CHANGELOG.md`, `DIAGRAM_REGISTER.md`, the chapter manuscript and this gate file are updated. |

Average score: 9.0

No category is below 8.5.

## Required gate checks

| Check | Result | Evidence |
|---|---|---|
| Required sections complete | Pass | Chapter includes purpose, outcomes, prerequisites, artefacts, examples, source requirements, main sections, checklist and references. |
| Deployment and infrastructure distinction | Pass | Chapter distinguishes runtime placement from platform, network, environment, resilience and operations concerns. |
| UML and C4 deployment guidance | Pass | Chapter explains UML nodes and artefacts, and distinguishes C4 containers from Docker containers. |
| Network topology guidance | Pass | Chapter distinguishes zones and traffic paths from process flow and firewall rule inventories. |
| Cloud guidance | Pass | Chapter uses NIST cloud terminology and keeps provider-specific guidance interpretive. |
| Kubernetes guidance | Pass | Chapter distinguishes Kubernetes Deployment, Pod, Service, Node, Namespace and Ingress. |
| Resilience and disaster recovery guidance | Pass | Chapter defines RTO and RPO as objectives, not guarantees, and includes dependencies, replication, failover and ownership. |
| Observability guidance | Pass | Chapter covers traces, metrics, logs, instrumentation, collection, processing, export, alerting and ownership. |
| Diagrams registered | Pass | `DIAGRAM_REGISTER.md` includes `FIG-11-01` through `FIG-11-05` at `Review`. |
| Diagrams rendered | Pass | SVG exports and PNG previews exist for all five Chapter 11 figures. |
| Diagram visual review | Pass | PNG previews were inspected for clipping, overlap, arrow direction, readable labels, colour dependence and page-width readability. |
| Repository checks | Pass | `check-structure.py`, `check-links.py`, `check-terminology.py`, `validate-diagrams.py`, `check-diagram-register.py` and `word-count.py` completed with exit code 0 on 2026-06-30. |

## Figure review notes

`FIG-11-01` is a UML deployment teaching view. Runtime nodes, deployed artefacts and external provider systems are distinct. The view is wide but readable, with no clipped text or colour-only meaning.

`FIG-11-02` is a network topology teaching view. It separates internet, edge, application, data and operations paths. There is minor line crossing around operations and data access, but labels remain readable and the topology concern is clear.

`FIG-11-03` is a Kubernetes deployment teaching view. It explicitly labels Ingress, Service, Deployment and Pod objects, and keeps the managed database and provider systems outside the cluster. The figure is wide but readable at SVG resolution.

`FIG-11-04` is a Horizon Bank hybrid deployment view. It separates cloud platform, controlled integration and retained core-banking boundaries without implying that the Core Deposit System is cloud-native.

`FIG-11-05` is a payment resilience view. It distinguishes normal traffic from replication and recovery paths using line style plus labels. It keeps RTO, RPO, observability, operations ownership and the retained core dependency visible.

## Render and visual validation record

| Figure ID | SVG export | PNG preview | Visual result |
|---|---|---|---|
| `FIG-11-01` | Present | Present | Pass, clear runtime placement and external systems. |
| `FIG-11-02` | Present | Present | Pass, zones and allowed paths are readable. |
| `FIG-11-03` | Present | Present | Pass, Kubernetes object types are explicit. |
| `FIG-11-04` | Present | Present | Pass, hybrid placement boundaries are clear. |
| `FIG-11-05` | Present | Present | Pass, normal, replication and recovery paths are distinguishable. |

## Remaining risks

- Final book-page layout review remains pending for all Chapter 11 diagrams because several figures are wider than simple conceptual figures.
- Later Chapters 20 and 49 should reuse Chapter 11 terminology consistently when they cover infrastructure and operational architecture in more depth.
- Chapter 12 should reuse the Chapter 11 topology and boundary vocabulary when introducing security modelling, without retrofitting Chapter 11 into a full threat model.

## Gate decision

Chapter 11 is `Ready for Author Approval`. The final quality score is 9.0, no category is below 8.5, all five figures render to SVG and PNG, source notes are recorded, repository checks pass and `FIG-11-01` through `FIG-11-05` remain at `Review`.
