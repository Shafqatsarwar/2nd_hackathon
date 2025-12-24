# Specification: Todo API CRUD Endpoints
### Phase II — Persistent FastAPI Backend

---

### 1. Context
This specification defines the RESTful API endpoints for managing Todo tasks, ensuring persistence via SQLModel and Neon PostgreSQL.

---

### 2. Objective
Enable the Frontend to perform full CRUD (Create, Read, Update, Delete) operations on tasks, isolated by `user_id`.

---

### 3. API Endpoints

#### GET /api/{user_id}/tasks
- **Description**: List all tasks for a specific user.
- **Output**: List of Task objects.

#### POST /api/{user_id}/tasks
- **Description**: Create a new task for a user.
- **Input**: `title` (required), `description` (optional).
- **Output**: Created Task object with ID.

#### GET /api/{user_id}/tasks/{id}
- **Description**: Get details of a single task.
- **Output**: Task object or 404.

#### PUT /api/{user_id}/tasks/{id}
- **Description**: Update task title or description.
- **Input**: Updated fields.
- **Output**: Updated Task object.

#### DELETE /api/{user_id}/tasks/{id}
- **Description**: Remove a task.
- **Output**: Success message or 404.

#### PATCH /api/{user_id}/tasks/{id}/complete
- **Description**: Toggle the completion status of a task.
- **Output**: Updated Task object.

---

### 4. Logic & Security
- **Isolation**: Every query must include a filter for `user_id`.
- **Validation**: Title cannot be empty.
- **Persistence**: All changes must be committed to the database.

---

### 5. Acceptance Criteria
- All 6 endpoints are functional.
- Data is correctly stored in the configured database.
- Correct status codes (200, 201, 404) are returned.
