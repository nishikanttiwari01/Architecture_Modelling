# Source Note: EVENT-CONTRACTS-PV51

## Bibliographic details

- Organisation or author: CloudEvents project under the Cloud Native Computing Foundation; AsyncAPI Initiative
- Title: CloudEvents specification; AsyncAPI Specification
- Version: CloudEvents 1.0.2; AsyncAPI 3.1.0
- Publication date: CloudEvents 1.0.2, February 2022; AsyncAPI 3.1.0, January 2026
- Access date: 2026-07-20
- URL or identifier: https://github.com/cloudevents/spec/tree/ce@v1.0.2; https://www.asyncapi.com/docs/reference/specification/v3.1.0
- Source type: Official specifications

## Supported claims

- Claim: CloudEvents standardises common event context and envelope information across services, platforms and transports; it does not define the business meaning of a bank event.
- Claim: AsyncAPI can describe message-driven interfaces using applications, channels, operations and messages without prescribing one transport or implementation.
- Claim: Event and message contracts still need ownership, versioning, delivery, ordering, duplicate, privacy and operational rules.
- Intended chapter(s): 51
- Normative or interpretive: Normative for specification scope; interpretive for Horizon Bank event-contract guidance.

## Relevant summary

CloudEvents provides a vendor-neutral event envelope. In the 1.0 specification line, required context attributes include `id`, `source`, `specversion` and `type`. Those fields improve interoperability and correlation, but they do not make a payload a valid domain event.

AsyncAPI provides a machine-readable way to describe message-driven application interfaces. It can cover event, command, request and response patterns. Horizon Bank still records the business fact or request, producer, consumer, classification, delivery behaviour and evidence outside the transport definition where necessary.

## Terminology and version notes

Do not call every asynchronous message an event. An event records a fact; a command requests an action; a message is the broader carrier. Preserve the verified version in contract metadata.

## Copyright or reuse notes

Paraphrase specification concepts and use original examples.

## Verification status

Checked
