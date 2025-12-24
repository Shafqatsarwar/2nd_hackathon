# Tasks Specification: Add Task
### Phase I — In-Memory Python Console App

---

### 1. Context

This specification defines the work required to implement the **Add Task** feature for **Phase I** of *The Evolution of Todo* project.

This feature is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

### 2. Objective

Enable a user to add a new todo task via the console. Tasks are stored in memory with an ID, title, description, and completion status.

---

### 3. Preconditions

- Application is running in a terminal  
- In-memory task list exists  
- User selects the “Add Task” option from the menu  

---

### 4. Tasks Breakdown

#### Task 1: Prompt for Task Title
**Description:** Prompt the user to enter a task title.  

**Rules:**  
- Title is required.  
- Empty or whitespace-only input is invalid.  
- Re-prompt until a valid title is provided.  

**Output:** Valid task title string.

---

#### Task 2: Prompt for Task Description
**Description:** Prompt the user to enter an optional task description.  

**Rules:**  
- Description may be empty.  
- Empty input is stored as an empty string.  

**Output:** Task description string (possibly empty).

---

#### Task 3: Generate Task ID
**Description:** Generate a unique identifier for the task.  

**Rules:**  
- ID must be an integer.  
- IDs start at `1` and increment sequentially (`len(tasks) + 1`).  
- IDs are not reused during a single program run.  

**Output:** Unique task ID.

---

#### Task 4: Create Task Object
**Description:** Create a new task container (dictionary) using the collected inputs.  

**Rules:**  
- Task must include: `id`, `title`, `description`, `completed`.  
- `completed` must be initialized to `false`.  

**Output:** Valid in-memory task dictionary.

---

#### Task 5: Store Task In Memory
**Description:** Add the dictionary to the in-memory task list.  

**Rules:**  
- No persistence.  

**Output:** Updated in-memory task list.

---

#### Task 6: Confirm Task Creation
**Description:** Display confirmation to the user.  

**Rules:**  
- Must confirm success.  
- Must display task ID and title.  

**Example Output:** `Task #1 'Buy Groceries' added successfully!`

---

### 5. Postconditions

- Task exists in memory.
- Total task count has increased.
- Program returns to the main menu.

---

### 6. Error Handling

- Empty title: Display error and re-prompt.
- Non-string input: Handle gracefully.

---

### 7. Constraints

- In-memory storage only.
- Console input/output only.
- No manual code edits.

---

### 8. Acceptance Criteria

- User can successfully add a task.
- Each task receives a unique ID.
- Confirmation is displayed.
- Implementation is fully spec-driven.

---

### 9. Traceability

This specification traces to:  
- `constitution.md` (Phase I)
- `specs/001-add-task/spec.md`
- `specs/001-add-task/plan.md`

---

**End of Tasks Specification — Add Task**
