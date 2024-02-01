def outer_function(x):       # funcion externa recibe el valor de x
    def inner_function(y):   # funcion interna recibe el valor de y
        return x + y
    return inner_function

print(outer_function(x=10)(y=6))