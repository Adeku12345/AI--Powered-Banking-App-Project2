from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="banking_app"
    )

@app.route('/savings', methods=['GET', 'POST'])
def savings():
    if request.method == 'POST':
        try:
            # Retrieve form data
            account_number = request.form['account_number']
            amount = float(request.form['amount'])
            transaction_type = request.form['transaction_type']

            # Database connection
            db = connect_db()
            cursor = db.cursor()

            # Fetch account details
            cursor.execute("SELECT balance FROM savings_accounts WHERE account_number = %s", (account_number,))
            result = cursor.fetchone()

            if not result:
                flash("Account not found!", "error")
                return redirect(url_for('savings'))

            balance = result[0]

            if transaction_type == 'deposit':
                new_balance = balance + amount
            elif transaction_type == 'withdraw':
                if amount > balance:
                    flash("Insufficient funds!", "error")
                    return redirect(url_for('savings'))
                new_balance = balance - amount
            else:
                flash("Invalid transaction type!", "error")
                return redirect(url_for('savings'))

            # Update balance
            cursor.execute("UPDATE savings_accounts SET balance = %s WHERE account_number = %s", (new_balance, account_number))

            # Log transaction
            cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, date) VALUES (%s, %s, %s, %s)",
                           (account_number, transaction_type, amount, datetime.now()))

            db.commit()
            flash(f"Transaction successful! New balance: {new_balance}", "success")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
        finally:
            cursor.close()
            db.close()

        return redirect(url_for('savings'))

    return render_template('savings.html')

if __name__ == '__main__':
    app.run(debug=True)
