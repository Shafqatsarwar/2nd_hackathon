from typing import Dict, Any
import re


class NLPAgent:
    """Natural Language Processing Agent for understanding user intents."""

    def __init__(self, name="NLPTaskBot"):
        self.name = name
        self.action_keywords = {
            'create': ['add', 'create', 'make', 'new', 'build', 'setup'],
            'update': ['update', 'change', 'modify', 'edit', 'fix', 'adjust'],
            'delete': ['delete', 'remove', 'cancel', 'kill', 'destroy'],
            'complete': ['complete', 'finish', 'done', 'mark done', 'accomplish'],
            'list': ['list', 'show', 'display', 'view', 'see', 'get']
        }

    def parse_intent(self, text: str) -> Dict[str, Any]:
        """
        Parse natural language input to extract intent and parameters.
        Example: "Add a task to buy groceries" -> {"action": "create", "task": "buy groceries"}
        """
        text_lower = text.lower().strip()
        intent = self._identify_intent(text_lower)
        parameters = self._extract_parameters(text_lower, intent)

        return {
            "intent": intent,
            "parameters": parameters,
            "original_text": text,
            "processed_by": self.name
        }

    def _identify_intent(self, text: str) -> str:
        """Identify the user's intent from the text."""
        for action, keywords in self.action_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return action
        # Default to create if no specific intent found
        return "create"

    def _extract_parameters(self, text: str, intent: str) -> Dict[str, Any]:
        """Extract parameters like task title, description, etc. from the text."""
        params = {}

        # Remove action keywords to get the task content
        clean_text = text
        for keywords in self.action_keywords.values():
            for keyword in keywords:
                clean_text = clean_text.replace(keyword, "").strip()

        # Clean up common phrases
        clean_text = re.sub(r'^(a |the |an )', '', clean_text)
        clean_text = re.sub(r'^to ', '', clean_text)
        clean_text = clean_text.strip()

        if clean_text:
            params["title"] = clean_text
            params["description"] = f"Natural language command: {text}"

        return params