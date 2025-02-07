def suma(numero_1,numero_2):
    s = numero_1 + numero_2
    return s

def resta(numero_1, numero_2):
    r = numero_1 - numero_2
    return r

def multiplicacion(numero_1, numero_2):
    m = numero_1* numero_2
    return m

def division(numero_1, numero_2):
    d= numero_1/ numero_2
    return d

def exponente(numero_1, numero_2):
    e = numero_1**numero_2
    return e

def tirada_dado():
    return randint(1, 6)

from random import *
numero = randint(1, 6)


n1 = tirada_dado()
n2 = tirada_dado()

resultado_suma = suma(n1,n2)
resultado_resta = resta(n1,n2)
resultado_multiplicacion = multiplicacion(n1,n2)
resultado_division = division(n1,n2)
resultado_exponente = exponente(n1,n2)

print(f"Suma: {resultado_suma} \n Resta: {resultado_resta}\n Multiplicacion: {resultado_multiplicacion} \n Division: {resultado_division} \n Exponente: {resultado_exponente}")
print(n1)
print(n2)
