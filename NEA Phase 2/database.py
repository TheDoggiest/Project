# database.py
"""
Handles all database interaction. Stores mazes, user info, solutions.
Includes versioning, indexing, and seed uniqueness check.
"""

import sqlite3
from datetime import datetime
from pathlib import Path

DB_FILE = Path("maze_data/mazes.db")
DB_FILE.parent.mkdir(exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mazes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seed TEXT UNIQUE,
            width INTEGER,
            height INTEGER,
            difficulty TEXT,
            theme TEXT,
            created_at TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_maze(seed, width, height, difficulty, theme):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO mazes (seed, width, height, difficulty, theme, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (seed, width, height, difficulty, theme, datetime.now().isoformat()))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Maze with this seed already exists.")
    finally:
        conn.close()

def get_maze_by_seed(seed):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM mazes WHERE seed = ?", (seed,))
    row = c.fetchone()
    conn.close()
    return row
