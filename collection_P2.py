"""Collections Module Practice #2
Create a dictionary called my_dictionary, for which, when a searched keyword is not found, it is loaded with the string "Value not found".

Load the dictionary with at least the following data pairs:

keyword = age

value = 44

Use the defaultdict method of the Collections module."""
from collections import defaultdict

my_dictionary = defaultdict(lambda: "Value not found")

# Agregar el dato solicitado
my_dictionary["age"] = 44

# Pruebas
print(my_dictionary["age"])      # 44
print(my_dictionary["name"])     # Value not found