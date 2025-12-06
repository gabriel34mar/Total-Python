"""You have three classes of characters in a game, which have their specific attack methods.

Create an iterator that performs a conjugate attack in the following order: Archer, Wizard, Samurai, by calling each character's attack() method. You'll need to instantiate each of the above classes to build an iterable (a list called characters) that can be iterated through in that order."""
class Wizard:
    def attack(self):
        print("magic attack")

class Archer:
    def attack(self):
        print("shoot arrow")

class Samurai:
    def attack(self):
        print("katana attack")

# Instanciar los personajes
archer1 = Archer()
wizard1 = Wizard()
samurai1 = Samurai()

# Crear el iterable en el orden solicitado
characters = [archer1, wizard1, samurai1]

# Iterador que realiza el ataque conjugado
for character in characters:
    character.attack()