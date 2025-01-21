primer_nr = int(input("Dime un número: "))
segundo_nr = int(input("Dime otro número: "))
tercer_nr = int(input("Dime uno más: "))
mcd = 0
menor = min(primer_nr, segundo_nr, tercer_nr)
if primer_nr < 0 or segundo_nr < 0 or tercer_nr< 0 :
    print("No pueden ser números negativos.")
if primer_nr == 0 or segundo_nr == 0 or  tercer_nr == 0:
    print("No tienen divisores.")
else:
    if primer_nr == segundo_nr == tercer_nr:
        print(f"El MCD es {primer_nr}")
    else: 
        for i in range(1, menor+1):
            div_primer_nr= primer_nr % i
            div_segundo_nr= segundo_nr % i
            div_tercer_nr = tercer_nr % i
            if div_primer_nr == 0 and div_segundo_nr == 0 and div_tercer_nr ==0:
                if i > mcd:
                    mcd = i
                    print(str(mcd))
        
