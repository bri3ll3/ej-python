from turtle import *
lados = int(input("Introduce el número de lados: "))
speed(10)
color("blue")
relleno = 0
tamaño = 100
while relleno < tamaño:
    for i in range(lados):
        forward(tamaño - relleno)
        right(360 / lados)
    relleno += 1
exitonclick()