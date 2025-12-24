# Claude Command: Constitution Management  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command manages the **Phase I Constitution** for *The Evolution of Todo* project.  

It is governed by:  
- `constitution.md` (Phase I) itself  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Provide a standardized interface for viewing, validating, and updating the Phase I Constitution, ensuring **all specifications, templates, and implementations comply with governance rules**.  

---

## 3. Preconditions

- Application is running in terminal  
- `constitution.md` exists in `.specify/memory/`  
- User has selected a valid constitution operation  

---

## 4. Command Steps

### Step 1: View Constitution
- [ ] Display full Constitution content in console  
- [ ] Highlight critical rules and constraints  

### Step 2: Validate Constitution
- [ ] Ensure all required sections (Project Context, Objectives, Development Approach, Functional Requirements, Constraints, Repository Structure, Governance, Code Rules, Deliverables, Windows Requirement) are present  
- [ ] Confirm consistency with Phase I rules  

### Step 3: Update Constitution
- [ ] Prompt for necessary updates  
- [ ] Apply changes according to Phase I rules  
- [ ] Preserve history and traceability  

### Step 4: Confirm Changes
- [ ] Review updated content  
- [ ] Save in `.specify/memory/`  
- [ ] Output success confirmation  

---

## 5. Postconditions

- Constitution is valid, up-to-date, and traceable  
- Program continues running  
- History of updates is preserved  

---

## 6. Error Handling

- [ ] Missing Constitution file triggers informative message  
- [ ] Invalid edits prevented  
- [ ] No operation should crash the program  

---

## 7. Constraints

- Console input/output only  
- Constitution must remain Markdown file  
- No manual edits to generated source code  
- Must comply with Phase I governance rules  

---

## 8. Acceptance Criteria

- [ ] Constitution can be viewed, validated, and updated  
- [ ] All Phase I rules enforced  
- [ ] Traceability and history maintained  
- [ ] Program continues running without errors  
- [ ] Implementation fully spec-driven  

---

## 9. Traceability

This command traces to:  
- `constitution.md` (Phase I)  
- All templates and Claude commands  
- Specifications, tasks, plans, checklists, agents, ADRs, and PHR prompts  

---

**End of sp.constitution.md**
