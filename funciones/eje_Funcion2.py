def compras(*productos):
    print(productos)
 
compras("Camisa", "Televisor", "Arroz") #Esto imprime: ('Camisa', 'Televisor', 'Arroz')


def persona(**datos):
    print(datos)
 
persona(Nombre = "Pepe Perez", Email = "pepe@email.com") #Esto imprime: {'Nombre': 'Pepe Perez', 'Email': 'pepe@email.com'}