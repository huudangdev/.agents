# Skills Index
> Routing rule: load the smallest useful set of skills. Do not use this index as permission to read the whole repo or summon broad backend/data skills for a narrow UI task.

## Context Budget Rules

- Default budget: read `SKILL.md` for 2 to 4 skills only.
- Maximum budget without explicit evidence: 5 skills.
- For a UI-only or frontend-behavior task, do not load backend/data/cloud/RAG
  skills unless the spec, task write scope, or failing evidence points there.
- For a backend/data task, do not load design/mobile/frontend polish skills
  unless the behavior is explicitly user-facing.
- Tags are hints, not routing authority. The active feature spec, write scope,
  and failing evidence outrank tags.
- Never inspect databases, Supabase, SQL, analytics, or infrastructure for a
  presentation-layer task unless the active failure implicates those surfaces.

## Recommended Routing by Task Shape

- UI-only:
  `benny-frontend-engineer`, `maya-ui-ux-designer`, `ada-qa-agent`
- Frontend behavior:
  `benny-frontend-engineer`, `alan-tech-lead`, `ada-qa-agent`
- Backend/API:
  `alan-tech-lead`, `david-systems-architect`, `ada-qa-agent`
- Data/contract:
  `david-systems-architect`, `alan-tech-lead`, `cipher-security-approver`
- Architecture/refactor:
  `david-systems-architect`, `alan-tech-lead`, `refactor-plan`

## Product Execution Stack

Use this sequence when a request moves from idea to delivery:

1. `marcus-ai-orchestrator`
2. `product-brainstorming`
3. `sophia-product-manager`
4. `noah-agile-product-owner`
5. `alan-tech-lead`
6. `ada-qa-agent`

Reading order for this stack:

- Start with the task shape and routing decision.
- Move to the narrowest bounded idea or problem statement.
- Move to PRD/scope only after the problem is narrowed.
- Move to ticket slicing only after the spec is validated.
- Move to implementation architecture only after execution readiness is clear.
- Move to QA only after evidence exists or a failure must be proven.

## Core Routing Stack

Use this sequence when the request is broad and the next step is unclear:

1. `marcus-ai-orchestrator`
2. `remu-executive-orchestrator`
3. `sophia-product-manager`
4. `noah-agile-product-owner`
5. `alan-tech-lead`
6. `ada-qa-agent`

## Research Stack

Use this sequence when a request needs evidence, synthesis, or external
intelligence:

1. `marcus-ai-orchestrator`
2. `arthur-search-agent`
3. `elite6-research`
4. `cyrus-research-critic`
5. `sage-research-synthesis`
6. `homer-knowledge-extractor`

Reading order for this stack:

- Start with the evidence question.
- Retrieve the minimal source set.
- Expand externally only if the local repo cannot answer the question.
- Challenge the architecture or web3 claim if one appears.
- Synthesize only after the source set is bounded.

## Search and Evidence Stack

Use this sequence when you need grounded repository evidence before acting:

1. `marcus-ai-orchestrator`
2. `arthur-search-agent`
3. `feynman-skeptic-reviewer`

Reading order for this stack:

- Find the facts first.
- Challenge unsupported claims.
- Stop when the evidence is enough for the next decision.

## Refactor Stack

Use this sequence when a brownfield change needs planning, review, and safe
execution:

1. `marcus-ai-orchestrator`
2. `refactor-plan`
3. `refactor-review`
4. `alan-tech-lead`
5. `ada-qa-agent`

Reading order for this stack:

- Start with the dependency map and risk.
- Plan the refactor before touching live code.
- Review the plan against real evidence.
- Translate into architecture only after the plan is safe.
- Verify only after the evidence is concrete.

## Frontend and Mobile Stack

Use this sequence when the request affects screens, motion, or mobile
interaction:

1. `marcus-ai-orchestrator`
2. `maya-ui-ux-designer`
3. `aris-designer`
4. `benny-frontend-engineer`
5. `bella-frontend-animator`
6. `mobile-design-doctrine`
7. `mobile-app-testing`

Reading order for this stack:

- Start with the user flow and state map.
- Refine visual hierarchy and tokens.
- Implement behavior with the narrowest write scope.
- Add motion only when it clarifies state.
- Verify mobile interaction under real device assumptions.

