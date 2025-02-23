num = int(input("Dime un número: "))
if num < 0:
    num = -num
if num > 1:
    for x in reversed(range(1,num+1)):
        esdiv = num % x
        if esdiv == 0:
            print(str(x)+" y "+str(-x))
if num == 1:
    print("1 y -1")
if num == 0:
    print("0")