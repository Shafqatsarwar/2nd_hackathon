# Tasks: User Authentication Implementation

### Task 1: Initialize Better Auth on Frontend
- Run `npm install better-auth`.
- Create `lib/auth.ts` on the frontend for Better Auth configuration.
- Set up the Better Auth API route in Next.js (`app/api/auth/[...better-auth]/route.ts`).

### Task 2: Create UI for Sign In & Sign Up
- Premium, glassmorphic UI matching the current theme.
- Forms for Email and Password.
- Integration with Better Auth client methods.

### Task 3: Backend JWT Middleware Implementation
- Install `pyjwt` in backend.
- Create `backend/auth_utils.py` to handle token verification.
- Implement a FastAPI dependency `get_current_user` to extract `user_id` from the Bearer header.

### Task 4: Secure the CRUD Endpoints
- Update all CRUD endpoints in `backend/main.py` to use `get_current_user` instead of taking `user_id` from the path.
- Verify that request without tokens fail.

### Task 5: End-to-End Verification
- Log in on the frontend.
- Create a task.
- Check the database to ensure `user_id` matches the authenticated user.
