# Claude Command: Convert Tasks to Issues  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command converts **in-memory tasks** into issue entries suitable for tracking or reporting.

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Automate the process of transforming **Add Task / View Task entries** into structured issue objects without modifying in-memory task data.

---

## 3. Preconditions

- Application is running in terminal  
- In-memory task collection exists  
- Tasks have valid IDs and titles  

---

## 4. Command Steps

### Step 1: Retrieve Tasks
- [ ] Access in-memory task list  
- [ ] Ensure no tasks are modified  

### Step 2: Transform to Issue Objects
- [ ] Map task properties to issue properties:  
  - `id` → `issue_id`  
  - `title` → `summary`  
  - `description` → `details`  
  - `completed` → `status` (`Open` / `Closed`)  
- [ ] Maintain order of tasks  

### Step 3: Output Issues
- [ ] Generate issue objects in a structured format (JSON, Markdown, or console table)  
- [ ] Display or return issues without modifying original tasks  

---

## 5. Postconditions

- Original in-memory tasks remain unchanged  
- Issue objects correctly reflect task data  
- Program continues running  

---

## 6. Error Handling

- [ ] Handle empty task list gracefully  
- [ ] Validate all task fields before conversion  
- [ ] No application crashes allowed  

---

## 7. Constraints

- In-memory storage only  
- Console input/output only  
- No persistence or external services  
- Must comply with Phase I specifications  

---

## 8. Acceptance Criteria

- [ ] Tasks converted to issue objects correctly  
- [ ] Empty task list handled gracefully  
- [ ] Conversion does not modify original tasks  
- [ ] Output is structured and readable  
- [ ] Implementation is fully spec-driven  

---

## 9. Traceability

This command traces to:  
- `constitution.md` (Phase I)  
- Task specifications (`tasks-template.md`)  
- Plan and checklist templates  

---

**End of sp.taskstoissues.md**
