# Architecture and Editorial Decision Log

Use the format below for all material decisions. Do not delete superseded decisions; mark their status and link the replacement.

## DEC-001: Use Markdown and Git as the source of truth

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Store the manuscript, research notes, diagrams, reviews and project-control files in this repository.
- **Reason:** It provides durable memory, version history, portability and Codex access.
- **Consequences:** Chat history is supplementary and must not be treated as the authoritative project state.

## DEC-002: Use two continuing case studies

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Use a simple online store for introductory examples and Horizon Bank for enterprise and BIAN examples.
- **Reason:** One simple example supports beginners, while one consistent banking example supports realistic traceability.
- **Consequences:** Names and facts in both examples must remain consistent across chapters.

## DEC-003: Make BIAN a complete practical part

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Dedicate Part V to a full business-and-technology BIAN implementation for a fictional full-service bank.
- **Reason:** BIAN should be taught as an enterprise banking reference architecture, not only as a technical API or microservices topic.
- **Consequences:** The part includes strategy, capabilities, all major bank process families, information, applications, security, operations and migration.

## DEC-004: Do not map Service Domains automatically to microservices

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Treat BIAN Service Domains as logical business capability boundaries. Physical service boundaries require separate design justification.
- **Reason:** Ownership, transaction consistency, scale, security, data and legacy constraints affect implementation.
- **Consequences:** Every physical mapping must state its rationale.

## DEC-005: Use British English and no em dashes

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Use British spelling and replace em dashes with commas, parentheses, colons or full stops.
- **Reason:** Maintain a consistent authorial style.

## DEC-006: Author approval is a manual gate

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Codex and automated scripts may move a chapter to `Ready for Author Approval`, but only the author can mark it `Approved`.
- **Reason:** Editorial responsibility remains with the author.

## Decision template

```markdown
## DEC-NNN: Decision title

- **Status:** Proposed | Approved | Superseded | Rejected
- **Date:** YYYY-MM-DD
- **Decision:**
- **Context:**
- **Alternatives considered:**
- **Reason:**
- **Consequences:**
- **Related chapters/files:**
- **Supersedes / superseded by:**
```
