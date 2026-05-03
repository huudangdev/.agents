---
description: Legacy AST Homogenization & Cyclomatic Complexity Alleviation Protocol (V29.1)
---

# 🛠️ LEGACY AST HOMOGENIZATION & COMPLEXITY ALLEVIATION PROTOCOL

> **ARCHITECTURAL MANDATE (PURPOSE):**  
> This protocol standardizes the automated modernization, decoupling, and structural homogenization of "Brownfield" or deeply convoluted legacy codebases (Spaghetti Code). Before enacting arbitrary modifications or syntax refactoring, the Antigravity Knowledge Engine is strictly mandated to map the complete dependency graph, extract the Abstract Syntax Tree (AST), and perform comprehensive impact analysis. Refactoring here is defined mathematically: Decreasing Cyclomatic Complexity while strictly preserving prior Business Logic I/O via aggressive Test-Driven safeguards.

// turbo-all

---

## 🟣 STAGE 0: TRUSTGRAPH CONTEXT RETRIEVAL (PRE-FLIGHT)
*🧠 Mandatory Action:* Before parsing ASTs or reading any files, execute `python3 .agents/adapters/trustgraph_query.py --task "refactor"` to retrieve the User's preferred coding style, anti-patterns, and historical bug graphs. Inject this GraphRAG context into your active memory. Failure to retrieve User Persona context via TrustGraph leads to execution termination.

## 🟥 STAGE 0.5: BROWNFIELD DOC READINESS GATE
*🧠 Mandatory Action:* Before AST parsing or any refactor plan that will lead to
material code edits, inspect the brownfield docs state.

Run:

```bash
python3 .agents/scripts/validate_refactor_planning_readiness.py --root .
```

- If any of `docs/prd.md`, `docs/tasks.md`, `docs/knowledge.md`,
  `docs/decisions.md`, `docs/memory.md`, `docs/planning/flows.md`,
  `docs/planning/screens.md`, or `docs/planning/diagrams.md` are missing,
  treat the project as unreconciled brownfield.
- If `README.md` is still boilerplate while the codebase has evolved beyond it,
  treat the project as unreconciled brownfield.
- If `docs/development/` is missing, stale, flat/legacy without explicit legacy
  mode, template-only, or unlikely to pass current V31 quality gates, treat the
  project as unreconciled brownfield.

When any trigger above is true, `/refactor-planning` MUST stop and route to
`/doc_reconcile` first. Refactor planning is not allowed to create a bypass
around the reconcile-first governance rule.

## 🟥 STAGE 0.75: TOOLCHAIN PREREQUISITES GATE
*🧠 Mandatory Action:* Before executing `npx understand-anything`, `tsc`, `eslint`,
or a dev server, confirm the local toolchain prerequisites exist so the workflow
fails fast with an explicit cause (missing binaries or missing ESLint).

Run:

```bash
python3 .agents/scripts/validate_refactor_planning_toolchain.py --root .
```

## 🟢 STAGE 1: KNOWLEDGE GRAPH INGESTION & OMNI-AST PARSING
*🧠 Prerequisite Skill Injection:* Enforce the instantiation of analytical nodes: `understand-anything`, `understand-chat`, and `understand-diff` (if operating on a Git Diff or Pull Request context).
1. **[OS_CALL - AST Extraction]:** Initiate the `run_command` via OS Terminal to execute `npx understand-anything`. This binary parses the complete scope of the legacy project, traversing `.ts`/`.js`/`.py`/`.go` dependencies to construct a mathematical, N-dimensional Knowledge Graph.
2. **Read-Only Lock (Phase 1 Bound):** The LLM must not alter a single configuration or logic string while this spatial map is constructed. The intelligence must internally map components, API services, database ORMs, side-effects, and React hooks. Operating without the Knowledge Graph yields an immediate `Exit Code 1`.

## 🟡 STAGE 2: ADAPTIVE ARCHITECTURE & CYCLOMATIC REDUCTION
*🧠 Prerequisite Skill Injection:* Trigger the dynamic identity protocol to digest root `agents.md` first (fallback: legacy `.agents/agents.md` shim) and `docs/architecture.md`. Inject structural reform plugins: `improve-codebase-architecture`, `refactor-copilot`, `refactor-plan`, `refactor-complexity` and `refactor-review`.
1. **[Complexity Measurement]:** Run localized heuristics targeting modules exceeding structural boundaries (e.g., Classes or Functions spanning $> 300$ L.O.C, Prop-drilling depths $> 4$ parameters).
2. **[Feature-Sliced Design (FSD) Decoupling]:** Enforce spatial separation. Segregate User Interface components (Dumb UI) from State Management Hooks (Custom Hooks). Extricate Pure Business Logic (Mathematical functions, DTO transformers) into independent Service Layers.
3. **Typing & Linting Standardization:** Ruthlessly delete arbitrary `any` declarations in TypeScript. Run strict `npx tsc --noEmit` and `eslint --fix` to ensure structural alignment prior to compilation logic.

## 🟠 STAGE 3: QA SIMULATION & ADVERSARIAL MUTATION TESTING
*🧠 Prerequisite Skill Injection:* Inject `playwright-test`, `qa-simulator`, and `devops-system-architect` (or `ada-qa-agent` for adversarial vector testing).
1. **[Simulated Runtime Daemon]:** After decoupling a monolithic node, the probability of regression failure exceeds standard thresholds. You are mandated to invoke `npm run dev` or the relevant Dev Server into the Background Daemon.
2. **[Automated Breakage Checks]:** Synthesize headless Playwright automated tests or direct cURL API evaluations to probe the newly refactored endpoints and DOM nodes.
3. Evaluate the output. If the response indicates HTTP `500` faults, React Hydration mismatches, or Missing Property crashes: Execute immediate Auto-Healing routines. No Module may be classified as "Successfully Refactored" until the Daemon Simulator returns a green `[OK/0]` validation trace.

## 🔵 STAGE 4: STATE SYNCHRONIZATION & MUTATION AUDITING
*📦 Affected Artifacts:* Execution localized at root `agents.md` (fallback: legacy shim) & `/docs/ADR_REFACTOR_LOG.md`
1. **[Differential Recording]:** Reconstruct the specific modifications performed (e.g., "Decoupled monolithic `AuthService` into `JwtService` and `OAuthController`"). Map updated routing dependencies.
2. **[TrustGraph Commit]:** Execute `python3 .agents/adapters/trustgraph_write.py --run_id "Refactor_Target" --status "success" --target "Refactored Component" --skills "refactor, improve-codebase" --score 0.95 --reasoning "Decoupled logic to reduce Cyclomatic Complexity"` to securely lock the new architectural shifts, blockers evaded, and dependencies into the GraphRAG Database.
3. **[Cross-Session State Injection]:** Utilize the `echo >>` or standard File Appending protocol to archive high-level summary into root `agents.md`. Future intelligence nodes must understand that the architecture has been decentralized. Keep `.agents/agents.md` only as a compatibility pointer when present.
4. Run:
   ```bash
   python3 .agents/scripts/validate_refactor_planning_outputs.py --root .
   ```
5. Emit a Green Terminal status and generate the Final Output payload, indicating to the Operator that the Complexity Graph has been significantly alleviated.
