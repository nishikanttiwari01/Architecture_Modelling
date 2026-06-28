#!/usr/bin/env python3
"""Check common terminology and style violations in the manuscript."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"

RULES = [
    (re.compile("\u2014"), "em dash is not allowed"),
    (re.compile(r"(?<!Unified )\bmodeling\b", re.I), "use British spelling 'modelling' unless it is the official name Unified Modeling Language"),
    (re.compile(r"\borganization\b", re.I), "use British spelling 'organisation'"),
    (re.compile(r"\bauthorization\b", re.I), "use British spelling 'authorisation'"),
    (re.compile(r"BIAN Service Domain(?:s)? (?:is|are) (?:a |the )?microservice", re.I),
     "do not equate a BIAN Service Domain directly with a microservice"),
    (re.compile(r"C4 container means (?:a )?Docker", re.I),
     "a C4 container does not automatically mean Docker"),
]


def main() -> int:
    findings = []
    for path in MANUSCRIPT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            for pattern, message in RULES:
                if pattern.search(line):
                    findings.append((path, line_no, message, line.strip()))
    if findings:
        for path, line_no, message, line in findings:
            print(f"{path.relative_to(ROOT)}:{line_no}: {message}\n  {line}")
        print(f"\n{len(findings)} terminology/style finding(s).")
        return 1
    print("Terminology and basic style checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
