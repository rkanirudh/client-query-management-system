import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rkas@2005",   # ← put your real MySQL password
        database="client_query_db"
    )
