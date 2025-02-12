class BankAccount:
    bank_title = "National Trust Bank"  # Class attribute for bank title
    
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"{self.customer_name} deposited ${amount:.2f}. New balance: ${self.current_balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Insufficient balance. Cannot withdraw ${amount:.2f} as it would go below the minimum balance.")
        else:
            self.current_balance -= amount
            print(f"{self.customer_name} withdrew ${amount:.2f}. New balance: ${self.current_balance:.2f}")
    
    def print_customer_info(self):
        print(f"Customer: {self.customer_name}")
        print(f"Current balance: ${self.current_balance:.2f}")
        print(f"Minimum balance: ${self.minimum_balance:.2f}")
        print()

# testing the functionality
customer1 = BankAccount("Alice Johnson", 1000, 500)
customer2 = BankAccount("Bob Smith", 300, 100)

customer1.deposit(200)
customer1.withdraw(600)
customer1.withdraw(100)

customer2.deposit(50)
customer2.withdraw(250)  # Should fail
customer2.withdraw(100)  # Should succeed

customer1.print_customer_info()
customer2.print_customer_info()

