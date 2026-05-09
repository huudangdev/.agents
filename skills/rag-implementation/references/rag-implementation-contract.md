# RAG Implementation Contract

Use this skill when writing production-ready RAG code.

## Required Inputs

- The approved RAG architecture
- Observability, fallback, and citation requirements
- The service boundaries and environment constraints

## Decision Rules

- Implement the documented topology, not a new one.
- Preserve fallback behavior and traceable citations.
- Treat auth, timeout, and parse failures as first-class blockers.

## Output Contract

- State the implementation boundary and the verification commands.
- Identify observability hooks and fallback behavior.
- Describe how docs sync targets are handled.
