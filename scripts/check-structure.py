#!/usr/bin/env python3
"""Validate the handbook repository structure and chapter metadata."""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"
EXPECTED_CHAPTERS = list(range(1, 64))

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "BOOK_PLAN.md",
    "STATUS.md",
    "DECISIONS.md",
    "STYLE_GUIDE.md",
    "SOURCE_POLICY.md",
    "GLOSSARY.md",
    "CHANGELOG.md",
    "WORKFLOW.md",
    "QUALITY_CHECKLIST.md",
    "DIAGRAM_REGISTER.md",
    "SOURCE_REGISTER.md",
    "CODEX_PROMPTS.md",
    "templates/chapter-template.md",
    "templates/modelling-topic-template.md",
    "templates/diagram-review-template.md",
    "templates/source-note-template.md",
    "templates/bian-scenario-template.md",
    "scripts/build-book.py",
    "scripts/build-book.ps1",
    "scripts/check-structure.py",
    "scripts/check-links.py",
    "scripts/check-terminology.py",
    "scripts/word-count.py",
    ".github/workflows/validate.yml",
]

REQUIRED_DIRECTORIES = [
    "manuscript/00-front-matter",
    "manuscript/part-01-fundamentals",
    "manuscript/part-02-modelling-languages",
    "manuscript/part-03-diagram-selection",
    "manuscript/part-04-architecture-lifecycle",
    "manuscript/part-05-bian-case-study",
    "manuscript/part-06-practical-reference",
    "manuscript/appendices",
    "research/uml",
    "research/c4",
    "research/bpmn",
    "research/archimate",
    "research/bian",
    "research/data",
    "research/security",
    "research/dmn",
    "research/domain-event",
    "research/infrastructure",
    "research/modelling-tools",
    "research/banking",
    "diagrams/source/plantuml",
    "diagrams/source/mermaid",
    "diagrams/source/drawio",
    "diagrams/source/archimate",
    "diagrams/exported/svg",
    "diagrams/exported/png",
    "examples/simple-online-store",
    "examples/horizon-bank",
    "reviews/technical-review",
    "reviews/beginner-review",
    "reviews/consistency-review",
    "reviews/final-review",
    "templates",
    "scripts",
]

FRONTMATTER_KEYS = {
    "title",
    "chapter",
    "part",
    "status",
    "author",
    "last_updated",
}


def parse_simple_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML delimiter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing closing YAML delimiter")
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def markdown_chapters() -> dict[int, Path]:
    chapters: dict[int, Path] = {}
    for path in MANUSCRIPT.glob("part-*/*.md"):
        match = re.match(r"(\d+)-", path.name)
        if not match:
            continue
        number = int(match.group(1))
        if number in chapters:
            raise ValueError(
                f"duplicate chapter number {number}: {chapters[number]} and {path}"
            )
        chapters[number] = path
    return chapters


def extract_linked_chapters(path: Path, pattern: str) -> dict[int, str]:
    text = path.read_text(encoding="utf-8")
    return {int(number): title.strip() for number, title in re.findall(pattern, text, re.M)}


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required file: {relative}")

    for relative in REQUIRED_DIRECTORIES:
        if not (ROOT / relative).is_dir():
            errors.append(f"missing required directory: {relative}")

    try:
        chapters = markdown_chapters()
    except ValueError as exc:
        errors.append(str(exc))
        chapters = {}

    actual_numbers = sorted(chapters)
    if actual_numbers != EXPECTED_CHAPTERS:
        missing = sorted(set(EXPECTED_CHAPTERS) - set(actual_numbers))
        extra = sorted(set(actual_numbers) - set(EXPECTED_CHAPTERS))
        errors.append(f"chapter sequence mismatch; missing={missing}, extra={extra}")

    actual_titles: dict[int, str] = {}
    for number, path in sorted(chapters.items()):
        text = path.read_text(encoding="utf-8")
        try:
            metadata = parse_simple_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue

        missing_keys = sorted(FRONTMATTER_KEYS - set(metadata))
        if missing_keys:
            errors.append(
                f"{path.relative_to(ROOT)}: missing frontmatter keys {missing_keys}"
            )

        if metadata.get("chapter") != str(number):
            errors.append(
                f"{path.relative_to(ROOT)}: frontmatter chapter is "
                f"{metadata.get('chapter')!r}, expected {number}"
            )

        heading_match = re.search(r"^#\s+(\d+)\.\s+(.+?)\s*$", text, re.M)
        if not heading_match:
            errors.append(f"{path.relative_to(ROOT)}: missing numbered H1 title")
        else:
            heading_number = int(heading_match.group(1))
            heading_title = heading_match.group(2).strip()
            if heading_number != number:
                errors.append(
                    f"{path.relative_to(ROOT)}: H1 chapter number {heading_number}, "
                    f"expected {number}"
                )
            if metadata.get("title") != heading_title:
                errors.append(
                    f"{path.relative_to(ROOT)}: frontmatter title and H1 differ"
                )
            actual_titles[number] = heading_title

        headings = [
            match.group(2).strip()
            for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", text, re.M)
        ]
        duplicates = sorted(
            title for title, count in collections.Counter(headings).items() if count > 1
        )
        if duplicates:
            errors.append(
                f"{path.relative_to(ROOT)}: duplicate headings {duplicates}"
            )

        for required_heading in [
            "## Chapter purpose",
            "## Reader outcomes",
            "## Prerequisites and dependencies",
            "## Required models and artefacts",
            "## Worked examples",
            "## Source requirements",
            "## Planned chapter structure",
            "## Key takeaways",
            "## Practical exercise",
            "## Review checklist",
            "## Drafting notes",
        ]:
            if required_heading not in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing section {required_heading}"
                )

    status_titles = extract_linked_chapters(
        ROOT / "STATUS.md", r"^\| (\d{2}) \| ([^|]+?) \|"
    )
    toc_titles = extract_linked_chapters(
        MANUSCRIPT / "00-front-matter/table-of-contents.md",
        r"^- \[(\d+)\. ([^\]]+?)\]",
    )
    plan_titles = extract_linked_chapters(
        ROOT / "BOOK_PLAN.md", r"^- \[(\d+)\. ([^\]]+?)\]"
    )

    for label, mapping in [
        ("STATUS.md", status_titles),
        ("table of contents", toc_titles),
        ("BOOK_PLAN.md", plan_titles),
    ]:
        if sorted(mapping) != EXPECTED_CHAPTERS:
            errors.append(f"{label}: does not contain exactly chapters 1 to 63")
        for number in EXPECTED_CHAPTERS:
            if number in actual_titles and mapping.get(number) != actual_titles[number]:
                errors.append(
                    f"{label}: chapter {number} title {mapping.get(number)!r} "
                    f"does not match {actual_titles[number]!r}"
                )

    if errors:
        print("Repository structure check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository structure check passed.")
    print(f"Validated {len(chapters)} numbered chapters (1 to 63).")
    print("BOOK_PLAN.md, STATUS.md, table of contents and chapter titles agree.")
    print("Required control files, directories, frontmatter and chapter sections exist.")
    print("No duplicate chapter headings were found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
