"""Generators Practice #3
Create a generator that subtracts the lives of a video game character one by one, and returns a message each time it is called:

"You have 3 lives left"

"You have 2 lives left"

"You have 1 live left"

"Game Over"

Store the generator in the variable lose_live"""

def my_generator():
    life = 3
    while life > 0:
        if life == 1:
            yield "You have 1 live left"
        else:
            yield f"You have {life} lives left"
        life -= 1
    yield "Game Over"

lose_live = my_generator()
