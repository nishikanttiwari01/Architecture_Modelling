# FIG-30-01: Horizon Bank Migration Control Thread

## Authorisation and status

- Authorisation to create the specification and proceed without a separate approval pause: author instruction dated 2026-07-11.
- This committed specification is the required checkpoint before diagram source production.
- Maximum Codex status: Review.

## Purpose

Show how a change trigger becomes a controlled migration wave, with evidence-based cutover, fallback, reconciliation, decommissioning and feedback.

## Audience

Beginner architects, change leads, delivery teams, service and data owners, operations, risk reviewers and sponsors.

## Question answered

How does Horizon Bank govern a migration wave from intake through cutover and post-change learning without treating the roadmap as a guarantee?

## Notation

Original PlantUML migration-flow teaching view.

## Required elements

Show trigger and intake; impact and dependency assessment; current, transition and target architecture; wave scope and entry criteria; rehearsal and readiness evidence; a proceed or stop decision; cutover; verification and reconciliation; fallback to a recoverable boundary; stabilisation; decommissioning checks; benefits and operational feedback.

## Required relationships

Label assessment, planning, readiness evidence, authority, migration, verification, fallback, retirement and feedback. Show that failed verification returns to a defined recoverable state rather than promising risk-free rollback.

## Main flow or structure

Use a compact page-readable portrait layout, no wider than 760 pixels and preferably no taller than 950 pixels. Arrange intake and architecture understanding at the top, wave preparation and decision in the middle, and cutover, recovery, retirement and learning at the bottom. Keep the main route clear and use no unlabelled decision arrows.

## Alternative and exception flows

Show a stop path from the readiness decision back to preparation. Show a verification failure path to fallback and reassessment. Do not imply that every migration can be reversed instantly, that parallel operation is always appropriate, or that a roadmap is a delivery guarantee.

## Scope

One Horizon Bank payment-platform migration wave, including a bounded customer cohort, payment instruction data, operational ownership and affected interfaces.

## Exclusions

Exclude a complete programme roadmap, detailed application topology, formal BPMN, vendor-specific deployment commands, full regulatory obligations and BIAN implementation detail.

## Accessibility requirements

Use short labels, explicit arrow text, sufficient contrast and shape or text differences in addition to colour. Avoid clipped text, overlapping labels, unreadable font sizes, excessive crossings and ambiguous arrow direction.

## Source references

Original figure informed by The Open Group ArchiMate implementation and migration concepts, NIST contingency-planning guidance and NIST Cybersecurity Framework 2.0 governance concepts. It reuses no source diagram.

## Review criteria

After this specification is committed, create and render source to SVG and PNG. Confirm dimensions, inspect the output at intended page width, and verify readable labels, correct arrows, no clipping or overlap, sufficient contrast and agreement with Chapter 30. The register may move only as far as Review.
