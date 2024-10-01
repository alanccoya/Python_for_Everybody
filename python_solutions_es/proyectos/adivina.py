#Adivina el numero!
import random

numero_secreto = random.randint(1, 30)

intentos = 0
max_intentos = 5

adivinanza = int(input("Adivina el numero entre 1 y 30:"))

while adivinanza != numero_secreto and intentos < max_intentos:
    intentos = intentos + 1  #Se puede escribir tambien "intentos += 1" que seria lo mismo que "intentos + 1".
    if adivinanza < numero_secreto:
         print("Demasiado bajo!")
    elif adivinanza > numero_secreto:
        print("Demasiado alto!")
    
    if intentos < max_intentos:
        adivinanza = int(input("Intenta de nuevo:"))
    else:
        print("Te has quedado sin intentos!")
if adivinanza == numero_secreto:
    print(f"Correcto! Adivinaste el numero en {intentos} intentos.")
else:
    print(f"Lo siento, no adivinaste el numero. Era {numero_secreto}.")
