








def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pass@#$123456",
        database="bankingdb2"
    )


import mysql.connector

class DatabaseManager:
    def __init__(self, host="localhost", user="root", password="Pass@#$123456", database=""bankingdb2"):
        # Connect to the MySQL database
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create Customer table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address TEXT NOT NULL,
            phone_number VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL
        )''')

        # Create Account table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Account (
            account_number VARCHAR(255) PRIMARY KEY,
            customer_id VARCHAR(255) NOT NULL,
            account_type VARCHAR(50) NOT NULL,
            balance DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customer (customer_id)
        )''')

        # Create Transaction table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Transaction (
            transaction_id VARCHAR(255) PRIMARY KEY,
            account_number VARCHAR(255) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            transaction_type VARCHAR(50) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (account_number) REFERENCES Account (account_number)
        )''')

        # Create Loan table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Loan (
            loan_id VARCHAR(255) PRIMARY KEY,
            customer_id VARCHAR(255) NOT NULL,
            loan_amount DECIMAL(10, 2) NOT NULL,
            loan_type VARCHAR(50) NOT NULL,
            interest_rate DECIMAL(5, 2) NOT NULL,
            duration INT NOT NULL,
            status VARCHAR(50) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customer (customer_id)
        )''')

        # Create Investment table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Investment (
            investment_id VARCHAR(255) PRIMARY KEY,
            customer_id VARCHAR(255) NOT NULL,
            investment_type VARCHAR(50) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            risk_level VARCHAR(50) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customer (customer_id)
        )''')

        self.connection.commit()

    def add_customer(self, customer_id, name, address, phone_number, email):
        self.cursor.execute('''
        INSERT INTO Customer (customer_id, name, address, phone_number, email)
        VALUES (%s, %s, %s, %s, %s)
        ''', (customer_id, name, address, phone_number, email))
        self.connection.commit()

    def add_account(self, account_number, customer_id, account_type, balance):
        self.cursor.execute('''
        INSERT INTO Account (account_number, customer_id, account_type, balance)
        VALUES (%s, %s, %s, %s)
        ''', (account_number, customer_id, account_type, balance))
        self.connection.commit()

    def record_transaction(self, transaction_id, account_number, amount, transaction_type):
        self.cursor.execute('''
        INSERT INTO Transaction (transaction_id, account_number, amount, transaction_type)
        VALUES (%s, %s, %s, %s)
        ''', (transaction_id, account_number, amount, transaction_type))
        self.connection.commit()

    def add_loan(self, loan_id, customer_id, loan_amount, loan_type, interest_rate, duration, status):
        self.cursor.execute('''
        INSERT INTO Loan (loan_id, customer_id, loan_amount, loan_type, interest_rate, duration, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (loan_id, customer_id, loan_amount, loan_type, interest_rate, duration, status))
        self.connection.commit()

    def add_investment(self, investment_id, customer_id, investment_type, amount, risk_level):
        self.cursor.execute('''
        INSERT INTO Investment (investment_id, customer_id, investment_type, amount, risk_level)
        VALUES (%s, %s, %s, %s, %s)
        ''', (investment_id, customer_id, investment_type, amount, risk_level))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db = DatabaseManager(host="localhost", user="root", password="your_password", database="banking_management")

    # Add a customer
    db.add_customer("CUST123", "Jane Doe", "456 Maple Avenue, London", "+44 123 987 6543", "janedoe@example.com")

    # Add an account for the customer
    db.add_account("ACC2001", "CUST123", "savings", 10000.0)

    # Record a transaction
    db.record_transaction("TXN1001", "ACC2001", 500.0, "deposit")

    # Add a loan for the customer
    db.add_loan("LOAN3001", "CUST123", 50000.0, "home", 3.5, 240, "approved")

    # Add an investment for the customer
    db.add_investment("INV4001", "CUST123", "stocks", 2000.0, "medium")

    # Close the database connection
    db.close_connection()
