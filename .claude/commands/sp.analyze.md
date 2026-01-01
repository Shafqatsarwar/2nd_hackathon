# Claude Command: Analyze Feature / Task Data  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command analyzes **existing tasks, specifications, plans, or agents** to extract insights, detect inconsistencies, and prepare for reverse-engineering or implementation in Phase I of *The Evolution of Todo* project.  

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Provide a standardized interface for analyzing in-memory and specification data, ensuring all extracted information **follows Phase I constraints** and supports spec-driven development.  

---

## 3. Preconditions

- Application is running in terminal  
- Relevant in-memory collections exist (tasks, plans, specifications, agents)  
- User has selected a valid analysis target  

---

## 4. Command Steps

### Step 1: Select Analysis Target
- [ ] Choose between tasks, plans, specifications, or agents  
- [ ] Validate target availability  

### Step 2: Extract Data
- [ ] Retrieve relevant data from in-memory structures or templates  
- [ ] Validate completeness and consistency  

### Step 3: Analyze Data
- [ ] Identify feature boundaries and dependencies  
- [ ] Detect missing, incomplete, or inconsistent elements  
- [ ] Summarize insights in a structured format  

### Step 4: Output Results
- [ ] Display analysis report in console or Markdown  
- [ ] Prepare data for reverse-engineering or implementation  

---

## 5. Postconditions

- Analysis report generated accurately  
- Original in-memory or template data remains unchanged  
- Program continues running  

---

## 6. Error Handling

- [ ] Invalid or missing analysis target handled gracefully  
- [ ] Incomplete or inconsistent data flagged in report  
- [ ] No operation should crash the program  

---

## 7. Constraints

- In-memory storage only  
- Console input/output only  
- No persistence or external services  
- Must comply with Phase I Constitution rules  

---

## 8. Acceptance Criteria

- [ ] Analysis target correctly processed  
- [ ] Inconsistencies or missing data reported  
- [ ] Program continues running without errors  
- [ ] Implementation is fully spec-driven  

---

## 9. Traceability

This command traces to:  
- `constitution.md` (Phase I)  
- Tasks (`tasks-template.md`), Plans (`plan-template.md`), Specifications (`spec-template.md`), and Agents (`agent-file-template.md`)  

---

**End of sp.analyze.md**
