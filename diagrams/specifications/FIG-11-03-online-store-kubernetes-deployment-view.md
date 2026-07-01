# FIG-11-03: Online Store Kubernetes Deployment View

## Purpose

Teach the minimum Kubernetes concepts needed to read a deployment model without confusing them with generic deployment wording.

## Audience

Developers, platform engineers and operations teams.

## Question answered

How do the Online Store web, API and worker workloads map to Kubernetes Gateway API, Services, Deployments, ReplicaSets, Pods and supporting storage?

## Notation

Kubernetes deployment teaching view, rendered with PlantUML after author acceptance of this specification.

## Required elements

- Kubernetes cluster boundary.
- Production namespace.
- GatewayClass, Gateway and HTTPRoute for public HTTPS routing.
- Optional note that Ingress is common for existing clusters but not the preferred new teaching example.
- Web Deployment and web Pods.
- API Deployment and API Pods.
- Worker Deployment and worker Pods.
- ReplicaSets managed by Deployments.
- Kubernetes Services for stable access where appropriate.
- Managed database outside the cluster.
- External Payment Provider System and Delivery Partner System.
- Visible note that StatefulSet is not shown because the Online Store workloads in this figure are replaceable stateless examples.

## Required relationships

- Gateway and HTTPRoute route external HTTPS traffic to a web or API Service.
- Deployment manages a ReplicaSet.
- ReplicaSet maintains Pod replicas.
- Service selects matching Pods.
- API Pods connect to the managed database and external provider systems.
- Worker Pods handle asynchronous fulfilment or notification work.

## Main flow or structure

Show Kubernetes control abstractions and workload replicas in a compact layout. Use labels that distinguish Gateway API resources, Deployment, ReplicaSet, Pod and Service.

## Alternative and exception flows

The figure may show multiple Pod replicas to make scaling visible, but it should not model rolling update steps.

## Scope

Conceptual Kubernetes deployment for the Simple Online Store.

## Exclusions

- No YAML manifest.
- No detailed container images, resource limits or autoscaling policy.
- No physical node scheduling, unless a later figure specifically asks that question.
- No Kubernetes security policy.
- No service mesh detail.
- No StatefulSet. Use StatefulSet when the workload needs stable identity or persistent state behaviour.

## Accessibility requirements

Use explicit text labels for each Kubernetes object type. Avoid small nested text that will be unreadable at book-page width.

## Source references

- [KUBERNETES-DOCS-2026]
- [NIST-SP-800-145]

## Review criteria

- Deployment, ReplicaSet, Pod, Service and Gateway API resources are not used interchangeably.
- Deployment manages ReplicaSets, and ReplicaSets maintain Pod replicas.
- StatefulSet is excluded visibly and for the correct reason.
- Cluster and namespace boundaries are explicit.
- External managed database and provider systems are clearly outside the cluster.
- Specification must be accepted by the author before creating the PlantUML source.