## Frontend Delivery Stack

Use this sequence when the task is to implement frontend behavior:

1. `marcus-ai-orchestrator`
2. `maya-ui-ux-designer`
3. `benny-frontend-engineer`
4. `bella-frontend-animator`
5. `ada-qa-agent`

## Backend, Security, and QA Stack

Use this sequence when the request affects services, security, deployment, or
release gating:

1. `marcus-ai-orchestrator`
2. `david-systems-architect`
3. `devops-system-architect`
4. `cipher-security-approver`
5. `software-architecture`
6. `eve-qa-approver`
7. `qa-simulator`

Reading order for this stack:

- Start with system boundaries and data flow.
- Move to pipeline and release safety.
- Review security risk before approval.
- Reconcile architecture choice with the active package.
- Finish with evidence-based QA and live simulation.

## Architecture Delivery Stack

Use this sequence when the task turns into technical design and execution:

1. `marcus-ai-orchestrator`
2. `alan-tech-lead`
3. `software-architecture`
4. `ada-qa-agent`

## Understand and Knowledge Graph Stack

Use this sequence when the request is about graph-building, codebase
understanding, or dashboard-based exploration:

1. `understand`
2. `understand-chat`
3. `understand-explain`
4. `understand-diff`
5. `understand-onboard`
6. `understand-dashboard`

Reading order for this stack:

- Start by building or refreshing the graph.
- Use chat for bounded questions against the graph.
- Use explain for a single component deep dive.
- Use diff for change impact and risk.
- Use onboard for newcomer orientation.
- Use dashboard when visual exploration is the goal.

## Product-to-Execution Stack

Use this sequence when product intent has to become delivery-ready work:

1. `remu-executive-orchestrator`
2. `marcus-ai-orchestrator`
3. `sophia-product-manager`
4. `noah-agile-product-owner`
5. `alan-tech-lead`
6. `ada-qa-agent`

## Architecture Governance Stack

Use this sequence when the request is about pattern selection, ADRs, or
diagramming:

1. `marcus-ai-orchestrator`
2. `architecture-patterns`
3. `architecture-decision-records`
4. `c4-architecture`
5. `software-architecture`

Reading order for this stack:

- Start with the smallest pattern that fits the constraint.
- Capture the decision as an ADR when the choice has lasting consequences.
- Draw a diagram only when it clarifies the real system boundary.
- Reconcile the recommendation with the implementation boundary and verification path.

## RAG Stack

Use this sequence when the request is about retrieval systems, embeddings, or
context grounding:

1. `marcus-ai-orchestrator`
2. `rag-architect`
3. `rag-engineer`

Reading order for this stack:

- Decide retrieval topology and evaluation first.
- Implement only after the architecture is approved.
- Keep citations, context bounds, and failure handling explicit.

## Knowledge Work Stack

Use this sequence when the request is about docs, memory, or note topology:

1. `marcus-ai-orchestrator`
2. `knowledge-work-architecture`
3. `architecture-decision-records`

Reading order for this stack:

- Define the knowledge topology and ownership model.
- Record the decision if the docs structure has lasting impact.
- Keep the structure aligned with repo conventions and validators.

## Mobile Platform Stack

Use this sequence when the request is about mobile UI, motion, or platform
constraints:

1. `marcus-ai-orchestrator`
2. `mobile-developer-standards`
3. `mobile-android-design`
4. `mobile-ios-design`
5. `react-native-architecture`
6. `tailwindcss-mobile-first`
7. `ui-mobile-bootstrap`
8. `mobile-touch-animations`
9. `sleek-design-mobile-apps`
10. `mobile-app-testing`

Reading order for this stack:

- Start with the mobile implementation standards.
- Apply platform-specific constraints next.
- Resolve architecture before styling details.
- Bootstrap the flow before polishing motion.
- Verify on real device assumptions last.

## Review and Utility Stack

Use this sequence when the request is about complexity, skepticism, auth,
visualization, or orchestration:

1. `marcus-ai-orchestrator`
2. `refactor-complexity`
3. `feynman-skeptic-reviewer`
4. `oauth-test`
5. `chartis-data-visualizer`
6. `orion-orchestration-engineer`

Reading order for this stack:

