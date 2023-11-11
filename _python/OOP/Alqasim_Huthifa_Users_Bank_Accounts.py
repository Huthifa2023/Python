class Users:
    def __init__(self, name, age='*empty*', email='*empty*'):
        self.name = name
        self.age = age
        self.email = email
        self.account = [BankAccount()]
    def create_account(self):
        self.account.append(BankAccount())
        
    def deposit(self, amount,account_num):
        self.account[account_num].balance += amount
        return self
    def withdraw(self, amount,account_num):
        self.account[account_num].balance -= amount
        return self
    def display_balance(self,account_num):
        print(self.account[account_num].balance)

class BankAccount:
    def __init__(self, balance = 0, int_rate=0.02):
        self.balance = balance
        self.int_rate = int_rate


huthifa = Users('Huthifa')
huthifa.deposit(100,0).deposit(100,0).withdraw(100,0).display_balance(0)
# print(huthifa.account[0])
# huthifa.create_account()
huthifa.create_account()
huthifa.deposit(100,1).deposit(1023423440,1).withdraw(200,1).display_balance(1)

