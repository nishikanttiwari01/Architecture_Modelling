# Source Note: KUBERNETES-DEPLOYMENT-PV52-2026

## Bibliographic details

- Organisation or author: Kubernetes project
- Title: Kubernetes documentation for workloads, Services and Gateway API
- Version: Current public documentation
- Publication date: Continuously maintained documentation
- Access date: 2026-07-20
- URL or identifier: https://kubernetes.io/docs/concepts/workloads/; https://kubernetes.io/docs/concepts/services-networking/service/; https://kubernetes.io/docs/concepts/services-networking/gateway/
- Source type: Official project documentation

## Supported claims

- Claim: Kubernetes Pods, Deployments, StatefulSets, Services, Nodes and Gateway API resources have distinct runtime and networking meanings.
- Claim: A logical application or software service should not be assumed to equal one Kubernetes Deployment, Pod or Service.
- Intended chapter(s): 52
- Normative or interpretive: Official for Kubernetes terminology; interpretive for deployment-modelling guidance.

## Relevant summary

Kubernetes distinguishes workload controllers, Pods, cluster Nodes and stable service-networking abstractions. Chapter 52 uses these terms only as an example of a possible physical deployment model. Horizon Bank has not selected Kubernetes for every application, so the governed logical application catalogue remains technology-neutral.

## Terminology and version notes

Capitalise Kubernetes object names when referring to the formal API object. Do not confuse a C4 container, operating-system container and Kubernetes Pod.

## Copyright or reuse notes

Paraphrase official documentation and use original modelling examples.

## Verification status

Checked
