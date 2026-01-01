# Claude Command: PHR Management  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command manages **PHR (Phase-Human-Readable) prompts** for Phase I of *The Evolution of Todo* project.  

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Provide a standardized interface for creating, retrieving, updating, and verifying **PHR prompts** for features, ensuring consistency and compliance with Phase I rules.

---

## 3. Preconditions

- Application is running in terminal  
- `.specify/templates/phr-template.prompt.md` exists  
- User has selected a valid PHR-related operation  

---

## 4. Command Steps

### Step 1: Create PHR Prompt
- [ ] Select feature or template  
- [ ] Generate PHR prompt from template  
- [ ] Populate necessary fields for the feature  
- [ ] Confirm creation and save in `.specify/`  

### Step 2: Retrieve PHR Prompt
- [ ] Select existing PHR prompt  
- [ ] Display content in console  

### Step 3: Update PHR Prompt
- [ ] Select existing PHR prompt  
- [ ] Make spec-driven updates  
- [ ] Confirm changes and preserve prompt history  

### Step 4: Verify PHR Prompt
- [ ] Ensure compliance with Phase I Constitution  
- [ ] Confirm all required sections are present  
- [ ] Validate traceability to feature specifications  

---

## 5. Postconditions

- PHR prompts are created, retrieved, or updated successfully  
- History of prompts is preserved  
- Program continues running  

---

## 6. Error Handling

- [ ] Invalid template or feature selection handled gracefully  
- [ ] Missing PHR template handled with informative message  
- [ ] No operation should crash the program  

---

## 7. Constraints

- Console input/output only  
- Prompts must remain Markdown files  
- No manual edits to generated source code  
- Must comply with Phase I Constitution rules  

---

## 8. Acceptance Criteria

- [ ] PHR prompts can be created, retrieved, updated, and verified  
- [ ] Templates are applied correctly  
- [ ] Traceability and history are maintained  
- [ ] Program continues running without errors  
- [ ] Implementation is fully spec-driven  

---

## 9. Traceability

This command traces to:  
- `constitution.md` (Phase I)  
- PHR template (`phr-template.prompt.md`)  
- Feature specifications, plans, tasks, and checklists  

---

**End of sp.phr.md**
