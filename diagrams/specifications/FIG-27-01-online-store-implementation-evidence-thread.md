# FIG-27-01: Online Store Implementation Evidence Thread

## Authorisation and status

- Authorisation to proceed without a separate diagram approval pause: author instruction dated 2026-07-11.
- Maximum Codex status: Review.

## Purpose

Show how solution-design intent is refined into complementary detailed-design artefacts, repository evidence and test feedback.

## Audience

Beginner architects, developers, testers, security practitioners, platform engineers, operators and reviewers.

## Question answered

How does a team turn architectural intent into implementable, traceable detail without treating design as frozen?

## Notation

Original PlantUML traceability teaching view.

## Required elements

Show ADR-26-01 and requirements as intent; responsibility design; API and event contracts; physical data design; security controls; deployment, configuration and observability; repository evidence; verification evidence; and feedback to intent.

## Required relationships

Label refinement, implementation, verification and feedback relationships.

## Main flow or structure

Use a compact, top-to-bottom landscape layout targeting 700 to 800 pixels wide. Keep detailed-design artefacts in separate labelled boxes. Repository and verification evidence must be visually distinct.

## Alternative and exception flows

Show verification evidence feeding back to architecture intent when implementation learning changes an assumption, decision or requirement.

## Scope

Use Online Store checkout.

## Exclusions

Exclude code listings, complete payloads, vendor-specific manifests and claims of formal notation conformance.

## Accessibility requirements

Use short labels, sufficient contrast and explicit relationship text. Colour may group concepts but must not carry meaning alone. Avoid clipping, overlap, small text and excessive crossings.

## Source references

Original figure informed by official OpenAPI, AsyncAPI, OpenTelemetry and Kubernetes documentation. It reuses no source diagram.

## Review criteria

Render to SVG and PNG. Inspect at intended page width for readable labels, correct arrow directions, no clipping or overlap, adequate contrast and agreement with Chapter 27. Only then may the register move to Review.
