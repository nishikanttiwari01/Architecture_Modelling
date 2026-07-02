# FIG-12-02: Online Store Customer Authentication Sequence

## Purpose

Show one delegated customer authentication pattern and the later access decision for account or order access.

## Audience

Beginners, developers, identity teams, testers and security reviewers.

## Question answered

How does the Online Store establish customer identity, and where is that authentication result separated from access authorisation?

## Notation

UML sequence diagram. PlantUML is the intended source tool after author approval.

## Required elements

- Customer.
- Browser or mobile app.
- Online Store web/API runtime.
- Identity Service, labelled as an external supporting security service for this security view.
- Application session or token handling, shown either as a separate participant or a note.
- Protected account or order action after authentication.
- Access decision at the Online Store before the protected action is performed.

## Required relationships

- Customer requests a protected account or order function.
- Online Store redirects or delegates the customer to the Identity Service.
- Customer authenticates directly with the Identity Service.
- Identity Service returns an authentication result to the Online Store.
- Online Store validates the result and creates or updates an application session.
- Customer requests a protected action using the session.
- Online Store checks whether the authenticated customer is authorised for that action and resource.
- Online Store permits or rejects the protected action.

## Main flow or structure

Show a successful delegated authentication path first, then the separate protected-action request and access decision. Use clear message labels and response arrows. Highlight that authentication establishes identity, not complete permission for every action.

## Alternative and exception flows

Include one compact alternate path for failed authentication or rejected access only if it remains readable.

## Scope

Customer authentication and first protected access decision for a beginner Online Store example.

## Exclusions

- Full OAuth, OpenID Connect or SAML protocol detail.
- Password storage design.
- Device fingerprinting or fraud scoring.
- Session expiry, logout, refresh, revocation, account recovery or multi-factor enrolment details.
- Complete access-control policy.

## Accessibility requirements

Keep message labels concise. Use textual annotations for sensitive credential, authentication result and session handling where needed.

## Source references

- `[OWASP-AUTH-CHEATSHEETS-2026]`
- `[OWASP-ASVS-5.0.0]`

## Review criteria

- Authentication is not confused with access authorisation.
- The customer authenticates with the Identity Service, not by sending credentials through every internal component.
- Sensitive credential, authentication result and session movements are visible enough for review.
- The diagram does not imply that session creation proves expiry, renewal, revocation or theft resistance.
- Failed authentication or rejected access is shown only if it does not obscure the main teaching path.
