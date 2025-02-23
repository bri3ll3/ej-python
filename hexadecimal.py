hexa = ""
num = int(input("Introduce un número decimal: "))
numcont = num
if num == 0:
    print("El decimal 0 es en hexadecimal 0")
else:
    while numcont > 0:
        resto = numcont % 16
        if resto == 10:
            hexa = "A" + hexa
        elif resto == 11:
            hexa = "B" + hexa
        elif resto == 12:
            hexa = "C" + hexa
        elif resto == 13:
            hexa = "D" + hexa
        elif resto == 14:
            hexa = "E" + hexa
        elif resto == 15:
            hexa = "F" + hexa
        else:
            hexa = str(resto) + hexa 
        numcont = numcont // 16
    print("El decimal "+str(num)+" es en binario "+hexa)