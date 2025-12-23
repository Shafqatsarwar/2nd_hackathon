# The Evolution of Todo

This project documents the evolution of a software system from a simple CLI tool to a distributed cloud-native AI system.

## Currently in: Phase I
**Objective**: Build a command-line Todo application using Python 13+, UV, and Spec-Driven Development.

- **Phase I**: In-Memory Todo Console App (CLI)
- **Phase II**: Full-Stack Web App (FastAPI + Next.js + Neon DB)

## 📂 Project Structure (Phase II)

### 🐍 Backend (FastAPI)
```text
backend/
  ├── main.py        (API Endpoints & Startup hooks)
  ├── models.py      (SQLModel schemas)
  ├── database.py    (Connection & fallback logic)
  └── .env.example   (Neon/Auth configuration guide)
```

### ⚛️ Frontend (Next.js)
```text
frontend/
  ├── app/           (Pages & Layouts)
  ├── package.json   (Dependencies)
  └── tsconfig.json  (TypeScript Config)
```

## Project Structure
- `constitution.md`: The governing rules of the project.
- `specs/`: Detailed specifications and implementation plans.
- `src/`: Generated application source code.
- `.specify/`: Spec-Kit Plus infrastructure (templates, scripts, history).

## Prerequisites
- Python 3.13+
- [UV](https://github.com/astral-sh/uv)
- Claude Code (enabled via Spec-Kit Plus)

## Setup and Running (Phase I)
1. **Sync Dependencies**:
   ```bash
   uv sync
   ```
2. **Run Application**:
   ```bash
   uv run src/main.py
   ```

## Development Workflow
1. Write/Update specification in `specs/<feature>/spec.md`.
2. Generate plan in `specs/<feature>/plan.md`.
3. Implementation is handled by Claude Code following the tasks in `specs/<feature>/tasks.md`.

*Note: For Windows users, WSL 2 is required for local development as per the Constitution.*
