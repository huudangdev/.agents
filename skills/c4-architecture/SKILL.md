---
name: c4-architecture
description: C4 Architecture Diagramming
---

# Directive: C4 Architecture Modeler

> Use this skill to map system boundaries clearly using C4-style diagrams when a diagram will reduce ambiguity.

## 🎯 MISSION (CORE OBJECTIVES)
1. **System Abstraction Mapping:** Render accurate C4 boundary boxes, relationship arrows, and API vectors.
2. **Mermaid Native CLI Rendering:** Adhere strictly to the physical transformation of `.mmd` files into `.pdf` or `.png` graphs via terminal automation.
3. **Diagram Discipline:** Produce diagrams only when they clarify decisions already grounded in the docs and code.

## ⚙️ EXECUTION PIPELINE (THE DIAGRAM CYCLE)

### Phase 1: Contextual Ingestion
- Read the relevant spec, plan, and architecture notes first.
- Map reality, not an imagined target state.

### Phase 2: Diagram Construction
- Produce one diagram level at a time.
- Include only the modules, services, and boundaries relevant to the active question.
- Recommend extra tooling only if the current repo cannot render or store the needed artifact.

### Phase 3: The C4 Execution String
Construct the physical Diagram payload. **You must strictly obey the following formatting rule:**
- Output raw, pristine `mermaid` code targeting exactly one level of the C4 structure (Level 1: System Context, or Level 2: Container). Do not mix depth levels chaotically.
- Quote node labels containing irregular characters (e.g., `Node["Label (Info)"]`).

### Phase 4: Rendering
- Render locally only if the environment supports it and the artifact is needed.
- If rendering is not available, keep the Mermaid source as the primary deliverable.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Fallback Diagramming
- If the OS environment cannot support Node.js/CLI execution, fallback to generating the raw Mermaid markdown block coupled with an actionable `drawio` MCP data structure.
- **[RENDERED]**: Emitted when a PNG or PDF is physically saved to the local workspace.
