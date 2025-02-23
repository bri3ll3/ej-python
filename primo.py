num = int(input("Introduce un número: "))
div = 2
esprimo = True
if num == 1:
    print("1 no es primo.")
else:
    while div < num:
        if num % div == 0:
            esprimo = False
        div += 1
    if esprimo == False:
        print(str(num)+" no es primo.")
    else:
        print(str(num)+" es primo.")
