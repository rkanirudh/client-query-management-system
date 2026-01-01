import uuid
from datetime import datetime
from database.db_connection import get_connection

def insert_client_query(email, mobile, heading, description):
    conn = get_connection()
    cursor = conn.cursor()

    query_id = "Q" + str(uuid.uuid4())[:8]
    created_time = datetime.now()
    status = "Open"

    sql = """
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
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (
        query_id,
        email,
        mobile,
        heading,
        description,
        status,
        created_time,
        None
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return query_id
