#Calculador de puntaje
try:
    puntuacion = float(input("Introduzca la puntuacion (0.0 - 1.0):"))
    
    if 0.0 <= puntuacion <= 1.0:
        if puntuacion >= 0.9:
            print("Sobresaliente!")
        elif puntuacion >= 0.8:
            print("Notable@")
        elif puntuacion >= 0.7:
            print("Bien")
        elif puntuacion >= 0.6:
            print("Suficiente")
        else:
            print("Insuficiente")
    else:
        print("Error, puntuacion fuera de rango.")
        
except ValueError:
    print("Error, por favor introduce una puntuacion.")