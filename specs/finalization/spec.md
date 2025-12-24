# Phase II Finalization & Deployment Readiness Specification

## 1. Overview
This specification covers the final steps required to transition "The Evolution of Todo" from a local development environment to a production-ready state, adhering strictly to the project Constitution.

## 2. Objectives
- **Zero-Hardcoding**: Extract all API URLs, Secrets, and Database strings into environment variables.
- **Production Parity**: Ensure the application performs identically in `dev` and `build` modes.
- **Neon Integration**: Finalize the cloud database connection logic for persistence.
- **Documentation**: Provide a foolproof "Hackathon Judge" guide for deployment.

## 3. Technical Requirements

### 3.1 Environment Variables
- **Backend (`.env`)**:
    - `DATABASE_URL`: Connection string for Neon PostgreSQL.
    - `BETTER_AUTH_SECRET`: Secret for JWT signing.
- **Frontend (`.env.local`)**:
    - `NEXT_PUBLIC_BACKEND_URL`: URL of the deployed FastAPI service.
    - `BETTER_AUTH_URL`: Canonical URL of the frontend (for Auth redirects).

### 3.2 Security
- Verify JWT verification logic in `auth_utils.py` uses the environment secret.
- Ensure the "Admin Bypass" is clearly marked as a demo feature for judges.

### 3.3 Persistence
- Ensure `database.py` in the backend correctly picks up `DATABASE_URL`.
- Ensure SQLModel migrations (auto-create) work on Neon.

## 4. Deliverables
1.  **Sanitized Source**: Source code free of hardcoded localhost URLs.
2.  **Verified Build**: Successful `npm run build` and `uv build` (if applicable).
3.  **Deployment Guide**: Step-by-step instructions for Vercel (Frontend) and Render/Fly.io (Backend).
