import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_DIR, "database.db")
MAX_PER_PROBLEM = 3
NUM_PROBLEMS = 20

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database() -> None:
    os.makedirs(APP_DIR, exist_ok=True)
    conn = get_db_connection()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS selections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                problem_id INTEGER NOT NULL CHECK (problem_id BETWEEN 1 AND 20)
            );
            """
        )
        conn.commit()
    finally:
        conn.close()
app = Flask(__name__)
initialize_database()
@app.get("/")
def index():
    counts = read_problem_counts()
    status = request.args.get("status")
    message = request.args.get("message")
    return render_template(
        "index.html",
        counts=counts,
        max_per_problem=MAX_PER_PROBLEM,
        num_problems=NUM_PROBLEMS,
        status=status,
        message=message,
    )

def read_problem_counts() -> dict:
    counts = {i: 0 for i in range(1, NUM_PROBLEMS + 1)}
    conn = get_db_connection()
    try:
        cur = conn.execute(
            "SELECT problem_id, COUNT(*) as cnt FROM selections GROUP BY problem_id"
        )
        for row in cur.fetchall():
            counts[int(row["problem_id"])] = int(row["cnt"])
    finally:
        conn.close()
    return counts

@app.post("/select")
def select():
    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    problem_id_raw = (request.form.get("problem_id") or "").strip()
    try:
        problem_id = int(problem_id_raw)
    except ValueError:
        return redirect(
            url_for(
                "index",
                status="error",
                message="Invalid problem selection.",
            )
        )
    if not name or not email or not (1 <= problem_id <= NUM_PROBLEMS):
        return redirect(
            url_for(
                "index",
                status="error",
                message="Please complete all fields with a valid selection.",
            )
        )
    conn = get_db_connection()
    try:
        cur = conn.execute(
            "SELECT COUNT(*) as cnt FROM selections WHERE problem_id = ?",
            (problem_id,),
        )
        current_count = int(cur.fetchone()["cnt"])
        if current_count >= MAX_PER_PROBLEM:
            return redirect(
                url_for(
                    "index",
                    status="error",
                    message="This problem statement is already full. Please choose another.",
                )
            )
        conn.execute(
            "INSERT INTO selections (name, email, problem_id) VALUES (?, ?, ?)",
            (name, email, problem_id),
        )
        conn.commit()
    finally:
        conn.close()
    return redirect(
        url_for(
            "index",
            status="success",
            message="Your selection has been saved successfully!",
        )
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)


