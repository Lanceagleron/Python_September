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

class User:

    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def make_withraw(self,amount):
        if self.account.balance > amount:
            self.account.balance = self.account.balance - amount
            print(f"withdrew ${amount}")
        else:
            self.account.balance = self.account.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def make_deposit(self,amount):
        self.account.balance = self.account.balance + amount
        print(f"You deposited ${amount}")
        return self
        # self.account.deposit()
        # print(self.account.balance)

    #display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print("=================")
        print(f"Name:{self.first_name}")
        print(f"Lastname:{self.last_name}")
        print(f"email:{self.email}")
        print(f"age:{self.age}")
        print(f"Balance ${self.account.balance}")
        print(f"Rewards Member:{self.is_rewards_member}")
        print(f"Gold Card Balance: {self.gold_card_points}")
        return self
        
        # print(f"Name:{self.first_name} Lastname:{self.last_name}, email:{self.email}, age:{self.age} Rewards Member:{self.is_rewards_member} Gold Card Balance: {self.gold_card_points}")

    def display_user_balance(self):
        print(f"Balance ${self.account.balance}")

    # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def enroll(self):
        if self.is_rewards_member == False:
            print(f"{self.first_name} enrolled!")
            self.is_rewards_member = self.is_rewards_member = True
            self.gold_card_points = self.gold_card_points + 200
        else:
            print("User already a member.")
        return self

    #spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        print(f"{self.first_name} spent {amount} Points.")
        self.gold_card_points = self.gold_card_points - amount
        return self

marco = User("Marco", "Cabrera", "marcocabrera@gmail.com", 29)
william = User("William","Pascaran","williampascaran@gmail.com", 27)
lance = User("Lance","Agleron","lanceagleron@gmail.com", 28)

lance.make_deposit(150).make_withraw(200).display_user_balance()