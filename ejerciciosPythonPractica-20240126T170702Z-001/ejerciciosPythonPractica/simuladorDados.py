import random
intentos = 0
resultadoDado = 0

while resultadoDado != 6:
    resultadoDado = random.randint(1,6)
    intentos += 1
    print(f"Lanzamiento {intentos}: {resultadoDado}")

print(f"Se botuvo un 6 en el intento {intentos}")