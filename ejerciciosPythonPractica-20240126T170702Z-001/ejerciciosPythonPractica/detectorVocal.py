
texto = input("ingresa un frase: ")
vocales = "AaEeIiOoUu"
j = 0
k = 0
for i in texto:
    if i in vocales:
        j = j+1
print(f"La frase tiene {j} vocales")
