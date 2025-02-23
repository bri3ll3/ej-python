num = int(input("Número de palabras de la lista: "))
palabras = []
if num <= 0:
    print("Número no válido.")
else:
    for x in range(1,num+1):
        palabra = input(f"Dime la palabra {x}: ")
        palabras.append(palabra)
    print(f"La lista creada es: {palabras}")