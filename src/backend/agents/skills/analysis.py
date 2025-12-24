def analyze_sentiment(text: str) -> str:
    """Analyze the sentiment/urgency of a task description."""
    urgent_keywords = ["asap", "urgent", "deadline", "now", "immediately"]
    if any(word in text.lower() for word in urgent_keywords):
        return "High Priority"
    return "Normal Priority"

def suggest_tags(text: str) -> list[str]:
    """Suggest tags based on keywords."""
    tags = []
    text = text.lower()
    if "bug" in text or "fix" in text:
        tags.append("Development")
    if "meeting" in text or "call" in text:
        tags.append("Communication")
    if "buy" in text or "shop" in text:
        tags.append("Personal")
    return tags or ["General"]
