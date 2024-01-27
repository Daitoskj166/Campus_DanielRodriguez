contraseña = input("Ingrese la contraseña: ")

  

if len(contraseña) >= 8:
    if any(caracter.isupper() for caracter in contraseña):
        if any(caracter.islower() for caracter in contraseña):
            if any(caracter.isdigit() for caracter in contraseña):
                print("Contraseña creada")
            else:
                print("La contraseña al menos debe tener un numero")
        else:
            print("La contraseña al menos debe tener una minuscula")
    else:
        print("La contraseña debe tener al menos una mayuscula")
else:
    print("La contraseña debe tener minimo 8 caracteres")
