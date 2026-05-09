# Executive Routing Contract

Use this skill to convert raw user intent into the right next workflow.

## Required Inputs

- The raw request
- The active project context
- The likely routing target or ambiguity

## Decision Rules

- Decide whether the work is a quick fix, a feature, or a doc reconcile path.
- Route to the smallest useful skill set.
- Do not improvise direct implementation for non-trivial requests.

## Output Contract

- State the statement of work.
- Name the next workflow and why.
- List the validation path if the work affects behavior.
