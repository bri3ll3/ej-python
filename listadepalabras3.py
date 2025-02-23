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
    sust = input("Palabra a sustituir: ")
    nuev = input("Palabra que reemplazará a la anterior: ")
    i = 0
    for x in palabras:
        if x == sust:
            palabras[i] = nuev
        i += 1
    print(f"La nueva lista es {palabras}.")
    