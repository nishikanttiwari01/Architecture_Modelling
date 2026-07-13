# FIG-35-01: Horizon Bank data-domain and authority map

## Purpose

Show major data domains, qualified authorities and movement from operational processing to reporting.

## Audience

Business, data, application, risk and finance architects.

## Question answered

What information does the bank govern, where is it authoritative and how does it reach reporting?

## Notation

PlantUML conceptual data and flow view after author approval.

## Required elements

All Chapter 35 data domains, operational authorities, accounting, reconciliation, analytical platform and management, risk and regulatory reporting.

## Required relationships

Create, authorise, reference, post, reconcile, transform and report.

## Main flow or structure

Operational domains to accounting and controlled analytical/reporting flows, with provenance retained.

## Alternative and exception flows

Late adjustment, rejected record and reconciliation-break repair.

## Scope

Conceptual authority and lineage.

## Exclusions

Physical schema, attribute-level authority and unverified BIAN objects.

## Accessibility requirements

Line styles and labels supplement colour; all flows have arrow direction.

## Source references

[BCBS-239], [W3C-PROV-DM-2013]

## Review criteria

Operational and analytical authority are distinct; accounting and exception paths are visible.
