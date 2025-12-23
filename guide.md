# Phase I Execution Guide: The Evolution of Todo

This guide contains all necessary commands to run, test, and maintain the Phase I Python CLI application.

## 🚀 Environment Setup

### Sync Dependencies
Use this command to ensure your local virtual environment is up to date based on `pyproject.toml`.
```powershell
uv sync
```

### Activate Virtual Environment (Optional)
```powershell
. .venv/Scripts/activate
```

## 💻 Running the Application

### Start the CLI Application
Run the interactive Todo manager.
```powershell
uv run src/main.py
```

## 🧪 Testing and Verification

### Run Automated Component Tests
Executes the full test suite (Add, View, Update, Delete, Toggle) non-interactively.
```powershell
uv run python -m src.test_core
```

## 🛠️ Project Maintenance

### Adding a New Feature (Spec-Kit Workflow)
1. **Initialize Feature**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .specify/scripts/powershell/create-new-feature.ps1 -ShortName "feature-name" "Full Description"
   ```
2. **Setup Implementation Plan**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .specify/scripts/powershell/setup-plan.ps1
   ```

### Prompt History Capture
Every interaction is documented in:
`history/prompts/<category>/<id>-<slug>.<stage>.prompt.md`

## 🌐 Phase II: Full-Stack Web App

Phase II involves a **FastAPI** backend and a **Next.js** frontend.

### 🐍 Backend (FastAPI) Setup
The backend is structured for persistence and multi-user isolation.

**Directory Structure**:
```text
backend/
  ├── main.py        (API Endpoints & Startup hooks)
  ├── models.py      (SQLModel schemas)
  ├── database.py    (Connection & fallback logic)
  └── .env.example   (Neon/Auth configuration guide)
```

1. **Initialize Environment**:
   ```powershell
   cd backend
   uv sync
   ```
2. **Run Backend**:
   ```powershell
   uv run uvicorn main:app --reload
   ```

### 🧪 Testing the API (CRUD)
FastAPI provides an automatic interactive documentation page.
1. Run the backend.
2. Open your browser to: `http://127.0.0.1:8000/docs`
3. You can test **Add, List, Update, and Delete** directly from this UI.
   - Use any string for `user_id` (e.g., `user123`) to test isolation.

### ⚛️ Frontend (Next.js) Setup
**IMPORTANT: Do NOT use Turbopack (`--turbo`).**
1. **Initialize Project**:
   ```powershell
   cd frontend
   npx create-next-app@latest . --typescript --eslint --tailwind --no-src-dir --app --import-alias "@/*"
   ```
2. **Install Better Auth**:
   ```powershell
   npm install better-auth
   ```
3. **Run Frontend**:
   ```powershell
   npm run dev
   ```

## 🛠️ Package Management (Standard)

### Adding Packages
- **Frontend**: `npm install <package-name>`
- **Backend**: `uv add <package-name>`

### Removing Packages
- **Frontend**: `npm uninstall <package-name>`
- **Backend**: `uv remove <package-name>`

### Testing
- **Frontend**: `npm test`
- **Backend**: `uv run pytest`

## ☁️ Cloud Credentials Setup

To move from local SQLite to Neon PostgreSQL and enable secure Auth, follow these steps:

### 1. Get Neon PostgreSQL (DATABASE_URL)
1. Go to [neon.tech](https://neon.tech) and sign up/in.
2. Create a new project (e.g., `todo-evolution`).
3. On the Dashboard, find the **Connection String** section.
4. Select **Pooled Connection** (recommended for serverless).
5. Copy the URL (starts with `postgresql://...`).
6. Create a file `backend/.env` and add:
   ```env
   DATABASE_URL=your_copied_connection_string
   ```

### 2. Generate Better Auth Secret (BETTER_AUTH_SECRET)
This secret is used to sign and verify JWT tokens between the Frontend and Backend.
1. It should be a long, random string.
2. You can generate one using:
   - **Linux/WSL**: `openssl rand -base64 32`
   - **PowerShell**: `[Convert]::ToBase64String((1..32 | % { [byte](Get-Random -Minimum 0 -Maximum 255) }))`
3. Add it to your `backend/.env`:
   ```env
   BETTER_AUTH_SECRET=your_generated_random_string
   ```
4. **Important**: Use the same secret in the Frontend configuration later.

---

## 🧯 Troubleshooting
- **Turbopack Issues**: If the frontend crashes or displays strange errors, verify you are NOT using `npm run dev -- --turbo`.
- **Windows Compatibility**: Use `-binary` versions of Python packages (e.g., `psycopg2-binary`) to avoid local compilation issues.
- **Port Conflicts**: FastAPI usually runs on port `8000`, Next.js on `3000`.
- **ModuleNotFoundError: No module named 'src'**: Always run commands from the project root. Ensure you use `python -m src.test_core` to correctly resolve imports.
- **Python Version**: Ensure Python 3.13+ is installed. `uv` manages the local version.
- **Permission Errors**: If PowerShell scripts fail, use `-ExecutionPolicy Bypass`.
