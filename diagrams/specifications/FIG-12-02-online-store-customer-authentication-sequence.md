# FIG-12-02: Online Store Customer Authentication Sequence

## Purpose

Show the order of interactions used to establish a customer identity before account or order access.

## Audience

Beginners, developers, identity teams, testers and security reviewers.

## Question answered

How does the Online Store establish customer identity, and where are authentication results used?

## Notation

UML sequence diagram. PlantUML is the intended source tool after author approval.

## Required elements

- Customer.
- Browser or mobile app.
- Online Store web/API runtime.
- Identity service.
- Session or token store, if shown as a separate participant.
- Optional account or order action after authentication.

## Required relationships

- Customer submits credentials or starts federated sign-in through the browser or mobile app.
- Browser or mobile app sends authentication request to the Online Store.
- Online Store delegates validation to the identity service.
- Identity service returns authentication success or failure.
- Online Store creates or receives a session or token.
- Customer uses the session or token for a subsequent account or order request.

## Main flow or structure

Show a successful authentication path first. Use clear message labels and response arrows. Highlight that authentication establishes identity, not complete authorisation for every action.

## Alternative and exception flows

Include a compact alternate path for authentication failure or step-up authentication if it remains readable.

## Scope

Customer authentication for a beginner Online Store example.

## Exclusions

- Full OAuth, OpenID Connect or SAML protocol detail.
- Password storage design.
- Device fingerprinting or fraud scoring.
- Complete authorisation policy.

## Accessibility requirements

Keep message labels concise. Use textual annotations for sensitive credential or token handling where needed.

## Source references

- `[OWASP-AUTH-CHEATSHEETS-2026]`
- `[OWASP-ASVS-5.0.0]`

## Review criteria

- Authentication is not confused with authorisation.
- Sensitive credential and token movements are visible enough for review.
- The diagram does not imply that token issuance proves token storage, expiry or theft resistance.
- Failed authentication or step-up handling is shown only if it does not obscure the main teaching path.
