---
description: Derive agent-owned implementation tasks from a Marcus Fleet plan.
---

# Marcus Tasks Workflow

Use this workflow after `/marcus.plan`.

## Required Actions

1. Read `plan.md`, `contracts/`, `data-model.md`, `quickstart.md`, and
   `agent-routing.md`.
2. Rewrite `tasks.md` into concrete work items.
3. Each task must include:
   - Stable task id
   - Owner skill
   - Write scope
   - Verification method
   - Documentation targets under `/docs/development/`
   - Doc sync expectation when source files change
   - Explicit failure or escalation condition
4. Mark `[P]` only when write scopes are disjoint.
5. For implementation tasks, include the expected epic/module/feature/page/task
   note and the legacy docs likely to need append/targeted patch updates.
6. Add an `Execution Monitoring` section naming pre-code gates, checkpoint
   cadence, and the human-escalation trigger.
7. Build an execution brief for the expected task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/<feature-id> --task-shape <ui-only|frontend-behavior|backend-api|data-contract|architecture-refactor|general>
   ```
   The brief must identify the relevant `docs/development/` notes for the work
   slice so `/develop` can read the right epic/feature/module/page/task memory
   without loading the whole ledger.
   When the active slice is already anchored to specific edits or a known
   failing check, add `--changed-files "<comma-separated-files>"` and
   `--failing-evidence "<bounded-failure-summary>"` so the brief foregrounds
   those signals without widening default reads.
8. Immediately prove the brief is current and the package is executable:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>
   ```

## Output

- Executable `tasks.md`
- Parallel groups and sequencing
- Documentation target matrix
- `execution-brief.md`
