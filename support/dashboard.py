import streamlit as st
import pandas as pd
from database.db_connection import get_connection


def support_dashboard():
    st.subheader("📊 Support Dashboard")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT query_id, client_email, client_mobile,
               query_heading, query_description,
               status, query_created_time
        FROM queries
        ORDER BY query_created_time DESC
    """)

    queries = cursor.fetchall()
    cursor.close()
    conn.close()

    if not queries:
        st.info("No client queries available.")
        return

    df = pd.DataFrame(queries)

    # ✅ Dataset table (UNCHANGED – good as deployed)
    st.subheader("📋 All Queries (Dataset View)")
    st.dataframe(df, use_container_width=True)

    # Query cards
    st.markdown("---")
    st.subheader("🛠 Query Management")

    for q in queries:
        with st.expander(f"{q['query_heading']} | Status: {q['status']}"):
            st.write("📧 Email:", q["client_email"])
            st.write("📱 Mobile:", q["client_mobile"])
            st.write("📝 Description:", q["query_description"])
            st.write("⏰ Created:", q["query_created_time"])

            new_status = st.selectbox(
                "Update Status",
                ["Open", "In Progress", "Closed"],
                index=["Open", "In Progress", "Closed"].index(q["status"]),
                key=f"status_{q['query_id']}"
            )

            if st.button("Update", key=f"btn_{q['query_id']}"):
                conn = get_connection()
                cur = conn.cursor()
                cur.execute(
                    "UPDATE queries SET status=%s WHERE query_id=%s",
                    (new_status, q["query_id"])
                )
                conn.commit()
                cur.close()
                conn.close()
                st.success("Status updated successfully")
                st.rerun()

    # ---------------------------
    # 📊 ANALYTICS
    # ---------------------------
    st.markdown("---")
    st.header("📊 Support Analytics")   # 🔥 ONLY CHANGE

    st.subheader("📌 Query Status Distribution")
    status_df = df["status"].value_counts()
    st.bar_chart(status_df)

    st.subheader("📈 Queries Over Time")
    df["query_created_time"] = pd.to_datetime(df["query_created_time"])
    time_df = df.groupby(df["query_created_time"].dt.date).size()
    st.line_chart(time_df)

    st.subheader("📊 Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Queries", len(df))
    col2.metric("Open Queries", (df["status"] == "Open").sum())
    col3.metric("Closed Queries", (df["status"] == "Closed").sum())
