#Conversion de Celsius a fahrenheit =

def celsius_a_fahrentheit(celsius):   #Convertir celsius a fahrenheit
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):  #Convertir fahrenheit a celcius
    return (fahrenheit - 32) * 5 / 9 


#Creamos un menu para mostar al usuario las opciones a elegir
def mostrar_menu():
    print("Selecciona el tipo de conversion:")
    print("1. Celsius a Fahrenheit.")
    print("2. Fahrenheit a Celsius.")
    print("3. Presiona 'q' para salir.")

    
while True: 
    mostrar_menu()
    opcion = input("Elige una opcion (1/2) o 'q' para salir:").lower() #añadimos ".lower()" para convertir todos los valores a minuscula.

    if opcion == "q":
        print("Saliendo del programa... bip boop. :D")
        break

    if opcion not in ["1", "2"]:   #not in 
        print(">>>>Opcion invalida, por favor selecciona (1, 2 o q) para salir.<<<<<")
        continue  

    try:
        if opcion == "1":
            celsius = float(input("Introduce la temperatura en Celsius: "))
            fahrenheit = celsius_a_fahrentheit(celsius)
            print(f"En grados fahrenheit son:  {fahrenheit:.2f}f   ")
        elif opcion == "2":
            fahrenheit = float(input("Introduzca la temperatura en fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"En grados celsius son: {celsius:.2f}C   ")
        
    except ValueError:
        print("Error, debes ingresar un numero valido.")