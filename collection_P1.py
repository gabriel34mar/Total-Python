"""Apply a Counter to the list of numbers given below, and store it in a variable called my_counter"""
from collections import Counter
my_list = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

my_counter = Counter(my_list)
print(my_counter)
