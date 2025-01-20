from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',        # MySQL host
            user='root',             # MySQL user
            password='password',     # MySQL password
            database='banking'       # The name of the database
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# Initialize database with simple structure if it doesn't exist
def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            balance DECIMAL(10, 2) NOT NULL DEFAULT 0)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS loans (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            account_id INT,
                            loan_amount DECIMAL(10, 2),
                            interest_rate DECIMAL(5, 2),
                            amount_paid DECIMAL(10, 2) DEFAULT 0,
                            FOREIGN KEY (account_id) REFERENCES accounts(id))''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS investments (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            account_id INT,
                            investment_amount DECIMAL(10, 2),
                            return_rate DECIMAL(5, 2),
                            total_value DECIMAL(10, 2),
                            FOREIGN KEY (account_id) REFERENCES accounts(id))''')
        
        conn.commit()
        cursor.close()
        conn.close()

@app.route('/create_account', methods=['POST'])
def create_account():
    name = request.json.get('name')
    initial_balance = request.json.get('balance', 0)
    
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO accounts (name, balance) VALUES (%s, %s)', (name, initial_balance))
        conn.commit()
        cursor.close()
        conn.close()

    return jsonify({"message": f"Account for {name} created with balance {initial_balance}"}), 201

@app.route('/get_balance/<int:account_id>', methods=['GET'])
def get_balance(account_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (account_id,))
        account = cursor.fetchone()
        cursor.close()
        conn.close()

    if account:
        return jsonify({"id": account['id'], "name": account['name'], "balance": account['balance']}), 200
    else:
        return jsonify({"error": "Account not found"}), 404

# Loan Request
@app.route('/request_loan', methods=['POST'])
def request_loan():
    account_id = request.json.get('account_id')
    loan_amount = request.json.get('loan_amount')
    interest_rate = request.json.get('interest_rate')

    if loan_amount <= 0 or interest_rate <= 0:
        return jsonify({"error": "Loan amount and interest rate must be positive"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (account_id,))
        account = cursor.fetchone()
        if account:
            cursor.execute('INSERT INTO loans (account_id, loan_amount, interest_rate) VALUES (%s, %s, %s)', 
                           (account_id, loan_amount, interest_rate))
            new_balance = account['balance'] + loan_amount
            cursor.execute('UPDATE accounts SET balance = %s WHERE id = %s', (new_balance, account_id))
            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({"message": f"Loan of {loan_amount} granted to account {account_id}. New balance: {new_balance}"}), 201
        else:
            cursor.close()
            conn.close()
            return jsonify({"error": "Account not found"}), 404

# Repay Loan
@app.route('/repay_loan', methods=['POST'])
def repay_loan():
    account_id = request.json.get('account_id')
    payment_amount = request.json.get('payment_amount')

    if payment_amount <= 0:
        return jsonify({"error": "Payment amount must be positive"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM loans WHERE account_id = %s', (account_id,))
        loan = cursor.fetchone()

        if loan:
            new_amount_paid = loan['amount_paid'] + payment_amount
            if new_amount_paid > loan['loan_amount'] * (1 + loan['interest_rate'] / 100):
                return jsonify({"error": "Loan already fully repaid"}), 400
            cursor.execute('UPDATE loans SET amount_paid = %s WHERE account_id = %s', (new_amount_paid, account_id))
            cursor.execute('SELECT * FROM accounts WHERE id = %s', (account_id,))
            account = cursor.fetchone()
            new_balance = account['balance'] - payment_amount
            cursor.execute('UPDATE accounts SET balance = %s WHERE id = %s', (new_balance, account_id))
            conn.commit()
            cursor.close()
            conn.close()
            
            return jsonify({"message": f"Loan repaid with {payment_amount}. New balance: {new_balance}"}), 200
        else:
            cursor.close()
            conn.close()
            return jsonify({"error": "No loan found for this account"}), 404

# Make Investment
@app.route('/invest', methods=['POST'])
def invest():
    account_id = request.json.get('account_id')
    investment_amount = request.json.get('investment_amount')
    return_rate = request.json.get('return_rate')

    if investment_amount <= 0 or return_rate <= 0:
        return jsonify({"error": "Investment amount and return rate must be positive"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (account_id,))
        account = cursor.fetchone()
        if account:
            cursor.execute('INSERT INTO investments (account_id, investment_amount, return_rate, total_value) VALUES (%s, %s, %s, %s)', 
                           (account_id, investment_amount, return_rate, investment_amount))
            new_balance = account['balance'] - investment_amount
            cursor.execute('UPDATE accounts SET balance = %s WHERE id = %s', (new_balance, account_id))
            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({"message": f"Investment of {investment_amount} made with return rate {return_rate}. New balance: {new_balance}"}), 201
        else:
            cursor.close()
            conn.close()
            return jsonify({"error": "Account not found"}), 404

# Get Investment Value
@app.route('/get_investment_value/<int:account_id>', methods=['GET'])
def get_investment_value(account_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM investments WHERE account_id = %s', (account_id,))
        investment = cursor.fetchone()
        cursor.close()
        conn.close()

    if investment:
        return jsonify({
            "account_id": account_id,
            "investment_amount": investment['investment_amount'],
            "return_rate": investment['return_rate'],
            "total_value": investment['total_value']
        }), 200
    else:
        return jsonify({"error": "No investment found for this account"}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
