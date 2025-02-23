import random
aleat = random.randint(10, 30)
num = int(input("Dime un número entre el 10 y el 30: "))
while num != aleat:   
    if num < 10 or num >30:
        print(str(num)+" 1no esta entre el 10 y el 30")
    else:
        if num > aleat:
            print("¡Te has pasado!")
        else:
            print("¡Te has quedado corto!")
    num = int(input("Dime un número entre el 10 y el 30: "))    
print("¡Muy bien! Era el "+str(aleat)+".")