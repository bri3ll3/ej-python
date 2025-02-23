def invertir_lista(lista):
    listaInvertida = []
    for x in reversed(lista):
        listaInvertida.append(x)
    return listaInvertida

miLista = [ "David", "llamo", "me", "Hola" ]
listaInvertida = invertir_lista( miLista )
print(f"La lista {miLista} invertida es: {listaInvertida}")