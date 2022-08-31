class Character:

    def __init__(self):
        self.health = 100
        self.strength = 5
        self.speed = 2

    def show_stats(self):
        print(f"Name:{self.name} \n HP:{self.health} \n Strength: {self.strength} \n Speed: {self.speed}")

    def attack(self,target):
        dmg = self.strength
        target.health = target.health - dmg
        # target.health -= self.strength
        print(f"{self.name} attacked {target.name} for {dmg} Damage! {target.name} is now at {target.health} HP!")
        return self

    def heal (self):
        self.health = self.health + 4
        print(f"{self.name} heals for 4 {self.name} now has {self.health} HP")