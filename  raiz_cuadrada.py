número = int(input("Introduzca un número entero para obtener su raíz cuadradada : "))

import math 

raíz = math.sqrt(número)

if raíz < 0 :
    print("La raíz de números negativos no se puede realizar: ")

else: 
    print(str(raíz))
    
