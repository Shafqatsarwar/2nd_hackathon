# 🚀 The Evolution of Todo - Phase II Deployment Guide

## 🌟 Project Overview
This project represents the evolution of a simple CLI Todo list into a full-stack AI-powered Web Application.
- **Frontend**: Next.js 16, TailwindCSS, Framer Motion (Glassmorphic UI)
- **Backend**: FastAPI, SQLModel, Neon (PostgreSQL)
- **Auth**: Better Auth (Secure, Self-hosted logic)

---

## 🛠️ Quick Start (Development)

### 1. Start the Backend (The Core)
The backend powers the logic and database connections.
```powershell
cd src/backend
uv run uvicorn main:app --host 0.0.0.0 --port 800 --reload
```
*   **Health Check**: Open `http://localhost:800/health` → `{"status": "healthy"}`
*   **Docs**: Open `http://localhost:800/docs` for Swagger UI.

### 2. Start the Frontend (The Interface)
The frontend provides the premium user experience.
```powershell
cd src/frontend
npm run dev
```
*   **App**: Open `http://localhost:3000`
*   **Note**: The app automatically connects to the backend on port 800.

---

##  Key Features & Usage

### 1. Guest Mode (The Sandbox)
*   Click the **'G' Badge** in the bottom-right## 📘 Environment Variables Master Class

This section explains every key you need, why you need it, and where to get it.

### 1. `DATABASE_URL` (The Memory)
*   **What it is**: The address where your data lives.
*   **Local Development**: Use `sqlite:///todo.db`. This works instantly and saves data to a file on your laptop.
*   **Production (Cloud)**: You need a cloud database. We recommend **Neon**.
    1.  Go to [Neon Console](https://console.neon.tech).
    2.  Create a Project.
    3.  Copy the **Connection String** (Pooled).
    4.  It looks like: `postgresql://user:pass@ep-host.neon.tech/neondb?sslmode=require`

### 2. `BETTER_AUTH_SECRET` (The Security)
*   **What it is**: A secret password used to encrypt user session cookies.
*   **How to get it**: You generate this yourself.
    *   **Option A**: Run `openssl rand -base64 32` in terminal.
    *   **Option B**: Type a random long string (e.g., `my_super_secure_hackathon_secret_key_2025`).

### 3. `NEXT_PUBLIC_BACKEND_URL` (The Bridge)
*   **What it is**: Tells the Frontend where the Backend lives.
*   **Local**: `http://127.0.0.1:800`
*   **Vercel**: `https://your-app-name.vercel.app/api` (If using Unified Deployment).

### 4. `NEXT_PUBLIC_BETTER_AUTH_URL` (The Home)
*   **What it is**: The URL of your website itself.
*   **Local**: `http://localhost:3000`
*   **Vercel**: `https://your-app-name.vercel.app`

---

## 📝 Configuration Cheatsheet

**Scenario A: Running Locally (Copy to `.env`)**
```env
DATABASE_URL="sqlite:///todo.db"
BETTER_AUTH_SECRET="local_dev_secret"
NEXT_PUBLIC_BACKEND_URL="http://127.0.0.1:800"
NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:3000"
```

**Scenario B: Deploying to Vercel (Add to Vercel Env Vars)**
```env
DATABASE_URL="postgresql://neondb_owner:..." (From Neon)
BETTER_AUTH_SECRET="complex_random_string"
NEXT_PUBLIC_BACKEND_URL="https://your-app.vercel.app/api"
NEXT_PUBLIC_BETTER_AUTH_URL="https://your-app.vercel.app"
```

### Build Command
To verify the production build locally:
```powershell
cd src/frontend
npm run build
```

### 🔐 API Testing (Admin Token)
When testing the Backend via Swagger (`/docs`) or cURL, you can bypass login using the Master Admin Token.
*   **Token Value**: `admin_token`
*   **Usage**: In the "Authorize" box, type: `admin_token` (or `Bearer admin_token` in headers).
*   **Effect**: Grants immediate access as the `admin` user.

---

## � Contribution & CLI
Legacy Phase I CLI tools are preserved in `src/cli`.
To run the original CLI:
```powershell
uv run python src/cli/main.py
```

---

## 🏛️ Architecture & Standards
This project follows strict **Agentic Development** principles.

*   **Isolation**: Logic is separated into `src/cli`, `src/backend`, and `src/frontend`.
*   **SDD Loop**: All features are Spec-Driven. See `specs/` for architectural decisions.
*   **Security**: Use path/JWT based user isolation in all API endpoints.
## 🚀 Pushing to GitHub
Your project is ready to go!

1.  **Create Repository**: Go to GitHub and create a new repository (e.g., `evolution-of-todo`).
2.  **Push Code**:
    ```powershell
    git remote add origin https://github.com/Shafqatsarwar/2nd_hackathon.git
    git branch -M master
    git push -u origin master
    ```
    done
