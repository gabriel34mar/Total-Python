"""If the Daughter class has inherited her way of laughing from her father, and her vocation from her mother, and today they have the same job at the Prosecutor's Office, create multiple inheritance that allows this class to inherit correctly from Father and Mother.



Complete the code provided below to achieve this."""

class Father():
    def work(self):
        print("Working in the Public Hospital")

    def laugh(self):
        print("Ha Ha Ha!")

class Mother():
    def work(self):
        print("Working in the Public Prosecutor's Office")
        
class Daughter(Mother,Father):
    pass