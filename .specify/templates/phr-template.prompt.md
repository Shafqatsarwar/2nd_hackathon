# Phase-Human-Readable (PHR) Prompt Template  
### Phase I — In-Memory Python Console App

---

## 1. Context

This template defines the **structure for Phase-Human-Readable (PHR) prompts** for Phase I of *The Evolution of Todo* project.  

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

PHRs capture the **intent, input, and expected output** of prompts used to generate features, plans, tasks, checklists, ADRs, or specifications. They ensure **traceability, reproducibility, and governance**.

---

## 2. Objective

Enable standardized creation, storage, and retrieval of PHR prompts:

- Preserve the original prompt (PROMPT_TEXT)  
- Capture the AI response (RESPONSE_TEXT)  
- Record metadata for traceability  
- Ensure compliance with Phase I rules  

---

## 3. Metadata (YAML Header)

```yaml
id: "<unique-id>"           # Auto-generated
stage: "<stage>"            # constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general
feature: "<feature-name>"   # Optional: associated feature
title: "<short-title>"      # 3–7 words descriptive
date: "<YYYY-MM-DD>"        # Creation date
author: "<agent-name>"      # Auto-filled by agent
