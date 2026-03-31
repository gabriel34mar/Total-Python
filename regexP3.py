"""The postal code of a given region is formed from two alphanumeric characters and four numeric characters after that (example: XX1234). Create a function, called check_pc to check if the zip code passed as an argument follows this pattern. If the pattern is correct, show the user the message "Ok", otherwise: "The zip code entered is not correct"."""
import re

def check_pc(pc):
    pattern=r'\w{2}\d{4}'
    if re.search(pattern,pc):
        print("Ok")
    else:
        print("The zip code entered is not correct")