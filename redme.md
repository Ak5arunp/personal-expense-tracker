# 💰 Personal Expense Tracker (Console App)

A simple, lightweight Python-based console application to help you track your daily expenses. Designed for personal use — with clean code, menu-driven interface, and data saved in JSON format.

---

## 📌 Features

- ✅ Add new expense (amount, category, description, date)
- ✅ View all expenses
- ✅ Update any existing expense
- ✅ Delete expense by index
- ✅ Filter by category
- ✅ Total expense calculation
- ✅ Category-wise expense summary
- ✅ Monthly & yearly expense summary
- ✅ Save and load data using JSON file

---

## 🛠️ How to Run

### 🔧 Requirements
- Python 3.x (recommended: Python 3.10+)

### ▶️ Steps

1. Clone this repo or download ZIP
2. Make sure `personal_expense_track.py` and `expenses.json` are in the same folder
3. Run using terminal or VS Code:

```bash
python personal_expense_track.py
................................
📁 Personal Expense Tracker
├── personal_expense_track.py  # Main application file
├── expenses.json              # Data file (auto-created)
└── README.md                  # This file


..... Expense Tracker Menu .....
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Filter by Category
6. Monthly & Yearly Summary
7. Category-wise Summary
8. Total Expenses
9. Exit

.........data storage format JSON..........
{
  "amount": 500,
  "category": "food",
  "description": "Lunch at restaurant",
  "date": "24-05-2025"
}
