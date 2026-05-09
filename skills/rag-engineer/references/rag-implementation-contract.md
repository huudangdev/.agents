# RAG Implementation Contract

Use this skill to implement an agreed retrieval design.

## Required Inputs

- The approved RAG architecture
- Embedding, chunking, and retrieval expectations
- Citation and grounding requirements
- Readiness gates for behavior-changing code

## Decision Rules

- Implement the documented retrieval flow, not a new one.
- Preserve citation fidelity and line/file traceability.
- Treat parse failures, retrieval drift, and context overflow as blockers.

## Output Contract

- Produce code or scripts that follow the approved topology.
- Keep retrieved context bounded to the active context window.
- Show how the implementation is verified locally.
