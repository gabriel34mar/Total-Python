"""Create a class called Pet, which has the following instance attributes: age, name, legs. Create another class, Dog, which inherits its attributes from the first."""
class Pet:
    def __init__ (self,age,name,legs):
        self.age=age
        self.name=name
        self.legs=legs
        
class Dog(Pet):
    pass