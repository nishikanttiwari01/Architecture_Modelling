# FIG-12-01: Online Store Trust Boundary View

## Purpose

Show the main trust contexts for customer login and checkout in the Simple Online Store.

## Audience

Beginners, solution architects, security reviewers and platform teams.

## Question answered

Where does trust change between the customer, the Online Store, restricted data and external provider systems?

## Notation

Conceptual security architecture view using labelled boundaries, actors, systems and directional flows. PlantUML is the intended source tool after author approval.

## Required elements

- Customer device.
- Internet or external network.
- Online Store edge endpoint.
- Online Store application runtime.
- Order and payment data store.
- Payment Provider System.
- Delivery Partner System.
- Operations access path.
- Trust boundary labels for external customer context, store platform context, restricted data context and external provider context.

## Required relationships

- Customer device sends login and checkout traffic to the Online Store edge.
- Edge endpoint forwards validated application traffic to the application runtime.
- Application runtime reads and writes order and payment data.
- Application runtime sends payment authorisation requests to the Payment Provider System.
- Application runtime or worker sends fulfilment requests to the Delivery Partner System.
- Operations access reaches the production environment through a separate controlled path.

## Main flow or structure

Arrange the view left to right from customer and internet to store platform, restricted data and external providers. Draw trust boundaries as labelled containers. Use arrows only for meaningful crossings that require review.

## Alternative and exception flows

Show operations access as a separate support path. Do not show every failed-login or checkout exception.

## Scope

Customer login and checkout security context for the Simple Online Store.

## Exclusions

- Firewall rule inventory.
- Detailed identity-provider protocol steps.
- Database schema.
- Kubernetes runtime detail.
- Provider-side internal architecture.

## Accessibility requirements

Do not rely on colour alone for trust level. Use boundary labels, relationship labels and a short legend if colour is used.

## Source references

- `[NIST-SP-800-207]`
- `[OWASP-AUTH-CHEATSHEETS-2026]`
- `[OWASP-THREAT-MODELLING-2026]`

## Review criteria

- Trust boundaries represent a change in trust assumption, not decorative grouping.
- Each crossing has a labelled flow.
- Operations access is not hidden inside customer traffic.
- External provider systems remain outside the Online Store trust boundary.
- The view does not claim that internal network placement alone proves trust.
