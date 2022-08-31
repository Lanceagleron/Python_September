from classes.character import Character

class Pirate(Character):

    def __init__( self , name ):
        super().__init__()
        self.name = name
        self.strength = 15
        # self.speed = 3
        # self.health = 100

    def pistol_shot(self, target):
        dmg = self.strength*.1 + self.strength
        target.health = target.health - dmg
        print(f"{self.name} Shoots his pistol at {target.name} for {dmg} Damage! {target.name} is now at {target.health} HP!")
        return self


    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack ( self , ninja ):
    #     ninja.health -= self.strength
    #     return self


