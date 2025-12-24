# Specification: Constitutional Alignment & Structural Recovery

### 1. Context
The project has diverged from the repository structure and development process defined in the **Constitution** and the **Phase I Requirements**. This specification outlines the steps to restore the project's integrity.

---

### 2. Objective
Reorganize the codebase to match the mandated directory structure, fix environment inconsistencies, and ensure all Phase I and Phase II components strictly follow the documented requirements.

---

### 3. Structural Reorganization
The root directory must be cleaned to follow Line 77 of the Constitution:
- **Move** `backend/` to `src/backend/`.
- **Move** `frontend/` to `src/frontend/`.
- **Move** existing `src/` CLI files to `src/cli/`.
- **Delete** non-mandated root files: `PHASE2_SETUP.md`, `error.log`, `backend/error.log`, `backend/test_api.py`.

### 4. Dependency Alignment
Update root `pyproject.toml` to manage the whole workspace properly using UV:
- Add `pytest` and `requests` for testing.
- Add `fastapi`, `sqlmodel`, `pyjwt`, etc., as project dependencies.

### 5. Requirements Audit (Phase II)
Verify that the following from `phase1_requirments.txt` is met:
- **Authentication**: JWT verification must use the shared secret correctly.
- **API Endpoints**: Path parameters (`user_id`) vs. JWT-extracted IDs must be reconciled.
- **Database**: Must support Neon PostgreSQL with a valid local SQLite fallback for dev.

---

### 6. Acceptance Criteria
- Repository structure matches Line 77 of the Constitution.
- Phase I tests (`pytest`) pass in the new structure.
- Phase II build (`npm run build`) works without database adapter errors.
- All implementations are preceded by specs and plans.
