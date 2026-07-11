# FIG-33-01: Horizon Bank operating-model traceability view

- **Status:** Review
- **Specification checkpoint:** Author-approved chapter programme and figure production checkpoint, 2026-07-11

## Purpose

Show one selected, qualified traceability thread through Horizon Bank's operating-model set.

## Audience

Beginner architects, business architects, bank transformation stakeholders and reviewers.

## Question answered

How do unlike operating-model elements connect without being treated as equivalent?

## Notation

Original layered explanatory view using labelled arrows, not formal BIAN notation.

## Required elements

- Customer outcome: `Usable banking relationship`.
- Value stage: `Identity and eligibility confirmed`.
- Capabilities: `Customer Onboarding`, `Identity Verification` and `Financial Crime Screening`.
- Process: `Establish customer and account`.
- Reference: `Candidate BIAN Service Domain responsibilities`, labelled `BIAN 14.0 logical reference`.
- Roles: `Process owner`, `Operations` and `Control owner`.
- Information: `Party`, `Identity Evidence`, `Screening Result` and `Account`.
- Applications: `Customer Onboarding Platform`, `Party and Customer Platform`, `Financial Crime Platform` and `Core Deposit System`.
- Technology: `Runtime, integration and operational views`.
- Controls and measures: identity and screening evidence; completion time, straight-through processing and control failures.

## Required relationships

Use qualified verbs including `is enabled by`, `is exercised by`, `is informed by`, `is supported in part by`, `uses`, `runs on`, `is constrained by` and `is measured by`. State that mappings can be partial and many-to-many. Do not name unverified Service Domains.

## Main flow or structure

Use a compact top-to-bottom business thread. Branch from process into reference responsibility, roles and information, converge on applications and technology, then end with controls and measures.

## Alternative and exception flows

None. This is a structural traceability view, not a process flow. Partial and transitional mappings are represented by the explanatory note rather than exception branches.

## Scope

Retail customer onboarding excerpt only. This is not a universal or complete bank diagram. Exclude detailed BPMN sequence, interfaces and physical infrastructure. Do not show one-to-one mappings between a Service Domain and a capability, process, organisation, application or microservice.

## Exclusions

Detailed process sequence, interface contracts, physical infrastructure, invented Service Domain names and any claim that the figure represents the complete bank are excluded.

## Accessibility requirements

Use light backgrounds, dark text, redundant layer labels and relationship labels. Colour must not be the only carrier of meaning. The SVG is primary and the PNG is a preview. The native export must be no wider than 760 pixels, with node and relationship text at least 11 pixels. Text must remain readable at book-page width without post-render scaling.

## Source references

- `research/bian/bian-service-landscape-14.0.md`
- `examples/horizon-bank/capabilities.md`
- `examples/horizon-bank/system-landscape.md`

The composition and mappings are original author guidance. No BIAN artwork is copied.

## Review criteria

- SVG and PNG exist and render without errors.
- Text is readable at intended book-page width.
- No clipped text, overlaps or excessive crossings appear.
- Arrow direction and relationship labels agree with the chapter.
- Controlled Horizon Bank names are used.
- Status remains `Review`, never `Approved`.

## Production review, 2026-07-11

PlantUML produced native 695 by 899 pixel SVG and PNG exports without post-render scaling. SVG inspection confirms 12-pixel node and relationship text and a 14-pixel title. Original-resolution and intended-width visual review found no clipped text, overlaps or unreadable labels. Relationship directions, layer labels, qualified mappings and the caution note agree with the chapter. Status remains `Review`.
