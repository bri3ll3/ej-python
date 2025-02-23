num = int(input("Número de palabras de la lista: "))
palabras = []
if num <= 0:
    print("Número no válido.")
else:
    
    #Crear lista
    for x in range(1,num+1):
        palabra = input(f"Dime la palabra {x}: ")
        palabras.append(palabra)
    print(f"La lista creada es: {palabras}")
    
    #Cambiar lista
    sust = input("Palabra a eliminar: ")
    i = 0
    while i < len(palabras):
        if palabras[i] == sust:
            del palabras[i]
            i -= 1
        i += 1
    print(f"La nueva lista es {palabras}.")