# Source Note: KUBERNETES-DOCS-2026

## Bibliographic details

- Organisation or author: Kubernetes project
- Title: Kubernetes documentation, concepts for Deployments, Services, Pods, Nodes, Namespaces and Ingress
- Version: Current public documentation
- Publication date: Current web documentation, individual pages vary
- Access date: 2026-06-30
- URL or identifier: https://kubernetes.io/docs/concepts/
- Source type: Official project documentation

## Supported claims

- Claim: Kubernetes modelling should distinguish nodes, pods, deployments, services, namespaces, ingress and persistent storage.
- Intended chapter(s): Chapter 11, Chapter 20, Chapter 49
- Normative or interpretive: Normative for Kubernetes terminology; interpretive for modelling guidance.

- Claim: A Kubernetes Deployment describes desired state for application workload replicas, while a Service provides a stable way to expose a set of Pods.
- Intended chapter(s): Chapter 11, Chapter 20, Chapter 49
- Normative or interpretive: Normative for Kubernetes concepts.

## Relevant summary

The Kubernetes documentation defines core cluster and workload concepts used in deployment views. Chapter 11 uses the documentation to keep Kubernetes examples from confusing application containers, pods, deployments, services and nodes.

## Terminology and version notes

Use Kubernetes terms with their project meanings. Avoid calling every deployable unit a Kubernetes Deployment unless the model is actually describing a Kubernetes object of that kind.

## Copyright or reuse notes

Paraphrase concepts and create original examples. Do not reproduce Kubernetes diagrams or long documentation excerpts.

## Verification status

Checked
