class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance
    
    def deposit(self,dep_value):
        self.balance += dep_value
        return self
    def withdraw(self,withd_value):
        self.balance -= withd_value
        return self
    def dispaly_balance(self):
        print(self.name+' available balance =',self.balance)
        return self
    def transfer_within_arabbank(self, account_name, amount):
        self.balance -= amount
        account_name.balance += amount
        return self


huthifa = User('Huthifa Alqasim','huthifa2013@live.com',10000)
maher   = User('Maher Ahmad','Maher1999@live.com')
baheej  = User('Baheej', 'OMG@outlook.com',103346)

huthifa.deposit(100).deposit(300).deposit(600).withdraw(500).dispaly_balance()
maher.deposit(100).deposit(200).withdraw(300).dispaly_balance()
baheej.deposit(3.12313).withdraw(3412).withdraw(12).withdraw(234.2345).dispaly_balance()

huthifa.dispaly_balance(), baheej.dispaly_balance()

baheej.transfer_within_arabbank(huthifa, 89000)
print('transfering...')
import time
time.sleep(6)
huthifa.dispaly_balance(), baheej.dispaly_balance()
