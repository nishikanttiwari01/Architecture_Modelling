# Chapter 19 Technical Review

## Metadata

- Chapter: 19, Modelling Data Architecture
- Review date: 2026-07-10
- Reviewer: Codex
- Review type: Technical accuracy
- Outcome: Pass for author review

## Scope Reviewed

- Full Chapter 19 manuscript.
- FIG-19-01 specification and diagram register row.
- Source usage against the five existing data research notes.
- Decision record DEC-027.

## Findings

### Critical

- None.

### Major

- None.

### Minor

- None unresolved.

## Technical Accuracy Checks

- Conceptual, logical and physical data views are separated by question and audience.
- ERDs are used for structure; DFDs for movement and transformation; lineage for origin,
  transformation, responsibility and use.
- The chapter does not present DFD notation as a current formal standard comparable to
  UML or BPMN.
- Ownership, stewardship, master data and reference data are described as
  organisation- and scope-dependent governance concepts.
- Privacy and retention guidance requires jurisdiction-specific verification and does
  not invent a legal rule.
- Runtime sequencing remains in Chapter 18 and infrastructure placement remains in
  Chapter 20.

## Diagram Review Notes

- FIG-19-01 is registered and has a complete PlantUML decision-guide specification.
- No source or export was created because author approval of the specification is
  pending.
- The register status is `Planned`, not `Approved`.

## Source Review Notes

- `[CHEN-ER-1976]`, `[CODD-RELATIONAL-1970]`,
  `[DEMARCO-STRUCTURED-ANALYSIS-1979]`, `[W3C-PROV-DM-2013]` and
  `[DAMA-DMBOK2-2017]` support the factual foundation.
- No new normative notation or unstable version claim was introduced.
- No source text or source diagram was copied.

## Recommendation

Move Chapter 19 to `Ready for Author Approval`. Do not mark the chapter, FIG-19-01 or
DEC-027 approved.
