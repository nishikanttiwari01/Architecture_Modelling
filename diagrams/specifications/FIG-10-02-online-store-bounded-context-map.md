# FIG-10-02: Online Store Bounded Context Map

## Purpose

Show how the Simple Online Store can be divided into bounded contexts with clear language and integration relationships.

## Audience

Beginners, software architects, analysts and delivery teams.

## Question answered

Where should one model and language stop and another begin?

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

## Required relationships

- Catalogue provides product information to Ordering.
- Ordering requests payment authorisation from Payment.
- Payment integrates with Payment Provider System.
- Payment publishes `PaymentAuthorised` to Ordering or Fulfilment.
- Ordering requests fulfilment from Fulfilment.
- Fulfilment integrates with Delivery Partner System.
- Support references Order and Shipment status for returns or cases.

## Main flow or structure

Place Ordering near the centre. Place Catalogue, Payment, Fulfilment and Support around it. Place external systems outside the Online Store boundary. Use labelled arrows for dependencies and event publication.

## Alternative and exception flows

Show Support as reading or referencing order and shipment information, not owning the order lifecycle.

## Scope

Simple Online Store bounded contexts and selected relationships.

## Exclusions

- Microservice deployment claims.
- Database ownership details.
- User-interface screens.
- Detailed order fulfilment process sequence.
- Full returns workflow.

## Accessibility requirements

Use text labels for relationship meaning. External systems should be visually distinguishable by boundary and label, not colour alone.

## Source references

- `[DDD-REFERENCE-2015]`
- `examples/simple-online-store/README.md`

## Review criteria

- The diagram does not imply that one bounded context equals one microservice.
- The diagram distinguishes internal contexts from external systems.
- Relationships have clear labels.
- Terms match Chapter 10 and the Simple Online Store example.
- The diagram remains readable at intended book-page width.
