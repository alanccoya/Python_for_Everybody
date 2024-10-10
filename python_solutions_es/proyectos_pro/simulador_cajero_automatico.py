#Proyecto: Simulador de Cajero Automatico

saldo = 0  #iniciamos con el saldo en "0"

# Usaremos "def" para definir funciones del menu de opciones
def consultar_saldo():
    """Funcion para consultar el saldo actual."""
    print(f"Tu saldo actual es: ${saldo:.2f}")

def depositar_dinero():
    """Funcion para depositar dinero en la cuenta."""
    global saldo #indicamos que vamos a modificar la variable global saldo
    try:
        monto = float(input("Introduce el monto a depositar: "))
        if monto > 0:
            saldo = saldo + monto #sumamos el monto al saldo
            registrar_transaccion("Depósito", monto) # registrar la transacción
            guardar_saldo() # guardar el saldo actualizado
            print(f"Has depositado ${monto:.2f}. Tu nuevo saldo es ${saldo:.2f}")
        else:
            print("El monto debe ser positivo.")
    except ValueError:
        print("Por favor, introduce un número válido.")

#al retirar dinero, debemos asegurarno que el usuario no retire mas dinero del que tiene disponible, nuevamente usamod try and except para evitar estos errores.
def retirar_dinero():
    """Función para retirar dinero de la cuenta."""
    global saldo #indicamos que vamos a modificar la variable global saldo
    try:
        monto = float(input("Introduce el monto a retirar: "))
        if monto > 0:
            if monto <= saldo:
                saldo = saldo - monto #restamos el monto del saldo(porque estamos retirando dinero)
                registrar_transaccion("Retiro", monto) #registrar la transaccion
                guardar_saldo() #guardar el saldo actualizado
                print(f"Has retirado ${monto:.2f}. Tu nuevo saldo es ${saldo:.2f}")
            else:
                print("ERROR: No tienes sufieciente saldo para retirar esa cantidad :(.")
        else:
            print("El monto debe ser positivo.")
    except ValueError:
        print("Por favor, introduce un número válido.")

def guardar_saldo():
    """"Función para guardar el saldo en un archivo."""
    with open("saldo.txt", "w") as archivo:
        archivo.write(str(saldo)) #guardamos el saldo como texto
    print("Saldo guardado correctamente.")

def cargar_saldo():
    """Función para cargar el saldo desde un archivo."""
    global saldo
    try:
        with open("saldo.txt", "r") as archivo:
            saldo = float(archivo.read()) #leemos el saldo y lo convertimos a float
        print(f"Saldo cargado correctamente: ${saldo:.2f}")
    except ValueError:
        print("No se encontró u narchivo de salario previo, se inicia con saldo $0.")

def registrar_transaccion(tipo, monto):
    """Función para registrar una transaccion en el historial."""
    with open("historial.txt", "a") as archivo:
        archivo.write(f"{tipo}: ${monto:.2f}\n") #guardamos la transaccion en el archivo

def mostrar_historial():
    """Función para mostrar el historial de transacciones."""
    try:
        with open("historial.txt", "r") as archivo:
            historial = archivo.read()
            if historial:
                print("\n--- Historial de transacciones ---")
                print(historial)
            else:
                print("El historial está vacío.")
    except ValueError:
        print("No se encontró un historial previo.")

def menu():
    """Menu pinrcipal del cajero automatico."""
    while True:
        #mostramos el menu al usuario usando print()
        print("\n--- Simulador de Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Deporsitar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial de transacciones")
        print("5. Salir")

        #soliicitamos al usuario que elija una opcion con input()
        opcion = input("Elije una opcion: ")

        #usamos condicionales para cada opcion if elif else
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar_dinero()
        elif opcion == "3":
            retirar_dinero()
        elif opcion == "4":
            mostrar_historial() # nueva opcion para mostrar el historial
        elif opcion == "5":
            print("Saliendo del programa... bip boop... :D")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

#agregamos siempre menu() al ultimo para que cargue el menu() y corra el programa
menu()
