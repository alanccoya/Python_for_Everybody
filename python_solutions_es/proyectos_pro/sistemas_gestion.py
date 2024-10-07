#Sistemas de gestion de tareas

#Lista que almacenara las tareas
tareas = []

def agregar_tarea():
    """Funcion para agregar una tarea a la lista de tareas."""
    descripcion = input("Introduce la descripcion de tareas: ")
    tarea = {"descripcion": descripcion, "completada": False}
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' añadida correctamente")

agregar_tarea()
print(tareas)

def mostrar_tareas():
    """"Funcion para mostrar todas las tareas almacenadas."""
    if not tareas: #si la lista esta vacia
        print("No hay tareas guardadas en la lista.")
    else:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas, start=1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea,['descripcion']} - {estado}")

def marcar_completada():
    """Funcion para marcar la tarea como completada."""
    if tareas: 
        try:
            num_tarea = int(input("Introduce el numero de la tarea que has completado: "))
            if i <= num_tarea <= len(tarea):
                tareas[num_tarea - 1]["completada"] = True
                print(f"Tarea '{tareas[num_tarea - 1]['descripcion']}'marcada como completada.")
            else:
                print("Numero de tarea invalido.")
        except ValueError:
            print("Por favor, introduce un numero valido.")

def menu():
    """Menu principal del sistema de gestion de tareas."""
    while True:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion  = input("Elige una opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            print("Saliendo del programa... bip bop... :D")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")

menu()