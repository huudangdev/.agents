---
description: Marcus Fleet Enterprise SDLC Phase 2 (Aesthetic, UI/UX, & Brand Guidelines)
---

# 🎨 DESIGN & AESTHETIC MATRIX (PHASE 2)

> **CORE ARCHITECTURE MANDATE:**  
> This operational protocol governs exclusively the Qualitative, Aesthetic, and UI/UX phase of the Software Development Life Cycle (SDLC). To prevent output-token exhaustion and systemic "AI Hallucinations," you are FORBIDDEN from generating source code or Backend architecture here. Your sole objective is to ingest the PRD/Screen Maps and output precise, pixel-perfect design constraints, Brand Guidelines, and CSS tokens.

// turbo-all

---

## ⬛ SYSTEMIC MEMORY & STATE INHERITANCE (ANTI-AMNESIA PROTOCOLS)

<state_propagation_boundary>
**DOGMATIC STATE PROPAGATION:** The Design sequence is physically incapable of initiating unless the output of the `/planning` phase (specifically `/docs/prd.md`, `/docs/planning/screens.md`, and `/docs/planning/flows.md`) has been dynamically read and ingested into the LLM context buffer. Focus intensely on exactly what screens and user flows are required.
</state_propagation_boundary>

---

## 🔲 DAG TOPOLOGY: CHRONOLOGICAL EXECUTION NODES (PHASE 2)

### 🔵 NODE 0: LOCALHOST ISOLATION & DATA INGESTION
*🔗 Input Vector:* root `agents.md` (fallback: legacy `.agents/agents.md` shim), `/docs/planning/screens.md`
**[Execution Protocol]:**
1. Run `python3 .agents/scripts/validate_design_readiness.py --root .`
2. Execute `python3 .agents/adapters/trustgraph_query.py --task "Design Phase Boot"`.
3. Read the PRD screen maps. Absorb the macro-context of the interface.

### 🟣 NODE 1: DIGITAL AESTHETIC BASELINE & BRAND ESSENCE
*🔗 Input Vector:* Macro-context from Node 0.
*🧠 Injected Tensors:* `maya-ui-ux-designer`, `aris-designer`, `design-system-rules`, `mobile-design-doctrine` (if mobile)
*📦 Emitted Artifacts:* `/docs/BRAND_GUIDELINES.md`
**[Execution Protocol]:**
1. Formulate Figma-equivalent Variable Mappings.
2. Define Typography Scalar Rules (Base 16px, Golden Ratio, Header hierarchies).
3. Generate high-contrast, mathematically accessible Color Palettes (Primary, Accent, Background, Surface, Semantic feedback).
4. Establish absolute spatial rhythm constraints (4px/8px grid systems, Border Radius constants).
5. Output the structural and definitive `BRAND_GUIDELINES.md` document inside `/docs`.

### 🟤 NODE 2: COMPONENT STATE & MICRO-INTERACTION DECLARATION
*🔗 Input Vector:* `/docs/BRAND_GUIDELINES.md`
*🧠 Injected Tensors:* `bella-frontend-animator`
*📦 Emitted Artifacts:* `/docs/UI_COMPONENTS_STATE.md`
**[Execution Protocol]:** Define the interactive physics of the system. Detail Hover states, Focus rings, Loading Skeleton layouts, and Framer Motion / Spring transitions for state changes. Document these behaviors explicitly so the frontend engineers have a deterministic rendering roadmap.

### 🟢 NODE 2.5: DESIGN OUTPUT GATE
*🔗 Input Vector:* `/docs/BRAND_GUIDELINES.md`, `/docs/UI_COMPONENTS_STATE.md`
**[Execution Protocol]:**
1. Run `python3 .agents/scripts/validate_design_outputs.py --root .`
2. Run `python3 .agents/scripts/run_required_docs_gates.py --root . --mode auto`
3. If validation fails, repair the missing, empty, or template-only design artifacts before
   presenting the phase for human review.

---

## 🛑 POINT OF NO RETURN: THE HUMAN OVERSIGHT HALT

> **[HALT COMMAND INITIATED]**
> You have reached the termination of the Phase 2 DAG Sequence. You are strictly prohibited from proceeding to source code generation.
> **ACTION REQUIRED:** Present the output files (`BRAND_GUIDELINES.md` and `UI_COMPONENTS_STATE.md`) to the Human Operator. Ask them to verify the colors, layout constraints, and overall aesthetic vision. They are expected to iteratively update these files until perfectly satisfied. Instruct them to invoke `/develop` ONLY WHEN the Design System is absolutely finalized.
