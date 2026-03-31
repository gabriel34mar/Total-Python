import os
import shutil

origen = "course.txt"
destino = r"C:\Users\gabri\Dropbox\UMx\Carreras\Udemy\Total Python\Day 9\course.txt"

shutil.move(origen, destino)

print("Archivo movido correctamente")