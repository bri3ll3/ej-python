num1 = int(input("Número de palabras de la lista: "))
lista1 = []
lista2 = []
if num1 <= 0:
    print("Número no válido.")
else:
    
    #Crear lista1
    for x in range(1,num1+1):
        palabra = input(f"Dime la palabra {x}: ")
        lista1.append(palabra)
    print(f"La lista creada es: {lista1}")

    #Crear lista2
    for x in reversed(lista1):
        lista2.append(x)
    print(f"La lista de palabras inversa es: {lista2}")