# FIG-08-05 Horizon Bank payment data lineage

## Purpose

Show a simple lineage view for Horizon Bank payment data.

## Audience

Data architects, solution architects, risk reviewers and beginner readers.

## Question answered

Where does payment information originate, how is it transformed, which platforms use it, and where is it consumed for reporting or control?

## Notation

Informal lineage view in PlantUML.

## Required elements

- Horizon Digital Channels
- Payments Platform
- Financial Crime Platform
- Core Deposit System
- Event Platform
- Enterprise Data Platform
- Payment instruction
- Screened payment event
- Posting result
- Payment data product

## Required relationships

- Payment instruction flows from digital channels to payments platform
- Screening request or event flows to financial crime platform
- Posting request and result connect payments platform and core deposit system
- Payment event flows to event platform
- Curated payment data flows to enterprise data platform

## Main flow or structure

Show origin, transformation, platform responsibility and downstream use. Keep the lineage view separate from a process diagram.

## Alternative and exception flows

Show a screening exception branch only as lineage context, not as full casework.

## Scope

Horizon Bank payment initiation and reporting lineage at architecture level.

## Exclusions

No full payment scheme rules, reconciliation detail, data warehouse physical schema, API payload design or BPMN repair process.

## Accessibility requirements

Use labelled arrows, readable node names and non-colour-dependent semantics.

## Source references

- W3C-PROV-DM-2013
- Horizon Bank example files

## Review criteria

- Origin, transformation and consumption are clear.
- It does not replace the BPMN payment repair view.
- It uses stable Horizon Bank system names.
- It has no clipped text or overlapping labels.
