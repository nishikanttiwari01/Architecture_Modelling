# FIG-13-02: Horizon Bank Customer Onboarding Value Stream

## Purpose

Show the major value stages for Horizon Bank customer onboarding and connect those stages to enabling capabilities.

## Audience

Business architects, enterprise architects, product owners and sponsors.

## Question answered

How does Horizon Bank create value for a prospective customer during onboarding, and which capabilities enable each stage?

## Notation

Value stream teaching view with stages and capability references. This is not BPMN.

## Required elements

- Triggering stakeholder: Retail Customer.
- Value stages: Need understood, Application established, Identity and eligibility confirmed, Banking relationship established, Services ready to use.
- Enabling capabilities: Digital Servicing, Relationship Management, Customer Onboarding, Document Capture, Identity Verification, Financial Crime Screening, Risk Assessment, Party Management, Account Opening, Product Management, Notification Management, Account Servicing.

## Required relationships

- Retail Customer triggers the value stream.
- Value stages appear in order from left to right.
- Each stage links to two or more enabling capabilities.

## Main flow or structure

Use a horizontal value stream with five stakeholder-value outcome stages. Place enabling capabilities below the relevant stages.

## Alternative and exception flows

Do not show detailed exception handling. Mention in a note that BPMN is better for detailed onboarding exceptions.

## Scope

Beginner business architecture explanation for Chapter 13.

## Exclusions

- Detailed BPMN task sequence.
- Lean value stream mapping waste-analysis notation.
- Customer-journey touchpoint and emotion mapping.
- KYC and AML regulatory detail.
- System integration detail.

## Accessibility requirements

Use text labels for every stage and capability. If colour is used, it must not be the only meaning carrier.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]`
- `examples/horizon-bank/capabilities.md`

## Review criteria

- Stages describe stakeholder value progression, not internal process tasks, systems or regulatory workflow.
- Capability names are stable and reusable.
- The figure does not conflict with later Chapter 14 business strategy coverage.
