import pandas as pd
from datetime import datetime
from database.db_connection import get_connection
import os

# ----------------------------------
# RESOLVE CSV PATH SAFELY
# ----------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "synthetic_client_queries.csv")

print("📂 Loading CSV from:", CSV_PATH)

# Load dataset
df = pd.read_csv(CSV_PATH)

# ----------------------------------
# BASIC CLEANING
# ----------------------------------
df = df.dropna(subset=["query_id", "client_email", "query_heading"])
df["client_mobile"] = df["client_mobile"].astype(str)
df["query_description"] = df["query_description"].fillna("No description")

# ----------------------------------
# ADD SYSTEM COLUMNS
# ----------------------------------
df["status"] = "Open"
df["query_created_time"] = datetime.now()
df["query_closed_time"] = None

# ----------------------------------
# INSERT INTO DATABASE
# ----------------------------------
conn = get_connection()
cursor = conn.cursor()

insert_query = """
INSERT INTO queries (
    query_id,
    client_email,
    client_mobile,
    query_heading,
    query_description,
    status,
    query_created_time,
    query_closed_time
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
ON DUPLICATE KEY UPDATE
    status = VALUES(status)
"""

for _, row in df.iterrows():
    cursor.execute(
        insert_query,
        (
            row["query_id"],
            row["client_email"],
            row["client_mobile"],
            row["query_heading"],
            row["query_description"],
            row["status"],
            row["query_created_time"],
            row["query_closed_time"]
        )
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Dataset cleaned and inserted successfully")
