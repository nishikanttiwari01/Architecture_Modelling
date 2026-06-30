# FIG-10-02: Online Store Bounded Context Map

## Purpose

Show explicit relationship direction, upstream/downstream dependency and translation boundaries between Simple Online Store bounded contexts.

## Audience

Beginners, software architects, analysts and delivery teams.

## Question answered

How do the Online Store bounded contexts depend on one another, and where is translation needed?

## Notation

Conceptual context map using PlantUML component-style or package-style boxes.

## Required elements

- Catalogue context
- Ordering context
- Payment context
- Fulfilment context
- Support context
- Payment Provider System
- Delivery Partner System
- Explicit relationship labels for upstream/downstream, Customer/Supplier, Conformist, Anti-Corruption Layer, Open Host Service, Published Language and Separate Ways where applicable

## Required relationships

- Catalogue is upstream of Ordering and exposes an Open Host Service with Published Language for product references.
- Ordering is downstream of Catalogue and uses product references without owning product master data.
- Ordering and Payment use a Customer/Supplier relationship for payment authorisation.
- Payment protects its model from Payment Provider System through an Anti-Corruption Layer.
- Ordering and Fulfilment use a Customer/Supplier relationship for fulfilment requests.
- Fulfilment protects its model from Delivery Partner System through an Anti-Corruption Layer.
- Support is downstream of Ordering and Fulfilment and conforms to selected order and shipment status terms.
- Support uses Separate Ways for internal case handling that does not alter the Ordering model.

## Main flow or structure

Place Ordering centrally. Place Catalogue upstream above or to the left. Place Payment and Fulfilment to the right, with their external provider systems beyond translation boundaries. Place Support below Ordering and Fulfilment. Label arrows with relationship pattern and direction.

## Alternative and exception flows

Show translation boundaries explicitly near Payment Provider System and Delivery Partner System. Do not show physical services, deployment units or databases.

## Scope

Simple Online Store bounded-context relationships and selected context-map patterns.

## Exclusions

- Claims that one bounded context equals one microservice.
- Database ownership details.
- User-interface screens.
- Detailed order fulfilment process sequence.
- Full returns workflow.

## Accessibility requirements

Use text labels for relationship meaning and direction. External systems and translation boundaries should be visually distinguishable by boundary and label, not colour alone.

## Source references

- `[DDD-REFERENCE-2015]`
- `examples/simple-online-store/README.md`

## Review criteria

- The diagram does not imply that one bounded context equals one microservice.
- Upstream and downstream direction is explicit.
- Translation boundaries are visible.
- Context-map pattern labels are readable.
- Terms match Chapter 10 and the Simple Online Store example.
- The diagram remains readable at intended book-page width.
