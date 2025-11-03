class BankAcct:
    def __init__(self, acct_name, acct_balance, interest_rate, acct_number):
        #Initializing values for the bank account like the account name, number, balance, and interest rate
        self.acct_name = acct_name
        self.acct_balance = acct_balance
        self.acct_interest_rate = interest_rate
        self.acct_number = acct_number

    def deposit(self, dollars):
        # Deposit money into the account solong as the value of the deposit is positive
        if dollars > 0:
            self.acct_balance += dollars
            print(f"{dollars} successfully deposited.")
        else:
            print("Deposit failed. Amount must be positive.")

    def withdraw(self, dollars):
        #Withdraw money from the account so long as a positive amount is being withdrawn, and there is at-least that much money in the account
        if dollars > self.acct_balance:
            print("Withdraw failed. Insufficient balance.")
        elif dollars <= 0:
            print("Withdraw amount must be positive.")
        else:
            self.acct_balance -= dollars
            print(f"{dollars} successfully withdrawn.")

    def adjust_interest(self, new_rate):
        #Adjust the interest rate of the account
        if new_rate < 0:
            print("Interest rate must be positive.")
        else:
            self.acct_interest_rate = new_rate
            print(f"Interest rate adjusted to {new_rate*100}%")

    def calculate_interest(self, days):
        #Calculates the interest accrued over a set number of days
        if days <= 0:
            print("Number of days must be positive.")
            return 0
        interest = self.acct_balance * self.acct_interest_rate * (days / 365)
        return interest

    def get_balance(self):
        #Returns the current account balance
        return self.acct_balance

    def __str__(self):
        return (f"Account Holder: {self.acct_name}\n"
                f"Account Number: {self.acct_number}\n"
                f"Account Balance: ${self.acct_balance: .2f}\n"
                f"Interest Rate: {self.acct_interest_rate*100:.2f}%\n")

def test_bankacct():
    # Create a BankAcct object
    acct = BankAcct("Ethan Back", 1000, 0.05, "12345678")
    print(acct)

    # Test deposit
    acct.deposit(500)
    print("After deposit:", acct.get_balance())

    # Test withdraw
    acct.withdraw(200)
    print("After withdrawal:", acct.get_balance())

    # Test interest calculation
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    # Adjust interest rate
    acct.adjust_interest(0.07)
    print("After adjusting interest rate:", acct)

    # Test withdrawal exceeding balance
    acct.withdraw(2000)

    # Test invalid deposit
    acct.deposit(-50)

    # Test invalid withdrawal
    acct.withdraw(-100)

# Run test function
if __name__ == "__main__":
    test_bankacct()