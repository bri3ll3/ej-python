#pedir las notas de cada parcial realizado en un trimestre

primero = int(input("Introduzca la nota de su primer paracial: "))
segundo = int(input("Introduzca la nota de su segundo parcial: "))
tercero = int(input("Introduzca la nota de su tercer parcial: "))

#calcular 

calcular = primero + segundo + tercero 
calcular_2 = calcular/3

##condiciones para aprobar

if calcular_2 >= 5 :
    print("Enorabuena has aprobado con un: " + str(calcular_2))
else:
    print("Has suspendido con un: " + str(calcular_2))

#yay listo 