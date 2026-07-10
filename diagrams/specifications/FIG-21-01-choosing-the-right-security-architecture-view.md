# FIG-21-01: Choosing the Right Security Architecture View

## Purpose

Help beginner architects select a first security architecture view from the question they need to answer.

## Audience

Architects, developers, identity, security, privacy, operations, risk and audit teams.

## Question answered

Which security architecture view should an architect try first?

## Notation

PlantUML activity-style decision guide with explicit directional, labelled arrows. The author authorised specification creation and source/export production without an approval pause on 2026-07-11. This authorisation permits production, not approval.

## Required elements

- Start point labelled `Start with the security question`.
- Eight concise security questions and one first-choice view for each.
- Fallback that asks for the asset, audience, boundary and decision to be clarified.

## Required relationships

- Scope and assets to security context.
- Trust change to trust-boundary view.
- Identity establishment to authentication sequence.
- Permission to access-authorisation model.
- Harm paths to threat-model DFD or attack tree.
- Mitigation traceability to security-control map.
- Personal-data handling to privacy data-flow or lifecycle view.
- Detection and response to audit and monitoring view.

## Main flow or structure

A left-to-right guide uses labelled arrows from the starting question to eight focused first choices. The figure is a first filter; Chapter 21 provides audiences, elements and companion evidence.

## Alternative and exception flows

When several questions apply, create separate linked views and reuse stable identifiers. When no question fits, clarify the asset, audience, boundary and decision before drawing.

## Scope

Security context, trust, authentication, access authorisation, threats, controls, privacy, audit and monitoring.

## Exclusions

The figure does not teach notation, prescribe products, provide exploit instructions, select a control baseline or claim that one view proves security.

## Accessibility requirements

- Text carries all meaning; colour is supporting only.
- Arrows are directional and labelled.
- Text remains readable at normal book-page width.
- No clipped text, overlap, excessive crossings or ambiguous direction.

## Source references

- NIST-CSF-2.0
- NIST-SP-800-207
- NIST-SP-800-53R5
- NIST-PRIVACY-FRAMEWORK-1.0
- OWASP-THREAT-MODELLING-2026
- OWASP-ASVS-5.0.0
- MICROSOFT-STRIDE-2026
- SCHNEIER-ATTACK-TREES-1999

## Review criteria

- Production authorisation is recorded before source creation.
- PlantUML renders to SVG and PNG.
- Chapter caption and accessibility text agree with the figure.
- Visual inspection checks clipping, overlap, font size, crossings, direction, contrast, terminology and page-width readability.
- Register status reaches no higher than `Review`.
