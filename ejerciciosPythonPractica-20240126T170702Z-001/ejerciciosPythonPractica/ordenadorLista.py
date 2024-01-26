ordenado = []

cantidad = eval(input("ingrese la cantidad de numeros que desea ingresar: "))

x = 1

while x <= cantidad:
    numero = eval(input("ingrese un numero: "))
    ordenado.append(numero)
    x += 1

print("La lista original es: " ,ordenado)

ordenado.sort()

print("La lista ordenada es: " ,ordenado)