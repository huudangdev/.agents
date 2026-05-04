#!/usr/bin/env python3
"""Validate /planning deep-research ledgers and legacy output files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_docs_substance import validate_docs


REQUIRED_OUTPUTS = [
    "docs/prd.md",
    "docs/tasks.md",
    "docs/knowledge.md",
    "docs/decisions.md",
    "docs/memory.md",
    "docs/planning/flows.md",
    "docs/planning/screens.md",
    "docs/planning/diagrams.md",
]

RESEARCH_FILES = [
    "docs/research/sources.jsonl",
    "docs/research/evidence.jsonl",
    "docs/research/claims.jsonl",
    "docs/research/contradictions.md",
    "docs/research/research_manifest.json",
]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for lineno, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{lineno}: invalid JSONL: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{lineno}: each JSONL row must be an object")
        rows.append(value)
    return rows


def validate(root: Path, strict_outputs: bool) -> list[str]:
    errors: list[str] = []

    for rel_path in RESEARCH_FILES:
        path = root / rel_path
        if not path.exists():
            errors.append(f"Missing research artifact: {rel_path}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty research artifact: {rel_path}")

    if strict_outputs:
        for rel_path in REQUIRED_OUTPUTS:
            path = root / rel_path
            if not path.exists():
                errors.append(f"Missing required planning output: {rel_path}")
            elif not path.read_text(encoding="utf-8").strip():
                errors.append(f"Empty required planning output: {rel_path}")
        for issue in validate_docs(root, strict_planning=True):
            errors.append(f"{issue.relpath}: {issue.message}")

    sources_path = root / "docs/research/sources.jsonl"
    evidence_path = root / "docs/research/evidence.jsonl"
    claims_path = root / "docs/research/claims.jsonl"
    manifest_path = root / "docs/research/research_manifest.json"

    if not all(path.exists() for path in [sources_path, evidence_path, claims_path, manifest_path]):
        return errors

    try:
        sources = read_jsonl(sources_path)
        evidence = read_jsonl(evidence_path)
        claims = read_jsonl(claims_path)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (ValueError, json.JSONDecodeError) as exc:
        errors.append(str(exc))
        return errors

    source_ids = {str(row.get("source_id")) for row in sources if row.get("source_id")}
    evidence_ids = {str(row.get("evidence_id")) for row in evidence if row.get("evidence_id")}
    claim_ids = {str(row.get("claim_id")) for row in claims if row.get("claim_id")}

    if len(sources) < int(manifest.get("quality_gates", {}).get("minimum_sources", 10)):
        errors.append("Not enough sources for configured quality gate")

    primary_count = sum(1 for row in sources if row.get("trust_tier") == "primary")
    if primary_count < int(manifest.get("quality_gates", {}).get("minimum_primary_sources", 3)):
        errors.append("Not enough primary sources for configured quality gate")

    if len(evidence) < int(manifest.get("quality_gates", {}).get("minimum_evidence_items", 15)):
        errors.append("Not enough evidence items for configured quality gate")

    for row in evidence:
        source_id = str(row.get("source_id", ""))
        supports = str(row.get("supports", ""))
        if source_id not in source_ids:
            errors.append(f"Evidence {row.get('evidence_id')} references unknown source {source_id}")
        if supports and supports not in claim_ids:
            errors.append(f"Evidence {row.get('evidence_id')} supports unknown claim {supports}")

    for row in claims:
        claim_id = str(row.get("claim_id", ""))
        status = row.get("status")
        ids = row.get("evidence_ids")
        if status == "supported" and (not isinstance(ids, list) or not ids):
            errors.append(f"Supported claim {claim_id} has no evidence_ids")
            continue
        if isinstance(ids, list):
            for evidence_id in ids:
                if str(evidence_id) not in evidence_ids:
                    errors.append(f"Claim {claim_id} references unknown evidence {evidence_id}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate /planning research artifacts.")
    parser.add_argument("--root", default=".", help="Workspace root containing docs/")
    parser.add_argument(
        "--strict-outputs",
        action="store_true",
        help="Also require the legacy /planning output files to exist.",
    )
    args = parser.parse_args()

    errors = validate(Path(args.root).resolve(), args.strict_outputs)
    if errors:
        print("PLANNING RESEARCH VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("PLANNING RESEARCH VALIDATION PASSED")


if __name__ == "__main__":
    main()
