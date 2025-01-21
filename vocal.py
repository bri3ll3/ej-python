#Diseña un programa, vocal.py, que lea un carácter por el teclado (en minúsculas) y muestre un mensaje indicando si el carácter introducido es una vocal.

#crear la variable pidiendo un carácter

carácter = str(input("Introduzca un carácter: "))

if carácter == "a" or carácter == "e" or carácter == "i" or carácter == "o" or carácter == "u":
    print(" Su carácter es una vocal.")
else: 
    print("Su carácter no es una vocal. ")

if carácter <= "A" and carácter <= "Z":
    print("Es una mayúscula.")
else: 
    print("Es una minúscula.")