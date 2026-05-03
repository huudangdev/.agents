---
name: langchain-architecture
description: Langchain Architecture
---

# Directive: LangChain Architecture

> Use this skill to shape multi-step LLM workflows with explicit state, routing, and failure boundaries.

## 🎯 MISSION (CORE OBJECTIVES)
1. **DAG Graph State Enforcement:** Abstract complex ReAct or Plan-and-Execute chains into LangGraph Node/Edge logic matrices. Avoid infinitely looping LLM calls.
2. **Context Compression (Memory):** Design stateful Conversation Buffer pipelines utilizing Vector Stores to summarize sliding windows of memory without exhausting token limits.
3. **Topology Discipline:** Prefer the simplest graph that satisfies the requirement. Avoid speculative multi-agent complexity.

## ⚙️ EXECUTION PIPELINE (THE AI ARCHITECTURE CYCLE)

### Phase 1: Contextual Flow Ingestion
- Read the active feature docs, current architecture notes, and model constraints first.

### Phase 2: Architecture Review
- Check node boundaries, state shape, recursion limits, and observability.
- Recommend extra libraries only as operator-reviewed additions.

### Phase 3: Topology Standardization
Enforce these structural components:
- **Routing Modules:** The root node must definitively route queries via Semantic Similarity before burning heavy reasoning cycles.
- **The Circuit Breaker Rule:** When designing the execution chain loop (ReAct loops), you MUST hardcode a `recursion_limit` (e.g., `< 5`) to mathematically guarantee the AI engine does not spin infinitely and burn cash/tokens.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Physical Diagram Execution
- Output a physically renderable `.mmd` (Mermaid) DAG flowchart representing the LLM's multi-step decision matrix. Prompt chains without flowcharts are strictly prohibited.
- **[REPORT]**: Emitted upon completing the Langchain blueprint.
