class LoanApplication:
    def __init__(self, applicant_name, income, credit_score, loan_amount, loan_term, interest_rate):
        self.applicant_name = applicant_name
        self.income = income
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.loan_term = loan_term  # in years
        self.interest_rate = interest_rate  # Annual interest rate in percentage

    def calculate_monthly_repayment(self):
        # Using the formula for monthly repayment: M = P[r(1+r)^n]/[(1+r)^n - 1]
        monthly_rate = self.interest_rate / (12 * 100)
        number_of_payments = self.loan_term * 12
        numerator = self.loan_amount * monthly_rate * (1 + monthly_rate) ** number_of_payments
        denominator = (1 + monthly_rate) ** number_of_payments - 1
        if denominator == 0:
            return "Cannot calculate repayment. Check interest rate and loan term."
        return numerator / denominator

    def check_eligibility(self):
        # UK-specific eligibility rules (example):
        # - Minimum income threshold: £20,000
        # - Minimum credit score: 600
        # - Loan amount cannot exceed 4.5 times annual income
        if self.income < 20000:
            return "Income below the minimum threshold for loan eligibility."
        if self.credit_score < 600:
            return "Credit score too low for loan eligibility."
        if self.loan_amount > 4.5 * self.income:
            return "Loan amount exceeds the permissible limit based on your income."
        return "Eligible for loan."


def process_loan_application(applicant_name, income, credit_score, loan_amount, loan_term, interest_rate):
    loan_application = LoanApplication(applicant_name, income, credit_score, loan_amount, loan_term, interest_rate)

    # Step 1: Check eligibility
    eligibility_result = loan_application.check_eligibility()
    if "Eligible" not in eligibility_result:
        return eligibility_result

    # Step 2: Calculate monthly repayment
    monthly_repayment = loan_application.calculate_monthly_repayment()
    return f"Loan approved for {applicant_name}. Monthly repayment: £{monthly_repayment:.2f}."



# Machine Learning: Loan Approval Prediction
def predict_loan_approval(customer_data):
    model = RandomForestClassifier()
    scaler = StandardScaler()

    # Example training (replace with actual data)
    X_train = np.array([[700, 50000, 0.4], [600, 30000, 0.6], [750, 80000, 0.2]])  # [Credit Score, Income, Debt-to-Income Ratio]
    y_train = np.array([1, 0, 1])  # 1 = Approved, 0 = Rejected

    X_train_scaled = scaler.fit_transform(X_train)
    model.fit(X_train_scaled, y_train)

    # Prediction
    X_test_scaled = scaler.transform([customer_data])
    return "Approved" if model.predict(X_test_scaled)[0] == 1 else "Rejected"

def create_agentic_ai_interface():
    llm = OpenAI()
    tools = [
        Tool(
            name="Loan Approval Predictor",
            func=lambda inputs: predict_loan_approval(inputs),
            description="Predicts loan approval based on customer data."
        ),]
    
    
# Generative AI: Investment and Loan Reports
def generate_customer_feedback(prompt):
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)    

