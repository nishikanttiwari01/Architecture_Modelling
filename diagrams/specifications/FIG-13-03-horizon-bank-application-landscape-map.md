# FIG-13-03: Horizon Bank Application Landscape Map

## Purpose

Show selected Horizon Bank systems and high-level relationships in a mixed current and target estate.

## Audience

Enterprise architects, solution architects and application owners.

## Question answered

Which major systems exist around Horizon Bank onboarding and payments, and how do they relate at landscape level?

## Notation

Application landscape map. C4 System Landscape or simple PlantUML boxes may be used after author approval.

## Required elements

- Horizon Digital Channels.
- Customer Onboarding Platform.
- Party and Customer Platform.
- Product Catalogue.
- Payments Platform.
- Financial Crime Platform.
- Core Deposit System.
- Enterprise Integration Platform.
- Event Platform.
- Enterprise Data Platform.

## Required relationships

- Horizon Digital Channels to Customer Onboarding Platform: submits onboarding applications.
- Horizon Digital Channels to Payments Platform: initiates payments and obtains payment status.
- Customer Onboarding Platform to Party and Customer Platform: establishes party and customer records.
- Customer Onboarding Platform to Product Catalogue: reads product and eligibility definitions.
- Customer Onboarding Platform to Financial Crime Platform: requests onboarding screening.
- Payments Platform to Financial Crime Platform: requests payment screening.
- Payments Platform to Enterprise Integration Platform: invokes retained-core integration services.
- Enterprise Integration Platform to Core Deposit System: mediates posting and account-access requests.
- Payments Platform to Event Platform: publishes governed payment-status events.
- Event Platform to Enterprise Data Platform: supplies governed events for data use.

## Main flow or structure

Group systems by channel, product or orchestration platforms, control platforms, integration or event platforms, retained core and data platform. Every displayed system must show exactly one lifecycle marker from `examples/horizon-bank/system-landscape.md`: `Target`, `Mixed`, `Transitional` or `Legacy retained initially`. Include a visible lifecycle legend using those four values.

## Alternative and exception flows

None. This is a structural landscape.

## Scope

High-level application landscape for Chapter 13 only.

## Exclusions

- Full interface catalogue.
- Data schema detail.
- Business process flow.
- Deployment or infrastructure placement.

## Accessibility requirements

Use labelled relationship arrows. Do not rely on icon meaning alone.

## Source references

- `[C4-OFFICIAL]`
- `[OPEN-GROUP-ARCHIMATE-4]`
- `examples/horizon-bank/system-landscape.md`

## Review criteria

- Stable Horizon Bank system names are used.
- The view is readable at book-page width.
- Relationship labels are high level but not vague.
- Current, target and legacy-retained meanings are not hidden.
- A note explains the limitation of a mixed-state landscape and does not imply all target systems already exist.
