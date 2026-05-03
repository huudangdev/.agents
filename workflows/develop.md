---
description: Marcus Fleet Enterprise SDLC Phase 3 (Code Execution, TDD, & Continuous Delivery)
---

# Execution Factory Matrix (Phase 3)

> This workflow governs code generation, testing, documentation, and deployment. It must use the smallest credible context set for the task at hand. Reading everything is not rigor; it is routing failure.

---

## ⬛ SYSTEMIC MEMORY & STATE INHERITANCE (ANTI-AMNESIA PROTOCOLS)

<state_propagation_boundary>
**MINIMUM VIABLE CONTEXT:** `/develop` must not ingest the whole planning corpus by default.
Read only the artifacts needed for the active write scope:

- Always read:
  - root `agents.md`
  - `.agents/memory/constitution.md`
  - the active `.agents/specs/<feature-id>/execution-brief.md`
- Inside `execution-brief.md`, read these subsections first and treat them as
  the routing contract for the current slice:
  - `### Task Shape Decision`
  - `### Required Reads`
  - `### Forbidden Default Reads`
  - `### Expansion Triggers`
- Always read the `docs/development/` notes explicitly listed under
  `execution-brief.md#Development Ledger Context`
- Expand into the active `.agents/specs/<feature-id>/spec.md`, `plan.md`,
  `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only
  when the brief shows that the write scope or failing evidence requires it
- Read `/docs` selectively:
  - UI-only changes: relevant brand, page, feature, and QA docs only
  - API/data changes: relevant contracts, data-model, module, and rollback docs only
  - architecture/refactor changes: relevant diagrams, decisions, and affected module docs only
- Do not read unrelated `/docs` files "just in case".
- If a document cannot materially change the implementation decision, skip it.
- If the execution brief is missing or stale, stop and rebuild it before code work.
- Do not read the entire `docs/development/` tree by default. Read the exact
  epic/feature/module/page/task notes named by the brief for the current slice.
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

<spec_execution_gate>
**SPEC EXECUTION GATE:** `/develop` MUST abort before behavior-changing edits if
the selected `.agents/specs/<feature-id>/` workspace fails
`python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>`.
The remediation path is to repair the spec, plan, tasks, and verification
package first. This gate also fails when `execution-brief.md` is stale relative
to the spec package or matched `docs/development/` notes. Code work is
downstream of validated execution artifacts, not a substitute for them.
Before behavior-changing edits, prefer the replayable wrapper:
`python3 .agents/scripts/run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>`.
That wrapper appends structured local evidence under `.agents/logs/harness/`
so the active chain and first failing command can be reviewed without scraping
raw console output.
</spec_execution_gate>

<scope_routing_gate>
**SCOPE ROUTING GATE:** `/develop` must classify the task before loading skills or
files:

- `UI-only`: component, page, style, accessibility, copy, animation
- `Frontend behavior`: client state, form logic, browser interaction
- `Backend/API`: routes, auth, services, queues, persistence
- `Data/contract`: schema, migration, SQL, Supabase, ORM, analytics events
- `Architecture/refactor`: boundaries, decomposition, cross-module concerns

Hard rules:

- A `UI-only` or `Frontend behavior` task must not inspect Supabase, database
  schemas, SQL, migrations, or analytics tooling unless the active spec or
  failing evidence explicitly points to a data-contract cause.
- A `Backend/API` or `Data/contract` task does not need to ingest visual design
  docs unless user-facing behavior or QA evidence depends on them.
- If the task classification changes mid-run, record the reason in
  `verification.md` before widening context.
</scope_routing_gate>

<skill_budget_gate>
**SKILL BUDGET GATE:** `/develop` must load the smallest skill set that can
finish the task.

- Default target: 2 to 4 skills.
- UI-only work: prefer frontend/design/QA skills only.
- Backend/data work: prefer architecture/backend/QA/security skills only.
- Do not summon analytics, RAG, orchestration, or cloud skills unless the spec,
  tasks, or failing evidence names that surface explicitly.
</skill_budget_gate>

<routing_regression_gate>
**ROUTING REGRESSION GATE:** When `/develop` behavior is changed or a new
release is being evaluated, run the task-shape checks in:

```text
.agents/ROUTING_REGRESSION_CHECKLIST.md
```

If a narrow task drifts into unrelated database, analytics, infrastructure, or
full-repo context without evidence, treat that as a routing regression and fix
the workflow or skill index before trusting the release.
</routing_regression_gate>

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

## Context Routing Matrix

Before any code read beyond the active files, choose one route:

| Task Shape | Required Reads | Preferred Skills | Forbidden Default Reads |
| --- | --- | --- | --- |
| UI-only | feature spec package, relevant page/feature docs, target components | `benny-frontend-engineer`, `maya-ui-ux-designer`, `ada-qa-agent` | Supabase, SQL, migrations, analytics, cloud configs |
| Frontend behavior | feature spec package, target components/hooks, relevant QA docs | `benny-frontend-engineer`, `alan-tech-lead`, `ada-qa-agent` | unrelated backend modules, data warehouse, cloud infra |
| Backend/API | feature spec package, contracts, data-model, affected services/tests | `alan-tech-lead`, `david-systems-architect`, `ada-qa-agent` | brand/theme docs unless UI/API coupling demands it |
| Data/contract | feature spec package, contracts, schema/model docs, rollback docs | `david-systems-architect`, `alan-tech-lead`, `cipher-security-approver` | unrelated page/component docs |
| Architecture/refactor | feature spec package, affected modules, decisions, diagrams | `david-systems-architect`, `alan-tech-lead`, `refactor-plan` | full repo scans without a bounded module list |

Escalate instead of widening context blindly when:

- the active feature workspace does not identify the affected write scope
- the failing evidence contradicts the chosen task shape
- the same hypothesis fails 3 times without new information

## Chronological Execution Nodes (Phase 3)

### Node 4: Execution Knowledge Ledger Bootstrap
*Input Vector:* active feature workspace, targeted `/docs` notes only
*Injected Skills:* routing, documentation, PM, and only the implementation skills needed by the chosen task shape
*Emitted Artifacts:* `/docs/development/development_manifest.json`, `/docs/development/index.md`, epic-first Markdown notes.
**[Execution Protocol]:** Decompose approved work into durable implementation documentation before code mutation. Each agent receiving a write scope must own at least one task note and, when applicable, one module/feature/page note under the correct `E-###-*` directory. Notes must include YAML frontmatter, `owner_skill`, `parent_epic` for child notes, `source_trace`, and `verification`.
Before code mutation, write the Story/Priority, Relationship Map, Issues, and
Work Log entries needed to prove the agent understands parent-child and sibling
feature relationships.
If `execution-brief.md#Development Ledger Context` names no matching ledger
notes for the active slice, stop and either:

