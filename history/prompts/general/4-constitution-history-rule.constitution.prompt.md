---
id: "4"
title: "Constitution Update: Mandatory History Recording"
stage: "constitution"
date: "2025-12-23"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "master"
user: "unknown"
command: "Add a role/mandate in constitution for saving chats to history"
labels:
  - "constitution"
  - "rules"
  - "history-mandate"
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "constitution.md"
tests:
  - "Manual verification of file content"
---

## Summary of Change

Updated the governing rules of the project to ensure accountability and traceability.

### 📝 Modified: `constitution.md`
Added **Core Mandate #5**:
> "ALL user prompts, chat iterations, and execution snapshots MUST be recorded verbatim in the root `history/` folder."

### 🧠 Rationale:
This rule ensures that every step taken during the Hackathon is documented, allowing judges and developers to track the evolution of the software and the interaction between the human architect and the AI agent.

### 📂 History Verification:
This prompt itself has been recorded under:
`history/prompts/general/4-constitution-history-rule.constitution.prompt.md` (renamed for clarity/consistency).
