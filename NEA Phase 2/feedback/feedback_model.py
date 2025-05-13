# feedback/feedback_model.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class FeedbackEntry:
    username: str
    message: str
    category: str  # e.g., Bug, Suggestion, Praise
    timestamp: datetime
