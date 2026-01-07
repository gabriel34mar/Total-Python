

from ticket_numbers import (
    cosmetics_generator,
    perfumes_generator,
    medicines_generator,
    decorator_turn
)

cosmetics = cosmetics_generator()
perfumes = perfumes_generator()
medicines = medicines_generator()


def ask_turn():
    option = input(
        "Choose an area:\n"
        "[C] Cosmetics\n"
        "[P] Perfumes\n"
        "[M] Medicines\n"
        "Option: "
    ).lower()

    if option == "c":

        @decorator_turn
        def give_turn():
            return next(cosmetics)

        give_turn()

    elif option == "p":

        @decorator_turn
        def give_turn():
            return next(perfumes)

        give_turn()

    elif option == "m":

        @decorator_turn
        def give_turn():
            return next(medicines)

        give_turn()

    else:
        print("Invalid option\n")


def run():
    while True:
        ask_turn()
        again = input("Do you want another turn? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break


run()
