# FIG-26-01: Online Store Solution Design Thread

## Authorisation and status

- Authorisation to proceed without a separate diagram approval pause: author instruction dated 2026-07-11.
- Maximum Codex status: Review.

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

Use a portrait flow from drivers through options and ADR to the five complementary design views and planned evidence.

## Alternative and exception flows

Show evidence feeding back to drivers to represent iterative refinement.

## Scope

One Online Store checkout design thread at solution level.

## Exclusions

Exclude API payloads, physical schemas, deployment manifests and formal notation conformance.

## Accessibility requirements

Use a portrait top-to-bottom layout for book-page width, short labels, sufficient contrast and labelled arrows. Colour supports grouping but is not the only carrier of meaning. Avoid clipping, overlap and excessive crossings.

## Source references

Original figure informed by official C4 guidance, UML 2.5.1, SEI quality attribute guidance and Nygard's ADR article. It reuses no source diagram.

## Review criteria

Source renders to SVG and PNG; both are visually inspected; content agrees with Chapter 26; register status is Review.
