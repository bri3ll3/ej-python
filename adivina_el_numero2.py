import random
aleat = random.randint(1, 50)
num = int(input("Dime un número entre el 1 y el 50: "))
intentos = 4
while intentos != 0:   
    if num < 1 or num >50:
        print(str(num)+" no esta entre el 1 y el 50")
    else:
        if num > aleat:
            print("¡Te has pasado! Te quedan "+str(intentos)+" intentos.")
        elif num == aleat:
            print("¡Muy bien! Era el "+str(aleat)+".")
            break
        else:
            print("¡Te has quedado corto! Te quedan "+str(intentos)+" intentos.")
        intentos -= 1
    num = int(input("Dime un número entre el 10 y el 50: "))    
print("Te has quedado sin intentos.")