import mysql.connector
from database.db_connection import get_connection
import hashlib

def register_user(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    query = """
        INSERT INTO users (username, hashed_password, role)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (username, hashed_password, role))

    conn.commit()
    cursor.close()
    conn.close()
