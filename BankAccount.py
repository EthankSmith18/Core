class BankAccount:

    bank_name = "Big Bank"
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charding a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self
        else:
            print("Balance is negative")
            return self
    @classmethod
    def print(cls):
        print(cls.bank_name)
    

account1 = BankAccount()
account2 = BankAccount()
account1.deposit(10).deposit(10).deposit(10).withdraw(10).yield_interest().display_account_info()
account2.deposit(20).deposit(20).withdraw(10).withdraw(10).withdraw(10).withdraw(5).yield_interest().display_account_info()
# BankAccount.print()