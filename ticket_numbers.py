
def decorator_turn(func):
    def wrapper():
        ticket = func()
        print("Your number is:")
        print(ticket)
        print("Wait and someone will be with you shortly\n")
    return wrapper


def cosmetics_generator():
    num_cos = 1
    while True:
        yield f"C-{num_cos}"
        num_cos += 1


def perfumes_generator():
    num_per = 1
    while True:
        yield f"P-{num_per}"
        num_per += 1


def medicines_generator():
    num_med = 1
    while True:
        yield f"M-{num_med}"
        num_med += 1
