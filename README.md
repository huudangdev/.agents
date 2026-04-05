<div align="center">
  <h1>🚀 Marcus Fleet Enterprise Matrix (.agents)</h1>
  <p><strong>The Academic Distributed AGI Core for Feature-Sliced Design, Semantic RAG Routing, and Deterministic Autonomous DevOps.</strong></p>

  ![Version](https://img.shields.io/badge/epoch-v29.4-blue.svg?style=for-the-badge)
  ![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)
  ![Routing](https://img.shields.io/badge/routing-Semantic%20RAG-orange.svg?style=for-the-badge)
  ![Governance](https://img.shields.io/badge/governance-SOC2%20CAB-purple.svg?style=for-the-badge)

  <p>
    <a href="#theoretical-overview">Overview</a> •
    <a href="#system-architecture">Architecture</a> •
    <a href="#installation-provisioning">Provisioning</a> •
    <a href="#execution-commands">Execution</a> •
    <a href="#academic-contributions">Contributions</a> •
    <a href="#sponsorship--support">Support/Donate</a>
  </p>
</div>

---

## 🔬 Enterprise Overview (V29.4)

The **Marcus Fleet Enterprise Matrix** represents a paradigm shift in Large Language Model (LLM) orchestration frameworks explicitly built for Enterprise Mono-repos. Distancing itself from monolithic unstructured chat, **Version 29.4** operates as an intelligent computational core bridging **Git-Hook Incremental RAG**, **Ephemeral Sandboxed Execution**, and **OpenTelemetry CI pipelines**.

By binding Agents to rigorous Finite State Machines (FSM) and forcing OS interactions through secure Ephemeral Sandboxes, the Antigravity ecosystem mitigates catastrophic automated failures, token exhaustion, and context window atrophy in codebases exceeding 1 million lines.

### The Bounded Stochastic Execution (Air-Gapped Sandbox & Multi-Tenant IAM)
The core system enforces absolute execution guardrails. No LLM interfacing with the `.agents` ecosystem possesses authorization to run destructive CLI instructions arbitrarily. The matrix is strictly compelled to funnel all bash generation through the `.agents/run_sandboxed.sh` wrapper, validating regex bounds, executing in temporary containerized arrays, and observing exit states to trigger OpenTelemetry Audit logs. Furthermore, all physical architecture alterations are gated by `.agents/iam_verify.sh` to enforce **Multi-Tenant Identity** isolation and CAB Role-Based Access Control (RBAC).

---

## 🏛️ System Architecture Topology

The following C4-styled data-flow layout outlines the cognitive processing, lexical retrieval routing, and execution mechanisms.

```mermaid
graph TD
    subgraph "Human Operator Context"
        U([User Entity]) -->|Stochastic Heuristic Requests| OS{Antigravity Dispatcher}
    end
    
    subgraph "Semantic Retrieval Matrix"
        OS -->|Regex / Keyword Scanning| Index[(SKILLS_INDEX Dictionary)]
        Index -->|N-Dimensional Selection| Router[Agent Routing Algorithm]
    end
    
    subgraph "Cognitive Attention Layer"
        Router -->|Lazy-load Context - Top-K Nodes| Context[LLM Context Window]
        Context <-->|Chronological File Append| LocalMemory[(.brain Local State Memory)]
    end
    
    subgraph "Execution Automata - Sandboxed IO"
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

    subgraph TrustGraph GoT Data Pipeline
        Agent[Agent Workflow] -->|adapter/trustgraph_write.py| Adapter[Graph Adapter]
        Adapter -->|Stores score & reasoning| Neo4j[(Neo4j Vector DB)]
        Neo4j --> Engine[Three.js Graph Engine]
    end

    subgraph 3D Rendering (Graph Ontology V2)
        R1((Run_Task)):::Run
        M1[Module.ts]:::Module
        S1{rag-architect}:::Skill

        R1 -- "[:OPTIMIZED] score: 0.95" --> M1
        R1 -- "[:CAUSED_ERROR] score: 0.4" --> M1
        R1 -- "[:LEVERAGED]" --> S1
    end
```

---

## ✨ Empirical System Features

- **Semantic RAG Vectoring:** Compresses the cognitive load by 95%. The system parses heuristic tags in a normalized `SKILLS_INDEX`, loading only the specific array of specialized computational frameworks required logically for the exact runtime sequence (e.g., `ada-qa-agent` + `benny-frontend-engineer`).
- **Deterministic Circuit Breaking:** Halts catastrophic infinite-execution edge cases. Any compilation module tracking $N \ge 3$ consecutive failures undergoes hardware-freeze lockouts.
- **Directed Acyclic Graph (DAG) Persistence:** Long-term memory logic overrides temporal dialog sessions by persistently serializing architectural alterations directly into file-system `.agents/brain/` components.
- **CAB Feature Flag Governance:** Introduces strict CI integration limits. AI output must be bounded within LaunchDarkly or equivalent Feature Flags, granting the central Change Advisory Board instantaneous Rollback authority.
- **Granular O11y Tracing:** Instead of flat JSON, the matrix operates a live Prometheus Exporter Daemon (:8000), broadcasting `rag_retrieval_latency_ms{tenant, repo}` to central Grafana arrays.
- **Multi-Level Fault Tolerance:** Ensures workflow resilience by gracefully degrading structural operations from Model Context Protocol (MCP) dependencies to natively embedded `grep`/Markdown functionalities during asynchronous API interruptions.

---

## 📦 Installation Provisioning & Universal Portability (V29.3)

Integrate the matrix framework into any local project directory securely via our automated One-Line cURL Installer.

```bash
# Execute this native pipeline to scaffold the AI cognitive engine
curl -sL https://raw.githubusercontent.com/huudangdev/.agents/main/install.sh | bash
```

### ⚡ The V29.3 Turn-Key Bootstrap
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
**The Matrix Genesis (Left-Brain Logic).** Triggers Phase 1 of the Software Development Life Cycle (SDLC). The system delegates control to pure Systems Architects and PM Agents (e.g., `@david-systems-architect`, `@sophia-product-manager`).
1. **Domain Research:** Explores edge cases and business complexities.
2. **Mega Synthesis:** Outputs the 6 Core Root Files directly into `/docs/` (e.g. `prd.md`, `tasks.md`, `knowledge.md`, etc.).
3. **UML Cartography:** Operates the `mermaid-cli` bin to mechanically map Database Entity-Relationship diagrams and system maps (`/docs/planning/diagrams.md`).
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
4. **Adversarial QA (Self-Healing Loop):** Boots the appropriate background daemon (`npm run dev`, `flutter run`, Xcode simulator) via Playwright or native XCTest. It runs rigorous automated tests. If a 500 Server Error or Hydration mismatch occurs, it analyzes the terminal stream, patches the bug autonomously, and restarts the check until compile outputs yield Green `[OK]`.

### 5. `/refactor-planning` (Spaghetti Code Decoupling)
**The Surgical Cleanse for Brownfield Architectures.** Designed specifically to decrease Cyclomatic Complexity in legacy codebases. It executes a 5-Stage deterministic loop to guarantee runtime safety:
1. **Persona Retrieval:** Queries the local GraphRAG database to inherit the user's historical coding patterns and avoid previous anti-patterns.
2. **AST Parsing:** Triggers `npx understand-anything` to mathematically extract an N-dimensional Knowledge Graph mapping API dependencies, missing exports, and prop-drilling depth.
3. **Cyclomatic Reduction:** Detects monolithic modules (e.g., >300 LOC) and algorithmically decouples them following Feature-Sliced Design (FSD)—flattening states and enforcing `eslint --fix` or typing constraints.
4. **Adversarial QA Simulation:** Spins up the Localhost Dev Server to execute endpoint validations or headless UI tests. Compiles the refactored code and applies self-healing try-catch algorithms if the refactor fractured the structural integrity.
5. **State Syncing:** Commits the refactoring success directly into the Neo4j TrustGraph to orient future agents.

### 6. `/quick_fix` (Micro-Mutation Bypass)
**Instantaneous Hotfix Protocol.** Bypasses the monolithic 3-Phase SDLC pipeline entirely. Designed exclusively to execute granular logic tweaks (e.g., fixing a misaligned margin, swapping a deprecated parameter, tracing a discrete stack trace exception) with O(1) latency. Overall cognitive overhead targets execution under 240 seconds by binding exactly one active agent context.

### 7. `/mobile_init` & `/marcus_init` (Ecosystem Bootstrapping)
**Native & Web Scaffolding Vectors.** Physical boilerplate constructors. 
- `/marcus_init` acts as the Web Genesis point, establishing baseline structural integrity for Next.js systems and injecting the `.clinerules` intelligence protocol into empty workspaces.
- `/mobile_init` initiates mobile doctrine, enforcing cross-platform physics (React Native/Flutter component boundaries, iOS Safe-Area adherence, mobile viewport limitations) to prepare the ground for the Planning phase.

### 8. `/update_brain` (OTA Intelligence Upgrade)
**Non-Destructive Neural Sync.** Executes a physical `/update.sh` script to pull the latest Antigravity schemas from the remote `main` branch. Crucially, it uses differential `rsync` logic to overwrite and upgrade system prompts and agent capabilities *without* destroying the local project's `.agents/agents.md` memory matrix or TrustGraph database.
> **SOP MANDATE:** It is strictly required to follow this command natively with `/init_brain`. This performs a "Soft Reboot" to purge the LLM's stale context, load the newly downloaded `.clinerules`, and re-ignite the TrustGraph stack.

---

## 🔬 Repository Architecture

```text
.agents/
├── README.md                      # Foundational system topology
├── USAGE_GUIDE.md                 # Heuristic routing and dispatch instructions
├── V29.2_RELEASE_NOTES.md         # Advanced academic paper / changelogs
├── .clinerules                    # Foundational Constitution Protocol (FSM Limits)
├── install.sh                     # Directory genesis installer
├── update.sh                      # OTA non-destructive Rsync patcher
├── mcp/                           # Model Context Protocol constraints
├── workflows/                     # Declarative Workflow subroutines
│   ├── init_brain.md 
│   ├── planning.md
│   ├── design.md
│   ├── develop.md
│   ├── refactor-planning.md
│   ├── update_brain.md
│   └── quick_fix.md
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
