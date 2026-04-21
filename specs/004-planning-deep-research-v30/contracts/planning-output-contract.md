# Contract: /planning V30 Output Preservation

## Required Legacy Outputs

The `/planning` workflow must continue producing these files:

```text
docs/prd.md
docs/tasks.md
docs/knowledge.md
docs/decisions.md
docs/memory.md
docs/planning/flows.md
docs/planning/screens.md
docs/planning/diagrams.md
```

## Added Deep Research Outputs

V30 adds these audit artifacts:

```text
docs/research/sources.jsonl
docs/research/evidence.jsonl
docs/research/claims.jsonl
docs/research/contradictions.md
docs/research/research_manifest.json
```

## Validation

For completed planning runs:

```bash
python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
python3 .agents/scripts/validate_planning_research.py --root . --strict-outputs
```

## Compatibility Rule

New research files support the legacy outputs. They must not replace, merge, or
rename the existing `/docs` files.
