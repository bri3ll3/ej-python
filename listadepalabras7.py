num1 = int(input("Número de palabras de la lista: "))
lista = []

if num1 <= 0:
    print("Número no válido.")
    
else:
    
    #Crear lista
    for x in range(1,num1+1):
        palabra = input(f"Dime la palabra {x}: ")
        lista.append(palabra)
    print(f"La lista creada es: {lista}")
    
    #Borrar repetidos
    for x in lista:
        i = 0
        repetido = False
        while i < len(lista):
            if x == lista[i]:
                if repetido == False:
                    repetido = True
                else:
                    del lista[i]
                    i -= 1
            i += 1
    print(f"La nueva lista es {lista}.")