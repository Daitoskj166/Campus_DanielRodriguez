"""
Verificación de Edad:
Pregunta a una persona su edad y utiliza una declaración if para determinar si es mayor de 18 años y puede votar.
"""

nota = eval(input("ingrese una calificacion numerica: "))

if nota <= 25:
    print("Tu nota es D")
elif nota <= 50:
    print("Tu nota es C")
elif nota <= 75:
    print("Tu nota es B")
else:
    print("Tun nota es A")    