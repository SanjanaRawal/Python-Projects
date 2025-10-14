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
            print("Your transactions are as follows : ")
            for i in range(len(self.transactions)):
                print(i + 1, "\t", self.transactions[i])

    def apply_interest(self , rate=2.5):
        if self.balance <= 0 :
            print("NO balance present in the account to apply interest")
            return
        interest = (self.balance * rate) / 100
        self.balance += interest
        self.transactions.append(f"Interest added : Rs{interest} with interest rate {rate}%")
        self.save_data()
        print(f"Interest of Rs{interest} successfully added at rate {rate}%")
        
    def transfer_money(self , receiver_username , amount):
        receiver_file = f"{receiver_username}.json"
        if not os.path.exists(receiver_file) :
            print("Receiver account doesn't exist")
            return
        if amount <= 0 :
            print("Invalid transferring amount entered")
            return
        if amount > self.balance :
            print("Insufficient balance in the account.")
            return
        self.balance -= amount
        self.transactions.append(f"Transferred Rs{amount} to {receiver_username}")
        self.save_data()
        with open(receiver_file , "r") as f :
            receiver_data = json.load(f)
        receiver_data["balance"] += amount
        receiver_data["transactions"].append(f"Received Rs {amount} from {self.username}")
        with open(receiver_file , "w") as f :
            json.dump(receiver_data , f)
        print(f"Successfully transferred Rs{amount} from {self.username} to {receiver_username}")

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

def manage(account):
    while True:
        print("\n**** Menu ****")
        print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Show Transactions\n5. Apply Interest\n6.Transfer Money\n7. Exit")

        try:
            ch = int(input("Enter choice (1-7): "))
        except ValueError:
            print("Invalid input! Enter a number between 1-7.")
            continue

        if ch == 1:
            try :
                amount = float(input("Enter amount to deposit: Rs "))
                account.deposit(amount)
            except ValueError :
                print("Invalid input. Please enter a numeric value.")
        elif ch == 2:
            try :
                amount = float(input("Enter amount to withdraw: Rs "))
                account.withdraw(amount)
            except ValueError :
                print("Invalid input. Please enter a numeric value.")
        elif ch == 3:
            account.check_balance()
        elif ch == 4:
            account.show_transactions()
        elif ch==5 :
            try:
                rate = float(input("Enter rate of interest (%) :  "))
                account.apply_interest(rate)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif ch==6 :
            receiver = input("Enter receiver's username : ").strip()
            try:
                amount = float(input("Enter amount to transfer: Rs "))
                account.transfer_money(receiver , amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif ch == 7:
            print("Exiting system... Thank you for using our bank.")
            break
        else:
            print("Invalid choice! Try again.")


print("Welcome to the banking system!")
account = None

while True:
    try :
        choice = int(input("\n1.Already have an account? (Login) \n2.Don't have an account? (Signup) \n3.Exit \nEnter your choice: "))
    except ValueError :
        print("Invalid Input. Enter 1 , 2 or 3 ")

    if choice == 1:  # Login
        print("\nPlease login to continue - \n")
        blocked_accounts = {}
        while True :
            username = input("Enter username: ").strip()
            pin = input("Enter PIN: ")
            if username not in blocked_accounts :
                blocked_accounts[username] = 3 #initialise 3 attempts for each user in dict
            if blocked_accounts[username]==0 :
                print(f"\nYour account {username} is temporarily blocked due to multiple failed attempts")
                continue
            account = BankAccount.load_data(username , pin)
            if account:
                print(f"\nLogin successful! Welcome back, {username}.\n")
                manage(account)
                break
            else:
                blocked_accounts[username] = blocked_accounts[username]-1
                if blocked_accounts[username] > 0:
                    print(f"Invalid credentials. Attempts left: {blocked_accounts[username]}\n")
                else:
                    print("\nToo many failed login attempts. Your account is temporarily blocked.")
    elif choice == 2:  # Signup
        print("\nCreate the account - \n")
        username = input("Enter username: ").strip()
        if os.path.exists(f"{username}.json"):
            print("Username already exists. Please choose a different username.")
            continue
        while True: #run when user doesn't exist already
            pin = input("Enter 4-digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                account = BankAccount(username, pin)
                account.save_data()
                print(f"\nHello {username}, your account is successfully created.")
                manage(account)
                break
            else:
                print("Invalid input, PIN must be a 4-digit number.")
    elif choice==3  :
        print("Exiting system....")
        break
    else:
        print("Invalid choice. Enter 1 or 2.")
