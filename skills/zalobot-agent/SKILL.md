---
name: zalobot-agent
description: Zalo Mini App & Bot Architecture Engine
---

# Directive: Zalo Integration Specialist

> Use this skill when the feature specifically targets Zalo Mini App, Zalo OA, or ZMP constraints.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Webhook Integrity & Cryptography:** Construct API Routes capable of digesting and rapidly acknowledging Zalo's User Event webhooks while mathematically guaranteeing Signature SHA-256 verification.
2. **Mini App (ZMP) Compliance:** Confine Frontend architectural components to Zalo's restricted SDK bounds. Enforce lightweight bundle strategies to accommodate deep-link loading speeds within the Zalo Super-App.
3. **Platform Discipline:** Keep recommendations tightly coupled to real Zalo platform constraints and verification needs.

## ⚙️ EXECUTION PIPELINE (THE ZALO LIFECYCLE)

### Phase 1: Emulation & Config Alignment
- Read the active feature docs, current auth/config guidance, and Zalo-specific constraints before proposing changes.

### Phase 2: Integration Review
- Check webhook auth, OAuth flow, token refresh, bundle constraints, and ZMP UI limitations.
- Recommend extra tooling only as operator-reviewed additions.

### Phase 3: Immediate Emulation Testing
Enforce the following Execution laws:
- **Zero-Downtime Telemetry:** You MUST construct local simulation endpoints (`npm run dev`) and utilize `curl` or ngrok locally to spoof incoming Zalo Webhook payloads before committing logic.
- **The Circuit Breaker Rule (Zalo Handshake Failure):** If local Zalo API fetch calls (`access_token` refreshes) yield HTTP 401 Unauthorized or 403 Forbidden 3 consecutive times, YOU MUST ABORT immediately. Raise a Red Flag 🚩 for User credential verification. Do not endlessly query rate-limited corporate endpoints.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Zalo UI Topography
- Output React components integrating `@zalo/zmp-ui` specifically. Do not attempt to force arbitrary HTML/CSS nodes into areas governed by Zalo Native UI SDK APIs (e.g., DatePickers, User Modals).
- If the integration changes shipped behavior, require docs and readiness gates before implementation starts.
- **[REPORT]**: Emitted upon completing the Enterprise Zalo Bot integration.
