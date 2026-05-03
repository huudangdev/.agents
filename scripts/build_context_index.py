#!/usr/bin/env python3
"""Build a lightweight context index under `.agents/index/`.

This is a deterministic alternative to ad-hoc "read everything" behavior.
The index is intentionally shallow and cheap:
- It records paths, headings, and small metadata.
- It does not attempt semantic summarization or vectorization.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from path_utils import resolve_agents_root


DEFAULT_EXCLUDES = {
    ".git",
    ".next",
    ".venv",
    "venv",
    "dist",
    "build",
    "out",
    "coverage",
    "node_modules",
    "logs",
    "trustgraph/data",
    "trustgraph-viewer/node_modules",
    ".playwright-mcp",
}

DOC_EXTS = {".md", ".mdx"}
CODE_EXTS = {
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".py",
    ".go",
    ".rs",
    ".java",
    ".kt",
    ".swift",
    ".dart",
    ".cs",
    ".php",
    ".rb",
    ".vue",
    ".svelte",
}

HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def norm_rel(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def should_exclude(root: Path, path: Path, excludes: set[str]) -> bool:
    rel = norm_rel(root, path)
    for item in excludes:
        if rel == item or rel.startswith(item.rstrip("/") + "/"):
            return True
    return False


def iter_files(root: Path, excludes: set[str], max_files: int) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        base = Path(dirpath)
        # prune excluded directories early
        pruned: list[str] = []
        for name in list(dirnames):
            candidate = base / name
            if should_exclude(root, candidate, excludes):
                pruned.append(name)
        for name in pruned:
            dirnames.remove(name)

        for name in filenames:
            path = base / name
            if should_exclude(root, path, excludes):
                continue
            files.append(path)
            if len(files) >= max_files:
                return files
    return files


def extract_headings(path: Path, limit: int = 18) -> list[str]:
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []
    headings: list[str] = []
    for line in lines:
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        headings.append(f"{'  ' * (level - 1)}- {title}")
        if len(headings) >= limit:
            break
    return headings


def file_meta(root: Path, path: Path) -> dict[str, object]:
    stat = path.stat()
    return {
        "path": norm_rel(root, path),
        "bytes": int(stat.st_size),
        "mtime": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
    }


def build_docs_index(root: Path, agents_root: Path, files: list[Path]) -> str:
    doc_files = [p for p in files if p.suffix.lower() in DOC_EXTS and "/docs/" in ("/" + norm_rel(root, p) + "/")]
    doc_files = sorted(doc_files, key=lambda p: norm_rel(root, p))[:300]

    lines: list[str] = []
    lines.append("# Docs Index")
    lines.append("")
    lines.append("This is a generated shallow index of `docs/` for fast routing.")
    lines.append("Read this file first before opening arbitrary docs.")
    lines.append("")
    for path in doc_files:
        rel = norm_rel(root, path)
        lines.append(f"## `{rel}`")
        headings = extract_headings(path)
        if headings:
            lines.append("")
            lines.extend(headings)
        lines.append("")
    if not doc_files:
        lines.append("- No `docs/` markdown files were discovered under this root.")
        lines.append("")
    lines.append(f"_Generated: {utc_timestamp()}_")
    lines.append(f"_Agents root: {agents_root}_")
    return "\n".join(lines).strip() + "\n"


def build_skills_index(root: Path, agents_root: Path) -> str:
    skills_root = agents_root / "skills"
    lines: list[str] = []
    lines.append("# Skills Index (Generated)")
    lines.append("")
    lines.append("This index lists available skills and their descriptions.")
    lines.append("Read this before loading many skills or scanning the full skills tree.")
    lines.append("")

    if not skills_root.exists():
        lines.append(f"- Missing skills directory: `{skills_root}`")
        lines.append("")
        lines.append(f"_Generated: {utc_timestamp()}_")
        return "\n".join(lines).strip() + "\n"

    skill_dirs = sorted([p for p in skills_root.iterdir() if p.is_dir()])
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        rel = norm_rel(root, skill_file)
        if not skill_file.exists():
            continue
        text = skill_file.read_text(encoding="utf-8", errors="ignore")
        first_heading = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), skill_dir.name)
        desc_line = ""
        for line in text.splitlines():
            if not line.strip():
                continue
            if line.startswith("#") or line.strip().startswith(">"):
                continue
            desc_line = line.strip()
            break
        desc_line = desc_line[:180] + ("..." if len(desc_line) > 180 else "")
        lines.append(f"- `{skill_dir.name}`")
        lines.append(f"  - File: `{rel}`")
        lines.append(f"  - Title: {first_heading}")
        if desc_line:
            lines.append(f"  - Summary: {desc_line}")
    lines.append("")
    lines.append(f"_Generated: {utc_timestamp()}_")
    return "\n".join(lines).strip() + "\n"


def build_code_index(root: Path, agents_root: Path, files: list[Path], max_files: int) -> str:
    candidates = [p for p in files if p.suffix.lower() in CODE_EXTS]
    candidates = sorted(candidates, key=lambda p: norm_rel(root, p))[:max_files]

    by_ext: dict[str, int] = {}
    top_dirs: dict[str, int] = {}
    for path in candidates:
        rel = norm_rel(root, path)
        by_ext[path.suffix.lower()] = by_ext.get(path.suffix.lower(), 0) + 1
        top = rel.split("/", 1)[0]
        top_dirs[top] = top_dirs.get(top, 0) + 1

    lines: list[str] = []
    lines.append("# Code Index")
    lines.append("")
    lines.append("This is a generated shallow index of code files for fast routing.")
    lines.append("Use it to pick the smallest set of files to open for the active task.")
    lines.append("")

    if by_ext:
        lines.append("## By Extension")
        for ext, count in sorted(by_ext.items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"- `{ext}`: {count} file(s)")
        lines.append("")

    if top_dirs:
        lines.append("## By Top-Level Directory")
        for name, count in sorted(top_dirs.items(), key=lambda kv: (-kv[1], kv[0]))[:30]:
            lines.append(f"- `{name}/`: {count} indexed file(s)")
        lines.append("")

    lines.append("## Indexed Files (Shallow)")
    for path in candidates:
        rel = norm_rel(root, path)
        meta = file_meta(root, path)
        lines.append(f"- `{rel}` ({meta['bytes']} bytes)")
    lines.append("")
    if not candidates:
        lines.append("- No code files were discovered under this root.")
        lines.append("")
    lines.append(f"_Generated: {utc_timestamp()}_")
    lines.append(f"_Agents root: {agents_root}_")
    return "\n".join(lines).strip() + "\n"


def build_architecture_graph(root: Path, agents_root: Path) -> str:
    # Heuristic, repo-agnostic architecture map: show `.agents` harness surfaces and top-level project dirs.
    top_dirs = [p for p in root.iterdir() if p.is_dir() and p.name not in {".git"}]
    top_names = sorted(p.name for p in top_dirs if p.name not in {"node_modules", "logs"})

    lines: list[str] = []
    lines.append("flowchart TD")
    lines.append('    subgraph Agents[".agents Harness"]')
    lines.append("        A1[workflows/] --> A2[scripts/]")
    lines.append("        A2 --> A3[validate_command_surface.py]")
    lines.append("        A2 --> A4[run_harness_preflight.py]")
    lines.append("        A2 --> A5[run_harness_postflight.py]")
    lines.append("        A1 --> A6[SLASH_COMMAND_REGISTRY.md]")
    lines.append("        A2 --> A7[index/ (generated)]")
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph Project["Project Root"]')
    for name in top_names[:18]:
        safe = re.sub(r"[^a-zA-Z0-9_]", "_", name)
        lines.append(f"        P_{safe}[{name}/]")
    lines.append("    end")
    lines.append("")
    lines.append("    A6 --> A3")
    lines.append("    A4 --> A3")
    lines.append("    A4 --> A7")
    if "docs" in top_names:
        lines.append("    A7 --> P_docs")
        lines.append("    P_docs --> A7")
    lines.append("")
    lines.append("%% Generated by build_context_index.py")
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build `.agents/index/` context index for deterministic routing.")
    parser.add_argument("--root", default=".", help="Project root containing `.agents/`.")
    parser.add_argument("--max-files", type=int, default=1200, help="Max files to scan for indexing.")
    parser.add_argument("--max-code-files", type=int, default=600, help="Max code files to list in code index.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents_root = resolve_agents_root(root)
    index_dir = agents_root / "index"
    index_dir.mkdir(parents=True, exist_ok=True)

    excludes = set(DEFAULT_EXCLUDES)
    # Never index `.agents/index` content itself.
    excludes.add(f"{norm_rel(root, agents_root)}/index")

    files = iter_files(root, excludes, max_files=args.max_files)

    docs_index = build_docs_index(root, agents_root, files)
    skills_index = build_skills_index(root, agents_root)
    code_index = build_code_index(root, agents_root, files, max_files=args.max_code_files)
    architecture = build_architecture_graph(root, agents_root)

    (index_dir / "docs_index.md").write_text(docs_index, encoding="utf-8")
    (index_dir / "skills_index.md").write_text(skills_index, encoding="utf-8")
    (index_dir / "code_index.md").write_text(code_index, encoding="utf-8")
    (index_dir / "architecture_graph.mmd").write_text(architecture, encoding="utf-8")

    manifest = {
        "generated_at": utc_timestamp(),
        "root": str(root),
        "agents_root": str(agents_root),
        "scanned_files": len(files),
        "max_files": int(args.max_files),
        "max_code_files": int(args.max_code_files),
        "excludes": sorted(excludes),
        "outputs": [
            "index/docs_index.md",
            "index/skills_index.md",
            "index/code_index.md",
            "index/architecture_graph.mmd",
            "index/index_manifest.json",
        ],
    }
    (index_dir / "index_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    print(index_dir)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise
    except Exception as exc:
        print(f"Failed to build context index: {exc}", file=sys.stderr)
        sys.exit(1)
