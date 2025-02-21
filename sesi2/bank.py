# Bank Account System
# Class: BankAccount
# Attributes: owner_name, balance, account_number
# Methods: deposit(), withdraw(), check_balance()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")
            
# Creating an account
account1 = BankAccount("Alice", 1000)
account1.deposit(500)
account1.withdraw(300)