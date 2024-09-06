class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

# Creating an instance of BankAccount
account = BankAccount(100)

# Accessing balance using a method
print(account.get_balance())  # Output: 100

# Depositing money
account.deposit(50)
print(account.get_balance())  # Output: 150

# Withdrawing money
account.withdraw(30)
print(account.get_balance())  # Output: 120

# Attempting to access the private attribute directly (will raise an AttributeError)
print(account.__balance)  # Commenting or Uncommenting this line will raise an AttributeError