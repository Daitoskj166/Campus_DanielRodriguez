def listaTuplas(lista1, lista2):
    NuevaLista = []
    for i,j in zip(lista1,lista2):
        lis = [i,j]
        tupla = tuple(lis)
        NuevaLista.append(tupla)


    print(NuevaLista)

lista1 = ["Real Madrid","Barcelona","Manchester United","Bayern Munich","Liverpool"]
lista2 = ["Boston Celtics","Angeles Lakers","Chicago Bulls","San Antonio Spurs","Miami Heat"]

listaTuplas(lista1, lista2)