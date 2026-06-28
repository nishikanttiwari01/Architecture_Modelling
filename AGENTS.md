# AGENTS.md

## Mission

Help create and maintain **Architecture Modelling: A Practical Beginner’s Handbook** as a reliable, beginner-friendly and technically accurate book. The repository, not the conversation, is the source of truth.

## Mandatory reading order before any task

1. `BOOK_PLAN.md`
2. `STATUS.md`
3. `STYLE_GUIDE.md`
4. `SOURCE_POLICY.md`
5. `DECISIONS.md`
6. `GLOSSARY.md`
7. The target chapter
8. The preceding and following chapter, where they exist
9. Relevant research notes and diagram-register entries

Do not ask the author to repeat information that already exists in these files.

## Task execution rules

- Work only on the requested scope unless a small adjacent correction is essential.
- Preserve approved structure and terminology unless the task explicitly changes them.
- Never mark a chapter `Approved`; only the author may do that.
- Never fabricate a standard, BIAN concept, quotation, version number or source.
- For unstable or current factual claims, use current primary sources and record them.
- Prefer official sources: OMG for UML/BPMN/DMN, The Open Group for ArchiMate, official C4 documentation, and BIAN for BIAN material.
- Separate established facts, interpretation and author recommendations.
- Keep the beginner explanation accurate; do not simplify it into falsehood.
- Do not equate a BIAN Service Domain with one microservice unless the design explicitly justifies it.
- Do not mix business-process, application and infrastructure detail on one diagram without a stated reason.
- Do not insert copyrighted standards text or diagrams verbatim. Paraphrase and create original diagrams.

## Chapter workflow

For a new or revised chapter:

1. Confirm its purpose and reader outcomes from the chapter file.
2. Check dependencies and glossary terms.
3. Research missing facts using `SOURCE_POLICY.md`.
4. Add source notes under `research/<topic>/`.
5. Draft using `templates/chapter-template.md` or `templates/modelling-topic-template.md`.
6. Add required diagram entries to `DIAGRAM_REGISTER.md` before producing diagrams.
7. Keep examples consistent with `examples/simple-online-store/` and `examples/horizon-bank/`.
8. Run the relevant review checklist.
9. Update `STATUS.md`.
10. Add a concise entry to `CHANGELOG.md`.
11. Add significant choices to `DECISIONS.md`.

## Required end-of-task report

At the end of a Codex task, report:

- Files changed
- What was completed
- Checks run and their results
- New sources added
- Decisions recorded
- Remaining work or risks

## Status rules

Allowed chapter statuses:

- Planned
- Researching
- Outlined
- Drafting
- Diagramming
- Under Review
- Revision Required
- Ready for Author Approval
- Approved
- Published

Update status only when the definition in `WORKFLOW.md` has been met.

## Writing rules

- Use British English.
- Explain simply first, introduce formal language second, and demonstrate third.
- Define an acronym at first use in every standalone chapter.
- Use short paragraphs and informative headings.
- Use tables when they improve comparison, not merely decoration.
- Avoid unexplained jargon, marketing language and vague claims.
- Avoid em dashes; use commas, parentheses or full stops.
- Use consistent terms from `GLOSSARY.md`.
- Every modelling chapter should answer:
  - What is it?
  - What question does it answer?
  - Who uses it?
  - What are its key elements?
  - When should it be used?
  - When should it not be used?
  - How does it compare with alternatives?
  - What mistakes are common?

## Diagram rules

- Give every diagram an ID in the form `FIG-<chapter>-<sequence>`.
- Record it in `DIAGRAM_REGISTER.md`.
- Store editable sources under `diagrams/source/`.
- Store publication exports under `diagrams/exported/svg/` and, only when needed, `diagrams/exported/png/`.
- Prefer SVG for publication.
- Include title, purpose, audience, notation, scope, legend where needed, and a meaningful caption.
- Label important relationships and direction.
- Use colour sparingly and never as the only carrier of meaning.
- Maintain accessibility through sufficient contrast and textual explanation.

## Source and citation rules

- Create one source note per meaningful source using `templates/source-note-template.md`.
- Register major sources in `SOURCE_REGISTER.md`.
- Record access date and the standard or framework version.
- Never cite a search-results page when the original source is available.
- Do not rely on blogs for normative definitions when an official specification exists.
- Keep quotations minimal and compliant with copyright.

## Git safety

- Do not run destructive commands such as `git reset --hard`, force push or branch deletion unless explicitly instructed.
- Do not push, merge, tag or create releases unless explicitly instructed.
- Prefer focused commits with a clear purpose.
- Do not commit generated temporary files, local caches or secrets.

## Required repository checks

Run these before completing a substantial task:

```text
python scripts/check-structure.py
python scripts/check-links.py
python scripts/check-terminology.py
python scripts/word-count.py
```

## Quality gates

A chapter is not ready for author approval until:

- Required sections are complete.
- Claims requiring sources have citations or source notes.
- Required diagrams exist or are explicitly deferred.
- Repository structure check passes.
- Terminology checks pass.
- Links check passes.
- Technical, beginner, consistency and source reviews are complete.
- Open issues are documented.

Last updated: 2026-06-28
