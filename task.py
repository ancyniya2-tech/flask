class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful!")
        print("New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
            print("New balance:", self.balance)
        else:
            print("Insufficient funds!")

    def display_info(self):
        print("Account Number:", self.account_number)
        print("Owner Name:", self.owner_name)
        print("Balance:", self.balance)
        print("Date Opened:", self.date_opened)

        



account1 = BankAccount("001234",5000,"Ancy Niya","25 August 2026")
print(type(account1))
print(account1.account_number)
print(account1.balance)
print(account1.owner_name)
print(account1.date_opened)
account1.deposit(2000)
account1.withdraw(1000)
account1.display_info()

print("--------------------------------------------------")

account2 = BankAccount("005678",10000,"Jane Doe","25 August 2026")
print(type(account2))
print(account2.account_number)
print(account2.balance)
print(account2.owner_name)
print(account2.date_opened)
account2.deposit(2000)
account2.withdraw(2000)
account2.display_info()