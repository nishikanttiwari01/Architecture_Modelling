# Chapter 16 Consistency Review

## Review metadata

- Chapter: 16, Modelling Software Structure
- Review date: 2026-07-07
- Reviewer: Codex
- Scope: Cross-chapter terminology, figure status, diagram integration, source and copyright consistency.
- Result: Pass for author review.

## Pass 1: Terminology and cross-chapter consistency

- Result: Pass.
- Findings: The chapter uses `Software system`, `Container (C4)`, `Component (C4)`, `System Context diagram`, `System Landscape diagram`, `Class`, `Deployment diagram` and related terms consistently with `GLOSSARY.md`.
- Findings: The chapter preserves Chapter 15's distinction between process flow and software structure.
- Findings: The chapter reuses Chapter 4 and Chapter 5 rather than re-teaching UML and C4 from scratch.
- Fixes made: Added explicit distinctions between capability, process, software system, container, component, package, class and deployment node.
- Remaining risks: No glossary edits were made because the chapter defines package and dependency views locally and the task scope did not require glossary expansion.

## Pass 2: Case-study consistency

- Result: Pass.
- Findings: Simple Online Store names match the established example style.
- Findings: Horizon Bank names match existing systems and roles used across Chapters 5, 14 and 15.
- Findings: The chapter does not start Chapter 17 or alter Chapter 14 or Chapter 15 content.
- Fixes made: Used consistent names such as Horizon Digital Channels, Payments Platform, Core Deposit System and Financial Crime Platform.
- Remaining risks: None.

## Pass 3: Diagram quality and accessibility

- Result: Pass.
- Findings: FIG-16-01 has a specification, Mermaid source and SVG export.
- Findings: FIG-16-01 remains at `Review` in `DIAGRAM_REGISTER.md`, not `Approved`.
- Findings: The Mermaid source has real line breaks and uses valid CSS such as `stroke-width:1px`.
- Findings: The chapter includes explanatory prose before and after the figure, and does not rely on the figure alone.
- Fixes made: Integrated the required caption exactly as requested.
- Remaining risks: Final book-page layout inspection remains a normal publication step under DEC-014.

## Pass 4: Source and copyright verification

- Result: Pass.
- Findings: The chapter cites registered source keys `[C4-OFFICIAL]` and `[OMG-UML]`.
- Findings: No official standard text or diagram is copied.
- Findings: The selection guide is an original Mermaid flowchart.
- Fixes made: Kept the source section clear that practical selection guidance is the author's interpretation.
- Remaining risks: None.

## Status consistency conclusion

- Chapter 16 manuscript status: `Ready for Author Approval`.
- FIG-16-01 status: `Review`.
- DEC-024 status: `Proposed`.
- Chapter 15 remains `Ready for Author Approval`.
- Chapter 14 remains `Revision Required`.
- Recommendation: status files may be updated to match this review.
