print("Weclome to expense tracker")
name=input("Please enter your name: ")
print("Hello",name)

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAll Expenses:")
    for exp in expenses:
        print("Category:", exp["category"], "| Amount:", exp["amount"])
        
def view_total(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    print("Total expense:", total)
    
def category_summary(expenses):
    summary = {}

    for exp in expenses:
        cat = exp["category"]
        amt = exp["amount"]

        if cat in summary:
            summary[cat] += amt
        else:
            summary[cat] = amt

    print("\nCategory-wise Summary:")
    for cat, amt in summary.items():
        print(cat, ":", amt)
    
        
expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Category-wise Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        view_total(expenses)
    elif choice == "4":
        category_summary(expenses)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
