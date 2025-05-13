# leaderboard/leaderboard_model.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LeaderboardEntry:
    player_name: str
    score: int
    mode: str
    width: int
    height: int
    date: datetime
