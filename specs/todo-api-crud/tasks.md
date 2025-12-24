# Tasks: Todo API CRUD Implementation

### Task 1: Create Schema for API Requests
- Define Pydantic models (SQLModel) for creating and updating tasks.
- Ensure `TaskCreate` and `TaskUpdate` models are clean.

### Task 2: Implement "List Tasks" Endpoint
- Logic to query `Task` table filtered by `user_id`.

### Task 3: Implement "Create Task" Endpoint
- Validate input.
- Assign `user_id` from URL.
- Commit to DB.

### Task 4: Implement "Update" and "Patch" Endpoints
- Fetch task by ID.
- Check if it belongs to the `user_id`.
- Update and commit.

### Task 5: Implement "Delete" Endpoint
- Fetch and remove task if it belongs to the user.

### Task 6: Manual Testing via Swagger UI
- Verify endpoints at `/docs`.
