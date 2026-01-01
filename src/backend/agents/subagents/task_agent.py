from ..skills.analysis import analyze_sentiment, suggest_tags

class TaskAgent:
    """A specialized subagent for Task Management."""
    
    def __init__(self, name="TaskBot"):
        self.name = name

    def process_task_input(self, description: str) -> dict:
        """
        Processes a raw task input and returns structured data.
        Example: "Fix the bug asap" -> {"priority": "High", "tags": ["Dev"]}
        """
        priority = analyze_sentiment(description)
        tags = suggest_tags(description)
        
        return {
            "processed_by": self.name,
            "original_text": description,
            "suggested_priority": priority,
            "suggested_tags": tags,
            "enhancement": f"Processed via {self.name} Core"
        }
