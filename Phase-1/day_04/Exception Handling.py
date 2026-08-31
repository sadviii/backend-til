"""def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Insufficient funds")
        if amount <= 0:
            raise ValueError("Invalid amount")
        
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Withdrawal successful")
withdraw(5000, 1000)
withdraw(5000, -100)
withdraw(5000, 6000)"""

"""class InvalidAgeError(Exception):
    pass
def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError("Age must be at least 18")
    except InvalidAgeError as e:
        print(f"Error: {e}")
    else:
        print("Age accepted ")
check_age(22)
check_age(15)"""

"""Create a Bank Account program.

Requirements

Create:

class BankAccount:

The account should have:

owner
balance

Create a method:

withdraw(amount)

Rules:

If amount <= 0
→ raise a custom InvalidAmountError
If amount > balance
→ raise a custom InsufficientBalanceError
Otherwise:
→ subtract the amount
→ print the remaining balance
Create two custom exceptions:
InvalidAmountError
InsufficientBalanceError

Both should inherit from Exception.

Then test:
Account balance = 5000

withdraw(1000)
withdraw(-100)
withdraw(6000)

Your program should handle the exceptions gracefully instead of crashing."""

class InvalidAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Invalid amount: Amount must be greater than zero.")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient funds: Cannot withdraw more than the current balance.")
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
        except (InvalidAmountError, InsufficientBalanceError) as e:
            print(f"Error: {e}")

# Test the BankAccount class
account = BankAccount("John Doe", 5000)
account.withdraw(1000)
account.withdraw(-100)
account.withdraw(6000)