- create them with `python3 .agents/scripts/create_development_docs.py --name "<epic-or-feature-name>" --feature-id "<feature-id>" --epic-number 001 --child-number 001 --task-number 001`, or
- route to `/doc_reconcile` when the project is brownfield or the ledger is stale.

Do not begin code edits until the required development-ledger notes exist and
have the minimum planned write scope.

### Node 5: Route-Specific Implementation
*Input Vector:* only the docs, code, and tests needed by the chosen task shape
*Injected Skills:* route-specific implementation and QA skills
*Emitted Artifacts:* changed code, tests, and updated notes for the active slice.
**[Execution Protocol]:**

- UI-only/frontend work starts from target components, page notes, and verification evidence.
- Backend/data work starts from contracts, services, models, and verification evidence.
- Do not route all work through backend scaffolding by default.
- If a feature-scoped workspace exists, use `execution-brief.md` as the primary
  entrypoint and expand into full spec/docs only when the current write scope or
  failing evidence requires it.
- Update only the relevant module, feature, page, and task notes with code paths, public contracts, and command evidence.

### 🔁 NODE 6.5: DOC SYNC CHECKPOINT
*🔗 Input Vector:* Git diff, changed source files, `/docs`, `/docs/development/`
*🧠 Injected Tensors:* `knowledge-work-architecture`, `development-ledger-architect`, `sophia-product-manager`, `ada-qa-agent`
*📦 Emitted Artifacts:* `/docs/development/E-###-*/sync/*.md` or `/docs/development/sync/*.md`, targeted updates to affected docs.
**[Execution Protocol]:** After each code slice, create a sync note, map changed source files to affected legacy planning docs and development ledger notes, apply targeted append/patch updates, reconcile manifest/index when needed, then run `validate_doc_sync.py --strict`. This node is a continuation gate: the next code slice is blocked when source files changed but documentation trace is missing.
Strict validation also rejects shallow or template-only sync notes, missing
Mermaid diagrams, and code changes without a global `/docs` update.
Strict validation also rejects missing docs-before-code evidence.

