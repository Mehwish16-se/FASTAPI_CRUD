import sqlite3

DB_NAME = "tasks.db"


def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
create_table()
def seed_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            ("Study FastAPI", 0)
        )

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            ("practise fastapi", 1)
        )

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            ("complete assigmant", 0)
        )

        conn.commit()

    conn.close()

seed_tasks()
create_table()