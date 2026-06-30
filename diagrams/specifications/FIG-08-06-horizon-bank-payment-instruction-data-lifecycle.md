# FIG-08-06 Horizon Bank payment instruction data lifecycle

## Purpose

Show the architecture-level lifecycle of a Horizon Bank payment instruction from capture to retention and archival or disposal.

## Audience

Data architects, solution architects, risk reviewers, operations reviewers and beginner readers.

## Question answered

Which lifecycle states does payment instruction data pass through, which systems are responsible, and where is the authoritative status at each stage?

## Notation

PlantUML lifecycle/state-style data view.

## Required elements

- Captured
- Validated
- Screened
- Posted
- Distributed
- Curated
- Retained
- Archived or Disposed
- Horizon Digital Channels
- Payments Platform
- Financial Crime Platform
- Core Deposit System
- Event Platform
- Enterprise Data Platform
- Records policy or retention owner

## Required relationships

- Captured data flows from Horizon Digital Channels to Payments Platform.
- Validated data remains under Payments Platform responsibility.
- Screening result comes from Financial Crime Platform and updates Payments Platform status.
- Posting result comes from Core Deposit System and updates Payments Platform status.
- Consolidated payment status event is distributed through Event Platform.
- Curated reporting data is managed by Enterprise Data Platform.
- Retention and archival or disposal follow records policy.

## Main flow or structure

Show a left-to-right lifecycle with each state labelled by state name, responsible system and authoritative status where useful.

## Alternative and exception flows

No detailed payment repair, screening investigation or posting exception process is required. Exception outcomes should be represented as possible status values, not process branches.

## Scope

Architecture-level data lifecycle for Horizon Bank payment instruction data.

## Exclusions

No payment scheme rules, operational repair process, regulatory retention period, physical archive design, database schema or implementation workflow.

## Accessibility requirements

Use readable labels, clear direction, sufficient contrast and state text that does not depend on colour.

## Source references

- W3C-PROV-DM-2013
- DAMA-DMBOK2-2017
- Horizon Bank example files

## Review criteria

- All required states are present and ordered.
- Responsible systems or ownership are visible where useful.
- Authoritative status is not ambiguous.
- The diagram is readable at book-page width.
- It has no clipped text or overlapping labels.
