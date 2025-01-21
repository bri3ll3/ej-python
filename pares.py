número = int(input("Introduzca un número entero menor que 100: "))

par = número%2

if par == 0:

 for i in range(número,1001,2):
    print(i)

else:
  for i in range(número,1001,2):
    print(i+1)