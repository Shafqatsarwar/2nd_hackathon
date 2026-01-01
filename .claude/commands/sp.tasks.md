# Claude Command: Task Management  
### Phase I — In-Memory Python Console App

---

## 1. Context

This command manages **in-memory tasks** for Phase I of *The Evolution of Todo* project.

It is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

## 2. Objective

Provide a standardized interface for creating, viewing, updating, deleting, and marking tasks **without modifying the underlying in-memory data structure outside allowed operations**.

---

## 3. Preconditions

- Application is running in terminal  
- In-memory task collection exists  
- User has selected a valid task-related menu option  

---

## 4. Command Steps

### Step 1: Add Task
- [ ] Prompt for task title (required, non-empty)  
- [ ] Prompt for optional description  
- [ ] Generate unique task ID  
- [ ] Create task object with `completed = false`  
- [ ] Store task in memory  
- [ ] Confirm task creation  

### Step 2: View Tasks
- [ ] Retrieve tasks from memory (read-only)  
- [ ] Display tasks with ID, title, status, and optional description  
- [ ] Handle empty task list gracefully  

### Step 3: Update Task
- [ ] Select task by ID  
- [ ] Prompt for updated title/description  
- [ ] Validate inputs  
- [ ] Update task in memory  
- [ ] Confirm update  

### Step 4: Delete Task
- [ ] Select task by ID  
- [ ] Remove task from memory  
- [ ] Confirm deletion  

### Step 5: Mark Complete / Incomplete
- [ ] Select task by ID  
- [ ] Toggle `completed` status  
- [ ] Confirm status change  

---

## 5. Postconditions

- In-memory task collection reflects all valid changes  
- Program continues running  
- Tasks remain consistent and retrievable  

---

## 6. Error Handling

- [ ] Empty title rejected when adding/updating task  
- [ ] Invalid task ID handled gracefully  
- [ ] No operation should crash the program  
- [ ] User re-prompted as necessary  

---

## 7. Constraints

- In-memory storage only  
- Console input/output only  
- No persistence or external services  
- Must comply with Phase I specifications  

---

## 8.
