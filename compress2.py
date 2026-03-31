import zipfile
path=r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9\file_compressed.zip'
open_zip=zipfile.ZipFile(path,'r')

open_zip.extractall()