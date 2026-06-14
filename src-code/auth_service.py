# auth_service.py

import sqlite3

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # VULNERABILITY: SQL injection via string concatenation
    query = f"""
    SELECT id, username, role
    FROM users
    WHERE username = '{username}'
    AND password = '{password}'
    """

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        user_id, user, role = result
        return {
            "id": user_id,
            "username": user,
            "role": role,
            "authenticated": True
        }

    return {"authenticated": False}