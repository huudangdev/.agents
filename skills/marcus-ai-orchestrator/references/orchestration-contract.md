# Orchestration Contract

Use this reference when `marcus-ai-orchestrator` needs to produce a routing plan or agent DAG.

## Required Inputs

- The task shape.
- The likely downstream skills.
- Any known blockers or stale packages.

## Output Structure

- Task classification.
- Routing plan.
- Constraints.
- Escalation paths.
- Final output.

## Evidence Rules

- Use the minimum viable skill set.
- Avoid overlap between owners.
- State blockers and stop conditions explicitly.
