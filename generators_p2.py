"""Generators Practice #2
Create a generator (stored in the variable practice_generator) that is capable of returning multiples of 7 indefinitely, starting from 7 itself, and that each time it is called returns the next multiple (7, 14, 21, 28... )."""

def my_generator():
    x = 7
    while True:
        yield x
        x += 7

practice_generator = my_generator()
