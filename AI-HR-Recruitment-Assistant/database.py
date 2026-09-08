import sqlite3

DB_NAME = "recruitment.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT, phone TEXT, skills TEXT,
        experience TEXT, resume_file TEXT,
        score REAL DEFAULT 0, status TEXT DEFAULT 'Pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT, description TEXT, skills TEXT, experience TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS interviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_id INTEGER, interview_date TEXT,
        interview_time TEXT, interviewer TEXT,
        status TEXT DEFAULT 'Scheduled'
    )""")
    conn.commit()
    conn.close()

def add_candidate(name, email, phone, skills, experience, resume_file):
    conn = get_connection()
    conn.execute("""INSERT INTO candidates
        (name,email,phone,skills,experience,resume_file)
        VALUES (?,?,?,?,?,?)""",
        (name,email,phone,skills,experience,resume_file))
    conn.commit()
    conn.close()

def get_candidates():
    conn = get_connection()
    rows = conn.execute("""SELECT id,name,email,phone,skills,experience,score,status
                           FROM candidates ORDER BY score DESC""").fetchall()
    conn.close()
    return rows

def add_job(title, description, skills, experience):
    conn = get_connection()
    conn.execute("""INSERT INTO jobs (title,description,skills,experience)
                    VALUES (?,?,?,?)""",
                 (title,description,skills,experience))
    conn.commit()
    conn.close()

def get_jobs():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM jobs ORDER BY id DESC").fetchall()
    conn.close()
    return rows
