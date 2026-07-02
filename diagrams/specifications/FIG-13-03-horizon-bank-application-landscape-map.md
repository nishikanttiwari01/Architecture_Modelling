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

- Horizon Digital Channels connects to Customer Onboarding Platform and Payments Platform.
- Customer Onboarding Platform connects to Party and Customer Platform, Product Catalogue and Financial Crime Platform.
- Payments Platform connects to Financial Crime Platform, Enterprise Integration Platform and Event Platform.
- Enterprise Integration Platform connects to Core Deposit System.
- Event Platform and selected operational systems feed Enterprise Data Platform.

## Main flow or structure

Group systems by channel, product or orchestration platforms, control platforms, integration or event platforms, retained core and data platform. Mark mixed or retained legacy where relevant.

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
