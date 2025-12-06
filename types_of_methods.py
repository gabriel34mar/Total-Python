class Bird:
    wings=True
    
    def __init__(self,color,species):
        self.color=color
        self.species=species
        
    def chirp(self):
        print("tweet")
        
    def fly(self,feet):
        print(f"The bird flies {feet} feet high")
        
    def paint_black(self):
        self.color="black"
        print(f"Now the bird is {self.color}")
    
    @classmethod
    def lay_eggs(cls,number):
        print(f"It laid {number} eggs")
        
    @staticmethod
    def _look():
        print("The bird looks")
    
Bird.looks()
Bird.lay_eggs(3)
tweetie=Bird("Yellow","Conary")
tweetie.fly(164)
tweetie.paint_black()


