# Feature Specification: Marcus Init Output Contract Hardening

> Feature ID: `015-marcus-init-output-contract-hardening`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Convert /marcus_init from workflow-only into a command with explicit scaffold-output validation, so project bootstrapping can be verified deterministically by any model.

## 1. Purpose

Harden `/marcus_init` so project bootstrapping no longer ends with a purely
narrative claim that a workspace was scaffolded correctly. The workflow already
describes a deterministic shell scaffold, root-memory creation, and PRD draft
seeding, but nothing in `.agents` currently validates the resulting project
root before the command is considered complete.

This feature adds a local scaffold-output validator and wires it into the public
slash-command contract. The goal is narrow and practical: any model should be
able to inspect `/marcus_init`, know which outputs must exist, and validate that
the scaffolded project root contains them before claiming the bootstrap phase
worked.

## 2. User Stories

- [x] As an operator, I need `/marcus_init` to prove the scaffolded project root
      contains the expected bootstrap artifacts so that new workspaces start
      from a real baseline.
- [x] As an implementation model, I need `/marcus_init` to name its required
      output validator so that I do not stop at shell prose.
- [x] As a governance maintainer, I need `/marcus_init` to be part of the
      shared command-surface contract so public docs and workflow stay aligned.

## 3. Functional Requirements

- `FR-001`: The system MUST provide a local validator for `/marcus_init` that
  checks the expected scaffold outputs for a generated project root.
- `FR-002`: The system MUST wire `/marcus_init` into the public slash-command
  contract so README, `USAGE_GUIDE.md`, registry, and workflow file all expose
  the output-validation step.
- `FR-003`: The system MUST fail validation when required scaffold outputs such
  as `agents.md`, `.agents/agents.md`, `.clinerules`, or `docs/prd_draft.md`
  are missing or empty.
- `FR-004`: The system MUST keep `/marcus_init` scoped to bootstrap verification
  and avoid expanding it into a general project-generator rewrite.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: scaffold validation must be a small local file check.
- `NFR-002`: Security: no new remote or privileged execution path is added.
- `NFR-003`: Observability: failures must name the missing or empty scaffold
  output explicitly.
- `NFR-004`: Maintainability: the validator should reflect the current workflow
  output contract, not invent a second bootstrap system.
- `NFR-005`: Documentation and traceability: `/marcus_init` must move from
  workflow-only to script-backed in the public command contract.

For any item that is intentionally deferred, say so explicitly and record the
accepted risk instead of leaving the field vague.

## 5. Acceptance Criteria

- `AC-001`: Given a scaffold root with `docs/`, `.agents/`, `.clinerules`,
  `agents.md`, `.agents/agents.md`, and `docs/prd_draft.md`, when
  `python3 scripts/validate_marcus_init_outputs.py --root <project-root>` runs,
  then it passes.
- `AC-002`: Given a scaffold root missing one required output, when the same
  validator runs, then it fails and names the missing path.
- `AC-003`: Given `/marcus_init` is published in README and `USAGE_GUIDE.md`,
  when `python3 scripts/validate_command_surface.py --root .` runs, then it
  confirms `/marcus_init` points to the output validator chain.
- `AC-004`: Given `/marcus_init` hardening is added, when command-surface
  validation replays, then the broader public contract still passes.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".

## 6. Clarifications

Record unresolved questions as explicit markers. Planning is blocked while any
marker remains unless the operator accepts the risk.

- No unresolved clarifications remain. Success means `/marcus_init` has a local
  scaffold-output validator and a public command contract entry.

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `workflows/marcus_init.md`, README,
  `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`,
  `scripts/validate_command_surface.py`, and this feature package.
- Files or modules out of scope: rewriting the bootstrap shell chain, changing
  downstream scaffolded app code, or adding remote project templating.
- Compatibility requirements: `/marcus_init` must stay a bootstrap command and
  must not become a generic repo mutation engine.
- Documentation prerequisites already reviewed: current `/marcus_init`
  workflow, public command docs, and registry state after features `013` and
  `014`.
- Rollback or containment expectations: removing the validator and contract
  markers should restore the previous workflow-only `/marcus_init` behavior.

Out of scope:

- Replacing the shell scaffold with a new Python orchestrator.
- Automatically validating the quality of the seeded PRD content.
- Converting `/refactor-planning` in this slice.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| validator and workflow drift later | models trust stale bootstrap contract | put `/marcus_init` under shared command-surface validation |
| scaffold expectations vary by project type | validator over-constrains output | keep required outputs limited to the current workflow's explicit baseline |
| command remains too shell-heavy | models still mis-handle execution | at least close the loop with deterministic output validation |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-architecture` | `T002`, `T004` | output validator passes on a valid scaffold fixture |
| `FR-002` | `plan.md#4-contracts`, `plan.md#7-migration-and-rollback` | `T003`, `T004` | command-surface validator includes `/marcus_init` |
| `FR-003` | `plan.md#3-architecture` | `T004`, `T005` | negative proof fails on missing scaffold output |
| `FR-004` | `plan.md#7-migration-and-rollback` | `T004`, `T005` | scope remains limited to output validation and public contract wiring |

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays limited to scaffold-output validation | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | `/marcus_init` output contract is explicit and testable | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | script-backed `/marcus_init` closeout is specific enough for implementation | Complete |
