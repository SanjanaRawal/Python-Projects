class BankAccount :
    def __init__(self , username , pin):
        self.username = username
        self.pin = pin
        self.balance = 0.0
        self.transactions = []

    def deposit(self , amount):
        if amount > 0 :
            self.balance += amount
            print(f"Amount deposited : Rs {amount}")
            print(f"Bank balance after deposit : Rs {self.balance} ")
            self.transactions.append(f"Deposited Rs {amount}")
        else :
            print("Invalid deposit amount entered")

    def withdraw(self , amount):
        if self.balance < amount :
            print("Insufficient balance")
        elif amount <= 0 :
            print("Invalid withdrawal amount entered")
        else :
            print(f"Amount withdrawn : {amount}")
            self.balance -= amount
            print(f"Bank balance after withdrawal : {self.balance} ")
            self.transactions.append(f"Withdrawn Rs {amount}")

    def check_balance(self):
        print(f"Your current bank balance is : {self.balance}")

    def show_transactions(self):
        if len(self.transactions)==0 :
            print("No transactions made yet.")
        else :
            for i in range(0 , len(self.transactions)) :
                print(i+1 , "\t" , self.transactions[i])


print("Welcome to the banking system!")
print("Create the account : \n")

name = input("Enter your name : ")
while True :
    pin = input("Enter 4 digit pin : ")
    if pin.isdigit() and len(pin)==4 :
        break
    else :
        print("Invalid input , Pin must be 4-digit number.")
account= BankAccount(name , pin)
print(f"Hello {name} , your account is successfully created \n")

print("Please login to continue : ")
attempts = 3
while attempts > 0 :
    login_name = input("Enter name : ")
    login_pin = input("Enter pin : ")
    if login_name==account.username and login_pin==account.pin :
        print("Login successful. Here's the menu - ")
        while True:
            print("\n****Menu****\n")
            print("1.Deposit \n2.Withdraw \n3.Check balance \n4.Show transactions \n5.Exit\n")
            ch = int(input("Enter choice (1-5) : "))
            if ch == 1:
                amount = float(input("Enter amount to be deposited (in Rs) : "))
                account.deposit(amount)
            elif ch == 2:
                amount = float(input("Enter amount to be withdrawn (in Rs) : "))
                account.withdraw(amount)
            elif ch == 3:
                account.check_balance()
            elif ch == 4:
                account.show_transactions()
            elif ch == 5:
                print("Exiting system....")
                break
            else:
                print("Invalid choice , choose again")
        break
    else :
        attempts -= 1
        print("Invalid credentials entered. Try again")
else :
    print("Too many failed attempts. Exiting.....")