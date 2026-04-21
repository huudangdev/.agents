#!/usr/bin/env python3
"""Shared TrustGraph runtime configuration for local adapters."""

import base64
import os
from pathlib import Path


def _load_local_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / "trustgraph.env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_local_env()

NEO4J_HTTP_ENDPOINT = os.getenv(
    "TRUSTGRAPH_NEO4J_HTTP_ENDPOINT",
    os.getenv("NEO4J_HTTP_ENDPOINT", "http://localhost:7474/db/neo4j/tx/commit"),
)
NEO4J_BOLT_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "trustgraph_secret")

CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8800"))
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "codebase")


def neo4j_auth_header() -> str:
    token = f"{NEO4J_USER}:{NEO4J_PASSWORD}".encode("utf-8")
    encoded = base64.b64encode(token).decode("ascii")
    return f"Basic {encoded}"
