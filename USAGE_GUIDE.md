# 🧭 ANTIGRAVITY OPERATING MANUAL (ROUTING GUIDE)
**Document Status:** Core / Mandatory Reading (For Human Operators and Autonomous AI)

This document serves as the supreme routing mechanism, specifying precisely **when to leverage Macro Workflows (Slash Commands)** and **when to invoke Targeted Agent Swarms (@Skills)**. 

Optimization relies heavily on context-aware execution: initiating a 9-step heavyweight factory workflow for a minor CSS adjustment is inefficient, just as delegating enterprise-level architectural planning to a single standalone coder agent will result in structural flaws.

---

## 🌊 PHASE 1: MACRO INITIALIZATION & RESTRUCTURING (Slash Commands)
Slash Commands (`/` + workflow) act as heavy artillery. They are exclusively reserved for project initialization, system-wide architectural planning, or profound refactoring.

| Macro Command | Ideal Invocation Context | Core Objective |
|:---|:---|:---|
| `/init_brain` | **MANDATORY first command** triggered at the genesis of any new session. | Boots the AI matrix, spins up the TrustGraph Docker stack automatically, enforces `.clinerules`, and stages the Semantic RAG SKILLS_INDEX. |
| `/marcus.specify` | Any non-trivial feature or governance change that needs durable intent. | Creates `.agents/specs/<feature-id>/spec.md` from the operator goal and records explicit clarification markers. |
| `/marcus.clarify` | A feature spec contains unresolved `[NEEDS CLARIFICATION]` markers. | Resolves ambiguity before technical planning and blocks silent assumptions. |
| `/marcus.plan` | A feature spec is accepted and needs technical translation. | Produces `plan.md`, contracts, data model, quickstart, and agent routing under the feature folder. |
| `/marcus.tasks` | A plan exists and work needs agent-owned execution units. | Derives `tasks.md` with owners, verification methods, and parallel-safe `[P]` groups. |
| `/marcus.verify` | A feature is implemented or ready to close. | Checks acceptance criteria, task evidence, `agents.md` memory, and TrustGraph write attempt. |
| `/marcus_init` | Project inception from scratch (Empty Directory). | Generates the foundational PRD, creates directory scaffolding, and injects the Antigravity OS state files into a clean workspace. |
| `/mobile_init` | Genesis of a new Mobile Application (React Native / Flutter). | Ingests the Mobile Design Doctrine, enforcing cross-platform physical constraints (Safe Area contexts, Spring Animation standards). |
| `/planning` | Project genesis or major feature planning requiring deep research, architecture, diagrams, and durable `/docs` outputs. | Orchestrates Phase 1 V30: preserves the legacy `/docs` output set, adds evidence ledgers under `/docs/research/`, validates claims/sources, strengthens diagrams, and halts for user review. |
| `/design` | Structuring the aesthetic logic (Colors, Typography, Layout constraints). | Orchestrates Phase 2: Prevents redundant planning executions. Emits Figma-logic variables, Hex codes, and Golden ratios. Pure Right-Brain synthesis. Halts for user review. |
| `/develop` | Translating approved architectural mockups, PRDs, & Brands into physical code. | Orchestrates Phase 3: Language-agnostic execution. Generates code, creates `/docs/development/` notes per epic/module/feature/page/task, continuously syncs changed code back into docs, and executes self-healing TDD loops until green. |
| `/doc_reconcile` | Active/brownfield projects whose development docs are stale, flat, shallow, duplicated, or out of sync with code. | Inventories the whole codebase, reviews existing docs, migrates/enriches `/docs/development` to V31.1 epic-first structure, creates epic `issues.md`, labels feature relationships, and updates global docs from code reality. |
| `/refactor-planning` | Targeting established legacy repositories (Brownfield). Requires structural decoupling. | Forces the AI to extract an AST Knowledge Graph via `Understand-Anything` before executing surgical Cyclomatic Complexity reductions safely. |
| `/update_brain`| Pulling upstream system changes to an active ongoing project. | Downloads the latest `.agents` capabilities via `update.sh`. **MUST be followed by `/init_brain`** to Soft Reboot the environment and prevent stale context. |

---

## 🧾 PHASE 1B: SPEC-DRIVEN FEATURE LIFECYCLE

Marcus Fleet now supports a Spec Kit-inspired feature lifecycle without replacing
the existing `.agents` skills, TrustGraph, or legacy `/planning` flow.

Use this lifecycle for meaningful changes:

```bash
python3 .agents/scripts/create_feature_spec.py "Feature Name" --prompt "Original operator prompt"
python3 .agents/scripts/validate_specs.py --feature .agents/specs/001-feature-name
```

Feature workspaces live under:

```text
.agents/specs/<feature-id>/
  spec.md
  plan.md
  tasks.md
  verification.md
  agent-routing.md
  research.md
  data-model.md
  quickstart.md
  contracts/
```

