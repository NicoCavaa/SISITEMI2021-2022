
#chiedere allutente qunati numeri vuole mettere in una stringa
"""
nelementi = int (input("inserisci il nuemro di numeri: "))
numeri = []

for x in range(nelementi):
    numeri.append(int(input("inserisci numero: ")))
print(numeri)

#altro medoto

risposta = "si"
lista = []
while(risposta == "si"):
    num=int(input("Inserisci un numero: "))
    lista.append(num)
    risposta = input("ancora? si/no ")
print(lista)
"""


#max e min
"""
numeri = [2,3,4,11,6,7,8,9]
max = numeri[0]
min = numeri[0]
for x in numeri:
    if x >max:
        max=x
    elif x < min:
        min = x
print(f"numero massimo: {max}\nnumero minimo: {min}")
"""


#numero primo
"""
def numPrimo(num):
    primo = True

    for x in range(2,num):
        if num % x==0:
            primo = False
    if primo:
        print("numero primo")
    else:
        print("numero non primo")

num = int(input("inserisci un numero: "))
numPrimo(num)

#altro metodo

def nprimi(n):
    k=2
    continua = True
    
    while continua == True and k<n:
        if(n%k==0):
            continua = False
        k=k+1
    return continua

n = int(input("inserisci un numero: "))
nprimi(n)
if(nprimi(n)==True):
    print("primo")
else:
    print("non primo")
"""


#tutti i numeri primi prima di 1000
"""
def nprimi(n):
    k=2
    continua = True
    
    while continua == True and k<n:
        if(n%k==0):
            continua = False
        k=k+1
    return continua

lista = []
cnt = 0
for k in range(2,1000):
    if(nprimi(k)==True):
        lista.append(k)
        cnt=cnt+1
print(cnt)
print(lista)
"""

#list comprehension
"""
primi = [k for k in range(2,1003) if nprimi(k)]
print(primi)

dispari = [k for k in range(1000) if k % 2 !=0]
print(dispari)

nomi = ["marco","luca", "nico","silvio","niaro"]
nomi_n = [nome for nome in nomi if nome[0]=='n']
print(nomi_n)
"""





