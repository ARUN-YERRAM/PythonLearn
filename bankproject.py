import json

# File paths
ACCOUNTS_FILE = 'C:\\Users\\Yerram Abhilash\\OneDrive\\Documents\\ArDocs\\PY.FILES\\accounts.py'
TRANSACTIONS_FILE = 'C:\\Users\\Yerram Abhilash\\OneDrive\\Documents\\ArDocs\\PY.FILES\\Transactions.py'

# Load account data from JSON file
def load_accounts():
    try:
        with open(ACCOUNTS_FILE) as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Load transaction history from JSON file
def load_transactions():
    try:
        with open(TRANSACTIONS_FILE) as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save account data to JSON file
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        json.dump(accounts, file)

# Save transaction history to JSON file
def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as file:
        json.dump(transactions, file)

# Create a new bank account
def create_account():
    accounts = load_accounts()
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder's name: ")
    address = input("Enter account holder's address: ")
    contact = input("Enter account holder's contact information: ")
    balance = float(input("Enter initial account balance:(minimum balance > 500) "))
    
    # Add account to accounts dictionary
    accounts[account_number] = {
        'name': name,
        'address': address,
        'contact': contact,
        'balance': balance
    }
    
    # Save accounts data
    save_accounts(accounts)
    print("Account created successfully!")

# Deposit funds into an account
def deposit_funds():
    accounts = load_accounts()
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account does not exist!")
        return
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid deposit amount!")
        return
    
    # Update account balance
    accounts[account_number]['balance'] += amount
    
    # Save accounts data
    save_accounts(accounts)
    
    # Add transaction to transaction history
    transactions = load_transactions()
    transactions.append({
        'account_number': account_number,
        'type': 'Deposit',
        'amount': amount
    })
    
    # Save transactions data
    save_transactions(transactions)
    print("Deposit successful!")

# Withdraw funds from an account
def withdraw_funds():
    accounts = load_accounts()
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account does not exist!")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    if amount > accounts[account_number]['balance']:
        print("Insufficient funds!")
        return
    
    # Update account balance
    accounts[account_number]['balance'] -= amount
    
    # Save accounts data
    save_accounts(accounts)
    
    # # Add transaction to transaction history
    # transactions = load_transactions()
    # transactions.append({
    #     'account_number': account_number,
    #     'type': 'Withdrawal',
    #     'amount': amount
    # })
    
    # # Save transactions data
    # save_transactions(transactions)
    # print("Withdrawal successful!")

# Check account balance
def check_balance():
    accounts = load_accounts()
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account does not exist!")
        return
    
    # Retrieve and display account balance
    balance = accounts[account_number]['balance']
    print(f"Account balance: {balance}")

# Display transaction history for an account
# def view_transactions():
#     accounts = load_accounts()
#     account_number = input("Enter account number: ")
#     if account_number not in accounts:
#         print("Account does not exist!")
#         return
    
#     transactions = load_transactions()
#     account_transactions = [t for t in transactions if t['account_number'] == account_number]
    
#     if len(account_transactions) == 0:
#         print("No transaction history found for this account!")
#     else:
#         print("Transaction History:")
#         for transaction in account_transactions:
#             print(f"Type: {transaction['type']}, Amount: {transaction['amount']}")
    
# Main menu
def main_menu():
    while True:
        print("\n=== Banking System ===")
        print("1. Create Bank Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_funds()
        elif choice == '3':
            withdraw_funds()
        elif choice == '4':
            check_balance()
        # elif choice == '5':
        #     view_transactions()
        elif choice == '6':
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == '__main__':
    main_menu()

# CGPA
# COMMUNICATION SKILLS
# 1st year: 1 LANGUAGE , CODING DSA , WEB  DEVELOPMENT ,SYSTEM DESIGN
# PROJECTS
# INTERNSHIPS,
# HACKATHONS
# CP , OPEN SOURCE , RESUME ,CS FUNDAMENTALS (OS,DBMS,CN,OOPS) , 