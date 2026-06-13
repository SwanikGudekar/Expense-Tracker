# Expense Tracker

expensesList = []  # list of expenses in the form of dictionary

print("Welcome to Expense Tracker")

while True:
    print("\n=== Menu ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Please Enter Your Choice: ")

    # 1. Add Expense
    if choice == "1":
        date = input("Enter Date: ")
        category = input("Enter the Category: ")
        description = input("Enter short description: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("Expense added successfully!")

    # 2. View All Expenses
    elif choice == "2":
        if len(expensesList) == 0:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")
            count = 1
            for i in expensesList:
                print(
                    f"Expense No.{count} -> "
                    f"{i['date']}, {i['category']}, "
                    f"{i['description']}, ₹{i['amount']}"
                )
                count += 1

    # 3. View Total Expense
    elif choice == "3":
        total = 0

        for i in expensesList:
            total += i["amount"]

        print("Total Expense = ₹", total)

    # 4. Exit
    elif choice == "4":
        print("Thanks for using Expense Tracker!")
        break

    else:
        print("Invalid Choice!")

