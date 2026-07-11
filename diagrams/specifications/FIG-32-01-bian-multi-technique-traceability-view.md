# FIG-32-01: BIAN and multi-technique traceability view

## Specification checkpoint

- Author instruction: create and continue without a separate approval pause
- Checkpoint date: 2026-07-11
- Maximum lifecycle state after rendering: Review
- Author-authorised correction: 2026-07-11. The prior 720 by 442 render did not implement the specified three-band landscape or name the worked Horizon Bank thread precisely enough. Replace it with an implementable three-band landscape no wider than 760 pixels. Regeneration is pending this corrected checkpoint.

## Purpose

Show how BIAN contributes banking responsibility and exchange semantics while complementary models answer process, software, information, decision, event and runtime questions.

## Audience

Beginners, banking architects, business analysts, software architects and reviewers.

## Question answered

How can Horizon Bank trace one payment change across distinct modelling questions without claiming one-to-one equivalence between model elements?

## Notation

Original PlantUML relationship view. The boxes are labelled by modelling question and artefact type. This is not formal BIAN, ArchiMate, BPMN, C4, UML or DMN notation.

## Required elements

Name this exact Horizon Bank worked thread in the figure:

- capability and business need: `Payment Initiation` and `Improve outgoing retail payments`;
- BIAN behaviour: `Outgoing customer payment Business Scenario`;
- BIAN responsibility: `Candidate payment-handling Service Domain responsibility`;
- Horizon application: `Payments Platform`;
- interface: `Outgoing Payment API`;
- data: `Payment Instruction`;
- event: `PaymentInstructionAccepted`;
- deployment: `Payments runtime`.

Also include a compact qualification note stating that mappings may be one-to-many, many-to-one or transitional, and that a Service Domain is not automatically a capability, process step, application, microservice, interface, event, data entity or deployment unit.

## Required relationships

Every visible relationship label must be exactly one of the following, with no prefixes, suffixes or synonyms: `frames`, `realises in part`, `participates in`, `exchanges meaning through`, `supports`, `invokes`, `informs`, `consumes or produces`, `persists as`, `runs on`.

## Main flow or structure

Use a compact landscape no wider than 760 pixels with exactly three horizontal bands. Reading order inside each band is left to right.

1. **Business and BIAN band:** business need and Payment Initiation capability, then Business Scenario, then candidate Service Domain responsibility.
2. **Application and exchange band:** Payments Platform, then Outgoing Payment API, then Payment Instruction and `PaymentInstructionAccepted` grouped compactly at the right.
3. **Runtime and qualification band:** Payments runtime, followed by the qualification note spanning the remaining width.

Use orthogonal or short direct connectors. Do not add a central traceability hub, diagonal feedback web, technique inventory or question text inside every node. The figure demonstrates one worked trace, while the chapter prose and matrix explain the wider technique set.

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

Use high contrast, readable text and left-to-right order within each band. Keep the SVG and PNG at no more than 760 pixels wide and page-readable at intended book width. Avoid clipped text, overlaps, tiny labels, diagonal feedback webs and excessive crossings. Relationship meaning must not depend on colour. Provide matching caption and accessibility text in Chapter 32.

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
- The exact worked-thread elements listed above are visible and correctly ordered across three bands.
- Every relationship label belongs to the exact allowed-label list.
- Labels, directions and terminology agree with Chapter 32 and the controlled Horizon Bank examples.
- SVG and PNG are no wider than 760 pixels and contain no clipping, overlap, unreadable text or excessive crossings at native and intended book-page width.
- Lifecycle state after successful rendering is `Review`, never `Approved`.
