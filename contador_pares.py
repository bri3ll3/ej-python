num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
pares = 0
i = num1
while num1 <= num2:
    if num1%2 == 0:
        pares += 1
    num1 += 1
print("Entre el "+str(i)+" y el "+str(num2)+" hay "+str(pares)+" pares.")