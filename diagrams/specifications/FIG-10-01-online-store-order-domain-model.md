# FIG-10-01: Online Store Order Domain Model

## Purpose

Show the main concepts inside the Ordering bounded context without making Catalogue, Payment or Fulfilment concepts look internally owned by Ordering.

## Audience

Beginners, analysts, software architects and developers.

## Question answered

Which concepts does the Ordering bounded context own, and which neighbouring concepts are only references?

## Notation

Conceptual domain model using PlantUML class-style boxes without implementation attributes or methods.

## Required elements

- Ordering bounded context
- Customer
- Basket
- Basket Item
- Order
- Order Line
- Product Snapshot or Product Reference
- Delivery Address as a value object
- Payment Attempt as externally owned reference
- Shipment as externally owned reference

## Required relationships

- Customer owns zero or more Baskets.
- Basket contains one or more Basket Items.
- Basket Item refers to Product Snapshot or Product Reference.
- Customer places zero or more Orders.
- Order contains one or more Order Lines.
- Order Line uses Product Snapshot or Product Reference.
- Order has one Delivery Address value object.
- Order may relate to zero or more Payment Attempts as external references.
- Order may relate to zero or more Shipments as external references.

## Main flow or structure

Keep Customer, Basket, Basket Item, Order, Order Line, Product Snapshot and Delivery Address inside a visible Ordering bounded-context boundary. Place Payment Attempt and Shipment outside that boundary and label them as externally owned references.

## Alternative and exception flows

Show optional Payment Attempt and Shipment references with `0..*` cardinality. Do not model payment authorisation, settlement, shipment dispatch or returns.

## Scope

Conceptual domain model for the Simple Online Store Ordering bounded context.

## Exclusions

- Catalogue-owned product master data.
- Payment processing internals.
- Fulfilment and delivery internals.
- Database tables, keys and columns.
- API resources and endpoints.
- UML operations or implementation methods.
- Returns and refund handling.

## Accessibility requirements

Use plain labels, readable font sizes, visible cardinalities and relationship labels. Do not rely on colour to distinguish internal ownership from external references.

## Source references

- `[DDD-REFERENCE-2015]`
- `examples/simple-online-store/README.md`

## Review criteria

- The figure reads as a conceptual domain model, not a physical data model.
- Ordering ownership is visually clear.
- Payment Attempt and Shipment are outside the Ordering boundary or absent from the internal model.
- Basket to Basket Item and Order to Order Line cardinalities are one or more.
- Order to Payment Attempt and Order to Shipment cardinalities are zero or more.
- The model agrees with Chapter 10 prose.
