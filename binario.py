#Variables
binar = ""
num = int(input("Introduce un número decimal: "))
bit = 0
#Rango
if 1024 > num >= 512:
    bit = 10
if 512 > num >= 256:
    bit = 9
if 256 > num >= 128:
    bit = 8
if 128 > num >= 64:
    bit = 7
if 64 > num >= 32:
    bit = 6
if 32 > num >= 16:
    bit = 5
if 16 > num >= 8:
    bit = 4
if 8 > num >= 4:
    bit = 3
if 4 > num >= 2:
    bit = 2
if 2 > num >= 0:
    bit = 1
#Calcula
if num > 1023 or num < 0:
    print("Has excedido el límite.")
else:
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    if bit > 0:
        binar = str(num % 2)+binar
        num = num // 2
        bit -= 1
    print(binar)