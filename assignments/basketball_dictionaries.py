
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]







class Player:

    new_team = []

    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        Player.new_team.append(self)


    def print_info(self):
        print(f"Name: {self.name} age: {self.age} position: {self.position} team:{self.team}")
        return self

    @classmethod
    def print_new_team(cls):
        for i in cls.new_team:
            
            i.print_info()
            



kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???

player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])

player_jason = Player(jason["name"], jason["age"], jason["position"], jason["team"])

player_kyrie = Player(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])



# print(player_kevin.team)
# print(player_jason.team)
# print(player_kyrie.team)

Player.print_new_team()

