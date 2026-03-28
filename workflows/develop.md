---
description: Marcus Fleet Enterprise SDLC Phase 3 (Code Execution, TDD, & Continuous Delivery)
---

# ⚙️ EXECUTION FACTORY MATRIX (PHASE 3)

> **CORE ARCHITECTURE MANDATE:**  
> This operational protocol governs the Code Generation, Testing, and Deployment phase of the SDLC. The Engine will linearly execute instructions exclusively derived from the pre-approved schemas residing in the `/docs` directory. Blind-guessing software logic without reading the PRD/SDD is a violation of the Deterministic Protocol.

// turbo-all

---

## ⬛ SYSTEMIC MEMORY & STATE INHERITANCE (ANTI-AMNESIA PROTOCOLS)

<state_propagation_boundary>
**DOGMATIC STATE PROPAGATION:** The Physical Construction sequence is physically incapable of initiating unless `BRAND_GUIDELINES.md`, `SDD_ARCHITECTURE.md`, and `PRD_*.md` files have been dynamically read and ingested into the LLM context buffer. Failure to read pre-requisite artifacts yields an immediate `Exit Code 1`.
</state_propagation_boundary>

---

## 🔲 DAG TOPOLOGY: CHRONOLOGICAL EXECUTION NODES (PHASE 3)

### 🔵 NODE 5 & 6: ADVERSARIAL QA & TDD BACKEND SCAFFOLDING
*🔗 Input Vector:* `/docs/SDD_ARCHITECTURE.md`, `/docs/PRD_PART2_EDGE_CASES.md`
*🧠 Injected Tensors:* `eve-qa-approver`, `alan-tech-lead`, `ada-qa-agent`
*📦 Emitted Artifacts:* Database Migrations, Route Handlers, Integration Suites source code.
**[Execution Protocol]:** Initialize Backend Infrastructure via Test-Driven Development (TDD). Generate isolated Unit-Test stubs detailing Boundary-Value handling and Fault Injection (Negative Path APIs). Validate API schema schemas against Null-value crashes before writing business logic.

### 🟣 NODE 7: ZERO-DOWNTIME LIVE SIMULATION (FSM FEEDBACK LOOP)
*🔗 Input Vector:* `/docs/BRAND_GUIDELINES.md`, `/docs/PRD_PART3_SCREEN_MAP.md`
*🧠 Injected Tensors:* `benny-frontend-engineer`, `qa-simulator`, `playwright-test`
**[Execution Protocol]:** Spawning the Daemon Simulator: Execute the bash command `npm run dev` or equivalent to mount a localized Runtime Protocol.
- **Bi-Directional Mutation Feedback:**
  - `benny-frontend-engineer` algorithmically renders UI Components enforcing predefined strict Spatial parameters based on `BRAND_GUIDELINES.md`.
  - `qa-simulator` evaluates the rendered port utilizing `playwright` telemetry or `cURL`. Evaluates UI Hydration errors, layout shifts, or Exceptions.
  - **The V29.1 Circuit Breaker:** If a specific rendering loop generates $\ge 3$ sequential compile errors, gracefully terminate the Node, flag a Terminal Red-Alert, and request Human Operator intervention.

### 🟤 NODE 8: CONTINUOUS DEPLOYMENT CLOSURE (CI/CD PIPELINE)
*🔗 Input Vector:* Validated Git Branch
*🧠 Injected Tensors:* `devops-system-architect`, `ops`
**[Execution Protocol]:** Define End-to-End Test suites validating User Lifecycle. Draft Infrastructure as Code (IaC) for AWS/Vercel/Cloudflare propagation. Resolve port-conflicts cleanly by terminating NODE 7 background tasks securely.

### ⚫ NODE 9: MICRO-BRAIN HISTORICAL ARCHIVING
*🔗 Input Vector:* Runtime Log / Git Diff Context
*🧠 Injected Tensors:* Internal State Machine (Sophia Butler Node)
**[Execution Protocol]:** Audit and compress the entire Session DAG Execution Path. Write architectural shifts and codebase metrics natively to `.agents/agents.md` utilizing Append-Only commands (`>>`). Next, execute `python3 .agents/adapters/trustgraph_write.py --run_id "ExecuteRun" --status "success" --target "Project" --skills "all"` to commit the entire Session Object to the GraphRAG Database. Signal total completion to Operator.
