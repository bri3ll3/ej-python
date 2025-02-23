import math
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
raiz = b**2-4*a*c
if raiz > 0:
    raizForm = math.sqrt(raiz)
    formPosit = (-b+raizForm)/2*a
    formNegat = (-b-raizForm)/2*a
    print("El valor de x puede ser "+str(formPosit)+" o "+str(formNegat)+".")
elif raiz == 0:
    formCero = -b/2*a
else:
    print("No tiene solución.")