class BankAccount:
    bank_name = "lance bank"
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance = self.balance + amount
        print(f"You deposited ${amount}")
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance > amount:
            self.balance = self.balance - amount
            print(f"withdrew ${amount}")
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        # print("interest rate: {self.int_rate}")
        print("======")
        return self

        
    def yield_interest(self):
        # your code here
        self.balance = self.balance + (self.balance * self.int_rate)

        return self

martin = BankAccount(.01, 1000)
lance = BankAccount(.01,300)

lance.deposit(100).deposit(150).deposit(150).withdraw(700).yield_interest().display_account_info()
martin.deposit(100).deposit(1000).withdraw(500).withdraw(300).withdraw(200).withdraw(100).yield_interest().display_account_info()
