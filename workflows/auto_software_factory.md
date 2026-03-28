---
description: Marcus Fleet Enterprise SDLC Continuous Delivery Pipeline (9-Node Directed Acyclic Graph)
---

# 🚀 CONTINUOUS SDLC DELIVERY GRAPH (V29.1 ENTERPRISE EDITION)

> **CORE ARCHITECTURE MANDATE (PURPOSE):**  
> This operational protocol governs the core Software Development Life Cycle (SDLC) via a strictly enforced **Directed Acyclic Graph (DAG)**. It maps the end-to-end multi-agent orchestration from Initial Requirements Gathering down to Physical Runtime Validation and Continuous Deployment. To guarantee Zero-Downtime Application generation and prevent systemic "AI Hallucinations," the Antigravity Engine is mathematically bounded by finite state controls, adversarial QA checkpoints, and absolute Dependency Graph isolation.

// turbo-all

> 🛑 **HARD BARRIER RULE (ANTI-SKIP):** You must operate sequentially. You are STRICTLY FORBIDDEN from generating or editing any source code (Nodes 5-7) until you have physically created the documentation artifacts for Nodes 1-4 (PRD, Architecture, Branding) in a `/docs` folder. You MUST stop and ask for the User's explicit approval after completing Node 4.

---

## ⬛ SYSTEMIC MEMORY & STATE INHERITANCE (ANTI-AMNESIA PROTOCOLS)

<identity_injection_vector>
**RAG-DRIVEN IDENTITY INJECTION:** To circumvent LLM context-window degradation (Amnesia), you are algorithmically prohibited from loading >10 Skill matrices concurrently. At the initiation of each Operational Node, the Engine **MUST** explicitly invoke the `view_file` operation against `SKILLS_INDEX.md`. Map the targeted operational phase (e.g., Database Modeling) to the specific Subject-Matter Expert identity (e.g., `david-systems-architect`) and perform an isolated extraction of that single `SKILL.md` file.
</identity_injection_vector>

<state_propagation_boundary>
**DOGMATIC STATE PROPAGATION:** Every State Transition from `NODE(N)` to `NODE(N+1)` demands an unconditional `Read` operation evaluating the absolute Artifacts emitted by the preceding stage. Example: The Frontend rendering node `NODE(7)` is physically incapable of initiating unless `BRAND_GUIDELINES.md` and `PRD_SCREEN_MAP.md` have been fully ingested into the context buffer. Failure to read pre-requisite artifacts yields an immediate `Exit Code 1`.
</state_propagation_boundary>

---

## 🔲 DAG TOPOLOGY: CHRONOLOGICAL EXECUTION NODES

### ⚪ NODE 0: LOCALHOST ISOLATION & MCP HANDSHAKE
*🔗 Input Domain Matrix:* `.agents/mcp/mcp.json`, `.agents/agents.md`
**[Execution Protocol]:** Initialize Model Context Protocol (MCP) telemetry. Establish asynchronous handshakes with peripheral nodes such as `playwright`. Execute `python3 .agents/adapters/trustgraph_query.py --task "Software Factory Boot"` to pull the TrustGraph Historical Matrix. Perform a Micro-Brain Audit via `.agents/agents.md` to reconstruct the exact development epoch and state architecture prior to dynamic memory allocation.

### 🔴 NODE 1 & 2: HEURISTIC DISCOVERY & REQUIREMENTS ENGINEERING
*🔗 Input Vector:* Exhaustive Web Search APIs.
*🧠 Injected Tensors:* `elite6-research`, `sophia-product-manager`, `antigravity-brainstorming`, `compound-brainstorming`
*📦 Emitted Artifacts:* Highly segmented, physical PRD sub-modules.
**[Execution Protocol]:** 
Trigger `elite6-research` to execute autonomous, concurrent `google_web_search` and `web_fetch` cycles exploring domain complexities, competitor UI paradigms, and API documentation. 
Delegate synthesis to `sophia-product-manager`. Sophia is explicitly forbidden from generating monolithic PRD documents. Output MUST be mechanically segmented into independent physical artifacts:
1. `PRD_PART1_FEATURES.md`: Granular Business Logic.
2. `PRD_PART2_EDGE_CASES.md`: Defensive programming constraints.
3. `PRD_PART3_SCREEN_MAP.md`: A 100% exhaustive Component/Routing Tree. Wildcards (e.g., `...`) are classified as lazy syntax and are globally blacklisted.

### 🟡 NODE 3: DIGITAL AESTHETIC BASELINE & DESIGN TOKENS
*🔗 Input Vector:* `PRD_PART3_SCREEN_MAP.md`
*🧠 Injected Tensors:* `maya-ui-ux-designer`, `aris-designer`, `design-system-rules`
*📦 Emitted Artifacts:* `BRAND_GUIDELINES.md`, Figma-equivalent Variable Mappings.
**[Execution Protocol]:** Synthesize Typography Scalar Rules (Base 16px, Golden Ratio H1-H6). Formulate contrast-accessible Color Palettes (Primary, Accent, Background, Surface, Semantic errors). Define spatial rhythm constraints (4px/8px absolute grid). Emit the structural `BRAND_GUIDELINES.md` required by all downstream rendering pipelines.

