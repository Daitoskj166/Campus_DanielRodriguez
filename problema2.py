''''
un programa que le pregunte al usuario el nombre, numero de horas trabajadas, el costo por hora, y debe mostrar al
final el señor tal se le debe tanto

'''''

nombre = input("ingrese su nombre: ")
horas = eval(input("ingrese las horas trabajadas: "))
costo = eval(input("ingrese el costo por hora: "))

total = (horas * costo)

print ("Al caballero " + nombre + "que trabajo ", horas, "horas " + "se le debe pagar ",  total, "dolares")