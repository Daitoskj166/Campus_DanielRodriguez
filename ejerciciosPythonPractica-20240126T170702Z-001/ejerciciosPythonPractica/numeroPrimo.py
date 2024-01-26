num = eval(input("Ingrese el numero: "))
x = 1
cont = 0
while x <= num:
    if num % x == 0:
        cont = cont + 1
    x += 1

if cont == 2:
    print("El numero",num,"es primo")
else:
    print("El numero",num,"no es primo")