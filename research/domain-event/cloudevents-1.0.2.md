# Source Note: CNCF-CLOUDEVENTS-1.0.2

## Bibliographic details

- Organisation or author: CloudEvents project under CNCF
- Title: CloudEvents specification
- Version: 1.0.2 release, compatible with CloudEvents v1.0
- Publication date: 2022-02-05 according to the project site; GitHub release page shows 2022-02-06
- Access date: 2026-06-30
- URL or identifier: https://cloudevents.io/ and https://github.com/cloudevents/spec/releases
- Source type: Official specification

## Supported claims

- Claim: CloudEvents is a specification for describing event data in a common way across services, platforms and transports.
- Claim: In CloudEvents 1.0.2, the required context attributes are `id`, `source`, `specversion` and `type`; `time` is optional.
- Claim: CloudEvents standardises event envelope and context metadata, not the business meaning of a domain-event payload.
- Intended chapter(s): Chapter 10 and later event architecture chapters
- Normative or interpretive: Normative for CloudEvents envelope terminology and version-sensitive claims.

## Relevant summary

The CloudEvents project describes CloudEvents as a specification for event data portability across services and platforms. The project site records CloudEvents 1.0.2 as the current stable release noted on the site, with compatibility to the existing v1.0 specification.

For Chapter 10, use CloudEvents to explain why event envelope and context metadata are different from the business meaning of the event payload. The required 1.0.2 context attributes are `id`, `source`, `specversion` and `type`; `time` is optional. Do not imply that all domain events must use CloudEvents.

## Terminology and version notes

Record version-sensitive references as CloudEvents 1.0.2 unless a later stable CloudEvents event-format release is verified. CloudEvents SQL has a separate v1.0.0 release and should not be mixed with the core event specification unless explicitly needed.

## Copyright or reuse notes

Paraphrase specification concepts. Use original event examples.

## Verification status

Checked
