---
description: Run a structured challenge loop across spec, plan, and task artifacts before execution.
---

# Marcus Review Workflow

Use this workflow after `/marcus.tasks` and before behavior-changing execution.

## Required Actions

1. Read `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, `agent-routing.md`,
   and `verification.md`.
2. Review the package from four angles:
   - scope correctness
   - architecture and contract coherence
   - verification realism
   - documentation handoff quality
3. Populate or update these sections with concrete findings:
   - `spec.md#10. Review Loop`
   - `tasks.md#Review Loop Tasks`
   - `verification.md#Review Rounds`
   - `execution-brief.md#Context Expansion Rules`
4. For each finding, choose one disposition only:
   - resolved now
   - accepted residual risk
   - blocked and must return to planning
5. Fail the review when:
   - POC slice is too broad to verify credibly
   - acceptance criteria are not requirement-linked
   - review topology does not identify a real evaluator
   - docs package contains ceremony without replayable evidence
6. Run:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/<feature-id> --task-shape <task-shape>
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>
   ```
   If the review narrows the slice to specific changed files or a concrete
   failing check, rebuild with `--changed-files` and `--failing-evidence`
   rather than widening the brief by hand.

## Output

- Updated review-loop artifacts
- A disposition of `proceed`, `revise`, or `stop`
- A short list of blocking findings or accepted residual risks
