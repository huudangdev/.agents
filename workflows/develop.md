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

<brownfield_reconcile_gate>
**BROWNFIELD GATE:** `/develop` MUST abort before source edits when the project
is already in progress and any of the following are true: required planning docs
are missing, `README.md` is still boilerplate while code has moved beyond it,
`/docs/development/` is missing or template-only, the ledger does not match code
reality, or quality gates would fail. In those cases the only valid next step
is `/doc_reconcile`, followed by strict validation, then resume `/develop` from
the reconciled docs package.
</brownfield_reconcile_gate>

---

## 🧾 CODE PHASE KNOWLEDGE CONTRACT (MANDATORY)

`/develop` MUST NOT only emit source code. Every code-phase run that implements
or materially changes behavior must maintain a dedicated development knowledge
ledger. V31 uses an epic-first topology as the default source of truth:

```text
/docs/development/
├── development_manifest.json
├── index.md
├── E-001-<epic-description>/
│   ├── epic.md
│   ├── issues.md
│   ├── features/F-001-001-<feature-description>.md
│   ├── modules/M-001-001-<module-description>.md
│   ├── pages/P-001-001-<page-description>.md
│   ├── tasks/T-001-001-001-<task-description>.md
│   └── sync/
├── sync/        # legacy/global sync fallback remains valid
└── _archive/    # stale flat or duplicate notes only after explicit migration
```

Legacy flat ledgers (`epics/`, `modules/`, `features/`, `pages/`, `tasks/`) are
still readable when an existing manifest does not opt into `topology:
epic_first`. New ledgers must use V31 epic-first unless the operator explicitly
requests legacy compatibility.

Minimum artifact rules:

1. **Epic notes** (`E-###-*/epic.md`) capture delivery outcomes, acceptance
   boundaries, linked children, and evidence.
2. **Epic issue notes** (`E-###-*/issues.md`) capture QA-detected or
   QA-reviewed issues, risks, blockers, evidence, and resolution.
3. **Feature notes** (`E-###-*/features/F-###-###-*.md`) capture user behavior,
   requirement traceability, code scope, rollout, and risk.
4. **Module notes** (`E-###-*/modules/M-###-###-*.md`) capture code ownership,
   public contracts, dependencies, failure modes, and verification.
5. **Page notes** (`E-###-*/pages/P-###-###-*.md`) capture route/screen state,
   interactions, accessibility, and visual verification. If the task is backend
   only, set `minimum_children.pages: 0` and record why in `index.md`.
6. **Task notes** (`E-###-*/tasks/T-###-###-###-*.md`) capture execution log,
   write scope, commands, results, blockers, and handoff.

Canonical ID rules:

- Epic: `E-001-short-description`
- Issues: `ISSUES-E-001-short-description` in `issues.md`
- Feature: `F-001-001-short-description`
- Module: `M-001-001-short-description`
- Page: `P-001-001-short-description`
- Task: `T-001-001-001-short-description`
- Child note frontmatter must include `parent_epic: E-001-short-description`.
- Filename stem and frontmatter `id` must match exactly.
- Do not create `epic-epic-*`, `feature-epic-*`, `*-000`, or title-only slug
  files.

Initialize the ledger before code edits:

```bash
python3 .agents/scripts/create_development_docs.py --name "<epic-or-feature-name>" --feature-id "<optional-feature-id>" --epic-number 001 --child-number 001 --task-number 001
```

Before the first source edit in any code slice:

1. Read the owning `E-###-*/epic.md` and all related child notes named in its
   `Relationship Map`.
2. Update the affected epic/feature/module/page/task note with the planned
   Story, Priority, relationship labels, and Work Log entry.
3. Ensure the epic has an `issues.md` file reviewed by `ada-qa-agent` or an
   equivalent QA skill.
4. Review sibling feature relationships using labels such as `DEPENDS_ON`,
   `BLOCKS`, `ENABLES`, `IMPLEMENTS`, `USES`, `EXTENDS`, `CONFLICTS_WITH`,
   `SUPERSEDES`, `DUPLICATES`, and `RELATES_TO`.
5. Only then perform source code edits.

If the agent cannot satisfy steps 1-4 because the docs package is absent,
misleading, or non-substantive, it must stop and route to `/doc_reconcile`
instead of improvising missing context.

Validate the ledger before reporting completion:

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

The code phase docs are not a replacement for `/planning` outputs. They are a
fine-grained implementation memory layer that keeps each epic, module, task,
feature, and page inspectable after code is generated.

### Documentation Quality Gate

Before closing any code slice, read:

