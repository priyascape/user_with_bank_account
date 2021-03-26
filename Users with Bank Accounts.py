from random import randint
import sys
sys.path.append(".")
from BankAccount import *

class Deposit:
    def __init__(self, name, email, balance):
        # print("test")
        self.name = name
        self.email = email
        self.account_balance = BankAccount(name = name, balance = 0, int_rate = 0.01)

    def make_deposit(self, amount):
        self.account_balance.deposit(amount)
        return self

    def make_withdrawal (self, amount):
        self.account_balance.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def printMe(self):
        print (f"Mr. {self.name} has {self.account_balance.account_balance} available in his account")


michealDeposit = Deposit(name = "Micheal", email = "mich@bbnt.com", balance=0)
michealDeposit.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).printMe()

johnDeposit=Deposit(name="John", email = "john@bbnt.com", balance=0)
johnDeposit.make_deposit(700).make_deposit(300).make_withdrawal(150).make_withdrawal(150).printMe()

jackDeposit=Deposit(name="Jack", email="jack@bbnt.com", balance=0)
jackDeposit.make_deposit(1500).make_withdrawal(120).make_withdrawal(100).make_withdrawal(200).printMe()
