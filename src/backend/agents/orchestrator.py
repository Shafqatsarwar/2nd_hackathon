from .subagents.task_agent import TaskAgent
from .subagents.nlp_agent import NLPAgent

class AgentOrchestrator:
    """
    Main entry point for the Agentic System.
    Routes requests to appropriate subagents.
    """
    def __init__(self):
        self.task_agent = TaskAgent()
        self.nlp_agent = NLPAgent()
        # Future: Add PlanningAgent, ReviewAgent etc.

    def delegate(self, query: str, context: str = "task") -> dict:
        if context == "nlp" or context == "chat":
            # Use NLP agent for natural language processing
            intent_data = self.nlp_agent.parse_intent(query)
            return {
                "intent_parsed": intent_data,
                "enhancement": "AI-mediated intent processing"
            }
        elif context == "task":
            return self.task_agent.process_task_input(query)
        else:
            return {"error": "No suitable agent found for this context."}

# Global Instance
orchestrator = AgentOrchestrator()
