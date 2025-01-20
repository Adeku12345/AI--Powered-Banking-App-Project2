class Card:
    def __init__(self, card_number, card_holder_name, expiry_date, cvv, balance):
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.balance = balance

    def validate_card(self, entered_cvv, entered_expiry_date):
        if self.cvv == entered_cvv and self.expiry_date == entered_expiry_date:
            return True
        return False

    def deduct_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


def process_card_payment(card, amount, entered_cvv, entered_expiry_date):
    # Step 1: Validate the card
    if not card.validate_card(entered_cvv, entered_expiry_date):
        return "Invalid card details. Payment failed."

    # Step 2: Check for sufficient balance
    if not card.deduct_amount(amount):
        return "Insufficient balance. Payment failed."

    # Step 3: Successful payment
    return f"Payment of {amount} completed successfully. Remaining balance: {card.balance}."


# Example usage
if __name__ == "__main__":
    # Sample card details
    user_card = Card(
        card_number="1234-5678-9876-5432",
        card_holder_name="John Doe",
        expiry_date="12/25",
        cvv="123",
        balance=5000.00
    )

    # Payment attempt
    payment_amount = 1500.00
    entered_cvv = "123"
    entered_expiry_date = "12/25"

    result = process_card_payment(user_card, payment_amount, entered_cvv, entered_expiry_date)
    print(result)
