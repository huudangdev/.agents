#!/usr/bin/env python3
"""Reject generated docs that are empty, scaffold-only, or template-like."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_PLANNING_DOCS = (
    "docs/prd.md",
    "docs/tasks.md",
    "docs/knowledge.md",
    "docs/decisions.md",
    "docs/memory.md",
    "docs/planning/flows.md",
    "docs/planning/screens.md",
    "docs/planning/diagrams.md",
)

DEFAULT_MIN_WORDS = 80

MIN_WORDS_BY_PATH = {
    "docs/prd.md": 250,
    "docs/tasks.md": 120,
    "docs/knowledge.md": 160,
    "docs/decisions.md": 120,
    "docs/memory.md": 100,
    "docs/planning/flows.md": 120,
    "docs/planning/screens.md": 120,
    "docs/planning/diagrams.md": 100,
    "docs/BRAND_GUIDELINES.md": 200,
    "docs/UI_COMPONENTS_STATE.md": 180,
    "docs/prd_draft.md": 300,
    "docs/ADR_REFACTOR_LOG.md": 120,
}

PLACEHOLDER_PATTERNS = (
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
    re.compile(r"\bstatus:\s*pending\b", re.IGNORECASE),
    re.compile(r"\|\s*pending\s*\|", re.IGNORECASE),
    re.compile(r"\[NEEDS CLARIFICATION:", re.IGNORECASE),
    re.compile(r"\{\{[^}\n]{2,80}\}\}"),
    re.compile(r"<[A-Z0-9_ -]{3,80}>", re.IGNORECASE),
    re.compile(r"^\s*-\s*(Describe|Explain|List|Capture|Record|Insert|Replace)\b", re.IGNORECASE | re.MULTILINE),
    re.compile(r"\b(lorem ipsum|replace this|insert .* here|fill .* in)\b", re.IGNORECASE),
)

DOCS_TO_SKIP = (
    "docs/research/",
    "docs/development/audits/",
)


@dataclass(frozen=True)
class SubstanceIssue:
    relpath: str
    message: str


def normalize_relpath(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def markdown_word_count(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"^---.*?---", " ", text, flags=re.DOTALL)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]{2,}", text))


def is_skipped(relpath: str, include_development: bool) -> bool:
    if relpath.startswith("docs/development/") and include_development:
        return False
    if relpath.startswith("docs/development/"):
        return True
    return any(relpath.startswith(prefix) for prefix in DOCS_TO_SKIP)


def placeholder_hits(text: str) -> list[str]:
    hits: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        match = pattern.search(text)
        if match:
            hits.append(match.group(0).strip())
    return hits


def validate_markdown_file(path: Path, root: Path, *, include_development: bool = False) -> list[SubstanceIssue]:
    relpath = normalize_relpath(path, root)
    if is_skipped(relpath, include_development):
        return []

    issues: list[SubstanceIssue] = []
    text = path.read_text(encoding="utf-8")
    stripped = text.strip()
    if not stripped:
        return [SubstanceIssue(relpath, "file is empty")]

    words = markdown_word_count(stripped)
    min_words = MIN_WORDS_BY_PATH.get(relpath, DEFAULT_MIN_WORDS)
    if words < min_words:
        issues.append(SubstanceIssue(relpath, f"too shallow: {words} words; minimum is {min_words}"))

    hits = placeholder_hits(stripped)
    if hits:
        joined = ", ".join(sorted(set(hits))[:5])
        issues.append(SubstanceIssue(relpath, f"contains template placeholders or scaffold instructions: {joined}"))

    if relpath == "docs/planning/diagrams.md" and "```mermaid" not in stripped:
        issues.append(SubstanceIssue(relpath, "missing Mermaid diagram source"))

    headings = len(re.findall(r"^#{1,6}\s+\S+", stripped, flags=re.MULTILINE))
    if headings >= 3 and words < min_words * 2 // 3:
        issues.append(SubstanceIssue(relpath, "mostly headings with insufficient explanatory content"))

    return issues


def iter_markdown_docs(root: Path, *, include_development: bool) -> list[Path]:
    docs_root = root / "docs"
    if not docs_root.exists():
        return []
    paths = sorted(path for path in docs_root.rglob("*.md") if path.is_file())
    return [path for path in paths if not is_skipped(normalize_relpath(path, root), include_development)]


def validate_docs(
    root: Path,
    *,
    strict_planning: bool = False,
    include_development: bool = False,
    require_docs: bool = False,
    targets: tuple[str, ...] = (),
) -> list[SubstanceIssue]:
    issues: list[SubstanceIssue] = []
    docs_root = root / "docs"
    if require_docs and not docs_root.exists():
        return [SubstanceIssue("docs/", "docs directory is missing")]

    if strict_planning:
        for relpath in REQUIRED_PLANNING_DOCS:
            path = root / relpath
            if not path.exists():
                issues.append(SubstanceIssue(relpath, "required planning doc is missing"))

    if targets:
        paths = [root / relpath for relpath in targets]
    else:
        paths = iter_markdown_docs(root, include_development=include_development)

    seen: set[str] = set()
    for path in paths:
        relpath = normalize_relpath(path, root)
        seen.add(relpath)
        if not path.exists():
            issues.append(SubstanceIssue(relpath, "required doc is missing"))
            continue
        issues.extend(validate_markdown_file(path, root, include_development=include_development))

    if strict_planning:
        for relpath in REQUIRED_PLANNING_DOCS:
            if relpath not in seen and (root / relpath).exists():
                issues.extend(validate_markdown_file(root / relpath, root, include_development=include_development))

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate generated docs contain real project-specific substance.")
    parser.add_argument("--root", default=".", help="Project root containing docs/")
    parser.add_argument("--strict-planning", action="store_true", help="Require the canonical /planning docs package.")
    parser.add_argument("--include-development", action="store_true", help="Also scan docs/development Markdown files.")
    parser.add_argument("--require-docs", action="store_true", help="Fail when docs/ is missing.")
    parser.add_argument("--target", action="append", default=[], help="Specific docs-relative file to validate.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    issues = validate_docs(
        root,
        strict_planning=args.strict_planning,
        include_development=args.include_development,
        require_docs=args.require_docs,
        targets=tuple(args.target),
    )
    if issues:
        print("DOCS SUBSTANCE VALIDATION FAILED")
        for issue in issues:
            print(f"- {issue.relpath}: {issue.message}")
        sys.exit(1)

    print("DOCS SUBSTANCE VALIDATION PASSED")
    print(f"- Root: {root}")


if __name__ == "__main__":
    main()
