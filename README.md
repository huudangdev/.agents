<div align="center">
  <h1>🚀 Marcus Fleet Enterprise Matrix (.agents)</h1>
  <p><strong>The Academic Distributed AGI Core for Feature-Sliced Design, Semantic RAG Routing, and Deterministic Autonomous DevOps.</strong></p>

  ![Version](https://img.shields.io/badge/epoch-v31.2-blue.svg?style=for-the-badge)
  ![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)
  ![Routing](https://img.shields.io/badge/routing-Semantic%20RAG-orange.svg?style=for-the-badge)
  ![Governance](https://img.shields.io/badge/governance-SOC2%20CAB-purple.svg?style=for-the-badge)

  <p>
    <a href="#-enterprise-overview-v310">Overview</a> •
    <a href="#-system-architecture-topology">Architecture</a> •
    <a href="#-spec-driven-governance-layer">Spec Governance</a> •
    <a href="#-installation-provisioning--universal-portability-v310">Provisioning</a> •
    <a href="#execution-commands">Execution</a> •
    <a href="#academic-contributions">Contributions</a> •
    <a href="#sponsorship--support">Support/Donate</a>
  </p>
</div>

---

## 🔬 Enterprise Overview (V31.2)

The **Marcus Fleet Enterprise Matrix** represents a paradigm shift in Large Language Model (LLM) orchestration frameworks explicitly built for Enterprise Mono-repos. Distancing itself from monolithic unstructured chat, **Version 31.2** operates as an intelligent computational core bridging **Git-Hook Incremental RAG**, **Spec-Driven Governance**, **Deep Research Planning**, **Epic-First Develop Knowledge Ledgers**, **Brownfield Doc Reconciliation**, **Continuous Documentation Sync**, **Ephemeral Sandboxed Execution**, and **OpenTelemetry CI pipelines**.

By binding Agents to rigorous Finite State Machines (FSM) and forcing OS interactions through secure Ephemeral Sandboxes, the Antigravity ecosystem mitigates catastrophic automated failures, token exhaustion, and context window atrophy in codebases exceeding 1 million lines.

### The Bounded Stochastic Execution (Air-Gapped Sandbox & Multi-Tenant IAM)
The core system enforces execution guardrails. No LLM interfacing with the `.agents` ecosystem possesses authorization to run destructive CLI instructions arbitrarily. The matrix is strictly compelled to funnel high-risk bash generation through the `.agents/run_sandboxed.sh` wrapper, which rejects shell metacharacter chaining, applies an explicit command allow-list, and observes exit states to trigger OpenTelemetry Audit logs. Furthermore, all physical architecture alterations are gated by `.agents/iam_verify.sh` to enforce **Multi-Tenant Identity** isolation and CAB Role-Based Access Control (RBAC).

---

## 🏛️ System Architecture Topology

The following C4-styled data-flow layout outlines the cognitive processing, lexical retrieval routing, and execution mechanisms.

```mermaid
graph TD
    subgraph HumanOperator ["Human Operator Context"]
        U([User Entity]) -->|Stochastic Heuristic Requests| OS{Antigravity Dispatcher}
    end
    
    subgraph SemanticRetrieval ["Semantic Retrieval Matrix"]
        OS -->|Regex / Keyword Scanning| Index[(SKILLS_INDEX Dictionary)]
        Index -->|N-Dimensional Selection| Router[Agent Routing Algorithm]
    end
    
    subgraph CognitiveAttention ["Cognitive Attention Layer"]
        Router -->|Lazy-load Context - Top-K Nodes| Context[LLM Context Window]
        Context <-->|Chronological File Append| LocalMemory[(.brain Local State Memory)]
    end
    
    subgraph ExecutionAutomata ["Execution Automata - Sandboxed IO"]
        Context -->|Native OS Shell Execution| Terminal[Terminal Environment]
        Terminal -->|Status 0 - Green| Validate[TDD Assertion Passed]
        Terminal -->|Status Not 0 - Exception| Tripper{FSM Circuit Breaker}
        Tripper -->|Failures < 3| HeuristicFeedback[Internal Self-Correction Loop]
        HeuristicFeedback --> Context
        Tripper -->|Failures >= 3| HardBlock[Execution Halting State]
        HardBlock -.->|Red Flag Ping or Terminate| U
    end

    classDef blue fill:#2563eb,stroke:#1d4ed8,stroke-width:2px,color:#fff;
    classDef orange fill:#ea580c,stroke:#c2410c,stroke-width:2px,color:#fff;
    classDef gray fill:#4b5563,stroke:#374151,stroke-width:2px,color:#fff;
    
    class U blue
    class HardBlock orange
    class LocalMemory gray
```

### 🧠 TrustGraph: Graph of Thoughts (GoT) RAG Schema

The most potent element of the Antigravity Brain is the Neo4j backend **TrustGraph**. As agents act, succeed, or fail, they emit Cognitive Vectors mapping their thought processes back into the knowledge graph. This self-healing topological memory is visualized natively via our **3D Particle Engine**.

```mermaid
graph TD
    classDef Run fill:#1e293b,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef Module fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef Skill fill:#334155,stroke:#ec4899,stroke-width:2px,color:#fff;

    subgraph Pipeline ["TrustGraph GoT Data Pipeline"]
        Agent[Agent Workflow] -->|adapter/trustgraph_write.py| Adapter[Graph Adapter]
        Adapter -->|Stores score & reasoning| Neo4j[(Neo4j Vector DB)]
        Neo4j --> Engine[Three.js Graph Engine]
    end

    subgraph Render ["3D Rendering (Graph Ontology V2)"]
        R1((Run_Task)):::Run
        M1[Module.ts]:::Module
        S1{rag-architect}:::Skill

        R1 -- "[:OPTIMIZED] score: 0.95" --> M1
        R1 -- "[:CAUSED_ERROR] score: 0.4" --> M1
        R1 -- "[:LEVERAGED]" --> S1
    end
```

---

## 🧾 Spec-Driven Governance Layer

Marcus Fleet now includes a local Spec Kit-inspired lifecycle for non-trivial
agent work. This layer is additive: it does not replace the skill swarm,
TrustGraph, O11y, sandboxing, or legacy `/planning` workflow.

Core artifacts:

```text
.agents/
├── memory/
│   └── constitution.md              # Stable principles and governance gates
├── templates/                       # Feature artifact templates
├── scripts/
│   ├── create_feature_spec.py        # Creates .agents/specs/NNN-slug/
│   ├── validate_specs.py             # Validates required files and gates
│   ├── validate_planning_research.py # Validates deep research ledgers
│   ├── audit_development_docs.py     # Inventories code/docs for brownfield reconciliation
│   ├── sync_project_mcp.py           # Publishes bundled MCP servers into project-root .mcp.json
│   ├── create_development_docs.py    # Creates /docs/development scaffolds
│   ├── validate_development_docs.py  # Validates code-phase knowledge notes
│   ├── create_doc_sync_note.py       # Creates per-code-slice sync notes
│   └── validate_doc_sync.py          # Validates docs kept pace with code
└── specs/
    └── 001-marcus-spec-foundation/   # First validated feature workspace
```

Typical usage:

```bash
python3 .agents/scripts/create_feature_spec.py "Feature Name" --prompt "Operator goal"
python3 .agents/scripts/validate_specs.py --feature .agents/specs/001-feature-name
```

The workflow sequence is:

```text
/marcus.specify -> /marcus.clarify -> /marcus.plan -> /marcus.tasks -> /marcus.verify
```

This gives agents a concrete contract before code changes: `spec.md` captures
what and why, `plan.md` captures how, `tasks.md` captures ownership, and
`verification.md` captures evidence.

### Backward Compatibility Contract

V30 is additive. The historical slash-command surface remains valid:

- `/planning` still emits the legacy `/docs` planning files.
- `/design` still consumes `/docs/planning/*` and emits visual guidance.
- `/develop` still consumes approved `/docs` artifacts before code generation.
- `/quick_fix` remains the low-latency path for localized fixes.

The new spec lifecycle and research ledgers strengthen acceptance criteria,
evidence tracking, and implementation readiness without replacing these flows.

### Code Phase Knowledge Ledger

V31 extends the V30.1 documentation contract for `/develop`. Code generation now has to
leave implementation memory behind, not only source files:

```text
docs/development/
├── development_manifest.json
├── index.md
├── E-001-feature-or-epic-name/
│   ├── epic.md
│   ├── issues.md
│   ├── features/F-001-001-feature-or-epic-name.md
│   ├── modules/M-001-001-feature-or-epic-name.md
│   ├── pages/P-001-001-feature-or-epic-name.md
│   ├── tasks/T-001-001-001-feature-or-epic-name.md
│   └── sync/
├── sync/
└── _archive/
```

The scaffold command is:

```bash
python3 .agents/scripts/create_development_docs.py --name "Feature Name" --feature-id "005-feature-name" --epic-number 001 --child-number 001 --task-number 001
python3 .agents/scripts/validate_development_docs.py --strict-counts
```

Each Markdown note must include frontmatter with `owner_skill`, `source_trace`,
and `verification`, plus the code or write scope it governs. Child notes must
also include `parent_epic`, and their frontmatter `id` must match the filename
stem exactly. This keeps epic, module, feature, page, and task knowledge
queryable by future agents.

Strict mode uses [DEVELOPMENT_DOCS_QUALITY_RUBRIC.md](./DEVELOPMENT_DOCS_QUALITY_RUBRIC.md)
to reject template-only output. Docs must include concrete code paths,
PM-visible impact, rationale, tradeoffs, evidence, residual risk, and Mermaid
diagrams. Behavior-changing code slices must also update at least one global
planning document under `/docs`.

V31.1 adds product-grade governance: docs are updated before code, every
epic/module/feature/page/task note carries Jira-style Story and Priority,
relationship labels, and a Work Log, and every epic carries a QA-reviewed
`issues.md` file.
Relationship labels include `DEPENDS_ON`, `BLOCKS`, `ENABLES`, `IMPLEMENTS`,
`USES`, `EXTENDS`, `CONFLICTS_WITH`, `SUPERSEDES`, `DUPLICATES`, and
`RELATES_TO`.

V31 uses epic-first documentation as the source of truth for new ledgers. Legacy
flat buckets remain readable for older projects, but new files should not be
created under root `epics/`, `modules/`, `features/`, `pages/`, or `tasks/`
unless legacy mode is explicitly requested.

### Continuous Documentation Sync

V30.2 adds a PM-grade continuity gate for long POC builds. After each material
code slice, agents create a sync note and patch only the affected documents:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "Checkout API slice" --changed-files "src/api/checkout.ts,tests/checkout.test.ts"
python3 .agents/scripts/validate_doc_sync.py --strict
```

For V31 ledgers, prefer epic-local sync notes:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "Checkout API slice" --epic-id "E-001-checkout" --changed-files "src/api/checkout.ts,tests/checkout.test.ts"
```

The sync note must include `## Docs Before Code` evidence: docs read, docs
updated, relationship map reviewed, and related features checked.

This keeps the original planning package, development ledger, and current code
aligned without replacing whole documents. New facts are appended, changed facts
are patched in place, and unchanged docs are explicitly marked as reviewed.

### Brownfield Docs Reconciliation

V31.2 adds `/doc_reconcile` for active projects whose docs drifted from code.
The command first inventories the whole codebase, then rebuilds or enriches
`/docs/development` into V31.1 epic-first docs with canonical names, real
content, relationship labels, Jira Story/Priority, epic `issues.md`, Mermaid,
and global docs sync.

```bash
python3 .agents/scripts/audit_development_docs.py --root .
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

Use `/doc_reconcile` before resuming `/develop` on a project whose development
docs contain flat buckets, duplicate names, empty templates, missing Mermaid,
stale planning docs, or unclear feature relationships.

This is now a strict routing rule, not a suggestion. For brownfield work,
missing planning docs, default boilerplate docs, stale `/docs/development/`,
template-only ledgers, or undocumented code reality all count as reconcile
blockers. `/develop`, `/quick_fix`, and implementation-oriented skills must
pause and reconcile first unless the operator explicitly overrides that risk.

The same gate now explicitly covers additional entry points:

- `/refactor-planning` must stop and route to `/doc_reconcile` before any
  brownfield refactor plan that would lead to material code edits when docs are
  missing, boilerplate-only, stale, or non-substantive.
- `/quick_fix` is only a valid bypass on a doc-ready project. Behavior-changing
  fixes on unreconciled brownfield code must fail closed into `/doc_reconcile`.
- `/bootstrap` guidance now points operators to `/doc_reconcile` whenever an
  existing project is brownfield and its docs package is not ready.
- CI now fails on source-changing diffs when `docs/development/` is missing and
  also when the required planning package files are missing.

### MCP Provisioning

Bundled MCP server definitions now live in `.agents/mcp/mcp.json`, but they are
also published into project-root `.mcp.json` during `install.sh`, `update.sh`,
`/bootstrap`, and `/init_brain`. This makes project-scoped servers such as
`playwright` available to MCP-compatible clients after setup instead of leaving
the config stranded inside `.agents/`.

---

## ✨ Empirical System Features

- **Semantic RAG Vectoring:** Compresses the cognitive load by 95%. The system parses heuristic tags in a normalized `SKILLS_INDEX`, loading only the specific array of specialized computational frameworks required logically for the exact runtime sequence (e.g., `ada-qa-agent` + `benny-frontend-engineer`).
- **Deterministic Circuit Breaking:** Halts catastrophic infinite-execution edge cases. Any compilation module tracking $N \ge 3$ consecutive failures undergoes hardware-freeze lockouts.
- **Directed Acyclic Graph (DAG) Persistence:** Long-term memory logic overrides temporal dialog sessions by persistently serializing architectural alterations directly into file-system `.agents/brain/` components.
- **CAB Feature Flag Governance:** Introduces strict CI integration limits. AI output must be bounded within LaunchDarkly or equivalent Feature Flags, granting the central Change Advisory Board instantaneous Rollback authority.
- **Granular O11y Tracing:** Instead of flat JSON, the matrix operates a live Prometheus Exporter Daemon (:8000), broadcasting `rag_retrieval_latency_ms{tenant, repo}` to central Grafana arrays.
- **Multi-Level Fault Tolerance:** Ensures workflow resilience by gracefully degrading structural operations from Model Context Protocol (MCP) dependencies to natively embedded `grep`/Markdown functionalities during asynchronous API interruptions.

---

## 📦 Installation Provisioning & Universal Portability (V31.0)

Integrate the matrix framework into any local project directory securely via our automated One-Line cURL Installer.

```bash
# Execute this native pipeline to scaffold the AI cognitive engine
curl -sL https://raw.githubusercontent.com/huudangdev/.agents/main/install.sh | bash
```

### ⚡ The V30.2 Turn-Key Bootstrap
Once the repository is cloned, you must awaken the Cognitive Brain. From your AI chat window, simply command:
> `/bootstrap`
*(Or manually execute `./.agents/bootstrap.sh`)*

This Universal Portability script will:
1. Autonomously spin up Neo4j and ChromaDB Vector clusters via Docker.
2. Synthesize an isolated Python `venv` preventing host pollution.
3. Ingest and Vectorize your entire codebase for O(1) Semantic RAG retrieval.
4. Ignite the Next.js `trustgraph-viewer` automatically.

### 🔄 Upgrading Existing Environments (OTA Sync)

For teams running older versions of the Engine that do not yet have the `/update_brain` slash command integrated, execute the physical **Non-Destructive Update Protocol** directly in your terminal. This specifically protects your `.agents/agents.md` local state file while updating the system schemas around it:

```bash
# Safely pull the newest Intelligence updates directly over your existing local repository.
curl -sL https://raw.githubusercontent.com/huudangdev/.agents/main/update.sh | bash
```

> ⚠️ **CRITICAL DEPENDENCY:** Read the [ROUTING & OPERATIONAL MANUAL](./USAGE_GUIDE.md) to understand multi-agent parallel dispatch paradigms before transmitting commands.

---

## 🚀 Execution Commands (Macro Routing)

Command execution is handled algorithmically via direct prompts.

### 1. `/init_brain` (Global Ignition & Context Alignment)
**MANDATORY for cold-start environments.** This is the crucial bootstrap sequence for the Antigravity OS. Relying on an uninitialized LLM context window causes hallucination. When executed, the engine autonomously runs through absolute initialization stages:
1. **Hardware Ignition:** It executes a background script to boot the TrustGraph local database cluster (Neo4j, Chroma, Postgres) via Docker Compose, bridging local memory with semantic vector spaces.
2. **Lexical Binding:** It forces the AI to ingest the `.clinerules` protocol, enforcing all architectural boundaries and syntax limitations natively.
3. **Skill Indexing:** It parses the `SKILLS_INDEX.md` dictionary to prepare the O(1) semantic routing table for agent selection.
The AI is computationally restricted from generating code until this node returns a green success status.

### 2. `/planning` (Architecture & Requirements: Phase 1)
**The Matrix Genesis (Left-Brain Logic).** Triggers Phase 1 of the Software Development Life Cycle (SDLC). The system delegates control to Systems Architects, PM Agents, research critics, and synthesis agents.
1. **Deep Research Map-Reduce:** Splits discovery into product, security, architecture, data, operations, UX, and risk lanes with source and evidence ledgers.
2. **Legacy Output Preservation:** Still outputs the approved `/docs` set: `prd.md`, `tasks.md`, `knowledge.md`, `decisions.md`, `memory.md`, `planning/flows.md`, `planning/screens.md`, and `planning/diagrams.md`.
3. **Evidence Ledger Upgrade:** Adds `/docs/research/sources.jsonl`, `evidence.jsonl`, `claims.jsonl`, `contradictions.md`, and `research_manifest.json` for traceable claims.
4. **UML Cartography:** Uses Mermaid/Draw.io-ready diagrams for architecture, data flow, state flow, rollback/CAB path, and observability signals.
5. **Validation Gates:** Runs `.agents/scripts/validate_planning_research.py` when research ledgers exist and `.agents/scripts/validate_specs.py` when a feature workspace is attached.
**Execution Halt:** Code writing operations are securely locked. The System presents the `/docs` payload to the human operator for explicit architectural approval.

### 3. `/design` (UI/UX Aesthetic Tokenization: Phase 2)
**The Visual Blueprint (Right-Brain Creativity).** Initiates Phase 2 to prevent token-exhaustion bridging backend logic and aesthetic layout.
1. **Ingestion:** Reads the Screen Maps from the `/planning` sequence.
2. **Variable Formulation:** Orchestrates UI/UX specialists (`@maya-ui-ux-designer`, `@aris-designer`) to define specific Figma-equivalent Hex Color Arrays, CSS variables, and padding grids.
3. **Physical Constraints:** Enforces absolute geometry (4px/8px layout rhythms, Golden Ratio typography scaling).
4. **Interactive States:** Defines Framer Motion spring properties, hover mechanics, and Skeleton loaders.
**Execution Halt:** Yields the `BRAND_GUIDELINES.md` to the user. Iterative prompt tweaks to colors and fonts happen here without reloading the entire SDD architecture.

### 4. `/develop` (The Software Factory Execution: Phase 3)
**Deterministic Code Generation & Testing.** The engine executes a sequential factory protocol, consuming `/docs` schemas to construct the physical environment.
1. **Targeting (Cross-Platform Contextualization):** Intelligently probes root-level manifestations (`package.json`, `pubspec.yaml`, `Podfile`) to pivot its underlying toolchain (Next.js, Flutter, iOS Native, etc.).
2. **TDD Scaffolding:** Writes the Test Suites *first* based on Edge Cases documented in the PRD.
3. **Component Interpolation:** Melds the PRD logic schemas and the UI/UX `BRAND_GUIDELINES.md` to output the component files into the active workspace.
4. **Development Knowledge Ledger:** Creates or updates `/docs/development/` notes per epic, module, feature, page, and task before material code edits.
5. **Continuous Documentation Sync:** After each material code slice, creates `/docs/development/sync/*.md` and patches affected planning/development docs without wholesale replacement.
6. **Adversarial QA (Self-Healing Loop):** Boots the appropriate background daemon (`npm run dev`, `flutter run`, Xcode simulator) via Playwright or native XCTest. It runs rigorous automated tests. If a 500 Server Error or Hydration mismatch occurs, it analyzes the terminal stream, patches the bug autonomously, and restarts the check until compile outputs yield Green `[OK]`.

### 5. `/doc_reconcile` (Brownfield Docs Reconciliation)
**Product-grade documentation recovery.** Reviews the whole codebase, audits
existing docs, migrates or enriches `/docs/development` into V31.1 epic-first
structure, creates one `issues.md` per epic, labels feature relationships, and
updates global planning docs based on actual implementation. Use before
continuing `/develop` on in-progress projects. This is the mandatory route when
brownfield code has missing planning docs, boilerplate-only docs, absent or
template-only `docs/development/`, or implementation reality that is not yet
captured by the PM documentation package.

### 6. `/refactor-planning` (Spaghetti Code Decoupling)
**The Surgical Cleanse for Brownfield Architectures.** Designed specifically to decrease Cyclomatic Complexity in legacy codebases. It executes a 5-Stage deterministic loop to guarantee runtime safety:
1. **Persona Retrieval:** Queries the local GraphRAG database to inherit the user's historical coding patterns and avoid previous anti-patterns.
2. **Brownfield Readiness Gate:** Checks the project docs package before refactor planning. If the planning package is missing, `README.md` is still boilerplate, or `docs/development/` is absent or non-substantive, this flow must stop and route to `/doc_reconcile`.
3. **AST Parsing:** Triggers `npx understand-anything` to mathematically extract an N-dimensional Knowledge Graph mapping API dependencies, missing exports, and prop-drilling depth.
4. **Cyclomatic Reduction:** Detects monolithic modules (e.g., >300 LOC) and algorithmically decouples them following Feature-Sliced Design (FSD)—flattening states and enforcing `eslint --fix` or typing constraints.
5. **Adversarial QA Simulation:** Spins up the Localhost Dev Server to execute endpoint validations or headless UI tests. Compiles the refactored code and applies self-healing try-catch algorithms if the refactor fractured the structural integrity.
6. **State Syncing:** Commits the refactoring success directly into the Neo4j TrustGraph to orient future agents.

### 7. `/quick_fix` (Micro-Mutation Bypass)
**Instantaneous Hotfix Protocol.** Bypasses the monolithic 3-Phase SDLC pipeline entirely only for truly localized work on a doc-ready project. Designed exclusively to execute granular logic tweaks (e.g., fixing a misaligned margin, swapping a deprecated parameter, tracing a discrete stack trace exception) with O(1) latency. Overall cognitive overhead targets execution under 240 seconds by binding exactly one active agent context. If a brownfield project is missing its planning package, relies on boilerplate docs, or lacks a substantive `docs/development/` ledger, `/quick_fix` must stop and route to `/doc_reconcile`. Behavior-changing hotfixes that remain in `/quick_fix` still create a `/docs/development/sync/*.md` note and run `validate_doc_sync.py` so PM documentation does not drift.

### 8. `/mobile_init` & `/marcus_init` (Ecosystem Bootstrapping)
**Native & Web Scaffolding Vectors.** Physical boilerplate constructors. 
- `/marcus_init` acts as the Web Genesis point, establishing baseline structural integrity for Next.js systems and injecting the `.clinerules` intelligence protocol into empty workspaces.
- `/mobile_init` initiates mobile doctrine, enforcing cross-platform physics (React Native/Flutter component boundaries, iOS Safe-Area adherence, mobile viewport limitations) to prepare the ground for the Planning phase.
- After `/bootstrap` on an existing brownfield project, the next command is not
  automatically `/planning` or `/refactor-planning`. If docs are missing,
  boilerplate-only, or stale, operators should route to `/doc_reconcile` first.

### 9. `/update_brain` (OTA Intelligence Upgrade)
**Non-Destructive Neural Sync.** Executes a physical `/update.sh` script to pull the latest Antigravity schemas from the remote `main` branch. Crucially, it uses differential `rsync` logic to overwrite and upgrade system prompts and agent capabilities *without* destroying the local project's `.agents/agents.md` memory matrix or TrustGraph database.
> **SOP MANDATE:** It is strictly required to follow this command natively with `/init_brain`. This performs a "Soft Reboot" to purge the LLM's stale context, load the newly downloaded `.clinerules`, and re-ignite the TrustGraph stack.

---

## 🔬 Repository Architecture

```text
.agents/
├── README.md                      # Foundational system topology
├── USAGE_GUIDE.md                 # Heuristic routing and dispatch instructions
├── V30.0_RELEASE_NOTES.md         # Current governance and planning changelog
├── .clinerules                    # Foundational Constitution Protocol (FSM Limits)
├── trustgraph.env.example         # Shared Neo4j/Chroma runtime config template
├── install.sh                     # Directory genesis installer
├── update.sh                      # OTA non-destructive Rsync patcher
├── memory/                        # Constitution and durable governance
│   └── constitution.md
├── templates/                     # Spec-driven feature templates
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── tasks-template.md
│   ├── development-*-template.*
│   └── planning-*-template.*
├── scripts/                       # Local creation and validation tools
│   ├── create_feature_spec.py
│   ├── audit_development_docs.py
│   ├── create_development_docs.py
│   ├── create_doc_sync_note.py
│   ├── validate_specs.py
│   ├── validate_development_docs.py
│   ├── validate_doc_sync.py
│   └── validate_planning_research.py
├── specs/                         # Feature-scoped source-of-truth artifacts
├── mcp/                           # Model Context Protocol constraints
├── workflows/                     # Declarative Workflow subroutines
│   ├── init_brain.md 
│   ├── marcus_specify.md
│   ├── marcus_clarify.md
│   ├── marcus_plan.md
│   ├── marcus_tasks.md
│   ├── marcus_verify.md
│   ├── planning.md
│   ├── design.md
│   ├── develop.md
│   ├── refactor-planning.md
│   ├── update_brain.md
│   └── quick_fix.md
├── trustgraph-viewer/
│   ├── app/api/health/route.ts    # Runtime health endpoint
│   ├── app/api/chroma/route.ts    # Shell-safe Chroma search bridge
│   ├── components/RuntimeStatus.tsx
│   └── lib/trustgraphConfig.ts    # Shared config reader
└── skills/                        # 64-Agent Cognitive Swarm Directory
    ├── SKILLS_INDEX.md            # Auto-compiled Semantic Pre-Index
    ├── ada-qa-agent/
    ├── david-systems-architect/
    └── benny-frontend-engineer/
```

---

## 🤝 Academic Contributions & Bug Reports

We rigorously welcome computational engineers focusing on Agentic Software AI, Semantic Routing, and Autonomous Testing.

1. **Bug Reports & Issues:** Encountering a runtime timeout or hallucination loophole? Please submit an [Issue Report](https://github.com/huudangdev/.agents/issues) detailing the LLM prompt, Context configuration, and local trace logs.
2. **Injecting New Entities:** When contributing a new Agent (Skill folder), name it identically to `{name}-{computational-role}` format. Provide your YAML Frontmatter, execute `tmp_skills.py` to regenerate the knowledge bank, and push the PR for internal network review.

---

## ☕ Sponsorship & Support

Engineering and maintaining an Advanced Distributed Agent Matrix takes prodigious computational hours and intensive R&D iterations. If this architectural framework has accelerated your enterprise, consider supporting our ongoing development:

[![Buy Me A Coffee](https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-yellow.svg?style=for-the-badge&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/huudangdev)  
[![GitHub Sponsors](https://img.shields.io/badge/Support-GitHub%20Sponsors-ea4aaa.svg?style=for-the-badge&logo=github)](https://github.com/sponsors/huudangdev)

---

## 📄 Licensing Status

Distributed unconditionally under the **MIT License**. Permissible for rigorous corporate modification, academic dissection, and commercial orchestration.
