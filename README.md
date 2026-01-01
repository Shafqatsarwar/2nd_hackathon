# 🚀 The Evolution of Todo - Spec-Driven Cloud-Native AI Todo System

This project implements Hackathon II: The Evolution of Todo using Spec-Driven Development and AI-Native Architecture.

The system evolves from a simple in-memory CLI to a cloud-native, event-driven, AI-powered Todo platform, without manual coding.
The engineer's role is system architect, not syntax writer.

## 🌟 Key Principles

**Golden Rule:**
❌ No handwritten application code
✅ All code is generated via Claude Code from validated specs

## 🏗️ Current Phase: Phase II - Full-Stack Web Application
- **Frontend**: Next.js 16+ (App Router) with Better Auth
- **Backend**: Python FastAPI with PostgreSQL
- **Authentication**: Better Auth (JWT-based)
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **AI Integration**: MCP-powered assistant capabilities

## 🚀 Phases

### Phase I: In-Memory Console Application
- Proved mastery of **Spec-Driven Development** without framework noise
- Single-process, in-memory state only
- Core features: Add, Update, Delete, List, Toggle completion

### Phase II: Full-Stack Web Application (Current)
- Multi-user, persistent, authenticated architecture
- Frontend and backend are isolated services
- Backend is the system of record
- Frontend never directly accesses database

### Phase III: AI-Powered Todo Chatbot (Next)
- Replace UI-driven CRUD with **AI-mediated intent**
- Stateless backend
- AI agents never access DB directly
- All actions go through MCP tools

### Phase IV: Local Kubernetes Deployment
- Prove the system is **cloud-native**, not cloud-hosted
- Containers are immutable
- Config via environment variables
- Infrastructure defined declaratively

### Phase V: Advanced Cloud-Native Deployment
- Evolve into a **distributed, event-driven AI system**
- Asynchronous over synchronous
- Loose coupling via events
- Infrastructure abstraction via Dapr

## 📁 Repository Structure
For detailed information about the directory structure, see [structure.md](./structure.md).

````
.
├── .spec-kit/              # Spec-Kit configuration
│   └── config.yaml
├── .specify/               # Constitution files
│   └── constitution/
├── specs/                  # Feature specifications
├── src/
│   ├── cli/               # Phase I CLI App
│   ├── backend/           # Phase II FastAPI service
│   └── frontend/          # Phase II Next.js application
├── history/               # Prompt History Records (PHR)
│   └── prompts/
│       ├── general/
│       ├── phase-ii/
│       └── phase-iii/     # Phase III history (newly created)
├── api/                   # Vercel serverless entry point
├── scripts/               # Database initialization scripts
└── vercel.json            # Vercel routing configuration
````

## 🛠️ Quick Start

### 1. Install Dependencies
```bash
# Install Python dependencies
cd src/backend
uv sync --dev  # or pip install -r requirements.txt

# Install Node.js dependencies
cd ../frontend
npm install
```

### 2. Set Up Environment Variables
Create `.env` files in both backend and frontend directories with the required configuration.

### 3. Run Database Migrations
```bash
cd src/frontend
npm run db:migrate
```

### 4. Start the Backend
```bash
cd src/backend
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Start the Frontend
```bash
cd src/frontend
npm run dev
```

For detailed setup and deployment instructions, see [guide.md](./guide.md).

## 🤖 MCP (Model Context Protocol) Integration
The backend includes MCP endpoints for AI assistant integration:
- `/mcp/ready` - MCP readiness check
- `/mcp/contexts` - List available contexts
- `/mcp/contexts/todo-context` - Todo application context
- `/mcp/contexts/database-context` - Database schema context
- `/mcp/contexts/auth-context` - Authentication system context

## 🚀 Deployment Architecture

This project uses a **unified deployment** approach on Vercel:
- **Frontend & Backend Combined**: Both deployed as a single Vercel application
- **`api/index.py`**: Bridges Vercel serverless functions to FastAPI backend
- **`vercel.json`**: Routes `/api/*` requests to Python backend, all other routes to Next.js
- **Result**: Single URL serves both frontend UI and backend API

**Live Endpoints** (after deployment):
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-app.vercel.app/api/*`
- API Docs: `https://your-app.vercel.app/docs`

See [guide.md](./guide.md) for complete deployment instructions.
