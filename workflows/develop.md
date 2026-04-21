---
description: Marcus Fleet Enterprise SDLC Phase 3 (Code Execution, TDD, & Continuous Delivery)
---

# ⚙️ EXECUTION FACTORY MATRIX (PHASE 3)

> **CORE ARCHITECTURE MANDATE:**  
> This operational protocol governs the Code Generation, Testing, Documentation, and Deployment phase of the SDLC. The Engine will linearly execute instructions exclusively derived from the pre-approved schemas residing in the `/docs` directory and any accepted `.agents/specs/<feature-id>/` workspace. Blind-guessing software logic without reading the PRD/SDD is a violation of the Deterministic Protocol.

// turbo-all

---

## ⬛ SYSTEMIC MEMORY & STATE INHERITANCE (ANTI-AMNESIA PROTOCOLS)

<state_propagation_boundary>
**DOGMATIC STATE PROPAGATION:** The Physical Construction sequence is physically incapable of initiating unless `/docs/BRAND_GUIDELINES.md`, `/docs/planning/diagrams.md`, `/docs/knowledge.md`, `/docs/prd.md`, `/docs/tasks.md`, `/docs/decisions.md`, and `/docs/memory.md` files have been dynamically read and ingested into the LLM context buffer. If `/docs/research/` or a relevant `.agents/specs/<feature-id>/` workspace exists, those artifacts must be read as supplemental source-of-truth context before implementation. Failure to read pre-requisite artifacts yields an immediate `Exit Code 1`.
</state_propagation_boundary>

---

## 🧾 CODE PHASE KNOWLEDGE CONTRACT (MANDATORY)

`/develop` MUST NOT only emit source code. Every code-phase run that implements
or materially changes behavior must maintain a dedicated development knowledge
ledger under:

```text
/docs/development/
├── development_manifest.json
├── index.md
├── epics/
├── modules/
├── features/
├── pages/
├── tasks/
└── sync/
```

Minimum artifact rules:

1. **Epic notes** (`/docs/development/epics/*.md`) capture delivery outcomes,
   acceptance boundaries, linked features, and evidence.
2. **Module notes** (`/docs/development/modules/*.md`) capture code ownership,
   public contracts, dependencies, failure modes, and verification.
3. **Feature notes** (`/docs/development/features/*.md`) capture user behavior,
   requirement traceability, code scope, rollout, and risk.
4. **Page notes** (`/docs/development/pages/*.md`) capture route/screen state,
   interactions, accessibility, and visual verification. If the task is backend
   only, keep `minimum_count: 0` for pages in the manifest and record why in
   `index.md`.
5. **Task notes** (`/docs/development/tasks/*.md`) capture the execution log,
   write scope, commands, results, blockers, and handoff.

Initialize the ledger before code edits:

```bash
python3 .agents/scripts/create_development_docs.py --name "<feature-or-epic-name>" --feature-id "<optional-feature-id>"
```

Validate the ledger before reporting completion:

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

The code phase docs are not a replacement for `/planning` outputs. They are a
fine-grained implementation memory layer that keeps each epic, module, task,
feature, and page inspectable after code is generated.

---

## 🔁 CONTINUOUS DOCUMENTATION SYNC LOOP (MANDATORY)

During POC execution, `/develop` is a repeated loop: code, test, inspect,
adjust, and continue. Documentation must move with that loop.

