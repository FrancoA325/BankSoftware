from bank import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, destination):
        if amount > self.current_balance - self.minimum_balance:
            print("Insufficient funds")
        elif amount > self.transfer_limit:
            print("Transfer limit reached, current transfer limit set as: {}".format(self.transfer_limit))
        else:
            self.current_balance = self.current_balance - amount
            destination.current_balance = destination.current_balance + amount
            print("Transfer sent successfully to: ", destination.customer_name)
            print("\n Amount: ", amount)