from random import randint

def suma(numero1,numero2):
    x = numero1 + numero2
    return x

def resta(numero1,numero2):
    x = numero1 - numero2
    return x

def multiplicacion(numero1,numero2):
    x = numero1 * numero2
    return x

def division(numero1,numero2):
    x = numero1 / numero2
    return x

def exponente(numero1,numero2):
    x = numero1 ** numero2
    return x
def tirada_dado():
    x = randint(1,6)
    return x
numero1 = tirada_dado()
numero2 = tirada_dado()
s = suma(numero1, numero2)
r = resta(numero1, numero2)
m = multiplicacion(numero1, numero2)
d = division(numero1, numero2)
e = exponente(numero1, numero2)
print( "Suma: " + str( s ) )
print( "Resta: " + str( r ) )
print( "Multiplicación: " + str( m ) )
print( "División: " + str( d ) )
print( "Exponente: " + str( e ) )