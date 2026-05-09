# Orchestration Contract

Use this skill when cloud or platform orchestration needs to be designed.

## Required Inputs

- The target cloud/runtime environment
- The boundary between app logic and infra orchestration
- Reliability, scaling, and rollback constraints

## Decision Rules

- Prefer the smallest orchestration topology that fits the need.
- Keep environment, deployment, and runtime boundaries explicit.
- Do not add orchestration layers without a clear operational gain.

## Output Contract

- State the orchestration topology and why it exists.
- Identify operational risks and rollback expectations.
- Describe what must be verified before rollout.
