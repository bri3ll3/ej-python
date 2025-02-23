def suma_divisores(num):
    sumadiv = 0
    for x in range(1,num):
        esdiv = num % x
        if esdiv == 0:
            sumadiv += x
    return sumadiv

def son_amigos(num1,num2):
    suma1 = suma_divisores(num1)
    suma2 = suma_divisores(num2)
    if suma1 == numero2 and suma2 == numero1:
        return True
    else:
        return False

numero1 = 1184
numero2 = 1210
if son_amigos( numero1, numero2 ):
    print( str(numero1) + " y " + str(numero2) + " son amigos")
else:
    print( str(numero1) + " y " + str(numero2) + " no son amigos" )