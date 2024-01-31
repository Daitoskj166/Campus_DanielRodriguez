lista_de_tareas = []

def añadir_tareas(tarea, lista_de_tareas,prioridad):
    if any(t['nombre'] == tarea for t in lista_de_tareas):
        print("La tarea ya existe.")
    else:
        nueva_tarea = {'nombre': tarea, 'prioridad': prioridad}
        lista_de_tareas.append(nueva_tarea)
        print(f"nombre '{tarea}' añadida con prioridad {prioridad}")

def mostrar_tareas(lista_de_tareas):
    if not lista_de_tareas:
        print("No hay tareas pendientes")
    else:
        print("Tareas pendientes")
        for tarea in sorted (lista_de_tareas, key=lambda x: x['prioridad'], reverse= True):
             print(f"Nombre: {tarea['nombre']}, Prioridad: {tarea['prioridad']}")

def eliminar_tareas(eliminarTarea,lista_de_tareas):    
    if not lista_de_tareas:
        print("No hay nada que eliminar")
    else:
        for tarea in lista_de_tareas:
            if tarea['nombre'] == eliminarTarea:
                lista_de_tareas.remove(tarea)
                print(f"Tarea: '{tarea}' eliminada")
            else:
                print(f"Tarea '{tarea}' no encontrado")


opcion = 0
while opcion != 4:
    print("1-Añadir una tarea, 2- Mostrar tareas pendientes, 3- Eliminar una tarea, 4-Salir del programa")
    opcion = eval(input("Porfavor escoja entre las siguientes opciones: "))
    if opcion > 4 or opcion < 1:
        print("Error, vuelva a ingresar")
    
    if opcion == 1:
        tarea = input("ingrese la tarea: ")
        tarea = tarea.lower()
        prioridad = eval(input("ingrese su prioridad: "))
        añadir_tareas(tarea,lista_de_tareas,prioridad)
    if opcion == 2:
        mostrar_tareas(lista_de_tareas)
    if opcion == 3:
        eliminarTarea = input("Ingrese el nombre de la tarea que desea eliminar: ")
        eliminartarea = eliminarTarea.lower()
        eliminar_tareas(eliminarTarea,lista_de_tareas)
else:
    print("Cesion Finalizada")