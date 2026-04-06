import sqlite3
import os
from datetime import datetime
from contextlib import contextmanager

DB_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DB_PATH = os.path.join(DB_DIR, "bot.db")

def ensure_db_dir():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR, exist_ok=True)

@contextmanager
def get_db():
    ensure_db_dir()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_seen TEXT
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                text TEXT,
                direction TEXT,
                timestamp TEXT
            )
        ''')

def save_user(user_id, username, first_name):
    with get_db() as db:
        db.execute('''
            INSERT OR REPLACE INTO users (user_id, username, first_name, last_seen)
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, first_name, datetime.now().isoformat()))

def get_user(user_id):
    with get_db() as db:
        return db.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()

def save_message(user_id, text, direction):
    with get_db() as db:
        db.execute('''
            INSERT INTO messages (user_id, text, direction, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (user_id, text, direction, datetime.now().isoformat()))