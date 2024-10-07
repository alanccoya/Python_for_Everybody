#Calculadora de promedio de mayor a menor

numeros = []

while True:
    entrada = input("Introduce un numero o 'fin' para terminar: ")
    
    if entrada.lower() == "fin":
        break

    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada invalida, por favor ingrese un numero valido.")

if numeros:
    maximo = max(numeros)
    minimo = min(numeros)

    print(f"Mmaximo: {maximo}, Minimo: {minimo}")
else:
    print("No se ingresaron numeros.")
