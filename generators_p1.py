"""Create a generator (stored in the practice_generator variable) that is capable of returning an infinite sequence of numbers, starting from 1, and returning a higher consecutive number each time it is called using next."""

def my_generator():
    x=0
    while True:
        yield x
        x+=1

practice_generator=my_generator()
print(next(practice_generator))