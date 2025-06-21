def add_expense(expenses, amount, category):
    """
    Append a new expense record to the expenses list.

    Args:
        expenses (list): List to store expense dictionaries.
        amount (float): Expense amount.
        category (str): Category of the expense.
    """
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses):
    """
    Print all expenses in a formatted manner.

    Args:
        expenses (list): List of expense dictionaries to display.
    """
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


def total_expenses(expenses):
    """
    Calculate the total of all expense amounts.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        float: The total expense amount.
    """
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    """
    Filter expenses by a specific category.

    Args:
        expenses (list): List of expense dictionaries.
        category (str): Category to filter expenses by.

    Returns:
        filter: An iterator containing matching expenses.
    """
    return filter(lambda expense: expense['category'] == category, expenses)


def main():
    """
    Entry point of the Expense Tracker application.
    Provides a menu interface for the user to interact with.
    """
    expenses = []

    while True:
        # Display menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        # Get user input for menu selection
        choice = input('Enter your choice: ')

        if choice == '1':
            # Prompt user to add a new expense
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Display all recorded expenses
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            # Show the sum of all expense amounts
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            # Filter and display expenses based on category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            # Exit the application
            print('Exiting the program.')
            break

# Run the main program
main()
