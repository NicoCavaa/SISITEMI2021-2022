
import math
"""

#rubrica
rubrica = {"Nico":"3662007888","Sara":"3469834445","Ugo":"340929587333"}
print(rubrica["Nico"]);


#***dopo la prima lettera
nome = input("Nome: ")
for x in nome:
    if x==nome[:1]:
        print(x,end="")
    else:
        print("*",end="")

#distanza con tuple
x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))

tuplax = (x1,x2)
tuplay = (y1,y2)

distanza = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
print(distanza)

#concatenare una Stringa N volte
numero = int(input("numero: "))
frase = input("frase: ")
print(frase*numero)
"""

