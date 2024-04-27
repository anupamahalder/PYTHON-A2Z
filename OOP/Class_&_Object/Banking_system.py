class Bank:
    # contsructor 
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    # method 
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added amount {amount} to the bank successfully!")
        else:
            print("Amount cannot be less than or equal to zero")

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Sorry, you cannot withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"Sorry, you cannot withdraw more than {self.max_withdraw}")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Here is your withdrawal money {amount}")
            print(f"Your current balance is {self.balance}")
        else:
            print("You don't have the sufficient balance!")
    
#create an object 
bbank = Bank(300)
#get balance
print(bbank.get_balance()) # 300
# withdraw amount
bbank.withdraw(500) # You don't have the sufficient balance!
# deposit amount
bbank.deposit(700) # Added amount 700 to the bank successfully!
#check current balance
print(bbank.get_balance()) # 1000
#withdraw
bbank.withdraw(500) # Here is your withdrawal money 500
# get current balance
print(bbank.get_balance()) # 500

