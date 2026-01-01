"""
MCP Agent Interface for Phase III AI Integration
Provides standardized interfaces for AI agents to interact with the system
"""
from typing import Dict, Any, Optional
from .todo_mcp_tools import todo_mcp_tools


class MCPTodoAgentInterface:
    """
    MCP Interface for AI Todo Agent
    Provides standardized methods for AI agents to interact with the todo system
    following MCP protocols for Phase III.
    """

    def __init__(self):
        self.tools = todo_mcp_tools

    def process_command(self, user_id: str, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process a command from an AI agent using MCP tools.
        """
        if params is None:
            params = {}

        command = command.lower().strip()

        if command == "list_tasks":
            status = params.get("status", "all")
            result = self.tools.list_tasks(user_id, status)
            return {
                "action": "list",
                "result": result,
                "status": "success"
            }
        elif command == "create_task":
            title = params.get("title", "Untitled Task")
            description = params.get("description", "")
            result = self.tools.create_task(user_id, title, description)
            return {
                "action": "create",
                "result": result,
                "status": result.get("status", "success")
            }
        elif command == "update_task":
            task_id = params.get("task_id")
            title = params.get("title")
            description = params.get("description")
            result = self.tools.update_task(user_id, task_id, title, description)
            return {
                "action": "update",
                "result": result,
                "status": result.get("status", "success")
            }
        elif command == "complete_task":
            task_id = params.get("task_id")
            result = self.tools.complete_task(user_id, task_id)
            return {
                "action": "complete",
                "result": result,
                "status": result.get("status", "success")
            }
        elif command == "delete_task":
            task_id = params.get("task_id")
            result = self.tools.delete_task(user_id, task_id)
            return {
                "action": "delete",
                "result": result,
                "status": result.get("status", "success")
            }
        else:
            return {
                "action": command,
                "result": {"error": f"Unknown command: {command}"},
                "status": "error"
            }


# Global instance
mcp_todo_agent = MCPTodoAgentInterface()