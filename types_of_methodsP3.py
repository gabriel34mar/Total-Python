"""Create an instance method throw_arrow() that subtracts by -1 the number of arrows a Character instance has, which in turn has an instance attribute called arrows_amount (that stores a certain number)."""
class Character:
    def __init__(self, arrows_amount):
        self.arrows_amount = arrows_amount
    def throw_arrow(self):
        self.arrows_amount = self.arrows_amount-1
        