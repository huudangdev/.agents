# Refactor Copilot Contract

Use this skill for narrow, behavior-preserving refactors.

## Required Inputs

- The target file set
- The change boundary and existing lint/test commands
- The behavior that must not change

## Decision Rules

- Keep the write scope narrow.
- Preserve outputs and contracts.
- Verify the file-level change before expanding further.

## Output Contract

- State the refactor boundaries.
- Show the verification command.
- Describe any docs or sync targets if contracts changed.
