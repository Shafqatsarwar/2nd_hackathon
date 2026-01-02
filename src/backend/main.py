from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from typing import List, Dict, Any
from database import create_db_and_tables, get_session
from models import Task, TaskCreate, TaskUpdate, User
from auth_utils import verify_jwt
from mcp_config import get_mcp_config, is_mcp_enabled

app = FastAPI(title="The Evolution of Todo - Phase III")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In development, allow all - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Phase III Backend", "status": "Ready"}

# --- TASK CRUD ENDPOINTS ---

@app.get("/api/{user_id}/tasks", response_model=List[Task])
def list_tasks(
    user_id: str,
    token_user_id: str = Depends(verify_jwt),
    session: Session = Depends(get_session)
):
    if user_id != token_user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this user's tasks")

    tasks = session.exec(select(Task).where(Task.user_id == user_id)).all()
    return tasks

@app.post("/api/{user_id}/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,
    task: TaskCreate,
    token_user_id: str = Depends(verify_jwt),
    session: Session = Depends(get_session)
):
    if user_id != token_user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create tasks for this user")

    db_user = session.get(User, user_id)
    if not db_user:
        db_user = User(id=user_id, email=f"{user_id}@example.com")
        session.add(db_user)

    db_task = Task.model_validate(task, update={"user_id": user_id})
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@app.get("/api/{user_id}/tasks/{id}", response_model=Task)
def get_task(
    user_id: str,
    id: int,
    token_user_id: str = Depends(verify_jwt),
    session: Session = Depends(get_session)
):
    if user_id != token_user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    task = session.exec(select(Task).where(Task.id == id, Task.user_id == user_id)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/api/{user_id}/tasks/{id}", response_model=Task)
def update_task_all(
    user_id: str,
    id: int,
    task: TaskUpdate,
    token_user_id: str = Depends(verify_jwt),
    session: Session = Depends(get_session)
):
    if user_id != token_user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db_task = session.exec(select(Task).where(Task.id == id, Task.user_id == user_id)).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = task.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@app.patch("/api/{user_id}/tasks/{id}/complete", response_model=Task)
def toggle_task(
    user_id: str,
    id: int,
    token_user_id: str = Depends(verify_jwt),
    session: Session = Depends(get_session)
):
    if user_id != token_user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db_task = session.exec(select(Task).where(Task.id == id, Task.user_id == user_id)).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.completed = not db_task.completed
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@app.delete("/api/{user_id}/tasks/{id}")
def delete_task(
    user_id: str,
    id: int,
    token_user_id: str = Depends(verify_jwt),
    session: Session = Depends(get_session)
):
    if user_id != token_user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db_task = session.exec(select(Task).where(Task.id == id, Task.user_id == user_id)).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(db_task)
    session.commit()
    return {"ok": True}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


# --- MCP (Model Context Protocol) ENDPOINTS ---
@app.get("/mcp/ready")
def mcp_ready():
    """
    MCP readiness endpoint - indicates if MCP services are available
    """
    return {"ready": is_mcp_enabled()}


@app.get("/mcp/contexts")
def list_mcp_contexts():
    """
    List available MCP context providers
    """
    config = get_mcp_config()
    if not is_mcp_enabled():
        raise HTTPException(status_code=503, detail="MCP services are not enabled")

    return {"contexts": config.MCP_CONTEXT_PROVIDERS}


@app.get("/mcp/contexts/todo-context")
def get_todo_context():
    """
    Provide context about the todo application structure and current state
    """
    if not is_mcp_enabled():
        raise HTTPException(status_code=503, detail="MCP services are not enabled")

    # Return information about the todo app structure
    return {
        "description": "Todo application context",
        "endpoints": [
            "GET /api/{user_id}/tasks",
            "POST /api/{user_id}/tasks",
            "GET /api/{user_id}/tasks/{id}",
            "PUT /api/{user_id}/tasks/{id}",
            "PATCH /api/{user_id}/tasks/{id}/complete",
            "DELETE /api/{user_id}/tasks/{id}"
        ],
        "authentication": "JWT tokens from Better Auth",
        "database": "PostgreSQL with SQLModel ORM",
        "features": [
            "Add Task (Title and Description)",
            "View Task List (with Status indicators)",
            "Update Task Details",
            "Delete Task by ID",
            "Mark Task as Complete/Incomplete"
        ]
    }


@app.get("/mcp/contexts/database-context")
def get_database_context():
    """
    Provide database schema context for the todo application
    """
    if not is_mcp_enabled():
        raise HTTPException(status_code=503, detail="MCP services are not enabled")

    # Return database schema information
    return {
        "description": "Database schema context",
        "tables": {
            "tasks": {
                "columns": [
                    {"name": "id", "type": "Integer", "primary_key": True},
                    {"name": "title", "type": "String", "required": True},
                    {"name": "description", "type": "String", "required": False},
                    {"name": "completed", "type": "Boolean", "default": False},
                    {"name": "user_id", "type": "String", "required": True},
                    {"name": "created_at", "type": "DateTime", "required": False}
                ]
            },
            "users": {
                "columns": [
                    {"name": "id", "type": "String", "primary_key": True},
                    {"name": "email", "type": "String", "required": True}
                ]
            }
        },
        "database_type": "PostgreSQL",
        "orm": "SQLModel"
    }


@app.get("/mcp/contexts/auth-context")
def get_auth_context():
    """
    Provide authentication system context
    """
    if not is_mcp_enabled():
        raise HTTPException(status_code=503, detail="MCP services are not enabled")

    return {
        "description": "Authentication system context",
        "provider": "Better Auth",
        "method": "JWT-based authentication",
        "user_flow": [
            "User registers/signs in via frontend",
            "JWT token is issued by Better Auth",
            "Token is sent with requests to backend",
            "Backend verifies JWT signature using shared secret",
            "User ID is extracted from token for authorization"
        ],
        "shared_secret": "BETTER_AUTH_SECRET environment variable",
        "token_format": "HS256 JWT with 'sub' claim containing user ID"
    }


# --- AGENT ENDPOINTS (PHASE III) ---
try:
    from agents.orchestrator import orchestrator
except ImportError:
    # Fallback for when running directly
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))
    from orchestrator import orchestrator
