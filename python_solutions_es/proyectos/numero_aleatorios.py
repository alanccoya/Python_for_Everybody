#Numeros aleatorios

import random

try:
    n = int(input("Cuantos numeros aleatorios deseas generar?"))
    if n <= 0:
        print("Debes ingresar un numero mayor que 0.")
    else:
        numeros = []
        for i in range(n):
            num = random.randint(1, 100)
            numeros.append(num)
    
        suma = sum(numeros)
        media = suma / n
        maximo = max(numeros)
    
        print(f"Numeros generados: {numeros}")
        print(f"Suma de los numeros: {suma}")
        print(f"Media de los numeros: {media}")
        print(f"Numero maximo: {maximo}")
except ValueError:
    print("Error: Debes ingresar un numero valido.")