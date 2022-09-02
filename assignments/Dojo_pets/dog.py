from pets import Pet

class Dog(Pet):

    def __init__(self, name, trick):
        super().__init__()
        self.name = name
        self.trick = trick
        self.speak = "Woof!"