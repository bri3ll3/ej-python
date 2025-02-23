x = int(input("Introduce un número entero: "))
i = 1
if x > 0:
    print("Los divisores de "+str(x)+" son: ")
    while i <= x:
        if x % i == 0:
            print(str(i)+" y "+str(-i))
        i += 1
elif x == 0:
    print("No tiene divisores.")
else:
    print("Los divisores de "+str(x)+" son: ")
    x = -x
    while i <= x:
        if x % i == 0:
            print(str(i)+" y "+str(-i))
        i += 1