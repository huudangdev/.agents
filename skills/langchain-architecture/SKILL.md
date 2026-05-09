---
name: langchain-architecture
description: Design LangChain routing, state, and recursion boundaries for LLM workflows
---

# LangChain Architecture

Use this skill when multi-step LLM routing or memory boundaries need design.

## Required Reads

- [langchain-architecture-contract.md](references/langchain-architecture-contract.md)
- The active workflow shape and state needs when they exist.

## Operating Rules

- Prefer the simplest graph that works.
- Hardcode recursion limits for looping chains.
- Make routing and state boundaries explicit.

## Output Expectations

- State the DAG or node-edge topology.
- Identify state shape, recursion limits, and failure boundaries.
- Provide a Mermaid diagram when it clarifies the topology.
