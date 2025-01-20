import unittest
from datetime import datetime, timedelta

class TestFraudDetection(unittest.TestCase):

    def setUp(self):
        # Setup initial conditions for the test
        self.bank_account = BankAccount("123456789", 10000.00)  # A bank account with 10000 balance
        self.fraud_detection = FraudDetection(self.bank_account)

    def test_large_transaction_detection(self):
        # Test that large transactions are flagged as potentially fraudulent
        result = self.fraud_detection.is_fraudulent(6000.00)  # A transaction of 6000 is considered large
        self.assertTrue(result, "Large transactions should be flagged as fraudulent")

    def test_normal_transaction(self):
        # Test that normal transactions are not flagged
        result = self.fraud_detection.is_fraudulent(1000.00)  # A normal transaction of 1000 should not be flagged
        self.assertFalse(result, "Normal transactions should not be flagged as fraudulent")

    def test_unusual_frequency_detection(self):
        # Test that frequent transactions within a short time are flagged as potentially fraudulent
        self.bank_account.withdraw(1000.00)
        self.bank_account.deposit(1000.00)
        self.bank_account.withdraw(1000.00)
        self.bank_account.deposit(1000.00)
        self.bank_account.withdraw(1000.00)  # This is the 5th transaction within a short time (10 minutes)
        
        # Now check if the fraud detection system flags the frequent transactions
        result = self.fraud_detection.is_fraudulent(500.00)
        self.assertTrue(result, "Frequent transactions within a short period should be flagged as fraudulent")

    def test_no_fraud_detection_for_slow_transactions(self):
        # Test that when transactions are spaced out, they're not flagged
        self.bank_account.withdraw(500.00)
        self.bank_account.deposit(1000.00)
        
        # Adding some delay
        future_time = datetime.now() + timedelta(minutes=20)
        self.bank_account.transactions[-1] = ('Deposit', 1000.00, future_time)
        
        result = self.fraud_detection.is_fraudulent(500.00)
        self.assertFalse(result, "Transactions spread over time should not be flagged as fraudulent")

if __name__ == '__main__':
    unittest.main()

