import random #libreria para llamar y crear numeros random

numeros = []



for x in range(1000):
    n = random.randint(1,1000)
    numeros.append(random.randint(1,1000))

numeros.sort()
print(numeros)
