import zipfile

with zipfile.ZipFile(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9\Project+Day+9.zip', 'r') as archivo_zip:
    archivo_zip.extractall(r'C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9')
