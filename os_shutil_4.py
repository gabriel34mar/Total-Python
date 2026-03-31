import os
import shutil
import send2trash

path= r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9'

for folder,subfolder,file in os.walk(path):
    print(f"In folder: {folder}")
    print(f"In subfolder are:")
    for sub in subfolder:
        print(f'\t{sub}')
    print("Files are: ")
    for fi in file:
        print(f'\t{fi}')
    print('\t')
    
    