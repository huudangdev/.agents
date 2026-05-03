---
description: Trigger OTA Upgrade from Github Repository while preserving agents.md local memory.
---

# 🔄 ANTIGRAVITY OTA UPGRADE PROTOCOL

> **ARCHITECTURAL MANDATE:**  
> This protocol downloads the latest Antigravity AI Engine (`.agents`) from the centralized `main` branch. It utilizes non-destructive `rsync` vectors to patch the intelligence fleet (new Slash Commands, new Prompts, updated UI protocols) while explicitly protecting the local `agents.md` memory construct (and preserving the legacy `.agents/agents.md` shim when present) and `trustgraph/data/` database.

// turbo-all

---

## 🟢 STAGE 1: INITIATE OTA PATCH SCRIPT
*🧠 Mandatory Action:* Run the global CURL command mapped to the `update.sh` endpoint. Assuming the user's terminal is at the project root:

1. **[OS_CALL - Remote Trigger]:**
   Execute the following command in the bash shell exactly as written:
   `curl -sL https://raw.githubusercontent.com/huudangdev/.agents/main/update.sh | bash`

2. After successful execution, the Terminal will emit a Green `✔ Update Complete!` confirmation. The Active Node must read this terminal stream to proceed.

## 🔵 STAGE 2: MEMORY RE-ALIGNMENT
1. Perform a manual scan using the LLM context reader to check if the `.clinerules` protocol was drastically updated.
2. Emit a success message to the User, signaling that the OTA pipeline has sealed the patch and the Agent Fleet is fully up to date. 
3. **CRITICAL Handoff:** You MUST explicitly instruct the Human Operator to run `/init_brain` immediately following this update. Explain that `/init_brain` acts as a "Soft Reboot" to lock in the new `.clinerules`, parse the updated `SKILLS_INDEX`, and re-ignite the TrustGraph Docker instances. No code alteration should be carried out during `/update_brain` unless explicitly requested.
