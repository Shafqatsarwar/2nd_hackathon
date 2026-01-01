# Constitution: The Evolution of Todo

## Project Overview
This project simulates the real-world evolution of software, starting from a simple Python CLI tool and evolving into a Kubernetes-managed, event-driven, AI-powered distributed system.

## Core Mandates
1. **Spec-Driven Development (SDD)**: All development MUST start with a specification.
2. **Process**: Write Spec → Generate Plan → Break into Tasks → Implement via Claude Code.
3. **No Manual Code**: Human editing of generated source code in `src/` is strictly prohibited.
4. **Agentic Dev Stack**: Primarily using Claude Code and Spec-Kit Plus.

---

## Phase I: Todo In-Memory Python Console App
**Objective**: Build a command-line todo application that stores tasks in memory.

### Requirements
- **Features**: Implement 5 Basic Level features:
  1. Add Task (Title and Description)
  2. View Task List (with Status indicators)
  3. Update Task Details
  4. Delete Task by ID
  5. Mark Task as Complete/Incomplete
- **Deployment**: Local execution using Python 3.13+ and UV.
- **Data**: In-memory storage only.

### Technology Stack (Phase I)
- **Runtime**: Python 3.13+
- **Package Manager**: UV
- **Tools**: Claude Code, Spec-Kit Plus

### Deliverables (Phase I)
- `constitution.md`: Project principles (this file).
- `/specs/`: Specification history folder containing all specification files.
- `/src/`: Python source code (generated only).
- `README.md`: Setup instructions.
- `CLAUDE.md`: Claude Code usage instructions.

---

## Phase II: Todo Full-Stack Web Application
**Objective**: Transform the console app into a multi-user web application with persistent storage and authentication.

### Requirements
- **Features**: All 5 Basic Level features implemented as a web application.
- **Architecture**: RESTful API backend, Responsive frontend.
- **Storage**: Neon Serverless PostgreSQL.
- **Authentication**: User signup/signin using Better Auth (JWT-based).

### Technology Stack (Phase II)
- **Frontend**: Next.js 16+ (App Router)
- **Backend**: Python FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth (Shared Secret JWT)
- **AI Tools**: Claude Code + Spec-Kit Plus

### API Endpoints (Phase II)
- `GET /api/{user_id}/tasks`: List all tasks
- `POST /api/{user_id}/tasks`: Create a new task
- `GET /api/{user_id}/tasks/{id}`: Get task details
- `PUT /api/{user_id}/tasks/{id}`: Update a task
- `DELETE /api/{user_id}/tasks/{id}`: Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete`: Toggle completion

---

## Development Environment (Windows Users)
Windows users MUST use WSL 2 (Ubuntu 22.04) for consistency.
- `wsl --install`
- `wsl --set-default-version 2`
- `wsl --install -d Ubuntu-22.04`

---

## Repository Structure
```
/
├── history/           # Prompt History Records (PHR) and ADRs
├── .specify/
│   ├── templates/     # Spec-Kit Plus templates
│   └── scripts/       # Automation scripts
├── specs/             # Feature specifications and plans
├── src/               # Generated source code
├── constitution.md
├── README.md
├── CLAUDE.md
└── pyproject.toml
```
