#Numero pares y numeros impares

try: 

numero = int(input("Por favor, ingresa un numero:"))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
    
except ValueError:
    print("Error, por favor introduzca un numero entero.")
    