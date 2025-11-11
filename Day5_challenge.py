from random import choice
#Creo las opciones posibles para la palabra escogida
words = ["apple", "banana", "cherry", "dragon", "elephant", "falcon", "guitar", "honey", "island", "jungle"]
#Aleatoriamente escoge una de las opciones 
secret_word = choice(words)
life=6
guessed_letter = ['_']* len(secret_word)
#funcion para pedir la letra 
def get_letter():
    while True:
        letter = input("Ingresa una letra de la a-z: ").lower()
        if letter.isalpha() and len(letter) == 1:
            return letter
        else:
            print("Entrada inválida, intenta otra vez.")
#Funcion para comprobar la letra
def check_letter(letter, secret_word, guessed_letter):
    acierto = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed_letter[i] = letter
            acierto = True
    return acierto
#Bucle checar si ganaste
def check_win(guessed_letter):
    if not '_' in guessed_letter:
        return True
    else:
        return False
#Bucle principal    
while life> 0 and not check_win(guessed_letter):
    print(" ".join(guessed_letter), f"Vidas restantes: {life}")
    letter=get_letter()
    if not check_letter(letter, secret_word, guessed_letter):
        life -= 1
        
# Mensaje final
if check_win(guessed_letter):
    print("¡Felicidades! ¡Ganaste!")
else:
    print(f"Perdiste. La palabra era: {secret_word}")
    