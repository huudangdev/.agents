# Zalo Integration Contract

Use this skill when the feature targets Zalo Mini App, Zalo OA, or ZMP constraints.

## Required Inputs

- The auth/config guidance and Zalo constraints
- Webhook, OAuth, and bundle limits
- Verification or simulation expectations

## Decision Rules

- Respect Zalo-native SDK boundaries.
- Treat webhook and token handling as blocking concerns.
- Keep the bundle light and the behavior verifiable locally.

## Output Contract

- State the Zalo-specific constraints.
- Identify the webhook, auth, and bundle risks.
- Describe the local verification or simulation required.
