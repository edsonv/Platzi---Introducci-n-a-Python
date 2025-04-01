class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Account is inactive. Cannot deposit.")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")

    def deactivate(self):
        self.is_active = False
        print("Account deactivated.")

    def activate(self):
        self.is_active = True
        print("Account activated.")


account1 = BankAccount("Alice", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)
account1.deactivate()
account1.deposit(100)
account1.activate()
account1.deposit(100)
account1.withdraw(200)

account2 = BankAccount("Bob", 2000)
account2.deposit(300)
account2.withdraw(500)
account2.withdraw(2500)
account2.deactivate()
account2.deposit(100)
account2.activate()
account2.deposit(100)
account2.withdraw(500)
account2.withdraw(2500)
account2.deactivate()
account2.activate()
