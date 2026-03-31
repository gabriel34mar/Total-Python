import zipfile

ruta = r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9\file_compressed.zip'

my_zip = zipfile.ZipFile(ruta, 'w')

my_zip.write(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9\My_Text_A.txt',arcname='My_Text_A.txt')
my_zip.write(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9\My_Text_B.txt',arcname='My_Text_B.txt')

my_zip.close()
