palabras = input("ingrese una palabra: ")
len(palabras)

if len(palabras) < 5:
    print("Corta")
elif len(palabras) >= 5 and len(palabras) <= 10:
    print("Media")
else:
    print("Larga")