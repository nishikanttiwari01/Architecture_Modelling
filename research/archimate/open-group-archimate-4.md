# Source Note: OPEN-GROUP-ARCHIMATE-4

## Bibliographic details

- Organisation or author: The Open Group
- Title: ArchiMate 4 Specification
- Version: 4
- Publication date: 27 Apr 2026
- Access date: 2026-06-29
- URL or identifier: https://publications.opengroup.org/standards/archimate/c260 and https://publications.opengroup.org/i260
- Source type: Official specification and official publication metadata

## Licence or access conditions

The public publication page identifies C260 as the official ArchiMate 4 Specification and states that it is available through Open Group licensing paths. The non-member page for I260 states that the specification can be downloaded free of charge for non-commercial use, starts with a free personal 90-day Evaluation License, can continue under a free perpetual non-commercial licence for internal use, and requires an annual commercial licence for commercial purposes.

The member licence text shown on the public product page includes an artificial intelligence use restriction. Because of that restriction, this source note uses only publicly visible Open Group publication metadata and product-page summaries. The specification document itself was not downloaded or incorporated into this AI-assisted drafting session.

## Supported claims

- Claim: ArchiMate 4 is the current official ArchiMate specification from The Open Group and supersedes ArchiMate 3.2.
- Intended chapter(s): Chapter 7, ArchiMate; Appendix D, ArchiMate Quick Reference; later diagram selection and repository-practice chapters.
- Normative or interpretive: Normative for version, status and publication metadata.

- Claim: ArchiMate is an open and independent modelling language for Enterprise Architecture that helps describe, analyse and visualise relationships among business domains.
- Intended chapter(s): Chapter 7, ArchiMate.
- Normative or interpretive: Normative for the language purpose, paraphrased from The Open Group publication page.

- Claim: ArchiMate 4 changes include replacing the term `layer` with `domain`, merging behaviour elements across former layers into generic service, process, function and event elements, replacing implementation event with the generic event element, merging business/application/technology collaborations into one collaboration element, replacing business role with a generic role element, moving path to the common domain, and allowing relationship multiplicity.
- Intended chapter(s): Chapter 7, ArchiMate.
- Normative or interpretive: Normative for the listed changes as public Open Group release information; interpretive for beginner teaching impact.

## Relevant summary

The Open Group publication page identifies ArchiMate 4 as an adopted Open Group Standard, product code C260, published on 27 Apr 2026. It says the standard defines an open and independent modelling language for Enterprise Architecture and gives enterprise architects a notation for describing, analysing and visualising relationships among business domains.

The public page describes Version 4 as a substantial evolution intended to clean up and streamline the standard. For Chapter 7, the most relevant teaching changes are:

- The formal term `domain` replaces the older `layer` framing.
- Behaviour elements are generic across domains, with service, process, function and event no longer presented as separate business, application or technology variants.
- The generic `Role` element replaces `Business Role`.
- A single `Collaboration` element replaces business, application and technology collaboration variants.
- `Implementation Event` is replaced by the generic `Event` element.
- `Gap`, `Constraint`, `Contract`, `Representation`, and layer-specific interaction elements are removed.
- `Path` is part of the Common Domain.
- Relationships can have multiplicity.

The companion white paper page, `The Motivation for Changes in the ArchiMate 4 Specification`, is also an official Open Group publication. The page identifies it as W262, by Marc Lankhorst and Jean-Baptiste Sarrodie, published on 27 Apr 2026. It was not downloaded into this AI session.

## Terminology and version notes

Chapter 7 should use `[OPEN-GROUP-ARCHIMATE-4]` as the current normative source key. `[OPEN-GROUP-ARCHIMATE-3.2]` remains a historical source note and should not be presented as current.

For beginner readability, Chapter 7 may mention that many practitioners still say "business layer", "application layer" and "technology layer". The formal ArchiMate 4 wording should be introduced as `domain`, and diagram specifications should use ArchiMate 4 elements.

