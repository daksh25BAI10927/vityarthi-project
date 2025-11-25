from datetime import datetime
import json
import os

expenses = []

# Load expenses from file if it exists
if os.path.exists('expenses.json'):
    with open('expenses.json', 'r') as f:
        expenses = json.load(f)


def save_expenses():
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)


class Sorter:
    def sort_by_date(self, exp_list):
        return sorted(exp_list, key=lambda x: x['date'])

    def sort_by_amount(self, exp_list):
        return sorted(exp_list, key=lambda x: x['amount'])


def add_expense():
    amount = float(input("Enter amount: ₹"))
    comment = input("Enter comment: ")
    date = datetime.now().strftime('%Y-%m-%d')

    expense = {
        'date': date,
        'amount': amount,
        'comment': comment
    }
    expenses.append(expense)
    save_expenses()
    print("\nExpense added!")


def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses yet.")
        return

    print("\nHow to sort?")
    print("1. By Date")
    print("2. By Amount")
    choice = input("Enter choice: ")

    sorter = Sorter()

    if choice == '1':
        sorted_exp = sorter.sort_by_date(expenses)
    elif choice == '2':
        sorted_exp = sorter.sort_by_amount(expenses)
    else:
        sorted_exp = expenses

    print("\n--- All Expenses ---")
    for exp in sorted_exp:
        print(f"{exp['date']} | ₹{exp['amount']} | {exp['comment']}")

    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal: ${total}")


# Main program
while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("Goodbye!")
        break
    else:

        print("Invalid choice!")
