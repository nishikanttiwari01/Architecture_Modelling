# Source Note: NYGARD-ADR-2011

## Bibliographic details

- Organisation or author: Michael Nygard
- Title: Documenting Architecture Decisions
- Version: Original public article
- Publication date: 2011-11-15
- Access date: 2026-07-02
- URL or identifier: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Source type: Primary-origin practitioner source

## Supported claims

- Claim: Architecture Decision Records (ADRs) are lightweight records for architecturally significant decisions and their rationale.
- Intended chapter(s): Chapters 13, 23 and 63 repository practice.
- Normative or interpretive: Primary-origin practitioner source for the ADR format popularised by Nygard.

- Claim: ADRs are usually small, numbered text records kept with the project source, with status, context, decision and consequences.
- Intended chapter(s): Chapters 13, 23 and 63.
- Normative or interpretive: Primary-origin source for the common lightweight ADR pattern.

- Claim: Superseded decisions should be retained rather than deleted.
- Intended chapter(s): Chapters 13, 23 and 63.
- Normative or interpretive: Practitioner guidance consistent with this repository's decision-log practice.

## Relevant summary

Nygard's 2011 article frames ADRs as small, maintainable records for decisions that affect structure, non-functional characteristics, dependencies, interfaces or construction techniques. The article recommends keeping ADRs in the project repository, numbering them sequentially, recording status, context, decision and consequences, and retaining superseded decisions with a clear status.

For Chapter 13, ADRs should be taught as a textual modelling companion rather than a visual notation. They explain why a model or design choice was made, what alternatives were considered and what consequences reviewers should remember later.

The original lightweight pattern emphasises status, context, decision and consequences. Recording alternatives considered is useful and common in later local variants, including the Chapter 13 Horizon Bank teaching example, but it should not be attributed as a mandatory field in Nygard's original pattern.

## Terminology and version notes

Use source key `[NYGARD-ADR-2011]`.

ADR practice has many later variants, but this note supports the lightweight pattern used in this repository's `DECISIONS.md`.

## Copyright or reuse notes

Do not copy the article's template or prose verbatim into the manuscript. Paraphrase and use the repository's existing decision-log style for examples.

## Verification status

Checked
