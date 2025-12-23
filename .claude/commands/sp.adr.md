# Claude Command: ADR Management  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command manages **Architecture Decision Records (ADRs)** for Phase I of *The Evolution of Todo* project.  

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Provide a standardized interface for creating, retrieving, updating, and verifying ADRs, ensuring all architectural decisions are documented and **fully spec-driven**.  

---

## 3. Preconditions

- Application is running in terminal  
- `.specify/templates/adr-template.md` exists  
- User has selected a valid ADR operation  

---

## 4. Command Steps

### Step 1: Create ADR
- [ ] Prompt for decision title  
- [ ] Select ADR template  
- [ ] Populate sections: Context, Decision, Status, Alternatives, Rationale, Implications, Dependencies, References  
- [ ] Confirm creation and save in `.specify/`  

### Step 2: Retrieve ADR
- [ ] Select existing ADR  
- [ ] Display content in console  

### Step 3: Update ADR
- [ ] Select ADR to modify  
- [ ] Make spec-driven updates  
- [ ] Confirm changes and preserve ADR history  

### Step 4: Verify ADR
- [ ] Ensure ADR aligns with Phase I Constitution  
- [ ] Confirm all required sections are present  
- [ ] Validate traceability to features, plans, and agents  

---

## 5. Postconditions

- ADRs are created, retrieved, or updated successfully  
- History of ADRs is preserved  
- Program continues running  

---

## 6. Error Handling

- [ ] Invalid template or feature selection handled gracefully  
- [ ] Missing ADR template handled with informative message  
- [ ] No operation should crash the program  

---

## 7. Constraints

- Console input/output only  
- ADRs must remain Markdown files  
- No manual edits to generated source code  
- Must comply with Phase I Constitution rules  

---

## 8. Acceptance Criteria

- [ ] ADRs can be created, retrieved, updated, and verified  
- [ ] Templates are applied correctly  
- [ ] Traceability and history are maintained  
- [ ] Program continues running without errors  
- [ ] Implementation is fully spec-driven  

---

## 9. Traceability

This command traces to:  
- `constitution.md` (Phase I)  
- ADR template (`adr-template.md`)  
- Feature specifications, plans, tasks, and agents  

---

**End of sp.adr.md**
