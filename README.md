# 🏨 Hotel Management System

A Hotel Management System built with **Python** and **MySQL**, designed to manage hotel operations such as booking rooms, managing customers, billing, and generating reports.  

---

## 🚀 Features
- 👤 **Customer Management** – Add, update, delete, and view customer details  
- 🏠 **Room Booking** – Check room availability and assign rooms to customers  
- 📅 **Check-in / Check-out** – Track guest stay duration and calculate charges  
- 💳 **Billing System** – Auto-generate bills based on room type, days stayed, and meal plan  
- 📊 **Reports** – View booking history and customer records  
- 🔐 **Login System** – Secure authentication for staff  

---

## 🛠️ Tech Stack
- **Python** (Tkinter for GUI)
- **MySQL** (Database)
- **PIL (Pillow)** for image handling
- **mysql-connector-python** for database connection

---

## ⚙️ Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/jawadkhan800050/Hotel_Management_System-project.git

2.Navigate into the project:
cd Hotel_Management_System-project

3.Install required dependencies:
pip install pillow mysql-connector-python

4.Setup MySQL database:

Create a database in MySQL (e.g., Hotel_Management_System)

Import the provided SQL file (if any) or run your own schema

5.Run the project:
python main.py

Future Improvements

Online booking system

Role-based access (Admin / Staff)

Integration with payment gateways

More detailed analytics and reporting

Author

Jawad Khan
GitHub Profile
⭐ If you like this project, don’t forget to star the repo!

---

# 📄 **.gitignore**
```gitignore
# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
venv/
.env/
.venv/

# Mac system files
.DS_Store

# VS Code settings
.vscode/

# Database files (if generated locally)
*.db
*.sqlite3

# Logs
*.log

# Backup files
*.bak
*.swp

# Other unwanted files
.idea/

Steps to add these files:

In your project folder, create:

README.md

.gitignore

Paste the above contents.

Commit & push them:
git add README.md .gitignore
git commit -m "Added README and .gitignore"
git push
