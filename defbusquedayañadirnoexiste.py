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

def añadir_si_no_existe(lista, valor):
    if busqueda(lista, valor) == -1:
        lista.append(valor)
        return True
    else:
        return False
lista = [ 1, 2, 3, 4, 5 ]

valor = 3
añadido = añadir_si_no_existe( lista, valor )
if añadido:
    print(f"El número {valor} se ha añadido a la lista {lista}")
else:
    print(f"El número {valor} ya existía en la lista {lista}")