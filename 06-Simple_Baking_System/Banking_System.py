import json
import os

class BankAccount:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited : Rs {amount}")
            print(f"Bank balance after deposit : Rs {self.balance}")
            self.transactions.append(f"Deposited Rs {amount}")
            self.save_data()
        else:
            print("Invalid deposit amount entered")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount entered")
        else:
            print(f"Amount withdrawn : Rs {amount}")
            self.balance -= amount
            print(f"Bank balance after withdrawal : Rs {self.balance}")
            self.transactions.append(f"Withdrawn Rs {amount}")
            self.save_data()

    def check_balance(self):
        print(f"Your current bank balance is : {self.balance}")

    def show_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions made yet.")
        else:
            for i in range(len(self.transactions)):
                print(i + 1, "\t", self.transactions[i])

    def save_data(self):
        data = {
            "username": self.username,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions
        }
        with open(f"{self.username}.json", "w") as f:
            json.dump(data, f)

    @classmethod
    def load_data(cls, username, pin):
        filename = f"{username}.json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                account = cls(data["username"], data["pin"])
                account.balance = data["balance"]
                account.transactions = data["transactions"]
                if account.pin == pin:
                    return account
        return None


print("Welcome to the banking system!")
account = None


def manage():
    while True:
        print("\n**** Menu ****")
        print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Show Transactions\n5. Exit")

        try:
            ch = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Invalid input! Enter a number between 1-5.")
            continue

        if ch == 1:
            amount = float(input("Enter amount to deposit: Rs "))
            account.deposit(amount)
        elif ch == 2:
            amount = float(input("Enter amount to withdraw: Rs "))
            account.withdraw(amount)
        elif ch == 3:
            account.check_balance()
        elif ch == 4:
            account.show_transactions()
        elif ch == 5:
            print("Exiting system... Thank you for using our bank.")
            break
        else:
            print("Invalid choice! Try again.")


while True:
    choice = int(input("\nAlready have an account? (Login) (1)\nDon't have an account? (Signup) (2)\nEnter your choice: "))

    if choice == 2:  # Signup
        print("\nCreate the account - \n")
        username = input("Enter username: ")
        while True:
            pin = input("Enter 4-digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                account = BankAccount(username, pin)
                account.save_data()
                print(f"\nHello {username}, your account is successfully created.")
                manage()
                break
            else:
                print("Invalid input, PIN must be a 4-digit number.")
        break

    elif choice == 1:  # Login
        print("\nPlease login to continue - \n")
        attempts = 3
        while attempts > 0:
            username = input("Enter username: ")
            pin = input("Enter PIN: ")
            account = BankAccount.load_data(username, pin)
            if account:
                print(f"\nLogin successful! Welcome back, {username}.\n")
                manage()
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Invalid credentials. Attempts left: {attempts}\n")
                else:
                    print("\nToo many failed login attempts. Your account is temporarily blocked.")
        break

    else:
        print("Invalid choice. Enter 1 or 2.")
