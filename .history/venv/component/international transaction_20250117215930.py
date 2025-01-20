class InternationalTransaction(Transaction):
    def __init__(self, transaction_id, sender, receiver, amount, currency, exchange_rate, transaction_type, date):
        super().__init__(transaction_id, sender, receiver, amount, transaction_type, date)
        self.currency = currency
        self.exchange_rate = exchange_rate

    def convert_currency(self):
        # Convert the amount to the target currency based on the exchange rate
        return self.amount * self.exchange_rate

    def display_transaction_details(self):
        converted_amount = self.convert_currency()
        return (super().display_transaction_details() +
                f"\nCurrency: {self.currency}\n"
                f"Exchange Rate: {self.exchange_rate}\n"
                f"Converted Amount: {converted_amount:.2f}")


def process_international_transaction(sender, receiver, amount, currency, exchange_rate, transaction_type):
    from datetime import datetime
    transaction_id = f"INTL{datetime.now().strftime('%Y%m%d%H%M%S')}"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if sender.balance < amount:
        return "Insufficient funds for the transaction."

    sender.balance -= amount
    converted_amount = amount * exchange_rate
    receiver.balance += converted_amount

    intl_transaction = InternationalTransaction(transaction_id, sender.card_holder_name, receiver.card_holder_name, amount, currency, exchange_rate, transaction_type, date)
    return intl_transaction.display_transaction_details()