### 🟢 NODE 4: ENTERPRISE ARCHITECTURE EMITTING (THE UML MANDATE)
*🔗 Input Vector:* `PRD_PART2_EDGE_CASES.md`, `PRD_PART3_SCREEN_MAP.md`
*🧠 Injected Tensors:* `david-systems-architect`, `chartis-data-visualizer`, `architecture-decision-records`, `c4-architecture`
*📦 Emitted Artifacts:* `SDD_*.md`, `.mmd` Scripts, `.png` Diagrams, `/docs/PDF_EXPORTS/*.pdf`
**[Execution Protocol]:** Architect internal Backend structures: Databases (ERD mapping), API specification parameters (REST/trpc), and physical Project scaffoldings (Next.js/Flutter FSD models).
**Critical Rendering Bypass:** You MUST execute native CLI operations to transform pseudo-code architecture into physical graphics. Run `npx -y @mermaid-js/mermaid-cli -i <file.mmd> -o <diagram.png>`. The Absolute URI `![chart](/docs/diagram.png)` is then embedded into the physical markdown to ensure Human interpretability prior to PDF compiling.

### 🔵 NODE 5 & 6: ADVERSARIAL QA & TDD BACKEND SCAFFOLDING
*🔗 Input Vector:* `FINAL_SPECS.md`
*🧠 Injected Tensors:* `eve-qa-approver`, `alan-tech-lead`, `ada-qa-agent`
*📦 Emitted Artifacts:* Database Migrations (e.g., Prisma), Route Handlers, Integration Suites.
**[Execution Protocol]:** Initialize Backend Infrastructure via Test-Driven Development (TDD). Generate isolated Unit-Test stubs detailing Boundary-Value handling and Fault Injection (Negative Path APIs). Validate API schema schemas against Null-value crashes.

### 🟣 NODE 7: ZERO-DOWNTIME LIVE SIMULATION (FSM FEEDBACK LOOP)
*🔗 Input Vector:* `BRAND_GUIDELINES.md`, `PRD_PART3_SCREEN_MAP.md`
*🧠 Injected Tensors:* `benny-frontend-engineer`, `qa-simulator`, `playwright-test`
**[Execution Protocol]:** Spawning the Daemon Simulator: Execute the bash command `npm run dev` or equivalent to mount a localized Runtime Protocol.
- **Bi-Directional Mutation Feedback (Pha 1 & Pha 2):**
  - `benny-frontend-engineer` algorithmically renders UI Components enforcing Glassmorphism or predefined strict Spatial parameters based on `BRAND_GUIDELINES.md`. No UI code may be pushed unless mathematically perfect.
  - `qa-simulator` concurrently evaluates the rendered port (e.g., `localhost:3000`) utilizing `playwright` or `cURL` telemetry. Evaluates Next.js Hydration errors, z-index collisions, or uncaught Exceptions.
  - **The V29.1 Circuit Breaker:** If a specific rendering loop generates $\ge 3$ sequential compile/hydration errors, Antigravity gracefully terminates the Node, flags a critical Terminal Red-Alert, and requests Human Operator intervention. "Blind Guessing" codebase injection is eradicated.
  - Strict Typescript audit via `npx tsc --noEmit` before state validation.

### 🟤 NODE 8: CONTINUOUS DEPLOYMENT CLOSURE (CI/CD PIPELINE)
*🔗 Input Vector:* Validated Git Branch
*🧠 Injected Tensors:* `devops-system-architect`, `ops`
**[Execution Protocol]:** Define End-to-End Test suites validating User Lifecycle (e.g., OAuth -> Checkout). Draft Infrastructure as Code (IaC) for AWS/Vercel/Cloudflare propagation. Resolve port-conflicts cleanly by terminating NODE 7 background tasks securely.

### ⚫ NODE 9: MICRO-BRAIN HISTORICAL ARCHIVING
*🔗 Input Vector:* Runtime Log / Git Diff Context
*🧠 Injected Tensors:* Internal State Machine (Sophia Butler Node)
**[Execution Protocol]:** Audit and compress the entire Session DAG Execution Path. Write architectural shifts, complex blockers evaded, and component rename metrics natively to `.agents/agents.md` utilizing Append-Only commands (`>>`). Mutating historical records via overwrite (`>`) is deemed catastrophic. Next, execute `python3 .agents/adapters/trustgraph_write.py --run_id "FactoryRun" --status "success" --target "Project" --skills "all"` to commit the entire Session Object to the GraphRAG Long-Term Database. Signal completion to Operator. DAG Chain Terminated.