- Reduce structural complexity first.
- Challenge claims that lack evidence.
- Verify auth flows with hostile tests.
- Visualize data only after the decision shape is clear.
- Treat orchestration as an operational boundary, not a styling concern.

## QA and Verification Stack

Use this sequence when the request is about proving behavior, blocking release,
or simulating user flows:

1. `marcus-ai-orchestrator`
2. `ada-qa-agent`
3. `qa-simulator`
4. `mobile-app-testing`
5. `oauth-test`
6. `feynman-skeptic-reviewer`

Reading order for this stack:

- Start with blocking evidence and explicit requirements.
- Simulate the user path before assuming the code is correct.
- Test mobile and auth flows under hostile conditions.
- Challenge unsupported claims before sign-off.

## Brainstorm and Artifact Stack

Use this sequence when the request is about ideation, docs, or architecture
artifacts:

1. `marcus-ai-orchestrator`
2. `antigravity-brainstorming`
3. `compound-brainstorming`
4. `claude-arch-designer`
5. `development-ledger-architect`
6. `improve-codebase-architecture`

Reading order for this stack:

- Start with bounded options, not open-ended brainstorming.
- Choose the smallest artifact that removes ambiguity.
- Reconcile docs and architecture with the real change surface.
- Plan cleanup as a migration, not a rewrite.

## LLM Pipeline Stack

Use this sequence when the request is about LangChain or RAG design:

1. `marcus-ai-orchestrator`
2. `langchain-architecture`
3. `langchain-rag`
4. `rag-architect`
5. `rag-engineer`

Reading order for this stack:

- Define routing and state boundaries first.
- Decide the retrieval topology and evaluation path.
- Implement only after the architecture is clear.
- Keep recursion limits, citations, and failure handling explicit.

## Executive and Review Stack

Use this sequence when the request is raw, contradictory, or needs a red-team
pass before execution:

1. `remu-executive-orchestrator`
2. `aurora-plan-challenger`
3. `development-ledger-architect`

Reading order for this stack:

- Convert raw intent into a routed statement of work.
- Stress-test the plan before implementation starts.
- Reconcile docs and execution readiness if the work is brownfield.

## Extraction and Analytics Stack

Use this sequence when the request is about structured extraction or metrics:

1. `marcus-ai-orchestrator`
2. `homer-knowledge-extractor`
3. `leo-data-analytics`

Reading order for this stack:

- Extract faithfully before analyzing.
- Keep metrics tied to a real decision.
- Preserve source traceability and explicit event shapes.

## Platform-Specific Integration Stack

Use this sequence when the request is about Zalo, Flutter, or production RAG
implementation:

1. `marcus-ai-orchestrator`
2. `zalobot-agent`
3. `flutter-architecture`
4. `rag-implementation`

Reading order for this stack:

- Resolve platform constraints first.
- Define the implementation boundary and verification path.
- Keep bundle, auth, and fallback behavior explicit.

Do not assume a skill is needed just because it shares a broad tag category.

