dinero = int(input("Introduce tu dinero: "))
if dinero >= 500:
    billet500 = dinero // 500
    dinero -= billet500 * 500
    print("Tienes "+str(billet500)+" billetes de 500 euros.")
if dinero >= 200:
    billet200 = dinero // 200
    dinero -= billet200 * 200
    print("Tienes "+str(billet200)+" billetes de 200 euros.")
if dinero >= 100:
    billet100 = dinero // 100
    dinero -= billet100 * 100
    print("Tienes "+str(billet100)+" billetes de 100 euros.")
if dinero >= 50:
    billet50 = dinero // 50
    dinero -= billet50 * 50
    print("Tienes "+str(billet50)+" billetes de 50 euros.")
if dinero >= 20:
    billet20 = dinero // 20
    dinero -= billet20 * 20
    print("Tienes "+str(billet20)+" billetes de 20 euros.")
if dinero >= 10:
    billet10 = dinero // 10
    dinero -= billet10 * 10
    print("Tienes "+str(billet10)+" billetes de 10 euros.")
if dinero >= 5:
    billet5 = dinero // 5
    dinero -= billet5 * 5
    print("Tienes "+str(billet5)+" billetes de 5 euros.")
if dinero >= 2:
    billet2 = dinero // 2
    dinero -= billet2 * 2
    print("Tienes "+str(billet2)+" monedas de 2 euros.")
if dinero >= 1:
    billet1 = dinero // 1
    dinero -= billet1 * 1
    print("Tienes "+str(billet1)+" monedas de 1 euro.")