```text
.agents/DEVELOPMENT_DOCS_QUALITY_RUBRIC.md
```

Generated templates are only scaffolds. They are invalid until every placeholder,
`TBD`, `pending`, unchecked checklist item, and generic bullet is replaced with
project-specific facts. Each note must include PM-visible impact, exact code
paths, rationale, tradeoffs, verification evidence, residual risk, and a useful
Mermaid diagram.

Every note must also include Jira-grade `Story` and `Priority`, labeled feature
relationships, and a `Work Log`. Every epic must include QA-reviewed `Issues`.

---

## 🔁 CONTINUOUS DOCUMENTATION SYNC LOOP (MANDATORY)

During POC execution, `/develop` is a repeated loop: code, test, inspect,
adjust, and continue. Documentation must move with that loop.

After every material code slice, the active agent MUST run a documentation sync
cycle before proceeding to the next slice:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "<code-slice-name>" --changed-files "<comma-separated-files>"
```

For V31 epic-first ledgers, prefer epic-local sync notes:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "<code-slice-name>" --epic-id "E-001-short-description" --changed-files "<comma-separated-files>"
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
6. **Update at least one global planning doc** under `/docs` for behavior-
   changing code slices.
7. **Refresh Mermaid diagrams** in epic/feature/page/module/task docs and, when
   architecture or flow changes, in `docs/planning/diagrams.md`.
8. **Reconcile manifest/index** when a new child doc is added, renamed,
   archived, or moved between epics.
9. **Record docs-before-code evidence** in the sync note: docs read, docs
   updated, relationship map reviewed, and related features checked.

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
*🧠 Injected Tensors:* `marcus-ai-orchestrator`, `knowledge-work-architecture`, `development-ledger-architect`, `sophia-product-manager`
*📦 Emitted Artifacts:* `/docs/development/development_manifest.json`, `/docs/development/index.md`, epic-first Markdown notes.
**[Execution Protocol]:** Decompose approved work into durable implementation documentation before code mutation. Each agent receiving a write scope must own at least one task note and, when applicable, one module/feature/page note under the correct `E-###-*` directory. Notes must include YAML frontmatter, `owner_skill`, `parent_epic` for child notes, `source_trace`, and `verification`.
Before code mutation, write the Story/Priority, Relationship Map, Issues, and
Work Log entries needed to prove the agent understands parent-child and sibling
feature relationships.

### 🔵 NODE 5 & 6: ADVERSARIAL QA & TDD BACKEND SCAFFOLDING
*🔗 Input Vector:* `/docs/planning/diagrams.md`, `/docs/knowledge.md`, `/docs/prd.md`, `/docs/development/E-###-*/modules/*.md`, `/docs/development/E-###-*/features/*.md`
*🧠 Injected Tensors:* `eve-qa-approver`, `alan-tech-lead`, `ada-qa-agent`
*📦 Emitted Artifacts:* Database migrations, route handlers, integration suites, updated module/feature/task notes.
**[Execution Protocol]:** Initialize Backend Infrastructure via Test-Driven Development (TDD). Generate isolated Unit-Test stubs detailing Boundary-Value handling and Fault Injection (Negative Path APIs). Validate API schemas against Null-value crashes before writing business logic. Update the relevant module, feature, and task notes with code paths, public contracts, and command evidence.

### 🔁 NODE 6.5: DOC SYNC CHECKPOINT
*🔗 Input Vector:* Git diff, changed source files, `/docs`, `/docs/development/`
*🧠 Injected Tensors:* `knowledge-work-architecture`, `development-ledger-architect`, `sophia-product-manager`, `ada-qa-agent`
*📦 Emitted Artifacts:* `/docs/development/E-###-*/sync/*.md` or `/docs/development/sync/*.md`, targeted updates to affected docs.
**[Execution Protocol]:** After each code slice, create a sync note, map changed source files to affected legacy planning docs and development ledger notes, apply targeted append/patch updates, reconcile manifest/index when needed, then run `validate_doc_sync.py --strict`. This node is a continuation gate: the next code slice is blocked when source files changed but documentation trace is missing.
Strict validation also rejects shallow or template-only sync notes, missing
Mermaid diagrams, and code changes without a global `/docs` update.
Strict validation also rejects missing docs-before-code evidence.

### 🟣 NODE 7: ZERO-DOWNTIME LIVE SIMULATION (FSM FEEDBACK LOOP)
*🔗 Input Vector:* `/docs/BRAND_GUIDELINES.md`, `/docs/planning/screens.md`, `/docs/development/E-###-*/pages/*.md`
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
