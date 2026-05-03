# Routing Regression Checklist

Use this checklist before trusting `/develop` on a new Marcus Fleet release or
after changing routing, workflows, or `SKILLS_INDEX.md`.

The goal is simple: confirm that narrow tasks stay narrow. A UI task should not
drift into backend, database, analytics, or infrastructure context unless the
spec or failing evidence proves that it must.

## How To Use

1. Pick one concrete prompt for each task shape below.
2. Record:
   - task classification
   - docs read
   - skills loaded
   - forbidden surfaces avoided
   - reason for any scope widening
3. Fail the checklist if the run reads unrelated systems without evidence.

## Pass Criteria

- The task is classified correctly before broad context loading.
- The docs read are the smallest set that can govern the change safely.
- The loaded skills stay within the expected budget and discipline.
- No forbidden default reads occur.
- If scope widens, `verification.md` records why.

## 1. UI-only

Example prompts:

- "Adjust button spacing and label hierarchy on the checkout page."
- "Polish the hero section layout and fix mobile padding."

Expected classification:

- `UI-only`

Expected docs:

- active feature workspace
- relevant brand/page/feature docs
- target component files

Expected skills:

- `benny-frontend-engineer`
- `maya-ui-ux-designer`
- `ada-qa-agent`

Forbidden default reads:

- Supabase
- SQL
- migrations
- analytics
- cloud configs
- unrelated backend services

## 2. Frontend Behavior

Example prompts:

- "Fix the client-side validation on the signup form."
- "The modal opens twice after clicking confirm."

Expected classification:

- `Frontend behavior`

Expected docs:

- active feature workspace
- relevant page/feature/task docs
- target components/hooks/tests

Expected skills:

- `benny-frontend-engineer`
- `alan-tech-lead`
- `ada-qa-agent`

Forbidden default reads:

- schema/migration files
- analytics stacks
- cloud orchestration

## 3. Backend/API

Example prompts:

- "Fix the 401 from the checkout API."
- "Patch the webhook route to reject malformed payloads."

Expected classification:

- `Backend/API`

Expected docs:

- active feature workspace
- contracts
- data-model
- affected module/service docs

Expected skills:

- `alan-tech-lead`
- `david-systems-architect`
- `ada-qa-agent`

Forbidden default reads:

- unrelated brand/theme/page docs
- animation or design skills unless QA evidence ties the issue to user-visible behavior

## 4. Data/Contract

Example prompts:

- "Add the missing field to the schema and rollout safely."
- "Fix the Supabase row policy mismatch."

Expected classification:

- `Data/contract`

Expected docs:

- active feature workspace
- contracts
- data-model
- rollback notes
- affected module docs

Expected skills:

- `david-systems-architect`
- `alan-tech-lead`
- `cipher-security-approver`

Forbidden default reads:

- unrelated page/component docs
- visual design skills

## 5. Architecture/Refactor

Example prompts:

- "Break this monolithic checkout module into bounded slices."
- "Untangle circular dependencies across these services."

Expected classification:

- `Architecture/refactor`

Expected docs:

- active feature workspace
- decisions/diagrams
- affected modules only

Expected skills:

- `david-systems-architect`
- `alan-tech-lead`
- `refactor-plan`

Forbidden default reads:

- full repo scans without a bounded module list
- random DB or UI exploration unrelated to the stated refactor boundary

## Failure Signals

Treat any of the following as a routing regression:

- UI-only task reads Supabase, SQL, analytics, or infra by default
- narrow task loads more than 4 skills without strong evidence
- `/develop` reads broad `/docs` sets before classifying the task
- backend/data tasks summon polish/animation/design skills without user-facing justification
- the same class of wrong-scope read appears repeatedly across runs

## Release Gate

Do not trust a `.agents` routing change until all 5 task shapes can pass this
checklist without scope drift.
