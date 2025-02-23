def es_primo(num):
    esprimo = True
    for x in range(2,num):
        esdiv = num % x
        if esdiv == 0:
            esprimo = False
    return esprimo


for i in range(1, 21):
    if es_primo(i):
        print(f"{i} es primo.")