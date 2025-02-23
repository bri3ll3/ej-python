numA = int(input("Dime un número: "))
numB = int(input("Dime otro número: "))
MCD = 0
if numA == numB:
    print("El MCD es "+str(numA))
elif numA > numB:
    for x in range(1, numB+1):
        esdiv = numA % x
        if esdiv == 0:
            for y in range(1, numB+1):
                esdiv = numB % y
                if esdiv == 0:
                    if x == y:
                        if x > MCD:
                            MCD = x
print(str(MCD))