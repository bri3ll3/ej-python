from random import randint
def tirada_dado():
    x = randint(1,6)
    return x
for i in range(10):
    tirada = tirada_dado()
    print(tirada)