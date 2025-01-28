#MCD de una lista indeterminada de números. -al principio del programa.-

#pedir de cuantos numeros quieres que sea la lista
#creamos una lista vacia para guardar los valores
x = int(input("De cuantos numeros quieres que sea la lista? Introduzca un numero positivo : "))
lista = []
for i in range(x):
    num = int(input("Dime un numero: "))
    lista.append(num)
#Definimos el menor
menor = min(lista)
mcd = 0
#Calcular el mcd
for i in range(1, menor+1):
     for j in lista :
        div =  j%i
        if div == 0:
          if i > mcd:
             mcd = i

print(str(mcd))
