from pathlib import Path
folder = Path(r"C:\Users\gabri\Documents\UMx\Carreras\Udemy\Total Python\Day 6\test.txt")
if not folder.exists():
    print("This file doesnt exist\n")
else:
    ("Yes it exist\n")  
      
print(folder.read_text())
