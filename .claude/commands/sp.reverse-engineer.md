# Claude Command: Reverse Engineer  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command reverse-engineers **existing in-memory tasks, plans, or specifications** into structured specifications or plans for Phase I of *The Evolution of Todo*.

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Enable the automated creation of specifications, plans, or checklists from existing task data or partially implemented features, **ensuring full compliance with Phase I rules**.

---

## 3. Preconditions

- Application is running in terminal  
- In-memory task collection exists (for tasks reverse-engineering)  
- Existing specifications or partial plans exist  

---

## 4. Command Steps

### Step 1: Select Source
- [ ] Choose data source: tasks, plan, checklist, or specification  
- [ ] Validate source availability  

### Step 2: Analyze Source
- [ ] Extract relevant information (IDs, titles, descriptions, completion status)  
- [ ] Identify feature boundaries and dependencies  

### Step 3: Generate Specification / Plan
- [ ] Map extracted data to `.specify/templates/` structure  
- [ ] Populate required sections (Context, Objective, Preconditions, Tasks, etc.)  
- [ ] Ensure Phase I constraints are enforced (in-memory, console I/O, no persistence)  

### Step 4: Confirm and Save
- [ ] Review generated output  
- [ ] Save in `.specify/` with proper history and traceability  

---

## 5. Postconditions

- Generated specifications or plans reflect the source accurately  
- Phase I rules are fully enforced  
- Program continues running without errors  

---

## 6. Error Handling

- [ ] Source not found: provide informative message  
- [ ] Invalid or incomplete source: flag inconsistencies  
- [ ] No operation should crash the program  

---

## 7. Constraints

- In-memory storage only  
- Console input/output only  
- No persistence, external services, or manual code edits  
- Must comply with Phase I Constitution rules  

---

## 8. Acceptance Criteria

- [ ] Reverse-engineered output follows template structure  
- [ ] All Phase I constraints enforced  
- [ ] Traceability to tasks, plans, or specifications is maintained  
- [ ] Program continues running without errors  
- [ ] Implementation is fully spec-driven  

---

## 9. Traceability

This command traces to:  
- `constitution.md` (Phase I)  
- `.specify/templates/` (all templates)  
- Existing tasks, plans, or specifications  

---

**End of sp.reverse-engineer.md**
