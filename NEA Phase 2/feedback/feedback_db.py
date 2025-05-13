# feedback/feedback_db.py
import sqlite3
from datetime import datetime
from feedback.feedback_model import FeedbackEntry

class FeedbackDB:
    def __init__(self, db_path="feedback.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            message TEXT NOT NULL,
            category TEXT NOT NULL,
            timestamp TEXT NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_feedback(self, entry: FeedbackEntry):
        query = """
        INSERT INTO feedback (username, message, category, timestamp)
        VALUES (?, ?, ?, ?);
        """
        self.conn.execute(query, (
            entry.username,
            entry.message,
            entry.category,
            entry.timestamp.isoformat()
        ))
        self.conn.commit()

    def get_all_feedback(self):
        cursor = self.conn.execute("SELECT username, message, category, timestamp FROM feedback;")
        return [
            FeedbackEntry(row[0], row[1], row[2], datetime.fromisoformat(row[3]))
            for row in cursor.fetchall()
        ]

    def close(self):
        self.conn.close()
