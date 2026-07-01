# Chapter 11 Consistency Review, 2026-07-01

## Scope

- Chapter: 11, Infrastructure and Deployment Modelling
- Manuscript: `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`
- HEAD reviewed: `99837319de0a9aa00358e83662fa3b7270e764b1`
- Review type: Cross-chapter, examples and repository consistency

## Findings

| ID | Severity | Affected file / section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH11-CONS-01 | Major | Chapter prerequisites and cross-chapter dependencies | Chapter 11 builds on Chapter 4 UML deployment and Chapter 5 C4 deployment, but lists only Chapter 10. | Correct prerequisites and keep dependency wording aligned with Chapter 4 and Chapter 5. | Resolved. |
| CH11-CONS-02 | Major | `GLOSSARY.md`, source note and manuscript | Glossary has Kubernetes Deployment and Service but lacks ReplicaSet, Gateway API, HTTPRoute, Kubernetes Ingress and Kubernetes Node/Namespace entries needed by the corrected chapter. | Add or update glossary entries and align them with the source note and manuscript. | Resolved. |
| CH11-CONS-03 | Major | `SOURCE_REGISTER.md` and `research/infrastructure/kubernetes-docs-2026.md` | Source register describes Kubernetes topics as Deployments, Services, Pods, Nodes, Namespaces and Ingress only. | Update source note and source register for ReplicaSet and Gateway API. | Resolved. |
| CH11-CONS-04 | Major | `DIAGRAM_REGISTER.md`, manuscript and diagram artefacts | If `FIG-11-04` is renamed, filenames, register title, manuscript link, source title and export names must stay consistent. | Apply a single title and filename convention across all touched artefacts. | Resolved. |
| CH11-CONS-05 | Minor | Control files | `STATUS.md`, `RESUME.md`, `CHANGELOG.md` still describe Chapter 11 as ready without the current correction cycle. | Update control files after corrections and checks. | Resolved. |

## Notes

- Horizon Bank system names were checked against `examples/horizon-bank/system-landscape.md`.
- Simple Online Store provider names were checked against `examples/simple-online-store/README.md`.