After every material code slice, the active agent MUST run a documentation sync
cycle before proceeding to the next slice:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "<code-slice-name>" --changed-files "<comma-separated-files>"
```

Then the agent must update only the affected documents:

1. **Append missing facts** to legacy planning docs when new behavior, scope,
   acceptance criteria, risks, flows, screens, diagrams, or decisions emerge.
2. **Patch changed facts** where implementation behavior supersedes a previous
   statement.
3. **Preserve historical decisions** by adding superseding notes instead of
   deleting prior reasoning.
4. **Update development ledger notes** for affected epic/module/feature/page/task.
5. **Mark unchanged docs intentionally** in the sync note with a reason.

The agent MUST NOT replace whole documents just to keep them fresh. Full-file
replacement is allowed only when the operator explicitly asks for a rewrite or
the file is a generated artifact with no useful history.

Before the agent reports completion or continues to the next major code slice,
run:

```bash
python3 .agents/scripts/validate_doc_sync.py --strict
```

If validation fails, code work pauses until the missing documentation trace is
added.

---

## 🔲 DAG TOPOLOGY: CHRONOLOGICAL EXECUTION NODES (PHASE 3)

### 🟡 NODE 4: EXECUTION KNOWLEDGE LEDGER BOOTSTRAP
*🔗 Input Vector:* `/docs/tasks.md`, `.agents/specs/<feature-id>/tasks.md`, `/docs/planning/diagrams.md`
*🧠 Injected Tensors:* `marcus-ai-orchestrator`, `knowledge-work-architecture`, `sophia-product-manager`
*📦 Emitted Artifacts:* `/docs/development/development_manifest.json`, `/docs/development/index.md`, bucketed Markdown notes.
**[Execution Protocol]:** Decompose approved work into durable implementation documentation before code mutation. Each agent receiving a write scope must own at least one task note and, when applicable, one module/feature/page note. Notes must include YAML frontmatter, `owner_skill`, `source_trace`, and `verification`.

### 🔵 NODE 5 & 6: ADVERSARIAL QA & TDD BACKEND SCAFFOLDING
*🔗 Input Vector:* `/docs/planning/diagrams.md`, `/docs/knowledge.md`, `/docs/prd.md`, `/docs/development/modules/*.md`, `/docs/development/features/*.md`
*🧠 Injected Tensors:* `eve-qa-approver`, `alan-tech-lead`, `ada-qa-agent`
*📦 Emitted Artifacts:* Database migrations, route handlers, integration suites, updated module/feature/task notes.
**[Execution Protocol]:** Initialize Backend Infrastructure via Test-Driven Development (TDD). Generate isolated Unit-Test stubs detailing Boundary-Value handling and Fault Injection (Negative Path APIs). Validate API schemas against Null-value crashes before writing business logic. Update the relevant module, feature, and task notes with code paths, public contracts, and command evidence.

### 🔁 NODE 6.5: DOC SYNC CHECKPOINT
*🔗 Input Vector:* Git diff, changed source files, `/docs`, `/docs/development/`
*🧠 Injected Tensors:* `knowledge-work-architecture`, `sophia-product-manager`, `ada-qa-agent`
*📦 Emitted Artifacts:* `/docs/development/sync/*.md`, targeted updates to affected docs.
**[Execution Protocol]:** After each code slice, create a sync note, map changed source files to affected legacy planning docs and development ledger notes, apply targeted append/patch updates, then run `validate_doc_sync.py --strict`. This node is a continuation gate: the next code slice is blocked when source files changed but documentation trace is missing.

### 🟣 NODE 7: ZERO-DOWNTIME LIVE SIMULATION (FSM FEEDBACK LOOP)
*🔗 Input Vector:* `/docs/BRAND_GUIDELINES.md`, `/docs/planning/screens.md`, `/docs/development/pages/*.md`
*🧠 Injected Tensors:* `benny-frontend-engineer`, `qa-simulator`, `playwright-test`
**[Execution Protocol]:** Spawning the Daemon Simulator: Execute the bash command `npm run dev` or equivalent to mount a localized Runtime Protocol.
- **Bi-Directional Mutation Feedback:**
  - `benny-frontend-engineer` algorithmically renders UI Components enforcing predefined strict Spatial parameters based on `BRAND_GUIDELINES.md`.
  - `qa-simulator` evaluates the rendered port utilizing `playwright` telemetry or `cURL`. Evaluates UI Hydration errors, layout shifts, or Exceptions.
  - Page notes must be updated with route, states, interactions, accessibility checks, screenshots/manual evidence, and responsive verification.
  - **The V30 Circuit Breaker:** If a specific rendering loop generates $\ge 3$ sequential compile errors, gracefully terminate the Node, flag a Terminal Red-Alert, and request Human Operator intervention.

### 🟤 NODE 8: CONTINUOUS DEPLOYMENT CLOSURE (CI/CD PIPELINE & CAB CABIN)
*🔗 Input Vector:* Validated Git Branch
*🧠 Injected Tensors:* `devops-system-architect`, `ops`
**[Execution Protocol]:** Define End-to-End Test suites validating User Lifecycle (SDLC). 
- **Feature Flag Containment:** Wrap all new Agent-generated logic inside physical LaunchDarkly feature flags (or equivalent `if (ENABLED)` switches) to satisfy CAB Rollback protocols.
- **Enterprise Webhook:** Resolve port-conflicts cleanly by terminating NODE 7 background tasks securely. Append Git Commit Hashes directly relating to the Jira Ticket payload. Draft Infrastructure as Code (IaC) for AWS/Vercel/Cloudflare propagation.
- **Documentation Gate:** Execute `python3 .agents/scripts/validate_development_docs.py --strict-counts` when `/docs/development/` exists. Completion is blocked until the implementation notes and verification evidence are coherent.
- **Continuous Sync Gate:** Execute `python3 .agents/scripts/validate_doc_sync.py --strict` when source files changed. Completion is blocked until changed code is referenced by a sync note and affected docs have been reviewed.

### ⚫ NODE 9: MICRO-BRAIN HISTORICAL ARCHIVING
*🔗 Input Vector:* Runtime Log / Git Diff Context
*🧠 Injected Tensors:* Internal State Machine (Sophia Butler Node)
**[Execution Protocol]:** Audit and compress the entire Session DAG Execution Path. Write architectural shifts and codebase metrics natively to `agents.md` utilizing append-only updates. The final report must list changed code paths and the matching `/docs/development/` notes. Next, execute `python3 .agents/adapters/trustgraph_write.py --run_id "ExecuteRun" --status "success" --target "Project" --skills "all" --score 0.9 --reasoning "Completed backend and frontend integration with development knowledge ledger"` to commit the entire Session Object to the GraphRAG Database. Signal total completion to Operator.
