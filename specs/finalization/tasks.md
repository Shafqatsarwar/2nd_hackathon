# Finalization Task List

## 🛠️ Task 1: Environment Variable Migration
- [ ] **Backend**: Update `src/backend/main.py` and `TaskInterface.tsx` to use environment variables for the backend URL.
- [ ] **Frontend**: Update `src/frontend/lib/auth.ts` to ensure it uses `process.env`.
- [ ] **Admin Logout**: Ensure `handleLogout` in Dashboard is robust.

## 🛠️ Task 2: Code Sanitation
- [ ] Remove `verify_backend.py` and other test residuals.
- [ ] Audit `src/backend/auth_utils.py` for any remaining hardcoded secrets.

## 🛠️ Task 3: Build & Verification
- [ ] Run `npm run build` in `src/frontend`.
- [ ] Verify `src/cli` tests still pass.
- [ ] Verify `src/backend` health check locally.

## 🛠️ Task 4: Documentation Finalization
- [ ] Update `README.md` with final project architecture.
- [ ] Update `guide.md` with Neon setup and deployment steps.
- [ ] Record final PHR.
