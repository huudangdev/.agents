---
description: Rehearse the smallest professional POC slice and issue a go/no-go recommendation.
---

# Marcus Rehearse Workflow

Use this workflow after `/marcus.review` and before `/develop` on non-trivial work.

## Required Actions

1. Read `plan.md#POC Slice and Review Cadence`, `quickstart.md`,
   `verification.md`, `agent-routing.md`, and `execution-brief.md`.
2. Identify the smallest end-to-end path that proves the feature package is
   executable without claiming the whole product is done.
3. Rehearse that path exactly as documented:
   - setup and preconditions
   - verification command or manual flow
   - evidence capture
   - rollback or containment check
4. Update:
   - `quickstart.md#POC Rehearsal`
   - `verification.md#Evidence`
   - `verification.md#Release Recommendation`
5. Rebuild and recheck the execution brief after rehearsal evidence changes the
   active slice, docs-to-read list, or release signals:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/<feature-id> --task-shape <task-shape>
   python3 .agents/scripts/validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>
   ```
   Add `--changed-files` and `--failing-evidence` when the rehearsal exposed a
   bounded edit set or a concrete failing command that should drive the next
   execution slice.
6. Issue one recommendation only:
   - `GO`
   - `GO WITH RESIDUAL RISK`
   - `NO-GO`
7. If the rehearsal reveals missing docs, vague commands, or non-replayable
   expectations, stop and route back to `/marcus.plan` or `/marcus.tasks`
   before implementation begins.

## Output

- Rehearsed POC path with captured evidence
- Updated release recommendation
- Clear `go/no-go` decision for `/develop`
