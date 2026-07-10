# Remaining Manuscript Completion Design

## Objective

Complete *Architecture Modelling: A Practical Beginner's Handbook* from Chapter 19 through Chapter 63, followed by Appendices A to H. Validate and revise each chapter before proceeding, preserve the repository's approved terminology and structure, and push the verified work to GitHub.

## Scope

The writing scope covers:

- Chapters 19 to 23, completing Part III.
- Chapters 24 to 30, completing Part IV.
- Chapters 31 to 56, completing the BIAN case study in Part V.
- Chapters 57 to 63, completing the practical reference in Part VI.
- Appendices A to H.
- Necessary updates to `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, `GLOSSARY.md`, `SOURCE_REGISTER.md`, `DIAGRAM_REGISTER.md`, research notes, reviews and cross-references.
- Necessary table-of-contents and front-matter reference corrections discovered during final validation.

Previously approved chapters are outside the rewriting scope unless a small adjacent correction is essential for consistency, terminology, links or build validity.

## Delivery approach

Work proceeds sequentially, one chapter at a time. Each chapter is treated as a bounded editorial unit so that factual, structural and terminology defects are found before they spread into later chapters. A part-level consistency review follows the last chapter of each part.

For each chapter:

1. Read its purpose, outcomes, dependencies and drafting notes.
2. Read the preceding and following chapter where present.
3. Read relevant research notes, source records, examples and diagram-register entries.
4. Research missing or unstable factual claims from current primary sources and record source notes.
5. Draft in British English using the approved chapter structure and glossary terminology.
6. Create or update required diagram specifications and register entries before any diagram work.
7. Run the technical, beginner, consistency and source review passes.
8. Run relevant repository checks, correct failures and repeat until the chapter is clean or a documented author-only dependency remains.
9. Update status, changelog and significant decisions.
10. Commit the coherent chapter batch before continuing.

## Diagram constraint

The author has directed the work not to pause for diagram approvals. Repository policy still prohibits creating diagram source before its specification is author-approved. Therefore:

- Required specifications and register entries will be prepared.
- Existing approved specifications may proceed through source creation, rendering and visual review.
- Unapproved specifications will remain awaiting author approval.
- A chapter may be completed editorially with its diagram work explicitly deferred.
- No diagram or chapter will be marked `Approved` by Codex.

## Sources and factual control

Official and primary sources take precedence. Current standards, frameworks and BIAN material will be verified rather than recalled. Each meaningful new source receives a source note and major sources are added to `SOURCE_REGISTER.md`. Established facts, interpretation and author recommendations remain distinct.

BIAN content will preserve the repository's key modelling constraint: a BIAN Service Domain is a logical functional partition and is not automatically one deployable microservice. BIAN version-specific claims will be recorded with their source and access date.

## Validation loop

Chapter validation includes structural completeness, beginner readability, technical accuracy, source support, glossary consistency, cross-chapter consistency, link validity and diagram-register integrity. Findings are repaired and checks rerun before moving on, except for clearly documented author-only approvals.

After the full manuscript and appendices are drafted, run and repair against:

```text
python scripts/check-structure.py
python scripts/check-links.py
python scripts/check-terminology.py
python scripts/validate-diagrams.py
python scripts/check-diagram-register.py
python scripts/word-count.py
```

Run the repository's book build as a final integration check. Completion claims require fresh successful output from the full validation set.

## Status and review outcomes

Codex will never assign `Approved`. A chapter advances only when the definition in `WORKFLOW.md` is met. The expected highest status is `Ready for Author Approval` when all applicable quality gates pass. Where an essential diagram or decision still requires author action, the status and next action will identify that dependency accurately.

## Git delivery

Use focused commits that preserve unrelated user changes. Before pushing, verify the worktree, pull only through a safe non-destructive workflow if the remote has advanced, rerun affected checks after integration, then push the current `main` branch to `origin`. Do not force-push.

## Completion report

The final report will list files changed, completed work, checks and results, new sources, decisions, remaining risks or author-only approvals, commits created and the GitHub push result.
