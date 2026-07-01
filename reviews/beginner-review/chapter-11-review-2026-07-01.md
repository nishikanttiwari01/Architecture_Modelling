# Chapter 11 Beginner Comprehension Review, 2026-07-01

## Scope

- Chapter: 11, Infrastructure and Deployment Modelling
- Manuscript: `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`
- HEAD reviewed: `99837319de0a9aa00358e83662fa3b7270e764b1`
- Review type: Beginner comprehension

## Findings

| ID | Severity | Affected file / section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH11-BEG-01 | Major | Prerequisites and dependencies | The chapter lists only Chapter 10, but the review depends on UML and C4 concepts from Chapters 4 and 5. | List Chapters 4, 5 and 10 as prerequisites, with Chapter 3 only as optional diagram-reading background if used. | Resolved. |
| CH11-BEG-02 | Major | Infrastructure versus deployment views | Reader outcome mentions logical versus physical deployment, but the chapter lacks a clear beginner subsection or table. | Add a logical versus physical deployment subsection and explain that one logical model can have several physical implementations. | Resolved. |
| CH11-BEG-03 | Major | Kubernetes deployment | The Kubernetes table omits ReplicaSet and Gateway API, and the figure/caption can teach that Deployment owns Pods directly. | Add beginner-safe table entries for ReplicaSet, Gateway API, HTTPRoute and Ingress. | Resolved. |
| CH11-BEG-04 | Major | Observability architecture and resilience figure | The observability chain is described but not demonstrated in enough detail for a beginner to review a real diagram. | Explain instrumentation/agent/collector, processing/export, backend, alerting and operational consumer in sequence. | Resolved. |
| CH11-BEG-05 | Minor | Practical exercise and cheat sheet | Exercise and checklist still ask for Kubernetes Deployments, Services, Pods, Namespaces and Ingress only. | Update learner prompts to include ReplicaSet and Gateway API where appropriate. | Resolved. |

## Notes

- The later author request explicitly required `FIG-11-06`. The six-figure set now separates the warm-standby resilience scenario in `FIG-11-05` from the payment observability view in `FIG-11-06`, which is clearer for beginners.
