# 🚀 The Evolution of Todo - Phase III Deployment Guide

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
cd src/backend uv sync
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```
*   **Health Check**: Open `http://localhost:8000/health` → `{"status": "healthy"}`
*   **Docs**: Open `http://localhost:8000/docs` for Swagger UI.


### 2. Start the Frontend (The Interface)
The frontend provides the premium user experience.
```powershell
cd src/frontend
npm run dev
```
*   **App**: Open `http://localhost:3000`
*   **Note**: The app automatically connects to the backend on port 800.

---
### 3. Contribution & CLI
Legacy Phase I CLI tools are preserved in `src/cli`.
To run the original CLI:
```powershell
uv run python src/cli/main.py
```

##  Key Features & Usage

### 1. Guest Mode (The Sandbox)
*   Click the **'G' Badge** in the bottom-right corner for quick AI chat access
*   Provides temporary guest session for trying the AI assistant

### 2. Dedicated AI Assistant
*   Visit **/chatbot** for a full-featured chat interface
*   Clean, focused environment for AI task management
*   Includes chat history and clear functionality

## 📘 Environment Variables Master Class

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
*   **Local**: `http://127.0.0.1:8000`
*   **Vercel**: `https://your-app-name.vercel.app/api` (If using Unified Deployment).

### 4. `NEXT_PUBLIC_BETTER_AUTH_URL` (The Home)
*   **What it is**: The URL of your website itself.
*   **Local**: `http://localhost:3000`
*   **Vercel**: `https://your-app-name.vercel.app`

