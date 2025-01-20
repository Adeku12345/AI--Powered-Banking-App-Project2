import unittest

class TestLoanAccount(unittest.TestCase):

    def setUp(self):
        # Setup initial conditions for the test
        self.bank_account = BankAccount("123456789", 5000.00)  # A bank account with 5000 balance
        self.loan_account = LoanAccount(self.bank_account, 3000.00, 0.05)  # A loan of 3000 with 5% interest

    def test_loan_approval_success(self):
        # Test that loan is approved if the account balance is sufficient
        result = self.loan_account.approve_loan()
        self.assertEqual(result, "Loan Approved")

    def test_loan_approval_failure(self):
        # Test that loan is denied if the account balance is insufficient
        self.bank_account.balance = 200  # Insufficient balance for loan approval
        result = self.loan_account.approve_loan()
        self.assertEqual(result, "Loan Denied")

    def test_make_payment_success(self):
        # Test that a payment towards the loan is successful
        result = self.loan_account.make_payment(1000.00)  # Making a payment of 1000
        self.assertEqual(result, "Payment of 1000.0 successful. Remaining balance: 2000.0")
        self.assertEqual(self.loan_account.get_loan_balance(), 2000.00)

    def test_make_payment_exceeding_balance(self):
        # Test that payment greater than the loan balance is not allowed
        result = self.loan_account.make_payment(3500.00)  # Trying to pay more than the remaining loan balance
        self.assertEqual(result, "Payment exceeds loan balance. Remaining balance: 3000.0")
        self.assertEqual(self.loan_account.get_loan_balance(), 3000.00)  # Balance should remain the same

    def test_loan_balance_after_payment(self):
        # Test loan balance after multiple payments
        self.loan_account.make_payment(500.00)  # First payment of 500
        self.loan_account.make_payment(200.00)  # Second payment of 200
        self.assertEqual(self.loan_account.get_loan_balance(), 2300.00)  # Remaining balance should be 2300

if __name__ == '__main__':
    unittest.main()
