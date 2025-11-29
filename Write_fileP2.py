'''Open the file called my_file.txt, and add a line at the end of it that says: New login.

Print the entire content of my_file.txt upon completion.

Hint: you will have to close it in write mode and reopen it in read mode.'''


file = open(r"C:\Users\gabri\Documents\UMx\Carreras\Udemy\Total Python\Day 6\my_file.txt","a")
file.write("New login")
file.close()
file = open(r"C:\Users\gabri\Documents\UMx\Carreras\Udemy\Total Python\Day 6\my_file.txt", "r")
print(file.read())
