# FIG-12-03: Horizon Bank Payment Authorisation Matrix

## Purpose

Show who or what may perform selected payment actions, and under which conditions.

## Audience

Beginners, product owners, architects, developers, operations, compliance reviewers and auditors.

## Question answered

Which subjects may perform which payment actions, and where are conditional approvals or separations required?

## Notation

Authorisation matrix as a structured table. Markdown table is acceptable for the chapter, with SVG export only if a publication figure is later required.

## Required elements

- Retail Customer.
- Operations Analyst.
- Compliance Officer.
- Payments Platform service identity.
- Core Deposit System service identity.
- Actions: create own payment, approve high-value payment, repair exception, override screening result, submit core posting request, view audit history.
- Conditions and review notes.

## Required relationships

- Retail Customer can create own payment only for entitled accounts.
- Operations Analyst can repair operational exceptions only under assignment and separation rules.
- Compliance Officer can review or approve screening-related actions within policy authority.
- Payments Platform service identity can submit posting requests only for authorised payments.
- Core Deposit System service identity can return posting results but cannot initiate customer payments.

## Main flow or structure

Use rows for subjects and columns for payment actions, or rows for subject-action pairs if conditions require more space. Use explicit values such as Allow, Deny and Conditional. Include a conditions column.

## Alternative and exception flows

Show high-value or manual-repair paths as conditional rather than universally allowed.

## Scope

Outgoing retail payment authorisation in the Horizon Bank case study.

## Exclusions

- Full policy language.
- Jurisdiction-specific regulatory rules.
- Detailed identity-provider configuration.
- User-interface permission screens.

## Accessibility requirements

Do not use ticks, crosses or colour as the only meaning carrier. Include text values in every relevant cell.

## Source references

- `[NIST-SP-800-207]`
- `[OWASP-AUTH-CHEATSHEETS-2026]`
- `[OWASP-ASVS-5.0.0]`

## Review criteria

- Subjects, actions, resources and conditions are explicit.
- Authentication is not treated as sufficient authorisation.
- Service identities are reviewed separately from human users.
- Maker-checker or separation concerns are visible where relevant.
