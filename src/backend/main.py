from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from typing import List
from database import create_db_and_tables, get_session
from models import Task, TaskCreate, TaskUpdate, User
from auth_utils import verify_jwt

app = FastAPI(title="The Evolution of Todo - Phase II")

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
    return {"message": "Welcome to Phase II Backend", "status": "Ready"}

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

# --- AGENT ENDPOINTS (PHASE III) ---
from agents.orchestrator import orchestrator
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
