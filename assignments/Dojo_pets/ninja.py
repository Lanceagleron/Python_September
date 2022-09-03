from cat import Cat
from dog import Dog

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is taking {self.pet.name} for a walk")
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name} is feeding {self.pet_food} to {self.pet.name}.")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.first_name} is cleaning {self.pet.name} ")
        self.pet.noise()
        return self

felix = Cat("felix", "stand")

bowser = Dog("Bowser", "rollover")
# list of pets
lance = Ninja("Lance", "Agleron", "Strawberry", "Meat", bowser)
mase = Ninja ("Mase" ,"Buquid" ,"Blueberry" ,"Tuna" , felix)

# dog.noise()

# lance.bathe()
# lance.walk()
# lance.feed()

mase.feed()
mase.bathe()