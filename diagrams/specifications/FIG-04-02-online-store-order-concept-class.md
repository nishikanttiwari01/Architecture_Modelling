# FIG-04-02: Online Store Order Concept Class Diagram

## Purpose

Show a small UML class diagram at analysis level for online store order concepts.

## Audience

Beginners, analysts and developers.

## Question answered

What important order-domain concepts exist, and how are they related?

## Abstraction level

Conceptual analysis view. It shows domain concepts and selected relationships, not database tables or implementation classes.

## Notation

UML class diagram.

## Required elements

- Customer
- Basket
- Product
- Order
- Order Line
- Payment
- Shipment

## Required relationships

- Customer places Order.
- Customer owns Basket.
- Basket references Product.
- Order contains Order Line.
- Order Line refers to Product.
- Order has Payment.
- Order has Shipment.

## Relationship semantics

Association means a meaningful domain relationship. Multiplicity states how many instances can participate. Composition is used where the part belongs to the whole's lifecycle, such as Order Line inside Order. Aggregation is used only for a weaker whole-part reference.

## Main flow or structure

Use a compact conceptual class diagram. Include multiplicities only where they aid beginner understanding, such as one Order containing one or more Order Lines.

## Alternative and exception flows

Not applicable. This is a structural diagram, not a flow diagram.

## Scope

Conceptual order-domain structure for the Simple Online Store.

## Exclusions

No private attributes, persistence annotations, table names, infrastructure or implementation classes.

## Accessibility requirements

Keep class boxes simple and readable. Avoid dense compartments and tiny multiplicity labels.

## Source references

- `[OMG-UML]` for UML class diagram notation.
- `examples/simple-online-store/README.md` for stable information concepts.

## Review criteria

- Diagram is clearly analysis-level, not physical database design.
- Multiplicities are readable and not excessive.
- Composition and aggregation are used sparingly and intentionally.
- Concepts match the repository example.
