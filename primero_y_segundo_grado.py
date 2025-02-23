import math
print("Para la fórmula ax²+bx+c = 0...")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
#Programa
if a != 0:
    print("Es una ecuación de segundo grado...")
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
else:
    print("Es una ecuación de primer grado...")
    if b == 0:
        if c == 0:
            print("Tiene infinitas soluciones porque a y b son 0.")
        else:
            print("No tiene solución porque a, b y c son 0.")
    else:
        x = -c/b
        print("El valor de x para "+str(b)+"x+"+str(c)+"=0 es "+str(x)+".")