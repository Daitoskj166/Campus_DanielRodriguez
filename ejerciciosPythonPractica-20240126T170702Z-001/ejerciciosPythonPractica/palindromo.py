variableIngresada = input ("ingrese la palabra para determinar si es palindroma: ")



if variableIngresada == variableIngresada[::-1]:
    print("Es palindroma")
else:
    print("No es palindroma")