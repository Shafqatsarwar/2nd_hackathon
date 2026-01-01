# Specification: User Authentication (Better Auth)
### Phase II — Full-Stack persistent web app

---

### 1. Context
This specification defines the implementation of user authentication for the Evolution of Todo app using **Better Auth** on the Next.js frontend and **JWT Verification** on the FastAPI backend.

---

### 2. Objective
Enable users to sign up and sign in securely. Every user must have an isolated account, and all API requests to the backend must be verified using JWT tokens.

---

### 3. Functional Requirements

#### A. Frontend (Next.js)
- **Library**: `better-auth`.
- **Flow**:
    - Sign Up page (Email/Password).
    - Sign In page (Email/Password).
    - Logout functionality.
- **Session Management**: Session stored as a JWT token.
- **API Interceptor**: Automatically attach the JWT token to the `Authorization: Bearer <token>` header for all backend requests.

#### B. Backend (FastAPI)
- **Verification**: Middleware/Dependency to verify JWT signature using `BETTER_AUTH_SECRET`.
- **Identity**: Extract `user_id` from the verified token.
- **Middleware**: Block any requests to `/api/*` if a valid token is missing (401 Unauthorized).

---

#### 4. Shared Configuration
- **BETTER_AUTH_SECRET**: A shared random string (stored in Environment Variables) used by both Frontend and Backend for token security.

---

### 5. Data Security
- No plain-text passwords stored (managed by Better Auth).
- User isolation enforced: Backend queries are strictly filtered by the `user_id` encoded in the JWT.

---

### 6. Acceptance Criteria
- User can create an account and log in.
- App redirects non-authenticated users to the Login page.
- FastAPI backend rejects requests with invalid or missing tokens.
- User-specific tasks are saved and retrieved correctly based on the logged-in user.
