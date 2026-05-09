# LangChain Architecture Contract

Use this skill when multi-step LLM routing or memory boundaries need design.

## Required Inputs

- The workflow shape and state needs
- Recursion, observability, and routing constraints
- The smallest graph that solves the problem

## Decision Rules

- Prefer the simplest graph that works.
- Hardcode recursion limits for looping chains.
- Make routing and state boundaries explicit.

## Output Contract

- State the DAG or node-edge topology.
- Identify state shape, recursion limits, and failure boundaries.
- Provide a Mermaid diagram when it clarifies the topology.
