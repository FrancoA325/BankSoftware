from bank import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit
