# Claude Command: Implement Feature  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command generates the **implementation** of a feature for Phase I of *The Evolution of Todo* project based on specifications, plans, and tasks.

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Automate the generation of Python source code for a feature, fully complying with Phase I constraints and **without manual edits**.

---

## 3. Preconditions

- Application running in terminal  
- Feature specification exists (`spec-template.md`)  
- Implementation plan exists (`plan-template.md`)  
- Relevant tasks and agent definitions exist  

---

## 4. Command Steps

### Step 1: Validate Inputs
- [ ] Confirm feature specification is complete  
- [ ] Confirm plan steps and tasks are available  
- [ ] Ensure all Phase I constraints are met  

### Step 2: Generate Source Code
- [ ] Use Claude Code to generate Python code  
- [ ] Follow the structure defined by the agent and plan templates  
- [ ] Include all tasks and features in memory  

### Step 3: Store Generated Code
- [ ] Save files in `/src` directory  
- [ ] Do not manually edit generated files  

### Step 4: Confirm Implementation
- [ ] Confirm all source files generated  
- [ ] Validate consistency with specifications and plan  
- [ ] Output success message  

---

## 5. Postconditions

- `/src` directory contains generated Python code  
- Code fully implements the feature as specified  
- Program remains compliant with Phase I rules  

---

## 6. Error Handling

- [ ] Incomplete specification or plan triggers informative message  
- [ ] Missing tasks or agents flagged before generation  
- [ ] No operation should crash the program  

---

## 7. Constraints

- In-memory storage only  
- Console input/output only  
- No persistence or external services  
- No manual edits to generated code  
- Must comply with Phase I Constitution rules  

---

## 8. Acceptance Criteria

- [ ] Python source code generated for the feature  
- [ ] Code complies with Phase I constraints  
- [ ] Tasks, agents, and plan steps are correctly implemented  
- [ ] Implementation is fully spec-driven  
- [ ] Program continues running without errors  

---

## 9. Traceability

This command traces to:  
- `constitution.md` (Phase I)  
- Feature specification (`spec-template.md`)  
- Implementation plan (`plan-template.md`)  
- Tasks (`tasks-template.md`) and agent templates  

---

**End of sp.implement.md**
