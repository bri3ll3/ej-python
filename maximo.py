num = int(input("Introduce un número: "))
max = 0
while num > 0:
    if num > max:
        max = num
    num = int(input("Introduce otro número: "))
print("El máximo es: "+str(max))