# 🧾 Python Expense Tracker (OOP Version)
A lightweight, console-based **Expense Tracker** built entirely in Python using **Object-Oriented Programming (OOP)** principles. This project allows users to record daily expenses, sort them, group them by date, and store them locally using JSON — without any external APIs or internet connection.

This project is ideal for students learning:
- Python fundamentals  
- File handling  
- Object-Oriented Programming  
- Basic data persistence  
- CLI (Command Line Interface) application design  

---

# 📌 Project Overview
The Expense Tracker is a simple command-line tool where users can:
- Add expenses with amount + note  
- Automatically attach today's date  
- View all stored expenses  
- Sort expenses by amount (ascending or descending)  
- View expenses grouped by date (date headline with items underneath)  
- Store all expenses in a JSON file  
- Load the data automatically when the program starts  

This project is intentionally built without any GUI or APIs so it remains easy, minimal, and accessible for beginners.

---

# ✨ Features
### ✔ Add Expense
- Enter expense amount  
- Add a note describing what was purchased  
- The system automatically assigns today's date  

### ✔ View All Expenses
- Displays each stored expense in a clean format  
- Shows the date, amount, and note  

### ✔ Sort Expenses by Amount
- Ascending order  
- Descending order  

### ✔ Group Expenses by Date
Displays expenses in a structured, readable format:

2025-02-18

₹150 - Groceries
₹40 - Snacks

2025-02-17

₹120 - Petrol

### ✔ Persistent Storage
- All expenses are saved into a file:  
- Automatically loads previous data on startup  

### ✔ Clean OOP Design
Two main classes:
- `Expense`
- `ExpenseTracker`

---

# 🏗 Project Architecture

+------------------------+
| Expense |
+------------------------+
| - date: str |
| - amount: float |
| - note: str |
+------------------------+
| + to_dict() |
| + from_dict() |
+------------------------+
       * (many)
          │
          │
          ▼
+------------------------+
| ExpenseTracker |
+------------------------+
| - expenses: list |
| - data_file: str |
+------------------------+
| + add_expense() |
| + list_expenses() |
| + sort_by_amount() |
| + sort_by_date_grouped()|
| + save() |
| + load() |
+------------------------+


---

# 📁 Folder Structure


/python-expense-tracker
│
├── expense_tracker.py # Main program (OOP)
├── expenses.json # Auto-created JSON data file
├── README.md # Documentation
└── statement.md # Problem statement & scope


---

# 🚀 Getting Started

## 1️⃣ Prerequisites
- Python 3.7 or higher

## 2️⃣ Installation & Setup
Clone the repository:
git clone https://github.com/<your-username>/python-expense-tracker.git
cd python-expense-tracker


(Optional) Create a virtual environment:

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux


Run the program:

python expense_tracker.py

🖥 How to Use
▶ Menu Options

Once you run the program, you will see a menu:

====== Expense Tracker (OOP) ======
1. Add Expense (auto date = today)
2. View All Expenses
3. Sort by Amount (ascending)
4. Sort by Amount (descending)
5. View by Date (grouped)
6. Exit


Choose the desired option and follow the prompts.

📊 Example Usage
Adding an Expense
Enter amount (₹): 150
Enter note: Groceries
Expense added successfully!

Grouped Output Example
--- Expenses Grouped by Date ---

2025-02-18
-----------
   ₹150 - Groceries
   ₹40 - Snacks

🧪 Testing

You can test using:

Test Case 1: Add Expense

Input:

Amount = 100
Note = Lunch


Expected:

Expense appears under today’s date

Test Case 2: Sort by Amount

Expected:

List displayed in order (ascending / descending)

Test Case 3: Group by Date

Expected:

Date printed once

Related expenses underneath

🔧 Future Enhancements (Optional Ideas)

You may include these in your report:

Monthly or weekly summary tables

Category tags (Food, Transport, Shopping...)

Export to CSV

Password/PIN lock

Tkinter GUI interface

Charts using matplotlib

📘 Learning Outcomes

Through this project, you will learn:

OOP in Python

JSON file handling

Basic validation and error handling

CLI application development

Clean code and modular design

How to structure a GitHub project

📝 License

This project is open-source under the MIT License.

🙌 Acknowledgements

This project was developed as part of academic coursework to demonstrate Python programming, OOP concepts, and simple data persistence techniques.
