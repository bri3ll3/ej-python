print("Muestre todos los números enteros del 0 al 100:")
for x in range(0,101):
    print(x)
print("Muestre todos los números enteros del 100 al 0:")
for x in range(-100,1):
    x = -x
    print(x)
print("Muestre todos los números pares del 0 al 100:")
for x in range(0,101):
    par = x%2
    if par == 0:
        print(x)
print("Muestre todos los números impares del 0 al 99:")
for x in range(0,100):
    par = x%2
    if par == 1:
        print(x)