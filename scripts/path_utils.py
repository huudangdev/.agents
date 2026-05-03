from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def resolve_agents_root(root: Path) -> Path:
    nested = root / ".agents"
    return nested if nested.is_dir() else root


def resolve_from_root(root: Path, relative_path: str) -> Path:
    if relative_path.startswith(".agents/"):
        return resolve_agents_root(root) / relative_path.removeprefix(".agents/")
    return root / relative_path


def resolve_script_path(root: Path, script_name: str) -> Path:
    return resolve_agents_root(root) / "scripts" / script_name


def resolve_harness_logs_dir(root: Path) -> Path:
    return resolve_agents_root(root) / "logs" / "harness"


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def append_jsonl(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")
