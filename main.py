
from bank import SavingsAccWithInterest
from bank import CheckingAccWithLimit

# Create instances of SavingsAccWithInterest
savings1 = SavingsAccWithInterest("Alice Johnson", 1000, 500, 123456, 4567, 5)
savings2 = SavingsAccWithInterest("Bob Smith", 300, 100, 987654, 7654, 3)

# Create instances of CheckingAccWithLimit
checking1 = CheckingAccWithLimit("Charlie Brown", 1500, 200, 111222, 333444, 500)
checking2 = CheckingAccWithLimit("Diana Prince", 800, 100, 555666, 777888, 300)

# Demonstrate functionality
savings1.add_interest()
savings2.add_interest()

checking1.transfer(600)
checking1.transfer(400)  # Should succeed

checking2.transfer(350)  # Should fail
checking2.transfer(200)  # Should succeed

savings1.print_customer_info()
savings2.print_customer_info()
checking1.print_customer_info()
checking2.print_customer_info()