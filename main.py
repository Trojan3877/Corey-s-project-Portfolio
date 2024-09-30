# personal-finance-tracker/main.py

import csv


# Function to add an expense or income
def add_transaction(transaction_type):
    description = input("Enter a description: ")
    amount = float(input(f"Enter the amount for {transaction_type}: "))
    transaction = {
        'Type': transaction_type,
        'Description': description,
        'Amount': amount
    }

    # Save transaction to CSV file
    with open('transactions.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=['Type', 'Description', 'Amount'])
        writer.writerow(transaction)

    print(
        f"{transaction_type.capitalize()} of ${amount} added successfully.\n")


# Function to show a summary
def show_summary():
    total_income = 0
    total_expense = 0

    # Read transactions from CSV
    try:
        with open('transactions.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Type'] == 'income':
                    total_income += float(row['Amount'])
                elif row['Type'] == 'expense':
                    total_expense += float(row['Amount'])

        balance = total_income - total_expense
        print("\nSummary:")
        print(f"Total Income: ${total_income}")
        print(f"Total Expenses: ${total_expense}")
        print(f"Remaining Balance: ${balance}\n")

    except FileNotFoundError:
        print("No transactions found. Please add some first.\n")


# Main menu
def main():
    print("Welcome to the Personal Finance Tracker!")

    # Check if the CSV file exists, if not create it
    try:
        with open('transactions.csv', mode='x', newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=['Type', 'Description', 'Amount'])
            writer.writeheader()
    except FileExistsError:
        pass  # CSV file already exists

    while True:
        print("Choose an option:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction('income')
        elif choice == '2':
            add_transaction('expense')
        elif choice == '3':
            show_summary()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.\n")


if __name__ == "__main__":
    main()
