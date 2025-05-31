import json
from datetime import datetime
from os import path

# File to store data
DATA_FILE = "expenses.json"

# Load existing data
expenses = []
if path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        try:
            expenses = json.load(file)
        except json.JSONDecodeError:
            expenses = []

# Save to file
def save_expenses():
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount (₹): "))
        category = input("Enter category: ").strip().lower()
        description = input("Enter description: ").strip()
        date_str = input("Enter date (dd-mm-yyyy): ").strip()
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date_obj.strftime("%d-%m-%Y")
        }
        expenses.append(expense)
        save_expenses()
        print(" Expense added!\n")
    except Exception as e:
        print(f" Error: {e}")

# View all
def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    print("\n All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category'].capitalize()} | {exp['description']} | {exp['date']}")
    print()

# Filter by category
def filter_by_category():
    cat = input("Enter category: ").strip().lower()
    filtered = [e for e in expenses if e['category'] == cat]
    if filtered:
        print(f"\n Expenses in '{cat}':")
        for e in filtered:
            print(f"₹{e['amount']} - {e['description']} on {e['date']}")
    else:
        print("No matching expenses found.")
    print()

# Category summary
def category_summary():
    summary = {}
    for e in expenses:
        cat = e['category']
        summary[cat] = summary.get(cat, 0) + e['amount']
    print("\n Category-wise Summary:")
    for cat, amt in summary.items():
        print(f"{cat.capitalize()}: ₹{amt:.2f}")
    print()

# Total expenses
def total_expenses():
    total = sum(e['amount'] for e in expenses)
    print(f"\n Total Expenses: ₹{total:.2f}\n")

# Monthly summary
def monthly_yearly_summary():
    summary = {}
    for e in expenses:
        try:
            date = datetime.strptime(e['date'], "%d-%m-%Y")
            key = date.strftime("%B-%Y")
            summary[key] = summary.get(key, 0) + e['amount']
        except Exception as err:
            print(f" Skipped invalid date entry: {e['date']}")
    print("\n Monthly-Yearly Summary:")
    for k, amt in sorted(summary.items()):
        print(f"{k}: ₹{amt:.2f}")
    print()

# Update expense
def update_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to update: ")) - 1
        if 0 <= index < len(expenses):
            exp = expenses[index]
            print(f"Current: ₹{exp['amount']} | {exp['category']} | {exp['description']} | {exp['date']}")
            exp['amount'] = float(input("New amount: ₹") or exp['amount'])
            exp['category'] = input("New category: ") or exp['category']
            exp['description'] = input("New description: ") or exp['description']
            new_date = input("New date (dd-mm-yyyy): ") or exp['date']
            datetime.strptime(new_date, "%d-%m-%Y")  # validate date
            exp['date'] = new_date
            save_expenses()
            print(" Expense updated!\n")
        else:
            print(" Invalid number.")
    except Exception as e:
        print(f" Error: {e}")

# Delete expense
def delete_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses()
            print(f" Deleted: ₹{deleted['amount']} - {deleted['category']} - {deleted['description']}")
        else:
            print(" Invalid number.")
    except Exception as e:
        print(f" Error: {e}")

# Menu
def main_menu():
    while True:
        print("========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Category-wise Summary")
        print("5. Total Expenses")
        print("6. Monthly & Year-wise Summary")
        print("7. Update Expense")
        print("8. Delete Expense")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            total_expenses()
        elif choice == '6':
            monthly_yearly_summary()
        elif choice == '7':
            update_expense()
        elif choice == '8':
            delete_expense()
        elif choice == '9':
            print(" Goodbye! Stay on budget.")
            break
        else:
            print(" Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()
