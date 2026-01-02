"""
MCP Tools for AI Agent Integration
These tools allow AI agents to interact with the todo system through standardized interfaces.
All actions go through MCP tools as required by Phase III architecture.
"""
from typing import List, Dict, Any, Optional
from sqlmodel import Session, select
try:
    from ..models import Task, User, TaskCreate, TaskUpdate
    from ..database import get_session
except (ImportError, ValueError):
    # Fallback for direct execution
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from models import Task, User, TaskCreate, TaskUpdate
    from database import get_session


class TodoMCPTasks:
    """
    MCP Tools for Task Management
    All actions are stateless and idempotent where possible
    """

    def __init__(self, session_getter=None):
        # Import the database module to get the session
        if session_getter is None:
            # Store a reference to the get_session function
            try:
                from ..database import get_session
                self.get_session_func = get_session
            except (ImportError, ValueError):
                # Fallback for direct execution
                import sys
                import os
                sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
                from database import get_session
                self.get_session_func = get_session

            # Define a method to get the session
            def get_session_method():
                # Get the session from the generator
                session_generator = self.get_session_func()
                session = next(session_generator)
                return session
            self.get_session = get_session_method
        else:
            self.get_session = session_getter

    def list_tasks(self, user_id: str, status: str = "all") -> List[Dict[str, Any]]:
        """
        List all tasks for a specific user.
        MCP Tool for AI agents to retrieve user's tasks.
        """
        with self.get_session() as session:
            query = select(Task).where(Task.user_id == user_id)

            if status == "pending":
                query = query.where(Task.completed == False)
            elif status == "completed":
                query = query.where(Task.completed == True)

            tasks = session.exec(query).all()

            return [
                {
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "completed": task.completed
                }
                for task in tasks
            ]

    def create_task(self, user_id: str, title: str, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new task for a user.
        MCP Tool for AI agents to create tasks.
        """
        # Get the session generator and extract the session
        session_gen = self.get_session_func()
        session = next(session_gen)
        try:
            task_data = TaskCreate(title=title, description=description or "")
            db_task = Task.model_validate(task_data, update={"user_id": user_id})
            session.add(db_task)
            session.commit()
            session.refresh(db_task)

            return {
                "task_id": db_task.id,
                "status": "created",
                "title": db_task.title,
                "description": db_task.description,
                "completed": db_task.completed
            }
        finally:
            # Close the session properly
            session.close()

    def update_task(self, user_id: str, task_id: int, title: Optional[str] = None,
                    description: Optional[str] = None) -> Dict[str, Any]:
        """
        Update an existing task.
        MCP Tool for AI agents to modify tasks.
        """
        session_gen = self.get_session_func()
        session = next(session_gen)
        try:
            db_task = session.exec(
                select(Task).where(Task.id == task_id, Task.user_id == user_id)
            ).first()

            if not db_task:
                return {
                    "error": f"Task {task_id} not found for user {user_id}",
                    "status": "error"
                }

            if title is not None:
                db_task.title = title
            if description is not None:
                db_task.description = description

            session.add(db_task)
            session.commit()
            session.refresh(db_task)

            return {
                "task_id": db_task.id,
                "status": "updated",
                "title": db_task.title
            }
        finally:
            session.close()

    def complete_task(self, user_id: str, task_id: int) -> Dict[str, Any]:
        """
        Mark a task as completed.
        MCP Tool for AI agents to toggle task completion.
        """
        session_gen = self.get_session_func()
        session = next(session_gen)
        try:
            db_task = session.exec(
                select(Task).where(Task.id == task_id, Task.user_id == user_id)
            ).first()

            if not db_task:
                return {
                    "error": f"Task {task_id} not found for user {user_id}",
                    "status": "error"
                }

            db_task.completed = True
            session.add(db_task)
            session.commit()
            session.refresh(db_task)

            return {
                "task_id": db_task.id,
                "status": "completed",
                "title": db_task.title
            }
        finally:
            session.close()

    def delete_task(self, user_id: str, task_id: int) -> Dict[str, Any]:
        """
        Delete a task.
        MCP Tool for AI agents to remove tasks.
        """
        session_gen = self.get_session_func()
        session = next(session_gen)
        try:
            db_task = session.exec(
                select(Task).where(Task.id == task_id, Task.user_id == user_id)
            ).first()

            if not db_task:
                return {
                    "error": f"Task {task_id} not found for user {user_id}",
                    "status": "error"
                }

            session.delete(db_task)
            session.commit()

            return {
                "task_id": task_id,
                "status": "deleted",
                "title": db_task.title
            }
        finally:
            session.close()


# Global instance of the MCP tools (using default session getter)
todo_mcp_tools = TodoMCPTasks()