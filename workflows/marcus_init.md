---
description: Marcus Fleet Startup Matrix (Autonomous Project Scaffolding & Agent Replication)
---
# 🚀 MARCUS FLEET - SUPREME PROJECT KICKSTARTER

This workflow physically automates 100% of manual boilerplate scaffolding (Directory generation, PRD initialization, `.agents` global state injection). Upon invocation, the Antigravity Engine MUST leverage OS-level authority to autonomously bootstrap the physical file tree.

> **ANTIGRAVITY EXECUTION DIRECTIVES:**

1. **Input Parsing:** If the User's command specifies `<Project_Name>` and `<Feature_Description>`, capture these parameters immediately. (If omitted, politely halt execution and prompt the User for these variables prior to proceeding to Step 2).

// turbo
2. **Ecosystem Structuring (Physical Scaffold):** You are MANDATED to execute the `run_command` tool running the following Bash script. This clones the core Intelligence framework into the newly isolated Project Boundary:
    ```bash
    export PROJECT_NAME="<lowercase_kebab_case_project_name>"
    mkdir -p projects/$PROJECT_NAME/docs
    cp -r .agents projects/$PROJECT_NAME/
    cp .agents/.clinerules projects/$PROJECT_NAME/.clinerules
    
    # Boot the TrustGraph localized DB clusters (Neo4j, Postgres, Chroma)
    cd projects/$PROJECT_NAME/.agents/trustgraph && docker-compose up -d && cd ../../../
    
    # Generate the Localized .agents/agents.md (Global Node State)
    cat <<EOF > projects/$PROJECT_NAME/.agents/agents.md
# 🧠 Project Node: $PROJECT_NAME (.agents/agents.md)
> This file governs the History, Task Log, and Active State. NEVER OVERWRITE ENTIRELY. APPEND ONLY.

## 1. 🎯 Macro Overview (Project State)
- **Status:** Bootstrapping
- **Macro-Architecture:** Undefined

## 2. 📝 Agile Backlog (Tasks & Progress)
- [x] Bootstrapped physical infrastructure via marcus_init
- [ ] Render Core PRD & Architectural UML
- [ ] Scaffold Initial UI State

## 3. 🚦 Execution History (Audit Log)
- Initialized State Node.
EOF
    ```

4. **Cognitive Seeding (V30 Planning Genesis):** Utilize the `write_to_file` tool to initialize the Master Specification:
    - **Target Path:** `projects/<Project_Name>/docs/prd_draft.md`
    - **Payload:** Extrapolate the User's raw ideas into an enterprise-grade PRD. This document MUST be thousands of words in density, featuring exhaustive structural logic. This serves as the seed node before `/planning` performs deep research to generate the full legacy `/docs` output contract and V30 research ledgers.

4. **Handoff & Ignition:** Upon successful scaffolding, report the deployment triumph. Instruct (or autonomously route) the User into the new Workspace context:
    > "Project Matrix has been successfully scaffolded. Traverse into the isolated node via `cd projects/<Project_Name>` and invoke `/planning` to authorize the AI Supreme Court to begin logical execution!"
