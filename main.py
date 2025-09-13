class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Adds the specified amount to the account balance 
        self.balance += amount 
        return "The new balance after adding " + str(amount)  + ", is " + str(self.balance) + "NOK"
    
    def withdraw(self, amount):
        # Subtracts the specified amount from the balance, if sufficient funds exist. 
        # If not, print a message indicating insufficient funds
        if amount > balance: 
            return "Insufficient funds for this withdrawal"
        else: 
            balance -= amount
            return str(amount) + "NOK withdrawn from account. Remaining funds: " + str(balance) + "NOK"
        
    def account_info(self):
        # Return the account holders name and balance 
        return "Account information: \n" + "Name: " + str(self.account_holder) + "\n" + "Balance: " + str(self.balance)
    
    
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self, interest_rate):
        # Applies interest to the balance (increase the balance by multiplying it by (1 + interest rate)
        self.balance *= (interest_rate / 100) # Balance multiplied by interest rate 3/100
        return self.balance
    

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, transaction_fee):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee # A fixed fee (e.g., $1) that is charged for every withdrawal.

    def withdraw(self, transaction_fee):
        # This method overrides the base class method to subtract 
        

        # the transaction fee in addition to the withdrawn amount.

        
        

