def maximo(lista):
    return max(lista)

def minimo(lista):
    return min(lista)

lista = [ "lunes", "martes", "miércoles", "jueves", "viernes" ]
cadenaMaxima = maximo(lista)
cadenaMinima = minimo(lista)
print( f"El máximo de {lista} es: {cadenaMaxima}" )
print( f"El mínimo de {lista} es: {cadenaMinima}" )