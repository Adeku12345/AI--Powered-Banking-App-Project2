class Transaction:
    def __init__(self, transaction_id, sender, receiver, amount, transaction_type, date):
        self.transaction_id = transaction_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transaction_type = transaction_type  # e.g., "transfer", "deposit", "withdrawal"
        self.date = date

    def display_transaction_details(self):
        return (f"Transaction ID: {self.transaction_id}\n"
                f"Sender: {self.sender}\n"
                f"Receiver: {self.receiver}\n"
                f"Amount: {self.amount}\n"
                f"Transaction Type: {self.transaction_type}\n"
                f"Date: {self.date}")


def process_transaction(sender, receiver, amount, transaction_type):
    from datetime import datetime
    transaction_id = f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if transaction_type == "transfer":
        if sender.balance < amount:
            return "Insufficient funds for the transaction."
        sender.balance -= amount
        receiver.balance += amount
    elif transaction_type == "deposit":
        receiver.balance += amount
    elif transaction_type == "withdrawal":
        if sender.balance < amount:
            return "Insufficient funds for withdrawal."
        sender.balance -= amount
    else:
        return "Invalid transaction type."

    transaction = Transaction(transaction_id, sender.card_holder_name, receiver.card_holder_name, amount, transaction_type, date)
    return transaction.display_transaction_details()
