class User:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello my name is {self.first_name} {self.last_name}! nice to meet you!")

lance = User("Lance","Agleron",28)
lance.greeting()