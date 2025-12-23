# Architecture Specification: Phase II Full-Stack Transition
### The Evolution of Todo — CLI to Cloud-Native

---

### 1. Context
This specification moves the project from a local, in-memory CLI (Phase I) to a multi-user, persistent Full-Stack Web Application (Phase II).

Governed by:
- `constitution.md`
- SDD Workflow (Spec -> Plan -> Tasks)
- Windows Compatibility Constraints (No Turbopack)

---

### 2. Objective
Build a robust, scalable Todo application with a clear separation of concerns between the Frontend (Next.js) and Backend (FastAPI).

---

### 3. System Architecture

#### A. Backend (FastAPI)
- **Framework**: FastAPI (Python 3.13+)
- **ORM**: SQLModel (pydantic + SQLAlchemy)
- **Database**: Neon Serverless PostgreSQL
- **Responsibility**: CRUD operations, user-specific data filtering, JWT verification.

#### B. Frontend (Next.js)
- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **Styling**: Vanilla CSS / Modern UI
- **Responsibility**: User Interface, Authentication Flow (Better Auth), state management.

---

### 4. Authentication Flow (JWT)
1. **Frontend**: Better Auth handles signup/login.
2. **Token**: Better Auth issues a JWT token.
3. **API Calls**: Frontend sends JWT in `Authorization: Bearer <token>` header.
4. **Backend**: Middleware verifies JWT using the shared `BETTER_AUTH_SECRET`.
5. **Context**: Backend extracts `user_id` and filters all queries.

---

### 5. Data Model (SQLModel)
- **User Table**: ID, Email, Name.
- **Task Table**: ID, Title, Description, Completed (bool), User_ID (Foreign Key).

---

### 6. Windows Compatibility & Stability
- **No Turbopack**: Always use `npm run dev` WITHOUT the `--turbo` flag.
- **Stable Packages**: Use `psycopg2-binary` for database connectivity.
- **Environment**: Managed via `.env` files for both Frontend and Backend.

---

### 7. Constraints
- Must remain compatible with Windows/WSL2.
- No complex state managers (use React hooks).
- Free-tier friendly (Neon DB).

---

### 8. Acceptance Criteria
- Full CRUD functionality as per Phase I.
- Data persistence in Neon PostgreSQL.
- User isolation (User A cannot see User B's tasks).
- Successful JWT verification on every protected route.
