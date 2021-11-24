import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

print(f"Dado 1 :{dado1}")
print(f"Dado 2 :{dado2}")

if(dado1>dado2):
    print("Dado 1 vince")
elif(dado1<dado2):
    print("Dado 2 vince")
else:
    print("Pareggio")
