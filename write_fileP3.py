"""Use the writelines method to write the values of the following list to the end of the register.txt file. Insert a tab between each item in the list to separate them.

record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]

Print the full content of register.txt upon completion.

Hint: remember that the scape sequence to concatenate a tab in a string is \t. Also, you will need to close the file in write mode and reopen it in read mode in order to print its content."""

record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]

# Open the file in append mode and write the values separated by tabs
file = open(r"C:\Users\gabri\Documents\UMx\Carreras\Udemy\Total Python\Day 6\register.txt", "a")
file.writelines(item + "\t" for item in record_last_session)
file.write("\n")  # opcional: agregar salto de línea útil para registros nuevos
file.close()

# Reopen the file in read mode and print its full content
file = open(r"C:\Users\gabri\Documents\UMx\Carreras\Udemy\Total Python\Day 6\register.txt", "r")
print(file.read())
file.close()
