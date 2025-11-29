"""Create a function called overwrite() that opens a file indicated as a parameter, and overwrites any previous content with the text 'content deleted'"""
def overwrite(filename):
    text = "content deleted"
    with open(filename, 'w') as file:
        file.write(text)
    return text
