import secrets
import random

listaR = []
listaS = []

for i in range(10):
    listaR.append(random.randint(1, 20))
    listaS.append(secrets.randbelow(20) + 1)

print(listaR)
print(listaS)