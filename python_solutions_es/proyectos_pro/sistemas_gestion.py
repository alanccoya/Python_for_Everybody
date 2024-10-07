#alanccoya #capitulo del 1 al 5 python for everybody


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
            print(f"{i}. {tarea['descripcion']} - {estado}")


def marcar_completada():
    """Funcion para marcar la tarea como completada."""
    if tareas: 
        try:
            num_tarea = int(input("Introduce el numero de la tarea que has completado: "))
            if 1 <= num_tarea <= len(tareas):
                tareas[num_tarea - 1]["completada"] = True
                print(f"Tarea '{tareas[num_tarea - 1]['descripcion']}'marcada como completada.")
            else:
                print("Numero de tarea invalido.")
        except ValueError:
            print("Por favor, introduce un numero valido.")


def eliminar_tarea():
    """Funcion para eliminar una tarea de la lista."""
    mostrar_tareas()
    if tareas:
        try:
            num_tarea = int(input("Introduce el numero de la tarea que deseas eliminar: "))
            if 1 <= num_tarea <= len(tareas):
                tarea_eliminada = tareas.pop(num_tarea - 1)
                print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
            else:
                print("Numero de tarea invalido.")
        except ValueError:
            print("Por favor, introduce un numero valido.")


def guardar_tareas():
    """Funcion para guardar las tareas en un archivo."""
    with open("tareas.txt", "w")as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea['descripcion']}, {tarea['completada']}\n")
    print("Tareas guardadas correctamente.")


def cargar_tareas():
    """Funcion para cargar las tareas desde un archivo."""
    try:
        with open("tareas.txt", "r") as archivo:
            for linea in archivo:
                descripcion, completada = linea.strip().split(",")
                tarea = {"descripcion": descripcion, "completada": completada == "True"}
                tareas.append(tarea)
        print("Tareas cargadas correctamente.")
    except ValueError:
        print("No se encontraron tareas guardadas.")


def menu():
    """Menu principal del sistema de gestion de tareas."""
    while True:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion  = input("Elige una opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            guardar_tareas()
            print("Saliendo del programa... bip bop... :D            @alanccoya")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")

menu()