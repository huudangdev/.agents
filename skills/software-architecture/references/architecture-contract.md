# Software Architecture Contract

Use this skill when a change affects boundaries, topology, verification, or release safety.

## Required Inputs

- Current feature spec or equivalent requirements
- Current plan or execution notes
- Verification evidence or the tests that will prove the change
- Local repo conventions, existing skills, and existing ADRs before proposing new structure

## Decision Rules

- Prefer the smallest architecture that satisfies the requirement.
- Do not introduce new patterns, frameworks, or services until local evidence justifies them.
- Separate domain, infrastructure, and presentation concerns explicitly.
- Treat cyclic dependencies, unclear ownership, and unverified topology as blockers.

## Output Contract

- Name the proposed boundaries and why they exist.
- Identify the change surface and likely blast radius.
- State the verification required before implementation and before merge.
- Provide diagrams or structured layout guidance only when they clarify the real system.
