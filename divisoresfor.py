def divisores(num): 
    divisores = []
    for x in range(1,num):
        esdiv = num % x
        if esdiv == 0:
            divisores.append(x)
    return divisores

numero = 17
divs = divisores(numero)
print(f"Los divisores de {numero} son {divs}")