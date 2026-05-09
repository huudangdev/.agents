# C4 Diagram Contract

Use this skill when a diagram reduces ambiguity.

## Required Inputs

- The active spec, plan, and architecture notes
- The system boundaries you want to explain
- The lowest useful C4 level for the question

## Decision Rules

- Render one level at a time.
- Prefer real boxes and arrows over generic abstractions.
- Keep the diagram scoped to the current question.

## Output Contract

- Output valid Mermaid for the requested C4 level.
- Quote labels that need it.
- If rendering is needed, use the local terminal path only when supported.
