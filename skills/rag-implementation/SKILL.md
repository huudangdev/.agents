---
name: rag-implementation
description: Implement production RAG code with observability, fallback behavior, and docs sync
---

# RAG Production Code Governor

Use this skill when writing production-ready RAG code.

## Required Reads

- [rag-implementation-contract.md](references/rag-implementation-contract.md)
- The approved RAG architecture and service boundaries when they exist.

## Operating Rules

- Implement the documented topology, not a new one.
- Preserve fallback behavior and traceable citations.
- Treat auth, timeout, and parse failures as first-class blockers.

## Output Expectations

- State the implementation boundary and the verification commands.
- Identify observability hooks and fallback behavior.
- Describe how docs sync targets are handled.
