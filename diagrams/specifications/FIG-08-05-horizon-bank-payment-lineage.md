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
- Screening result
- Posting result
- Consolidated payment status event
- Payment data product

## Required relationships

- Payment instruction flows from digital channels to payments platform
- Screening request flows to financial crime platform
- Screening result becomes an input to the consolidated payment status event
- Posting request flows to core deposit system
- Posting result becomes an input to the consolidated payment status event
- Payments platform context and lineage inputs produce a consolidated payment status event using the original payment instruction, screening result and posting result
- Curated payment data flows to enterprise data platform

## Main flow or structure

Show origin, screening and posting result inputs, consolidation, platform responsibility and downstream use. Keep the lineage view separate from a process diagram.

## Alternative and exception flows

Show screening and posting outcomes only as lineage inputs, not as full operational casework.

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

- Origin, returned results, consolidated event and downstream consumption are clear.
- The final data product has traceable lineage from payment instruction, screening result, posting result and consolidated payment status event.
- It does not replace the BPMN payment repair view.
- It uses stable Horizon Bank system names.
- It has no clipped text or overlapping labels.
