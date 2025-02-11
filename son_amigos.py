def suma_divisores(valor):
    suma = 0
    if valor >= 0:
     for i in range(n1-1, 0, -1): #desde el número hasta 1
      if valor % i ==0: #Si el resto es 0, es divisor
         suma += i
    return suma

def son_amigos(valor_1,valor_2):
    if suma_divisores(valor_1) == valor_2 and suma_divisores(valor_2) == valor_1 :
        return True

n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro número: "))

div_y_suma = suma_divisores(n1)
div_y_suma_2 = suma_divisores(n2)

if son_amigos(n1,n2):
    print(f"{n1} y {n2} son amigos. ")
else:
    print(f"{n1} y {n2} no son amigos. ")

print(div_y_suma)
print(div_y_suma_2)
