#introducir un nr.
nr = int(input("Introduzca un introduzca un número entero: "))

#el doble

op = nr*2

#hacer la operación

op2 = op%2

if op2 == 0:
    print("El doble del número es par ")
else:
    print("El doble del número no es par.")

    