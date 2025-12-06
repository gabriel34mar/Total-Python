class Animal:

    def __init__(self,age,color):
        self.age=age
        self.color=color

    def born(self):
        print("This animal has been born"  )

    def Talk(self):
        print("This animal makes a sound")

class Bird(Animal):

    def __init__(self, age, color,altitud):
        super().__init__(age,color)
        self.altitud=altitud

    def Talk(self):
        print("Chirp")
    
    def fly(self,feet):
        print(f'This bird flies {feet} feet')

tweetie = Bird(3,'yellow',90)
tweetie.fly(560)

my_animal=Animal(5,"Black")
