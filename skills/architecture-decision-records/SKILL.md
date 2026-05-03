---
name: architecture-decision-records
description: ADR Management Skill
---

# Directive: Architecture Decision Record Master

> Capture significant technical decisions as durable artifacts that explain why a path was chosen, what alternatives were rejected, and what operational cost or risk was accepted.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Context Preservation:** Capture the *Why* behind engineering decisions, not just the *What*.
2. **Standardization:** Enforce strict ADR templates (e.g., Markdown based, MADR format).
3. **Documentation Governance:** Prefer the local ADR conventions, templates, and validators first. Recommend extra tooling only when it solves a documented gap.

## ⚙️ EXECUTION PIPELINE (THE ADR CYCLE)

### Phase 1: Contextual Interrogation
- Read the root `agents.md`, existing ADRs, and the active feature workspace first.
- You cannot write a valid ADR without understanding the historical constraints and the current change package.
- If the User's request lacks technical motivation (e.g., "Change to MongoDB"), interrogate them aggressively: "What are the latency constraints? Why is relational SQL no longer viable?"

### Phase 2: Capability Escalation
If the repo lacks adequate ADR structure or documentation support:
1. Inspect `.agents/templates/`, `.agents/scripts/`, and current docs patterns first.
2. Propose any new tooling or template addition as an operator-reviewed recommendation.
3. Document what problem it solves and how it affects governance.

### Phase 3: ADR Construction
Emit a strict, physically separated Markdown artifact formatted as follows:
- **Title:** `ADR-[Number]: [Short Name]`
- **Status:** [Proposed | Accepted | Deprecated | Superseded]
- **Context:** The technical / business forces driving the decision.
- **Decision:** The absolute mathematical or architectural choice made.
- **Consequences:** Positive traits, negative debts incurred, and risks accepted.
- **Verification Impact:** What testing, monitoring, or migration obligations the decision creates.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Zero-Downtime Memory
- Link the ADR from the appropriate project memory or docs index using the repo's normal editing workflow.
- If the ADR changes active delivery scope, ensure the feature workspace and execution-readiness gates are updated alongside it.
- **[REPORT]**: Emitted when delivering the final ADR Artifact to the system.
