"""Open the file my_text.txt and print only the second line.

"""

file = open(r'C:\Users\gabri\Documents\UMx\Carreras\Udemy\Total Python\Day 6\test.txt')

first = file.readline()   # lee la primera línea
second = file.readline()  # lee la segunda línea

print(second)             # imprime solo la segunda línea

file.close()
