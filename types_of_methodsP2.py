"""Create a class method called revive() that acts on the Player class's alive attribute, setting it to True each time it is invoked. The default value of the alive attribute should be False."""
class Player:
    alive = False

    @classmethod
    def revive(cls):
        cls.alive = True
