# Feature Specification: Harness Auto Enforcement and Freshness

> Feature ID: `011-harness-auto-enforcement-and-freshness`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Upgrade .agents from mostly documented context/harness discipline to stronger mechanical enforcement: add runnable preflight/postflight orchestration and a repo-wide contract freshness validator, then verify and document the result.

## 1. Purpose

Upgrade `.agents` from a mostly documented governance layer into a stronger
mechanical harness. Operators already have spec validation, routing validation,
and bootstrap checks, but those protections still depend too much on an agent
remembering which commands to run and in what order. This feature adds a
one-command preflight and postflight path for the most critical execution
moments, plus a repo-wide freshness validator that catches stale workflow/docs/
script wiring before an agent starts or closes work.

The outcome is narrower than "make the whole system autonomous." It is to make
the current harness harder to forget, easier to replay, and more resistant to
doc drift. An operator should be able to run a bootstrap preflight, an
execution preflight, and an execution postflight and get a deterministic answer
about whether `.agents` is in a safe state for the next step.

## 2. User Stories

- [x] As an operator, I need a single preflight entrypoint so that I do not
      rely on memory to run the right bootstrap and readiness checks.
- [x] As an implementation agent, I need a single postflight entrypoint so that
      closeout validation is replayable after workflow or harness changes.
- [x] As a harness maintainer, I need a repo-wide freshness validator so that
      README, USAGE, workflows, and scripts do not silently drift apart.

## 3. Functional Requirements

- `FR-001`: The system MUST provide a runnable harness preflight command for
  bootstrap and execution phases, with deterministic exit status and clear
  reporting.
- `FR-002`: The system MUST provide a runnable harness postflight command for
  execution closeout so operators can replay core validation after edits.
- `FR-003`: The system MUST provide a repo-wide harness contract validator that
  fails when core `.agents` docs, workflows, and scripts disagree about the
  required enforcement chain.
- `FR-004`: The system MUST wire the new commands into the public `.agents`
  operating surface, including bootstrap, `/develop`, `/quick_fix`, README, and
  USAGE guidance.
- `FR-005`: The system MUST remain compatible with both supported root layouts:
  project root containing `.agents`, and the standalone `.agents` repository.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must state observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: the orchestration commands must finish quickly enough
  for routine use and must only call existing local scripts.
- `NFR-002`: Security: no new network installers, shell `eval`, or destructive
  filesystem operations are introduced.
- `NFR-003`: Observability: every orchestration command must print which checks
  ran and whether failures are blocking or warning-only.
- `NFR-004`: Maintainability: path resolution logic should be reused rather than
  copied again into every new script.
- `NFR-005`: Documentation and traceability: the spec package, workflows, and
  verification evidence must record the exact command chain now expected.

For any item that is intentionally deferred, say so explicitly and record the
accepted risk instead of leaving the field vague.

## 5. Acceptance Criteria

- `AC-001`: Given the standalone `.agents` repository, when an operator runs
  the bootstrap preflight, then MCP sync, health classification, update brief,
  and harness freshness checks run in one deterministic chain.
- `AC-002`: Given a feature-scoped execution path, when an operator runs the
  execution preflight and postflight, then readiness and harness checks run in
  the documented order and fail non-zero on blocking problems.
- `AC-003`: Given stale or missing workflow/doc/script wiring, when the harness
  contract validator runs, then it reports the mismatched file and missing
  marker instead of silently passing.
- `AC-004`: Given updated harness scripts, when README, USAGE, `/init_brain`,
  `/develop`, and `/quick_fix` are read, then they present the same preflight
  and postflight command chain.
- `AC-005`: Given either supported root layout, when the new scripts run, then
  they resolve paths correctly without `.agents/.agents/...` regressions.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".

## 6. Clarifications

Record unresolved questions as explicit markers. Planning is blocked while any
marker remains unless the operator accepts the risk.

- No unresolved clarifications. Success means the new commands run in the
  standalone `.agents` repository and the updated docs/workflows present the
  same chain that verification replayed.

## 7. Constraints

- Constitution articles that apply: Article I (spec as source of truth),
  Article IV (verification evidence), Article IX (execution readiness),
  Article X (review loop), and Article XI (POC rehearsal).
- Existing files or modules in scope: `.agents/scripts/`, `README.md`,
  `USAGE_GUIDE.md`, `workflows/init_brain.md`, `workflows/develop.md`,
  `workflows/quick_fix.md`, `workflows/marcus_verify.md`, `mcp/mcp.json`, and
  the feature spec package.
- Files or modules out of scope: downstream application repositories, TrustGraph
  adapters, and unrelated skills or workflow content that do not participate in
  harness enforcement.
- Compatibility requirements: preserve the current slash-command surface and the
  two supported root layouts; avoid forcing networked services or external
  dependencies.
- Documentation prerequisites already reviewed: `memory/constitution.md`,
  `workflows/marcus_specify.md`, `workflows/develop.md`, `workflows/quick_fix.md`,
  `workflows/init_brain.md`, and `specs/010-brownfield-doc-reconcile-command/`.
- Rollback or containment expectations: the new orchestration layer must be
  removable without corrupting existing validators or feature packages.

Out of scope:

- Full observability dashboards, historical metrics storage, or automatic
  background daemons.
- Rewriting every `.agents` document for style consistency.
- Replacing existing validators that already prove useful localized behavior.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Orchestration wrappers hide the underlying failing command | Debugging gets harder | Print each invoked command and preserve non-zero exit codes |
| Freshness validation becomes another shallow marker check | Drift still sneaks through | Bind the validator to actual public workflows and script names |
| Scope grows into full agent telemetry platform | Delivery stalls | Keep this feature focused on orchestration and freshness only |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-architecture` | `T002`, `T004` | preflight bootstrap + execution replay |
| `FR-002` | `plan.md#3-architecture` | `T002`, `T004` | postflight execution replay |
| `FR-003` | `plan.md#4-contracts` | `T003`, `T004` | negative and positive freshness checks |
| `FR-004` | `plan.md#6-agent-routing` | `T003`, `T004` | README/USAGE/workflow marker checks |
| `FR-005` | `plan.md#7-migration-and-rollback` | `T002`, `T004` | standalone `.agents` replay |

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | orchestration stays bounded to harness enforcement, not full telemetry | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | requirements and acceptance criteria name concrete commands and surfaces | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | spec package is stable enough for `plan.md` and code work | Complete |
