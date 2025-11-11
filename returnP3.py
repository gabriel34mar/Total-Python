"""Create a function called reverse_word that takes the characters of a given word as an argument, reverses the order of their characters, and returns them that way and in uppercase.

For example, if we pass it the word "Python", it should return: "NOHTYP"

Also, you must create a variable called word, which contains any string, to pass it as an argument to the created function."""



word='pyhton'
def reverse_word(word):
    return word[::-1].upper()