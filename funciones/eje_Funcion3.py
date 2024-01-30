#Crear una funcion que pida nombre del usuario, cantidad de productos, precio
#-colocar valores por defecto
#-pedir la información por input
#Nombre función: calcularPrecio
#Resultado= Hola nombre, tienes que pagar $ por la cantidad de productos #

def calcularPrecio(nombre= "usuario", cantProducto= 0, precio= 0):
    precio = precio * cantProducto
    print(f"Hola {nombre} tienes que pagar:  {precio} por la cantidad de:  {cantProducto}")
    
    
print("Bienvenido a su sistema")    
nombre = input("ingrese su nombre: ")
empanada = 2000
jugo = 2500
jabon_en_polvo = 3500
print(f"Los productos son: , empanada: ,{empanada} - Jugo:  {jugo} - jabon_en_polvo:  {jabon_en_polvo}" )
productos = input("Que productos desea: ")
cantProductos = eval(input("Ingrese la cantidad de productos: "))

if productos == empanada:
    precio= 2000
elif productos == jugo:
    precio = 2500
else:
    precio = 3500

calcularPrecio(nombre, cantProductos, precio)



