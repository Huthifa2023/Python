class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance
    
    def deposit(self,dep_value):
        self.balance += dep_value
    def withdraw(self,withd_value):
        self.balance -= withd_value
    def dispaly_balance(self):
        print(self.name+'available balance =',self.balance)
    def transfer_within_arabbank(self, account_name, amount):
        self.balance -= amount
        account_name.balance += amount


huthifa = User('Huthifa Alqasim','huthifa2013@live.com',10000)
maher   = User('Maher Ahmad','Maher1999@live.com')
baheej  = User('Baheej', 'OMG@outlook.com',89346)

# huthifa.deposit(100), huthifa.deposit(300), huthifa.deposit(600), huthifa.withdraw(500), huthifa.dispaly_balance()
# maher.deposit(100), maher.deposit(200), maher.withdraw(300), maher.dispaly_balance()
# baheej.deposit(3.12313), baheej.withdraw(3412), baheej.withdraw(23982), baheej.withdraw(234.2345), baheej.dispaly_balance()

huthifa.dispaly_balance(), baheej.dispaly_balance()

baheej.transfer_within_arabbank(huthifa, 89000)
print('transfering...')
import time
time.sleep(6)
huthifa.dispaly_balance(), baheej.dispaly_balance()
