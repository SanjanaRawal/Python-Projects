class BankAccount :
    def __init__(self , account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self , amount):
        if amount > 0 :
            self.balance += amount
            print(f"Amount deposited : {amount}")
            print(f"Bank balance after deposit :{self.balance} ")
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

    def check_balance(self):
        print(f"Your current bank balance is : {self.balance}")

print("Welcome to the banking system")
name = input("Enter your name : ")
account= BankAccount(name)

while True :
    print("\n****Menu****\n")
    print("1.Deposit \n2.Withdraw \n3.Check balance \n4.Exit\n")
    ch = int(input("Enter choice (1-4) : "))
    if ch==1 :
        amount = float(input("Enter amount to be deposited : "))
        account.deposit(amount)
    elif ch==2 :
        amount = float(input("Enter amount to be withdrawn : "))
        account.withdraw(amount)
    elif ch==3 :
        account.check_balance()
    elif ch==4 :
        print("Exiting system....")
        break
    else :
        print("Invalid choice , choose again")

