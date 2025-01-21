#pedir los valores
print("Este programa resuelve la siguiente ecuación: ax + b = 0")
a = float(input("Introduzca un introduzca un valor para la a: "))
b = float(input("Introduzca un introduzca un valor para la b: "))

#calcular la ec.

x = -b/a 

###solución:

if a == 0 or b == 0 :
    print("La ecuación no tiene solución.")
else: 
    print("La solución de la ecuación es: " + str(x))