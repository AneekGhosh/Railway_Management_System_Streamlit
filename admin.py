import streamlit as st
import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("railway_system.db", check_same_thread=False)

def admin_panel():
    st.subheader("🧑‍💼 Admin Dashboard")

    ADMIN_USER = "admin"
    ADMIN_PASS = "admin123"

    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    conn = get_connection()
    c = conn.cursor()

    if not st.session_state.admin_logged_in:
        u = st.text_input("Admin Username")
        p = st.text_input("Password", type="password")
        if st.button("Login"):
            if u == ADMIN_USER and p == ADMIN_PASS:
                st.session_state.admin_logged_in = True
                st.success("✅ Logged in successfully as Admin")
                st.rerun()
            else:
                st.error("Invalid credentials.")
    else:
        st.success("Welcome, Admin!")
        choice = st.radio("Choose Action", ["Add Train", "View Trains", "Delete Train", "Set Fare", "View All Bookings", "Logout"])

        # Add Train
        if choice == "Add Train":
            t_no = st.text_input("Train Number")
            t_name = st.text_input("Train Name")
            t_date = st.date_input("Departure Date")
            start = st.text_input("Start Station")
            end = st.text_input("End Station")

            if st.button("Add Train"):
                if all([t_no, t_name, start, end]):
                    try:
                        c.execute("INSERT INTO trains VALUES (?, ?, ?, ?, ?)", (t_no, t_name, str(t_date), start, end))
                        conn.commit()
                        st.success("✅ Train added successfully!")
                    except sqlite3.IntegrityError:
                        st.error("Train number already exists.")
                else:
                    st.warning("Please fill all fields before adding.")

        # View Trains
        elif choice == "View Trains":
            c.execute("SELECT * FROM trains")
            trains = c.fetchall()
            if trains:
                st.dataframe(pd.DataFrame(trains, columns=["No", "Name", "Date", "Start", "End"]))
            else:
                st.info("No trains found.")

        # Delete Train
        elif choice == "Delete Train":
            t_no = st.text_input("Enter Train Number to delete")
            if st.button("Delete Train"):
                c.execute("DELETE FROM trains WHERE train_number=?", (t_no,))
                conn.commit()
                st.success(f"Train {t_no} deleted successfully.")

        # Set Fare
        elif choice == "Set Fare":
            t_no = st.text_input("Train Number")
            seat_type = st.selectbox("Seat Type", ["Aisle", "Middle", "Window"])
            price = st.number_input("Fare (₹)", min_value=0.0, step=10.0)
            if st.button("Save Fare"):
                c.execute("DELETE FROM fares WHERE train_number=? AND seat_type=?", (t_no, seat_type))
                c.execute("INSERT INTO fares VALUES (?, ?, ?)", (t_no, seat_type, price))
                conn.commit()
                st.success(f"Fare set for Train {t_no} ({seat_type}): ₹{price}")

            c.execute("SELECT * FROM fares")
            fares = c.fetchall()
            if fares:
                st.dataframe(pd.DataFrame(fares, columns=["Train", "Seat Type", "Fare (₹)"]))

        # View All Bookings
        elif choice == "View All Bookings":
            c.execute("SELECT * FROM bookings")
            bookings = c.fetchall()
            if bookings:
                st.dataframe(pd.DataFrame(bookings, columns=["Train", "Passenger", "Seat Type", "Fare (₹)"]))
            else:
                st.info("No bookings found yet.")

        elif choice == "Logout":
            st.session_state.admin_logged_in = False
            st.success("Logged out successfully.")
            st.rerun()

    conn.close()
