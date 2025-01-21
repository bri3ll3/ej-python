cantidad = int(input("Introduzca una cantidad entera de euros: "))
denominaciones = [500,200,100,50,20,10,5,2,1]

for dinero in denominaciones:
    
    total = cantidad // dinero
    cantidad %= dinero

    # Comprueba si es moneda
    if dinero==1 or dinero ==2:

         #Si tengo más de una moneda
        if total >=2 :
            print(f"{total} monedas de {dinero} €")
        elif total == 1:
            print(f"{total} moneda de {dinero} €")

        # Si no, tengo solo una moneda

    # Si no, es billete
    else:
        # Si tengo más de un billete
        if total>=2:
            print(f"{total} billetes de {dinero} €")
         #Si no, tengo solo un billete
        elif total==1:
            print(f"{total} billete de {dinero} € ")

        