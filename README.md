# 🚀 Marcus Fleet Enterprise Matrix (.agents)
**Version:** Antigravity V29.1 - The Dynamic Lazy-Loading Epoch

**The Ultimate AGI Core for Software Architecture, FSD/DDD Coding, Pixel-perfect UI/UX, and Autonomous DevOps.**

This repository contains the most advanced Distributed AI Agent Core. Moving beyond traditional static prompt models, **V29.1** operates as a "Dynamic Sandbox": it seamlessly transitions between macro workflows and micro-tasks, utilizes dynamic RAG (Retrieval-Augmented Generation) for on-the-fly skill configuration, employs a Circuit Breaker system for API budget protection, and orchestrates a matrix of **64 Specialized Elite Agents**.

The system natively operates with 100% autonomy, enforcing Zero-Truncation (full file rewrites) and eliminating the need for users to manually execute CLI instructions.

---

## 🏗️ V29.1 ARCHITECTURAL WORKFLOW

```mermaid
graph TD
    User([Operator / Human]) --> |Inputs Slash Command| AgentCore{Antigravity Core}
    
    subgraph "Federal Brain Matrix (Core Engine)"
    AgentCore --> |1. Lazy-Loading| RAG[🧠 SKILLS_INDEX.md]
    RAG --> |2. Retrieve 5-7 Relevant Skills| Context[LLM Context Window]
    end
    
    subgraph "System Guards & Execution"
    Context --> |3. Autonomous Execution| Code[Code Editor / Terminal]
    Code --> |Limit Exceeded 3x| CircuitBreaker[Circuit Breaker]
    CircuitBreaker -.-> |Human-in-the-Loop required| User
    Context --> |4. Service Unavailable?| Fallback[Native Fallback: Mermaid / Shell Grep]
    end
    
    subgraph "Macro Workflows"
    Context --> W1["/quick_fix"]
    Context --> W2["/auto_software_factory"]
    Context --> W3["/refactor_project"]
    end
```

---

## 🌟 BREAKTHROUGH FEATURES (V29.1)
1. **Semantic RAG Lazy-Loading:** Prevents context window fragmentation and AI hallucination caused by mass-loading 64 skill folders. Antigravity dynamically parses `SKILLS_INDEX.md`, identifies semantic tags (e.g., `[Frontend]`, `[QA]`, `[Architecture]`), and injects only the necessary personas. This reduces initial load times and token consumption by 80%.
2. **The 3-Strike Circuit Breaker:** If an AI agent attempts to fix a build compilation or terminal error and fails 3 consecutive times, the system will **autonomously halt execution** and raise a Red Flag (🚩) requiring human intervention. This entirely eliminates infinite error-loop billing anomalies.
3. **Micro-Brain Local Memory:** The system maintains persistent state preservation. Architectural decisions and bug fixes are continuously logged into `agents.md` and component-level `.brain/` directories, completely bypassing the memory limitations of isolated chat sessions.
4. **Resilient Fallback Protocols:** If external MCP (Model Context Protocol) servers like *Draw.io* or *Understand-Anything* experience downtime, the AI seamlessly degrades to native Markdown Mermaid diagramming and local `grep` shell searches to maintain momentum without throwing fatal errors.

---

## 📦 INSTALLATION
To utilize this AGI core, simply construct a master workspace and clone the `.agents` engine into your project.

```bash
# 1. Create a primary workspace directory
mkdir marcus-workspace && cd marcus-workspace

# 2. Clone the Marcus Fleet AI Core (as a hidden `.agents` directory)
git clone https://github.com/huudangdev/.agents.git .agents

# 3. Open the codebase in your AI IDE (Cursor / Antigravity / OpenClaw) and begin.
```

> **📖 ESSENTIAL READING:** Before initializing development, review the [OPERATING MANUAL (USAGE_GUIDE.md)](./USAGE_GUIDE.md) to comprehend when to utilize Macro Commands (`/commands`) versus Targeted Agent Swarms (`@skills`).

---

## ⚡ CORE SLASH COMMANDS
The system is engineered to mechanically automate developer interactions. Initiate tasks by typing the following commands directly into the AI prompt console:

### 1. 🟢 System Initialization (Required for New Sessions)
> Type: `/init_brain`
- **Objective:** Awakens the 64-Agent Matrix. Ingests the Semantic RAG Index and enforces the overarching `.clinerules` constitution.
- **Usage Context:** **MANDATORY** at the start of any new chat thread or operating session. Prevents Cold Start hallucination.

### 2. 🟡 The Lightweight Bypass: Rapid Bug Fixes
> Type: `/quick_fix`
- **Objective:** Bypasses all heavyweight PRD, UML, and System Design phases. Designed strictly for rapid, localized modifications (e.g., updating UI typography, modifying button states, appending an API field).
- **Process:** AI dynamically retrieves 1 specific agent ➔ Alters the code ➔ Executes Terminal Verification ➔ Records History ➔ Terminates. Average completion: < 4 Minutes.

### 3. 🔴 The Heavyweight Engine: Auto Software Factory
> Type: `/auto_software_factory`
- **Objective:** Scaffolds entirely new enterprise-grade repositories (Monorepos, Web Apps, Backend Systems) or engineers massive Fullstack feature branches.
- **Process (9 Sequential Phases):** 
  Establishes Architecture (FSD/DDD) -> Generates PRDs & Scenarios -> Constructs C4 Diagrams -> Executes TDD Backend -> Synthesizes E2E Playwright Tests -> Migrates Databases. 

### 4. 🔵 Legacy Codebase Modernization (Refactoring)
> Type: `/refactor_project`
- **Objective:** Engineered for deep-cleaning technical debt in brownfield projects.
- **Process:** Strictly mandates the execution of the `npx understand-anything` tool to map a 100% coverage Knowledge Graph of the existing codebase. Audits cyclomatic complexity before applying structural refactoring.

### 5. 🟣 The Mobile Application Framework
> Type: `/mobile_init`
- **Objective:** Delegates full authority to the **Mobile Design Doctrine**.
- **Process:** Enforces React Native / Flutter Boilerplates customized with strict safe-area wrapping, iOS/Tailwind compliance, and touch-responsive spring animations.

---

## 🔒 ZERO SUGGESTION POLICY
Any LLM interfacing with the `.agents` ecosystem is permanently **revoked of its ability to offer manual commands ("Suggestions")**.

The AI is **STRICTLY PROHIBITED** from generating bash code inside markdown blocks and instructing the user to "Copy and paste this into your terminal". It **MUST** utilize native OS terminal tools to type, build, and debug autonomously, returning control to the user only upon successful validation!