Routing rule:

- Use `/quick_fix` for a tiny localized change that can be verified in one loop.
- Use `/marcus.specify` -> `/marcus.verify` for non-trivial behavior,
  architecture, governance, security, multi-agent, or user-facing changes.
- Use legacy `/planning` when creating broad global `/docs` artifacts for an
  entire new project or a major planning package. V30 still produces the legacy
  files (`prd.md`, `tasks.md`, `knowledge.md`, `decisions.md`, `memory.md`,
  `planning/flows.md`, `planning/screens.md`, `planning/diagrams.md`) and adds
  `/docs/research/` ledgers for sources, evidence, claims, contradictions, and
  manifest. Migrate accepted outputs into feature specs when implementation starts.

Validation rule:

```bash
python3 .agents/scripts/validate_specs.py
python3 .agents/scripts/validate_planning_research.py --root .
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

Run the research validator only when `/docs/research/` exists. It is designed to
catch shallow planning outputs before `/design` or `/develop` consumes them.
Run the development-docs validator only when `/docs/development/` exists. It is
designed to catch code-phase work that changes behavior without preserving
epic/module/feature/page/task implementation memory.
Run the doc-sync validator when source files changed during `/develop`. It is
designed to catch code progress that did not update or intentionally review the
corresponding planning and development docs.
For `/quick_fix`, run doc-sync validation when the hotfix changes behavior, UI,
API contracts, data, tests, or user flows.

Compatibility rule:

- Do not rename or collapse the legacy `/planning` outputs.
- Add research ledgers beside the old files, not instead of them.
- `/design` and `/develop` may use `.agents/specs/<feature-id>/` as extra
  context, but approved `/docs` artifacts remain the default handoff contract.
- `/develop` may add `/docs/development/` artifacts, but must not rewrite or
  collapse the approved planning package.
- `/develop` must update docs by append or targeted patch. Do not replace
  planning/development docs wholesale unless the operator explicitly asks for a
  rewrite.

Code phase documentation rule:

```bash
python3 .agents/scripts/create_development_docs.py --name "Checkout Flow" --feature-id "005-checkout-flow"
python3 .agents/scripts/validate_development_docs.py --strict-counts
```

Expected structure:

```text
docs/development/
  development_manifest.json
  index.md
  E-001-checkout-flow/
    epic.md
    issues.md
    features/F-001-001-checkout-flow.md
    modules/M-001-001-checkout-flow.md
    pages/P-001-001-checkout-flow.md
    tasks/T-001-001-001-checkout-flow.md
    sync/
  sync/
```

Each Markdown artifact must identify its owner skill, source planning/spec
trace, write or code scope, and verification evidence.
New ledgers use V31 epic-first topology. Child docs must include `parent_epic`
and canonical IDs: `E-001-*`, `F-001-001-*`, `M-001-001-*`, `P-001-001-*`,
and `T-001-001-001-*`. Existing legacy-flat ledgers remain readable, but new
work should not create root flat bucket notes unless legacy mode is explicit.

Substantive quality rule:

- Generated development templates are scaffolds, not acceptable deliverables.
- Before closing `/develop`, read `.agents/DEVELOPMENT_DOCS_QUALITY_RUBRIC.md`.
- Strict validation rejects `TBD`, `pending`, `<Name>`, unchecked boxes, generic
  bullets, missing code paths, missing rationale, and shallow notes.
- PM-facing notes must explain impact, tradeoff, evidence, and risk.
- Every epic/module/feature/page/task note must contain a useful Mermaid diagram.
- Every behavior-changing code slice must update at least one global planning
  document under `/docs`; feature docs alone are not enough.
- Docs must be updated or confirmed before code begins.
- Every epic/module/feature/page/task note must include Jira-style Story,
  Priority, Relationship Map, and Work Log.
- Every epic must include an `issues.md` file reviewed with QA skill reasoning.
- Relationship labels must be explicit: `DEPENDS_ON`, `BLOCKS`, `ENABLES`,
  `IMPLEMENTS`, `USES`, `EXTENDS`, `CONFLICTS_WITH`, `SUPERSEDES`,
  `DUPLICATES`, `RELATES_TO`.

Continuous documentation sync rule:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "Checkout API slice" --changed-files "src/api/checkout.ts,tests/checkout.test.ts"
python3 .agents/scripts/validate_doc_sync.py --strict
```

