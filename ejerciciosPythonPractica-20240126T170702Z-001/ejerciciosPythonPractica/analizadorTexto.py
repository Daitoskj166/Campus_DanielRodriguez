
texto = input("ingresa un texto: ")
vocales = "AaEeIiOoUu"
letras = "QqWwRrTtYyPpSsDdFfGgHhJjKkLlÑñZzXxCcVvBbNnMm""aeiouuAeiou"
j = 0
k = 0
for i in texto:
    if i in vocales:
        j = j+1
print(f"La frase tiene {j} vocales")


for i in texto:
    if i in letras:
        k = k+1
print(f"La frase tiene {k} letras")