'''Create a function called log_error() that opens a file given as a parameter, and updates it by adding a line at the end that says "an execution error has been registered". Finally, you need to close the file.'''
def log_error(filename):
    file = open(filename, 'a')        
    file.write("an execution error has been registered")   
    file.close()                      

