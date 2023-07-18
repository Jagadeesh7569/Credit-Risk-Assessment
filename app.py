import streamlit as st

def main():
    st.title("Credit Application Form")

    month = st.select_slider("Month", options=[1, 2, 3, 4, 5, 6, 7, 8])
    age = st.text_input("Age", value="")
    ssn = st.text_input("SSN", value="")
    occupation = st.selectbox("Occupation", options=["Accountant", "Architect", "Developer", "Doctor", "Engineer",
                                                    "Entrepreneur", "Journalist", "Lawyer", "Manager", "Mechanic",
                                                    "Media_Manager", "Musician", "Scientist", "Teacher", "Writer"])
    annual_income = st.text_input("Annual Income", value="")
    monthly_inhand_salary = st.text_input("Monthly Inhand Salary", value="")
    num_bank_accounts = st.text_input("Number of Bank Accounts", value="")
    num_credit_cards = st.text_input("Number of Credit Cards", value="")
    interest_rate = st.text_input("Interest Rate", value="")
    num_of_loans = st.text_input("Number of Loans", value="")
    delay_from_due_date = st.text_input("Delay from Due Date", value="")
    num_of_delayed_payments = st.text_input("Number of Delayed Payments", value="")
    changed_credit_limit = st.text_input("Changed Credit Limit", value="")
    num_credit_inquiries = st.text_input("Number of Credit Inquiries", value="")
    credit_mix = st.selectbox("Credit Mix", options=["Bad", "Good", "Standard"])
    credit_score = st.selectbox("Credit Score", options=["Good", "Poor", "Standard"])
    payment_behavior = st.selectbox("Payment Behavior",
                                    options=["High_spent_Large_value_payments", "High_spent_Medium_value_payments",
                                             "High_spent_Small_value_payments", "Low_spent_Large_value_payments",
                                             "Low_spent_Medium_value_payments", "Low_spent_Small_value_payments"])
    payment_of_min_amount = st.selectbox("Payment of Minimum Amount", options=["NM", "No", "Yes"])

    submit_button = st.button("Submit")

    if submit_button:
        # Process the form data
        process_form_data(month, age, ssn, occupation, annual_income, monthly_inhand_salary, num_bank_accounts,
                          num_credit_cards, interest_rate, num_of_loans, delay_from_due_date,
                          num_of_delayed_payments, changed_credit_limit, num_credit_inquiries, credit_mix,
                          credit_score, payment_behavior, payment_of_min_amount)

def process_form_data(month, age, ssn, occupation, annual_income, monthly_inhand_salary, num_bank_accounts,
                      num_credit_cards, interest_rate, num_of_loans, delay_from_due_date, num_of_delayed_payments,
                      changed_credit_limit, num_credit_inquiries, credit_mix, credit_score, payment_behavior,
                      payment_of_min_amount):
    # Process the data here
    # You can perform calculations, validations, or send the data to a backend server

    # Example: Printing the form data
    print(f"Month: {month}")
    print(f"Age: {age}")
    print(f"SSN: {ssn}")
    print(f"Occupation: {occupation}")
    print(f"Annual Income: {annual_income}")
    print(f"Monthly Inhand Salary: {monthly_inhand_salary}")
    print(f"Number of Bank Accounts: {num_bank_accounts}")
    print(f"Number of Credit Cards: {num_credit_cards}")
    print(f"Interest Rate: {interest_rate}")
    print(f"Number of Loans: {num_of_loans}")
    print(f"Delay from Due Date: {delay_from_due_date}")
    print(f"Number of Delayed Payments: {num_of_delayed_payments}")
    print(f"Changed Credit Limit: {changed_credit_limit}")
    print(f"Number of Credit Inquiries: {num_credit_inquiries}")
    print(f"Credit Mix: {credit_mix}")
    print(f"Credit Score: {credit_score}")
    print(f"Payment Behavior: {payment_behavior}")
    print(f"Payment of Minimum Amount: {payment_of_min_amount}")

if __name__ == "__main__":
    main()
