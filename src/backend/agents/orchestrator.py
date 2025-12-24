from .subagents.task_agent import TaskAgent

class AgentOrchestrator:
    """
    Main entry point for the Agentic System.
    Routes requests to appropriate subagents.
    """
    def __init__(self):
        self.task_agent = TaskAgent()
        # Future: Add PlanningAgent, ReviewAgent etc.

    def delegate(self, query: str, context: str = "task") -> dict:
        if context == "task":
            return self.task_agent.process_task_input(query)
        else:
            return {"error": "No suitable agent found for this context."}

# Global Instance
orchestrator = AgentOrchestrator()
