import unittest

class TestCardPayment(unittest.TestCase):

    def setUp(self):
        # Setup initial conditions for tests
        self.account = BankAccount("123456789", 500.00)  # A bank account with 500 balance
        self.card_payment = CardPayment("4111111111111111", self.account)

    def test_payment_successful(self):
        # Test that payment is successful when balance is sufficient
        result = self.card_payment.make_payment(200.00)
        self.assertEqual(result, "Payment Successful")
        self.assertEqual(self.account.get_balance(), 300.00)  # Balance should be reduced by 200

    def test_payment_insufficient_funds(self):
        # Test that payment fails when there are insufficient funds
        result = self.card_payment.make_payment(600.00)
        self.assertEqual(result, "Insufficient funds")
        self.assertEqual(self.account.get_balance(), 500.00)  # Balance should remain the same

    def test_payment_exact_balance(self):
        # Test that payment works when amount is exactly equal to balance
        result = self.card_payment.make_payment(500.00)
        self.assertEqual(result, "Payment Successful")
        self.assertEqual(self.account.get_balance(), 0.00)  # Balance should be 0 after payment

if __name__ == '__main__':
    unittest.main()
