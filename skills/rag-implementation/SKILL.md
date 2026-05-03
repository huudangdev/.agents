---
name: rag-implementation
description: Specialized guidelines for writing production-ready RAG code (retrievers, generators, routing).
---

# Directive: RAG Production Code Governor

> Implement RAG code with explicit abstractions, observability, and fallback behavior. Production readiness means the retrieval path, failure modes, and evidence model are all documented and testable.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Production Hardening:** Refactor raw RAG scripts into abstracted Classes, Controllers, and Service layers utilizing the principles of Dependency Injection.
2. **Telemetry Enforcement:** Integrate LangSmith (or equivalent) systemic tracking to measure token burn, latency tracking, and generation fidelity.
3. **Execution Governance:** Use the approved architecture, local toolchain, and existing libraries first. Recommend extra components only when the current plan cannot satisfy the documented requirements.

## ⚙️ EXECUTION PIPELINE (THE PRODUCTION CYCLE)

### Phase 1: Blueprint Ingestion
- Read the agreed architecture, active feature docs, and existing service boundaries first.
- If implementation diverges from the documented topology, stop and surface the mismatch.

### Phase 2: Capability Escalation
If caching, tracing, or retrieval tooling is missing:
1. Inspect repo libraries, config, and existing deployment constraints first.
2. Propose any addition as an operator-reviewed recommendation.
3. Document the evidence or operational capability it unlocks.

### Phase 3: Secure Secrets Mapping
- **Zero-Downtime Rule & Circuit Breaker:** Guarantee that API Keys (`OPENAI_API_KEY`, Database URIs) are ONLY read via `.env` runtime extraction (e.g., `os.getenv()`). If local terminal deployments (`npx ts-node` or `python main.py`) crash 3 times due to uninitialized Tokens, STOP executing blindly, and present a 🚩 requesting `.env` file updates from the Human-In-The-Loop.
- Every implementation handoff must include executed verification commands, fallback behavior, observability hooks, and docs sync targets.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Graceful Degradation
- If the Vector search times out or the Embedding API limits are hit, your production architecture MUST catch the `503/429` error logically and return a graceful fallback string to the Frontend UI instead of crashing the physical server.
- Require execution-readiness validation before behavior-changing RAG implementation begins.
- **[REPORT]**: Emitted upon successfully deploying the production RAG abstractions.
