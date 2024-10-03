#Calculadora matematica

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b
    
def mostrar_menu():
    print("Selecciona una operacion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("Presiona 'q' para salir.")

while True:
    mostrar_menu()
    opcion = input("Elije una opción (1/2/3/4): ")

    if opcion == "q":
        print("Saliendo de la calculadora...")
        break
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))

        if opcion == "1":
            print(f"El resultado de la suma es: {sumar(a, b)}")
        elif opcion == "2":
            print(f"El resultado de la restas es: {restar(a, b)}")
        elif opcion == "3":
            print(f"El resultado de la multiplicacion es: {multiplicar(a, b)}")
        elif opcion == "4":
            print(f"El resultado de la division es: {dividir(a, b)}")
        else: 
            print("Opcion invalida.")
    except ValueError:
        print("Error: Debes ingresar números validos.")