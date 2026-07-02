# FIG-12-01: Online Store Trust Boundary View

## Purpose

Show the main trust contexts for customer login and checkout in the Simple Online Store, including the basis for each boundary.

## Audience

Beginners, solution architects, security reviewers and platform teams.

## Question answered

Where does the trust basis change between the customer, the Online Store, identity support, restricted data and provider systems?

## Notation

Conceptual security architecture view using labelled boundaries, actors, systems and directional flows. PlantUML is the intended source tool after author approval.

## Required elements

- Customer device.
- Public network.
- Online Store edge endpoint.
- Online Store application runtime.
- Order and payment data store.
- Identity Service, labelled as an external supporting security service introduced only for this security view.
- Payment Provider System.
- Delivery Partner System.
- Customer Support Agent or operations support role.
- Controlled support interface for privileged access.
- Trust boundary labels that state the basis of the boundary, such as administrative authority, identity authority, data custody, security policy, execution environment, network enforcement or organisational responsibility.

## Required relationships

- Customer device sends login, account and checkout traffic through the public network.
- Public network traffic enters the Online Store edge as a public request entering a controlled edge, not as an authenticated interaction.
- Edge endpoint filters, routes and forwards a filtered and routed request to the application runtime. Do not label this as complete validation.
- Application runtime performs authentication-result validation, session validation, input validation, authorisation and business-rule enforcement before protected business actions.
- Application runtime reads and writes order and payment data.
- Application runtime delegates customer identity establishment to the Identity Service.
- Application runtime sends payment-provider transaction requests to the Payment Provider System.
- Application runtime or worker sends fulfilment requests to the Delivery Partner System.
- Customer Support Agent or operations support role reaches production support functions only through the controlled support interface.
- Privileged support access shows authentication, access authorisation and audit logging. It must not show generic direct access to the production database.

## Main flow or structure

Arrange the view left to right from customer and public network to store edge, application runtime, restricted data and provider systems. Draw boundaries as labelled containers. Use arrows only for meaningful crossings that require review.

## Alternative and exception flows

Show support access as a separate controlled path. Do not show every failed-login or checkout exception.

## Scope

Customer login, account access, checkout and controlled support access for the Simple Online Store security context.

## Exclusions

- Firewall rule inventory.
- Detailed identity-provider protocol steps.
- Database schema.
- Kubernetes runtime detail.
- Provider-side internal architecture.
- Full privileged-access-management workflow.

## Accessibility requirements

Do not rely on colour alone for boundary type or control strength. Use boundary labels, relationship labels and a short legend if colour is used.

## Source references

- `[NIST-SP-800-207]`
- `[OWASP-AUTH-CHEATSHEETS-2026]`
- `[OWASP-THREAT-MODELLING-2026]`

## Review criteria

- Each boundary states the basis for trust change.
- External, internal and trusted are not used as synonyms.
- Each crossing has a labelled flow and an explicit review concern.
- Support access is not hidden inside customer traffic.
- External provider systems remain outside the Online Store administrative boundary.
- The view does not claim that network placement alone grants access.
