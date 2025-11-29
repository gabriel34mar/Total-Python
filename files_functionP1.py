"""Create a function called open_read() that opens a file indicated as a parameter, and returns its content (read)."""
def open_read(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content