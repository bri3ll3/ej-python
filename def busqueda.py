def busqueda(lista,valor):
    i = 0
    estaenlista = False
    for x in lista:
        i += 1
        if x == valor:
            estaenlista = True
            return i
    if estaenlista == False:
        return -1

lista = [ 20, 30, 2, 3, 100 ]
valor = 30
indice = busqueda( lista, valor )
print("Índice: " + str(indice))