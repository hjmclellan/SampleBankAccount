class User:	
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

class UserCatalog:
    def __init__(self):
        self.userList={}

class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance = (self.int_rate*self.balance)+self.balance
        return self

#return to this later; needs tweaking for this application
    '''def transfer_money(self, name, amount):
        self.balance -= amount
        name.account.balance += amount
        print("Money transfer successful! New balances:")
        print(f"User:{self.name}, Balance: ${self.account_balance}")
        print(f"User:{name.name}, Balance: ${name.account_balance}")'''

scott = User("Scott Knight","msk@cornbell.edu", BankAccount())
martin = User("Martin Light","uniduck@carvana.com", BankAccount())
david = User("David Canty","garnet@uni.com", BankAccount())

#sample
scott.account.deposit(500).yield_interest().display_account_info()

#Is there a way to assign random account numbers to associate with a user? requires more work

