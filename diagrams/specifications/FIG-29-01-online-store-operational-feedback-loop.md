# FIG-29-01: Online Store Operational Feedback Loop

## Authorisation and status

- Authorisation to create the specification and proceed without a separate approval pause: author instruction dated 2026-07-11.
- This committed specification is the required checkpoint before diagram source production.
- Consistency correction: architecture records provide evidence for change governance but do not themselves hold approval authority. The relationship from architecture records to governed change must be labelled `informs approved change`. This correction is to be committed before source and export regeneration.
- Maximum Codex status: Review.

## Purpose

Show that operating and supporting a service is an owned, evidence-led loop that can change architecture, not a passive activity after delivery.

## Audience

Beginner architects, service owners, engineers, operators, support staff, security and data practitioners, and change authorities.

## Question answered

How do runtime signals and support experience lead to response, learning and governed architecture change?

## Notation

Original PlantUML operational-flow teaching view.

## Required elements

Show the Online Store checkout service and dependencies; customers and support; telemetry; service objectives and alerts; named service ownership; incident response; runbooks; incident and problem learning; architecture records and models; and governed change back into the service.

## Required relationships

Label telemetry collection, alert routing, customer escalation, diagnosis, restoration, learning, architecture update and controlled change. Label the relationship from architecture records to governed change `informs approved change`, so that approval is not attributed to the records themselves. Distinguish immediate service restoration from longer-term problem treatment.

## Main flow or structure

Use a compact page-readable portrait layout, no wider than 760 pixels and preferably no taller than 900 pixels. Arrange runtime service and signals near the top, response and support in the middle, and learning plus architecture change at the bottom. Make the feedback path unmistakable without excessive crossings.

## Alternative and exception flows

Show that an alert may start response and that a customer report may reveal a problem not detected by an alert. Show controlled change returning to the runtime service. Do not imply that monitoring prevents every failure or that every incident requires architecture change.

## Scope

Online Store checkout, including the API Application, payment provider, order data, observability path, service owner and customer support.

## Exclusions

Exclude product-specific monitoring tools, a complete incident-management process, detailed infrastructure topology, formal BPMN, guaranteed service levels and a claim that support owns all architecture decisions.

## Accessibility requirements

Use short labels, explicit arrow text, sufficient contrast and shape or text differences in addition to colour. Avoid clipped text, overlapping labels, unreadable font sizes and ambiguous arrow direction.

## Source references

Original figure informed by Google SRE guidance on service-level indicators and objectives, NIST SP 800-61 Revision 3 incident response guidance, NIST SP 800-34 Revision 1 contingency planning and OpenTelemetry observability concepts. It reuses no source diagram.

## Review criteria

After this specification is committed, create and render source to SVG and PNG. Confirm dimensions, inspect the output at intended page width, and verify readable labels, correct arrows, no clipping or overlap, sufficient contrast and agreement with Chapter 29. The register may move only as far as Review.
