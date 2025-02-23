x = int(input("Introduce un número entero: "))
i = 1
y = 0
while i <= x:
    y += i
    i += 1
print("El sumatorio de todos los numeros hasta el "+str(x)+" es "+str(y)+".")