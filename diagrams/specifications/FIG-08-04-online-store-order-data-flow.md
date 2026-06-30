# FIG-08-04 Online Store order data flow

## Purpose

Show a data flow diagram for order placement.

## Audience

Beginners, analysts, integration architects and reviewers.

## Question answered

Where does order data move, which processes transform it, and which data stores or external systems are involved?

## Notation

Informal data flow diagram in PlantUML.

## Required elements

- Customer external entity
- Capture order process
- Authorise payment process
- Create shipment request process
- Order data store
- Payment Provider System
- Delivery Partner System

## Required relationships

- Customer sends basket and delivery details to Capture order
- Capture order writes order data
- Authorise payment sends a payment authorisation request to Payment Provider System
- Payment Provider System returns a payment authorisation result to Authorise payment
- Create shipment request sends a shipment request to Delivery Partner System
- Delivery Partner System returns shipment confirmation and tracking data to Create shipment request

## Main flow or structure

Show movement and transformation of data using only normal DFD concepts: external entities, processes, a data store and labelled directional data flows. The exchanged data must appear as labels on arrows, not as separate data-flow boxes.

## Alternative and exception flows

Show payment declined as a possible payment authorisation result, but do not model the full exception process.

## Scope

Order placement data movement for Simple Online Store.

## Exclusions

No database schema, BPMN task sequence, C4 container structure or deployment detail.

## Accessibility requirements

Use readable arrows, labelled flows and sufficient contrast. Meaning must not depend on colour alone.

## Source references

- DEMARCO-STRUCTURED-ANALYSIS-1979
- Simple Online Store example file

## Review criteria

- Data flows are labelled with information names.
- Payment and shipment requests and results are direct labelled arrows, not rectangular nodes.
- Processes are verbs, data stores are nouns and external entities are clear.
- The diagram is not confused with an ERD or BPMN process.
- It has no clipped text or overlapping labels.
