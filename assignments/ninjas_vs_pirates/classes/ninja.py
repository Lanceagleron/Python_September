from classes.character import Character


class Ninja(Character):

    def __init__( self , name ):
        super().__init__()
        self.name = name
        self.strength = 10
        # self.speed = 5
        # self.health = 100
    
    def throw_shuriken(self, target):
        dmg = self.strength*.5 + self.strength
        target.health = target.health - dmg
        print(f"{self.name} throws shuriken at {target.name} for {dmg} Damage! {target.name} is now at {target.health} HP!")
        return self

    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack( self , pirate ):
    #     pirate.health -= self.strength
    #     return self

        