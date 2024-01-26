temperatura = eval(input("ingrese la temperatura: "))
celsius1 = True
Fahrenheit1 = True

preguntas = eval(input("Quiere hacer la conversion? T/F: "))

if preguntas == True:
    if celsius1 == True and Fahrenheit1 == True:
        operacion = (temperatura*(9/5)+32)
        print("La conversion Celsius de" ,temperatura, "Celsius a" ,operacion, "Fahrenheit")
        operacion1 = ((temperatura-32)* 5/9)
        print("La conversion Fahrenheit de:" ,temperatura, "Fahrenheit a" ,operacion1, "Celsius")
    else:
        print("Adios")
else:
    print("Adios")
