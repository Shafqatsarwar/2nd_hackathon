# Specification: Phase I Core Features
### Todo In-Memory Python Console App

---

### 1. Context
This specification defines the core functionality for the Phase I Todo CLI application. 
Governed by `constitution.md`.

---

### 2. Objective
Implement the 5 basic level features:
1. Add Task (Title & Description)
2. View Task List (Displaying ID, Status, Title, Description)
3. Update Task (Modify Title or Description by ID)
4. Delete Task (Remove by ID)
5. Mark Complete/Incomplete (Toggle status by ID)

---

### 3. Functional Requirements

#### F1: Add Task
- **Input**: Title (required), Description (optional).
- **ID**: Auto-incrementing integer.
- **Status**: Default "Incomplete".

#### F2: View Tasks
- **Output**: Table or list of all tasks.
- **Empty State**: Show "No tasks found."

#### F3: Update Task
- **Input**: Existing Task ID.
- **Fields**: Prompt for new Title and new Description. Retain old if empty.

#### F4: Delete Task
- **Input**: Task ID.
- **Outcome**: Task removed from memory.

#### F5: Toggle Completion
- **Input**: Task ID.
- **Outcome**: Flip `completed` boolean.

---

### 4. Constraints
- In-memory list storage.
- Python 3.13 / UV.
- Console I/O only.

---

### 5. Acceptance Criteria
- Full CRUD + Toggle capability.
- Validated inputs (no empty titles).
- Sequential unique IDs.
