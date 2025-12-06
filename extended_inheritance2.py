class Father:
    def talk(self):
        print("hello")

class Mother:
    def laugh(self):
        print("ha ha ")
    
    def talk(self):
        print("How are you? ")

class Child(Father,Mother):
    pass

class Grandchild(Child):
    pass

my_grandchild= Grandchild()

print(Grandchild.__mro__)
