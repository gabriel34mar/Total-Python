"""Create a function called check_greeting to check if a phrase given as an argument starts with the word "Hello". If the pattern is found, the function should end by displaying the message "Ok", but if it detects that the phrase does not start with "Hello", it should inform the user "You didn't say hello" by printing the message to the screen."""
import re
def check_greeting(sentence):
    pattern=r'^Hello'
    if re.search(pattern,sentence):
        print("Ok")
    else:
        print("You didn't say hello")