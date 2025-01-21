número = int(input("Dime un número entero: "))
sumatorio = 0
for i in range(1,número+1,2):
    sumatorio = sumatorio + i

print(f"El sumatorio de impares del 1 al {número} : {sumatorio}")