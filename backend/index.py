# ========== MODELS ==========
from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    
    tasks: List["Task"] = Relationship(back_populates="user")

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)
    
    user_id: str = Field(foreign_key="user.id", index=True)
    user: Optional[User] = Relationship(back_populates="tasks")

class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# ========== DATABASE ==========
import os
import logging
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, select
from sqlalchemy.pool import QueuePool, StaticPool

load_dotenv()
logger = logging.getLogger("api")

# Database URL should be in .env: 
# DATABASE_URL=postgresql://user:pass@ep-hostname.region.aws.neon.tech/dbname?sslmode=require
# USER PROVIDED FALLBACK:
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_zhJvIP74aTle@ep-long-waterfall-abcwopjg-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")

engine = None

if not DATABASE_URL:
    logger.warning("DATABASE_URL not found, falling back to in-memory SQLite")
    # Use in-memory SQLite for Vercel build/startup if no DB is provided
    DATABASE_URL = "sqlite://" 
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    try:
        engine = create_engine(
            DATABASE_URL,
            echo=True,
            poolclass=QueuePool,
        )
    except Exception as e:
        logger.error(f"Failed to create engine with DATABASE_URL: {e}")
        # Final fallback to memory
        DATABASE_URL = "sqlite://"
        engine = create_engine(
            DATABASE_URL,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )

def create_db_and_tables():
    if engine:
        try:
            SQLModel.metadata.create_all(engine)
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")

def get_session():
    if not engine:
        raise HTTPException(status_code=500, detail="Database engine not initialized")
    with Session(engine) as session:
        yield session

# ========== AUTH UTILS ==========
import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Shared secret between Frontend and Backend
# PREDEFINED FALLBACK: This key is used if BETTER_AUTH_SECRET is not set in environment variables.
BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET", "my_super_secure_hackathon_secret_key_2025")

security = HTTPBearer()

def verify_jwt(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Verifies the JWT token from Better Auth.
    Expects 'Authorization: Bearer <token>'
    Allows 'guest_token' for public demo access.
    """
    token = credentials.credentials
    
    # Guest & Admin Access Bypass for Hackathon Demo
    if token == "guest_token":
        return "guest_user"
    if token == "admin_token":
        return "admin"

    try:
        # Better Auth usually issues RS256 or HS256. 
        # For simplicity in this Hackathon project, we assume the shared secret HS256 flow.
        payload = jwt.decode(
            token, 
            BETTER_AUTH_SECRET, 
            algorithms=["HS256"],
            # Better Auth tokens might have specific audience settings, 
            # we keep it flexible for now or skip if verification is purely signature based.
            options={"verify_aud": False}
        )
        user_id = payload.get("sub") # 'sub' is standard for user ID in JWTs
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token missing user ID ('sub')",
            )
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

# ========== FASTAPI APP ==========
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="The Evolution of Todo - Phase II")

# Initialize database on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
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

@app.get("/api/health")
def health_check():
    db_status = "Not Initialized"
    if engine:
        try:
            with Session(engine) as session:
                session.exec(select(1))
            db_status = "Connected"
        except Exception as e:
            db_status = f"Error: {str(e)}"
    
    return {
        "status": "healthy",
        "database": db_status,
        "database_url_configured": bool(os.getenv("DATABASE_URL")),
        "python_version": os.sys.version
    }

# No handler needed for modern Vercel FastAPI support
# Vercel will automatically find the 'app' variable.
