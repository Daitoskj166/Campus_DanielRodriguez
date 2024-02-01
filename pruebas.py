def añadir_tarea(nombre_tarea, lista_tareas):
    nueva_tarea = {'nombre': nombre_tarea, 'prioridad': 5}
    lista_tareas.append(nueva_tarea)
    print(f"Tarea '{nombre_tarea}' añadida con prioridad {nueva_tarea['prioridad']}.")

def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for tarea in sorted(lista_tareas, key=lambda x: x['prioridad'], reverse=True):
            print(f"Nombre: {tarea['nombre']}, Prioridad: {tarea['prioridad']}")

def eliminar_tarea(nombre_tarea, lista_tareas):
    for tarea in lista_tareas:
        if tarea['nombre'] == nombre_tarea:
            lista_tareas.remove(tarea)
            print(f"Tarea '{nombre_tarea}' eliminada.")
            return
    print(f"Tarea '{nombre_tarea}' no encontrada.")

# Inicialización de la lista de tareas
lista_de_tareas = []

while True:
    print("\nMenú:")
    print("1. Añadir una nueva tarea.")
    print("2. Mostrar todas las tareas pendientes.")
    print("3. Eliminar una tarea.")
    print("4. Salir del programa.")

    opcion = input("Por favor, elija una opción (1-4): ")

    if opcion == '1':
        nombre_tarea = input("Ingrese el nombre de la tarea: ")
        añadir_tarea(nombre_tarea, lista_de_tareas)
    elif opcion == '2':
        mostrar_tareas(lista_de_tareas)
    elif opcion == '3':
        nombre_tarea = input("Ingrese el nombre de la tarea que desea eliminar: ")
        eliminar_tarea(nombre_tarea, lista_de_tareas)
    elif opcion == '4':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")