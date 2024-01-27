#creo una lista para guardar los numeros ingresados, la lista se llamara "ordenado"
ordenado = []
#luego le pregunto al usuario que ingrese la cantidad de numeros que quiere ingresar, para guardar esa cantidad en la lista ordenado
cantidad = eval(input("ingrese la cantidad de numeros que desea ingresar: "))
#creo una variable para usarla en un ciclo
x = 1
#creo un ciclo while desde x=1 hasta la cantidad ingresada por el usuario
#donde mientras arranque va a pedir un numero y se ira guardando ese numero
#en la lista, y al final de ese ciclo pongo una suma acumulada x += 1
while x <= cantidad:
    numero = eval(input("ingrese un numero: "))
    ordenado.append(numero)
    x += 1

print("La lista original es: " ,ordenado)
#luego uso una funcion sort para ordenar de menor a mayor todos los numeros ingresados en la lista "ordenado" y luego lo imprimo

ordenado.sort()

print("La lista ordenada es: " ,ordenado)