import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.pool import QueuePool

load_dotenv()

# Database URL should be in .env: 
# DATABASE_URL=postgresql://user:pass@ep-hostname.region.aws.neon.tech/dbname?sslmode=require
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Fallback for local development if Neon URL is not provided
    DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    poolclass=QueuePool,
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
