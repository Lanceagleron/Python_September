
class Pet:
    def __init__(self):
        
        self.energy = 100
        self.health = 50

    def sleep(self):
        self.health = self.health + 25

        print(f"{self.name} is sleeping soundly.")

        return self

    def eat(self):
        self.health = self.health + 10 
        self.energy = self.energy + 5

        print(f"{self.name} is eating.")
        

        return self

    def play(self):
        self.health = self.health + 5

        print(f"{self.name} is playing.")

        return self

    def noise(self):
        print(f"{self.speak}")
        return self

