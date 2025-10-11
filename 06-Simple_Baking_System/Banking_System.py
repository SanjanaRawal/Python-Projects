class BankAccount :
    def __init__(self , account_holder):
        self.account_holder = account_holder
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
            for i in self.transactions :
                print(i)


print("Welcome to the banking system")
name = input("Enter your name : ")
account= BankAccount(name)

while True :
    print("\n****Menu****\n")
    print("1.Deposit \n2.Withdraw \n3.Check balance \n4.Show transactions \n5.Exit\n")
    ch = int(input("Enter choice (1-5) : "))
    if ch==1 :
        amount = float(input("Enter amount to be deposited (in Rs) : "))
        account.deposit(amount)
    elif ch==2 :
        amount = float(input("Enter amount to be withdrawn (in Rs) : "))
        account.withdraw(amount)
    elif ch==3 :
        account.check_balance()
    elif ch==4 :
        account.show_transactions()
    elif ch==5 :
        print("Exiting system....")
        break
    else :
        print("Invalid choice , choose again")

