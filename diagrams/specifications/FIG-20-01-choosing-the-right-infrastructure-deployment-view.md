# FIG-20-01: Choosing the Right Infrastructure and Deployment View

## Purpose

Help beginner architects select a first infrastructure or deployment view from the
operational question they need to answer.

## Audience

Beginner and practising architects, developers, platform and cloud teams, network and
operations teams, service owners, continuity specialists and risk reviewers.

## Question answered

Which infrastructure or deployment view should an architect try first?

## Notation

PlantUML decision guide using simple shapes and labelled branches. Source and export are
deferred until author approval of this specification.

## Required elements

- Start point labelled `Start with the operational question`.
- Eight concise question prompts.
- One first-choice view for each prompt.
- Reminder to state audience, boundary, environment and abstraction level.
- Fallback to clarify the decision before drawing.

## Required relationships

- Runtime placement points to a UML or C4 deployment view.
- Network zones and traffic paths point to a network topology.
- Cloud services and responsibility point to a cloud architecture view.
- Cluster workload objects point to a Kubernetes deployment view.
- Environment differences point to an environment comparison matrix.
- Continuity through expected failure points to an availability or resilience view.
- Restoration after serious disruption points to a recovery view.
- Monitoring and action ownership points to an ownership matrix or observability view.

## Main flow or structure

The reader starts with an operational question and follows the first matching branch.
The result is a first-choice view, not a complete mandatory diagram set. Chapter 20's
selection table provides audience, elements and companion-view detail.

## Alternative and exception flows

When several questions apply, advise separate linked views with stable names and
identifiers. If no question fits, direct the reader to clarify the decision, audience,
boundary, environment and level before drawing.

## Scope

Runtime deployment, network topology, cloud services, Kubernetes, environment
differences, availability, recovery, operational ownership and observability.

## Exclusions

The figure does not teach notation, prescribe a cloud provider, show Kubernetes manifest
fields, provide firewall rules, define a recovery runbook or replace a security model.

## Accessibility requirements

- Labels carry all meaning; colour is optional support only.
- Text remains readable at normal book-page width.
- Direction is visible through arrows and branch labels.
- No clipped text, overlapping labels or dense crossings.
- The figure remains understandable with the prose and caption without colour.

## Source references

- OMG-UML
- C4-OFFICIAL
- NIST-SP-800-145
- KUBERNETES-DOCS-2026
- AWS-WA-RELIABILITY-2026
- NIST-SP-800-34R1
- OPENTELEMETRY-DOCS-2026

## Review criteria

- Author signs off this specification before source creation.
- PlantUML source renders to SVG after sign-off.
- Register paths are updated after rendering.
- Chapter 20 receives a meaningful caption and accessibility text after rendering.
- Output is readable at intended page width and visually inspected.
- Register status moves only to `Review` after rendering and inspection; approval remains
  author-only.
