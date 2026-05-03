---
name: improve-codebase-architecture
description: Improve Codebase Architect
---

# Directive: Improve Codebase Architecture

> Use this skill for structural cleanup that crosses module boundaries. Prefer migration paths over rewrite fantasies.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Structural De-coupling:** Identify Circular Dependencies (`A imports B, B imports A`) and aggressively amputate them via Interface abstractions or Dependency Injections.
2. **Domain-Driven Design (DDD):** Reorganize legacy MVC (Model-View-Controller) topologies into explicit Feauture-Based Directories (Next.js App Router topology / Layered Domains).
3. **Blast-Radius Discipline:** Structural changes must be justified by real coupling, duplication, or instability.

## ⚙️ EXECUTION PIPELINE (THE BLUEPRINT CYCLE)

### Phase 1: Dependency Tracing
- Read the active feature docs, affected modules, and dependency relationships first.
- Do not restructure a shared module without mapping its callers and contracts.

### Phase 2: Refactor Planning
- Define:
  - target boundaries
  - migration sequence
  - verification commands
  - docs/ADR updates
- Recommend extra tooling only when the existing repo cannot surface the needed dependency evidence.

### Phase 3: The Surgical Overhaul
Declare exactly which files will be Deleted `[DELETE]`, Modified `[MODIFY]`, or Created `[NEW]`.
- **The Circuit Breaker Rule (Build Failure):** The ultimate test of an Architectural Refactor is the compiler. If the OS Terminal `npm run build` or `npm run type-check` throws the corresponding cascade of TypeErrors 3 consecutive times, you have broken the interface boundaries. STOP. Roll back the Git index and raise a 🚩.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Backward Compatibility (The Adapter Pattern)
- Whenever possible, wrap legacy systems in an Adapter Class instead of physically rewriting 10-year-old active production files.
- If the refactor is behavior-changing or multi-module, require execution-readiness validation before implementation starts.
- **[REPORT]**: Emitted upon successfully migrating the File Tree Architecture.
