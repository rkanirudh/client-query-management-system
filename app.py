import streamlit as st
import uuid
from datetime import datetime

from auth.register import register_user
from auth.login import authenticate_user
from database.db_connection import get_connection
from support.dashboard import support_dashboard

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Client Query Management System",
    layout="centered"
)

# ---------------------------
# SESSION STATE INIT
# ---------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

# ---------------------------
# TITLE
# ---------------------------
st.title("Client Query Management System")

# ======================================================
# AUTH PAGES (ONLY WHEN NOT LOGGED IN)
# ======================================================
if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "Select Option",
        ["Login", "Register"]
    )

    # ---------------------------
    # REGISTER
    # ---------------------------
    if menu == "Register":
        st.subheader("User Registration")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Client", "Support"])

        if st.button("Register"):
            if username and password:
                try:
                    register_user(username, password, role)
                    st.success("Registration successful! Please login.")
                except:
                    st.error("Username already exists.")
            else:
                st.warning("Please fill all fields.")

    # ---------------------------
    # LOGIN
    # ---------------------------
    elif menu == "Login":
        st.subheader("User Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = authenticate_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = user["role"]
                st.success(f"Welcome! Logged in as {user['role']}")
                st.rerun()
            else:
                st.error("Invalid username or password")

# ======================================================
# LOGOUT
# ======================================================
if st.session_state.logged_in:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.rerun()

# ======================================================
# CLIENT VIEW (STEP 4)
# ======================================================
if st.session_state.logged_in and st.session_state.role == "Client":

    st.markdown("---")
    st.subheader("Submit a New Query")

    email = st.text_input("Email ID")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    description = st.text_area("Query Description")

    if st.button("Submit Query"):
        if email and mobile and heading and description:
            conn = get_connection()
            cursor = conn.cursor()

            query_id = f"Q{uuid.uuid4().hex[:6].upper()}"

            cursor.execute("""
                INSERT INTO queries (
                    query_id, client_email, client_mobile,
                    query_heading, query_description,
                    status, query_created_time
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (
                query_id,
                email,
                mobile,
                heading,
                description,
                "Open",
                datetime.now()
            ))

            conn.commit()
            cursor.close()
            conn.close()

            st.success(f"Query submitted successfully! ID: {query_id}")
        else:
            st.warning("Please fill all fields.")

# ======================================================
# SUPPORT DASHBOARD (STEP 5)
# ======================================================
elif st.session_state.logged_in and st.session_state.role == "Support":

    st.markdown("---")
    support_dashboard()
