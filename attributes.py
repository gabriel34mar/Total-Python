class Bird:
    wings=True
    
    def __init__(self,color,species):
        self.color=color
        self.species=species
        
        
my_bird=Bird("Black","Tucan")

print(my_bird.color)
print(my_bird.species)
print(my_bird.wings)
