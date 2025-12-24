# Implementation Plan: Add Task
### Phase I — In-Memory Python Console App

---

### 1. Context

This plan outlines the step-by-step approach to implement the **Add Task** feature for **Phase I** of *The Evolution of Todo* project.

This plan is governed by:  
- `constitution.md` (Phase I)  
- Spec-Kit Plus rules  
- Claude Code execution model  

---

### 2. Objective

Implement the logic to capture task information from the user and store it in an in-memory list using a Python-generated CLI.

---

### 3. Preconditions

- Application running in terminal  
- In-memory list `tasks = []` initialized  
- Entry point `src/main.py` created  

---

### 4. Implementation Steps

#### Step 1: Initialize Task Storage
**Description:** Ensure a global or class-level list exists to store task dictionaries.  

**Inputs Required:** None  

**Process:** Create a variable `tasks = []` in the main script or a dedicated container.  

**Outputs Produced:** Empty list ready for storage.

---

#### Step 2: Implement User Input Loop
**Description:** Create the CLI menu and capture user input for Title and Description.  

**Inputs Required:** User keyboard input.  

**Process:** Use `input()` to capture data. Implement a loop that keeps the program running until the user chooses to exit.  

**Outputs Produced:** Captured Title and Description strings.

---

#### Step 3: Logic for Task Creation
**Description:** Bundle the Title, Description, and a generated ID into a dictionary.  

**Inputs Required:** Title, Description, and current task count for ID generation.  

**Process:** `id = len(tasks) + 1`. Create `new_task = {"id": id, "title": title, "description": desc, "completed": False}`.  

**Outputs Produced:** New task dictionary.

---

#### Step 4: Add to Menu
**Description:** Integrate the "Add Task" logic as choice '1' in the main menu.

**Inputs Required:** None

**Process:** Update the `while` loop logic in `main.py`.

**Outputs Produced:** Functional menu option.

---

### 5. Dependencies

- Needs `src/main.py` to be the entry point.
- Depends on basic console I/O.

---

### 6. Error Handling Plan

- If Title is empty: Show `Error: Title cannot be empty`, then re-prompt for the title only.

---

### 7. Technical Constraints

- In-memory storage only.
- Console input/output only.

---

### 8. Validation & Verification

- **Internal Check:** Run the app, select '1', enter "Buy Milk" and "Go to shop". 
- **Expected Result:** App displays "Task added successfully!" and returns to menu.

---

### 9. Traceability

This plan traces to:  
- `constitution.md` (Phase I)
- `specs/001-add-task/spec.md`

---

**End of Implementation Plan — Add Task**
