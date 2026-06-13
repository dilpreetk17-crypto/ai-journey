# Day 5 - Lists & Dictionaries
# Personal Budget Tracker

expenses = []  # empty list to store expense dictionaries

def add_expense(item, amount, category):
    expense = {
        "item": item,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print("✅ Added:", item, "₹" + str(amount))

def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet!")
        return
    print("\n--- Your Expenses ---")
    for i, expense in enumerate(expenses):
        print(i+1, ".", expense["item"], 
              "| ₹" + str(expense["amount"]), 
              "| Category:", expense["category"])
    print("Total spent: ₹" + str(sum(e["amount"] for e in expenses)))
    print("---")

def view_by_category(category):
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    if len(filtered) == 0:
        print("No expenses in that category")
        return
    print("\n--- Category:", category, "---")
    for e in filtered:
        print("-", e["item"], "₹" + str(e["amount"]))
    total = sum(e["amount"] for e in filtered)
    print("Category total: ₹" + str(total))

# Main program
print("💰 Personal Budget Tracker")
print("---")

while True:
    print("\nWhat do you want to do?")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View by category")
    print("4. Quit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        item = input("Item name: ")
        amount = float(input("Amount (₹): "))
        category = input("Category (Food/Transport/Entertainment/Other): ")
        add_expense(item, amount, category)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category = input("Enter category: ")
        view_by_category(category)

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice, try again")