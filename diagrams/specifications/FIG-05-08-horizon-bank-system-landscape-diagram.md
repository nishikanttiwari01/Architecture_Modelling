# FIG-05-08: Horizon Bank System Landscape Diagram

## Purpose

Show the wider Horizon Bank software landscape around the payments platform.

## Audience

Enterprise architects, solution architects and senior technology stakeholders.

## Question answered

Which major Horizon Bank systems relate to digital channels and payments, and where does the Payments Platform sit in that estate?

## Notation

C4 System Landscape using C4-PlantUML context notation.

## Required elements

- Retail Customer
- Operations Analyst
- Horizon Digital Channels
- Customer Onboarding Platform
- Party and Customer Platform
- Payments Platform
- Core Deposit System
- Financial Crime Platform
- Enterprise Integration Platform
- Event Platform
- Enterprise Data Platform

## Required relationships

- Retail Customer uses Horizon Digital Channels.
- Operations Analyst monitors Payments Platform.
- Horizon Digital Channels use Customer Onboarding Platform, Party and Customer Platform and Payments Platform.
- Payments Platform requests customer context from Party and Customer Platform.
- Payments Platform requests screening from Financial Crime Platform.
- Payments Platform requests account posting through Enterprise Integration Platform.
- Enterprise Integration Platform adapts calls to Core Deposit System.
- Payments Platform publishes events to Event Platform.
- Event Platform feeds Enterprise Data Platform.

## Main flow or structure

Show a landscape-level map of software systems. Keep responsibilities broad and avoid container or component detail.

## Alternative and exception flows

None. This is a structural landscape view.

## Scope

Major systems around retail channels, customer information, payments, integration, financial crime, deposit accounts and data.

## Exclusions

No containers, services, databases, processes, user stories or deployment nodes.

## Accessibility requirements

Use short relationship labels, readable spacing and enough white space for page-width rendering.

## Source references

- `[C4-OFFICIAL]`
- `examples/horizon-bank/system-landscape.md`
- `examples/horizon-bank/actors.md`

## Review criteria

- The view stays above a single system context.
- Systems are not decomposed into containers.
- The Payments Platform is visible without dominating the whole landscape.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 correction on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
