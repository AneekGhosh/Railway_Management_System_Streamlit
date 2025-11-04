import streamlit as st
import sqlite3
import pandas as pd
import os
from admin import admin_panel
from passenger import passenger_portal

DB_PATH = "railway_system.db"


# ---------------------- AUTO DATABASE FIX ----------------------
def ensure_correct_schema():
    """Check database schema and reset if mismatched"""
    if os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        try:
            c.execute("PRAGMA table_info(bookings)")
            columns = [col[1] for col in c.fetchall()]
            required = ["train_number", "passenger", "seat_type", "fare"]
            if not all(col in columns for col in required):
                raise Exception("Schema mismatch")
        except:
            conn.close()
            os.remove(DB_PATH)
            st.warning("⚠️ Old database found with mismatched schema. Resetting automatically...")
        else:
            conn.close()


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# ---------------------- DATABASE SETUP ----------------------
def setup_database():
    """Create required tables if they don’t exist"""
    conn = get_connection()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS trains(
                    train_number TEXT PRIMARY KEY,
                    train_name TEXT,
                    departure_date TEXT,
                    start TEXT,
                    end TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS fares(
                    train_number TEXT,
                    seat_type TEXT,
                    price REAL
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS passengers(
                    username TEXT PRIMARY KEY,
                    password TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS bookings(
                    train_number TEXT,
                    passenger TEXT,
                    seat_type TEXT,
                    fare REAL
                )''')

    conn.commit()
    conn.close()


# Initialize database
ensure_correct_schema()
setup_database()

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Railway Management System", layout="centered")
st.title("🚆 Railway Management System")
st.caption("Developed by Aneek Ghosh | Python • Streamlit • SQLite")

# ---------------------- SIDEBAR ----------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Admin Panel", "Passenger Portal", "About"]
)

# ---------------------- HOME ----------------------
if menu == "Home":
    st.subheader("Welcome to the Railway Management System!")
    st.write("""
    This project demonstrates a **complete railway reservation system** with two user roles:

    🧑‍💼 **Admin** – Manage trains, set fares, view all bookings  
    👥 **Passenger** – Create accounts, view trains, book tickets, and view personal bookings  

    ### Key Features
    - Role-based access control  
    - Secure login system  
    - Dynamic train and fare management  
    - Passenger-specific booking history  
        """)

# ---------------------- ADMIN PANEL ----------------------
elif menu == "Admin Panel":
    admin_panel()

# ---------------------- PASSENGER PORTAL ----------------------
elif menu == "Passenger Portal":
    passenger_portal()

# ---------------------- ABOUT ----------------------
elif menu == "About":
    st.subheader("📘 About This Project")
    st.write("""
    **Railway Management System**  
    - Developed with **Streamlit**, **Python**, and **SQLite**  
    - Implements **role-based user access**  
    - CRUD operations for Admin, controlled booking system for Passengers  
    ---
    💡 *Created by Aneek Ghosh (2025)*
    """)
