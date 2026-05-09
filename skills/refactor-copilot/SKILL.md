---
name: refactor-copilot
description: Perform narrow, behavior-preserving refactors with explicit verification
---

# Pair-Programming Refactor Specialist

Use this skill for narrow, behavior-preserving refactors.

## Required Reads

- [refactor-copilot-contract.md](references/refactor-copilot-contract.md)
- The target file set and existing lint/test commands when they exist.

## Operating Rules

- Keep the write scope narrow.
- Preserve outputs and contracts.
- Verify the file-level change before expanding further.

## Output Expectations

- State the refactor boundaries.
- Show the verification command.
- Describe any docs or sync targets if contracts changed.
