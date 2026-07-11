# FIG-32-01: BIAN and multi-technique traceability view

## Specification checkpoint

- Author instruction: create and continue without a separate approval pause
- Checkpoint date: 2026-07-11
- Maximum lifecycle state after rendering: Review

## Purpose

Show how BIAN contributes banking responsibility and exchange semantics while complementary models answer process, software, information, decision, event and runtime questions.

## Audience

Beginners, banking architects, business analysts, software architects and reviewers.

## Question answered

How can Horizon Bank trace one payment change across distinct modelling questions without claiming one-to-one equivalence between model elements?

## Notation

Original PlantUML relationship view. The boxes are labelled by modelling question and artefact type. This is not formal BIAN, ArchiMate, BPMN, C4, UML or DMN notation.

## Required elements

- Payment Initiation capability and customer payment scenario.
- Candidate BIAN Service Domain responsibility and labelled Service Operation or business exchange.
- BPMN process collaboration and DMN routing decision.
- C4 application/container responsibility and UML sequence interaction.
- Conceptual business information and governed logical data model.
- Event contract and deployment/operational view.
- Explicit traceability record containing source, target, relationship, rationale, owner, version and evidence.
- A visible warning that mappings can be many-to-many and that no Service Domain automatically equals a capability, process step, application, container, microservice, endpoint, event topic, entity or deployment unit.

## Required relationships

Use labelled relationships only: frames, realises in part, participates in, exchanges meaning through, supports, invokes, informs, consumes or produces, persists as, and runs on. Route traceability through a central evidence record rather than drawing an unreadable web of direct equivalence arrows.

## Main flow or structure

Use a compact landscape with three bands. The left band establishes business intent through capability and scenario. The centre band shows BIAN responsibility and semantic exchange plus behavioural detail. The right band shows software, information and runtime choices. A traceability record spans the bottom and records qualified mappings. A warning note spans the top or bottom.

## Alternative and exception flows

The view must permit one application to support several Service Domains and several applications to realise one Service Domain. It must also permit a process task, interface, event or data concept to relate to several logical responsibilities.

## Scope

One Horizon Bank outgoing-payment teaching thread. The view demonstrates how artefacts complement one another and how a reviewer follows a change from business intent to operational evidence.

## Exclusions

- A complete BIAN landscape or normative BIAN diagram.
- A complete payment process, API specification, event schema, physical data model or deployment topology.
- Claims of BIAN conformance.
- Any automatic Service Domain-to-implementation translation.

## Accessibility requirements

Use high contrast, readable text, a left-to-right reading order and relationship labels that do not depend on colour. Keep the export page-readable at intended book width. Avoid clipped text, overlaps and excessive line crossings. Provide textual explanation and a meaningful caption in Chapter 32.

## Source references

- `research/bian/bian-service-landscape-14.0.md`
- `research/bian/bian-introduction-how-to-guide-v7.md`
- `research/bian/bian-semantic-api-practitioner-guide-v8.1.md`
- Official primary-source notes already registered for ArchiMate, BPMN, C4, UML and DMN.
- `examples/horizon-bank/capabilities.md`
- `examples/horizon-bank/system-landscape.md`

## Review criteria

- Every technique is associated with an explicit question.
- BIAN is shown as a reference contribution, not a modelling-language replacement.
- No relationship implies one-to-one equivalence.
- The worked thread includes capability, scenario, Service Domain responsibility, application, interface, data, event and deployment concerns.
- Labels, directions and terminology agree with Chapter 32 and the controlled Horizon Bank examples.
- SVG and PNG contain no clipping, overlap, unreadable text or excessive crossings at native and intended book-page width.
- Lifecycle state after successful rendering is `Review`, never `Approved`.
