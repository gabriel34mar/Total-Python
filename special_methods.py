class CD:
    def __init__(self,songwritter,tittle,songs):
        self.songwritter=songwritter
        self.tittle=tittle
        self.songs=songs

    def __str__(self):
        return f"Album: {self.tittle} by {self.songwritter}"
    
    def __len__(self):
        return self.songs
    
    def __del__ (self):
        print("CD has been deleted")

my_cd=CD("Pink Floyd","The wall",24)

print(len(my_cd))
print(my_cd)

del my_cd