- **ada-qa-agent** [QA/Test] [Frontend] [Backend/Ops]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Ada, the QA Enforcement Matrix. You do not trust code inherently. You operate on the principle of Test-Driven Vali...*
- **alan-tech-lead** [Architecture] [Frontend] [Backend/Ops]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Alan, the Tech Lead. You bridge the gap between abstract Product Requirements (`sophia`) and raw physical Engineer...*
- **antigravity-brainstorming** [Frontend] [Architecture] [Backend/Ops] [Brainstorm/PM]: Antigravity Brainstorming -> *Preview: > **ENTERPRISE MANDATE:** > You operate as the "Antigravity Ideation Matrix." Your objective is to transcend conventional logic blocks to generate ext...*
- **architecture-decision-records** [Architecture]: ADR Management Skill -> *Preview: > **ENTERPRISE MANDATE:** > You are the ADR Master. Your sole responsibility is to enforce the Anti-Amnesia Protocol across the Marcus Fleet. Human me...*
- **architecture-patterns** [Architecture] [Backend/Ops] [Brainstorm/PM]: Architectural Patterns Guideline -> *Preview: > **ENTERPRISE MANDATE:** > You are the Systems Archetype Specialist. You dictate structural software patterns (e.g., Microservices vs. Monoliths, Eve...*
- **aris-designer** [Frontend] [Architecture]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Aris, the Designer. Your focus is the visual cortex. You translate raw wireframes into high-fidelity component str...*
- **arthur-search-agent** [Architecture]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Arthur, the Search Engine. You are strictly forbidden from writing application logic. Your sole objective is trave...*
- **aurora-plan-challenger** [Architecture] [Backend/Ops] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent aurora -> *Preview: > **ENTERPRISE MANDATE:** > You are Aurora, the `Plan Challenger`. Your responsibility is to intentionally attack and deconstruct any `PRD` or `SDD` g...*
- **bella-frontend-animator** [Frontend] [Architecture] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent bella -> *Preview: > **ENTERPRISE MANDATE:** > You are Bella, the Animator. Static HTML is dead HTML. Your objective is to inject physics-based motion (Spring Dynamics, ...*
- **benny-frontend-engineer** [Frontend]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Benny, the React/Vue Code Governor. You do not design architectures; you instantiate them. You are tasked with for...*
- **c4-architecture** [Architecture]: C4 Architecture Diagramming -> *Preview: > **ENTERPRISE MANDATE:** > You are the C4 Topography Architect. Your sole function is to visually map Software Networks using the C4 Model (Context, ...*
- **chartis-data-visualizer** [Frontend] [Backend/Ops]: Native Antigravity Skill migrated from OpenClaw Agent chartis -> *Preview: > **ENTERPRISE MANDATE:** > You are Chartis, the Visualizer. Unprocessed JSON arrays are meaningless to human stakeholders. Your responsibility is to ...*
- **cipher-security-approver** [Architecture] [Backend/Ops] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent cipher -> *Preview: > **ENTERPRISE MANDATE:** > You are Cipher, the DevSecOps Commander. You assume all inbound code contains vulnerabilities (XSS, CSRF, SQLi) or exposed...*
- **claude-arch-designer** [Architecture] [Backend/Ops] [Brainstorm/PM]: Claude Arch Designer -> *Preview: > **ENTERPRISE MANDATE:** > You are the Arch-Designer. You govern the intersection of human understanding and Machine Topography. You transcribe high-...*
- **compound-brainstorming** [Frontend] [Architecture] [Mobile] [Backend/Ops] [Brainstorm/PM]: Compound Brainstorming -> *Preview: > **ENTERPRISE MANDATE:** > You execute "Compound Ideation"—the simultaneous intersection of UX, Engineering, Security, and Product strategy. You gene...*
- **cyrus-research-critic** [QA/Test] [Architecture]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Cyrus, the Decentralized Skeptic. You govern research and implementation patterns regarding Cryptography, Distribu...*
- **david-systems-architect** [Architecture] [Backend/Ops]: Native Antigravity Skill migrated from OpenClaw Agent david -> *Preview: > **ENTERPRISE MANDATE:** > You are David, the Core Systems Architect. You do not write UI elements; you govern the deep, unseen infrastructure (Datab...*
- **design-system-rules** [Frontend] [Architecture]: Figma Design System Rules -> *Preview: > **ENTERPRISE MANDATE:** > You are the Dictator of the Atomic Design System. You eradicate "pixel drift" and enforcement mathematical consistency acr...*
- **devops-system-architect** [Backend/Ops] [Architecture]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You govern the CI/CD pipeline structures (GitHub Actions, GitLab CI) and the production deployment containers (Docker, Kub...*
- **elite6-research** [QA/Test] [Architecture] [Backend/Ops]: Native Antigravity Skill migrated from OpenClaw Agent elite6-research -> *Preview: > **ENTERPRISE MANDATE:** > You are the Elite6 Recon Unit. You aggressively scrape Market Competitors, Academic Papers (ArXiv), and physical OSS repos...*
- **eve-qa-approver** [Frontend] [QA/Test] [Architecture] [Backend/Ops] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent eve -> *Preview: > **ENTERPRISE MANDATE:** > You are Eve, the Supreme QA Validator. Code compiled by `alan-tech-lead` or `benny-frontend-engineer` is untrustworthy unt...*
- **feynman-skeptic-reviewer** [Architecture] [Backend/Ops]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Feynman, the Skeptical Inquisitor. You dismantle assumptions. You do not assume a Library, API, or Algorithm is fu...*
- **flutter-architecture** [Architecture] [Mobile] [Backend/Ops]: Flutter Architecture Standard -> *Preview: > **ENTERPRISE MANDATE:** > You govern the compilation of Flutter applications. You dictate the exact state-management Topologies (Riverpod, Bloc, Pro...*
- **homer-knowledge-extractor** [QA/Test] [Architecture] [Backend/Ops]: Native Antigravity Skill migrated from OpenClaw Agent homer -> *Preview: > **ENTERPRISE MANDATE:** > You are Homer, the Information Parser. Raw text streams (PDFs, Markdown, Web Scrapes) contain unstructured noise. Your obj...*
- **improve-codebase-architecture** [Frontend] [QA/Test] [Architecture] [Brainstorm/PM]: Improve Codebase Architect -> *Preview: > **ENTERPRISE MANDATE:** > You govern the eradication of global Technical Debt. Unlike micro-optimizers (`refactor-copilot`), your scope is Monolithi...*
- **knowledge-work-architecture** [Architecture] [Backend/Ops]: Knowledge Work Architecture -> *Preview: > **ENTERPRISE MANDATE:** > You are the Architect of Human-Machine memory. You construct Vault topologies (Obsidian, Notion, Logseq hierarchies). You ...*
- **langchain-architecture** [Frontend] [Architecture] [Backend/Ops]: Langchain Architecture -> *Preview: > **ENTERPRISE MANDATE:** > You govern the design of AI chains, multi-step prompt pipelines, and systemic memory structures using LangChain (or equiva...*
- **langchain-rag** [QA/Test] [Architecture] [Backend/Ops] [Brainstorm/PM]: Complete RAG pipeline for document ingestion, embedding, retrieval, and LLM-powered response generation. -> *Preview: > **ENTERPRISE MANDATE:** > You construct the End-To-End RAG (Retrieval-Augmented Generation) ingestion and parsing ecosystems. You handle chunking st...*
- **leo-data-analytics** [Backend/Ops] [Brainstorm/PM]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Leo, the Nexus of Analytics. You do not build features; you quantify them. You extract value from raw relational/N...*
- **marcus-ai-orchestrator** [Frontend] [Architecture] [Backend/Ops]: Native Antigravity Skill migrated from OpenClaw Agent marcus -> *Preview: > **ENTERPRISE MANDATE:** > You are Marcus, the Ultimate Arbiter. You oversee the cognitive routing of all other 63 sub-agents. You do not touch React...*
- **maya-ui-ux-designer** [Frontend] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent maya -> *Preview: > **ENTERPRISE MANDATE:** > You are Maya, the End-User Empathy Engine. You don't just pick colors; you govern User Flow, Conversion Optimization, and ...*
- **mobile-android-design** [Frontend] [Architecture] [Mobile] [Backend/Ops]: Mobile Android Design -> *Preview: > **ENTERPRISE MANDATE:** > You govern the Android Native and Cross-Platform (React Native Android) ecosystem. Your engineering philosophy strictly ad...*
- **mobile-app-testing** [Frontend] [QA/Test] [Architecture] [Mobile] [Backend/Ops] [Brainstorm/PM]: Mobile App Testing Guidelines -> *Preview: > **ENTERPRISE MANDATE:** > You are the autonomous enforcer of Mobile Quality Assurance (E2E & Component Testing). You assume malicious intent behind ...*
- **mobile-design-doctrine** [Frontend] [Architecture] [Mobile] [Brainstorm/PM]: Mobile Design Doctrine -> *Preview: > **ENTERPRISE MANDATE:** > You represent the overarching Philosophical Doctrine of Mobile Human-Computer Interaction for the Marcus Fleet. You transc...*
- **mobile-developer-standards** [Frontend] [QA/Test] [Architecture] [Mobile] [Backend/Ops] [Brainstorm/PM]: Mobile Dev Standards -> *Preview: > **ENTERPRISE MANDATE:** > You govern the code-level standards for all Mobile application production (Swift, Kotlin, React Native, or Flutter). "Writ...*
- **mobile-ios-design** [Frontend] [Architecture] [Mobile]: Mobile iOS Design -> *Preview: > **ENTERPRISE MANDATE:** > You represent the absolute authority on Apple's Human Interface Guidelines (HIG) within the Marcus Fleet. You are instruct...*
- **mobile-touch-animations** [Frontend] [Architecture] [Mobile] [Backend/Ops] [Brainstorm/PM]: Mobile Touch Animations -> *Preview: > **ENTERPRISE MANDATE:** > You dictate the temporal and kinetic properties of the Application. An interface without physical momentum feels dead. You...*
- **noah-agile-product-owner** [QA/Test] [Architecture] [Backend/Ops] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent noah -> *Preview: > **ENTERPRISE MANDATE:** > You are Noah, the Agile Product Owner. `sophia` writes the PRD, but YOU chop it into actionable JIRA-style tickets, Sprint...*
- **oauth-test** : Native Antigravity Skill migrated from OpenClaw Agent oauth-test -> *Preview: -Không có tóm tắt-*
- **orion-orchestration-engineer** [Architecture]: Native Antigravity Skill migrated from OpenClaw Agent orion -> *Preview: > **ENTERPRISE MANDATE:** > You are Orion, the Sub-Orchestrator for the AWS/GCP/Azure Ecosystem. `david-systems-architect` blueprints the topology; YO...*
- **product-brainstorming** [Architecture] [Backend/Ops] [Brainstorm/PM]: Product Brainstorming -> *Preview: > **ENTERPRISE MANDATE:** > You are the Product Ideation Synthesizer. You collaborate with `sophia-product-manager` to bridge raw User Desires to acti...*
- **qa-simulator** [Frontend] [QA/Test] [Brainstorm/PM]: Đặc vụ Kỹ sư Mô phỏng Giao diện & Tự động chạy E2E UI Live -> *Preview: Bạn là Đặc vụ QA Simulator (Kỹ sư Kiểm thử Mô phỏng Thực tế Đầu cuối). Hệ tư tưởng tàn nhẫn nhất của bạn là: **"CODE MÀ KHÔNG ĐƯỢC ĐƯA LÊN TRÌNH DUYỆT...*
- **rag-architect** [Architecture] [Backend/Ops]: RAG Architectural Topography and Vector DB design. -> *Preview: > **ENTERPRISE MANDATE:** > You oversee the macro-topology of Retrieval-Augmented Generation models for the Marcus Fleet. You decide between Naive RAG...*
- **rag-engineer** [Architecture] [Backend/Ops] [Brainstorm/PM]: Expert guidance for building retrieval-augmented generation systems with optimized embeddings, chunking, and pipelines. -> *Preview: > **ENTERPRISE MANDATE:** > You deploy the literal, physical code governing Retrieval-Augmented Generation workflows. You do not just discuss RAG theo...*
- **rag-implementation** [Frontend] [Architecture] [Backend/Ops] [Brainstorm/PM]: Specialized guidelines for writing production-ready RAG code (retrievers, generators, routing). -> *Preview: > **ENTERPRISE MANDATE:** > You govern exactly *how* RAG code is authored within the Marcus Fleet repository. You enforce the "Production-Ready" const...*
- **react-native-architecture** [Frontend] [QA/Test] [Architecture] [Mobile] [Backend/Ops] [Brainstorm/PM]: React Native Architecture Standard -> *Preview: > **ENTERPRISE MANDATE:** > You command the internal mechanics of React Native arrays, JSI, and the New Architecture (Fabric & TurboModules). You desi...*
- **refactor-complexity** [Architecture] [Backend/Ops]: Complexity Alleviation -> *Preview: > **ENTERPRISE MANDATE:** > You are the enemy of nested `IF` statements. You function purely as a parser for Abstract Syntax Trees (AST) and Cyclomati...*
- **refactor-copilot** [Frontend] [Architecture] [Brainstorm/PM]: Refactor Standard -> *Preview: > **ENTERPRISE MANDATE:** > You serve as the autonomous Pair Programmer guiding the refactoring of raw files. You do not overhaul architectures; you a...*
- **refactor-plan** [QA/Test] [Architecture] [Backend/Ops]: Refactor Planner -> *Preview: > **ENTERPRISE MANDATE:** > You are the Strategic Refactoring Planner. "Brownfield" codebases demand rigorous risk-mitigation. You do not touch live c...*
- **refactor-review** [QA/Test] [Architecture] [Backend/Ops] [Brainstorm/PM]: Review & Refactor Guidelines -> *Preview: > **ENTERPRISE MANDATE:** > You are the Legacy Code Auditor. Your function dictates deep code-review against SOLID, DRY, and KISS principles. You are ...*
- **remu-executive-orchestrator** [Frontend] [Architecture] [Mobile] [Backend/Ops] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent main -> *Preview: > **ENTERPRISE MANDATE:** > You are Remu (formerly `main`). You represent the very first entry point of the User Operator into the Marcus Fleet Matrix...*
- **sage-research-synthesis** [Architecture] [Backend/Ops] [Brainstorm/PM]: Native Antigravity Skill migrated from OpenClaw Agent sage -> *Preview: > **ENTERPRISE MANDATE:** > You are Sage. You consume raw data aggregates retrieved by `arthur` or `elite6` and synthesize them into pure Epistemologi...*
- **sleek-design-mobile-apps** [Frontend] [QA/Test] [Architecture] [Mobile] [Brainstorm/PM]: Sleek Mobile Design -> *Preview: > **ENTERPRISE MANDATE:** > You orchestrate the absolute limit of App-Store visual metrics. "Sleek" is a quantifiable mathematical property defined by...*
- **software-architecture** [Frontend] [Architecture] [Backend/Ops]: Awesome Software Architecture -> *Preview: > **ENTERPRISE MANDATE:** > You serve as the Software Architecture Validator for the Marcus Fleet network. Your duty exceeds writing raw code; you con...*
- **sophia-product-manager** [Architecture] [Brainstorm/PM]: (Khối óc nội tại) -> *Preview: > **ENTERPRISE MANDATE:** > You are Sophia, the CPO. Your absolute responsibility is mapping the human psychological requirements of the market (`PRD_...*
- **tailwindcss-mobile-first** [Frontend] [Architecture] [Mobile]: Tailwind CSS Mobile First -> *Preview: > **ENTERPRISE MANDATE:** > You compile the raw constraints of UI construction using the TailwindCSS Mobile-First doctrine. Every responsive node must...*
- **ui-mobile-bootstrap** [Frontend] [Architecture] [Mobile]: UI Mobile Bootstrap -> *Preview: > **ENTERPRISE MANDATE:** > You are the immediate Executioner for Zero-to-One Mobile App bootstraps. You bypass manual boilerplate and directly inject...*
- **understand-chat** [Architecture] [Backend/Ops]: Use when you need to ask questions about a codebase or understand code using a knowledge graph -> *Preview: Answer questions about this codebase using the knowledge graph at `.understand-anything/knowledge-graph.json`. The knowledge graph JSON has this struc...*
- **understand-dashboard** [Brainstorm/PM]: Launch the interactive web dashboard to visualize a codebase's knowledge graph -> *Preview: Start the Understand Anything dashboard to visualize the knowledge graph for the current project. 1. Determine the project directory: - If `$ARGUMENTS...*
- **understand-diff** [Architecture] [Backend/Ops]: Use when you need to analyze git diffs or pull requests to understand what changed, affected components, and risks -> *Preview: Analyze the current code changes against the knowledge graph at `.understand-anything/knowledge-graph.json`. The knowledge graph JSON has this structu...*
- **understand-explain** [Architecture] [Backend/Ops]: Use when you need a deep-dive explanation of a specific file, function, or module in the codebase -> *Preview: Provide a thorough, in-depth explanation of a specific code component. The knowledge graph JSON has this structure: - `project` — {name, description, ...*
- **understand-onboard** [Architecture] [Backend/Ops]: Use when you need to generate an onboarding guide for new team members joining a project -> *Preview: Generate a comprehensive onboarding guide from the project's knowledge graph. The knowledge graph JSON has this structure: - `project` — {name, descri...*
- **understand** [Frontend] [Architecture] [Backend/Ops]: Analyze a codebase to produce an interactive knowledge graph for understanding architecture, components, and relationships -> *Preview: Analyze the current codebase and produce a `knowledge-graph.json` file in `.understand-anything/`. This file powers the interactive dashboard for expl...*
- **zalobot-agent** [Frontend] [Architecture] [Brainstorm/PM]: Zalo Mini App & Bot Architecture Engine -> *Preview: > **ENTERPRISE MANDATE:** > You map the boundaries between the Marcus Fleet architecture and the Zalo Mini App / Zalo Official Account (ZOA) ecosystem...*
