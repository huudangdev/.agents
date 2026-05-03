# Implementation Plan: Marcus Spec Foundation

> Feature ID: `001-marcus-spec-foundation`
> Spec: `spec.md`
> Constitution: `.agents/memory/constitution.md`

## 1. Technical Summary

Implement the first Marcus Fleet spec-driven foundation as an additive layer
inside `.agents`. This plan creates durable governance and feature-scoped
artifacts while preserving existing workflows and skills.

The implementation is intentionally small and local:

- Markdown constitution and templates.
- Python standard-library scripts for feature creation and validation.
- Workflow docs that map the new lifecycle to Marcus Fleet agents.
- A sample feature folder proving the process works.

## 2. Constitution Gates

- [x] Specification has no unresolved `[NEEDS CLARIFICATION]` markers, or the
      operator accepted the residual risk.
- [x] Contracts are defined before implementation.
- [x] Verification method is named before implementation.
- [x] No shell `eval` or unbounded command execution is introduced.
- [x] No hardcoded production secret is introduced.
- [x] TypeScript changes avoid `any` unless justified in Complexity Tracking.
- [x] Rollback path is documented for user-facing or operational changes.

## 3. Architecture

### 3.1 Current State

- Existing modules: `.agents/workflows`, `.agents/skills`,
  `.agents/adapters`, root `agents.md`.
- Current coupling: workflows depend on global `/docs` artifacts and skill
  routing depends on `SKILLS_INDEX.md`; neither provides feature-scoped
  acceptance criteria.
- Known constraints: preserve current commands and avoid network-dependent
  tooling in this step.

### 3.2 Target State

- New or changed modules:
  - `.agents/memory/constitution.md`
  - `.agents/templates/*.md`
  - `.agents/scripts/create_feature_spec.py`
  - `.agents/scripts/validate_specs.py`
  - `.agents/workflows/marcus_*.md`
  - `.agents/specs/001-marcus-spec-foundation/*`
- Data flow: operator prompt -> feature spec -> plan/contracts -> tasks ->
  implementation evidence -> `agents.md` and TrustGraph.
- Operational flow: agents use legacy workflows for execution but use
  feature-scoped specs as the source of truth for non-trivial work.

### 3.3 Mermaid Diagram

```mermaid
flowchart TD
    Prompt[Operator Prompt] --> Create[create_feature_spec.py]
    Create --> Spec[spec.md]
    Spec --> Clarify[marcus_clarify]
    Clarify --> Plan[plan.md]
    Plan --> Tasks[tasks.md]
    Tasks --> Work[Agent Work]
    Work --> Verify[verification.md]
    Verify --> Memory[agents.md + TrustGraph]
```

## 4. Contracts

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `contracts/spec-workspace.md` | Defines required files and pass/fail gates for a feature workspace. | `david-systems-architect` | All workflow agents |

Contract rules applied in this feature:

- The workspace contract is filesystem-native and must remain readable without a
  service dependency.
- The validator is the compatibility check for the workspace contract.
- Any future expansion must keep numbered feature directories and required file
  names stable unless a migration note is added.

## 5. Data Model

The data model is filesystem-based. Core entities: Constitution, Feature,
SpecArtifact, Task, VerificationEvidence.

Validation and lifecycle notes:

- `Feature` owns one immutable feature id and one mutable documentation package.
- `SpecArtifact` moves from draft to accepted only after validation and review.
- `VerificationEvidence` must be append-only enough to preserve what command was
  run, when it was run, and what residual risk remained.

## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Specification | `sophia-product-manager` | `spec.md` | no unresolved clarifications |
| Architecture | `david-systems-architect` | `plan.md`, `contracts/` | constitution gates |
| Orchestration | `marcus-ai-orchestrator` | `agent-routing.md` | owners and write scopes |
| QA | `ada-qa-agent` | `verification.md` | evidence table |

Execution monitoring:

- Blocking gates before implementation: `spec.md` clarity, contracts present,
  verification plan named, and no placeholder-heavy artifacts in the workspace.
- Evidence checkpoints during implementation: feature creation, validator pass,
  workflow population, and `agents.md` memory update.
- Escalation condition after repeated failure: if validation fails repeatedly
  for the same unresolved artifact without new edits, stop and repair the spec
  package before continuing.

## 7. Migration and Rollback

- Migration steps:
  1. Add constitution, templates, scripts, workflow docs.
  2. Generate first feature workspace.
  3. Validate feature workspace.
  4. Update `agents.md` and TrustGraph memory.
- Rollback steps:
  1. Remove `.agents/memory/constitution.md`.
  2. Remove `.agents/templates/`, `.agents/scripts/`, new `marcus_*.md`
     workflows, and `.agents/specs/001-marcus-spec-foundation/`.
  3. Revert the `agents.md` session entry.
- Compatibility notes: legacy `/planning`, `/design`, `/develop`, and
  `/quick_fix` remain available.

## 8. Complexity Tracking

This section records intentional abstraction or governance tradeoffs rather than
acting as a placeholder for future thinking.

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Add new spec scripts instead of installing upstream Spec Kit CLI | Keep Marcus Fleet self-contained and offline-friendly | Pulling external CLI into the project | Low |

## 9. POC Slice and Review Cadence

- POC slice boundary: create one feature workspace, populate all required docs,
  pass strict validators locally, and prove the workflows can reference the
  package without legacy tool vocabulary.
- Success evidence for the slice: validators pass, workflow docs are updated,
  sample workspace artifacts are concrete, and readiness gate passes.
- What remains intentionally unproven after the slice: full migration of every
  historical skill and live execution against a real application codebase.
- Review cadence:
  - Draft architecture review: after templates and validator contract are
    defined.
  - Challenge review: after workflow docs and routing model are populated.
  - Verification readiness review: after the sample workspace is reconciled to
    the same stricter rules.
- Stop conditions: repeated validator failures without new artifact edits or a
  need to migrate the broader repo to keep this feature valid.
- Proceed conditions: spec package complete, review loop closed, sample feature
  passes both `validate_specs.py` and `validate_execution_readiness.py`.
