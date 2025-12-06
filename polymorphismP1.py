"""The built-in function in Python len() has a polymorphic behavior, since it calculates the length of an object based on its type (strings, lists, tuples, among others), returning the number of items or characters that make it.

Create an iterator that iterates through the following objects: word, list, tuple and displays on the screen (using print()) for each of them its length with the len() function."""
a_word = "polymorphism"
a_list = ["Classes", "OOP", "Polymorphism"]
a_tuple = (1, 2, 3, 80)

for obj in [a_word,a_list,a_tuple]:
    print(len(obj))