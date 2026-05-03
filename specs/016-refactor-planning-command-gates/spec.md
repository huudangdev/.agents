# Feature Specification: Refactor Planning Command Gates

> Feature ID: `016-refactor-planning-command-gates`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Convert /refactor-planning from mixed shell/workflow into a command with explicit readiness and output validators, while preserving its brownfield governance role.

## 1. Purpose

Harden `/refactor-planning` so a model can no longer treat it as an open-ended
refactor ritual with only narrative guardrails. The existing workflow already
contains two strong contract ideas: it must stop on unreconciled brownfield
docs, and it must leave a durable refactor audit trail. What is missing is the
mechanical gate that proves those conditions before and after the workflow runs.

This feature adds deterministic local validators around `/refactor-planning`.
Before the workflow begins, a readiness gate must confirm that the brownfield
docs package is present and that the development ledger meets the current
quality gate. After the workflow completes, an output gate must confirm the
refactor closeout artifacts exist. The goal is to make this risky command more
enterprise-safe without rewriting its AST, lint, or QA runtime body.

## 2. User Stories

- [x] As an operator, I need `/refactor-planning` to fail closed when brownfield
      docs are unreconciled so that refactor work does not bypass governance.
- [x] As an implementation model, I need `/refactor-planning` to name its
      required entry and exit validators so I can follow the command
      deterministically.
- [x] As a governance maintainer, I need `/refactor-planning` to be part of the
      shared command-surface contract so public docs and workflow markers stay aligned.

## 3. Functional Requirements

- `FR-001`: The system MUST provide a readiness validator for
  `/refactor-planning` that checks the required brownfield planning docs and
  development-ledger quality gate before the command proceeds.
- `FR-002`: The system MUST provide an output validator for
  `/refactor-planning` that checks for `agents.md` and `docs/ADR_REFACTOR_LOG.md`
  before the command is considered complete.
- `FR-003`: The system MUST wire `/refactor-planning` into the public
  slash-command contract so README, `USAGE_GUIDE.md`, registry, and workflow all
  point to the same validator-backed chain.
- `FR-004`: The system MUST preserve `/refactor-planning` as a brownfield
  governance and planning command rather than rewriting the refactor engine itself.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: the new gates must remain local and file-oriented.
- `NFR-002`: Security: no new remote or privileged execution path is added.
- `NFR-003`: Observability: failures must identify the exact missing docs input,
  failed ledger gate, or missing closeout artifact.
- `NFR-004`: Maintainability: the validators should sit beside the existing
  workflow, not replace it with a new orchestrator.
- `NFR-005`: Documentation and traceability: `/refactor-planning` must move
  from mixed shell/workflow status into the script-backed public command surface.

For any item that is intentionally deferred, say so explicitly and record the
accepted risk instead of leaving the field vague.

## 5. Acceptance Criteria

- `AC-001`: Given a project root with the required brownfield planning docs and
  a minimally valid development ledger, when
  `python3 scripts/validate_refactor_planning_readiness.py --root <project-root>`
  runs, then it passes.
- `AC-002`: Given a project root missing a required planning doc or failing the
  development-doc quality gate, when the same validator runs, then it fails and
  names the exact blocking input or gate.
- `AC-003`: Given a project root with non-empty `agents.md` and
  `docs/ADR_REFACTOR_LOG.md`, when
  `python3 scripts/validate_refactor_planning_outputs.py --root <project-root>`
  runs, then it passes.
- `AC-004`: Given `/refactor-planning` is published in README and
  `USAGE_GUIDE.md`, when `python3 scripts/validate_command_surface.py --root .`
  runs, then it confirms the readiness and output validator chain.
- `AC-005`: Given `/refactor-planning` hardening is added, when command-surface
  validation replays, then the broader public command contract still passes.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".

## 6. Clarifications

Record unresolved questions as explicit markers. Planning is blocked while any
marker remains unless the operator accepts the risk.

- No unresolved clarifications remain. Success means `/refactor-planning` has a
  local readiness gate, a local output gate, and public command-surface wiring.

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `workflows/refactor-planning.md`, README,
  `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`,
  `scripts/validate_command_surface.py`, `scripts/validate_development_docs.py`,
  and this feature package.
- Files or modules out of scope: rewriting the AST/refactor engine, executing
  the full refactor toolchain in this feature, or changing downstream app code.
- Compatibility requirements: `/refactor-planning` must stay a brownfield
  planning and governance command.
- Documentation prerequisites already reviewed: current `/refactor-planning`
  workflow, `/doc_reconcile` brownfield requirements, and the hardened public
  command surface from features `013` to `015`.
- Rollback or containment expectations: removing the two validators should
  restore the previous mixed shell/workflow contract without altering the rest
  of the refactor flow.

Out of scope:

- Replacing `npx understand-anything`, lint, typecheck, or QA runtime steps.
- Validating the quality of the actual refactor plan content.
- Adding browser or AST-runtime integration tests for this slice.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| readiness gate is too weak | models still bypass brownfield guardrails | call the existing development-doc quality validator inside readiness |
| readiness gate is too strict for minimal fixtures | false negatives slow maintenance | use explicit documented inputs and existing quality gates only |
| command remains partially shell-driven | models still need workflow narrative | at least make entry and exit deterministic and validator-backed |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-architecture` | `T002`, `T004` | readiness validator passes and fails on the expected docs package |
| `FR-002` | `plan.md#3-architecture` | `T002`, `T004` | output validator passes on required closeout artifacts |
| `FR-003` | `plan.md#4-contracts`, `plan.md#7-migration-and-rollback` | `T003`, `T004` | command-surface validator includes `/refactor-planning` |
| `FR-004` | `plan.md#7-migration-and-rollback` | `T004`, `T005` | scope remains limited to command gates and public wiring |

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays limited to command gates, not an engine rewrite | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | `/refactor-planning` has explicit deterministic entry and exit rules | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | validator-backed contract is specific enough for implementation | Complete |
