a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
if a == 0:
    if b == 0:
        print("Tiene infinitas soluciones porque a es 0.")
    else:
        print("No tiene solución porque tanto a como b son 0.")
else:
    x = -b/a
    print("El valor de x para "+str(a)+"x+"+str(b)+"=0 es "+str(x)+".")
    