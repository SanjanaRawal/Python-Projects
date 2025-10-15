import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

#Bank Account Class - deals with logic
class BankAccount:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited Rs {amount}")
            self.save_data()
            return f"Deposited Rs {amount}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        self.transactions.append(f"Withdrawn Rs {amount}")
        self.save_data()
        return f"Withdrawn Rs {amount}"

    def apply_interest(self, rate=2.5):
        if self.balance <= 0:
            return "No balance to apply interest"
        interest = (self.balance * rate) / 100
        self.balance += interest
        self.transactions.append(f"Interest added: Rs {interest:.2f} at {rate}%")
        self.save_data()
        return f"Interest Rs {interest:.2f} added at {rate}%"

    def transfer_money(self, receiver_username, amount):
        receiver_file = f"{receiver_username}.json"
        if not os.path.exists(receiver_file):
            return "Receiver not found"
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient balance"

        # Deduct from sender's account
        self.balance -= amount
        self.transactions.append(f"Transferred Rs {amount} to {receiver_username}")
        self.save_data()
        # Add to receiver's account
        with open(receiver_file, "r") as f:
            receiver_data = json.load(f)
        receiver_data["balance"] += amount
        receiver_data["transactions"].append(f"Received Rs {amount} from {self.username}")
        with open(receiver_file, "w") as f:
            json.dump(receiver_data, f)

        return f"Transferred Rs {amount} to {receiver_username}"

    def check_balance(self):
        return f"Your current balance: Rs {self.balance:.2f}"

    def show_transactions(self):
        if not self.transactions:
            return "No transactions yet."
        return "\n".join(self.transactions[-10:])  # last 10 transactions

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
                if data["pin"] == pin:
                    account = cls(data["username"], data["pin"])
                    account.balance = data["balance"]
                    account.transactions = data["transactions"]
                    return account
        return None


#Banking App class - deals with GUI
class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Banking System")
        self.root.geometry("400x400")
        self.account = None
        self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #login/signup
    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="🏦 Smart Banking System", font=("Arial", 14, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="PIN:").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()

        def login():
            username = username_entry.get().strip()
            pin = pin_entry.get().strip()
            account = BankAccount.load_data(username, pin)
            if account:
                self.account = account
                messagebox.showinfo("Login", f"Welcome back, {username}!")
                self.dashboard()
            else:
                messagebox.showerror("Error", "Invalid credentials")

        def signup():
            username = username_entry.get().strip()
            pin = pin_entry.get().strip()
            if os.path.exists(f"{username}.json"):
                messagebox.showerror("Error", "Username already exists!")
                return
            if not pin.isdigit() or len(pin) != 4:
                messagebox.showerror("Error", "PIN must be 4 digits")
                return
            account = BankAccount(username, pin)
            account.save_data()
            messagebox.showinfo("Signup", "Account created successfully!")
            self.account = account
            self.dashboard()

        tk.Button(self.root, text="Login", command=login).pack(pady=10)
        tk.Button(self.root, text="Sign Up", command=signup).pack(pady=5)

    #dashboard
    def dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Welcome, {self.account.username}!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"Balance: Rs {self.account.balance:.2f}", font=("Arial", 12)).pack(pady=5)

        tk.Button(self.root, text="Deposit", command=self.deposit_window, width=20).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_window, width=20).pack(pady=5)
        tk.Button(self.root, text="Check Transactions", command=self.show_transactions, width=20).pack(pady=5)
        tk.Button(self.root, text="Apply Interest", command=self.apply_interest, width=20).pack(pady=5)
        tk.Button(self.root, text="Transfer Money", command=self.transfer_window, width=20).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen, width=20).pack(pady=10)

    # different tasks

    def deposit_window(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount:")
        if amount is not None:
            msg = self.account.deposit(amount)
            if "Deposited" in msg:
                messagebox.showinfo("Success", msg)
            else:
                messagebox.showerror("Error", msg)
            self.dashboard()

    def withdraw_window(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount:")
        if amount is not None:
            msg = self.account.withdraw(amount)
            if "Withdrawn" in msg:
                messagebox.showinfo("Success", msg)
            else:
                messagebox.showerror("Error", msg)
            self.dashboard()

    def show_transactions(self):
        msg = self.account.show_transactions()
        messagebox.showinfo("Transactions", msg)

    def apply_interest(self):
        rate = simpledialog.askfloat("Interest", "Enter interest rate (%):", initialvalue=2.5)
        if rate:
            msg = self.account.apply_interest(rate)
            messagebox.showinfo("Interest", msg)
            self.dashboard()

    def transfer_window(self):
        receiver = simpledialog.askstring("Transfer", "Enter receiver username:")
        amount = simpledialog.askfloat("Transfer", "Enter amount:")
        if receiver and amount:
            msg = self.account.transfer_money(receiver, amount)
            messagebox.showinfo("Transfer", msg)
            self.dashboard()


#running program
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