For V31 ledgers, prefer:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "Checkout API slice" --epic-id "E-001-checkout-flow" --changed-files "src/api/checkout.ts,tests/checkout.test.ts"
```

The sync note must say which legacy docs changed, which development ledger notes
changed, and which docs were intentionally left unchanged. This gives a PM a
living POC package instead of stale planning documents.
It must also capture docs-before-code evidence and related feature review.

Brownfield reconciliation rule:

```bash
python3 .agents/scripts/audit_development_docs.py --root .
```

Use `/doc_reconcile` when a project is already mid-build and docs do not match
code. The command must review the full code inventory, map code clusters to
epics/features/modules/pages/tasks, create or update epic `issues.md`, label all
relationships, update global docs, and run strict validators before returning.

Quick fix documentation rule:

- If `/quick_fix` only changes comments, formatting, or a non-behavioral typo,
  record the session in `agents.md` and TrustGraph as usual.
- If `/quick_fix` changes behavior, UI, API contracts, data, tests, or user
  flows, it must also create a doc sync note and run `validate_doc_sync.py`.

---

## 🎯 PHASE 2: TARGETED MICRO-ROUTING (Executing @Skills)
During active mid-project development, **DO NOT RE-INVOKE OVERARCHING SLASH COMMANDS**. Operators should rely on the `/quick_fix` bypass or explicitly invoke Targeted AI Agents (`@skills`) to guarantee precision execution while maximizing token economy.

📌 *Directive for Antigravity AI: Upon processing a prompt containing an `@skill-name`, you MUST immediately utilize the `view_file` tool to load the corresponding `SKILL.md` file designated by that identifier.*

### 🛠️ 1. High-End Frontend Engineering Swarm (UI/UX & Animations)
> **Syntax Prompt Example:** *"Please utilize `@benny-frontend-engineer`, `@bella-frontend-animator`, and `@maya-ui-ux-designer` to construct this Hero Section strictly adhering to Linear-grade standards."*
- **@maya-ui-ux-designer:** Guarantees strict adherence to the foundational layout requirements and structural integrity.
- **@benny-frontend-engineer:** Enforces perfect grid alignment (4px/8px margins/padding), Border Radius standards, and Tailwind hierarchies.
- **@bella-frontend-animator:** Injects advanced Framer Motion transitions, perpetual state spinners, and glow effects.

### 🛡️ 2. Autonomous TDD & Quality Assurance Swarm
> **Syntax Prompt Example:** *"Please deploy `@ada-qa-agent` and `@qa-simulator` to investigate an API 401 error rendering on the Login Screen."*
- **@ada-qa-agent:** Engineers the overarching test strategy and ensures test coverage metrics are met.
- **@qa-simulator:** Autonomously executes terminal instances, renders the UI locally, and uses `curl` / browser automation to catch React Hydration errors.
- **@eve-qa-approver:** Conducts rapid, uncompromising peer reviews of generated Pull Requests.

### 🏛️ 3. Systems Architecture & Infrastructure Swarm
> **Syntax Prompt Example:** *"I need to restructure the monolithic backend. Summon `@david-systems-architect`, `@alan-tech-lead`, and `@chartis-data-visualizer` to map out the C4 Diagram."*
- **@david-systems-architect:** Architects the root Feature-Sliced Design (FSD) directory structure.
- **@alan-tech-lead:** Reviews Data Models and API Data Contracts to prevent payload mismatch.
- **@chartis-data-visualizer:** Generates comprehensive PlantUML/Mermaid diagrams representing the new topology.

### 🧠 4. Langchain RAG & Vector Processing Swarm
> **Syntax Prompt Example:** *"Have `@homer-knowledge-extractor` parse this documentation corpus, then utilize `@rag-architect` to build our semantic Vector Database."*
- Unstructured Data Parsing (PDFs, industry documents): Requires **@homer-knowledge-extractor**.
- Structuring Vector DBs & Langchain Pipelines: Requires **@rag-architect** and **@langchain-rag**.

---

## 🚩 AUTONOMOUS DELEGATION (AI-DRIVEN CHAINING PROTOCOL)
Within the `Marcus Fleet` Matrix, operators hold the right to orchestrate multi-agent chains.

**Core Directives for the Antigravity AI Engine:**
When the Operator assigns a macro-level objective (e.g., *"Fix the checkout cart layout and write coverage tests"*) without explicit skill tags, the Antigravity Engine **MUST AUTONOMOUSLY DELEGATE (RAG Routing)**:
1. Scan the `SKILLS_INDEX.md` dictionary for contextually appropriate Tags.
2. Dynamically Lazy-Load the most relevant agents (e.g., **[Frontend] (Benny)** + **[QA/Test] (Ada)**) into the Context Window.
3. Transition state to the Frontend Agent to refactor the UI component.
4. Transition state to the QA Agent to automatically execute the Terminal test suites.
5. Code Error Encountered? Activate the V30 Circuit Breaker protocol.
6. Execution Successful? Log the transaction securely into `.agents/agents.md` and the localized `.agents/brain/` component history.

Final Doctrine: **A true General AI (Antigravity) does not blindly generate code; it routes specialized capability sets (Skills) to conquer complex objectives with surgical precision.**
