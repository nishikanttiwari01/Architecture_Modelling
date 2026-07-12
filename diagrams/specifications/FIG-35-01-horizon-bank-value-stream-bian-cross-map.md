# FIG-35-01: Horizon Bank value-stream and BIAN responsibility cross-map

- **Status:** Author-approved for production
- **Specification checkpoint:** Author-authorised chapter programme and figure production checkpoint, 2026-07-12

## Purpose

Show how five stakeholder-value stages connect to controlled Horizon Bank capabilities and candidate BIAN reference responsibilities without making value stages, capabilities, Service Domains or processes equivalent.

## Audience

Beginner architects, business architects, product owners, process owners and banking transformation stakeholders.

## Question answered

Where is value created during customer acquisition, and which local capabilities and candidate BIAN responsibilities should be assessed at each stage?

## Notation

Original PlantUML cross-map. It is not formal ArchiMate, BPMN or BIAN notation.

## Required elements

- Stakeholder: `Retail Customer`.
- Outcome: `Usable banking relationship`.
- Value stages in order: `Need understood`, `Application established`, `Identity and eligibility confirmed`, `Banking relationship established`, `Services ready to use`.
- Controlled capabilities: `Relationship Management`, `Digital Servicing`, `Document Capture`, `Identity Verification`, `Risk Assessment`, `Financial Crime Screening`, `Party Management`, `Account Opening`, `Notification Management` and `Account Servicing`.
- One candidate BIAN mapping band labelled `BIAN 14.0 logical reference`, with five stage-aligned cells saying `Assess candidate Service Domains and interactions` rather than inventing names.
- Caution: mappings are candidate, partial and many-to-many; a Service Domain is not a value stage, process step, application or microservice.

## Required relationships

- Stakeholder `seeks value through` the value stream.
- Each stage `contributes to` the outcome.
- Capabilities `enable` stages, with primary or supporting contribution stated in text.
- Candidate BIAN responsibilities `inform responsibility analysis for` each stage.
- No connector may say or imply `equals`.

## Main flow or structure

Use a portrait, page-readable table or stacked cross-map. Show the ordered value stages as the main spine. For each stage, list primary and supporting capabilities in a separate local-capability band and place the candidate BIAN assessment in a separate reference band. Use text and headings so colour is not the only carrier of meaning.

## Alternative and exception flows

None. Detailed sequence, referral, timeout and exception behaviour belongs in Chapter 34 process views and Chapter 36 Business Scenarios.

## Scope

Retail customer acquisition through a usable banking relationship. The view teaches the mapping method and does not claim complete bank coverage or verified one-to-one BIAN mappings.

## Exclusions

Detailed process tasks, BPMN gateways, organisation lanes, applications, interfaces, deployment, BIAN artwork, unverified Service Domain names, funding scores and universal performance targets are excluded.

## Accessibility requirements

Use light backgrounds, dark text, explicit row headings and relationship verbs. SVG is the publication format and PNG is a preview. Native output must be no wider than 760 pixels and should be no taller than 950 pixels, with node and relationship text at least 11 pixels. Do not rely on post-render scaling.

## Source references

- `research/other-modelling/open-group-business-architecture-guides-2022.md`
- `research/bian/bian-service-landscape-14.0.md`
- `examples/horizon-bank/capabilities.md`

The value stages, contribution mappings and visual composition are original teaching guidance. No standards artwork is copied.

## Review criteria

- SVG and PNG exist and render without errors.
- Text is readable at intended book-page width without clipping or overlap.
- Stage order, capability names and primary or supporting contributions agree with the chapter.
- Candidate BIAN cells remain qualified and do not name unverified Service Domains.
- The figure does not treat a Service Domain as a value stage, process step, application or microservice.
- Final status remains `Review`, never `Approved`.

## Production review, 2026-07-12

PlantUML produced native 690 by 814 pixel SVG and PNG exports without post-render scaling. SVG inspection confirms 12-pixel node text and a 14-pixel title. Original-resolution and intended-page-width visual review found no clipped text, overlap or ambiguous connector semantics. Three separately headed, row-aligned bands distinguish value stages, local capabilities and candidate BIAN assessment cells. Every stage states independently that it contributes to the outcome; band headings state that capabilities enable aligned stages and BIAN informs responsibility analysis. Hidden connectors provide layout only, and no stage-to-stage process sequence is drawn. Stage order, capability names, qualified BIAN cells, caution and chapter caption agree. Status remains `Review`.
