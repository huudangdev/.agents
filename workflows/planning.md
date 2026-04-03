---
description: Marcus Fleet Enterprise SDLC Phase 1 (Deep Research, Architecture, & 6-File Setup)
---

# 📝 MACRO ARCHITECT PLANNING MATRIX (PHASE 1 - DEEP RESEARCH)

> **CORE ARCHITECTURE MANDATE:**  
> This operational protocol governs the strictly bounded Planning & Architecture Phase. Your sole objective is to perform exhaustive heuristic discovery and emit the **"6 Core Files That Run Your AI Build"**. To prevent LLM superficiality and hallucination, you MUST employ a Deep Research MapReduce Algorithm. Generating source code during this phase is FORBIDDEN.

// turbo-all

---

## ⬛ SYSTEMIC MEMORY & STATE INHERITANCE (ANTI-AMNESIA PROTOCOLS)

<identity_injection_vector>
**RAG-DRIVEN IDENTITY INJECTION:** To circumvent LLM context-window degradation, start by invoking `view_file` against `SKILLS_INDEX.md` and load the specific Subject-Matter Expert identities (`david-systems-architect`, `sophia-product-manager`, `cyrus-research-critic`, `elite6-research`).
</identity_injection_vector>

---

## 🔲 DAG TOPOLOGY: CHRONOLOGICAL EXECUTION NODES (PHASE 1)

### ⚪ NODE 0: LOCALHOST ISOLATION & KNOWLEDGE BOOTSTRAP
*🔗 Input Vector:* `.agents/agents.md`, User Requirements.
**[Execution Protocol]:** Execute `python3 .agents/adapters/trustgraph_query.py --task "Planning Phase Boot"` to pull the TrustGraph Historical Matrix. Perform a Micro-Brain Audit via `.agents/agents.md`.

### 🔴 NODE 1: MAP-REDUCE RESEARCH BIFURCATION (DEEP RESEARCH)
*🧠 Injected Tensors:* `cyrus-research-critic`, `elite6-research`
**[Algorithm]:** 
1. **Keyword Decomposition:** Break down the User's core project idea into 5-10 specialized domains (e.g., Payment ERD, Security GDPR, System Architecture).
2. **Web Scraping:** Independently execute exhaustive web searches (`search_web` or URL reading) for each domain to pull real-world constraints, whitepapers, and best practices.
3. **Data Staging:** Write the raw findings to temporary workspace files (`/docs/tmp/research_1.md`, etc.). *Do not synthesize yet.*

### 🟢 NODE 2: MEGA SYNTHESIS (THE 6-FILE GENERATION)
*🧠 Injected Tensors:* `sophia-product-manager`, `david-systems-architect`
**[Algorithm]:** Read all staged temporary files and synthesize the exhaustive truth. Output the following files *directly into the `/docs/` directory*. **Constraint: Technical depth must be absolute (Targeting >= 50KB detail per file over time).**

1. **`/docs/prd.md`**: Your product's brain. What you're building, target audience, core logic.
2. **`/docs/tasks.md`**: Your product's to-do list. Component milestones with checkboxes.
3. **`/docs/knowledge.md`**: Your product's soul (like `CLAUDE.md`). Tech stack, design preferences, and the strict "never do" list.
4. **`/docs/decisions.md`**: Your learning log. Architectural tradeoffs (For Humans).
5. **`/docs/memory.md`**: Your product's long-term memory. Known bugs, structural patterns.
6. **`/docs/planning/flows.md`**: User flows, state machines.
7. **`/docs/planning/screens.md`**: Screen maps and navigation topology.
8. **`/docs/planning/diagrams.md`**: C4 Model system diagrams (You MUST generate `.mmd` and render to `.png` via Mermaid CLI if applicable).

*Cleanup:* Delete the `/docs/tmp/` directory after staging is successfully synthesized.

---

## 🛑 POINT OF NO RETURN: THE HUMAN OVERSIGHT HALT

> **[HALT COMMAND INITIATED]**
> You have reached the termination of the Phase 1 DAG Sequence. You are strictly prohibited from proceeding to source code generation.
> **ACTION REQUIRED:** Present the 6 Core Root Files to the Human Operator. Instruct them to review the depth of `prd.md`, `planning/`, and `tasks.md`. Instruct them to invoke `/design` ONLY WHEN they are 100% satisfied with the architectural blueprint.
