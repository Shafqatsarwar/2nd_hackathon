# Tasks: Structural & Constitutional Alignment

### Task 1: Repository Restructure
- [ ] Create `src/cli`, `src/backend`, `src/frontend` directories.
- [ ] Move Phase I files from `src/` to `src/cli/`.
- [ ] Move `backend/` contents to `src/backend/`.
- [ ] Move `frontend/` contents to `src/frontend/`.
- [ ] Delete temporary and non-mandated root files.

### Task 2: Root Project Configuration
- [ ] Update `pyproject.toml` with workspace members and base dependencies.
- [ ] Add `pytest` to dev dependencies.

### Task 3: Fix Import Paths
- [ ] Update `src/backend/main.py` and `src/backend/database.py` imports to be relative/absolute correctly based on the new nested structure.

### Task 4: Verify Phase I
- [ ] Run `pytest` on `src/cli/test_core.py`.

### Task 5: Final Documentation Sync
- [ ] Update `guide.md` and `README.md` to reflect the NEW sanctioned structure.
