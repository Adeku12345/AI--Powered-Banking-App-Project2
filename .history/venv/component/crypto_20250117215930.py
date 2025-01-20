class CryptoWallet:
    def __init__(self, wallet_address, balance):
        self.wallet_address = wallet_address
        self.balance = balance

    def convert_and_deduct(self, fiat_amount, conversion_rate):
        crypto_amount = fiat_amount / conversion_rate
        if self.balance >= crypto_amount:
            self.balance -= crypto_amount
            return crypto_amount
        return None


def process_crypto_payment(wallet, fiat_amount, conversion_rate):
    # Step 1: Convert fiat to crypto and deduct
    crypto_amount = wallet.convert_and_deduct(fiat_amount, conversion_rate)
    if crypto_amount is None:
        return "Insufficient crypto balance. Payment failed."

    # Step 2: Successful payment
    return f"Payment of {fiat_amount} completed successfully. Deducted {crypto_amount:.6f} crypto. Remaining crypto balance: {wallet.balance:.6f}."


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

    # Payment attempt using card
    payment_amount = 1500.00
    entered_cvv = "123"
    entered_expiry_date = "12/25"

    result = process_card_payment(user_card, payment_amount, entered_cvv, entered_expiry_date)
    print(result)

    # Sample crypto wallet details
    user_wallet = CryptoWallet(
        wallet_address="0xABC123DEF456",
        balance=2.5  # Crypto balance (e.g., in Bitcoin or Ethereum)
    )

    # Payment attempt using crypto
    fiat_amount = 1500.00
    conversion_rate = 30000.00  # Example: 1 crypto = $30,000

    crypto_result = process_crypto_payment(user_wallet, fiat_amount, conversion_rate)
    print(crypto_result)
