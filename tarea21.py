import random #libreria para llamar y crear numeros random

personas = {}
numeros = []
par = 0
ma = 0
#1) lista de tamaño de 100 
for x in range(100):
    numeros.append(random.randint(0,10))


print(numeros)

ma = max(numeros)
mi = min(numeros)

#2) numeros con los indices pares
for x in range(len(numeros)):
    if x %2==0:
        print(f"posicion : {x} numeros : {numeros[x]}")


for x in range(len(numeros)):
    if numeros[x]%2==0:
        par +=1

#3)  mostrar el numero menor y mayor
print(f"numero mayor de la lista : {ma}")
print(f"numero minimo de la lista : {mi}")
print(f"cantidad de numeros pares : {par}")

#4) donde esta los numeros mayores
for x in range(len(numeros)):
    if numeros[x]==max(numeros):
        print("indice de numeros mayores  : ")
        print(x, end=" ")
print(" ")

for x in range(len(numeros)):
    if numeros[x]==min(numeros):
        print("indice de numeros menores : ")
        print(x, end=" ")
print(" ")

print("""
1) agregar personas
2) ver personas """)

seleccion = int("elija que opcion quiere hacer : ")

