# 🚆 Railway Management System (Streamlit + SQLite)

![Project Banner](images/banner.png)

### 💻 Built by [Aneek Ghosh](https://github.com/AneekGhosh)

A modern and easy-to-use **Railway Management System** built using **Python**, **Streamlit**, and **SQLite**, featuring secure role-based access for **Admins** and **Passengers**.
This project is designed to showcase real-world CRUD operations, authentication, and database integration — perfect for your resume, internship portfolio, and technical interviews.

---

## ✨ Features

### 👨‍💼 Admin Panel

* Secure login with hardcoded credentials
* Add, view, and delete trains
* Set fares for multiple seat types (Aisle, Middle, Window)
* View and manage all passenger bookings
* Auto-database creation and schema validation

### 👥 Passenger Portal

* Sign up with username and password
* Login securely using session-based authentication
* Browse available trains and fares
* Book tickets and view personal booking history
* Logout safely

---

## 🧩 Tech Stack

| Component          | Technology Used     |
| ------------------ | ------------------- |
| **Frontend**       | Streamlit           |
| **Backend**        | Python              |
| **Database**       | SQLite              |
| **Libraries**      | pandas, sqlite3     |
| **Authentication** | Session-based login |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/AneekGhosh/Railway_Management_System_Streamlit.git
cd Railway_Management_System_Streamlit
```

### 2️⃣ Install Required Packages

Make sure you have Python 3.8+ installed, then run:

```bash
pip install streamlit pandas
```

### 3️⃣ Run the Application

```bash
streamlit run main.py
```

Then open the link shown in your terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## 🔑 Admin Login

| Username | Password   |
| -------- | ---------- |
| `admin`  | `admin123` |

---

## 🧠 How It Works

1. The app automatically creates the **SQLite database** and all necessary tables on startup.
2. **Admins** can add new trains, assign fares, and manage all passenger bookings.
3. **Passengers** can sign up, view available trains, book seats, and view only their own bookings.
4. All data is stored persistently in the **SQLite** database.
5. The app uses Streamlit’s session management for a seamless login/logout experience.

---

## 📸 Screenshots

| Admin Dashboard                                | Passenger Portal                                 |
| ---------------------------------------------- | ------------------------------------------------ |
| ![Admin Dashboard](images/admin_dashboard.png) | ![Passenger Portal](images/passenger_portal.png) |

---

## 🚀 Deployment

You can deploy this app online using **Streamlit Cloud**:

1. Go to [https://share.streamlit.io](https://share.streamlit.io)
2. Log in with your GitHub account
3. Connect this repository
4. Set the **main file path** to `main.py`
5. Click **Deploy** 🎉

Your app will go live with a public URL to showcase in your portfolio or resume.

---

## 🧾 Future Improvements

* Email-based authentication
* Downloadable ticket in PDF format
* Live seat availability tracking
* Integration with real train APIs
* Dark mode toggle for UI

---

## 🏁 Conclusion

This **Railway Management System** is a perfect **intermediate-level project** demonstrating:

* Real-world CRUD operations
* Role-based authentication
* Data persistence using SQLite
* A polished Streamlit front-end

It’s **clean, professional, and interview-ready** — ideal for MCA or BCA students, internship portfolios, and early-career developers.

💡 *Built with passion and code by* **Aneek Ghosh** ❤️
