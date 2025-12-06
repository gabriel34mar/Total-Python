"""Create a class called Character, and assign the following class attribute to it:

real = False

Create an instance called harry_potter with the following instance attributes:

species = "Human"

magical = True

age = 17"""

class Character:
    real=False
    
    def __init__(self,species,magical,age):
        self.species=species
        self.magical=magical
        self.age=age
        
harry_potter=Character("Human",True,17)