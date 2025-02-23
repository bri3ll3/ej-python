num1 = int(input("Número de palabras de la lista: "))
num2 = int(input("Número de palabras de la lista que se eliminan: "))
lista1 = []
lista2 = []
if num1 <= 0 or num2 <= 0:
    print("Número no válido.")
else:
    
    #Crear lista1
    for x in range(1,num1+1):
        palabra = input(f"Dime la palabra {x}: ")
        lista1.append(palabra)
    print(f"La lista creada es: {lista1}")

    #Crear lista2
    for x in range(1,num2+1):
        palabra = input(f"Dime la palabra {x}: ")
        lista2.append(palabra)
    print(f"La lista de palabras a eliminar es: {lista2}")

    #Eliminación
    for palabElimina in lista2:
        i = 0
        while i < len(lista1):
            if palabElimina == lista1[i]:
                del lista1[i]
                i -= 1
            i += 1
    print(f"La lista final es {lista1}")