per1 = int(input("Elige entre 1(Piedra) , 2(Papel) o 3(Tijeras): "))
per2 = int(input("Elige entre 1(Piedra) , 2(Papel) o 3(Tijeras): "))
if per1 == 1 and per2 == 1:
    print("Empate (piedra y piedra)")
elif per1 == 1 and per2 == 2:
    print("Gana la persona 2 (piedra pierde a papel)")
elif per1 == 1 and per2 == 3:
    print("Gana la persona 1 (piedra gana a tijeras)")
elif per1 == 2 and per2 == 1:
    print("Gana la persona 1 (papel gana a piedra)")
elif per1 == 2 and per2 == 2:
    print("Empate (papel y papel)")
elif per1 == 2 and per2 == 3:
    print("Gana la persona 2 (papel pierde a tijeras)")
elif per1 == 3 and per2 == 1:
    print("Gana la persona 2 (tijeras pierde a piedra)")
elif per1 == 3 and per2 == 2:
    print("Gana la persona 1 (tijeras gana a papel)")
elif per1 == 3 and per2 == 3:
    print("Empate (tijeras y tijeras)")
else:
    print("Introduce valores adecuados.")