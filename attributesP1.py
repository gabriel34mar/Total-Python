"""Create a class called House, and assign attributes to it: color, floors.

Create an instance of House, called white_house, with color "white" and number of floors equal to 4."""

class House:
    
    def __init__(self,color,floors):
        self.color=color
        self.floors=floors
        
        
white_house=House("white",4)

print(white_house.floors)
print(white_house.color)