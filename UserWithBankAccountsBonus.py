class User:
    def __init__(self, name, type, email):
        self.name = name
        self.email = email
        self.type = type
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_withdrawal(self, type, amount):
        self.account.balance -= amount
        return self 

    def make_deposit(self, type, amount):
        self.account.balance += amount
        return self
    def display_user_balance(self):
        print(self.account.balance)
        return self
    
    def transfer_money(self, amount, other_user):
        other_user.account.balance += amount
        self.account.balance -= amount
        print(f"Remaining balance after transer: ${self.account.balance}")
        return self

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

# user1 = BankAccount()
# user2 = BankAccount()
# user1.deposit(10).deposit(10).deposit(10).withdraw(10).yield_interest().display_account_info()
# user2.deposit(20).deposit(20).withdraw(10).withdraw(10).withdraw(10).withdraw(5).yield_interest().display_account_info()
# user3 = User("John","test")
# print(user3.name)
# print(user3.account.int_rate)
# print(user3.account.balance)
# user3.make_deposit(100).make_withdrawal(10).display_user_balance()
# print(user3.account.balance)

user4 = User("John", "Checking", "Bob")
user4.make_deposit("Checking",100)
print(user4.name,user4.type,"Balance:",user4.account.balance)

user5 = User("John", "Savings", "Bob")
user5.make_deposit("Savings",200)
print(user5.name,user5.type,"Balance:",user5.account.balance)

user6 = User("Scott", "Savings", "GurdyMail")
user6.make_deposit("Savings",200)
print(user6.name,user6.type,"Balance:",user6.account.balance)

# print(user5.account.balance)
user5.transfer_money(100,user6)
