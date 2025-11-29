import random


class robot:
    name = "machine"
    game = ["pedra","paper","tisora"]

    def playing(self):
        choice = random.choice(self.game)
        return choice
    
class moneda:
    name = "moneda"
    game = ["cara","creu"]

    def playing(self):
        choice = random.choice(self.game)
        return choice
    
class tresenratlla:
    name = "tresenratlla"
    game = ["1a","2a","3a","1b","2b","3b","1c","2c","3c"]

    def playing(self):
        choice = random.choice(self.game)
        return choice