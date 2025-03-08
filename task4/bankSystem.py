# Banking System Simulation (Multilevel & Method Overriding)
# Class: BankAccount, SavingsAccount, PremiumSavingsAccount
# Attributes: owner_name, account_number, account_holder (public), _balance (protected), __pin (private)
# Methods: deposit(), withdraw(), check_balance(), get_balance(), set_balance(), verify_pin()

class BankAccount:  # basic bank account
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if self.verify_pin(pin):
            self._balance += amount
            print(f"{self.owner} deposited ${amount}. New balance: ${self._balance}")

    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                print(f"{self.owner} withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Insufficient funds!")

    def show_info(self):
        return f"{self.owner} balance: ${self._balance}"

    def verify_pin(self, pin):
        if pin != self.__pin:
            print("Invalid PIN!")
            return False
        return True


class SavingsAccount(BankAccount):  # overrides the `withdraw` method to enforce a withdrawal limit of `$500` per transaction
    def __init__(self, owner, balance, pin):
        super().__init__(owner, balance, pin)

    def withdraw(self, amount, pin):
        if amount > 500:
            print("Withdrawal limit exceeded for Savings Account. Maximum allowed is $500.")
            return
        super().withdraw(amount, pin)


class PremiumSavingsAccount(SavingsAccount):  # increases the withdrawal limit to `$2000`
    def __init__(self, owner, balance, pin):
        super().__init__(owner, balance, pin)

    def withdraw(self, amount, pin):
        if amount > 2000:
            print("Withdrawal limit exceeded for Premium Savings Account. Maximum allowed is $2000.")
            return
        # Call the withdraw method from the BankAccount class directly
        BankAccount.withdraw(self, amount, pin)


# Main program to manage accounts
accounts = []

while True:
    print("--Menu--")
    print("1. List Accounts")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        for index, account in enumerate(accounts):
            print(f"{index} - {account.show_info()}")

    elif menu == "2":
        account_type = input("Choose account type (1: BankAccount, 2: SavingsAccount, 3: PremiumSavingsAccount): ")
        name = input("Insert name: ")
        balance = int(input("Insert balance: "))
        pin = int(input("Insert PIN: "))
        
        if account_type == "1":
            accounts.append(BankAccount(name, balance, pin))
        elif account_type == "2":
            accounts.append(SavingsAccount(name, balance, pin))
        elif account_type == "3":
            accounts.append(PremiumSavingsAccount(name, balance, pin))
        else:
            print("Invalid account type!")

    elif menu == "3":
        index = int(input("Choose account index: "))
        amount = int(input("Insert deposit amount: "))
        pin = int(input("Insert PIN: "))
        accounts[index].deposit(amount, pin)

    elif menu == "4":
        index = int(input("Choose account index: "))
        amount = int(input("Insert withdraw amount: "))
        pin = int(input("Insert PIN: "))
        accounts[index].withdraw(amount, pin)

    elif menu == "5":
        break

    else:
        print("Invalid choice")