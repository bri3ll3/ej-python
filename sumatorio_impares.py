x = int(input("Introduce un número entero: "))
i = 1
y = 0
while i <= x:
    if i%2 == 1:
        y += i
    i += 1
print("El sumatorio de todos los numeros impares hasta el "+str(x)+" es "+str(y)+".")
