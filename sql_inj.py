# vulnerable_sql.py
import sqlite3

def get_user_profile(db_path, username):
    # BAD: building SQL by concatenating untrusted input
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT id, username, email FROM users WHERE username = '" + username + "';"
    cur.execute(query)              # <-- SQL injection possible here
    row = cur.fetchone()
    conn.close()
    return row

if __name__ == "__main__":
    db = "example.db"
    user = input("Enter username to look up: ")
    profile = get_user_profile(db, user)
    if profile:
        print("Found user:", profile)
    else:
        print("User not found")
