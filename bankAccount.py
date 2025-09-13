class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Adds the specified amount to the account balance 
        self.balance += amount 
        return "The new balance after depositing " + str(amount)  + " NOK, is " + str(self.balance) + " NOK"
    
    def withdraw(self, amount):
        # Subtracts the specified amount from the balance, if sufficient funds exist. 
        # If not, print a message indicating insufficient funds
        if amount > self.balance: 
            return "Insufficient funds for " + str(amount) + " NOK withdrawal"
        else: 
            self.balance -= amount
            return str(amount) + " NOK withdrawn from account. Remaining funds: " + str(self.balance) + " NOK"
        
    def account_info(self):
        # Return the account holders name and balance 
        return "Account information: \n" + "Name: " + str(self.account_holder) + "\n" + "Balance: " + str(self.balance) + " NOK"
    
    
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Applies interest to the balance (increase the balance by multiplying it by (1 + interest rate)
        self.balance *=(1 + self.interest_rate / 100) # Balance multiplied by interest rate 3/100
        return "Total balance after interest: " + str(self.balance) + " NOK"
    
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, transaction_fee):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee # A fixed fee (e.g., $1) that is charged for every withdrawal.

    def withdraw(self, amount):
        # This method overrides the base class method 
        # To subtract the transaction fee in addition to the withdrawn amount.
        total_withdrawal = self.transaction_fee + amount
         
        # Check if account has sufficient funds
        if total_withdrawal > self.balance: 
            return "Insufficient funds for " + str(total_withdrawal) + " NOK withdrawal (including transaction fee of " + str(self.transaction_fee) + " NOK)"
        else:
            self.balance -= total_withdrawal # Subtracting the transaction fee in addition to the withdrawn amount.
            return str(total_withdrawal) + " NOK withdrawn from account (including transaction fee of " + str(self.transaction_fee) + " NOK). Remaining funds: " + str(self.balance) + "NOK"


# Code for testing the different scenarios for the different classes
# Test BankAccount
print("=== BankAccount Tests ===")
acc1 = BankAccount("Alice", 1000)
print(acc1.account_info())
print()
print(acc1.deposit(500))
print()
print(acc1.withdraw(200))
print()
print(acc1.withdraw(2000)) # should fail because of insufficient funds 
print()
print(acc1.account_info())
print()

# Test SavingsAccount
print("\n=== SavingsAccount Tests ===")
savings = SavingsAccount("Bob", 2000, 5)  # 5% interest
print(savings.account_info())
print()
print(savings.apply_interest())  # apply 5% interest to 2000 NOK -> 2100 NOK
print()
print(savings.deposit(400))
print()
print(savings.withdraw(500))
print()
print(savings.account_info())

# Test CheckingAccount
print("\n=== CheckingAccount Tests ===")
checking = CheckingAccount("Charlie", 1500, 1)  # 1 NOK fee per withdrawal
print(checking.account_info())
print()
print(checking.withdraw(300))   # withdraw 300 + transaction fee 1 = 301 NOk
print()
print(checking.withdraw(2000))  # should fail (not enough funds)
print()
print(checking.deposit(200))
print()
print(checking.withdraw(100))
print()
print(checking.account_info())

        
        

