variable_1 = int(input("Dime un número: "))
variable_2 = int(input("Dime otro número: "))

mcd = 0
menor = variable_1
mayor = variable_2

if variable_2 < variable_1:
    menor = variable_2
    mayor = variable_1

for x in range(1, menor+1):
    div_1 = menor % x
    div_2 = mayor % x
    if div_1 == 0 and div_2 == 0:
         if x > mcd:
          mcd = x 
print(str(mcd))


