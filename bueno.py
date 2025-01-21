numA = int(input("Dime un número: "))
numB = int(input("Dime otro número: "))
numC = int(input("Dime otro número: "))
MCD = 0
menor = min(numA, numB, numC)
if numA < 0 or numB < 0 or numC < 0:
    print("No pueden ser negativos.")
if numA == 0 or numB == 0 or numC == 0:
    print("0 no tiene divisores.")
else:
    if numA == numB == numC:
        print("El MCD es "+str(numA))
    else:
        for x in range(1, menor+1):
            esdivA = numA % x
            esdivB = numB % x
            esdivC = numC % x
            if esdivA == 0 and esdivB == 0 and esdivC == 0:
                if x > MCD:
                    MCD = x
    print(str(MCD))