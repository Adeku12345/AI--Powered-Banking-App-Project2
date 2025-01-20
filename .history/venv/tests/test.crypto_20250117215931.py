import unittest

class TestCryptoConversion(unittest.TestCase):

    def setUp(self):
        # Setup initial conditions for the test
        self.bank_account = BankAccount("123456789", 5000.00)  # A bank account with 5000 USD
        self.crypto_account = CryptoAccount(self.bank_account, 2.0)  # 2 BTC in the crypto account
        self.conversion_rate_manager = ConversionRateManager()  # Initialize the conversion rate manager

    def test_crypto_conversion_btc_to_eth(self):
        # Test converting 1 BTC to ETH
        result = self.crypto_account.convert_crypto(1.0, "BTC", "ETH", self.conversion_rate_manager)
        self.assertEqual(result, "Converted 1.0 BTC to 1.5000 ETH")  # 1 BTC = 1.5 ETH based on exchange rates
        self.assertEqual(self.crypto_account.get_crypto_balance(), 3.5)  # Crypto balance should be updated (2 + 1.5)

    def test_crypto_conversion_eth_to_btc(self):
        # Test converting 1 ETH to BTC
        result = self.crypto_account.convert_crypto(1.0, "ETH", "BTC", self.conversion_rate_manager)
        self.assertEqual(result, "Converted 1.0 ETH to 0.6667 BTC")  # 1 ETH = 0.6667 BTC based on exchange rates
        self.assertEqual(self.crypto_account.get_crypto_balance(), 2.6667)  # Crypto balance should be updated (2 + 0.6667)

    def test_crypto_conversion_invalid(self):
        # Test invalid conversion (unsupported crypto pair)
        result = self.crypto_account.convert_crypto(1.0, "BTC", "XRP", self.conversion_rate_manager)
        self.assertEqual(result, "Cannot convert BTC to XRP")
        self.assertEqual(self.crypto_account.get_crypto_balance(), 2.0)  # Crypto balance should remain unchanged

if __name__ == '__main__':
    unittest.main()
