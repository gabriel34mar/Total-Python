"""A son has inherited all his characteristics from his father, however, they have different hobbies. Make the Child class inherit all its methods and attributes from Father, overriding the hobby() method so that it returns [1]: "I play video games in my free time"



[1]: make sure to use return statement instead of print()"""

class Father():
    eye_color = "brown"
    hair = "curly"
    height = "average"
    voice = "deep"
    favorite_sport = "tennis"
    def laugh(self):
        return "LOL"
    def hobby(self):
        return "I work with wood in my free time"
    def walk(self):
        return "Walking with long and quick steps"
        
class Child(Father):
    def hobby(self):
        return "I play video games in my free time"