"""You have three character classes in a game, all of which have their specific defense methods.

Create a function called general_defense(), which can receive an object (an instance of your character classes), and execute its defend() method regardless of what type of character it is."""
class Wizard():
    def defend(self):
        print("magic shield")

class Archer():
    def defend(self):
        print("duck")

class Samurai():
    def defend(self):
        print("block")
        
def general_defense(obj):
    obj.defend()