variable_1 = int(input("Dime un número: "))
variable_2 = int(input("Dime otro número: "))
mcd = 0
if variable_1 == variable_2:
    print("El MCD es "+str(variable_1))
elif variable_1 > variable_2:
    for x in range(1, variable_2+1):
        esdiv = variable_1 % x
        if esdiv == 0:
            for y in range(1, variable_2+1):
                esdiv = variable_2 % y
                if esdiv == 0:
                    if x == y:
                        if x > mcd:
                            mcd = x
print(str(mcd))

