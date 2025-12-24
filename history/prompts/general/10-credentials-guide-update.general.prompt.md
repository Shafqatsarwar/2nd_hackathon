---
id: "10"
title: "Cloud Configuration & Credentials Guide"
stage: "general"
date: "2025-12-23"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "infrastructure"
branch: "master"
user: "unknown"
command: "Add instructions to guide.md for Neon DB and Better Auth secrets"
labels:
  - "documentation"
  - "credentials"
  - "neon"
  - "better-auth"
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "guide.md"
tests:
  - "none"
---

## Summary of Activity

Enhanced the project guide with actionable instructions for setting up cloud credentials.

### 🛠️ Work Done:
- **Neon DB Integration Guide**: Added step-by-step instructions for creating a Neon project and extracting the Pooled Connection string.
- **Shared Secret Generation**: Provided cross-platform commands (PowerShell and WSL/Linux) to generate secure base64 secrets for Better Auth JWT verification.
- **Environment Management**: Explained how to map these secrets to the `backend/.env` file.

### 🧠 Decision Log:
- Providing PowerShell-specific commands ensures that Windows users (non-WSL) can also generate secure secrets without external tools.
- Emphasized "Pooled Connection" for Neon to ensure compatibility with serverless environments.

### 📂 History Record:
This update satisfies the user's request for clear setup instructions and maintains the verbatim history requirement.
