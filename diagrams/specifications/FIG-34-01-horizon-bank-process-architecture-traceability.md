# FIG-34-01: Horizon Bank process-architecture decomposition and traceability view

- **Status:** Author-approved for production
- **Specification checkpoint:** Author-approved chapter programme and figure production checkpoint, 2026-07-12

## Purpose

Show how a bank-wide process family decomposes into an end-to-end process and selected subprocesses, then trace that process to ownership, outcomes, controls, measures, capabilities and candidate BIAN responsibilities without implying equivalence.

## Audience

Beginner architects, business analysts, process owners, control owners and bank transformation stakeholders.

## Question answered

How can a reader navigate from a bank process catalogue to governed detail and related architecture elements?

## Notation

Original PlantUML explanatory view. This is not BPMN or formal BIAN notation.

## Required elements

- Catalogue level: `Customer and party management` process family.
- End-to-end level: `Establish customer relationship` process.
- Subprocess level: `Capture application`, `Verify identity and screen`, `Resolve referral`, `Create party and account records`, and `Confirm usable service`.
- Accountable role: `Onboarding process owner`.
- Outcome: `Usable banking relationship`.
- Controls: `Identity evidence` and `Screening evidence`.
- Measures: `Elapsed time`, `Straight-through processing`, `Referral rate`, and `Control failures`.
- Capabilities: `Customer Onboarding`, `Identity Verification`, `Financial Crime Screening`, `Party Management`, and `Account Opening`.
- Reference: `Candidate BIAN Service Domains and interactions`, labelled `BIAN 14.0 logical reference`.
- Detail pointer: `Selected BPMN collaboration`, explicitly not a full-bank diagram.

## Required relationships

Label decomposition as `contains` and `decomposes to`. Label other relationships `is accountable for`, `produces`, `is constrained by`, `is measured by`, `exercises`, `is informed by` and `details selected behaviour`. State that BIAN mappings are candidate, partial and many-to-many. Do not name unverified Service Domains.

## Main flow or structure

Use a top-to-bottom decomposition spine on the left. Place governance and traceability elements in a compact right-hand column. Keep subprocesses in a short horizontal row or wrapped group. Use relationship labels rather than proximity to convey meaning.

## Alternative and exception flows

`Resolve referral` represents the principal exception path. The figure does not model its detailed sequence, timer or escalation behaviour.

## Scope

One retail onboarding excerpt from Horizon Bank's enterprise process architecture. It demonstrates the catalogue pattern and does not claim to show every process family or one universal process.

## Exclusions

Detailed BPMN notation, application components, interfaces, deployment, organisation chart, complete process inventory, prescriptive BIAN sequence, and one-to-one Service Domain mapping are excluded.

## Accessibility requirements

Use light backgrounds, dark text, redundant headings and explicit relationship labels. Colour must not be the only carrier of meaning. SVG is the publication format and PNG is a preview. Native output should fit a portrait book page, with node and relationship text at least 11 pixels.

## Source references

- `research/bian/bian-service-landscape-14.0.md`
- `research/bian/bian-portal-2026.md`
- `research/bpmn/omg-bpmn-2.0.2.md`
- `examples/horizon-bank/capabilities.md`

The decomposition, mappings and visual composition are original author guidance. No standards artwork is copied.

## Review criteria

- SVG and PNG exist and render without errors.
- Text is readable at intended book-page width.
- No clipped text, overlap, excessive crossings or ambiguous arrows appear.
- Decomposition and traceability relationship directions agree with the chapter.
- The figure states its selected scope and does not imply a universal process model.
- Service Domains are not shown as process steps, applications or microservices.
- Final status remains `Review`, never `Approved`.

## Production review, 2026-07-12

PlantUML produced native SVG and PNG exports without post-render scaling. Original-resolution visual review found no clipped text, overlaps or ambiguous arrow direction. The selected process scope, exception subprocess, labelled relationships, BIAN caution and chapter caption agree. Status remains `Review`.
