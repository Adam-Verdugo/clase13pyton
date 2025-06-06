import random #libreria para llamar y crear numeros random

numeros = []



for x in range(10):
    n = random.randint(1,10)
    numeros.append(random.randint(1,10))

numeros.sort()
print(numeros)

par = 0
impar = 0

for i in range(len(numeros)):
    if numeros[i]%2==0:
        par +=1
    else: impar +=1

print(f"""cantidad de numeros pares : {par}
cantidad de numeros impars : {impar}""")

