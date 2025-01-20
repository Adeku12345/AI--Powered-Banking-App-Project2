class FraudDetection:
    def __init__(self):
        self.flagged_transactions = []

    def detect_fraud(self, card):
        # Example rule-based fraud detection
        from datetime import datetime, timedelta

        flagged = []
        now = datetime.now()

        # Rule 1: Multiple transactions within a short period
        short_period = timedelta(minutes=5)
        transaction_times = [
            datetime.strptime(txn["date"], "%Y-%m-%d %H:%M:%S")
            for txn in card.transaction_history
        ]
        transaction_times.sort()
        for i in range(len(transaction_times) - 2):
            if transaction_times[i + 2] - transaction_times[i] <= short_period:
                flagged.append(card.transaction_history[i])

        # Rule 2: Large single transactions
        large_transaction_limit = 5000  # Example limit
        for txn in card.transaction_history:
            if txn["amount"] > large_transaction_limit:
                flagged.append(txn)

        # Rule 3: Transactions in different regions within a short period
        # (This is a placeholder, as we don't have region data here)

        self.flagged_transactions.extend(flagged)
        return flagged

    def display_flagged_transactions(self):
        if not self.flagged_transactions:
            return "No fraudulent transactions detected."
        return "Flagged Transactions:\n" + "\n".join(str(txn) for txn in self.flagged_transactions)


# Example usage
if __name__ == "__main__":
    # Create a card
    user_card = Card(
        card_number="1234-5678-9876-5432",
        card_holder_name="John Doe",
        expiry_date="12/25",
        cvv="123",
        balance=10000.00
    )

    # Perform some transactions
    from time import sleep
    process_card_payment(user_card, 1000, "123", "12/25")
    sleep(1)
    process_card_payment(user_card, 200, "123", "12/25")
    sleep(1)
    process_card_payment(user_card, 6000, "123", "12/25")
    sleep(1)
    process_card_payment(user_card, 100, "123", "12/25")

    # Detect fraud
    fraud_detector = FraudDetection()
    frauds = fraud_detector.detect_fraud(user_card)
    print(fraud_detector.display_flagged_transactions())
