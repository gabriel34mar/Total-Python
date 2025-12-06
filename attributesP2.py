"""Create a class called Cube, and assign the class attribute to it:

sides = 6

and the instance attribute:

color

Create a red_cube instance of that color."""

class Cube:
    sides=6
    
    def __init__(self,color):
        self.color=color
        
red_cube=Cube('red')