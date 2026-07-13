# FIG-36-01: Horizon Bank critical-operation dependency map

## Purpose

Trace a time-critical payment through people, applications, data, technology, facilities and third parties.

## Audience

Business, technology, security, resilience and operations stakeholders.

## Question answered

What must continue, recover or degrade safely for Horizon Bank to deliver a critical payment operation?

## Notation

PlantUML dependency view after author approval.

## Required elements

Customer, support and operations roles; identity; channel; payments; screening; account posting; clearing; settlement; communication; reconciliation; runtime, network and third-party dependencies.

## Required relationships

Depends on, authenticates through, processes, controls, records, connects to, monitors and recovers through.

## Main flow or structure

Customer outcome centred dependency map, not a platform-centred deployment view.

## Alternative and exception flows

Degraded channel, screening referral, clearing outage, delayed posting and manual repair.

## Scope

One illustrative critical operation and its principal dependencies.

## Exclusions

Invented numerical tolerances, detailed network addresses and universal regulatory claims.

## Accessibility requirements

Dependency categories use labelled containers; colour is optional and never exclusive.

## Source references

[BCBS-OPERATIONAL-RESILIENCE-2021], [NIST-CSF-2.0]

## Review criteria

People and third parties are included; degraded modes and evidence are visible; recovery is not reduced to component failover.
