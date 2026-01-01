import mysql.connector

# Connect to MySQL Server using project_user
conn = mysql.connector.connect(
    host="localhost",
    user="project_user",
    password="project123"
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS client_query_db")
cursor.execute("USE client_query_db")

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    hashed_password VARCHAR(256),
    role VARCHAR(20)
)
""")

# Create queries table
cursor.execute("""
CREATE TABLE IF NOT EXISTS queries (
    query_id VARCHAR(20) PRIMARY KEY,
    client_email VARCHAR(150),
    client_mobile VARCHAR(15),
    query_heading VARCHAR(255),
    query_description TEXT,
    status VARCHAR(20),
    query_created_time DATETIME,
    query_closed_time DATETIME
)
""")

conn.commit()
cursor.close()
conn.close()

print("Database and tables created successfully")
