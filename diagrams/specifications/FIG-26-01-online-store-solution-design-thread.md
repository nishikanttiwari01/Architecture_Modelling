# FIG-26-01: Online Store Solution Design Thread

## Authorisation and status

- Authorisation to proceed without a separate diagram approval pause: author instruction dated 2026-07-11.
- Revision authorisation: the author authorised this corrected specification on 2026-07-11 and permits regeneration without another pause.
- Maximum Codex status: Review.

## Production history

The initial specification, source and exports were committed together, so their ordering was not independently auditable. This revision restores an explicit specification-first checkpoint. Regenerated source and exports must follow in a later commit.

## Purpose

Show how analysed drivers lead through option assessment and an ADR to a coherent multi-view solution design, planned evidence and iterative feedback.

## Audience

Beginner architects, analysts, engineers, security practitioners, operators and reviewers.

## Question answered

How do solution-design decisions connect drivers, complementary views and evidence without implying a one-pass lifecycle?

## Notation

Original PlantUML traceability teaching view.

## Required elements

Show design drivers, three options, ADR-26-01, structure, interaction, information, security and deployment views, planned evidence and a feedback link.

## Required relationships

Label the driver-to-option, option-to-ADR, ADR-to-view, view-to-evidence and evidence-to-driver relationships.

## Main flow or structure

Use a compact portrait, top-to-bottom flow in this visible order:

1. design drivers;
2. options;
3. ADR-26-01;
4. five separate view boxes arranged as stacked rows, with no enclosing package that can reverse routing; and
5. planned evidence.

Place Structure, Interaction and Information in the first view row. Place Security and Deployment in the second view row. Use hidden or layout-only links when necessary to preserve rank and reading order. Do not merge the five views.

## Alternative and exception flows

Show evidence feeding back to drivers to represent iterative refinement.

## Scope

One Online Store checkout design thread at solution level.

## Exclusions

Exclude API payloads, physical schemas, deployment manifests and formal notation conformance.

## Accessibility requirements

Use a portrait top-to-bottom layout targeting 700 to 750 pixels wide at native PNG export. Use short native-size labels, sufficient contrast and explicit relationship labels. Colour supports grouping but is not the only carrier of meaning. Avoid clipping, overlap, line-label collisions and excessive crossings.

## Source references

Original figure informed by official C4 guidance, UML 2.5.1, SEI quality attribute guidance and Nygard's ADR article. It reuses no source diagram.

## Review criteria

Source renders after this specification checkpoint to SVG and PNG at approximately 700 to 750 pixels wide. Inspection confirms the required top-to-bottom order, five separate views, readable native labels, explicit relationship labels, no clipping or overlap, correct arrow directions, sufficient contrast and agreement with Chapter 26. Only then may the register return to Review.
