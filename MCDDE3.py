variable_1 = int(input("Dime un número: "))
variable_2 = int(input("Dime otro número: "))
variable_3 = int(input("Dime otro número: "))

mcd = 0
menor = variable_1

if variable_2 < variable_1:
    menor = variable_2

for x in range(1, menor+1):
    div_1 = variable_1 % x
    div_2 = variable_2 % x
    div_3 = variable_3 % x
    if div_1 == 0 and div_2 == 0 and div_3 == 0:
         if x > mcd:
          mcd = x 
print(str(mcd))
