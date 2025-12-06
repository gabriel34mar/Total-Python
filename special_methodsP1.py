"""Given the Book class, implement the special method __str__ so that each time the object is printed, it returns '"{title}", from {author}' (note: the title must be enclosed in double quotes)."""
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__ (self):
        return f'"{self.title}", from {self.author}'