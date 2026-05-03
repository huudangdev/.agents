# Feature Specification: Slash Command Workflow Contract Hardening

> Feature ID: `013-slash-command-workflow-contract-hardening`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Ensure every slash command published in README/USAGE has an explicit workflow file, the correct script chain, and a validator-enforced contract so any model can follow .agents deterministically.

## 1. Purpose

Harden the `.agents` operating surface so published slash commands are no longer
described only by prose spread across README, `USAGE_GUIDE.md`, and workflow
files. The immediate problem is ambiguity: some commands are visible in one
public doc but not another, some workflow files call important scripts without a
single source of truth, and validators only cover a narrow subset of the
surface. That leaves too much room for model guesswork, especially when a new
model or a shallow context window tries to infer which script should run next.

This feature establishes a deterministic slash-command contract for the
published `.agents` surface. The outcome must be concrete: if a command is
presented as supported, the repo must show which workflow file owns it, which
script or gate chain it must invoke, and which validator proves the public docs
and workflow still agree. The business value is governance quality. Any model
should be able to read the contract, follow the same execution chain, and fail
closed when the contract drifts instead of improvising enterprise-critical
workflow behavior.

## 2. User Stories

- [x] As an operator, I need every published slash command to resolve to one
      explicit workflow so that execution does not depend on model intuition.
- [x] As an implementation model, I need the required script chain for each
      supported command so that I can follow `.agents` deterministically.
- [x] As a governance maintainer, I need a validator-backed public command
      registry so that README, `USAGE_GUIDE.md`, and workflow files cannot drift
      silently.

## 3. Functional Requirements

- `FR-001`: The system MUST define a public slash-command registry for the
  published `.agents` commands, including the owning workflow file and required
  script or gate chain for each script-backed command.
- `FR-002`: The system MUST fail validation when README, `USAGE_GUIDE.md`, the
  registry, and workflow files disagree about a published slash command or its
  required script chain.
- `FR-003`: The system MUST normalize command-surface coverage for commands that
  were previously under-specified, including `/bootstrap` and
  `/marcus.routecheck`.
- `FR-004`: The system MUST preserve existing bounded-context and harness
  behavior while adding this stricter public contract.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: command-surface validation must stay lightweight and
  file-based; no network or external services.
- `NFR-002`: Security: the registry must describe commands and local entrypoints
  only, not introduce new privilege or remote execution paths.
- `NFR-003`: Observability: validation failures must identify the exact command,
  file, and missing marker that broke the contract.
- `NFR-004`: Maintainability: one validator should hold the command registry
  contract instead of scattering fragile one-off checks across multiple files.
- `NFR-005`: Documentation and traceability: public docs must explicitly point
  maintainers to the registry and validator as the contract source of truth.

For any item that is intentionally deferred, say so explicitly and record the
accepted risk instead of leaving the field vague.

## 5. Acceptance Criteria

- `AC-001`: Given a published script-backed slash command, when a maintainer
  reads `.agents/SLASH_COMMAND_REGISTRY.md`, then the owning workflow file and
  required script or gate chain are explicit.
- `AC-002`: Given a drift between a workflow file and the public command
  contract, when `python3 scripts/validate_command_surface.py --root .` runs,
  then it fails with the offending command and missing marker.
- `AC-003`: Given the public docs are aligned, when
  `python3 scripts/validate_command_surface.py --root .` runs, then it passes
  and confirms README, `USAGE_GUIDE.md`, registry, and workflow files agree.
- `AC-004`: Given `/bootstrap` and `/marcus.routecheck` are part of the public
  surface, when operators read README and `USAGE_GUIDE.md`, then those commands
  are no longer hidden or inconsistently documented.
- `AC-005`: Given command-surface hardening is added, when routing and harness
  validators replay, then they still pass without changing bounded-context or
  harness semantics.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".

## 6. Clarifications

Record unresolved questions as explicit markers. Planning is blocked while any
marker remains unless the operator accepts the risk.

- No unresolved clarifications remain. Success means published commands are
  backed by explicit workflow and script-chain evidence, and command-surface
  drift fails validation instead of being tolerated.

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `README.md`, `USAGE_GUIDE.md`,
  `workflows/*.md`, `scripts/validate_command_surface.py`, and this feature
  package.
- Files or modules out of scope: downstream repos, external model adapters,
  TrustGraph runtime, and application source code outside `.agents`.
- Compatibility requirements: existing harness and routing validators must keep
  working; command-surface hardening must be additive and file-local.
- Documentation prerequisites already reviewed: current README execution command
  sections, `USAGE_GUIDE.md` slash-command wiring rules, and the workflow files
  for published commands.
- Rollback or containment expectations: reverting the registry and validator
  changes should restore the prior looser command-surface checks without
  affecting source-edit workflows.

Out of scope:

- Rewriting every legacy workflow into a fully automated script chain.
- Introducing external registries, remote metadata, or runtime command brokers.
- Changing command semantics beyond making the published contract explicit and
  validator-enforced.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Registry and validator diverge again later | models trust stale contract text | validator checks the registry, README, USAGE, and workflow files together |
| Legacy commands still have narrative-only segments | maintainers over-assume full automation | registry labels mixed or workflow-only commands explicitly |
| Public docs over-promise deterministic behavior | models call wrong scripts | only script-backed commands get hard script-chain markers in the registry |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-architecture`, `plan.md#4-contracts` | `T002`, `T004` | registry lists workflow and required invocations |
| `FR-002` | `plan.md#3-architecture`, `plan.md#6-agent-routing` | `T003`, `T004` | command-surface validator fails on drift |
| `FR-003` | `plan.md#7-migration-and-rollback` | `T004`, `T005` | README and USAGE expose `/bootstrap` and `/marcus.routecheck` consistently |
| `FR-004` | `plan.md#7-migration-and-rollback` | `T004`, `T006` | routing and harness validators still pass |

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays inside `.agents` and does not widen into unrelated automation | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | public command contract is specific enough for any model to follow | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | validator, registry, and doc-surface strategy are stable enough for implementation | Complete |
