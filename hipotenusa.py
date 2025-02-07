from  math  import  * 

def hipotenusa(cateto_1,cateto_2):
    cat1 = cateto_1**2
    cat2 = cateto_2**2
    resultado = sqrt(cat1 + cat2)
    return resultado

print("Para calcular la hipotenusa se utiliza \nel teorema de Pitágoras:h² = a² + b² ")
primer_cateto = int(input("Introduzca el valor de la a: "))
segundo_cateto = int(input("Introduzca el valor de la b: "))

h = hipotenusa(primer_cateto,segundo_cateto)
print(f"La hipotenusa es : {h}")