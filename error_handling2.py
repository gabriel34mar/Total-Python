def ask_number():
    while True:

        try:
            number=int(input("Enter a number "))
        except:
            print("Thats not a number")
        else:
            print(f"You have enter a number {number}")
            break
    print("Thank you")

ask_number()