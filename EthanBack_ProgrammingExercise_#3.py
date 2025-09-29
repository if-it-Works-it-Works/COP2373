from functools import reduce

def expense_lister():
    # Establishing our list
    expenses = []

    # Starting our loop so the user is prompted until they've entered all information
    while True:
        expense_type = input("Enter Your Expense Type (Press Enter to Exit ): ")

        # This checks for answer the prompt with an enter key, at which it breaks the loop
        if expense_type == "":
            print("\n")
            break
        try:
            amount = float(input(f"Enter Your Expense Amount for {expense_type}: "))
            # Adds each expense as a dict, with 'type' and 'amount' keys
            expenses.append({'type': expense_type,  'amount': amount})
        except ValueError:
            print("Please enter a number. ")
    return expenses

def main():
    expenses = expense_lister()

    # This just checks whether our "expenses" list is empty or not
    if not expenses:
        print("No Expenses found\n")
        return

    total = reduce(lambda acc, x:acc + x['amount'], expenses, 0)
    highest = reduce(lambda a, b: a if a['amount'] > b['amount'] else b, expenses )
    lowest = reduce(lambda a,b : a if a['amount'] < b['amount'] else b, expenses)

    print(f"Your Expense Total: {total:.2f}\n")
    print(f"Your Highest Expense Came From: {highest['type']} for ${highest['amount']:.2f}\n")
    print(f"Your Lowest Expense Came From: {lowest['type']} for ${lowest['amount']:.2f}\n")




if __name__ == "__main__":
    main()