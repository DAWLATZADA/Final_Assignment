# ✈️ Flight Booking System Overbooking – Critical Section Project

## 📌 Project Overview

This project demonstrates how **overbooking** can occur in a flight booking system due to
a **race condition** when multiple users try to book seats simultaneously.

The project is based on a **real-world case (Centrum Air)** where two passengers were left
at Istanbul Airport because more tickets were sold than available seats.

This is an **Operating Systems** project focusing on:
- Critical Section
- Read/Write conflict
- Race Condition
- Synchronization (Mutex Lock)

---

## 🎯 Project Objectives

- Simulate a flight booking system
- Demonstrate how overbooking happens
- Show the problem of unprotected critical sections
- Fix the problem using synchronization mechanisms
- Connect theory with a real-world airline booking case

---

## 📁 Project Structure


---

## ⚙️ Technologies Used

- Python 3
- Python threading module
- HTML & CSS (Visualization only)
- Markdown for documentation

---

## 🚫 Important Note

- **Backend logic is mandatory**
- **HTML is optional and only for visualization**
- No booking logic exists in HTML
- This project follows Operating Systems syllabus rules

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites
- Python 3 installed on your system

Check Python version:
```bash

python --version

cd backend
python no_lock.py

cd backend
python with_lock.py
