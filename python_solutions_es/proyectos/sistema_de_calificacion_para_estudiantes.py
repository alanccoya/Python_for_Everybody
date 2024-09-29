#Sistema de calificacion para estudiantes

puntuacion = float(input("Introduzca su puntuacion obtenida(0-100):"))

if 0 <= puntuacion <= 100:
    
    if puntuacion >= 80:
        print("A")
    elif puntuacion >= 60:
        print("B")
    elif puntuacion >= 40:
        print("C")
    elif puntuacion >= 20:
        print("D")
    else:
        print("F")
else:
    print("Error: Introduzca una puntuacion de (0-100).")