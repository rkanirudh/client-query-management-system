# client-query-management-system
A Streamlit and MySQL based Client Query Management System with support dashboard and analytics.

# Client Query Management System

## 📌 Project Overview
The **Client Query Management System** is a data-driven web application designed to organize, track, and manage client support queries efficiently.  
It enables clients to submit queries and allows support teams to monitor, update, and analyze query resolution performance using dashboards and analytics.

This project is built as part of a **Data Science / SQL / Python capstone project** and demonstrates practical usage of **Python, Pandas, MySQL, and Streamlit**.

---

## 🎯 Problem Statement
Organizations often struggle to manage client queries efficiently due to:
- Lack of centralized tracking
- No clear query status updates
- Difficulty in analyzing support performance

This system solves these problems by providing a **centralized query management and analytics platform**.

---

## 🛠️ Tech Stack

| Component | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | MySQL |
| Data Processing | Pandas |
| Visualization | Streamlit Charts |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

# Client Query Management System

## 📌 Project Overview
The **Client Query Management System** is a data-driven web application designed to organize, track, and manage client support queries efficiently.  
It enables clients to submit queries and allows support teams to monitor, update, and analyze query resolution performance using dashboards and analytics.

This project is built as part of a **Data Science / SQL / Python capstone project** and demonstrates practical usage of **Python, Pandas, MySQL, and Streamlit**.

---

## 🎯 Problem Statement
Organizations often struggle to manage client queries efficiently due to:
- Lack of centralized tracking
- No clear query status updates
- Difficulty in analyzing support performance

This system solves these problems by providing a **centralized query management and analytics platform**.

---

## 🛠️ Tech Stack

| Component | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | MySQL |
| Data Processing | Pandas |
| Visualization | Streamlit Charts |
| Version Control | Git & GitHub |

---

## 📂 Project Structure
client-query-management-system/
│
├── app.py # Main Streamlit application
│
├── auth/
│ ├── register.py # User registration logic
│ └── login.py # User authentication logic
│
├── database/
│ ├── db_connection.py # MySQL connection handler
│ ├── create_tables.py # Database & table creation
│ └── clean_and_insert_data.py# Dataset cleaning & insertion
│
├── support/
│ └── dashboard.py # Support dashboard & analytics
│
├── data/
│ └── synthetic_client_queries.csv # Initial dataset
│
├── requirements.txt
└── README.md


---

## 🔐 User Roles

### 👤 Client
- Submit new queries
- Provide email, mobile number, query heading, and description

### 🧑‍💼 Support Team
- View all client queries
- Update query status (Open / In Progress / Closed)
- Analyze query trends and resolution statistics

---

## 🧾 Dataset Details
- **File:** `synthetic_client_queries.csv`
- **Columns:**
  - `query_id`
  - `client_email`
  - `client_mobile`
  - `query_heading`
  - `query_description`
  - `status`
  - `query_created_time`
  - `query_closed_time`

The dataset is cleaned using **Pandas** and inserted into **MySQL** using Python scripts.

---

## ⚙️ Application Features

### ✅ Client Query Submission
- Real-time query submission via Streamlit form
- Automatic timestamping
- Default status set to **Open**

### ✅ Support Dashboard
- View all queries in tabular format
- Update query status
- Expandable query details

### ✅ Analytics Dashboard
- Query status distribution (Bar Chart)
- Queries over time (Line Chart)
- Summary metrics:
  - Total Queries
  - Open Queries
  - Closed Queries

---

## 🗄️ Database Design

### Tables Used:
1. **users**
   - id
   - username
   - hashed_password
   - role

2. **queries**
   - query_id (Primary Key)
   - client_email
   - client_mobile
   - query_heading
   - query_description
   - status
   - query_created_time
   - query_closed_time

---

## ▶️ How to Run the Project Locally

### 1️⃣ Activate Virtual Environment
```bash
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py


