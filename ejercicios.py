"""
Verificación de Edad:
Pregunta a una persona su edad y utiliza una declaración if para determinar si es mayor de 18 años y puede votar.

Clasificación de Notas:
Pide una calificación numérica y utiliza condicionales elif para asignar una calificación en letras, como A, B, C o D.

Decisión de Comida:
Permítele a alguien elegir un tipo de comida y utiliza condicionales if para recomendar un restaurante según la elección (por ejemplo, comida italiana, mexicana o china).

Verificación de Contraseña:
Solicita una contraseña y utiliza una declaración if para verificar si coincide con una contraseña predefinida antes de permitir el acceso.

Verificación de Palíndromo:
Pide a alguien que ingrese una palabra y utiliza condicionales para determinar si es un palíndromo, es decir, si s

"""

#Verificacion de Edad:
#Pregunta a una persona su edad y utiliza una declaración if para determinar si es mayor de 18 años y puede votar.
edad = eval(input("ingrese su edad: "))

if edad < 18:
    print("Eres menor de edad, por eso no puedes votar")
else:
    print("Eres mayor de edad, Puedes votar")


#Clasificación de Notas:
#Pide una calificación numérica y utiliza condicionales elif para asignar una calificación en letras, como A, B, C o D.

nota = eval(input("ingrese una calificacion numerica: "))

if nota <= 25:
    print("Tu nota es D")
elif nota <= 50:
    print("Tu nota es C")
elif nota <= 75:
    print("Tu nota es B")
else:
    print("Tun nota es A")    
    
    
#Decisión de Comida:
#Permítele a alguien elegir un tipo de comida y utiliza condicionales if para recomendar un restaurante según la elección (por ejemplo, comida italiana, mexicana o china).

print("pasta, ramen, taco, bandeja paisa")
restaurante = input("ingresa comida desea comer: ")

if restaurante == "pasta":
    print("Valla a un restaurante italiano")
elif restaurante == "ramen":
    print("Valla a un restaurante japones")
elif restaurante == "bandeja paisa":
    print("Valla a un restaurante colombiano")