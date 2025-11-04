import streamlit as st
import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("railway_system.db", check_same_thread=False)

def passenger_portal():
    st.subheader("🎫 Passenger Portal")

    if "user" not in st.session_state:
        st.session_state.user = None

    conn = get_connection()
    c = conn.cursor()

    tab = st.radio("Choose Action", ["Sign Up", "Login", "View Trains", "Book Ticket", "My Bookings", "Logout"])

    # --- SIGN UP ---
    if tab == "Sign Up":
        u = st.text_input("Create Username")
        p = st.text_input("Create Password", type="password")
        if st.button("Create Account"):
            if u and p:
                try:
                    c.execute("INSERT INTO passengers VALUES (?, ?)", (u, p))
                    conn.commit()
                    st.success("✅ Account created successfully! Please log in.")
                except sqlite3.IntegrityError:
                    st.error("Username already exists.")
            else:
                st.warning("Please fill all fields.")

    # --- LOGIN ---
    elif tab == "Login":
        if st.session_state.user:
            st.info(f"Already logged in as {st.session_state.user}")
        else:
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.button("Login"):
                c.execute("SELECT * FROM passengers WHERE username=? AND password=?", (u, p))
                if c.fetchone():
                    st.session_state.user = u
                    st.success(f"Welcome, {u}! 🎉")
                    st.rerun()
                else:
                    st.error("Invalid credentials.")

    # --- VIEW TRAINS ---
    elif tab == "View Trains":
        c.execute("SELECT * FROM trains")
        trains = c.fetchall()
        if trains:
            st.dataframe(pd.DataFrame(trains, columns=["Train No", "Name", "Date", "Start", "End"]))
        else:
            st.info("No trains available currently.")

    # --- BOOK TICKET ---
    elif tab == "Book Ticket":
        if not st.session_state.user:
            st.warning("Please log in first.")
        else:
            c.execute("SELECT * FROM trains")
            trains = c.fetchall()
            if not trains:
                st.info("No trains available for booking.")
            else:
                st.dataframe(pd.DataFrame(trains, columns=["Number", "Name", "Date", "Start", "End"]))
                t_no = st.text_input("Enter Train Number to Book")
                seat_type = st.selectbox("Seat Type", ["Aisle", "Middle", "Window"])
                if t_no:
                    c.execute("SELECT price FROM fares WHERE train_number=? AND seat_type=?", (t_no, seat_type))
                    fare = c.fetchone()
                    if fare:
                        price = fare[0]
                        st.info(f"Fare for {seat_type} seat: ₹{price}")
                        if st.button("Confirm Booking"):
                            c.execute("INSERT INTO bookings VALUES (?, ?, ?, ?)",
                                      (t_no, st.session_state.user, seat_type, price))
                            conn.commit()
                            st.success(f"🎟️ Ticket booked successfully for ₹{price}")
                    else:
                        st.warning("Fare not set for this train.")

    # --- MY BOOKINGS ---
    elif tab == "My Bookings":
        if not st.session_state.user:
            st.warning("Please log in first.")
        else:
            c.execute("SELECT * FROM bookings WHERE passenger=?", (st.session_state.user,))
            data = c.fetchall()
            if data:
                st.dataframe(pd.DataFrame(data, columns=["Train", "Passenger", "Seat Type", "Fare (₹)"]))
            else:
                st.info("No bookings found yet.")

    # --- LOGOUT ---
    elif tab == "Logout":
        if st.session_state.user:
            st.session_state.user = None
            st.success("Logged out successfully.")
            st.rerun()
        else:
            st.info("You are not logged in.")

    conn.close()
