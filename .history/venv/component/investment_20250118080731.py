class InvestmentAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.investments = []  # List to store investment details

    def add_investment(self, investment_name, amount, return_rate):
        if self.balance >= amount:
            self.balance -= amount
            investment = {
                "name": investment_name,
                "amount": amount,
                "return_rate": return_rate  # Annual return rate in percentage
            }
            self.investments.append(investment)
            return f"Invested {amount} in {investment_name}. Remaining balance: {self.balance}."
        return "Insufficient balance for investment."

    def calculate_returns(self):
        total_returns = 0
        for investment in self.investments:
            annual_return = investment["amount"] * (investment["return_rate"] / 100)
            total_returns += annual_return
        return total_returns


def manage_investment(account, investment_name, amount, return_rate):
    # Step 1: Add investment
    result = account.add_investment(investment_name, amount, return_rate)
    if "Insufficient balance" in result:
        return result

    # Step 2: Calculate potential returns
    total_returns = account.calculate_returns()
    return f"{result} Potential annual returns from all investments: {total_returns}."


# Example usage
if __name__ == "__main__":
    
    user_card = Card(
    card_number="1234-5678-9876-5432",
    card_holder_name="John Doe",
    expiry_date="12/25",
    cvv="123",
    balance=5000.00
)

# Example usage
print(f"Card Holder: {user_card.card_holder_name}, Balance: ${user_card.balance}")

# Payment attempt using card
payment_amount = 1500.00
entered_cvv = "123"
entered_expiry_date = "12/25"

result = process_card_payment(user_card, payment_amount, entered_cvv, entered_expiry_date)
print(result)

#Sample crypto wallet details
user_wallet = CryptoWallet(
wallet_address="0xABC123DEF456",
balance=2.5  # Crypto balance (e.g., in Bitcoin or Ethereum)
)

# Payment attempt using crypto
fiat_amount = 1500.00
conversion_rate = 30000.00  # Example: 1 crypto = $30,000

crypto_result = process_crypto_payment(user_wallet, fiat_amount, conversion_rate)
print(crypto_result)

# Sample investment account details
investment_account = InvestmentAccount(
acccount_holder="John Doe",
balance=10000.00
)

# Investment attempt
investment_name = "Tech Fund"
investment_amount = 3000.00
return_rate = 8.0  # 8% annual return rate

investment_result = manage_investment(investment_account, investment_name, investment_amount, return_rate)
print(investment_result)
    
    
# Machine Learning: Investment Recommendation
def recommend_investments(customer_profile):
    model = LinearRegression()

# Example training (replace with actual data)
x_train = np.array([[25, 5000], [40, 20000], [35, 15000]])  # [Age, Savings]
y_train = np.array(["High Risk", "Low Risk", "Medium Risk"])  # Investment Categories

# Fit the model
model.fit(X_train, np.arange(len(y_train)))  # Encoding categories

# Prediction
risk_index = round(model.predict([customer_profile])[0])
return y_train[risk_index]    # Payment attempt using card

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

# Sample investment account details
investment_account = InvestmentAccount(
account_holder="John Doe",
balance=10000.00
    )

    # Investment attempt
    investment_name = "Tech Fund"
    investment_amount = 3000.00
    return_rate = 8.0  # 8% annual return rate

    investment_result = manage_investment(investment_account, investment_name, investment_amount, return_rate)
    print(investment_result)
    
    
    # Machine Learning: Investment Recommendation
def recommend_investments(customer_profile):
    model = LinearRegression()

    # Example training (replace with actual data)
    X_train = np.array([[25, 5000], [40, 20000], [35, 15000]])  # [Age, Savings]
    y_train = np.array(["High Risk", "Low Risk", "Medium Risk"])  # Investment Categories

    # Fit the model
    model.fit(X_train, np.arange(len(y_train)))  # Encoding categories

    # Prediction
    risk_index = round(model.predict([customer_profile])[0])
    return y_train[risk_index]


# Agentic AI: Interactive Loan and Investment Assistance
def create_agentic_ai_interface():
    llm = OpenAI()
    tools = [
        Tool(
            name="Loan Approval Predictor",
            func=lambda inputs: predict_loan_approval(inputs),
            description="Predicts loan approval based on customer data."
        ),
        Tool(
            name="Investment Recommender",
            func=lambda inputs: recommend_investments(inputs),
            description="Recommends investment options based on customer profile."
        )
    ]
    agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")
    return agent


# Generative AI: Investment and Loan Reports
def generate_customer_feedback(prompt):
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    