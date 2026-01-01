from database.db_connection import get_connection
import hashlib

def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    query = """
        SELECT * FROM users
        WHERE username=%s AND hashed_password=%s
    """
    cursor.execute(query, (username, hashed_password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user