### 5. `OPENAI_API_KEY` (AI Integration - Optional)
*   **What it is**: API key for OpenAI integration (for Phase III AI features)
*   **Note**: This is optional and only needed for advanced AI features
*   **Local**: Add to your `.env` file (not in example files for security)
*   **Get from**: [OpenAI Platform](https://platform.openai.com/api-keys)
*   **Example**: `sk-...your-key-here...`

---

## 📝 Configuration Cheatsheet

**Scenario A: Running Locally (Copy to `.env`)**
```env
DATABASE_URL="sqlite:///todo.db"
BETTER_AUTH_SECRET="local_dev_secret"
NEXT_PUBLIC_BACKEND_URL="http://127.0.0.1:8000"
NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:3000"
```

**Scenario B: Deploying to Vercel (Add to Vercel Env Vars)**
```env
DATABASE_URL="postgresql://neondb_owner:..." (From Neon)
BETTER_AUTH_SECRET="complex_random_string"
NEXT_PUBLIC_BACKEND_URL="https://your-app-name.vercel.app/api"
NEXT_PUBLIC_BETTER_AUTH_URL="https://your-app-name.vercel.app"
```

---

## 🚀 Deploying to Vercel (Combined Frontend + Backend)

This project uses a **unified deployment architecture** where both the Next.js frontend and FastAPI backend are deployed together on Vercel as a single application.

### 🏗️ Architecture Overview

The combined deployment works through these key components:

1. **`api/index.py`** (Root Level)
   - Acts as a bridge/entry point for Vercel serverless functions
   - Imports and exposes the FastAPI app from `src/backend/main.py`
   - Vercel automatically detects this as a Python serverless function

2. **`vercel.json`** (Root Level)
   - Configures URL rewrites to route API requests to the Python backend
   - Routes `/api/*`, `/docs`, and `/openapi.json` to `api/index.py`
   - All other routes are handled by Next.js frontend

3. **`src/frontend/`**
   - Contains the Next.js application
   - Vercel automatically detects and builds this as the main application
   - Frontend makes API calls to `/api/*` which are routed to the backend

### 📂 Deployment File Structure
```text
.
├── api/
│   └── index.py          # Vercel serverless function entry point
├── vercel.json           # Routing configuration
├── src/
│   ├── backend/          # FastAPI application
│   │   ├── main.py       # Main FastAPI app
│   │   └── ...
│   └── frontend/         # Next.js application (build root)
│       ├── app/
│       ├── package.json
│       └── ...
└── pyproject.toml        # Python dependencies
```

### 🔧 Vercel Project Configuration

When setting up your Vercel project:

1. **Root Directory**: Leave as `.` (project root)
2. **Build Command**: Vercel auto-detects from `src/frontend/package.json`
3. **Output Directory**: `.next` (auto-detected)
4. **Install Command**: `npm install` (in `src/frontend`)

### 📝 Environment Variables (Vercel Dashboard)

Add these in your Vercel project settings:

```env
DATABASE_URL=postgresql://neondb_owner:xxxxx@ep-xxxxx.region.aws.neon.tech/neondb?sslmode=require
BETTER_AUTH_SECRET=your_complex_random_string_here
NEXT_PUBLIC_BACKEND_URL=https://your-app-name.vercel.app/api
NEXT_PUBLIC_BETTER_AUTH_URL=https://your-app-name.vercel.app
```

> [!IMPORTANT]
> - `DATABASE_URL`: Get from [Neon Console](https://console.neon.tech) (use Pooled connection string)
> - `BETTER_AUTH_SECRET`: Generate with `openssl rand -base64 32`
> - `NEXT_PUBLIC_BACKEND_URL`: Your Vercel URL + `/api`
> - `NEXT_PUBLIC_BETTER_AUTH_URL`: Your Vercel URL

### 🚀 Deployment Steps

#### Option A: Deploy via Vercel Dashboard

1. **Push to GitHub**:
   ```powershell
   git add .
   git commit -m "Ready for deployment"
   git push origin master
   ```

2. **Import to Vercel**:
   - Go to [vercel.com/new](https://vercel.com/new)
   - Import your GitHub repository
   - Vercel auto-detects Next.js configuration

3. **Configure Settings**:
   - **Framework Preset**: Next.js
   - **Root Directory**: `./` (leave default)
   - **Build Command**: (leave default - auto-detected)
   - **Output Directory**: (leave default - auto-detected)

4. **Add Environment Variables**:
   - Add all 4 environment variables listed above
   - Make sure to use your actual Neon database URL

5. **Deploy**:
   - Click "Deploy"
   - Wait for build to complete (~2-3 minutes)

#### Option B: Deploy via Vercel CLI

**Starting Directory**: Project root (`d:\Panaverse\Hackathon\2nd_hackathon-phase1-2`)

```powershell
# Navigate to project root (if not already there)
cd d:\Panaverse\Hackathon\2nd_hackathon-phase1-2

# Install Vercel CLI (one-time setup)
npm i -g vercel

# Login to Vercel (one-time setup)
vercel login

# Deploy from project root
vercel

# Follow prompts and add environment variables when asked
```

### ✅ Verify Deployment

After deployment, test these endpoints:

1. **Frontend**: `https://your-app.vercel.app`
2. **Backend Health**: `https://your-app.vercel.app/api/health`
3. **API Docs**: `https://your-app.vercel.app/docs`
4. **OpenAPI Spec**: `https://your-app.vercel.app/openapi.json`

### 🧪 Local Production Build Test

Before deploying, test the production build locally:

```powershell
cd src/frontend
npm run build
npm start
```

### 🔍 Troubleshooting

**Build Fails**:
- Check that all environment variables are set in Vercel dashboard
- Verify `api/index.py` correctly imports from `src.backend.main`
- Ensure `pyproject.toml` includes all Python dependencies

**API Routes Not Working**:
- Verify `vercel.json` rewrites are configured correctly
- Check that `NEXT_PUBLIC_BACKEND_URL` points to `/api`
- Review Vercel function logs in dashboard

**Database Connection Issues**:
- Ensure using Neon's **Pooled** connection string (not Direct)
- Verify `sslmode=require` is in the connection string
- Check Neon database is not paused/suspended

### 🔐 API Testing (Admin Token)
When testing the Backend via Swagger (`/docs`) or cURL, you can bypass login using the Master Admin Token.
*   **Token Value**: `admin_token`
*   **Usage**: In the "Authorize" box, type: `admin_token` (or `Bearer admin_token` in headers).
*   **Effect**: Grants immediate access as the `admin` user.


---

## 🏛️ Architecture & Standards
This project follows strict **Agentic Development** principles.

*   **Isolation**: Logic is separated into `src/cli`, `src/backend`, and `src/frontend`.
*   **SDD Loop**: All features are Spec-Driven. See `specs/` for architectural decisions.
*   **Security**: Use path/JWT based user isolation in all API endpoints.

---

## 📤 Pushing to GitHub

1. **Create Repository**: Go to GitHub and create a new repository (e.g., `evolution-of-todo`).

2. **Push Code**:
   ```powershell
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M master
   git push -u origin master
   ```

3. **Next Steps**: After pushing, you can deploy to Vercel (see deployment section above).