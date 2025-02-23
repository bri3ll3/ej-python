num1 = int(input("Número de palabras de la lista 1: "))
num2 = int(input("Número de palabras de la lista 2: "))

if num1 <= 0 or num2 <= 0:
    print("Número no válido.")
    
else:
    
    def crearLista(num):
        lista = []
        #Crear lista
        for x in range(1,num+1):
            palabra = input(f"Dime la palabra {x}: ")
            
            #Comprobar que no este repetida la lista
            repetido = False
            for y in lista:
                if palabra == y:
                    repetido = True
            if repetido == False:
                lista.append(palabra)

        return lista
    
    lista1 = crearLista(num1)
    print(f"La lista 1 es {lista1}")
    
    lista2 = crearLista(num2)
    print(f"La lista 2 es {lista2}")
    
    #Listas nuevas
    listaRepe = []
    listaSolo1 = []
    listaSolo2 = []
    repetido = False
    for palabra1 in lista1:
        for palabra2 in lista2:
            if palabra2 == palabra1:
                repetido = True
        if repetido == True:
            listaRepe.append(palabra1)
        else:
            listaSolo1.append(palabra1)
    
    for palabra2 in lista2:
        for palabra1 in lista1:
            if palabra2 == palabra1:
                repetido = True
        if repetido == False:
            listaSolo1.append(palabra1)
