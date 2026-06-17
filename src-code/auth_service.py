import sqlite3

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # FIX: parameterized query
    query = """
    SELECT id, username, role
    FROM users
    WHERE username = ?
    AND password = ?
    """

    cursor.execute(query, (username, password))
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