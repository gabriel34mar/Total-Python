"""In the previous lesson we have seen how error handling is usually implemented in Python. For this exercise, however, I'll need you to do it in a slightly different way so that it can be tested: you'll need to implement it INSIDE the function. In the form of a comment, you will see an example resolution. Keep in mind, however, that the preferred form is the one we've seen in class.



For the following sum_num() function, implement a simple error handler that, in case of any error, prints the message: "Unexpected error" on the screen. Otherwise, it should limit itself to displaying the result of the sum between the two numbers given as arguments."""

def sum_num(num1, num2):
    try:
        result = num1 + num2
    except:
        print("Unexpected error")
    else:
        print(result)