num = int(input("Número de palabras de la lista: "))
palabras = []
if num <= 0:
    print("Número no válido.")
else:
    for x in range(1,num+1):
        palabra = input(f"Dime la palabra {x}: ")
        palabras.append(palabra)
    print(f"La lista creada es: {palabras}")
    y = input("Palabra a buscar: ")
    i = 0
    for x in palabras:
        if x == y:
            i += 1
    print(f"La palabra esta {i} veces.")