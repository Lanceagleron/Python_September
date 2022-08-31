from pickle import TRUE


class User:

    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    #display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"Name:{self.first_name}")
        print(f"Lastname:{self.last_name}")
        print(f"email:{self.email}")
        print(f"age:{self.age}")
        print(f"Rewards Member:{self.is_rewards_member}")
        print(f"Gold Card Balance: {self.gold_card_points}")
        
        # print(f"Name:{self.first_name} Lastname:{self.last_name}, email:{self.email}, age:{self.age} Rewards Member:{self.is_rewards_member} Gold Card Balance: {self.gold_card_points}")

    # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def enroll(self):
        self.is_rewards_member = self.is_rewards_member = True
        self.gold_card_points = self.gold_card_points + 200

    #spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

marco = User("Marco", "Cabrera", "marcocabrera@gmail.com", 29)
william = User("William","Pascaran","williampascaran@gmail.com", 27)
lance = User("Lance","Agleron","lanceagleron@gmail.com", 28)



lance.display_info()
print("==========")
william.display_info()
print("==========")
marco.display_info()
print("==========")
lance.enroll()
lance.display_info()
lance.spend_points(50)
print("==========")
lance.display_info()
william.enroll()
william.spend_points(80)
print("==========")
william.display_info()