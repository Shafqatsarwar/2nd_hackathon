# Specification: Add Task
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

Allow the user to create a new Todo task with a title and a description, which will be stored in memory.

---

### 3. Preconditions

- Application is running in a terminal  
- The in-memory task collection is initialized  
- User selects the "Add Task" option from the main menu  

---

### 4. Tasks Breakdown

#### Task 1: Prompt for Task Details
**Description:** Ask the user to input the task title and description.  

**Rules:**  
- Title cannot be empty.
- Description is optional but should be prompted.
- Validate input for non-empty title; re-prompt if empty.

**Output:** Valid Title and Description strings.

---

#### Task 2: Create and Store Task Object
**Description:** Generate a unique ID for the task, create the task object, and add it to the in-memory list.

**Rules:**  
- Increment IDs sequentially (starting from 1).
- Default status: Incomplete.
- Store in a simple list or dictionary in memory.

**Output:** Confirmation message that task was added successfully.

---

### 5. Postconditions

- A new task exists in the in-memory data structure.
- Total task count has increased by one.
- Correct ID and status are assigned.

---

### 6. Error Handling

- Empty title: Provide a clear error message ("Title cannot be empty") and re-prompt.
- Non-string input: Handle gracefully to prevent crashes.

---

### 7. Constraints

- In-memory storage only  
- Console input/output only  
- No persistence  
- Fields: ID, Title, Description, Completion Status  

---

### 8. Acceptance Criteria

Feature is complete when:  
- User can input title and description.
- Task is correctly added and can be retrieved later in the same session.
- Success/Failure messages are clear in the console.

---

### 9. Traceability

This specification traces to:  
- `constitution.md` (Phase I)
- Deliverables: "Adding tasks with title and description"

---

**End of Specification — Add Task**
