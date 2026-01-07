"""In the previous lesson we have seen how error handling is usually implemented in Python. For this exercise, however, I'll need you to do it in a slightly different way so that it can be tested: you'll need to implement it INSIDE the function. In the form of a comment, you will see an example resolution. Keep in mind, however, that the preferred form is the one we've seen in class.

Implement an error handler inside the following function, open_file():

If the file you are trying to open cannot be found (FileNotFoundError), display the message: "The file was not found"

In case another type of error occurs, display the message: "Unknown error"

If no error occurs, print to screen: "Opening successfully"

In all cases, at the end, print: "Ending execution" """


def open_file(file_name):
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("The file was not found")
        print("Ending execution")
    except:
        print("Unknown error")
        print("Ending execution")
    else:
        print("Opening successfully")
        print("Ending execution")