### Node 6: Zero-Downtime Live Simulation
*Input Vector:* relevant page/component docs and QA expectations only when the route is user-facing
*Injected Skills:* frontend and QA simulation skills only when needed
**[Execution Protocol]:** Spawning the Daemon Simulator: Execute the bash command `npm run dev` or equivalent to mount a localized Runtime Protocol.
- **Bi-Directional Mutation Feedback:**
  - `benny-frontend-engineer` algorithmically renders UI Components enforcing predefined strict Spatial parameters based on `BRAND_GUIDELINES.md`.
  - `qa-simulator` evaluates the rendered port utilizing `playwright` telemetry or `cURL`. Evaluates UI Hydration errors, layout shifts, or Exceptions.
  - Page notes must be updated with route, states, interactions, accessibility checks, screenshots/manual evidence, and responsive verification.
  - **The V30 Circuit Breaker:** If a specific rendering loop generates $\ge 3$ sequential compile errors, gracefully terminate the Node, flag a Terminal Red-Alert, and request Human Operator intervention.

### Node 7: Continuous Deployment Closure
*🔗 Input Vector:* Validated Git Branch
*🧠 Injected Tensors:* `devops-system-architect`, `ops`
**[Execution Protocol]:** Define End-to-End Test suites validating User Lifecycle (SDLC). 
- **Feature Flag Containment:** Wrap all new Agent-generated logic inside physical LaunchDarkly feature flags (or equivalent `if (ENABLED)` switches) to satisfy CAB Rollback protocols.
- **Enterprise Webhook:** Resolve port-conflicts cleanly by terminating NODE 7 background tasks securely. Append Git Commit Hashes directly relating to the Jira Ticket payload. Draft Infrastructure as Code (IaC) for AWS/Vercel/Cloudflare propagation.
- **Documentation Gate:** Execute `python3 .agents/scripts/validate_development_docs.py --strict-counts` when `/docs/development/` exists. Completion is blocked until the implementation notes and verification evidence are coherent.
- **Continuous Sync Gate:** Execute `python3 .agents/scripts/validate_doc_sync.py --strict` when source files changed. Completion is blocked until changed code is referenced by a sync note and affected docs have been reviewed.
- **Harness Postflight Gate:** Before final closeout, prefer `python3 .agents/scripts/run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>` so command-surface, routing, freshness, and readiness checks replay in one deterministic chain.

### Node 8: Historical Archiving
*🔗 Input Vector:* Runtime Log / Git Diff Context
*🧠 Injected Tensors:* Internal State Machine (Sophia Butler Node)
**[Execution Protocol]:** Audit and compress the entire Session DAG Execution Path. Write architectural shifts and codebase metrics natively to `agents.md` utilizing append-only updates. The final report must list changed code paths and the matching `/docs/development/` notes. Next, execute `python3 .agents/adapters/trustgraph_write.py --run_id "ExecuteRun" --status "success" --target "Project" --skills "all" --score 0.9 --reasoning "Completed backend and frontend integration with development knowledge ledger"` to commit the entire Session Object to the GraphRAG Database. Signal total completion to Operator.
