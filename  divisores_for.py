
numero = int(input("Dime un número: "))

if numero >= 0:
    for i in range(numero, 0, -1): #desde el número hasta 1
        if numero % i ==0: #Si el resto es 0, es divisor
            print(i)
else:
    print("Introduzca un número y pruebe nuevamente.")





