#Generador de Contraseñas Seguras        by @alanccoya

import random
import string

def pedir_criterios():
    """Función para pedir los criterios de la contraseña al usuario."""
    print("Seleccione los criterios para generar la contraseña:")
    
    incluir_mayusculas = input("Quieres incluir letras mayúsculas? (si/no): ").lower() == "si"
    incluir_minusculas = input("Quieres incluir letras minúsculas? (si/no): ").lower() == "si"
    incluir_numeros = input("Quieres incluir números? (si/no): ").lower() == "si"
    incluir_simbolos = input("Quieres incluir símbolos? (si/no): ").lower() == "si"
    
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña: "))
            if longitud > 0:
                break
            else:
                print("La longitud debe ser un número positivo.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    return incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos, longitud

def generar_contraseña(mayusculas, minusculas, numeros, simbolos, longitud):
    """Función para generar una contraseña segura basada en los criterios."""
    caracteres = ""
    
    if mayusculas:
        caracteres += string.ascii_uppercase    #aqui podriamos usar caracteres = caracteres + string.x, pero para resumirlo usamos += que es equivalente
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        return "No se seleccionaron criterios válidos para la contraseña."
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

def menu():
    """Menú principal para generar contraseñas seguras."""
    while True:
        print("\n--- Generador de Contraseñas Seguras ---")
        print("1. Generar una o más contraseñas")
        print("2. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos, longitud = pedir_criterios()

            # Validamos que se haya seleccionado al menos un criterio
            if not (incluir_mayusculas or incluir_minusculas or incluir_numeros or incluir_simbolos):
                print("Debes seleccionar al menos un criterio para generar una contraseña.")
                continue  # Volvemos al menú si no se seleccionó nada
            
            # Pedimos al usuario cuántas contraseñas generar
            while True:
                try:
                    cantidad = int(input("Cuántas contraseñas quieres generar? "))
                    if cantidad > 0:
                        break
                    else:
                        print("Debes generar al menos una contraseña.")
                except ValueError:
                    print("Por favor, introduce un número válido.")
            
            # Generamos las contraseñas
            for i in range(cantidad):
                contraseña = generar_contraseña(incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos, longitud)
                print(f"Contraseña {i + 1}: {contraseña}")
            
            # Ofrecemos al usuario guardar las contraseñas
            guardar = input("Quieres guardar las contraseñas en un archivo? (si/no): ").lower()
            if guardar == "s":
                with open("contraseñas.txt", "a") as archivo:
                    for i in range(cantidad):
                        contraseña = generar_contraseña(incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos, longitud)
                        archivo.write(f"Contraseña {i + 1}: {contraseña}\n")
                print("Contraseñas guardadas correctamente.")
        
        elif opcion == "2":
            print("Saliendo del programa...  bip boop... :D       @alanccoya")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Ejecutamos el menú
menu()
