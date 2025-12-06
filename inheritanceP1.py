"""Create a class called Person, which has the following instance attributes: name, age. Create another class, Student, which inherits these attributes from the first."""

class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        
class Student(Person):
    pass
