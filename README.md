<div align="center">
  <h1>🚀 Marcus Fleet Enterprise Matrix (.agents)</h1>
  <p><strong>The Academic Distributed AGI Core for Feature-Sliced Design, Semantic RAG Routing, and Deterministic Autonomous DevOps.</strong></p>

  ![Version](https://img.shields.io/badge/epoch-v29.1.5-blue.svg?style=for-the-badge)
  ![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)
  ![Routing](https://img.shields.io/badge/routing-Semantic%20RAG-orange.svg?style=for-the-badge)
  ![Automata](https://img.shields.io/badge/automata-Finite%20State-purple.svg?style=for-the-badge)

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

## 🔬 Theoretical Overview

The **Marcus Fleet Enterprise Matrix** represents a paradigm shift in Large Language Model (LLM) orchestration frameworks. Distancing itself from monolithic static-prompt environments, **Version 29.1** operates as an intelligent computational hive-mind composed of **64 Specialized Elite Agents**.

Through the implementation of **Semantic Retrieval-Augmented Generation (RAG)** and **Finite State Machine (FSM) Failure Limitations**, the Antigravity operating system mitigates critical flaws present in contemporary autonomous systems: context window atrophy, algorithmic hallucination, and runaway API expenditure loops.

### The Zero-Suggestion Doctrine
The core system enforces absolute autonomic determinism. No LLM interfacing with the `.agents` ecosystem possesses authorization to output manual CLI instructions (e.g., "Copy this terminal command"). The matrix is strictly compelled to autonomously instantiate native terminal processes, validate I/O streams, and resolve unit-test failures symmetrically prior to returning Human-In-The-Loop feedback vectors.

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

---

## ✨ Empirical System Features

- **Semantic RAG Vectoring:** Compresses the cognitive load by 95%. The system parses heuristic tags in a normalized `SKILLS_INDEX`, loading only the specific array of specialized computational frameworks required logically for the exact runtime sequence (e.g., `ada-qa-agent` + `benny-frontend-engineer`).
- **Deterministic Circuit Breaking:** Halts catastrophic infinite-execution edge cases. Any compilation module tracking $N \ge 3$ consecutive failures undergoes hardware-freeze lockouts.
- **Directed Acyclic Graph (DAG) Persistence:** Long-term memory logic overrides temporal dialog sessions by persistently serializing architectural alterations directly into file-system `.agents/brain/` components.
- **Multi-Level Fault Tolerance:** Ensures workflow resilience by gracefully degrading structural operations from Model Context Protocol (MCP) dependencies to natively embedded `grep`/Markdown functionalities during asynchronous API interruptions.

---

## 📦 Installation Provisioning

Integrate the matrix framework into any local project directory securely via our automated One-Line cURL Installer.

```bash
# Execute this native pipeline to scaffold the AI cognitive engine
curl -sL https://raw.githubusercontent.com/huudangdev/.agents/main/install.sh | bash
```

> ⚠️ **CRITICAL DEPENDENCY:** Read the [ROUTING & OPERATIONAL MANUAL](./USAGE_GUIDE.md) to understand multi-agent parallel dispatch paradigms before transmitting commands.

---

## 🚀 Execution Commands (Macro Routing)

Command execution is handled algorithmically via direct prompts.

### 1. `/init_brain` (Global Ignition & Context Alignment)
**MANDATORY for cold-start environments.** This command serves as the critical bootstrap sequence. It autonomously boots the local TrustGraph memory stack (Neo4j, Chroma, Postgres) via Docker Compose, loads the global constitution (`.clinerules`), and provisions the `SKILLS_INDEX.md` mapping. The AI is physically prohibited from executing code until this semantic ingestion is complete.

### 2. `/planning` (Architecture & Requirements Phase)
**The Genesis of Software.** Triggers Phase 1 of the SDLC. The AI acts as a pure Systems Architect (Left Brain). It maps Feature-Sliced Architectures, synthesizes complete Product Requirement Documents (PRD), and constructs C4 PlantUML/Mermaid diagrams. Code generation is blocked; the system writes output strictly to `/docs` and triggers a **Hard Halt** for human review.

### 3. `/design` (UI/UX Aesthetic Matrix)
**The Visual Tokenization Phase.** Initiates Phase 2 of the SDLC. The AI acts exclusively as an Art Director (Right Brain). It consumes the PRD and emits strict Figma-equivalent CSS variables, Typography scalar rules (Golden Ratio), Spacing constraints (4px/8px grid), and Brand Color Palettes into `BRAND_GUIDELINES.md`. This prevents token exhaustion by decoupling design logic from backend schemas. Halts for human review.

### 4. `/develop` (Execution & QA Simulation)
**The deterministic Software Factory.** Initiates Phase 3 of the SDLC. A highly rigorous operational flow where the AI merges the Architectural Schemas (`/planning`) and the Design Matrix (`/design`) to physically structure the source code. It features **Cross-Platform Adaptability**—intelligently scanning the root directory to determine the exact execution framework (e.g. Next.js, Go, iOS Swift, Flutter) and launching the corresponding environment (`npm run dev`, `xcodebuild test`, etc.) to execute continuous TDD and Adversarial Playwright/XCTest simulations until all Exit Codes yield Green.

### 5. `/refactor` (Spaghetti Code Decoupling)
**The Surgical Cleanse.** Designed strictly for "Brownfield" or legacy repositories. Before touching any logic, it executes Node commands (e.g. `npx understand-anything`) to extract the full Abstract Syntax Tree (AST) and generate an N-dimensional Knowledge Graph. It then strategically reduces Cyclomatic Complexity (e.g. flattening prop-drilling, decoupling monoliths into FSD), while utilizing aggressive automated testing to self-heal any compilation failures caused by the mutation.

### 6. `/quick_fix` (Micro-Mutation Bypass)
**Instantaneous Hotfix Protocol.** Circumvents all macro-planning pipelines for O(1) latency fixes (e.g. tweaking a CSS variable or catching a rogue null pointer). The cognitive load is minimized to under 240 seconds per execution.

### 7. `/mobile_init` & `/marcus_init` (Ecosystem Bootstrapping)
**Native & Web Scaffolding Vectors.** Physical boilerplate constructors. `/mobile_init` enforces cross-platform mobile doctrines (React Native/Flutter bounds, iOS Safe-Area rules, continuous spring animations). `/marcus_init` establishes the baseline web structure and Antigravity intelligence directory injection.

---

## 🔬 Repository Architecture

```text
.agents/
├── README.md                      # Foundational system topology
├── USAGE_GUIDE.md                 # Heuristic routing and dispatch instructions
├── V29.1_RELEASE_NOTES.md         # Advanced academic paper / changelogs
├── .clinerules                    # Foundational Constitution Protocol (FSM Limits)
├── mcp/                           # Model Context Protocol constraints
├── workflows/                     # Declarative Workflow subroutines
│   ├── init_brain.md 
│   ├── planning.md
│   ├── design.md
│   ├── develop.md
│   ├── refactor.md
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
