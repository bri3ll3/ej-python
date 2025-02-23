dinero = int(input("Introduce una cantidad de dinero: "))
billetes = [500,200,100,50,5,2,1]
for x in billetes:
    billet = dinero // x
    if billet > 0:
        if x > 2:
            print("Hay "+str(billet)+" billetes de "+str(x)+".")
        else:
            print("Hay "+str(billet)+" monedas de "+str(x)+".")
    dinero = dinero % x