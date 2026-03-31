"""RegEx Practice #1
Create a function called check_email to check if an email address is correct, which checks if the email given as argument contains "@" and ends with ".com".

If the pattern is found, the function should end displaying the "Ok" message, but if it detects that the given parameter does not contain the indicated elements, it should inform the user "The email address is incorrect" by printing the message on the screen."""

import re

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.com$'
    
    if re.search(pattern, email):
        print("Ok")
    else:
        print("The email address is incorrect")