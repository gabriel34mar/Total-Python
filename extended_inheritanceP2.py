""""The platypus is one of the rarest creatures in the world: although it is a mammal, it lays eggs; and it nurses its young but has no nipples." (National Geographic)

Create a Platypus class that inherits from other classes: Vertebrate, Fish, Reptile, Bird, and Mammal, so that you "build" an animal that has the following methods and attributes:

- lay_eggs()

- has_peak = True

- vertebrate = True

- poisonous = True

- swim()

- walk()

- nurse()"""

class Vertebrate:
    vertebrate = True

class Bird(Vertebrate):
    has_peak = True
    def lay_eggs(self):
        print("laying eggs")

class Reptile(Vertebrate):
    poisonous = True

class Fish(Vertebrate):
    def swim(self):
        print("swimming")
    def lay_eggs(self):
        print("laying eggs")

class Mammal(Vertebrate):
    def walk(self):
        print("walking")
    def nurse(self):
        print("nursing pups")

class Platypus(Bird,Reptile,Fish,Mammal):
    pass