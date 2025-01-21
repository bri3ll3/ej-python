edad1 = int(input("Introduzca una edad: "))
edad2 = int(input("Introduzca otra edad: "))
#comparar las edades de cada uno
if edad1 < edad2 :
    print("La edad " + str(edad1) + " es menor a la edad " + str(edad2)+ ".")
elif edad1 > edad2:
       print("La edad " + str(edad1) + " es mayor a la edad " + str(edad2) + ".")
#si las edades son iguales
else:
  print("La edad " + str(edad1) + " es igual a la edad "+ str(edad2))