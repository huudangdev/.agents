# Complexity Reduction Contract

Use this skill when code shape is the problem.

## Required Inputs

- The target file or module
- The observed coupling, nesting, or size issue
- The verification risk of each simplification

## Decision Rules

- Remove complexity only where it has measurable value.
- Prefer structural extraction over broad rewrites.
- Keep behavior stable unless a change is explicitly justified.

## Output Contract

- State the complexity source.
- Name the reduction path and its risk.
- Describe the verification that protects behavior.
