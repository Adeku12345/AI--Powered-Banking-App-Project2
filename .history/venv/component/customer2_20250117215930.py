class Customer:
    def __init__(self, customer_id, name, address, phone_number, email):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.accounts = []  # List to store accounts linked to the customer

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return f"Account {account_number} removed successfully."
        return f"Account {account_number} not found."

    def display_customer_details(self):
        account_details = "\n".join([f"Account Number: {acc.account_number}, Balance: {acc.balance}" for acc in self.accounts])
        return (f"Customer ID: {self.customer_id}\n"
                f"Name: {self.name}\n"
                f"Address: {self.address}\n"
                f"Phone Number: {self.phone_number}\n"
                f"Email: {self.email}\n"
                f"Accounts:\n{account_details}")


class Account:
    def __init__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type  # e.g., "savings", "checking"
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}."

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount}. New balance: {self.balance}."
        return "Insufficient funds for withdrawal."

    def transfer(self, amount, target_account):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            return f"Transferred {amount} to Account {target_account.account_number}. New balance: {self.balance}."
        return "Insufficient funds for transfer."


# Example usage
if __name__ == "__main__":
    # Create a customer
    customer = Customer(
        customer_id="CUST12345",
        name="John Doe",
        address="123 Elm Street, London, UK",
        phone_number="+44 123 456 7890",
        email="johndoe@example.com"
    )

    # Create accounts for the customer
    savings_account = Account(account_number="ACC1001", account_type="savings", balance=5000)
    checking_account = Account(account_number="ACC1002", account_type="checking", balance=2000)

    # Add accounts to the customer
    customer.add_account(savings_account)
    customer.add_account(checking_account)

    # Display customer details
    print(customer.display_customer_details())

    # Perform some account operations
    print(savings_account.deposit(1000))
    print(checking_account.withdraw(500))
    print(savings_account.transfer(2000, checking_account))

    # Remove an account
    print(customer.remove_account("ACC1002"))

    # Display updated customer details
    print(customer.display_customer_details())
