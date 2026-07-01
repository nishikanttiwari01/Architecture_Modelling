# Chapter 11 Quality Gate: Infrastructure and Deployment Modelling

- **Date:** 2026-07-01
- **Chapter status:** Ready for Author Approval
- **Diagram status:** `FIG-11-01` through `FIG-11-06` remain `Review`, not `Approved`.
- **Gate decision:** Pass
- **Final score:** 9.1

## Scorecard

| Category | Score | Evidence |
|---|---:|---|
| Scope coverage | 9.1 | Covers deployment views, infrastructure views, logical versus physical deployment, UML and C4 deployment diagrams, network topology, cloud responsibility, Kubernetes, capacity and scalability, environments, resilience, disaster recovery, observability and practical diagram tooling. |
| Technical accuracy | 9.1 | Kubernetes Deployment, ReplicaSet, Pod, Service, StatefulSet, Gateway API and Ingress wording was checked against current Kubernetes documentation. Cloud responsibility and resilience guidance separates fact, interpretation and modelling recommendation. |
| Beginner comprehension | 9.1 | Adds clearer prerequisites, a logical-versus-physical comparison table, an Online Store worked example, Kubernetes concept table, cloud responsibility table, capacity table, environment guidance and six captioned figures with accessibility text. |
| Educational flow | 9.0 | Moves from placement and topology to Kubernetes, cloud, capacity, environments, resilience, observability and tool practice, then closes with comparison, mistakes and exercises. |
| Diagram quality | 9.0 | `FIG-11-01` through `FIG-11-06` have specifications, PlantUML sources, SVG exports and PNG previews. Affected figures were rerendered and visually inspected. Wider figures remain flagged for final page-layout review. |
| Source and copyright discipline | 9.2 | Uses official or primary sources, records current Kubernetes and OpenTelemetry checks, records NIST SP 800-34 Revision 1 as historical official guidance used informatively, and uses original teaching diagrams. |
| Consistency with book | 9.2 | Uses the Simple Online Store and Horizon Bank examples consistently and preserves terminology from Chapters 4, 5 and 10. |
| Review readiness | 9.0 | Technical, beginner, consistency and final review records exist, all critical and major findings are resolved, and repository validations pass. |

Average: 9.1. No category is below 8.5.

## Figure Assessment

| Figure | Specification | Source | SVG | PNG | Status | Assessment |
|---|---|---|---|---|---|---|
| `FIG-11-01` | Present | Present | Present | Present | Review | UML deployment teaching view remains valid and registered. |
| `FIG-11-02` | Present | Present | Present | Present | Review | Network topology view separates internet, edge, application and data zones and avoids routine operations-to-database access. |
| `FIG-11-03` | Present | Present, rerendered | Present, rerendered | Present, rerendered | Review | Shows Gateway API, Services, Deployments, ReplicaSets and Pods. It states that StatefulSet is omitted for beginner readability and should be used when stable identity or persistent state behaviour is required. |
| `FIG-11-04` | Present | Present | Present | Present | Review | Hybrid infrastructure and placement view matches the renamed specification and register entry. |
| `FIG-11-05` | Present, updated | Present, rerendered | Present, rerendered | Present, rerendered | Review | Now shows one warm-standby scenario with failover trigger, dependency readiness, failback, data reconciliation, separate backup and explicit resilience cautions. |
| `FIG-11-06` | Present, new | Present, new | Present, new | Present, new | Review | New observability view shows Horizon Bank payment systems, traces, metrics, logs, OpenTelemetry Collector, filtering and sensitive-data redaction, observability backends, dashboards, alert routing, Operations Team, Service Owner and the six required payment indicators. |

All six Chapter 11 figures are present and remain at `Review`.

## Checks Run

| Check | Result |
|---|---|
| `python scripts/check-structure.py` | Pass |
| `python scripts/check-links.py` | Pass |
| `python scripts/check-terminology.py` | Pass |
| `python scripts/validate-diagrams.py` | Pass |
| `python scripts/check-diagram-register.py` | Pass |
| `python scripts/word-count.py` | Pass, Chapter 11 word count 7,550 |
| `python scripts/build-book.py` | Pass |

## Visual Review Notes

- `FIG-11-03` has no clipped text or overlapping labels. Arrow direction correctly shows Gateway API routing, Deployment to ReplicaSet and ReplicaSet to Pods.
- `FIG-11-05` has no clipped text. It is a wide resilience view, so final book-page layout should confirm whether it needs full-width placement.
- `FIG-11-06` has no clipped text or unreadable labels in the rendered PNG preview. It remains a wide left-to-right observability flow, so final page layout should confirm whether it needs full-width placement.

## Source Review

- Current Kubernetes guidance was checked against official Kubernetes documentation on 2026-07-01.
- OpenTelemetry Collector and signal wording was checked against official OpenTelemetry documentation on 2026-07-01.
- NIST SP 800-34 Revision 1 is recorded as historical official NIST guidance used informatively, not as a current banking regulation or unqualified current normative source.
- Infrastructure diagram tooling and icon-library guidance is supported by a new source note and source-register entry.

## Remaining Risks

- Final publication layout must still check wide Chapter 11 diagrams at the actual page size.
- Provider icon-library reuse terms should be checked separately before any provider icons are copied into publication assets.

## Decision

Chapter 11 is `Ready for Author Approval`. The final quality score is 9.1, all six figures are present, all validations pass, and `FIG-11-01` through `FIG-11-06` remain at `Review`, not `Approved`.
