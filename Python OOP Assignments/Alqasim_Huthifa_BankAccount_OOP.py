class BankAccont:
    def __init__(self, balance = 0, interest_rate=0.02):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_info(self):
        print('the balance is =',self.balance)
        return self
    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self
    
account1 = BankAccont(balance=1000)
account2 = BankAccont()

# account1.display_info(), account2.display_info()

account1.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_info()
account2.deposit(52124).deposit(52124).deposit(52124).deposit(52124).withdraw(1123).yield_interest().display_info()