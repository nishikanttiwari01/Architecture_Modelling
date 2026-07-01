# Source Note: KUBERNETES-DOCS-2026

## Bibliographic details

- Organisation or author: Kubernetes project
- Title: Kubernetes documentation, concepts for Deployments, ReplicaSets, StatefulSets, Services, Pods, Nodes, Namespaces, Gateway API and Ingress
- Version: Current public documentation
- Publication date: Current web documentation, individual pages vary
- Access date: 2026-07-01
- URL or identifier: https://kubernetes.io/docs/concepts/; https://kubernetes.io/docs/concepts/workloads/controllers/deployment/; https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/; https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/; https://kubernetes.io/docs/concepts/services-networking/service/; https://kubernetes.io/docs/concepts/services-networking/gateway/; https://kubernetes.io/docs/concepts/services-networking/ingress/
- Source type: Official project documentation

## Supported claims

- Claim: Kubernetes modelling should distinguish nodes, pods, deployments, ReplicaSets, services, namespaces, Gateway API resources, ingress and persistent storage.
- Intended chapter(s): Chapter 11, Chapter 20, Chapter 49
- Normative or interpretive: Normative for Kubernetes terminology; interpretive for modelling guidance.

- Claim: A Kubernetes Deployment provides declarative updates for Pods and ReplicaSets, while a ReplicaSet maintains a stable set of replica Pods.
- Intended chapter(s): Chapter 11, Chapter 20, Chapter 49
- Normative or interpretive: Normative for Kubernetes concepts.

- Claim: A Deployment is generally suitable for replaceable stateless workloads, while StatefulSet is the Kubernetes workload API for stateful applications that need stable identity, persistent storage or ordered behaviour.
- Intended chapter(s): Chapter 11, Chapter 20, Chapter 49
- Normative or interpretive: Normative for Kubernetes concepts; interpretive for beginner selection guidance.

- Claim: A Kubernetes Service provides stable network access to a logical set of endpoints, usually Pods.
- Intended chapter(s): Chapter 11, Chapter 20, Chapter 49
- Normative or interpretive: Normative for Kubernetes concepts.

- Claim: Gateway API is the Kubernetes project API family for extensible and role-oriented service networking; Ingress remains generally available, is frozen, and is not planned for removal, while the Kubernetes project recommends Gateway API for newer routing designs.
- Intended chapter(s): Chapter 11, Chapter 20, Chapter 49
- Normative or interpretive: Normative for Kubernetes project positioning; interpretive for beginner modelling guidance.

## Relevant summary

The Kubernetes documentation defines core cluster, workload and service networking concepts used in deployment views. Chapter 11 uses the documentation to keep Kubernetes examples from confusing application containers, Pods, Deployments, ReplicaSets, StatefulSets, Services, Nodes, Namespaces, Gateway API and Ingress.

## Terminology and version notes

Use Kubernetes terms with their project meanings. Avoid calling every deployable unit a Kubernetes Deployment unless the model is actually describing a Kubernetes object of that kind. For new teaching examples, prefer Gateway API when explaining modern HTTP routing, while explaining that Ingress remains common, generally available, frozen and not planned for removal.

## Copyright or reuse notes

Paraphrase concepts and create original examples. Do not reproduce Kubernetes diagrams or long documentation excerpts.

## Verification status

Checked