The Chapter 7 draft and specifications should avoid treating removed 3.2 elements as current ArchiMate 4 notation. Where the teaching needs to explain a change from one architecture state to another, it should use `Plateau`, `Work Package`, `Deliverable`, `Outcome`, `Assessment`, or prose, rather than the removed `Gap` element.

## Important differences from ArchiMate 3.2 for Chapter 7

| Topic | ArchiMate 3.2 wording or element | ArchiMate 4 impact for Chapter 7 |
|---|---|---|
| Overall structure | Layers and aspects | Use `domain` as the formal term. Explain old layer wording only as familiar practitioner shorthand. |
| Behaviour | Business, application and technology behaviour variants | Teach the common pattern: active structure element assigned to a process or function, which realises a service. |
| Role | Business Role | Use generic `Role`. Explain actors as behaviour-capable entities and roles as responsibilities those actors perform. |
| Collaboration | Business/Application/Technology Collaboration | Use generic `Collaboration` where collaboration is needed. |
| Implementation event | Implementation Event | Use generic `Event`. |
| Gap | Gap | Do not use as a current ArchiMate 4 element in Chapter 7 diagrams. |
| Constraint | Constraint | Do not use as a current ArchiMate 4 element. Use requirement, principle, outcome, assessment or prose as appropriate. |
| Contract and representation | Contract, Representation | Avoid in the beginner chapter unless later source review justifies a historical note. |
| Path | Technology-layer path | Treat `Path` as a Common Domain element. |
| Relationships | No relationship multiplicity in earlier wording | Relationship multiplicity is available in ArchiMate 4, but Chapter 7 should not teach it beyond a brief mention because it is not needed for the beginner examples. |

## Copyright or reuse notes

Do not copy The Open Group diagrams, metamodel tables or specification text into the manuscript. Use only short source keys in draft prose and original diagrams/specifications. Do not incorporate licensed specification content into generated text beyond public product-page metadata and paraphrased high-level release information.

## Chapter 14 usage: motivation and strategy elements and relationship verification

Chapter 14 and figure `FIG-14-01` use the following ArchiMate concept names as element types: `Driver`, `Goal`, `Outcome`, `Capability`, `Course of Action` and `Work Package`. These element names are treated here as widely published, public-metadata-level concept names for the motivation, strategy and implementation-and-migration areas of ArchiMate. `Constraint` is not used as a current ArchiMate 4 element, because the public release information for ArchiMate 4 lists `Constraint` among the removed elements (see the differences table above).

Relationship verification note (important): the exact ArchiMate 4 relationship types, their allowed source and target element pairs, their directions, and any derived-relationship rules are defined in the licensed ArchiMate 4 specification text. Under the member licence artificial-intelligence use restriction recorded in the licence section above, that specification text has not been downloaded or incorporated into this AI-assisted drafting session. Therefore this repository cannot, within its own source policy, assert specific formal ArchiMate 4 relationship types and directions (for example, which relationship formally connects a `Driver` to a `Goal`, or a `Goal` to an `Outcome`) as verified against an approved primary source.

Consequence for Chapter 14 and `FIG-14-01`:

- The figure is classified as an `ArchiMate-informed strategy traceability teaching view`, not as a formal ArchiMate view.
- Its connectors are simplified, directional teaching traceability links carrying neutral verbs (for example, `raises`, `sets`, `needs`, `guides`, `delivers`). They are explicitly not presented as formal ArchiMate relationship notation.
- The element concept names above are used, and `Constraint` is avoided, but no formal relationship semantics are claimed.
- A licensed human reviewer with lawful access to the ArchiMate 4 specification should confirm the exact formal relationships and directions before any future upgrade of the figure to a formal ArchiMate view. Until then, the simplified teaching-link classification stands.

This treatment is consistent with `AGENTS.md` (use only public product-page metadata and paraphrased release information; do not incorporate licensed specification content) and with `SOURCE_POLICY.md` (a source must be represented accurately and only support claims it actually supports).

## Verification status

Checked. Chapter 14 relationship-semantics verification against the licensed specification text is intentionally not performed in this AI-assisted session; see the Chapter 14 usage note above.
