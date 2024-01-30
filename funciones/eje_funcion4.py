def nombres(nombre):
    print("Hola ", nombre)


def areaCuadrado(lado):
    return lado * lado
    
    

nombre = input("ingrese su nombre: ")
nombres(nombre)

lado = eval(input("ingrese el lado: "))
areaCuadrado(lado)

area = areaCuadrado(lado)
print("El area es: ", area, "Cm")