from pydantic import BaseModel

class AgentRequest(BaseModel):
    query: str = "Fix the login bug asap"
    context: str = "task"

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "query": "Buy milk and eggs",
                    "context": "task"
                }
            ]
        }
    }

@app.post("/api/agent/consult")
def consult_agent(request: AgentRequest):
    """
    Direct interface to the Backend Agent System.
    """
    return orchestrator.delegate(request.query, request.context)


# --- PHASE III: AI-POWERED CHATBOT ENDPOINTS ---
try:
    from agents.skills.mcp_agent_interface import mcp_todo_agent
except ImportError:
    # Fallback for when running directly
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), 'agents', 'skills'))
    from mcp_agent_interface import mcp_todo_agent
from pydantic import BaseModel


class AICommandRequest(BaseModel):
    user_id: str
    command: str
    parameters: dict = {}


@app.post("/api/ai/command")
def execute_ai_command(request: AICommandRequest):
    """
    Execute a command from the AI chatbot using MCP tools.
    All actions go through MCP tools as required by Phase III architecture.
    """
    return mcp_todo_agent.process_command(
        user_id=request.user_id,
        command=request.command,
        params=request.parameters
    )


class NaturalLanguageRequest(BaseModel):
    user_id: str
    query: str


@app.post("/api/ai/chat")
def chat_with_ai_assistant(request: NaturalLanguageRequest):
    """
    Natural language interface for the AI-powered todo chatbot.
    Uses NLP to understand user intent and executes appropriate actions via MCP tools.
    """
    # Use the orchestrator to parse the natural language
    result = orchestrator.delegate(request.query, context="nlp")

    # Extract intent and potentially execute it via MCP tools
    intent_data = result.get("intent_parsed", {})
    intent = intent_data.get("intent", "unknown")

    # For now, return the parsed intent - in a full implementation,
    # this would execute the appropriate MCP tool based on the intent
    return {
        "user_id": request.user_id,
        "original_query": request.query,
        "parsed_intent": intent_data,
        "action_taken": f"Intent '{intent}' recognized, ready for MCP tool execution"
    }
