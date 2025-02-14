class BankAccount:
    bank_title = "National Trust Bank"  # Class attribute for bank title
    
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number  
    
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
        print(f"Account number: {self._account_number}")
        print(f"Routing number: {self.__routing_number}")
        print()
class SavingsAccWithInterest(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.current_balance * self.interest_rate / 100
        self.current_balance += interest
        print(f"Interest added at rate {self.interest_rate}%. New balance: ${self.current_balance:.2f}")

class CheckingAccWithLimit(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit
    
    def transfer(self, amount):
        if amount > self.transfer_limit:
            print(f"Transfer amount exceeds the limit of ${self.transfer_limit:.2f}.")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Insufficient balance. Cannot transfer ${amount:.2f} as it would go below the minimum balance.")
        else:
            self.current_balance -= amount
            print(f"{self.customer_name} transferred ${amount:.2f}. New balance: ${self.current_balance:.2f}")